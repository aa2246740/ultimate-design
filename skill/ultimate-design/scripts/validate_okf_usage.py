#!/usr/bin/env python3
"""Validate that active OKF concepts changed concrete design decisions."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


OKF_PATH_RE = re.compile(r"(?:references/)?(design-okf/[A-Za-z0-9_./-]+\.md)")
EMPTY_VALUES = {"", "-", "none", "n/a", "na", "tbd", "todo", "placeholder"}
RESERVED_OKF_NAMES = {"index.md", "log.md"}


def section_text(text: str, heading: str) -> str | None:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^##\s+|\Z)",
        flags=re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    match = pattern.search(text)
    return match.group("body") if match else None


def subsection_text(text: str, heading: str) -> str | None:
    pattern = re.compile(
        rf"^###\s+{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^###\s+|^##\s+|\Z)",
        flags=re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    match = pattern.search(text)
    return match.group("body") if match else None


def active_concepts(preflight: str) -> list[str]:
    explicit = subsection_text(preflight, "Active OKF Concepts")
    search_space = explicit if explicit is not None else preflight
    return sorted(
        {
            concept
            for concept in OKF_PATH_RE.findall(search_space)
            if Path(concept).name not in RESERVED_OKF_NAMES
        }
    )


def clean_cell(value: str) -> str:
    return value.strip().strip("`").strip()


def is_filled(value: str) -> bool:
    return clean_cell(value).lower() not in EMPTY_VALUES


def table_rows(section: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for raw in section.splitlines():
        line = raw.strip()
        if not (line.startswith("|") and line.endswith("|")):
            continue
        cells = [clean_cell(cell) for cell in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        if cells[0].lower() == "reference" or all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells[:4]):
            continue
        rows.append(cells[:4])
    return rows


def validate(path: Path, allow_no_okf: bool) -> tuple[int, dict[str, object]]:
    text = path.read_text(encoding="utf-8")
    preflight = section_text(text, "OKF Preflight")
    bindings = section_text(text, "OKF Decision Bindings")
    errors: list[str] = []

    if preflight is None:
        errors.append("OKF Preflight section missing")
        active: list[str] = []
    else:
        active = active_concepts(preflight)

    rows = table_rows(bindings or "")
    valid_rows: list[dict[str, str]] = []
    for cells in rows:
        reference, decision, target, verification = cells
        row = {
            "reference": reference,
            "decision": decision,
            "artifact_target": target,
            "verification": verification,
        }
        if not all(is_filled(value) for value in cells):
            errors.append(f"Incomplete OKF decision binding: {reference or '<missing reference>'}")
            continue
        valid_rows.append(row)

    if active and bindings is None:
        errors.append("OKF Decision Bindings section missing")

    bound: set[str] = set()
    for row in valid_rows:
        row_ref = row["reference"]
        for concept in active:
            if concept in row_ref or Path(concept).name in row_ref:
                bound.add(concept)

    for concept in active:
        if concept not in bound:
            errors.append(f"Active OKF concept has no decision binding: {concept}")

    if not active and not allow_no_okf:
        no_okf_reason = bool(preflight and re.search(r"(?i)no\s+(active\s+)?okf|no\s+okf\s+concept|无.*OKF|不适用", preflight))
        if not no_okf_reason:
            errors.append("No active OKF concept found and no explicit no-OKF reason recorded")

    summary: dict[str, object] = {
        "schemaVersion": "ultimate-design.okf-usage.v1",
        "path": str(path),
        "active_concepts": active,
        "bound_concepts": sorted(bound),
        "binding_rows": valid_rows,
        "errors": errors,
        "status": "pass" if not errors else "fail",
    }
    return (0 if not errors else 1), summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate OKF decision bindings in DESIGN.md.")
    parser.add_argument("path", nargs="?", default="DESIGN.md", help="Path to DESIGN.md")
    parser.add_argument("--allow-no-okf", action="store_true", help="Allow a contract with no active OKF concept.")
    parser.add_argument("--json", action="store_true", help="Print the full JSON report.")
    args = parser.parse_args()

    path = Path(args.path).resolve()
    if not path.exists():
        print(f"ERROR file not found: {path}", file=sys.stderr)
        return 2

    code, summary = validate(path, args.allow_no_okf)
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"OKF USAGE VALIDATION {str(summary['status']).upper()}")
        print(f"Checked: {path}")
        print(f"Active concepts: {len(summary['active_concepts'])}")
        print(f"Bound concepts: {len(summary['bound_concepts'])}")
        for error in summary["errors"]:
            print(f"ERROR {error}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
