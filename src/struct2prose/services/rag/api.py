import time
import uuid

from fastapi import FastAPI, HTTPException

from struct2prose.config import Config
from struct2prose.services.rag.prompt import build_rag_prompt
from struct2prose.services.rag.retriever import RagRetriever
from struct2prose.services.rag.schemas import ChatCompletionRequest, SearchRequest
from struct2prose.services.llm_client import generate_text, LLMResponseTruncatedError

MODEL_COLLECTIONS = {
    "struct2prose-rag": Config.QDRANT_CONTEXTUALIZED_COLLECTION,
    "baseline-rag": Config.QDRANT_BASELINE_COLLECTION,
}
app = FastAPI(title="struct2prose RAG Service")

retriever = RagRetriever()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/v1/models")
def list_models() -> dict:
    return {
        "object": "list",
        "data": [
            {
                "id": model_id,
                "object": "model",
                "created": 0,
                "owned_by": "struct2prose",
            }
            for model_id in MODEL_COLLECTIONS
        ]
    }

@app.post("/search")
def search(request: SearchRequest) -> dict:
    collection_name = MODEL_COLLECTIONS.get(request.model)
    chunks = retriever.search(
        request.query,
        collection_name=collection_name,
        top_k=request.top_k,
    )

    return {
        "query": request.query,
        "results": [
            {
                "score": chunk.score,
                "text": chunk.text,
                "payload": chunk.payload,
            }
            for chunk in chunks
        ],
    }


def _last_user_message(messages) -> str:
    for message in reversed(messages):
        if message.role == "user":
            return message.content.strip()

    raise HTTPException(status_code=400, detail="No user message found.")

def _format_sources(chunks) -> str:
    seen = set()
    lines = []

    for chunk in chunks:
        title = chunk.payload.get("title", "Unbekanntes Dokument")
        url = chunk.payload.get("xwiki_url")
        section = chunk.payload.get("section_heading")

        if not url or url in seen:
            continue

        seen.add(url)

        label = title
        if section:
            label += f" – {section}"

        lines.append(f"- [{label}]({url})")

    if not lines:
        return ""

    return "\n\n## Quellen\n" + "\n".join(lines)

@app.post("/v1/chat/completions")
def chat_completions(request: ChatCompletionRequest) -> dict:
    # if request.stream:
    #     raise HTTPException(
    #         status_code=400,
    #         detail="Streaming is not supported yet.",
    #     )
    # Streaming wird aktuell ignoriert.
    # Die Antwort wird non-streaming zurückgegeben.

    question = _last_user_message(request.messages)
    print(f"[RAG] question={question!r}")
    collection_name = MODEL_COLLECTIONS.get(request.model)

    if collection_name is None:
        raise HTTPException(
            status_code=404,
            detail=f"Unknown model: {request.model}",
        )

    chunks = retriever.search(
        question,
        collection_name=collection_name,
        top_k=5,
    )
    prompt = build_rag_prompt(question, chunks)

    try:
        answer = generate_text(
            prompt=prompt,
            system_prompt=(
                "Du bist ein RAG-Assistent für technische Dokumentation. "
                "Antworte nur auf Basis des bereitgestellten Kontextes."
            ),
        )
    except LLMResponseTruncatedError:
        answer = (
            "Die Antwort konnte nicht vollständig erzeugt werden, weil das verwendete "
            "Sprachmodell seine maximale Ausgabelänge erreicht hat. "
            "Die Frage erfordert vermutlich eine umfangreiche Auflistung oder Aggregation "
            "mehrerer Wissenseinheiten. Bitte stelle die Frage enger, z. B. nach einem "
            "bestimmten Standort, Abschnitt oder System."
        )

    now = int(time.time())

    return {
        "id": f"chatcmpl-{uuid.uuid4()}",
        "object": "chat.completion",
        "created": now,
        "model": request.model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": answer,
                },
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
        },
    }