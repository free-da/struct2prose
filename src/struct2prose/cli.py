import argparse
from pathlib import Path

from struct2prose.steps.step3_parse import run as run_step3


def main() -> None:
    parser = argparse.ArgumentParser(prog="struct2prose")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_parse = sub.add_parser("parse", help="Parse raw HTML to processed JSON")
    p_parse.add_argument("--raw-dir", type=Path, default=Path("raw_data"))
    p_parse.add_argument("--out-dir", type=Path, default=Path("processed_data"))

    args = parser.parse_args()

    if args.cmd == "parse":
        run_step3(args.raw_dir, args.out_dir)
