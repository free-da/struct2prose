from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from struct2prose.models.documents import (
    CleanDocument,
    DocumentMetadata,
    StrippedDocument,
)
from struct2prose.preprocessing.ui_strip import strip_ui_elements
from struct2prose.persistence.db import connect
from struct2prose.persistence.store import (
    create_document_version,
    create_step_run,
    finish_step_run,
)

STEP_NAME = "strip_ui"

def _make_step_run_id(run_id: str, source_id: str) -> str:
    safe_source_id = source_id.replace(":", "_")
    return f"{run_id}:{STEP_NAME}:{safe_source_id}"

def _make_input_version_id(run_id: str, source_id: str) -> str:
    safe_source_id = source_id.replace(":", "_")
    return f"{run_id}:clean_data:{safe_source_id}"

def _make_output_version_id(run_id: str, source_id: str) -> str:
    safe_source_id = source_id.replace(":", "_")
    return f"{run_id}:stripped_data:{safe_source_id}"

def _load_clean_document(path: Path) -> CleanDocument:
    data = json.loads(path.read_text(encoding="utf-8"))

    metadata = DocumentMetadata(**data["metadata"])

    return CleanDocument(
        metadata=metadata,
        raw_content=data["raw_content"],
        cleaned_content=data["cleaned_content"],
        content_root_hint=data.get("content_root_hint"),
    )


def _save_stripped_document(doc: StrippedDocument, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(asdict(doc), ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )

def run(
    clean_dir: Path,
    stripped_dir: Path,
    *,
    pipeline_version: str | None = None,
    run_id: str | None = None,
    db_path: Path | None = None,
) -> None:
    stripped_dir.mkdir(parents=True, exist_ok=True)

    for file in sorted(clean_dir.glob("*.json")):
        clean_doc = _load_clean_document(file)

        clean_doc.metadata.pipeline_version = pipeline_version or clean_doc.metadata.pipeline_version
        clean_doc.metadata.pipeline_run_id = run_id or clean_doc.metadata.pipeline_run_id

        step_run_id = None
        input_version_id = None
        output_version_id = None

        try:
            if run_id is not None and db_path is not None:
                step_run_id = _make_step_run_id(run_id, clean_doc.metadata.source_id)
                input_version_id = _make_input_version_id(run_id, clean_doc.metadata.source_id)

                with connect(db_path) as conn:
                    create_step_run(
                        conn,
                        step_run_id=step_run_id,
                        run_id=run_id,
                        source_id=clean_doc.metadata.source_id,
                        step_name=STEP_NAME,
                        input_version_id=input_version_id,
                    )

            stripped_content = strip_ui_elements(clean_doc.cleaned_content)

            stripped_doc = StrippedDocument(
                metadata=clean_doc.metadata,
                raw_content=clean_doc.raw_content,
                cleaned_content=clean_doc.cleaned_content,
                stripped_content=stripped_content,
                content_root_hint=clean_doc.content_root_hint,
            )

            out_path = stripped_dir / file.name
            _save_stripped_document(stripped_doc, out_path)

            if run_id is not None and db_path is not None:
                output_version_id = _make_output_version_id(run_id, stripped_doc.metadata.source_id)

                with connect(db_path) as conn:
                    create_document_version(
                        conn,
                        version_id=output_version_id,
                        source_id=stripped_doc.metadata.source_id,
                        run_id=run_id,
                        stage_name="stripped_data",
                        artifact_path=out_path,
                    )
                    finish_step_run(
                        conn,
                        step_run_id=step_run_id,
                        status="completed",
                        output_version_id=output_version_id,
                    )

            print(f"[step2] wrote {out_path}")

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