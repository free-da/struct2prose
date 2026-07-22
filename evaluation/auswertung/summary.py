from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


DELIMITER = ";"

QUESTION_ID = "Frage-ID"
QUESTION = "Frage"
SYSTEM = "System"
MODEL = "Modell"
COMMENTS = "Bemerkungen"

RETRIEVAL_CRITERIA = (
    "Relevanz Chunk 1 (0-2)",
    "Relevanz Chunk 2 (0-2)",
    "Relevanz Chunk 3 (0-2)",
)

ANSWER_CRITERIA = (
    "Fachliche Korrektheit (0-2)",
    "Vollständigkeit (0-2)",
    "Fragebezug (0-2)",
    "Quellennachvollziehbarkeit (0-2)",
)

EXPECTED_SYSTEMS = (
    ("Untersuchungssystem", "struct2prose-rag"),
    ("Referenzsystem", "baseline-rag"),
)

RETRIEVAL_MAX_PER_ROW = len(RETRIEVAL_CRITERIA) * 2
ANSWER_MAX_PER_ROW = len(ANSWER_CRITERIA) * 2
TOTAL_MAX_PER_ROW = RETRIEVAL_MAX_PER_ROW + ANSWER_MAX_PER_ROW


@dataclass(frozen=True)
class ScoredRow:
    question_id: str
    question: str
    system: str
    model: str
    retrieval_score: int
    answer_score: int
    total_score: int
    comments: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validiert eine ausgefüllte ratings.csv und berechnet Retrieval-, "
            "Antwort- und Gesamtscores."
        )
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("ratings.csv"),
        help="Ausgefüllte Bewertungsdatei (Standard: ratings.csv)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("summary.csv"),
        help="Zieldatei für die Auswertung (Standard: summary.csv)",
    )
    return parser.parse_args()


def read_ratings(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    if not path.is_file():
        raise ValueError(f"Eingabedatei nicht gefunden: {path.resolve()}")

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, delimiter=DELIMITER)
        fieldnames = reader.fieldnames or []
        rows = [
            {key: (value or "").strip() for key, value in row.items() if key is not None}
            for row in reader
        ]

    if not rows:
        raise ValueError("Die Eingabedatei enthält keine Bewertungszeilen.")

    return rows, fieldnames


def validate_columns(fieldnames: list[str]) -> None:
    required = {
        QUESTION_ID,
        QUESTION,
        SYSTEM,
        MODEL,
        COMMENTS,
        *RETRIEVAL_CRITERIA,
        *ANSWER_CRITERIA,
    }
    missing = sorted(required.difference(fieldnames))
    if missing:
        raise ValueError("Fehlende Spalten: " + ", ".join(missing))


def parse_score(row_number: int, row: dict[str, str], column: str) -> int:
    raw = row.get(column, "").strip()
    if raw == "":
        raise ValueError(
            f"Zeile {row_number}: Bewertung in '{column}' fehlt."
        )

    try:
        value = int(raw)
    except ValueError as exc:
        raise ValueError(
            f"Zeile {row_number}: '{raw}' in '{column}' ist keine ganze Zahl."
        ) from exc

    if value not in (0, 1, 2):
        raise ValueError(
            f"Zeile {row_number}: Wert {value} in '{column}' liegt nicht zwischen 0 und 2."
        )

    return value


def validate_structure(rows: list[dict[str, str]]) -> None:
    errors: list[str] = []

    question_ids = [row.get(QUESTION_ID, "") for row in rows]
    counts = Counter(question_ids)

    if "" in counts:
        errors.append("Mindestens eine Zeile enthält keine Frage-ID.")

    for question_id, count in counts.items():
        if question_id and count != 2:
            errors.append(
                f"Frage {question_id} kommt {count}-mal statt genau zweimal vor."
            )

    grouped: dict[str, list[tuple[int, dict[str, str]]]] = defaultdict(list)
    for row_number, row in enumerate(rows, start=2):
        grouped[row.get(QUESTION_ID, "")].append((row_number, row))

    expected_pairs = list(EXPECTED_SYSTEMS)
    for question_id, entries in grouped.items():
        if not question_id or len(entries) != 2:
            continue

        questions = {row.get(QUESTION, "") for _, row in entries}
        if "" in questions:
            errors.append(f"Frage {question_id} enthält einen leeren Fragetext.")
        elif len(questions) != 1:
            errors.append(
                f"Frage {question_id} besitzt in den beiden Zeilen unterschiedliche Fragetexte."
            )

        actual_pairs = [
            (row.get(SYSTEM, ""), row.get(MODEL, ""))
            for _, row in entries
        ]
        if actual_pairs != expected_pairs:
            errors.append(
                f"Frage {question_id}: Erwartet wird zuerst "
                "Untersuchungssystem/struct2prose-rag und danach "
                "Referenzsystem/baseline-rag."
            )

    if errors:
        raise ValueError("\n".join(errors))


def score_rows(rows: list[dict[str, str]]) -> list[ScoredRow]:
    scored: list[ScoredRow] = []

    for row_number, row in enumerate(rows, start=2):
        retrieval_score = sum(
            parse_score(row_number, row, column)
            for column in RETRIEVAL_CRITERIA
        )
        answer_score = sum(
            parse_score(row_number, row, column)
            for column in ANSWER_CRITERIA
        )

        scored.append(
            ScoredRow(
                question_id=row[QUESTION_ID],
                question=row[QUESTION],
                system=row[SYSTEM],
                model=row[MODEL],
                retrieval_score=retrieval_score,
                answer_score=answer_score,
                total_score=retrieval_score + answer_score,
                comments=row.get(COMMENTS, ""),
            )
        )

    return scored


def percentage(score: int, maximum: int) -> str:
    return f"{score / maximum * 100:.2f}"


def write_summary(path: Path, scored_rows: list[ScoredRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "Frage-ID",
        "Frage",
        "System",
        "Modell",
        "Retrievalscore",
        "Retrieval-Maximum",
        "Retrieval-Prozent",
        "Antwortscore",
        "Antwort-Maximum",
        "Antwort-Prozent",
        "Gesamtscore",
        "Gesamt-Maximum",
        "Gesamt-Prozent",
        "Bemerkungen",
    ]

    grouped: dict[tuple[str, str], list[ScoredRow]] = defaultdict(list)
    for row in scored_rows:
        grouped[(row.system, row.model)].append(row)

    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            delimiter=DELIMITER,
            extrasaction="ignore",
        )
        writer.writeheader()

        for row in scored_rows:
            writer.writerow(
                {
                    "Frage-ID": row.question_id,
                    "Frage": row.question,
                    "System": row.system,
                    "Modell": row.model,
                    "Retrievalscore": row.retrieval_score,
                    "Retrieval-Maximum": RETRIEVAL_MAX_PER_ROW,
                    "Retrieval-Prozent": percentage(
                        row.retrieval_score, RETRIEVAL_MAX_PER_ROW
                    ),
                    "Antwortscore": row.answer_score,
                    "Antwort-Maximum": ANSWER_MAX_PER_ROW,
                    "Antwort-Prozent": percentage(
                        row.answer_score, ANSWER_MAX_PER_ROW
                    ),
                    "Gesamtscore": row.total_score,
                    "Gesamt-Maximum": TOTAL_MAX_PER_ROW,
                    "Gesamt-Prozent": percentage(
                        row.total_score, TOTAL_MAX_PER_ROW
                    ),
                    "Bemerkungen": row.comments,
                }
            )

        for system, model in EXPECTED_SYSTEMS:
            system_rows = grouped[(system, model)]
            question_count = len(system_rows)
            retrieval_score = sum(row.retrieval_score for row in system_rows)
            answer_score = sum(row.answer_score for row in system_rows)
            total_score = sum(row.total_score for row in system_rows)

            retrieval_max = question_count * RETRIEVAL_MAX_PER_ROW
            answer_max = question_count * ANSWER_MAX_PER_ROW
            total_max = question_count * TOTAL_MAX_PER_ROW

            writer.writerow(
                {
                    "Frage-ID": "GESAMT",
                    "Frage": f"Gesamtergebnis über {question_count} Fragen",
                    "System": system,
                    "Modell": model,
                    "Retrievalscore": retrieval_score,
                    "Retrieval-Maximum": retrieval_max,
                    "Retrieval-Prozent": percentage(
                        retrieval_score, retrieval_max
                    ),
                    "Antwortscore": answer_score,
                    "Antwort-Maximum": answer_max,
                    "Antwort-Prozent": percentage(answer_score, answer_max),
                    "Gesamtscore": total_score,
                    "Gesamt-Maximum": total_max,
                    "Gesamt-Prozent": percentage(total_score, total_max),
                    "Bemerkungen": "",
                }
            )


def print_system_totals(scored_rows: list[ScoredRow]) -> None:
    grouped: dict[tuple[str, str], list[ScoredRow]] = defaultdict(list)
    for row in scored_rows:
        grouped[(row.system, row.model)].append(row)

    print(f"Gefundene Fragen: {len(scored_rows) // 2}")
    print(f"Gefundene Bewertungszeilen: {len(scored_rows)}")
    print("Validierung erfolgreich.\n")

    for system, model in EXPECTED_SYSTEMS:
        rows = grouped[(system, model)]
        retrieval = sum(row.retrieval_score for row in rows)
        answer = sum(row.answer_score for row in rows)
        total = sum(row.total_score for row in rows)
        total_max = len(rows) * TOTAL_MAX_PER_ROW

        print(f"{system} ({model})")
        print(f"  Retrieval: {retrieval}/{len(rows) * RETRIEVAL_MAX_PER_ROW}")
        print(f"  Antwort:   {answer}/{len(rows) * ANSWER_MAX_PER_ROW}")
        print(
            f"  Gesamt:    {total}/{total_max} "
            f"({percentage(total, total_max)} %)"
        )


def main() -> int:
    args = parse_args()

    try:
        rows, fieldnames = read_ratings(args.input)
        validate_columns(fieldnames)
        validate_structure(rows)
        scored_rows = score_rows(rows)
        write_summary(args.output, scored_rows)
    except (OSError, ValueError) as exc:
        print(f"Fehler: {exc}", file=sys.stderr)
        return 1

    print(f"Eingabedatei: {args.input.resolve()}")
    print(f"Ausgabedatei: {args.output.resolve()}\n")
    print_system_totals(scored_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
