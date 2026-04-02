import json
import os
import time
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Any

from groq import Groq

from struct2prose.config import Config
from struct2prose.models.documents import (
    ContextualizationResult,
    ContextualizationTask,
    ContextualizedBlock,
    ContextualizedDocument,
    FailedBlock,
    SkippedBlock,
)
from struct2prose.parser.models import (
    ContentBlock,
    Section,
    WikiDocument,
)
from struct2prose.services.llm_client import generate_text

MODEL_DEFAULT = Config.get_model_name()


def _table_to_csv(rows: list[list[str]]) -> str:
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


def _prompt_for_table(doc_title: str, section_heading: str, table_rows: list[list[str]]) -> str:
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


def _prompt_for_list(doc_title: str, section_heading: str, items: list[str]) -> str:
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


def _is_contextualizable(block: ContentBlock) -> bool:
    return block.block_type in {"table", "list"}


def _strategy_for_block(block: ContentBlock) -> str:
    if block.block_type == "table":
        return "table_to_prose"
    if block.block_type == "list":
        return "list_to_prose"
    return "passthrough"


def _prompt_for_block(doc: WikiDocument, section: Section, block: ContentBlock) -> str:
    if block.block_type == "table":
        return _prompt_for_table(
            doc_title=doc.metadata.title,
            section_heading=section.heading,
            table_rows=block.content,
        )
    if block.block_type == "list":
        return _prompt_for_list(
            doc_title=doc.metadata.title,
            section_heading=section.heading,
            items=block.content,
        )
    raise ValueError(f"Unsupported contextualizable block type: {block.block_type}")


def _validate_contextualized_text(text: str | None) -> bool:
    if text is None:
        return False
    stripped = text.strip()
    if not stripped:
        return False
    if len(stripped) < 20:
        return False
    return True


def _make_task_id(doc: WikiDocument, section: Section, block: ContentBlock) -> str:
    return f"{doc.metadata.source_id}:{section.section_id}:{block.block_id}:contextualize"


def _make_contextualized_block_id(task: ContextualizationTask) -> str:
    return f"ctx-{task.source_block_id}"


def _create_task(
    doc: WikiDocument,
    section: Section,
    block: ContentBlock,
    model: str,
    prompt_name: str = "contextualization",
    prompt_version: str = "v1",
) -> ContextualizationTask:
    return ContextualizationTask(
        task_id=_make_task_id(doc, section, block),
        source_id=doc.metadata.source_id,
        pipeline_run_id=doc.metadata.pipeline_run_id,
        source_block_id=block.block_id,
        section_id=section.section_id,
        section_heading=section.heading,
        block_type=block.block_type,
        strategy=_strategy_for_block(block),
        prompt_name=prompt_name,
        prompt_version=prompt_version,
        model_name=model,
        created_at=datetime.utcnow(),
    )


def _execute_task(
    doc: WikiDocument,
    section: Section,
    block: ContentBlock,
    task: ContextualizationTask,
    model: str,
) -> ContextualizationResult:
    prompt = _prompt_for_block(doc, section, block)

    try:
        contextualized = generate_text(
            prompt=prompt,
            system_prompt="Du bist ein hilfreicher Assistent für technische Dokumentation.",
            model=model,
        )

        if not _validate_contextualized_text(contextualized):
            return ContextualizationResult(
                task_id=task.task_id,
                source_block_id=task.source_block_id,
                status="failed",
                contextualized_text=None,
                error_message="LLM-Antwort war leer oder nicht ausreichend verwertbar.",
                prompt_name=task.prompt_name,
                prompt_version=task.prompt_version,
                model_name=task.model_name,
                generated_at=datetime.utcnow(),
            )

        return ContextualizationResult(
            task_id=task.task_id,
            source_block_id=task.source_block_id,
            status="completed",
            contextualized_text=contextualized.strip(),
            error_message=None,
            prompt_name=task.prompt_name,
            prompt_version=task.prompt_version,
            model_name=task.model_name,
            generated_at=datetime.utcnow(),
        )

    except Exception as e:
        return ContextualizationResult(
            task_id=task.task_id,
            source_block_id=task.source_block_id,
            status="failed",
            contextualized_text=None,
            error_message=str(e),
            prompt_name=task.prompt_name,
            prompt_version=task.prompt_version,
            model_name=task.model_name,
            generated_at=datetime.utcnow(),
        )


def _markdown_for_passthrough_block(block: ContentBlock) -> str:
    content = block.content

    if block.block_type == "paragraph":
        text = str(content).strip()
        return text + "\n" if text else ""

    if block.block_type == "code":
        code = str(content).rstrip()
        if not code:
            return ""
        return "```\n" + code + "\n```\n"

    if content is None:
        return ""

    text = str(content).strip()
    return text + "\n" if text else ""


