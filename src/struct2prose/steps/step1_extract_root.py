from __future__ import annotations

from datetime import datetime
import hashlib
from pathlib import Path
import json
from dataclasses import asdict

from struct2prose.models.documents import (
    CleanDocument,
    DocumentMetadata,
    SourceDocument,
)
from struct2prose.persistence.db import connect
from struct2prose.persistence.store import (
    create_document_version,
    create_step_run,
    finish_step_run,
    upsert_document,
)
from struct2prose.preprocessing.content_root import extract_content_root

STEP_NAME = "extract_root"

def _compute_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def _make_step_run_id(run_id: str, source_id: str) -> str:
    safe_source_id = source_id.replace(":", "_")
    return f"{run_id}:{STEP_NAME}:{safe_source_id}"

def _make_output_version_id(run_id: str, source_id: str) -> str:
    safe_source_id = source_id.replace(":", "_")
    return f"{run_id}:clean_data:{safe_source_id}"

def _load_source_document_from_file(file_path: Path) -> SourceDocument:
    raw_content = file_path.read_text(encoding="utf-8")

    metadata = DocumentMetadata(
        source_id=f"file:{file_path.stem}",
        title=file_path.stem,
        xwiki_url=None,
        xwiki_page_reference=None,
        source_hash=_compute_sha256(raw_content),
        retrieved_at=datetime.utcnow(),
        last_modified=None,
        pipeline_version=None,
        pipeline_run_id=None,
    )

    return SourceDocument(
        metadata=metadata,
        raw_content=raw_content,
        content_type="text/html",
    )


def _extract_root(source_doc: SourceDocument, root_class: str = "xcontent") -> CleanDocument:
    cleaned_content = extract_content_root(source_doc.raw_content)

    return CleanDocument(
        metadata=source_doc.metadata,
        raw_content=source_doc.raw_content,
        cleaned_content=cleaned_content,
        content_root_hint=root_class,
    )


def _export_clean_document(clean_doc: CleanDocument, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(asdict(clean_doc), ensure_ascii=False, indent=2, default=str),
        encoding="utf-8",
    )


def run(
        raw_dir: Path,
        clean_dir: Path,
        root_class: str = "xcontent",
        *,
        pipeline_version: str | None = None,
        run_id: str | None = None,
        db_path: Path | None = None,
) -> None:
    clean_dir.mkdir(parents=True, exist_ok=True)

    for file_path in sorted(raw_dir.glob("*.htm")):
        source_doc = _load_source_document_from_file(file_path)
        source_doc.metadata.pipeline_version = pipeline_version
        source_doc.metadata.pipeline_run_id = run_id

        step_run_id = None
        output_version_id = None

        try:
            if run_id and db_path:
                step_run_id = _make_step_run_id(run_id, source_doc.metadata.source_id)

                with connect(db_path) as conn:
                    upsert_document(conn, source_doc.metadata)
                    create_step_run(
                        conn,
                        step_run_id=step_run_id,
                        run_id=run_id,
                        source_id=source_doc.metadata.source_id,
                        step_name=STEP_NAME,
                        input_version_id=None,
                    )

            clean_doc = _extract_root(source_doc, root_class=root_class)

            out_path = clean_dir / f"{file_path.stem}.json"
            _export_clean_document(clean_doc, out_path)

            if run_id is not None and db_path is not None:
                output_version_id = _make_output_version_id(run_id, clean_doc.metadata.source_id)

                with connect(db_path) as conn:
                    create_document_version(
                        conn,
                        version_id=output_version_id,
                        source_id=clean_doc.metadata.source_id,
                        run_id=run_id,
                        stage_name="clean_data",
                        artifact_path=out_path,
                    )
                    finish_step_run(
                        conn,
                        step_run_id=step_run_id,
                        status="completed",
                        output_version_id=output_version_id,
                    )

            print(f"[step1] wrote {out_path}")

        except Exception as e:
            if run_id and db_path and step_run_id:
                with connect(db_path) as conn:
                    finish_step_run(
                        conn,
                        step_run_id=step_run_id,
                        status="failed",
                        error_message=str(e),
                    )
            raise