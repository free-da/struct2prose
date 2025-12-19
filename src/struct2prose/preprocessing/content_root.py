from __future__ import annotations

from bs4 import BeautifulSoup, Tag


def extract_content_root(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # Prefer the real content container
    root: Tag | None = soup.select_one("#xwikicontent")
    if root is None:
        # Fallback: broader container
        root = soup.select_one(".xcontent")
    if root is None:
        root = soup.body if soup.body else soup

    # Minimal cleanup inside root (safe even if root is xcontent)
    for bad in root.find_all(["script", "style", "noscript"]):
        bad.decompose()

    out = BeautifulSoup("<html><body></body></html>", "html.parser")
    out.body.append(root)
    return str(out)
