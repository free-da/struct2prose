# Version: 2026-07-22-corrected-order
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


@dataclass(frozen=True)
class SystemTotals:
    system: str
    model: str
    question_count: int
    retrieval_score: int
    answer_score: int
    total_score: int

    @property
    def retrieval_max(self) -> int:
        return self.question_count * RETRIEVAL_MAX_PER_ROW

    @property
    def answer_max(self) -> int:
        return self.question_count * ANSWER_MAX_PER_ROW

    @property
    def total_max(self) -> int:
        return self.question_count * TOTAL_MAX_PER_ROW

    @property
    def retrieval_average(self) -> float:
        return self.retrieval_score / self.question_count

    @property
    def answer_average(self) -> float:
        return self.answer_score / self.question_count

    @property
    def total_average(self) -> float:
        return self.total_score / self.question_count

    @property
    def retrieval_percent(self) -> float:
        return self.retrieval_score / self.retrieval_max * 100

    @property
    def answer_percent(self) -> float:
        return self.answer_score / self.answer_max * 100

    @property
    def total_percent(self) -> float:
        return self.total_score / self.total_max * 100


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
        help="Zieldatei für die Detailauswertung (Standard: summary.csv)",
    )
    parser.add_argument(
        "--totals-output",
        type=Path,
        default=Path("summary_totals.csv"),
        help="Zieldatei für aggregierte Ergebnisse (Standard: summary_totals.csv)",
    )
    parser.add_argument(
        "--latex-output",
        type=Path,
        default=Path("summary.tex"),
        help="Zieldatei für die LaTeX-Tabelle (Standard: summary.tex)",
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
        raise ValueError(f"Zeile {row_number}: Bewertung in '{column}' fehlt.")

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
            errors.append(f"Frage {question_id} kommt {count}-mal statt genau zweimal vor.")

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row.get(QUESTION_ID, "")].append(row)

    expected_pairs = list(EXPECTED_SYSTEMS)
    for question_id, entries in grouped.items():
        if not question_id or len(entries) != 2:
            continue

        questions = {row.get(QUESTION, "") for row in entries}
        if "" in questions:
            errors.append(f"Frage {question_id} enthält einen leeren Fragetext.")
        elif len(questions) != 1:
            errors.append(
                f"Frage {question_id} besitzt in den beiden Zeilen unterschiedliche Fragetexte."
            )

        actual_pairs = [(row.get(SYSTEM, ""), row.get(MODEL, "")) for row in entries]
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
            parse_score(row_number, row, column) for column in RETRIEVAL_CRITERIA
        )
        answer_score = sum(
            parse_score(row_number, row, column) for column in ANSWER_CRITERIA
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


def calculate_totals(scored_rows: list[ScoredRow]) -> dict[str, SystemTotals]:
    grouped: dict[tuple[str, str], list[ScoredRow]] = defaultdict(list)
    for row in scored_rows:
        grouped[(row.system, row.model)].append(row)

    totals: dict[str, SystemTotals] = {}
    for system, model in EXPECTED_SYSTEMS:
        rows = grouped[(system, model)]
        totals[system] = SystemTotals(
            system=system,
            model=model,
            question_count=len(rows),
            retrieval_score=sum(row.retrieval_score for row in rows),
            answer_score=sum(row.answer_score for row in rows),
            total_score=sum(row.total_score for row in rows),
        )
    return totals


def write_summary(path: Path, scored_rows: list[ScoredRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "Frage-ID", "Frage", "System", "Modell",
        "Retrievalscore", "Retrieval-Maximum", "Retrieval-Prozent",
        "Antwortscore", "Antwort-Maximum", "Antwort-Prozent",
        "Gesamtscore", "Gesamt-Maximum", "Gesamt-Prozent", "Bemerkungen",
    ]

    totals = calculate_totals(scored_rows)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=DELIMITER)
        writer.writeheader()

        for row in scored_rows:
            writer.writerow({
                "Frage-ID": row.question_id,
                "Frage": row.question,
                "System": row.system,
                "Modell": row.model,
                "Retrievalscore": row.retrieval_score,
                "Retrieval-Maximum": RETRIEVAL_MAX_PER_ROW,
                "Retrieval-Prozent": percentage(row.retrieval_score, RETRIEVAL_MAX_PER_ROW),
                "Antwortscore": row.answer_score,
                "Antwort-Maximum": ANSWER_MAX_PER_ROW,
                "Antwort-Prozent": percentage(row.answer_score, ANSWER_MAX_PER_ROW),
                "Gesamtscore": row.total_score,
                "Gesamt-Maximum": TOTAL_MAX_PER_ROW,
                "Gesamt-Prozent": percentage(row.total_score, TOTAL_MAX_PER_ROW),
                "Bemerkungen": row.comments,
            })

        for system, model in EXPECTED_SYSTEMS:
            total = totals[system]
            writer.writerow({
                "Frage-ID": "GESAMT",
                "Frage": f"Gesamtergebnis über {total.question_count} Fragen",
                "System": system,
                "Modell": model,
                "Retrievalscore": total.retrieval_score,
                "Retrieval-Maximum": total.retrieval_max,
                "Retrieval-Prozent": f"{total.retrieval_percent:.2f}",
                "Antwortscore": total.answer_score,
                "Antwort-Maximum": total.answer_max,
                "Antwort-Prozent": f"{total.answer_percent:.2f}",
                "Gesamtscore": total.total_score,
                "Gesamt-Maximum": total.total_max,
                "Gesamt-Prozent": f"{total.total_percent:.2f}",
                "Bemerkungen": "",
            })


def metric_values(total: SystemTotals, prefix: str) -> tuple[int, int, float, float]:
    return (
        getattr(total, f"{prefix}_score"),
        getattr(total, f"{prefix}_max"),
        getattr(total, f"{prefix}_average"),
        getattr(total, f"{prefix}_percent"),
    )


def write_totals_summary(path: Path, totals: dict[str, SystemTotals]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    investigation = totals["Untersuchungssystem"]
    reference = totals["Referenzsystem"]
    fieldnames = [
        "Bewertung", "Maximum je Frage",
        "Untersuchung Summe", "Untersuchung Maximum", "Untersuchung Durchschnitt", "Untersuchung Prozent",
        "Referenz Summe", "Referenz Maximum", "Referenz Durchschnitt", "Referenz Prozent",
        "Delta Durchschnitt", "Delta Prozentpunkte",
    ]
    metrics = [
        ("Retrievalscore", RETRIEVAL_MAX_PER_ROW, "retrieval"),
        ("Antwortscore", ANSWER_MAX_PER_ROW, "answer"),
        ("Gesamtscore", TOTAL_MAX_PER_ROW, "total"),
    ]

    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=DELIMITER)
        writer.writeheader()
        for label, maximum, prefix in metrics:
            ref_score, ref_max, ref_avg, ref_pct = metric_values(reference, prefix)
            inv_score, inv_max, inv_avg, inv_pct = metric_values(investigation, prefix)
            writer.writerow({
                "Bewertung": label,
                "Maximum je Frage": maximum,
                "Referenz Summe": ref_score,
                "Referenz Maximum": ref_max,
                "Referenz Durchschnitt": f"{ref_avg:.2f}",
                "Referenz Prozent": f"{ref_pct:.2f}",
                "Untersuchung Summe": inv_score,
                "Untersuchung Maximum": inv_max,
                "Untersuchung Durchschnitt": f"{inv_avg:.2f}",
                "Untersuchung Prozent": f"{inv_pct:.2f}",
                "Delta Durchschnitt": f"{inv_avg - ref_avg:+.2f}",
                "Delta Prozentpunkte": f"{inv_pct - ref_pct:+.2f}",
            })


def latex_number(value: float, signed: bool = False) -> str:
    text = f"{value:+.2f}" if signed else f"{value:.2f}"
    return text.replace(".", "{,}")


def write_latex_summary(path: Path, totals: dict[str, SystemTotals]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    investigation = totals["Untersuchungssystem"]
    reference = totals["Referenzsystem"]
    metrics = [
        ("Retrievalscore", RETRIEVAL_MAX_PER_ROW, "retrieval"),
        ("Antwortscore", ANSWER_MAX_PER_ROW, "answer"),
        ("Gesamtscore", TOTAL_MAX_PER_ROW, "total"),
    ]

    rows: list[str] = []
    for label, maximum, prefix in metrics:
        _, _, ref_avg, ref_pct = metric_values(reference, prefix)
        _, _, inv_avg, inv_pct = metric_values(investigation, prefix)
        rows.append(
            f"{label} & {maximum} & "
            f"{latex_number(inv_avg)} ({latex_number(inv_pct)}\\,\\%) & "
            f"{latex_number(ref_avg)} ({latex_number(ref_pct)}\\,\\%) & "
            f"{latex_number(inv_avg - ref_avg, signed=True)} & "
            f"{latex_number(inv_pct - ref_pct, signed=True)} \\\\"
        )

    latex = """\\begin{table}[bht]
\\centering
\\caption{Quantitative Ergebnisse der Evaluation}
\\label{tab:evaluation_summary}
\\begin{tabular}{lrrrrr}
\\toprule
\\textbf{Bewertung} &
\\textbf{Max.} &
\\textbf{Untersuchungssystem} &
\\textbf{Referenzsystem} &
\\textbf{$\\Delta$ Punkte} &
\\textbf{$\\Delta$ Prozentpunkte} \\\\
\\midrule
""" + "\n".join(rows) + """
\\bottomrule
\\end{tabular}
\\end{table}
"""
    path.write_text(latex, encoding="utf-8")


def print_system_totals(scored_rows: list[ScoredRow]) -> None:
    totals = calculate_totals(scored_rows)
    print(f"Gefundene Fragen: {len(scored_rows) // 2}")
    print(f"Gefundene Bewertungszeilen: {len(scored_rows)}")
    print("Validierung erfolgreich.\n")

    for system, model in EXPECTED_SYSTEMS:
        total = totals[system]
        print(f"{system} ({model})")
        print(
            f"  Retrieval: {total.retrieval_score}/{total.retrieval_max} "
            f"(Ø {total.retrieval_average:.2f}/{RETRIEVAL_MAX_PER_ROW}; {total.retrieval_percent:.2f} %)"
        )
        print(
            f"  Antwort:   {total.answer_score}/{total.answer_max} "
            f"(Ø {total.answer_average:.2f}/{ANSWER_MAX_PER_ROW}; {total.answer_percent:.2f} %)"
        )
        print(
            f"  Gesamt:    {total.total_score}/{total.total_max} "
            f"(Ø {total.total_average:.2f}/{TOTAL_MAX_PER_ROW}; {total.total_percent:.2f} %)"
        )

    investigation = totals["Untersuchungssystem"]
    reference = totals["Referenzsystem"]
    print("\nDifferenz Untersuchungssystem gegenüber Referenzsystem")
    print(
        f"  Retrieval: {investigation.retrieval_average - reference.retrieval_average:+.2f} "
        f"Punkte; {investigation.retrieval_percent - reference.retrieval_percent:+.2f} Prozentpunkte"
    )
    print(
        f"  Antwort:   {investigation.answer_average - reference.answer_average:+.2f} "
        f"Punkte; {investigation.answer_percent - reference.answer_percent:+.2f} Prozentpunkte"
    )
    print(
        f"  Gesamt:    {investigation.total_average - reference.total_average:+.2f} "
        f"Punkte; {investigation.total_percent - reference.total_percent:+.2f} Prozentpunkte"
    )


def main() -> int:
    args = parse_args()
    try:
        rows, fieldnames = read_ratings(args.input)
        validate_columns(fieldnames)
        validate_structure(rows)
        scored_rows = score_rows(rows)
        totals = calculate_totals(scored_rows)
        write_summary(args.output, scored_rows)
        write_totals_summary(args.totals_output, totals)
        write_latex_summary(args.latex_output, totals)
    except (OSError, ValueError) as exc:
        print(f"Fehler: {exc}", file=sys.stderr)
        return 1

    print(f"Eingabedatei: {args.input.resolve()}")
    print(f"Detailauswertung: {args.output.resolve()}")
    print(f"Gesamtauswertung: {args.totals_output.resolve()}")
    print(f"LaTeX-Tabelle: {args.latex_output.resolve()}\n")
    print_system_totals(scored_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
