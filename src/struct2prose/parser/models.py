from dataclasses import dataclass, field
from typing import Any, List

from struct2prose.models.documents import DocumentMetadata


@dataclass
class ContentBlock:
    block_id: str
    block_type: str   # "paragraph", "table", "list", "div_text", "code"
    content: Any


@dataclass
class Section:
    section_id: str
    heading: str
    blocks: List[ContentBlock] = field(default_factory=list)


@dataclass
class WikiDocument:
    metadata: "DocumentMetadata"
    sections: list[Section] = field(default_factory=list)