def _wiki_document_from_json(data: dict[str, Any], source_file: str) -> WikiDocument:
    """
    Adapter for current parser output JSON -> WikiDocument.
    Keeps step 4 compatible while step 3 is still being migrated.
    """
    from struct2prose.models.documents import DocumentMetadata

    metadata_dict = data.get("metadata")
    if metadata_dict:
        metadata = DocumentMetadata(
            source_id=metadata_dict["source_id"],
            title=metadata_dict["title"],
            xwiki_url=metadata_dict.get("xwiki_url"),
            xwiki_page_reference=metadata_dict.get("xwiki_page_reference"),
            source_hash=metadata_dict["source_hash"],
            retrieved_at=(
                datetime.fromisoformat(metadata_dict["retrieved_at"])
                if metadata_dict.get("retrieved_at")
                else None
            ),
            last_modified=metadata_dict.get("last_modified"),
            pipeline_run_id=metadata_dict.get("pipeline_run_id"),
            pipeline_version=metadata_dict.get("pipeline_version"),
        )
    else:
        metadata = DocumentMetadata(
            source_id=Path(source_file).stem,
            title=data.get("title", Path(source_file).stem),
            xwiki_url=None,
            xwiki_page_reference=None,
            source_hash="unknown",
            retrieved_at=None,
            last_modified=None,
            pipeline_run_id=None,
            pipeline_version=None,
        )

    sections: list[Section] = []

    for sec_index, sec in enumerate(data.get("sections", []), start=1):
        section_id = sec.get("section_id") or f"sec-{sec_index}"
        heading = sec.get("heading", "Abschnitt")

        blocks: list[ContentBlock] = []
        for block_index, block in enumerate(sec.get("blocks", []), start=1):
            block_id = block.get("block_id") or f"{section_id}-blk-{block_index}"
            blocks.append(
                ContentBlock(
                    block_id=block_id,
                    block_type=block.get("block_type", "unknown"),
                    content=block.get("content"),
                )
            )

        sections.append(
            Section(
                section_id=section_id,
                heading=heading,
                blocks=blocks,
            )
        )

    return WikiDocument(
        metadata=metadata,
        sections=sections,
    )


def _contextualize_document(doc: WikiDocument, model: str) -> tuple[ContextualizedDocument, str]:
    contextualized_doc = ContextualizedDocument(metadata=doc.metadata)

    md_lines: list[str] = [f"# {doc.metadata.title}\n"]

    for section in doc.sections:
        md_lines.append(f"## {section.heading}\n")

        for block in section.blocks:
            if not _is_contextualizable(block):
                passthrough_md = _markdown_for_passthrough_block(block)
                if passthrough_md:
                    md_lines.append(passthrough_md)

                contextualized_doc.skipped_blocks.append(
                    SkippedBlock(
                        source_block_id=block.block_id,
                        section_id=section.section_id,
                        section_heading=section.heading,
                        block_type=block.block_type,
                        reason="block_type_not_contextualized",
                    )
                )
                continue

            task = _create_task(doc=doc, section=section, block=block, model=model)
            result = _execute_task(
                doc=doc,
                section=section,
                block=block,
                task=task,
                model=model,
            )

            if result.status == "completed" and result.contextualized_text:
                contextualized_block = ContextualizedBlock(
                    block_id=_make_contextualized_block_id(task),
                    source_block_id=block.block_id,
                    section_id=section.section_id,
                    section_heading=section.heading,
                    block_type=block.block_type,
                    text=result.contextualized_text,
                    prompt_name=result.prompt_name,
                    prompt_version=result.prompt_version,
                    model_name=result.model_name,
                    created_at=result.generated_at,
                )
                contextualized_doc.contextualized_blocks.append(contextualized_block)
                md_lines.append(result.contextualized_text + "\n")
            else:
                contextualized_doc.failed_blocks.append(
                    FailedBlock(
                        source_block_id=block.block_id,
                        section_id=section.section_id,
                        section_heading=section.heading,
                        block_type=block.block_type,
                        error_message=result.error_message or "Unbekannter Fehler",
                    )
                )
                md_lines.append(
                    f"[LLM-Fehler bei {block.block_type}-Kontextualisierung: "
                    f"{result.error_message or 'Unbekannter Fehler'}]\n"
                )

            time.sleep(0.2)

    markdown = "\n".join(md_lines).strip() + "\n"
    return contextualized_doc, markdown


def run(processed_dir: Path, contextualized_dir: Path, model: str = MODEL_DEFAULT) -> None:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY ist nicht gesetzt (PyCharm Run Configuration -> Environment).")

    client = Groq(api_key=api_key)
    _ = client  # kept intentionally so the existing dependency/init remains in place

    contextualized_dir.mkdir(parents=True, exist_ok=True)

    for file in sorted(processed_dir.glob("*.json")):
        data: dict[str, Any] = json.loads(file.read_text(encoding="utf-8"))

        doc = _wiki_document_from_json(data=data, source_file=file.name)
        contextualized_doc, markdown = _contextualize_document(doc=doc, model=model)

        out_md_path = contextualized_dir / f"{file.stem}.md"
        out_md_path.write_text(markdown, encoding="utf-8")

        out_json_path = contextualized_dir / f"{file.stem}.contextualized.json"
        out_json_path.write_text(
            json.dumps(
                asdict(contextualized_doc),
                ensure_ascii=False,
                indent=2,
                default=str,
            ),
            encoding="utf-8",
        )

        print(f"[step4] wrote {out_md_path}")
        print(f"[step4] wrote {out_json_path}")