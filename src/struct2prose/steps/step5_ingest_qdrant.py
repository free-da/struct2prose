
from pathlib import Path
import json
import uuid
import os

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer

QDRANT_URL = os.getenv("QDRANT_URL", "http://10.200.200.33:6333")


def stable_chunk_id(source_id: str, block_id: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"{source_id}:{block_id}"))


def ensure_collection(
        client: QdrantClient,
        collection_name: str,
        vector_size: int
) -> None:
    collections = client.get_collections().collections
    names = [c.name for c in collections]
    print(f"Collection Name: {collection_name}")
    if collection_name not in names:
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )


def load_contextualized_documents(contextualized_dir: Path):
    for path in contextualized_dir.glob("*.contextualized.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        yield path, data

def split_text(
    text: str,
    *,
    max_chars: int = 1000,
    min_chars: int = 120,
) -> list[str]:
    text = text.strip()
    if not text:
        return []

    if len(text) <= max_chars:
        return [text] if len(text) >= min_chars else []

    # Absätze bevorzugen
    paragraphs = [p.strip() for p in text.splitlines() if p.strip()]

    chunks: list[str] = []
    current = ""

    for paragraph in paragraphs:
        # Sehr kurze Fragmente nicht allein als Chunk speichern
        if len(paragraph) < min_chars:
            if current:
                current = f"{current} {paragraph}".strip()
            else:
                current = paragraph
            continue

        if len(current) + len(paragraph) + 1 <= max_chars:
            current = f"{current} {paragraph}".strip()
        else:
            if len(current) >= min_chars:
                chunks.append(current.strip())
            current = paragraph

    if current and len(current) >= min_chars:
        chunks.append(current.strip())

    return chunks

def make_points(doc: dict, embedder: SentenceTransformer) -> list[PointStruct]:
    metadata = doc["metadata"]
    points = []


    for block in doc.get("rag_blocks", []):
        text = block["text"].strip()
        if not text:
            continue

        chunks = split_text(text)

        for i, chunk_text in enumerate(chunks):
            if len(chunk_text.strip()) < 120:
                continue

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
                    "chunk_index": i,
                    "chunk_total": len(chunks),
                    "chunk_text_length": len(chunk_text),
                },
            )

            points.append(point)

    return points


def run(
    contextualized_dir: Path,
    collection_name: str
) -> None:
    client = QdrantClient(url=QDRANT_URL)
    embedder = SentenceTransformer(os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"))
    vector_size = embedder.get_sentence_embedding_dimension()
    ensure_collection(client, collection_name, vector_size)

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
