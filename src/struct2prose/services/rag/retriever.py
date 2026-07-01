import os
from dataclasses import dataclass
from typing import Any

from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

QDRANT_URL = os.getenv("QDRANT_URL", "http://10.200.200.33:6333")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL","sentence-transformers/all-MiniLM-L6-v2")


@dataclass
class RetrievedChunk:
    text: str
    score: float
    payload: dict[str, Any]


class RagRetriever:
    def __init__(self) -> None:
        self.client = QdrantClient(url=QDRANT_URL)
        self.embedder = SentenceTransformer(EMBEDDING_MODEL)

    def search(
            self,
            query: str,
            *,
            collection_name: str,
            top_k: int = 5,
    ) -> list[RetrievedChunk]:
        query_vector = self.embedder.encode(query).tolist()

        hits = self.client.query_points(
            collection_name=collection_name,
            query=query_vector,
            limit=top_k,
        ).points

        results: list[RetrievedChunk] = []

        for hit in hits:
            payload = hit.payload or {}

            print(
                f"score={hit.score:.4f} "
                f"section={hit.payload.get('section_heading')} "
                f"block={hit.payload.get('source_block_id')}"
            )
            print(
                f"score={hit.score:.4f} "
                f"section={payload.get('section_heading')} "
                f"block={payload.get('source_block_id')} "
                f"chunk={payload.get('chunk_index')}/{payload.get('chunk_total')}"
            )
            print(payload.get("text", "")[:500])
            print("-" * 80)

            text = str(payload.get("text", "")).strip()

            if not text:
                continue

            results.append(
                RetrievedChunk(
                    text=text,
                    score=float(hit.score),
                    payload=payload,
                )
            )

        return results