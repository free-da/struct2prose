import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from struct2prose.models.documents import StrippedDocument, DocumentMetadata
from struct2prose.parser.html_parser import parse_html

def _load_stripped_document(path: Path) -> StrippedDocument:
    data = json.loads(path.read_text(encoding="utf-8"))

    metadata_data = data["metadata"]
    metadata = DocumentMetadata(
        source_id=metadata_data["source_id"],
        title=metadata_data["title"],
        xwiki_url=metadata_data.get("xwiki_url"),
        xwiki_page_reference=metadata_data.get("xwiki_page_reference"),
        source_hash=metadata_data["source_hash"],
        retrieved_at=datetime.fromisoformat(metadata_data["retrieved_at"]),
        pipeline_version=metadata_data["pipeline_version"],
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

def run(stripped_dir: Path, processed_dir: Path) -> None:
    processed_dir.mkdir(parents=True, exist_ok=True)

    for file in sorted(stripped_dir.glob("*.json")):
        stripped_doc = _load_stripped_document(file)
        parsed_doc = parse_html(
            stripped_doc.stripped_content,
            metadata=stripped_doc.metadata,
        )
        out_path = processed_dir / file.name
        _save_parsed_document(parsed_doc, out_path)

        print(f"[step3] wrote {out_path}")
