from __future__ import annotations

from pathlib import Path

from struct2prose.preprocessing.ui_strip import strip_ui_elements


def run(clean_dir: Path, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    for file in sorted(clean_dir.glob("*.htm")):
        html = file.read_text(encoding="utf-8")
        stripped = strip_ui_elements(html)

        out_path = out_dir / file.name
        out_path.write_text(stripped, encoding="utf-8")
        print(f"[step2] wrote {out_path}")
