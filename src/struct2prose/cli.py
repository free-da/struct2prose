import argparse
from pathlib import Path

from struct2prose.steps.step1_extract_root import run as run_step1
from struct2prose.steps.step3_parse import run as run_step3


def main() -> None:
    parser = argparse.ArgumentParser(prog="struct2prose")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_root = sub.add_parser("extract-root", help="Extract XWiki main content into clean HTML")
    p_root.add_argument("--raw-dir", type=Path, default=Path("raw_data"))
    p_root.add_argument("--out-dir", type=Path, default=Path("clean_data"))

    p_parse = sub.add_parser("parse", help="Parse clean HTML to processed JSON")
    p_parse.add_argument("--raw-dir", type=Path, default=Path("clean_data"))
    p_parse.add_argument("--out-dir", type=Path, default=Path("processed_data"))

    p_all = sub.add_parser("all", help="Run extract-root and parse")
    p_all.add_argument("--raw-dir", type=Path, default=Path("raw_data"))
    p_all.add_argument("--clean-dir", type=Path, default=Path("clean_data"))
    p_all.add_argument("--out-dir", type=Path, default=Path("processed_data"))

    args = parser.parse_args()

    if args.cmd == "extract-root":
        run_step1(args.raw_dir, args.out_dir)
    elif args.cmd == "parse":
        run_step3(args.raw_dir, args.out_dir)
    elif args.cmd == "all":
        run_step1(args.raw_dir, args.clean_dir)
        run_step3(args.clean_dir, args.out_dir)
