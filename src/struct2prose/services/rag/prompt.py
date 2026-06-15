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

        source_url_line = f"URL: {source_url}\n" if source_url else ""

        parts.append(
            f"[Quelle {index}]\n"
            #f"Dokument: {title}\n"
            f"{source_url_line}"
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
Du beantwortest Fragen auf Basis einer Wissensbasis.

Regeln:
- Nutze ausschließlich den bereitgestellten Kontext.
- Der Kontext kann bereits semantisch transformierte Informationen enthalten.
- Tabellen, Listen oder strukturierte Inhalte wurden möglicherweise bereits in Fließtext umgewandelt.
- Betrachte alle Aussagen im Kontext als nutzbare Wissensrepräsentationen, auch wenn die ursprüngliche Tabellenstruktur nicht mehr sichtbar ist.
- Informationen können verteilt über mehrere Quellen oder Aussagen vorliegen.
- Kombiniere zusammengehörige Informationen aus mehreren Kontextstellen.
- Fasse relevante Informationen aus mehreren Quellen oder Aussagen zusammen, wenn dies zur Beantwortung der Frage erforderlich ist.
- Wenn die Antwort nicht ausreichend aus dem Kontext ableitbar ist, sage klar, welche Information fehlt.
- Erfinde keine Details.
- Antworte präzise und sachlich.
- Gib ausschließlich die Seiten, aus denen du Informationen zitierst als Quellen an.
- Verwende nur URLs, die im Kontext ausdrücklich als URL angegeben sind.
- Wenn du Quellen nennst, verwende klickbare Markdown-Links im Format [Dokumenttitel - Abschnitt](URL). 
- Nutze ausschließlich die im Kontext angegebene URL. Erfinde oder rekonstruiere keine Abschnittsanker.
- Wenn eine Quelle eine Abschnitts-URL enthält, verwende genau diese URL unverändert.
- Wenn keine Abschnitts-URL vorhanden ist, verwende die Dokument-URL.


Kontext:
{context}

Frage:
{question}
""".strip()