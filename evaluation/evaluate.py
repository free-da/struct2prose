from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests


MODELS = ("struct2prose-rag", "baseline-rag")


@dataclass
class ChunkResult:
    rank: int
    score: float
    text: str
    title: str | None
    section_heading: str | None
    section_url: str | None
    source_id: str | None
    source_block_id: str | None
    transformation: str | None


@dataclass
class ModelResult:
    model: str
    answer: str
    chunks: list[ChunkResult]
    finish_reason: str | None
    duration_seconds: float
    error: str | None = None


@dataclass
class QuestionResult:
    question_id: str
    question: str
    results: dict[str, ModelResult]


LATEX_REPLACEMENTS = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def latex_escape(value: Any) -> str:
    text = "" if value is None else str(value)
    return "".join(LATEX_REPLACEMENTS.get(char, char) for char in text)


def load_questions(path: Path) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    questions = data.get("questions")
    if not isinstance(questions, list) or not questions:
        raise ValueError("questions.json must contain a non-empty 'questions' list.")

    normalized = []
    for index, entry in enumerate(questions, start=1):
        question = str(entry.get("question", "")).strip()
        if not question:
            raise ValueError(f"Question {index} is empty.")
        normalized.append({
            "id": str(entry.get("id") or f"F{index:02d}"),
            "question": question,
        })
    return normalized


def ask_model(
    session: requests.Session,
    *,
    base_url: str,
    model: str,
    question: str,
    top_k: int,
    timeout: int,
) -> ModelResult:
    started = time.perf_counter()
    try:
        response = session.post(
            f"{base_url.rstrip('/')}/v1/chat/completions",
            json={
                "model": model,
                "messages": [{"role": "user", "content": question}],
                "temperature": 0.0,
                "stream": False,
                "top_k": top_k,
            },
            timeout=timeout,
        )
        response.raise_for_status()
        data = response.json()

        choice = data["choices"][0]
        answer = str(choice["message"]["content"]).strip()
        finish_reason = choice.get("finish_reason")

        raw_chunks = data.get("retrieval", {}).get("chunks", [])
        chunks = []
        for raw in raw_chunks:
            payload = raw.get("payload") or {}
            chunks.append(
                ChunkResult(
                    rank=int(raw.get("rank", len(chunks) + 1)),
                    score=float(raw.get("score", 0.0)),
                    text=str(raw.get("text", "")).strip(),
                    title=payload.get("title"),
                    section_heading=payload.get("section_heading"),
                    section_url=payload.get("section_url") or payload.get("xwiki_url"),
                    source_id=payload.get("source_id"),
                    source_block_id=payload.get("source_block_id"),
                    transformation=payload.get("transformation"),
                )
            )

        if len(chunks) != top_k:
            raise RuntimeError(
                f"Expected {top_k} retrieval chunks, received {len(chunks)}. "
                "Install the supplied API patch."
            )

        return ModelResult(
            model=model,
            answer=answer,
            chunks=chunks,
            finish_reason=finish_reason,
            duration_seconds=round(time.perf_counter() - started, 3),
        )
    except Exception as exc:
        return ModelResult(
            model=model,
            answer="",
            chunks=[],
            finish_reason=None,
            duration_seconds=round(time.perf_counter() - started, 3),
            error=f"{type(exc).__name__}: {exc}",
        )


def chunk_to_latex(chunk: ChunkResult) -> str:
    title = latex_escape(chunk.title or "Unbekanntes Dokument")
    section = latex_escape(chunk.section_heading or "Unbekannter Abschnitt")
    source_id = latex_escape(chunk.source_id or "")
    block_id = latex_escape(chunk.source_block_id or "")
    transformation = latex_escape(chunk.transformation or "")
    url = chunk.section_url

    source_line = f"{title} -- {section}"

    if url:
        source_line = rf"\href{{{url}}}{{{source_line}}}"

    return (rf"""
\begin{{lstlisting}}[style=EvaluationChunk]
Chunk:          {chunk.rank}
Score:          {chunk.score:.4f}
Quelle:         {title} -- {section}
Source-ID:      {source_id}
Block-ID:       {block_id}
Transformation: {transformation}

------------------------------------------------------------

{chunk.text}
\end{{lstlisting}}
\textbf{{Quelle:}} {source_line}
""".strip())


def model_result_to_latex(result: ModelResult) -> str:
    if result.error:
        body = rf"\EvaluationError{{{latex_escape(result.error)}}}"
    else:
        chunks = "\n\n".join(chunk_to_latex(chunk) for chunk in result.chunks)
        body = rf"""
\begin{{EvaluationAnswer}}
{latex_escape(result.answer)}
\end{{EvaluationAnswer}}

\textbf{{Laufzeit:}} {result.duration_seconds:.3f}\,s \qquad
\textbf{{Finish reason:}} \texttt{{{latex_escape(result.finish_reason or "")}}}

\subsubsection*{{Top-{len(result.chunks)}-Chunks}}
{chunks}
""".strip()

    return body


