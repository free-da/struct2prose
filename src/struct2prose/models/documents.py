from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class DocumentMetadata:
    source_id: str
    title: str
    xwiki_url: str | None
    xwiki_page_reference: str | None
    source_hash: str
    retrieved_at: datetime
    last_modified: str | None = None
    pipeline_run_id: str | None = None
    pipeline_version: str | None = None


@dataclass
class SourceDocument:
    metadata: DocumentMetadata
    raw_content: str
    content_type: str = "text/html"


@dataclass
class CleanDocument:
    metadata: DocumentMetadata
    raw_content: str
    cleaned_content: str
    content_root_hint: str | None = None


@dataclass
class StrippedDocument:
    metadata: DocumentMetadata
    # ursprünglicher Content-Root (aus Step 1)
    raw_content: str
    # nach extract_content_root
    cleaned_content: str
    # nach ui_strip (entscheidender Output dieses Schritts)
    stripped_content: str
    # optional: Hinweis, wie der Root bestimmt wurde
    content_root_hint: str | None = None
    # optional: Debug/Transparenz
    removed_elements: list[str] | None = None

@dataclass
class ContextualizedBlock:
    block_id: str
    source_block_id: str
    section_id: str
    section_heading: str | None
    content_type: str
    text: str


@dataclass
class ContextualizedDocument:
    metadata: DocumentMetadata
    contextualized_blocks: list[ContextualizedBlock] = field(default_factory=list)