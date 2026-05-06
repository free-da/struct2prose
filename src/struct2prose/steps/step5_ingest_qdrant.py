# .contextualized.json laden
# → ContextualizedBlock lesen
# → Text chunkweise vorbereiten
# → Embedding erzeugen
# → Qdrant upsert

from pathlib import Path
import json
import uuid
import os

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer


COLLECTION_NAME = os.getenv("QDRANT_COLLECTION", "struct2prose_knowledge")
VECTOR_SIZE = 384  # all-MiniLM-L6-v2
QDRANT_URL = os.getenv("QDRANT_URL", "http://10.200.200.33:6333")


def stable_chunk_id(source_id: str, block_id: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"{source_id}:{block_id}"))


def ensure_collection(client: QdrantClient) -> None:
    collections = client.get_collections().collections
    names = [c.name for c in collections]

    if COLLECTION_NAME not in names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE,
            ),
        )


def load_contextualized_documents(contextualized_dir: Path):
    for path in contextualized_dir.glob("*.contextualized.json"):
        data = json.loads(path.read_text(encoding="utf-8"))
        yield path, data

def split_text(text: str, max_chars: int = 800) -> list[str]:
    chunks = []
    current = ""

    for sentence in text.split(". "):
        if len(current) + len(sentence) < max_chars:
            current += sentence + ". "
        else:
            chunks.append(current.strip())
            current = sentence + ". "

    if current:
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
) -> None:
    client = QdrantClient(url=QDRANT_URL)
    embedder = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

    ensure_collection(client)

    for path, doc in load_contextualized_documents(contextualized_dir):
        points = make_points(doc, embedder)

        if not points:
            print(f"[step5] no points for {path}")
            continue

        client.upsert(
            collection_name=COLLECTION_NAME,
            points=points,
        )

        print(f"[step5] upserted {len(points)} points from {path}")
