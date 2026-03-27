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
    path.write_text(
        json.dumps(asdict(doc), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def run(clean_dir: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    for file in sorted(clean_dir.glob("*.json")):
        clean_doc = _load_clean_document(file)

        stripped_content = strip_ui_elements(clean_doc.cleaned_content)

        stripped_doc = StrippedDocument(
            metadata=clean_doc.metadata,
            raw_content=clean_doc.raw_content,
            cleaned_content=clean_doc.cleaned_content,
            stripped_content=stripped_content,
            content_root_hint=clean_doc.content_root_hint,
        )

        out_path = out_dir / file.name
        _save_stripped_document(stripped_doc, out_path)
        print(f"[step2] wrote {out_path}")