def render_latex(results: list[QuestionResult], generated_at: str, top_k: int) -> str:
    blocks = []
    for item in results:
        struct_result = item.results["struct2prose-rag"]
        baseline_result = item.results["baseline-rag"]

        blocks.append(rf"""
        \section{{{latex_escape(item.question_id)}: {latex_escape(item.question)}}}

        \subsection*{{struct2prose-rag}}

        {model_result_to_latex(struct_result)}

        \subsection*{{baseline-rag}}

        {model_result_to_latex(baseline_result)}
        """.strip())

    content = "\n\n\\clearpage\n\n".join(blocks)

    return rf"""\documentclass[a4paper,10pt]{{article}}

\usepackage[utf8]{{inputenc}}
\usepackage[T1]{{fontenc}}
\usepackage[ngerman]{{babel}}
\usepackage{{geometry}}
\usepackage{{parskip}}
\usepackage{{tcolorbox}}
\tcbuselibrary{{breakable}}
\usepackage{{hyperref}}
\usepackage{{xurl}}
\usepackage{{microtype}}\
\usepackage{{listings}}

\geometry{{margin=18mm}}
\hypersetup{{hidelinks}}
\setlength{{\emergencystretch}}{{3em}}\

\lstdefinestyle{{EvaluationChunk}}{{
  basicstyle=\ttfamily\small,
  frame=single,

  breaklines=true,
  breakatwhitespace=false,
  columns=flexible,
  keepspaces=true,
  showstringspaces=false,

  xleftmargin=1em,
  xrightmargin=1em,

  framexleftmargin=1em,
  framexrightmargin=1em,

  aboveskip=1.5em,
  belowskip=1.5em,

  framesep=8pt
}}

\newenvironment{{EvaluationAnswer}}
  {{\begin{{tcolorbox}}[title=Antwort,breakable,colback=white]}}
  {{\end{{tcolorbox}}}}

\newcommand{{\EvaluationError}}[1]{{%
  \begin{{tcolorbox}}[title=Fehler,breakable,colback=white]
  #1
  \end{{tcolorbox}}
}}

\title{{Vergleich struct2prose-rag und baseline-rag}}
\author{{Automatisierte Evaluation}}
\date{{{latex_escape(generated_at)}}}

\begin{{document}}
\maketitle

\noindent
Verglichene Modelle: \texttt{{struct2prose-rag}} und
\texttt{{baseline-rag}}. Pro Antwort wurden exakt Top-{top_k}-Chunks
für Retrieval und Generierung verwendet.

\tableofcontents
\clearpage

{content}

\end{{document}}
"""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare struct2prose-rag and baseline-rag and export LaTeX."
    )
    parser.add_argument("--base-url", default="http://127.0.0.1:8000")
    parser.add_argument("--questions", type=Path, default=Path("questions.json"))
    parser.add_argument("--output-dir", type=Path, default=Path("evaluation_results"))
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=300)
    args = parser.parse_args()

    if args.top_k < 1:
        parser.error("--top-k must be at least 1")

    questions = load_questions(args.questions)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    all_results: list[QuestionResult] = []

    for index, entry in enumerate(questions, start=1):
        print(f"[{index}/{len(questions)}] {entry['id']}: {entry['question']}")
        model_results = {}
        for model in MODELS:
            print(f"  -> {model}")
            model_results[model] = ask_model(
                session,
                base_url=args.base_url,
                model=model,
                question=entry["question"],
                top_k=args.top_k,
                timeout=args.timeout,
            )
        all_results.append(
            QuestionResult(
                question_id=entry["id"],
                question=entry["question"],
                results=model_results,
            )
        )

    generated_at = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    raw_data = {
        "generated_at": generated_at,
        "base_url": args.base_url,
        "top_k": args.top_k,
        "models": list(MODELS),
        "questions": [asdict(item) for item in all_results],
    }

    json_path = args.output_dir / "evaluation_results.json"
    tex_path = args.output_dir / "evaluation_results.tex"

    json_path.write_text(
        json.dumps(raw_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    tex_path.write_text(
        render_latex(all_results, generated_at, args.top_k),
        encoding="utf-8",
    )

    errors = [
        result.error
        for question in all_results
        for result in question.results.values()
        if result.error
    ]

    print(f"Wrote {json_path}")
    print(f"Wrote {tex_path}")

    if errors:
        print(f"Completed with {len(errors)} failed model calls.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
