import argparse
from pathlib import Path
import uuid

from struct2prose.persistence.db import connect, init_db
from struct2prose.persistence.store import create_pipeline_run, finish_pipeline_run
from struct2prose.steps.step1_extract_root import run as run_extract_root
from struct2prose.steps.step2_strip_ui import run as run_strip_ui
from struct2prose.steps.step3_parse import run as run_parse
from struct2prose.steps.step4_contextualize import run as run_contextualize
from struct2prose.config import Config

PIPELINE_VERSION = "v1"
DB_PATH_DEFAULT= Path("state/struct2prose.db")

def main() -> None:
    Config.validate()
    parser = argparse.ArgumentParser(prog="struct2prose")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_root = sub.add_parser("extract-root", help="Extract XWiki main content into clean HTML")
    p_root.add_argument("--raw-dir", type=Path, default=Path("raw_data"))
    p_root.add_argument("--clean-dir", type=Path, default=Path("clean_data"))
    p_root.add_argument("--pipeline-version", type=str, default=PIPELINE_VERSION)
    p_root.add_argument("--db-path", type=Path, default=DB_PATH_DEFAULT)


    p_ui = sub.add_parser("strip-ui", help="Remove remaining UI elements inside extracted content")
    p_ui.add_argument("--clean-dir", type=Path, default=Path("clean_data"))
    p_ui.add_argument("--stripped-dir", type=Path, default=Path("stripped_data"))
    p_ui.add_argument("--db-path", type=Path, default=DB_PATH_DEFAULT)
    p_ui.add_argument("--pipeline-version", type=str, default=PIPELINE_VERSION)

    p_parse = sub.add_parser("parse", help="Parse clean HTML to processed JSON")
    p_parse.add_argument("--stripped-dir", type=Path, default=Path("stripped_data"))
    p_parse.add_argument("--processed-dir", type=Path, default=Path("processed_data"))
    p_parse.add_argument("--pipeline-version", type=str, default=PIPELINE_VERSION)
    p_parse.add_argument("--db-path", type=Path, default=DB_PATH_DEFAULT)

    p_norm = sub.add_parser("contextualize", help="contextualize processed JSON into markdown via Groq")
    p_norm.add_argument("--processed-dir", type=Path, default=Path("processed_data"))
    p_norm.add_argument("--contextualized-dir", type=Path, default=Path("contextualized_data"))
    p_norm.add_argument("--model", type=str, default=Config.get_model_name())
    p_norm.add_argument("--db-path", type=Path, default=DB_PATH_DEFAULT)
    p_norm.add_argument("--pipeline-version", type=str, default=PIPELINE_VERSION)

    p_all = sub.add_parser("all", help="Run extract-root, strip-ui, parse, contextualize")
    p_all.add_argument("--raw-dir", type=Path, default=Path("raw_data"))
    p_all.add_argument("--clean-dir", type=Path, default=Path("clean_data"))
    p_all.add_argument("--stripped-dir", type=Path, default=Path("stripped_data"))
    p_all.add_argument("--processed-dir", type=Path, default=Path("processed_data"))
    p_all.add_argument("--contextualized-dir", type=Path, default=Path("contextualized_data"))
    p_all.add_argument("--model", type=str, default=Config.get_model_name())
    p_all.add_argument("--db-path", type=Path, default=DB_PATH_DEFAULT)
    p_all.add_argument("--pipeline-version", type=str, default=PIPELINE_VERSION)

    args = parser.parse_args()

    # state directory / DB file vorbereiten
    args.db_path.parent.mkdir(parents=True, exist_ok=True)

    # DB immer initialisieren, damit Schema sicher vorhanden ist
    with connect(args.db_path) as conn:
        init_db(conn)

    if args.cmd == "extract-root":
        run_extract_root(
            args.raw_dir,
            args.clean_dir,
            "xcontent",
            pipeline_version=args.pipeline_version,
            run_id=None,
            db_path=args.db_path,
        )
    elif args.cmd == "strip-ui":
        run_strip_ui(
            args.clean_dir,
            args.stripped_dir,
            pipeline_version=args.pipeline_version,
            run_id=None,
            db_path=args.db_path,
        )
    elif args.cmd == "parse":
        run_parse(
            args.stripped_dir,
            args.processed_dir,
            pipeline_version=args.pipeline_version,
            run_id=None,
            db_path=args.db_path,
        )
    elif args.cmd == "contextualize":
        run_contextualize(
            args.processed_dir,
            args.contextualized_dir,
            model=args.model,
            pipeline_version=args.pipeline_version,
            run_id=None,
            db_path=args.db_path,
        )
    elif args.cmd == "all":
        run_id = str(uuid.uuid4())

        with connect(args.db_path) as conn:
            create_pipeline_run(
                conn,
                run_id=run_id,
                pipeline_version=args.pipeline_version,
                llm_provider=Config.LLM_PROVIDER,
                model_name=args.model,
            )

        try:
            run_extract_root(
                args.raw_dir,
                args.clean_dir,
                "xcontent",
                pipeline_version=args.pipeline_version,
                run_id=run_id,
                db_path=args.db_path,
            )
            run_strip_ui(
                args.clean_dir,
                args.stripped_dir,
                pipeline_version=args.pipeline_version,
                run_id=run_id,
                db_path=args.db_path,
            )
            run_parse(
                args.stripped_dir,
                args.processed_dir,
                pipeline_version=args.pipeline_version,
                run_id=run_id,
                db_path=args.db_path,
            )
            run_contextualize(
                args.processed_dir,
                args.contextualized_dir,
                model=args.model,
                pipeline_version=args.pipeline_version,
                run_id=run_id,
                db_path=args.db_path,
            )
            with connect(args.db_path) as conn:
                finish_pipeline_run(conn, run_id, "completed")

        except Exception:
            with connect(args.db_path) as conn:
                finish_pipeline_run(conn, run_id, "failed")
            raise