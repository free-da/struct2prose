from __future__ import annotations

from bs4 import BeautifulSoup, Tag
from pathlib import Path

from struct2prose.models.documents import DocumentMetadata
from struct2prose.parser.models import WikiDocument, Section, ContentBlock


BLOCK_TAGS = {"p", "ul", "ol", "table", "pre", "code", "div"}


def extract_text_with_breaks(tag: Tag) -> str:
    """
    Extract text from a tag, converting <br> to line breaks and
    normalizing whitespace while preserving meaningful line breaks.
    """
    tag = tag.__copy__() if hasattr(tag, "__copy__") else BeautifulSoup(str(tag), "html.parser").find()
    if tag is None:
        return ""

    for br in tag.find_all("br"):
        br.replace_with("\n")

    text = tag.get_text(separator=" ", strip=True)

    lines = [line.strip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line)


def _new_section(section_index: int, heading: str) -> Section:
    return Section(
        section_id=f"sec-{section_index}",
        heading=heading,
    )


def _next_block_id(section: Section) -> str:
    return f"{section.section_id}-blk-{len(section.blocks) + 1}"


def _parse_container(
    container: Tag,
    sections: list[Section],
    current: Section,
    section_index: int,
) -> tuple[Section, int]:
    for child in container.find_all(recursive=False):
        if not isinstance(child, Tag):
            continue

        name = (child.name or "").lower()

        if name in {"h1", "h2", "h3"}:
            if current.blocks or current.heading != "Einleitung":
                sections.append(current)

            heading = child.get_text(" ", strip=True) or "Abschnitt"
            section_index += 1
            current = _new_section(section_index, heading)

        elif name == "p":
            text = extract_text_with_breaks(child)
            if text:
                current.blocks.append(
                    ContentBlock(
                        block_id=_next_block_id(current),
                        block_type="paragraph",
                        content=text,
                    )
                )

        elif name in {"ul", "ol"}:
            items = [
                li.get_text(" ", strip=True)
                for li in child.find_all("li", recursive=False)
            ]
            items = [it for it in items if it]
            if items:
                current.blocks.append(
                    ContentBlock(
                        block_id=_next_block_id(current),
                        block_type="list",
                        content=items,
                    )
                )

        elif name == "table":
            rows: list[list[str]] = []
            for row in child.find_all("tr"):
                cells = [
                    cell.get_text(" ", strip=True)
                    for cell in row.find_all(["td", "th"])
                ]
                if cells:
                    rows.append(cells)

            if rows:
                current.blocks.append(
                    ContentBlock(
                        block_id=_next_block_id(current),
                        block_type="table",
                        content=rows,
                    )
                )

        elif name in {"pre", "code"}:
            code = extract_text_with_breaks(child)
            if code:
                current.blocks.append(
                    ContentBlock(
                        block_id=_next_block_id(current),
                        block_type="code",
                        content=code,
                    )
                )

        elif name == "div":
            classes = set(child.get("class", []) or [])

            # XWiki: code blocks are often rendered as <div class="code">...</div>
            if "code" in classes:
                code = child.get_text("\n", strip=True)
                if code:
                    current.blocks.append(
                        ContentBlock(
                            block_id=_next_block_id(current),
                            block_type="code",
                            content=code,
                        )
                    )
                continue

            # div as container; if it contains block children, recurse
            has_block_children = child.find(list(BLOCK_TAGS), recursive=False) is not None

            if has_block_children:
                current, section_index = _parse_container(child, sections, current, section_index)
            else:
                text = extract_text_with_breaks(child)
                if text:
                    current.blocks.append(
                        ContentBlock(
                            block_id=_next_block_id(current),
                            block_type="div_text",
                            content=text,
                        )
                    )

        # everything else is ignored

    return current, section_index


def parse_html(html: str, metadata: DocumentMetadata) -> WikiDocument:
    soup = BeautifulSoup(html, "html.parser")

    title = (
        soup.title.string.strip()
        if soup.title and soup.title.string
        else metadata.title
    )

    sections: list[Section] = []
    section_index = 1
    current = _new_section(section_index, "Einleitung")

    root = soup.body if soup.body else soup
    current, section_index = _parse_container(root, sections, current, section_index)

    if current.blocks or not sections:
        sections.append(current)

    return WikiDocument(
        metadata=metadata,
        sections=sections,
    )


def parse_html_file(path: Path) -> WikiDocument:
    html = path.read_text(encoding="utf-8")

    metadata = DocumentMetadata(
        source_id=f"file:{path.stem}",
        title=path.stem,
        xwiki_url=None,
        xwiki_page_reference=None,
        source_hash="",
        retrieved_at=None,
        pipeline_version="legacy",
    )

    return parse_html(html, metadata)