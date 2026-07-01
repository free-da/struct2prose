import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from struct2prose.models.documents import StrippedDocument, DocumentMetadata
from struct2prose.parser.html_parser import parse_html
from struct2prose.persistence.db import connect
from struct2prose.persistence.store import (
    create_document_version,
    create_step_run,
    finish_step_run,
)

STEP_NAME = "parse"


def _make_step_run_id(run_id: str, source_id: str) -> str:
    safe_source_id = source_id.replace(":", "_")
    return f"{run_id}:{STEP_NAME}:{safe_source_id}"


def _make_input_version_id(run_id: str, source_id: str) -> str:
    safe_source_id = source_id.replace(":", "_")
    return f"{run_id}:stripped_data:{safe_source_id}"


def _make_output_version_id(run_id: str, source_id: str) -> str:
    safe_source_id = source_id.replace(":", "_")
    return f"{run_id}:processed_data:{safe_source_id}"


def _load_stripped_document(path: Path) -> StrippedDocument:
    data = json.loads(path.read_text(encoding="utf-8"))

    metadata_data = data["metadata"]
    metadata = DocumentMetadata(
        source_id=metadata_data["source_id"],
        title=metadata_data["title"],
        xwiki_url=metadata_data.get("xwiki_url"),
        xwiki_page_reference=metadata_data.get("xwiki_page_reference"),
        source_hash=metadata_data["source_hash"],
        retrieved_at=(
            datetime.fromisoformat(metadata_data["retrieved_at"])
            if metadata_data.get("retrieved_at")
            else None
        ),
        last_modified=metadata_data.get("last_modified"),
        pipeline_run_id=metadata_data.get("pipeline_run_id"),
        pipeline_version=metadata_data.get("pipeline_version"),
    )

    return StrippedDocument(
        metadata=metadata,
        raw_content=data["raw_content"],
        cleaned_content=data["cleaned_content"],
        stripped_content=data["stripped_content"],
        content_root_hint=data.get("content_root_hint"),
    )


def _save_parsed_document(doc, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(asdict(doc), ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )


def run(
    stripped_dir: Path,
    processed_dir: Path,
    *,
    pipeline_version: str | None = None,
    run_id: str | None = None,
    db_path: Path | None = None,
) -> None:
    processed_dir.mkdir(parents=True, exist_ok=True)

    for file in sorted(stripped_dir.glob("*.json")):
        stripped_doc = _load_stripped_document(file)

        stripped_doc.metadata.pipeline_version = (
            pipeline_version or stripped_doc.metadata.pipeline_version
        )
        stripped_doc.metadata.pipeline_run_id = (
            run_id or stripped_doc.metadata.pipeline_run_id
        )

        step_run_id = None
        input_version_id = None
        output_version_id = None

        try:
            if run_id is not None and db_path is not None:
                step_run_id = _make_step_run_id(run_id, stripped_doc.metadata.source_id)
                input_version_id = _make_input_version_id(run_id, stripped_doc.metadata.source_id)

                with connect(db_path) as conn:
                    create_step_run(
                        conn,
                        step_run_id=step_run_id,
                        run_id=run_id,
                        source_id=stripped_doc.metadata.source_id,
                        step_name=STEP_NAME,
                        input_version_id=input_version_id,
                    )

            parsed_doc = parse_html(
                stripped_doc.stripped_content,
                metadata=stripped_doc.metadata,
            )

            out_path = processed_dir / file.name
            _save_parsed_document(parsed_doc, out_path)

            if run_id is not None and db_path is not None:
                output_version_id = _make_output_version_id(run_id, parsed_doc.metadata.source_id)

                with connect(db_path) as conn:
                    create_document_version(
                        conn,
                        version_id=output_version_id,
                        source_id=parsed_doc.metadata.source_id,
                        run_id=run_id,
                        stage_name="processed_data",
                        artifact_path=out_path,
                    )
                    finish_step_run(
                        conn,
                        step_run_id=step_run_id,
                        status="completed",
                        output_version_id=output_version_id,
                    )

            print(f"[step3] wrote {out_path}")

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