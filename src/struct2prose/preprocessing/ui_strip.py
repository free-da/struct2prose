from __future__ import annotations

from bs4 import BeautifulSoup, Tag


def strip_ui_elements(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    root: Tag | None = soup.body or soup

    # 1) Remove XWiki "Contents" box (TOC) often rendered as: <div class="box"><strong>Contents</strong>...
    for box in root.select("div.box"):
        text = box.get_text(" ", strip=True).lower()
        if text.startswith("contents") or " contents " in f" {text} ":
            box.decompose()

    # 2) Remove sticky / inplace editing controls if they slipped into the export
    for sel in [
        ".sticky-buttons-wrapper",
        ".inplace-editing-buttons",
        "#autosaveControl",
        "#contentmenu",
        "#exportModal",
    ]:
        for el in root.select(sel):
            el.decompose()

    # 3) Remove empty remnants
    for el in root.select("div:empty, span:empty"):
        el.decompose()

    return str(soup)
