import json
import time
import re
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Any

from struct2prose.config import Config
from struct2prose.models.documents import (
    ContextualizationResult,
    ContextualizationTask,
    ContextualizedBlock,
    ContextualizedDocument,
    FailedBlock,
    SkippedBlock,
    RagBlock
)
from struct2prose.parser.models import (
    ContentBlock,
    Section,
    WikiDocument,
)
from struct2prose.persistence.db import connect
from struct2prose.persistence.store import (
    create_contextualization_task,
    create_document_version,
    create_step_run,
    finish_contextualization_task,
    finish_step_run,
)
from struct2prose.services.llm_client import generate_text

MODEL_DEFAULT = Config.get_model_name()
STEP_NAME = "contextualize"


def _make_step_run_id(run_id: str, source_id: str) -> str:
    safe_source_id = source_id.replace(":", "_")
    return f"{run_id}:{STEP_NAME}:{safe_source_id}"


def _make_input_version_id(run_id: str, source_id: str) -> str:
    safe_source_id = source_id.replace(":", "_")
    return f"{run_id}:processed_data:{safe_source_id}"


def _make_output_version_id(run_id: str, source_id: str) -> str:
    safe_source_id = source_id.replace(":", "_")
    return f"{run_id}:contextualized_data:{safe_source_id}"


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


def _prompt_for_table(
    doc_title: str,
    section_heading: str,
    table_rows: list[list[str]],
) -> str:
    table_csv = _table_to_csv(table_rows)

    return f"""
Du erhältst eine Tabelle aus einer technischen Wiki-Seite.

Dokumenttitel: {doc_title}
Abschnitt: {section_heading}

Tabelleninhalt (CSV):
{table_csv}

Aufgabe:

- Verwende ausschließlich Informationen aus der Tabelle sowie bereitgestellte Dokumenttitel und Abschnittsüberschriften.
- Erfinde keine Informationen, die nicht aus diesen Quellen hervorgehen.
- Formuliere vollständige, grammatikalisch korrekte Sätze.
- Verwende Spaltenüberschriften und bereitgestellten Kontext zur Beschreibung der jeweiligen Werte und ihrer Beziehungen.
- Wenn die Tabelle eine Schlüssel-Wert-Struktur besitzt, beschreibe die Eigenschaften als Merkmale derselben Entität statt als unabhängige Entitäten.
- Wenn kein Tabellenkopf vorhanden ist, behandle den Wert der ersten Spalte als primäre Entität der Zeile.
- Leere Zellen übernehmen den zuletzt gültigen Wert derselben Spalte aus den vorherigen Zeilen.
- Besteht eine Zeile nur aus einer einzelnen befüllten Zelle, interpretiere sie als tabelleninterne Abschnittsüberschrift. Die Überschrift gilt für alle folgenden Zeilen bis zur nächsten Abschnittsüberschrift oder bis zum Ende der Tabelle.
- Tabelleninterne Abschnittsüberschriften gelten nur als Kontext und nicht als Zellwert.
- Wenn eine Zelle mit mehreren, mit Komma getrennten, Werten besteht, verkette sie wie in einer normalen Aufzählung miteinander.
- Gib für jede Datenzeile genau einen Satz zurück. Gib keine Einleitung, Zusammenfassung, Aufzählungen oder Erklärungen aus.
- Jede Tabellenzeile mit Daten muss verarbeitet und zurückgegeben werden. Kein Wert darf ausgelassen werden. 

Beispiel Eingabe:
Dokumenttitel: Poly-VK
Abschnitt: Standorte

Standort | Konfiguration
A.1.1 | Standard

Beispiel Ausgabe:
Die Poly-VK verwendet am Standort A.1.1 die Konfiguration Standard.
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
- Erfinde keine Erklärungen zu Begriffen.
- Nutze ausschließlich die Listeneinträge.
- Wenn die Liste nur aus Einzelnachweisen, Links oder Begriffen besteht, fasse sie neutral als Verweisliste zusammen.
""".strip()


def _is_contextualizable(block: ContentBlock, section: Section | None = None) -> bool:
    if section and section.heading.strip().lower() in {"einzelnachweise", "referenzen", "quellen"}:
        return False

    return block.block_type in {"table", "list"}

def _looks_language_corrupted(text: str) -> bool:
    cjk_chars = re.findall(r"[\u4e00-\u9fff]", text)
    return len(cjk_chars) > 20

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

    if _looks_language_corrupted(stripped):
        return False

    return True

def _make_contextualized_block_id(task: ContextualizationTask) -> str:
    return f"ctx-{task.source_block_id}"


def _create_task(
    doc: WikiDocument,
    section: Section,
    block: ContentBlock,
    model: str,
    *,
    step_run_id: str | None = None,
    prompt_name: str = "contextualization",
    prompt_version: str = "v1",
) -> ContextualizationTask:
    if step_run_id is not None:
        safe_step_run_id = step_run_id.replace(":", "_")
        task_id = f"{safe_step_run_id}:{block.block_id}"
    else:
        # Fallback (z. B. bei Einzelaufruf ohne run_id)
        task_id = f"{doc.metadata.source_id}:{section.section_id}:{block.block_id}:contextualize"
    return ContextualizationTask(
        task_id=task_id,
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
                anchor=sec.get("anchor"),
                blocks=blocks,
            )
        )

    return WikiDocument(
        metadata=metadata,
        sections=sections,
    )


