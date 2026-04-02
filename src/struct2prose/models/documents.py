from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

@dataclass
class DocumentMetadata:
    source_id: str
    title: str
    xwiki_url: str | None
    xwiki_page_reference: str | None
    source_hash: str
    retrieved_at: datetime | None
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
    raw_content: str
    cleaned_content: str
    stripped_content: str
    content_root_hint: str | None = None

@dataclass
class ContextualizationTask:
    task_id: str
    source_id: str
    pipeline_run_id: str | None
    source_block_id: str
    section_id: str
    section_heading: str | None
    block_type: str
    strategy: str
    prompt_name: str
    prompt_version: str
    model_name: str | None = None
    created_at: datetime | None = None


@dataclass
class ContextualizationResult:
    task_id: str
    source_block_id: str
    status: str                  # "completed", "failed", "skipped"
    contextualized_text: str | None = None
    error_message: str | None = None
    prompt_name: str | None = None
    prompt_version: str | None = None
    model_name: str | None = None
    generated_at: datetime | None = None


@dataclass
class ContextualizedBlock:
    block_id: str
    source_block_id: str
    section_id: str
    section_heading: str | None
    block_type: str
    text: str
    prompt_name: str | None = None
    prompt_version: str | None = None
    model_name: str | None = None
    created_at: datetime | None = None


@dataclass
class SkippedBlock:
    source_block_id: str
    section_id: str
    section_heading: str | None
    block_type: str
    reason: str


@dataclass
class FailedBlock:
    source_block_id: str
    section_id: str
    section_heading: str | None
    block_type: str
    error_message: str


@dataclass
class ContextualizedDocument:
    metadata: "DocumentMetadata"
    contextualized_blocks: list[ContextualizedBlock] = field(default_factory=list)
    skipped_blocks: list[SkippedBlock] = field(default_factory=list)
    failed_blocks: list[FailedBlock] = field(default_factory=list)