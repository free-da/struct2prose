import os
from dataclasses import dataclass
from typing import Any

from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

COLLECTION_NAME = os.getenv("COLLECTION_NAME", "struct2prose")
QDRANT_URL = os.getenv("QDRANT_URL")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")


@dataclass
class RetrievedChunk:
    text: str
    score: float
    payload: dict[str, Any]


class RagRetriever:
    def __init__(self) -> None:
        self.client = QdrantClient(url=QDRANT_URL)
        self.embedder = EMBEDDING_MODEL

    def search(self, query: str, top_k: int = 5) -> list[RetrievedChunk]:
        query_vector = self.embedder.encode(query).tolist()

        hits = self.client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=top_k,
        )

        results: list[RetrievedChunk] = []

        for hit in hits:
            payload = hit.payload or {}
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