from __future__ import annotations

from bs4 import BeautifulSoup, Tag
from pathlib import Path

from struct2prose.parser.models import WikiDocument, Section, ContentBlock


BLOCK_TAGS = {"p", "ul", "ol", "table", "pre", "code", "div"}

def extract_text_with_breaks(tag: Tag) -> str:
    """
    Extract text from a tag, converting <br> to line breaks and
    normalizing whitespace.
    """
    for br in tag.find_all("br"):
        br.replace_with("\n")

    text = tag.get_text(separator=" ", strip=True)

    # Normalize excessive whitespace but keep line breaks
    lines = [line.strip() for line in text.splitlines()]
    return "\n".join(line for line in lines if line)

def _parse_container(container: Tag, sections: list[Section], current: Section) -> Section:
    for child in container.find_all(recursive=False):
        if not isinstance(child, Tag):
            continue

        name = (child.name or "").lower()

        if name in {"h1", "h2", "h3"}:
            if current.blocks or current.heading != "Einleitung":
                sections.append(current)
            heading = child.get_text(" ", strip=True) or "Abschnitt"
            current = Section(heading=heading)

        elif name == "p":
            text = extract_text_with_breaks(child)
            if text:
                current.blocks.append(ContentBlock("paragraph", text))

        elif name in {"ul", "ol"}:
            items = [li.get_text(" ", strip=True) for li in child.find_all("li", recursive=False)]
            items = [it for it in items if it]
            if items:
                current.blocks.append(ContentBlock("list", items))

        elif name == "table":
            rows: list[list[str]] = []
            for row in child.find_all("tr"):
                cells = [cell.get_text(" ", strip=True) for cell in row.find_all(["td", "th"])]
                rows.append(cells)
            current.blocks.append(ContentBlock("table", rows))

        elif name in {"pre", "code"}:
            code = extract_text_with_breaks(child)
            if code:
                current.blocks.append(ContentBlock("code", code))


        elif name == "div":

            # XWiki: code blocks are often rendered as <div class="code">...</div>

            classes = set(child.get("class", []) or [])

            if "code" in classes:

                code = child.get_text("\n", strip=True)

                if code:
                    current.blocks.append(ContentBlock("code", code))

                continue

            # div als Container; wenn keine Block-Kinder: als Textblock

            has_block_children = child.find(list(BLOCK_TAGS), recursive=False) is not None

            if has_block_children:

                current = _parse_container(child, sections, current)

            else:

                text = extract_text_with_breaks(child)

                if text:
                    current.blocks.append(ContentBlock("div_text", text))

        # alles andere ignorieren

    return current


def parse_html_file(path: Path) -> WikiDocument:
    with open(path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    title = soup.title.string.strip() if soup.title and soup.title.string else path.stem

    sections: list[Section] = []
    current = Section(heading="Einleitung")

    if soup.body:
        current = _parse_container(soup.body, sections, current)

    if current.blocks or not sections:
        sections.append(current)

    return WikiDocument(title=title, sections=sections, source_file=path.name)
