from struct2prose.services.rag.retriever import RetrievedChunk


def build_context(chunks: list[RetrievedChunk]) -> str:
    parts: list[str] = []

    for index, chunk in enumerate(chunks, start=1):
        title = chunk.payload.get("title", "Unbekanntes Dokument")
        section = chunk.payload.get("section_heading", "Unbekannter Abschnitt")
        section_anchor = chunk.payload.get("section_anchor")
        #block_type = chunk.payload.get("block_type", "unknown")
        #transformation = chunk.payload.get("transformation", "unknown")
        url = chunk.payload.get("xwiki_url")

        if url and section_anchor:
            source_url = f"{url}#{section_anchor}"
        else:
            source_url = url

        source_url_line = f"{source_url}\n" if source_url else ""

        parts.append(
            f"[Quelle {index}]\n"
            f"Dokument: {title}\n"
            f"URL: {source_url_line}"
            f"Abschnitt: {section}\n"
            f"Abschnittsanker: {section_anchor or 'Nicht vorhanden'}\n"
            #f"Blocktyp: {block_type}\n"
            #f"Transformation: {transformation}\n"
            #f"Score: {chunk.score:.4f}\n\n"
            f"{chunk.text}"
        )

    return "\n\n---\n\n".join(parts)


def build_rag_prompt(question: str, chunks: list[RetrievedChunk]) -> str:
    context = build_context(chunks)

    return f"""
Du beantwortest auf Deutsch Fragen auf Basis einer Wissensbasis.

Regeln:
- Nutze ausschließlich den bereitgestellten Kontext für die Antwortgenerierung.
- Betrachte alle Aussagen im Kontext als nutzbare Wissensrepräsentationen, auch wenn die ursprüngliche Tabellenstruktur nicht mehr sichtbar ist.
- Informationen können verteilt über mehrere Quellen oder Aussagen vorliegen.
- Kombiniere zusammengehörige Informationen aus mehreren Kontextstellen.
- Gib eine Übersicht aus allen im Kontext vorliegenden Informationen zum abgefragten Thema zurück.
- Wenn die Antwort nicht ausreichend aus dem Kontext ableitbar ist, sage klar, welche Information fehlt.
- Erfinde keine Details.
- Antworte präzise und sachlich.
- Wenn du Quellen aus dem Kontext verwendest, gib sie am Ende deiner Antwort an.
- Nenne Quellen als klickbare Markdown-Links im Format [Dokumenttitel - Abschnitt](URL) oder [Dokumenttitel](URL).



Kontext:
{context}

Frage:
{question}
""".strip()