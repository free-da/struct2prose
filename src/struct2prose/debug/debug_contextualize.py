from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from struct2prose.config import Config
from struct2prose.models.documents import ContextualizationTask
from struct2prose.parser.models import ContentBlock, Section, WikiDocument
from struct2prose.steps.step4_contextualize import (
    _execute_task,
    _is_contextualizable,
    _prompt_for_block,
    _wiki_document_from_json,
)


class Step4ContextualizeDebugger:
    def __init__(self, *, model: str | None = None) -> None:
        self.model = model or Config.get_model_name()

    def debug_file(
        self,
        file: Path,
        *,
        block_id: str | None = None,
        show_all_blocks: bool = False,
    ) -> None:
        doc = self._load_processed_document(file)

        print("\n=== DOCUMENT ===")
        print(f"Title: {doc.metadata.title}")
        print(f"Source ID: {doc.metadata.source_id}")
        print(f"File: {file}")

        if show_all_blocks:
            self._print_block_overview(doc)
            return

        if block_id:
            section, block = self._find_block(doc, block_id)
            self._debug_block(doc, section, block)
            return

        self._debug_all_contextualizable_blocks(doc)

    def _load_processed_document(self, file: Path) -> WikiDocument:
        if not file.exists():
            raise FileNotFoundError(f"Processed file not found: {file}")

        data: dict[str, Any] = json.loads(file.read_text(encoding="utf-8"))

        return _wiki_document_from_json(
            data=data,
            source_file=file.name,
        )

    def _print_block_overview(self, doc: WikiDocument) -> None:
        print("\n=== BLOCK OVERVIEW ===")

        for section in doc.sections:
            print(f"\n## {section.heading} ({section.section_id})")

            for block in section.blocks:
                status = (
                    "contextualizable"
                    if _is_contextualizable(block, section)
                    else "passthrough"
                )

                preview = self._preview_block(block)

                print(
                    f"- {block.block_id} | "
                    f"type={block.block_type} | "
                    f"{status} | "
                    f"{preview}"
                )

    def _debug_all_contextualizable_blocks(self, doc: WikiDocument) -> None:
        found = False

        for section in doc.sections:
            for block in section.blocks:
                if _is_contextualizable(block, section):
                    found = True
                    self._debug_block(doc, section, block)

        if not found:
            print("\nNo contextualizable blocks found.")

    def _find_block(
        self,
        doc: WikiDocument,
        block_id: str,
    ) -> tuple[Section, ContentBlock]:
        for section in doc.sections:
            for block in section.blocks:
                if block.block_id == block_id:
                    return section, block

        raise ValueError(f"Block not found: {block_id}")

    def _debug_block(
        self,
        doc: WikiDocument,
        section: Section,
        block: ContentBlock,
    ) -> None:
        print("\n" + "=" * 80)
        print("=== BLOCK ===")
        print(f"Section: {section.heading}")
        print(f"Section ID: {section.section_id}")
        print(f"Section anchor: {section.anchor}")
        print(f"Block ID: {block.block_id}")
        print(f"Block type: {block.block_type}")
        print(f"Contextualizable: {_is_contextualizable(block, section)}")

        print("\n=== INPUT BLOCK ===")
        print(self._format_block_content(block))

        if not _is_contextualizable(block, section):
            print("\n=== SKIPPED ===")
            print("Block is not contextualizable by step4.")
            return

        prompt = _prompt_for_block(doc, section, block)

        print("\n=== GENERATED PROMPT ===")
        print(prompt)

        task = ContextualizationTask(
            task_id=f"debug:{doc.metadata.source_id}:{section.section_id}:{block.block_id}",
            source_id=doc.metadata.source_id,
            pipeline_run_id=None,
            source_block_id=block.block_id,
            section_id=section.section_id,
            section_heading=section.heading,
            block_type=block.block_type,
            strategy="debug",
            prompt_name="debug_contextualization",
            prompt_version="debug",
            model_name=self.model,
        )

        result = _execute_task(
            doc=doc,
            section=section,
            block=block,
            task=task,
            model=self.model,
        )

        print("\n=== LLM OUTPUT ===")
        if result.status == "completed":
            print(result.contextualized_text)
        else:
            print(f"FAILED: {result.error_message}")

    def _format_block_content(self, block: ContentBlock) -> str:
        if block.block_type == "table":
            rows = block.content or []
            return "\n".join(
                " | ".join(str(cell) for cell in row)
                for row in rows
            )

        if block.block_type == "list":
            return "\n".join(f"- {item}" for item in block.content or [])

        return str(block.content)

    def _preview_block(self, block: ContentBlock, max_len: int = 120) -> str:
        text = self._format_block_content(block).replace("\n", " ")
        return text[:max_len] + ("..." if len(text) > max_len else "")