def _contextualize_document(
    doc: WikiDocument,
    model: str,
    *,
    step_run_id: str | None = None,
    db_path: Path | None = None,
) -> tuple[ContextualizedDocument, str]:
    contextualized_doc = ContextualizedDocument(metadata=doc.metadata)

    md_lines: list[str] = [f"# {doc.metadata.title}\n"]

    for section in doc.sections:
        md_lines.append(f"## {section.heading}\n")

        for block in section.blocks:
            if not _is_contextualizable(block, section):
                passthrough_md = _markdown_for_passthrough_block(block)
                if passthrough_md:
                    md_lines.append(passthrough_md)

                    contextualized_doc.rag_blocks.append(
                        RagBlock(
                            block_id=f"rag-{block.block_id}",
                            source_block_id=block.block_id,
                            section_id=section.section_id,
                            section_heading=section.heading,
                            section_anchor=section.anchor,
                            block_type=block.block_type,
                            text=passthrough_md.strip(),
                            transformation="passthrough",
                        )
                    )

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

            task = _create_task(
                doc=doc,
                section=section,
                block=block,
                model=model,
                step_run_id=step_run_id,
            )
            if step_run_id is not None and db_path is not None:
                with connect(db_path) as conn:
                    create_contextualization_task(
                        conn,
                        task_id=task.task_id,
                        step_run_id=step_run_id,
                        source_id=task.source_id,
                        source_block_id=task.source_block_id,
                        section_id=task.section_id,
                        section_heading=task.section_heading,
                        block_type=task.block_type,
                        strategy=task.strategy,
                        prompt_name=task.prompt_name,
                        prompt_version=task.prompt_version,
                        model_name=task.model_name,
                        status="running",
                        created_at=task.created_at.isoformat() if task.created_at else None,
                    )

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

                contextualized_doc.rag_blocks.append(
                    RagBlock(
                        block_id=f"rag-{contextualized_block.block_id}",
                        source_block_id=block.block_id,
                        section_id=section.section_id,
                        section_heading=section.heading,
                        section_anchor=section.anchor,
                        block_type=block.block_type,
                        text=result.contextualized_text,
                        transformation="contextualized",
                        prompt_name=result.prompt_name,
                        prompt_version=result.prompt_version,
                        model_name=result.model_name,
                        created_at=result.generated_at,
                    )
                )

                md_lines.append(result.contextualized_text + "\n")

                if step_run_id is not None and db_path is not None:
                    with connect(db_path) as conn:
                        finish_contextualization_task(
                            conn,
                            task_id=task.task_id,
                            status="completed",
                            contextualized_block_id=contextualized_block.block_id,
                            error_message=None,
                        )
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

                if step_run_id is not None and db_path is not None:
                    with connect(db_path) as conn:
                        finish_contextualization_task(
                            conn,
                            task_id=task.task_id,
                            status="failed",
                            contextualized_block_id=None,
                            error_message=result.error_message or "Unbekannter Fehler",
                        )

            time.sleep(0.2)

    markdown = "\n".join(md_lines).strip() + "\n"
    return contextualized_doc, markdown


def run(
    processed_dir: Path,
    contextualized_dir: Path,
    *,
    model: str = MODEL_DEFAULT,
    pipeline_version: str | None = None,
    run_id: str | None = None,
    db_path: Path | None = None,
) -> None:
    contextualized_dir.mkdir(parents=True, exist_ok=True)

    for file in sorted(processed_dir.glob("*.json")):
        data: dict[str, Any] = json.loads(file.read_text(encoding="utf-8"))
        doc = _wiki_document_from_json(data=data, source_file=file.name)

        doc.metadata.pipeline_version = pipeline_version or doc.metadata.pipeline_version
        doc.metadata.pipeline_run_id = run_id or doc.metadata.pipeline_run_id

        step_run_id = None
        output_version_id = None

        try:
            if run_id is not None and db_path is not None:
                step_run_id = _make_step_run_id(run_id, doc.metadata.source_id)
                input_version_id = _make_input_version_id(run_id, doc.metadata.source_id)

                with connect(db_path) as conn:
                    create_step_run(
                        conn,
                        step_run_id=step_run_id,
                        run_id=run_id,
                        source_id=doc.metadata.source_id,
                        step_name=STEP_NAME,
                        input_version_id=input_version_id,
                    )

            contextualized_doc, markdown = _contextualize_document(
                doc=doc,
                model=model,
                step_run_id=step_run_id,
                db_path=db_path,
            )

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

            if run_id is not None and db_path is not None:
                output_version_id = _make_output_version_id(run_id, doc.metadata.source_id)

                with connect(db_path) as conn:
                    create_document_version(
                        conn,
                        version_id=output_version_id,
                        source_id=doc.metadata.source_id,
                        run_id=run_id,
                        stage_name="contextualized_data",
                        artifact_path=out_json_path,
                    )
                    finish_step_run(
                        conn,
                        step_run_id=step_run_id,
                        status="completed",
                        output_version_id=output_version_id,
                    )

            print(f"[step4] wrote {out_md_path}")
            print(f"[step4] wrote {out_json_path}")

        except Exception as e:
            if run_id is not None and db_path is not None and step_run_id is not None:
                with connect(db_path) as conn:
                    finish_step_run(
                        conn,
                        step_run_id=step_run_id,
                        status="failed",
                        error_message=str(e),
                    )
            raise