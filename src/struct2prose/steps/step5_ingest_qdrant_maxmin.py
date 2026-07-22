from pathlib import Path
import json
import uuid
import os
import re

import numpy as np
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer


VECTOR_SIZE = int(os.getenv("VECTOR_SIZE", "384"))  # all-MiniLM-L6-v2 default
QDRANT_URL = os.getenv("QDRANT_URL", "http://10.200.200.33:6333")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

# Hybrid strategy: keep short RagBlocks intact; only split long ones semantically.
MAX_CHUNK_CHARS = int(os.getenv("MAX_CHUNK_CHARS", "800"))
CHUNKING_STRATEGY = os.getenv("CHUNKING_STRATEGY", "maxmin")  # maxmin | sentence
MAXMIN_FIXED_THRESHOLD = float(os.getenv("MAXMIN_FIXED_THRESHOLD", "0.6"))
MAXMIN_C = float(os.getenv("MAXMIN_C", "0.9"))
MAXMIN_INIT_CONSTANT = float(os.getenv("MAXMIN_INIT_CONSTANT", "1.5"))


def stable_chunk_id(source_id: str, block_id: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"{source_id}:{block_id}"))


def ensure_collection(client: QdrantClient, collection_name: str) -> None:
    collections = client.get_collections().collections
    names = [c.name for c in collections]
    print(f"Collection Name: {collection_name}")
    if collection_name not in names:
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )


def load_contextualized_documents(contextualized_dir: Path):
    for path in contextualized_dir.glob("*.contextualized.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        yield path, data


def _split_sentences(text: str) -> list[str]:
    """Simple sentence splitter without extra dependencies.

    Good enough for generated German prose. It intentionally avoids splitting on every
    period inside IDs/IPs as far as possible, but this is still a pragmatic splitter.
    """
    cleaned = re.sub(r"\s+", " ", text.strip())
    if not cleaned:
        return []

    # Split after sentence punctuation followed by whitespace and an uppercase letter,
    # digit, or opening bracket. This avoids many abbreviation/IP edge cases.
    parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ0-9\[])", cleaned)
    return [part.strip() for part in parts if part.strip()]


