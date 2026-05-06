from struct2prose.services.rag.retriever import RetrievedChunk


def build_context(chunks: list[RetrievedChunk]) -> str:
    parts: list[str] = []

    for index, chunk in enumerate(chunks, start=1):
        title = chunk.payload.get("title", "Unbekanntes Dokument")
        section = chunk.payload.get("section_heading", "Unbekannter Abschnitt")
        block_type = chunk.payload.get("block_type", "unknown")
        transformation = chunk.payload.get("transformation", "unknown")

        parts.append(
            f"[Quelle {index}]\n"
            f"Dokument: {title}\n"
            f"Abschnitt: {section}\n"
            f"Blocktyp: {block_type}\n"
            f"Transformation: {transformation}\n"
            f"Score: {chunk.score:.4f}\n\n"
            f"{chunk.text}"
        )

    return "\n\n---\n\n".join(parts)


def build_rag_prompt(question: str, chunks: list[RetrievedChunk]) -> str:
    context = build_context(chunks)

    return f"""
Du beantwortest Fragen auf Basis einer technischen Wissensbasis.

Regeln:
- Nutze ausschließlich den bereitgestellten Kontext.
- Wenn die Antwort nicht im Kontext enthalten ist, sage klar, dass die Wissensbasis dazu keine ausreichende Information enthält.
- Erfinde keine Details.
- Antworte präzise und sachlich.
- Wenn möglich, nenne das relevante Dokument oder den Abschnitt.

Kontext:
{context}

Frage:
{question}
""".strip()