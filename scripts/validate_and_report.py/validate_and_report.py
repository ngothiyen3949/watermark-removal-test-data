#!/usr/bin/env python3
"""Validate the published CSV and render its recorded sample rows as Markdown."""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "video-sample-results.csv"
REQUIRED = {
    "sample_id",
    "mark_description",
    "input_format",
    "input_codec",
    "resolution",
    "fps",
    "duration_seconds",
    "frame_count",
    "input_bytes",
    "output_bytes",
    "elapsed_seconds",
    "observed_result",
}
INTEGER_FIELDS = ("fps", "duration_seconds", "frame_count", "input_bytes", "output_bytes")
DECIMAL_FIELDS = ("elapsed_seconds",)


def validate_row(row: dict[str, str], line_number: int) -> None:
    missing = [field for field in REQUIRED if not row.get(field, "").strip()]
    if missing:
        raise ValueError(f"line {line_number}: missing values for {', '.join(sorted(missing))}")

    for field in INTEGER_FIELDS:
        if not re.fullmatch(r"\d+", row[field]):
            raise ValueError(f"line {line_number}: {field} must be a non-negative integer")

    for field in DECIMAL_FIELDS:
        if not re.fullmatch(r"\d+(?:\.\d+)?", row[field]):
            raise ValueError(f"line {line_number}: {field} must be a non-negative decimal")


def main() -> None:
    with CSV_PATH.open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        if reader.fieldnames is None or set(reader.fieldnames) != REQUIRED:
            raise ValueError("CSV header does not match the documented schema")
        rows = list(reader)

    if not rows:
        raise ValueError("CSV contains no sample rows")

    for line_number, row in enumerate(rows, start=2):
        validate_row(row, line_number)

    columns = [
        "Sample",
        "Mark description",
        "Input (bytes)",
        "Output (bytes)",
        "Elapsed (seconds)",
        "Observed result",
    ]
    print("| " + " | ".join(columns) + " |")
    print("| " + " | ".join("---" for _ in columns) + " |")
    for row in rows:
        print(
            "| "
            + " | ".join(
                (
                    row["sample_id"],
                    row["mark_description"],
                    row["input_bytes"],
                    row["output_bytes"],
                    row["elapsed_seconds"],
                    row["observed_result"].replace("|", "\\|"),
                )
            )
            + " |"
        )


if __name__ == "__main__":
    main()

