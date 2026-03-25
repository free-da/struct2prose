import argparse
from pathlib import Path

from struct2prose.steps.step1_extract_root import run as run_extract_root
from struct2prose.steps.step2_strip_ui import run as run_strip_ui
from struct2prose.steps.step3_parse import run as run_parse
from struct2prose.steps.step4_contextualize import run as run_contextualize
from struct2prose.config import Config


def main() -> None:
    Config.validate()
    parser = argparse.ArgumentParser(prog="struct2prose")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_root = sub.add_parser("extract-root", help="Extract XWiki main content into clean HTML")
    p_root.add_argument("--raw-dir", type=Path, default=Path("raw_data"))
    p_root.add_argument("--out-dir", type=Path, default=Path("clean_data"))

    p_ui = sub.add_parser("strip-ui", help="Remove remaining UI elements inside extracted content")
    p_ui.add_argument("--in-dir", type=Path, default=Path("clean_data"))
    p_ui.add_argument("--out-dir", type=Path, default=Path("clean_data"))  # MVP: overwrite by default

    p_parse = sub.add_parser("parse", help="Parse clean HTML to processed JSON")
    p_parse.add_argument("--raw-dir", type=Path, default=Path("clean_data"))
    p_parse.add_argument("--out-dir", type=Path, default=Path("processed_data"))

    p_norm = sub.add_parser("contextualize", help="contextualize processed JSON into markdown via Groq")
    p_norm.add_argument("--in-dir", type=Path, default=Path("processed_data"))
    p_norm.add_argument("--out-dir", type=Path, default=Path("contextualized_data"))
    p_norm.add_argument("--model", type=str, default="llama-3.3-70b-versatile")

    p_all = sub.add_parser("all", help="Run extract-root, strip-ui, parse, contextualize")
    p_all.add_argument("--raw-dir", type=Path, default=Path("raw_data"))
    p_all.add_argument("--clean-dir", type=Path, default=Path("clean_data"))
    p_all.add_argument("--processed-dir", type=Path, default=Path("processed_data"))
    p_all.add_argument("--contextualized-dir", type=Path, default=Path("contextualized_data"))
    p_all.add_argument("--model", type=str, default="llama-3.3-70b-versatile")

    args = parser.parse_args()

    if args.cmd == "extract-root":
        run_extract_root(args.raw_dir, args.out_dir)
    elif args.cmd == "strip-ui":
        run_strip_ui(args.in_dir, args.out_dir)
    elif args.cmd == "parse":
        run_parse(args.raw_dir, args.out_dir)
    elif args.cmd == "contextualize":
        run_contextualize(args.in_dir, args.out_dir, model=args.model)
    elif args.cmd == "all":
        run_extract_root(args.raw_dir, args.clean_dir)
        run_strip_ui(args.clean_dir, args.clean_dir)  # overwrite
        run_parse(args.clean_dir, args.processed_dir)
        run_contextualize(args.processed_dir, args.contextualized_dir, model=args.model)
