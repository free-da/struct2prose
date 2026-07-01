from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import quote, unquote

import requests


def _slug(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "page"


def _sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def _view_url_from_rest_page_link(base_url: str, href: str) -> str:
    # .../spaces/A/spaces/B/pages/WebHome
    parts = re.findall(r"/spaces/([^/]+)", href)
    parts = [unquote(p) for p in parts]

    path = "/".join(quote(p) for p in parts)
    return f"{base_url}/bin/view/{path}/"


def _html_url_from_rest_page_link(base_url: str, href: str) -> str:
    return _view_url_from_rest_page_link(base_url, href) + "?xpage=plain"

def _view_url(base_url: str, page_ref: str) -> str:
    parts = page_ref.split(".")
    if parts[-1] == "WebHome":
        parts = parts[:-1]
    path = "/".join(quote(p) for p in parts)
    return f"{base_url}/bin/view/{path}/"


def _html_url(base_url: str, page_ref: str) -> str:
    parts = page_ref.split(".")
    if parts[-1] == "WebHome":
        parts = parts[:-1]
    path = "/".join(quote(p) for p in parts)
    return f"{base_url}/bin/view/{path}/?xpage=plain"

def _is_allowed_page(
    page_ref: str,
    *,
    include_spaces: set[str] | None = None,
    exclude_prefixes: tuple[str, ...] = (
        "XWiki.",
        "Main.",
        "Sandbox.",
        "Help.",
        "Dashboard.",
        "Panels.",
        "Scheduler.",
        "AppWithinMinutes.",
        "Menu.",
        "FlamingoThemes.",
    ),
) -> bool:
    if any(page_ref.startswith(prefix) for prefix in exclude_prefixes):
        return False

    if include_spaces:
        top_space = page_ref.split(".", 1)[0]
        return top_space in include_spaces

    return True

def fetch_xwiki_pages(
    *,
    wiki_base_url: str,
    wiki_id: str,
    raw_dir: Path,
    include_spaces: set[str] | None = None,
    username: str | None = None,
    password: str | None = None,
) -> None:
    raw_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    if username and password:
        session.auth = (username, password)

    # Erstmal pragmatisch über REST search.
    search_url = f"{wiki_base_url}/rest/wikis/{wiki_id}/search"
    response = session.get(
        search_url,
        params={
            "q": "",
            "scope": "name",
            "number": 1000,
            "media": "json",
        },
        timeout=30,
    )
    response.raise_for_status()

    data = response.json()
    results = data.get("searchResults", [])

    manifest = []

    for item in results:
        page_ref = item.get("pageFullName") or item.get("id") or item.get("pageName")
        title = item.get("title") or page_ref

        if not page_ref:
            continue

        if not _is_allowed_page(page_ref, include_spaces=include_spaces):
            print(f"[fetch-xwiki] skipped {page_ref}")
            continue
        page_link = next(
            (
                link["href"]
                for link in item.get("links", [])
                if link.get("rel") == "http://www.xwiki.org/rel/page"
            ),
            None,
        )

        if page_link:
            wiki_url = _view_url_from_rest_page_link(wiki_base_url, page_link)
            html_url = _html_url_from_rest_page_link(wiki_base_url, page_link)
        else:
            html_url = _html_url(wiki_base_url, page_ref)
            wiki_url = _view_url(wiki_base_url, page_ref)

        html_response = session.get(html_url, timeout=60)
        html_response.raise_for_status()

        content_type = html_response.headers.get("Content-Type", "")

        if "text/html" not in content_type:
            print(f"[fetch-xwiki] skipped non-html response for {page_ref}: {content_type}")
            continue

        html = html_response.text

        if not html.strip():
            print(f"[fetch-xwiki] WARNING empty html for {page_ref}: {html_url}")
            continue

        file_name = f"{_slug(page_ref)}.htm"
        out_path = raw_dir / file_name
        out_path.write_text(html, encoding="utf-8")

        manifest.append(
            {
                "file": file_name,
                "source_id": f"xwiki:{page_ref}",
                "title": title,
                "xwiki_url": wiki_url,
                "xwiki_page_reference": page_ref,
                "source_hash": _sha256(html),
                "retrieved_at": datetime.utcnow().isoformat(),
                "html_export_url": html_url,
            }
        )

        print(f"[fetch-xwiki] wrote {out_path} ({len(html)} chars) from {html_url}")

    (raw_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )