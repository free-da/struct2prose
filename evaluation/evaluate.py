from __future__ import annotations

import argparse
import csv
import json
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import re
import requests


MODELS = ("struct2prose-rag", "baseline-rag")
TOP_K = 3


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
""".strip())

MARKDOWN_LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def split_answer_and_sources(answer: str) -> tuple[str, list[tuple[str, str]]]:
    """
    Trennt den eigentlichen Antworttext von einem Markdown-Quellenblock.

    Erwartetes Format:

    Antworttext

    ## Quellen
    - [Titel](URL)
    """
    parts = re.split(
        r"(?im)^\s*#{1,6}\s*Quellen\s*$",
        answer,
        maxsplit=1,
    )

    answer_text = parts[0].strip()
    sources: list[tuple[str, str]] = []

    if len(parts) == 2:
        source_block = parts[1]

        for label, url in MARKDOWN_LINK_PATTERN.findall(source_block):
            sources.append((label.strip(), url.strip()))

    return answer_text, sources

def answer_sources_to_latex(sources: list[tuple[str, str]]) -> str:
    if not sources:
        return r"\textbf{Angegebene Quellen:} Keine auswertbare Quellenangabe."

    source_lines = []

    for label, url in sources:
        escaped_label = latex_escape(label)

        # Prozentzeichen in URLs dürfen in LaTeX nicht als Kommentar beginnen.
        escaped_url = url.replace("%", r"\%")

        source_lines.append(
            rf"\item \href{{{escaped_url}}}{{{escaped_label}}}"
        )

    items = "\n".join(source_lines)

    return rf"""
\textbf{{Angegebene Quellen:}}
\begin{{itemize}}
{items}
\end{{itemize}}
""".strip()

def answer_to_latex(answer: str) -> str:
    answer_text, sources = split_answer_and_sources(answer)

    sources_latex = answer_sources_to_latex(sources)

    return rf"""
\begin{{lstlisting}}[style=EvaluationAnswer]
{answer_text}
\end{{lstlisting}}

{sources_latex}
""".strip()

def model_result_to_latex(result: ModelResult) -> str:
    if result.error:
        body = rf"""
        \textbf{{Fehler}}

        \begin{{lstlisting}}[style=EvaluationChunk]
        {result.error}
        \end{{lstlisting}}
        """.strip()
    else:
        chunks = "\n\n".join(
            chunk_to_latex(chunk)
            for chunk in result.chunks
        )

        answer_latex = answer_to_latex(result.answer)

        body = rf"""
\textbf{{Antwort}}
{answer_latex}

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

        \subsection*{{Untersuchungssystem: struct2prose-rag}}

        {model_result_to_latex(struct_result)}

        \subsection*{{Referenzsystem: baseline-rag}}

        {model_result_to_latex(baseline_result)}

        """.strip())

    content = "\n\n\\clearpage\n\n".join(blocks)

    return rf"""\documentclass[a4paper,10pt]{{article}}

\usepackage[ngerman]{{babel}}
\usepackage{{geometry}}
\usepackage{{parskip}}
\usepackage{{hyperref}}
\usepackage{{xurl}}
\usepackage{{microtype}}
\usepackage{{listings}}
\usepackage{{array}}
\usepackage{{booktabs}}
\usepackage{{xcolor}}

\geometry{{margin=18mm}}
\hypersetup{{hidelinks}}
\setlength{{\emergencystretch}}{{3em}}

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

\lstdefinestyle{{EvaluationAnswer}}{{
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
  aboveskip=0.8em,
  belowskip=0.8em,
  framesep=10pt,
  rulecolor=\color{{black}},
  backgroundcolor=\color{{black!4}}
}}

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



def write_ratings_csv(path: Path, questions: list[dict[str, str]]) -> None:
    fieldnames = [
        "Frage-ID",
        "Frage",
        "System",
        "Modell",
        "Relevanz Chunk 1 (0-2)",
        "Relevanz Chunk 2 (0-2)",
        "Relevanz Chunk 3 (0-2)",
        "Fachliche Korrektheit (0-2)",
        "Vollständigkeit (0-2)",
        "Fragebezug (0-2)",
        "Quellennachvollziehbarkeit (0-2)",
        "Bemerkungen",
    ]

    with path.open("w", encoding="utf-8-sig", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()

        system_names = {
            "struct2prose-rag": "Untersuchungssystem",
            "baseline-rag": "Referenzsystem",
        }

        for entry in questions:
            for model in MODELS:
                writer.writerow({
                    "Frage-ID": entry["id"],
                    "Frage": entry["question"],
                    "System": system_names[model],
                    "Modell": model,
                    "Relevanz Chunk 1 (0-2)": "",
                    "Relevanz Chunk 2 (0-2)": "",
                    "Relevanz Chunk 3 (0-2)": "",
                    "Fachliche Korrektheit (0-2)": "",
                    "Vollständigkeit (0-2)": "",
                    "Fragebezug (0-2)": "",
                    "Quellennachvollziehbarkeit (0-2)": "",
                    "Bemerkungen": "",
                })

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare struct2prose-rag and baseline-rag and export LaTeX and a ratings CSV."
    )
    parser.add_argument("--base-url", default="http://127.0.0.1:8000")
    parser.add_argument("--questions", type=Path, default=Path("questions.json"))
    parser.add_argument("--output-dir", type=Path, default=Path("evaluation_results"))
    parser.add_argument("--timeout", type=int, default=300)
    args = parser.parse_args()

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
                top_k=TOP_K,
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
        "top_k": TOP_K,
        "models": list(MODELS),
        "questions": [asdict(item) for item in all_results],
    }

    json_path = args.output_dir / "evaluation_results.json"
    tex_path = args.output_dir / "evaluation_results.tex"
    ratings_csv_path = args.output_dir / "ratings.csv"

    json_path.write_text(
        json.dumps(raw_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    tex_path.write_text(
        render_latex(all_results, generated_at, TOP_K),
        encoding="utf-8",
    )
    write_ratings_csv(ratings_csv_path, questions)

    errors = [
        result.error
        for question in all_results
        for result in question.results.values()
        if result.error
    ]

    print(f"Wrote {json_path}")
    print(f"Wrote {tex_path}")
    print(f"Wrote {ratings_csv_path}")

    if errors:
        print(f"Completed with {len(errors)} failed model calls.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())