from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path

from struct2prose.models.documents import DocumentMetadata
from struct2prose.persistence.db import compute_file_sha256


def utc_now_iso() -> str:
    return datetime.utcnow().isoformat()


def upsert_document(conn: sqlite3.Connection, metadata: DocumentMetadata) -> None:
    conn.execute(
        """
        INSERT INTO documents (
            source_id, title, xwiki_url, xwiki_page_reference,
            source_hash, retrieved_at, last_modified
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(source_id) DO UPDATE SET
            title = excluded.title,
            xwiki_url = excluded.xwiki_url,
            xwiki_page_reference = excluded.xwiki_page_reference,
            source_hash = excluded.source_hash,
            retrieved_at = excluded.retrieved_at,
            last_modified = excluded.last_modified
        """,
        (
            metadata.source_id,
            metadata.title,
            metadata.xwiki_url,
            metadata.xwiki_page_reference,
            metadata.source_hash,
            metadata.retrieved_at.isoformat() if metadata.retrieved_at else None,
            metadata.last_modified,
        ),
    )


def create_pipeline_run(
    conn: sqlite3.Connection,
    run_id: str,
    pipeline_version: str | None,
    llm_provider: str | None,
    model_name: str | None,
) -> None:
    conn.execute(
        """
        INSERT INTO pipeline_runs (
            run_id, started_at, status, pipeline_version, llm_provider, model_name
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (run_id, utc_now_iso(), "running", pipeline_version, llm_provider, model_name),
    )


def finish_pipeline_run(conn: sqlite3.Connection, run_id: str, status: str) -> None:
    conn.execute(
        """
        UPDATE pipeline_runs
        SET finished_at = ?, status = ?
        WHERE run_id = ?
        """,
        (utc_now_iso(), status, run_id),
    )


def create_document_version(
    conn: sqlite3.Connection,
    version_id: str,
    source_id: str,
    run_id: str,
    stage_name: str,
    artifact_path: Path,
) -> None:
    conn.execute(
        """
        INSERT INTO document_versions (
            version_id, source_id, run_id, stage_name,
            artifact_path, artifact_hash, created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            version_id,
            source_id,
            run_id,
            stage_name,
            str(artifact_path),
            compute_file_sha256(artifact_path) if artifact_path.exists() else None,
            utc_now_iso(),
        ),
    )


def create_step_run(
    conn: sqlite3.Connection,
    step_run_id: str,
    run_id: str,
    source_id: str,
    step_name: str,
    input_version_id: str | None,
) -> None:
    conn.execute(
        """
        INSERT INTO step_runs (
            step_run_id, run_id, source_id, step_name,
            input_version_id, started_at, status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (step_run_id, run_id, source_id, step_name, input_version_id, utc_now_iso(), "running"),
    )


def finish_step_run(
    conn: sqlite3.Connection,
    step_run_id: str,
    status: str,
    output_version_id: str | None = None,
    error_message: str | None = None,
) -> None:
    conn.execute(
        """
        UPDATE step_runs
        SET finished_at = ?, status = ?, output_version_id = ?, error_message = ?
        WHERE step_run_id = ?
        """,
        (utc_now_iso(), status, output_version_id, error_message, step_run_id),
    )


def create_contextualization_task(
    conn: sqlite3.Connection,
    *,
    task_id: str,
    step_run_id: str,
    source_id: str,
    source_block_id: str,
    section_id: str,
    section_heading: str | None,
    block_type: str,
    strategy: str,
    prompt_name: str,
    prompt_version: str,
    model_name: str | None,
    status: str,
    created_at: str | None,
) -> None:
    conn.execute(
        """
        INSERT INTO contextualization_tasks (
            task_id, step_run_id, source_id, source_block_id,
            section_id, section_heading, block_type, strategy,
            prompt_name, prompt_version, model_name, status, created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            task_id,
            step_run_id,
            source_id,
            source_block_id,
            section_id,
            section_heading,
            block_type,
            strategy,
            prompt_name,
            prompt_version,
            model_name,
            status,
            created_at,
        ),
    )


def finish_contextualization_task(
    conn: sqlite3.Connection,
    task_id: str,
    status: str,
    contextualized_block_id: str | None = None,
    error_message: str | None = None,
) -> None:
    conn.execute(
        """
        UPDATE contextualization_tasks
        SET finished_at = ?, status = ?, contextualized_block_id = ?, error_message = ?
        WHERE task_id = ?
        """,
        (utc_now_iso(), status, contextualized_block_id, error_message, task_id),
    )