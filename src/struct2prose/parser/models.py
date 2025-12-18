from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class ContentBlock:
    block_type: str   # "paragraph", "table", "list", "div_text", "code"
    content: Any


@dataclass
class Section:
    heading: str
    blocks: List[ContentBlock] = field(default_factory=list)


@dataclass
class WikiDocument:
    title: str
    sections: List[Section]
    source_file: str
