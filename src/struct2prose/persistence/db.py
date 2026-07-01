from __future__ import annotations

import hashlib
import sqlite3
from contextlib import contextmanager
from pathlib import Path


DEFAULT_DB_PATH = Path("struct2prose.db")


def compute_file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def get_connection(db_path: Path | str = DEFAULT_DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


@contextmanager
def connect(db_path: Path | str = DEFAULT_DB_PATH):
    conn = get_connection(db_path)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS pipeline_runs (
            run_id TEXT PRIMARY KEY,
            started_at TEXT NOT NULL,
            finished_at TEXT,
            status TEXT NOT NULL,
            pipeline_version TEXT,
            llm_provider TEXT,
            model_name TEXT
        );

        CREATE TABLE IF NOT EXISTS documents (
            source_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            xwiki_url TEXT,
            xwiki_page_reference TEXT,
            source_hash TEXT,
            retrieved_at TEXT,
            last_modified TEXT
        );

        CREATE TABLE IF NOT EXISTS document_versions (
            version_id TEXT PRIMARY KEY,
            source_id TEXT NOT NULL,
            run_id TEXT NOT NULL,
            stage_name TEXT NOT NULL,
            artifact_path TEXT NOT NULL,
            artifact_hash TEXT,
            created_at TEXT NOT NULL,
            FOREIGN KEY (source_id) REFERENCES documents(source_id),
            FOREIGN KEY (run_id) REFERENCES pipeline_runs(run_id)
        );

        CREATE TABLE IF NOT EXISTS step_runs (
            step_run_id TEXT PRIMARY KEY,
            run_id TEXT NOT NULL,
            source_id TEXT NOT NULL,
            step_name TEXT NOT NULL,
            input_version_id TEXT,
            output_version_id TEXT,
            started_at TEXT NOT NULL,
            finished_at TEXT,
            status TEXT NOT NULL,
            error_message TEXT,
            FOREIGN KEY (run_id) REFERENCES pipeline_runs(run_id),
            FOREIGN KEY (source_id) REFERENCES documents(source_id),
            FOREIGN KEY (input_version_id) REFERENCES document_versions(version_id),
            FOREIGN KEY (output_version_id) REFERENCES document_versions(version_id)
        );

        CREATE TABLE IF NOT EXISTS contextualization_tasks (
            task_id TEXT PRIMARY KEY,
            step_run_id TEXT NOT NULL,
            source_id TEXT NOT NULL,
            source_block_id TEXT NOT NULL,
            section_id TEXT NOT NULL,
            section_heading TEXT,
            block_type TEXT NOT NULL,
            strategy TEXT NOT NULL,
            prompt_name TEXT NOT NULL,
            prompt_version TEXT NOT NULL,
            model_name TEXT,
            status TEXT NOT NULL,
            contextualized_block_id TEXT,
            error_message TEXT,
            created_at TEXT,
            finished_at TEXT,
            FOREIGN KEY (step_run_id) REFERENCES step_runs(step_run_id),
            FOREIGN KEY (source_id) REFERENCES documents(source_id)
        );

        CREATE INDEX IF NOT EXISTS idx_document_versions_source_id
            ON document_versions(source_id);

        CREATE INDEX IF NOT EXISTS idx_step_runs_run_id
            ON step_runs(run_id);

        CREATE INDEX IF NOT EXISTS idx_step_runs_source_id
            ON step_runs(source_id);

        CREATE INDEX IF NOT EXISTS idx_contextualization_tasks_step_run_id
            ON contextualization_tasks(step_run_id);
        """
    )