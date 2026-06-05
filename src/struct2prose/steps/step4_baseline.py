import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from struct2prose.parser import ContentBlock
from struct2prose.persistence.db import connect
from struct2prose.persistence.store import create_step_run, create_document_version, finish_step_run
from struct2prose.steps.step4_contextualize import MODEL_DEFAULT, _wiki_document_from_json, _make_step_run_id, \
    _make_input_version_id

STEP_NAME = "baseline"

def _make_output_version_id(run_id: str, source_id: str) -> str:
    safe_source_id = source_id.replace(":", "_")
    return f"{run_id}:baseline_data:{safe_source_id}"

def _text_for_baseline_block(block: ContentBlock) -> str:
    if block.block_type == "paragraph":
        return str(block.content).strip()

    if block.block_type == "code":
        return "```\n" + str(block.content).strip() + "\n```"

    if block.block_type == "list":
        return "\n".join(f"- {item}" for item in block.content)

    if block.block_type == "table":
        rows = block.content
        return "\n".join(" | ".join(str(cell) for cell in row) for row in rows)

    return str(block.content).strip()

def run(
    processed_dir: Path,
    baseline_dir: Path,
    *,
    pipeline_version: str | None = None,
    run_id: str | None = None,
    db_path: Path | None = None,
markdown=None) -> None:
    baseline_dir.mkdir(parents=True, exist_ok=True)

    for file in sorted(processed_dir.glob("*.json")):
        data: dict[str, Any] = json.loads(file.read_text(encoding="utf-8"))
        doc = _wiki_document_from_json(data=data, source_file=file.name)

        doc.metadata.pipeline_version = pipeline_version or doc.metadata.pipeline_version
        doc.metadata.pipeline_run_id = run_id or doc.metadata.pipeline_run_id

        step_run_id = None
        output_version_id = None

        try:
            if run_id is not None and db_path is not None:
                step_run_id = _make_step_run_id(run_id, doc.metadata.source_id)
                input_version_id = _make_input_version_id(run_id, doc.metadata.source_id)

                with connect(db_path) as conn:
                    create_step_run(
                        conn,
                        step_run_id=step_run_id,
                        run_id=run_id,
                        source_id=doc.metadata.source_id,
                        step_name=STEP_NAME,
                        input_version_id=input_version_id,
                    )

            out_md_path = baseline_dir / f"{file.stem}.md"
            out_md_path.write_text(markdown, encoding="utf-8")

            out_json_path = baseline_dir / f"{file.stem}.baseline.json"
            out_json_path.write_text(
                json.dumps(
                    asdict(baseline_dir),
                    ensure_ascii=False,
                    indent=2,
                    default=str,
                ),
                encoding="utf-8",
            )

            if run_id is not None and db_path is not None:
                output_version_id = _make_output_version_id(run_id, doc.metadata.source_id)

                with connect(db_path) as conn:
                    create_document_version(
                        conn,
                        version_id=output_version_id,
                        source_id=doc.metadata.source_id,
                        run_id=run_id,
                        stage_name="contextualized_data",
                        artifact_path=out_json_path,
                    )
                    finish_step_run(
                        conn,
                        step_run_id=step_run_id,
                        status="completed",
                        output_version_id=output_version_id,
                    )

            print(f"[step4] wrote {out_md_path}")
            print(f"[step4] wrote {out_json_path}")

        except Exception as e:
            if run_id is not None and db_path is not None and step_run_id is not None:
                with connect(db_path) as conn:
                    finish_step_run(
                        conn,
                        step_run_id=step_run_id,
                        status="failed",
                        error_message=str(e),
                    )
            raise