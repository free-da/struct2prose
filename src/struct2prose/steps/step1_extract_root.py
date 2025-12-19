from __future__ import annotations

from pathlib import Path

from struct2prose.preprocessing.content_root import extract_content_root


def run(raw_dir: Path, clean_dir: Path, root_class: str = "xcontent") -> None:
    clean_dir.mkdir(parents=True, exist_ok=True)

    for file in sorted(raw_dir.glob("*.htm")):
        html = file.read_text(encoding="utf-8")
        cleaned = extract_content_root(html)

        out_path = clean_dir / file.name
        out_path.write_text(cleaned, encoding="utf-8")
        print(f"[step1] wrote {out_path}")
