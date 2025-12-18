import json
from dataclasses import asdict
from pathlib import Path

from struct2prose.parser import parse_html_file


def run(raw_dir: Path, processed_dir: Path) -> None:
    processed_dir.mkdir(parents=True, exist_ok=True)

    for file in sorted(raw_dir.glob("*.htm")):
        doc = parse_html_file(file)
        out_path = processed_dir / f"{file.stem}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(asdict(doc), f, ensure_ascii=False, indent=2)
        print(f"[step3] wrote {out_path}")
