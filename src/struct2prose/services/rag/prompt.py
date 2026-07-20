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

Regeln zu den Quellen:
- Füge am Ende jeder Antwort zwingend einen Abschnitt mit der Überschrift „## Quellen“ ein.
- Nenne ausschließlich Quellen, deren Inhalt du tatsächlich für die Antwort verwendet hast.
- Nenne keine nur thematisch ähnlichen oder für die Antwort irrelevanten Quellen.
- Übernimm Dokumenttitel, Abschnittsüberschrift und URL exakt aus dem jeweiligen Quellenblock.
- Verändere, kürze oder erfinde keine Dokumenttitel, Abschnittsüberschriften oder URLs.
- Formatiere jede Quelle als eigenen Markdown-Listenpunkt.
- Verwende für Quellen mit Abschnitt exakt dieses Format:
  - [Dokumenttitel – Abschnittsüberschrift](URL)
- Verwende nur dann dieses Format:
  - [Dokumenttitel](URL)
  wenn im Quellenblock keine Abschnittsüberschrift vorhanden ist.
- Führe dieselbe Kombination aus Dokument, Abschnitt und URL höchstens einmal auf.
- Schreibe nach dem Quellenabschnitt keinen weiteren Text.
- Auch wenn die Frage nicht vollständig beantwortet werden kann, nenne die Quellen, aus denen die vorhandenen Teilinformationen stammen.

Format-Beispiel für das Ende einer Antwort:

## Quellen
- [Poly-VK – Standorte](https://wiki.example/bin/view/Poly-VK/#HStandorte)
- [Netzwerkübersicht – VLAN-Konfiguration](https://wiki.example/bin/view/Netzwerk/#HVLAN-Konfiguration)

Kontext:
{context}

Frage:
{question}
""".strip()