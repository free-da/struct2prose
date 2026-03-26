import json
import os
import time
from pathlib import Path
from typing import Any, List

from groq import Groq

from struct2prose.config import Config
from struct2prose.services.llm_client import generate_text

MODEL_DEFAULT = Config.get_model_name()

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
1) Gib den Titel der Tabelle an, wenn es einen gibt. Nutze dafür entweder die Über- oder Unterschrift der Tabelle. Wenn es keinen Titel gibt, gib der Tabelle eine inhaltlich passende Bezeichnung.
2) Beschreibe kurz, was diese Tabelle insgesamt darstellt (1-2 Sätze).
3) Erkläre die Bedeutung jeder Spalte (stichpunktartig oder kurze Sätze).
4) Formuliere jede Tabellenzeile als beschreibenden Satz (pro Zeile ein Satz).
   - Wenn eine Zeile eine Art "Fortsetzung" ist (z.B. erste Spalte leer), beziehe dich auf die letzte nicht-leere Kategorie/Instanz aus der ersten Spalte.
5) Gib KEINEN CSV/Tabellen-Output zurück, sondern gut lesbaren Fließtext.
6) Erfinde keine Inhalte oder Angaben darüber, was in der Tabelle enthalten sein könnte. Wenn eine Tabelle oder einzelne Felder leer sind, dann gib das einfach so wieder.

Format:
- Wenn möglich Überschriften auf Markdown-Ebene auf sinnvoller Strukturebene.
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



def run(processed_dir: Path, contextualized_dir: Path, model: str = MODEL_DEFAULT) -> None:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY ist nicht gesetzt (PyCharm Run Configuration -> Environment).")

    client = Groq(api_key=api_key)

    contextualized_dir.mkdir(parents=True, exist_ok=True)

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
                    # MVP: contextualize tables via LLM
                    prompt = _prompt_for_table(title, heading, content)
                    try:
                       # contextualized = _call_groq(client, prompt, model=model)
                        contextualized = generate_text(
                            prompt=prompt,
                            system_prompt="Du bist ein hilfreicher Assistent für technische Dokumentation.",
                            model=model,
                        )
                    except Exception as e:
                        contextualized = f"[LLM-Fehler bei Tabellen-Kontextualisierung: {e}]"
                    md_lines.append(contextualized + "\n")
                    time.sleep(0.2)  # tiny pacing; keeps things calmer in practice

                elif btype == "list":
                    # optional: also contextualize lists via LLM
                    prompt = _prompt_for_list(title, heading, content)
                    try:
                       # contextualized = _call_groq(client, prompt, model=model)
                       contextualized = generate_text(
                            prompt=prompt,
                            system_prompt="Du bist ein hilfreicher Assistent für technische Dokumentation.",
                            model=model,
                        )

                    except Exception as e:
                        contextualized = f"[LLM-Fehler bei Listen-Kontextualisierung: {e}]"
                    md_lines.append(contextualized + "\n")
                    time.sleep(0.2)

                else:
                    # Unknown block type: keep as plain text
                    if content:
                        md_lines.append(str(content).strip() + "\n")

        out_path = contextualized_dir / f"{file.stem}.md"
        out_path.write_text("\n".join(md_lines).strip() + "\n", encoding="utf-8")
        print(f"[step4] wrote {out_path}")
