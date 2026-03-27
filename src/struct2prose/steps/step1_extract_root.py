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
from struct2prose.preprocessing.content_root import extract_content_root


def _compute_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _load_source_document_from_file(file_path: Path) -> SourceDocument:
    raw_content = file_path.read_text(encoding="utf-8")

    metadata = DocumentMetadata(
        source_id=f"file:{file_path.stem}",
        title=file_path.stem,
        xwiki_url=None,
        xwiki_page_reference=None,
        source_hash=_compute_sha256(raw_content),
        retrieved_at=datetime.now(),
        pipeline_version="v1",
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


def run(raw_dir: Path, clean_dir: Path, root_class: str = "xcontent") -> None:
    clean_dir.mkdir(parents=True, exist_ok=True)

    for file_path in sorted(raw_dir.glob("*.htm")):
        source_doc = _load_source_document_from_file(file_path)
        clean_doc = _extract_root(source_doc, root_class=root_class)

        out_path = clean_dir / f"{file_path.stem}.json"
        _export_clean_document(clean_doc, out_path)

        print(f"[step1] wrote {out_path}")