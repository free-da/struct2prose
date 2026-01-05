import json
import os
import time
from pathlib import Path
from typing import Any, List

from groq import Groq


MODEL_DEFAULT = "llama-3.3-70b-versatile"


def _table_to_csv(rows: List[List[str]]) -> str:
    """Very small CSV renderer (good enough for LLM input)."""
    def esc(cell: str) -> str:
        cell = "" if cell is None else str(cell)
        needs_quotes = any(ch in cell for ch in [",", "\n", '"'])
        cell = cell.replace('"', '""')
        return f'"{cell}"' if needs_quotes else cell

    lines = []
    for row in rows:
        lines.append(",".join(esc(c) for c in row))
    return "\n".join(lines)


def _prompt_for_table(doc_title: str, section_heading: str, table_rows: List[List[str]]) -> str:
    table_csv = _table_to_csv(table_rows)

    return f"""
Du erhältst eine Tabelle aus einer technischen Wiki-Seite.

Dokumenttitel: {doc_title}
Abschnitt: {section_heading}

Tabelleninhalt (CSV):
{table_csv}

Aufgabe:
1) Beschreibe kurz, was diese Tabelle insgesamt darstellt (1-2 Sätze).
2) Erkläre die Bedeutung jeder Spalte (stichpunktartig oder kurze Sätze).
3) Formuliere jede Tabellenzeile als beschreibenden Satz (pro Zeile ein Satz).
   - Wenn eine Zeile eine Art "Fortsetzung" ist (z.B. erste Spalte leer), beziehe dich auf die letzte nicht-leere Kategorie/Instanz aus der ersten Spalte.
4) Gib KEINEN CSV/Tabellen-Output zurück, sondern gut lesbaren Fließtext.

Format:
- Keine Überschriften auf Markdown-Ebene (die kommen außerhalb).
- Nutze, wenn sinnvoll, kurze Absätze und Aufzählungen.
""".strip()


def _prompt_for_list(doc_title: str, section_heading: str, items: List[str]) -> str:
    bullets = "\n".join(f"- {it}" for it in items)
    return f"""
Du erhältst eine Liste aus einer technischen Wiki-Seite.

Dokumenttitel: {doc_title}
Abschnitt: {section_heading}

Liste:
{bullets}

Aufgabe:
- Formuliere die Liste als gut lesbaren Fließtext.
- Wenn es sich um Schritte handelt, gib eine klare Schrittfolge aus (nummeriert).
- Ansonsten erkläre kurz, was die Liste zusammenfasst, und fasse die Punkte verständlich zusammen.
""".strip()


def _call_groq(client: Groq, prompt: str, model: str) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Du bist ein hilfreicher Assistent für technische Dokumentation."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()


def run(processed_dir: Path, normalized_dir: Path, model: str = MODEL_DEFAULT) -> None:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY ist nicht gesetzt (PyCharm Run Configuration -> Environment).")

    client = Groq(api_key=api_key)

    normalized_dir.mkdir(parents=True, exist_ok=True)

    for file in sorted(processed_dir.glob("*.json")):
        data: dict[str, Any] = json.loads(file.read_text(encoding="utf-8"))
        title: str = data.get("title", file.stem)
        sections: list[dict[str, Any]] = data.get("sections", [])

        md_lines: list[str] = []
        md_lines.append(f"# {title}\n")

        for sec in sections:
            heading = sec.get("heading", "Abschnitt")
            blocks = sec.get("blocks", [])

            md_lines.append(f"## {heading}\n")

            for block in blocks:
                btype = block.get("block_type")
                content = block.get("content")

                if btype == "paragraph":
                    text = str(content).strip()
                    if text:
                        md_lines.append(text + "\n")

                elif btype == "code":
                    code = str(content).rstrip()
                    if code:
                        md_lines.append("```")
                        md_lines.append(code)
                        md_lines.append("```\n")

                elif btype == "table":
                    # MVP: normalize tables via LLM
                    prompt = _prompt_for_table(title, heading, content)
                    try:
                        normalized = _call_groq(client, prompt, model=model)
                    except Exception as e:
                        normalized = f"[LLM-Fehler bei Tabellen-Normalisierung: {e}]"
                    md_lines.append(normalized + "\n")
                    time.sleep(0.2)  # tiny pacing; keeps things calmer in practice

                elif btype == "list":
                    # optional: also normalize lists via LLM
                    prompt = _prompt_for_list(title, heading, content)
                    try:
                        normalized = _call_groq(client, prompt, model=model)
                    except Exception as e:
                        normalized = f"[LLM-Fehler bei Listen-Normalisierung: {e}]"
                    md_lines.append(normalized + "\n")
                    time.sleep(0.2)

                else:
                    # Unknown block type: keep as plain text
                    if content:
                        md_lines.append(str(content).strip() + "\n")

        out_path = normalized_dir / f"{file.stem}.md"
        out_path.write_text("\n".join(md_lines).strip() + "\n", encoding="utf-8")
        print(f"[step4] wrote {out_path}")
