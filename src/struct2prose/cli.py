import argparse
import os
from pathlib import Path
import uuid

from struct2prose.persistence.db import connect, init_db
from struct2prose.persistence.store import create_pipeline_run, finish_pipeline_run
from struct2prose.steps.step0_fetch_xwiki import fetch_xwiki_pages
from struct2prose.steps.step1_extract_root import run as run_extract_root
from struct2prose.steps.step2_strip_ui import run as run_strip_ui
from struct2prose.steps.step3_parse import run as run_parse
from struct2prose.steps.step4_contextualize import run as run_contextualize
from struct2prose.steps.step5_ingest_qdrant import run as run_ingest_qdrant
from struct2prose.config import Config
from struct2prose.steps.step4_baseline import run as run_baseline

PIPELINE_VERSION = "v1"
DB_PATH_DEFAULT= Path("state/struct2prose.db")

def main() -> None:
    Config.validate()
    parser = argparse.ArgumentParser(prog="struct2prose")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_fetch = sub.add_parser("fetch-xwiki", help="Fetch XWiki pages as raw HTML")
    p_fetch.add_argument("--base-url", type=str, default=os.getenv("XWIKI_BASE_URL"))
    p_fetch.add_argument("--wiki-id", type=str, default="xwiki")
    p_fetch.add_argument("--raw-dir", type=Path, default=Path("raw_data"))
    p_fetch.add_argument("--username", type=str, default=None)
    p_fetch.add_argument("--password", type=str, default=None)
    p_fetch.add_argument("--include-space", action="append", default=None, help="Only fetch pages from this top-level XWiki space. Can be used multiple times.")

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
    p_all.add_argument("--base-url", type=str, default=os.getenv("XWIKI_BASE_URL"))
    p_all.add_argument("--wiki-id", type=str, default="xwiki")
    p_all.add_argument("--username", type=str, default=None)
    p_all.add_argument("--password", type=str, default=None)
    p_all.add_argument("--raw-dir", type=Path, default=Path("raw_data"))
    p_all.add_argument("--clean-dir", type=Path, default=Path("clean_data"))
    p_all.add_argument("--stripped-dir", type=Path, default=Path("stripped_data"))
    p_all.add_argument("--processed-dir", type=Path, default=Path("processed_data"))
    p_all.add_argument("--contextualized-dir", type=Path, default=Path("contextualized_data"))
    p_all.add_argument("--model", type=str, default=Config.get_model_name())
    p_all.add_argument("--db-path", type=Path, default=DB_PATH_DEFAULT)
    p_all.add_argument("--pipeline-version", type=str, default=PIPELINE_VERSION)
    p_all.add_argument("--include-space", action="append", default=["Dummy-Content"], help="Only fetch pages from this top-level XWiki space. Can be used multiple times.")

    p_ingest = sub.add_parser("ingest-qdrant", help="Ingest contextualized documents into Qdrant")
    p_ingest.add_argument("--contextualized-dir", type=Path, default=Path("contextualized_data"))
    p_ingest.add_argument("--db-path", type=Path, default=DB_PATH_DEFAULT)

    p_all_eval = sub.add_parser("all-eval", help="Run evaluation pipeline with contextualized and baseline collections")
    p_all_eval.add_argument("--base-url", type=str, default=os.getenv("XWIKI_BASE_URL"))
    p_all_eval.add_argument("--wiki-id", type=str, default="xwiki")
    p_all_eval.add_argument("--username", type=str, default=None)
    p_all_eval.add_argument("--password", type=str, default=None)
    p_all_eval.add_argument("--raw-dir", type=Path, default=Path("raw_data"))
    p_all_eval.add_argument("--clean-dir", type=Path, default=Path("clean_data"))
    p_all_eval.add_argument("--stripped-dir", type=Path, default=Path("stripped_data"))
    p_all_eval.add_argument("--processed-dir", type=Path, default=Path("processed_data"))
    p_all_eval.add_argument("--contextualized-dir", type=Path, default=Path("contextualized_data"))
    p_all_eval.add_argument("--baseline-dir", type=Path, default=Path("baseline_data"))
    p_all_eval.add_argument("--model", type=str, default=Config.get_model_name())
    p_all_eval.add_argument("--db-path", type=Path, default=DB_PATH_DEFAULT)
    p_all_eval.add_argument("--pipeline-version", type=str, default=PIPELINE_VERSION)
    p_all_eval.add_argument("--include-space", action="append", default=["Dummy-Content"])

    args = parser.parse_args()

    # state directory / DB file vorbereiten
    args.db_path.parent.mkdir(parents=True, exist_ok=True)

    # DB immer initialisieren, damit Schema sicher vorhanden ist
    with connect(args.db_path) as conn:
        init_db(conn)

    if args.cmd == "fetch-xwiki":
        fetch_xwiki_pages(
            wiki_base_url=args.base_url,
            wiki_id=args.wiki_id,
            raw_dir=args.raw_dir,
            username=args.username,
            password=args.password,
            include_spaces=set(args.include_space) if args.include_space else None
        )
    elif args.cmd == "extract-root":
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
    elif args.cmd == "ingest-qdrant":
        run_ingest_qdrant(
            args.contextualized_dir
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
            fetch_xwiki_pages(
                wiki_base_url=args.base_url,
                wiki_id=args.wiki_id,
                raw_dir=args.raw_dir,
                username=args.username,
                password=args.password,
                include_spaces=set(args.include_space) if args.include_space else None
            )
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
            run_ingest_qdrant(
                args.contextualized_dir
            )
            with connect(args.db_path) as conn:
                finish_pipeline_run(conn, run_id, "completed")

        except Exception:
            with connect(args.db_path) as conn:
                finish_pipeline_run(conn, run_id, "failed")
            raise

    elif args.cmd == "all-eval":
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
            fetch_xwiki_pages(
                wiki_base_url=args.base_url,
                wiki_id=args.wiki_id,
                raw_dir=args.raw_dir,
                username=args.username,
                password=args.password,
                include_spaces=set(args.include_space) if args.include_space else None
            )
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
            run_baseline(
                args.processed_dir,
                args.baseline_dir,
                pipeline_version=args.pipeline_version,
                run_id=run_id,
                db_path=args.db_path,
            )
            run_ingest_qdrant(
                args.contextualized_dir,
                Config.QDRANT_CONTEXTUALIZED_COLLECTION,
            )

            run_ingest_qdrant(
                args.baseline_dir,
                Config.QDRANT_BASELINE_COLLECTION,
            )
            with connect(args.db_path) as conn:
                finish_pipeline_run(conn, run_id, "completed")

        except Exception:
            with connect(args.db_path) as conn:
                finish_pipeline_run(conn, run_id, "failed")
            raise