def _cosine_similarity(vector: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    vector_norm = np.linalg.norm(vector)
    matrix_norms = np.linalg.norm(matrix, axis=1)
    denominator = matrix_norms * vector_norm
    denominator[denominator == 0] = 1e-12
    return (matrix @ vector) / denominator


def _sigmoid(x: float) -> float:
    return 1 / (1 + np.exp(-x))


def _fallback_sentence_chunk(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    """Previous pragmatic sentence-based splitter, slightly safer than .split('. ')."""
    sentences = _split_sentences(text)
    if not sentences:
        return []

    chunks: list[str] = []
    current = ""

    for sentence in sentences:
        if not current:
            current = sentence
            continue

        candidate = f"{current} {sentence}"
        if len(candidate) <= max_chars:
            current = candidate
        else:
            chunks.append(current.strip())
            current = sentence

    if current.strip():
        chunks.append(current.strip())

    return chunks


def maxmin_chunk_text(
    text: str,
    embedder: SentenceTransformer,
    *,
    max_chars: int = MAX_CHUNK_CHARS,
    fixed_threshold: float = MAXMIN_FIXED_THRESHOLD,
    c: float = MAXMIN_C,
    init_constant: float = MAXMIN_INIT_CONSTANT,
) -> list[str]:
    """Hybrid Max-Min semantic chunking for one RagBlock.

    - RagBlocks <= max_chars are preserved unchanged.
    - Longer RagBlocks are split into sentences.
    - Sentences are greedily grouped by semantic similarity.
    - max_chars remains a hard upper bound where possible, so chunks stay manageable.

    This is an implementation of the Max-Min idea adapted to struct2prose's RagBlock
    level instead of complete-document chunking.
    """
    text = text.strip()
    if not text:
        return []

    if len(text) <= max_chars:
        return [text]

    sentences = _split_sentences(text)
    if len(sentences) <= 1:
        return _fallback_sentence_chunk(text, max_chars=max_chars)

    embeddings = embedder.encode(
        sentences,
        convert_to_numpy=True,
        show_progress_bar=False,
    )

    chunks: list[list[str]] = []
    current: list[str] = [sentences[0]]
    cluster_start = 0
    cluster_end = 1
    pairwise_min = -float("inf")

    for i in range(1, len(sentences)):
        sentence = sentences[i]
        candidate_text = " ".join(current + [sentence])

        # Keep the size constraint explicit. This makes the method usable for your
        # local RAG context limit and keeps the 800-character rule explainable.
        if len(candidate_text) > max_chars and current:
            chunks.append(current)
            current = [sentence]
            cluster_start = i
            cluster_end = i + 1
            pairwise_min = -float("inf")
            continue

        cluster_embeddings = embeddings[cluster_start:cluster_end]

        if cluster_end - cluster_start > 1:
            similarities = _cosine_similarity(embeddings[i], cluster_embeddings)
            adjusted_threshold = pairwise_min * c * _sigmoid((cluster_end - cluster_start) - 1)
            new_sentence_similarity = float(np.max(similarities))
            pairwise_min = min(float(np.min(similarities)), pairwise_min)
        else:
            adjusted_threshold = 0.0
            similarities = _cosine_similarity(embeddings[i], cluster_embeddings)
            pairwise_min = float(similarities[0])
            new_sentence_similarity = init_constant * pairwise_min

        if new_sentence_similarity > max(adjusted_threshold, fixed_threshold):
            current.append(sentence)
            cluster_end += 1
        else:
            chunks.append(current)
            current = [sentence]
            cluster_start = i
            cluster_end = i + 1
            pairwise_min = -float("inf")

    if current:
        chunks.append(current)

    return [" ".join(chunk).strip() for chunk in chunks if " ".join(chunk).strip()]


def split_text(
    text: str,
    *,
    embedder: SentenceTransformer | None = None,
    max_chars: int = MAX_CHUNK_CHARS,
) -> list[str]:
    """Central chunking function used by ingest.

    Set CHUNKING_STRATEGY=sentence to use the old sentence-length strategy.
    Default CHUNKING_STRATEGY=maxmin keeps short RagBlocks unchanged and applies
    Max-Min semantic chunking only when len(text) > max_chars.
    """
    if CHUNKING_STRATEGY == "sentence" or embedder is None:
        return _fallback_sentence_chunk(text, max_chars=max_chars)

    if CHUNKING_STRATEGY == "maxmin":
        return maxmin_chunk_text(text, embedder, max_chars=max_chars)

    raise ValueError(f"Unknown CHUNKING_STRATEGY: {CHUNKING_STRATEGY}")


def make_points(doc: dict, embedder: SentenceTransformer) -> list[PointStruct]:
    metadata = doc["metadata"]
    points = []

    for block in doc.get("rag_blocks", []):
        text = block["text"].strip()
        if not text:
            continue

        chunks = split_text(text, embedder=embedder)
        section_anchor = block.get("section_anchor")
        xwiki_url = metadata.get("xwiki_url")

        section_url = (
            f"{xwiki_url}#{section_anchor}"
            if xwiki_url and section_anchor
            else xwiki_url
        )
        for i, chunk_text in enumerate(chunks):
            vector = embedder.encode(
                sentences=chunk_text,
                convert_to_numpy=True,
                show_progress_bar=False,
            ).tolist()

            point = PointStruct(
                id=stable_chunk_id(
                    metadata["source_id"],
                    f"{block['block_id']}:{i}",
                ),
                vector=vector,
                payload={
                    "text": chunk_text,
                    "source_id": metadata["source_id"],
                    "title": metadata["title"],
                    "xwiki_url": metadata.get("xwiki_url"),
                    "section_anchor": section_anchor,
                    "section_url": section_url,
                    "xwiki_page_reference": metadata.get("xwiki_page_reference"),
                    "source_hash": metadata.get("source_hash"),
                    "pipeline_run_id": metadata.get("pipeline_run_id"),
                    "pipeline_version": metadata.get("pipeline_version"),
                    "section_id": block.get("section_id"),
                    "section_heading": block.get("section_heading"),
                    "block_type": block.get("block_type"),
                    "source_block_id": block.get("source_block_id"),
                    "prompt_name": block.get("prompt_name"),
                    "prompt_version": block.get("prompt_version"),
                    "model_name": block.get("model_name"),
                    "created_at": block.get("created_at"),
                    "transformation": block.get("transformation"),
                    "chunking_strategy": CHUNKING_STRATEGY,
                    "chunk_max_chars": MAX_CHUNK_CHARS,
                    "chunk_index": i,
                    "chunk_total": len(chunks),
                    "chunk_text_length": len(chunk_text),
                },
            )

            points.append(point)

    return points


def run(
    contextualized_dir: Path,
    collection_name: str,
) -> None:
    client = QdrantClient(url=QDRANT_URL)
    embedder = SentenceTransformer(EMBEDDING_MODEL)

    ensure_collection(client, collection_name)

    for path, doc in load_contextualized_documents(contextualized_dir):
        points = make_points(doc, embedder)

        if not points:
            print(f"[step5] no points for {path}")
            continue

        client.upsert(
            collection_name=collection_name,
            points=points,
        )

        print(f"[step5] upserted {len(points)} points from {path}")
