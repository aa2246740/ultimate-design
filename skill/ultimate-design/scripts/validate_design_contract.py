#!/usr/bin/env python3
"""Validate a DESIGN.md design contract.

This is a local structural fallback for the ultimate-design skill. Prefer the
official @google/design.md tooling when it is available and current enough for
the project.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except Exception as exc:  # pragma: no cover - exercised only in stripped envs
    yaml = None  # type: ignore[assignment]
    YAML_IMPORT_ERROR = exc
else:
    YAML_IMPORT_ERROR = None


OFFICIAL_TOP_LEVEL = {
    "version",
    "name",
    "description",
    "colors",
    "typography",
    "rounded",
    "spacing",
    "components",
}

BAD_TOP_LEVEL = {
    "radius": "Use official `rounded`, not `radius`.",
    "borderRadius": "Use official `rounded`, not `borderRadius`.",
}

OFFICIAL_COMPONENT_PROPS = {
    "backgroundColor",
    "textColor",
    "typography",
    "rounded",
    "padding",
    "size",
    "height",
    "width",
}

BAD_COMPONENT_PROPS = {
    "background": "Use `backgroundColor` when mapping component background color.",
    "color": "Use `textColor` when mapping component text color.",
    "radius": "Use `rounded` for component radius token references.",
    "borderRadius": "Use `rounded` for component radius token references.",
    "border-radius": "Use `rounded` for component radius token references.",
}

STANDARD_SECTIONS = [
    "overview",
    "colors",
    "typography",
    "layout",
    "elevation & depth",
    "shapes",
    "components",
    "do's and don'ts",
]

SECTION_ALIASES = {
    "brand & style": "overview",
    "layout & spacing": "layout",
    "elevation": "elevation & depth",
    "dos and don'ts": "do's and don'ts",
    "do and don't": "do's and don'ts",
    "do's & don'ts": "do's and don'ts",
}

ULTIMATE_SECTIONS = [
    "request anchor",
    "content model",
    "okf preflight",
    "information architecture",
    "quality gates",
    "assumptions",
    "open questions",
    "review log",
]

REQUEST_ANCHOR_FIELDS = [
    "Original user request",
    "Latest user override",
    "Deliverable",
    "Primary audience",
    "Core job to be done",
    "Success criteria",
    "Non-goals",
    "Must preserve",
    "Validation must check against",
]

OKF_PREFLIGHT_FIELDS = [
    "Active references loaded",
    "Constraints extracted",
    "Deliberate exceptions",
    "Verification hooks",
]

DIMENSION_RE = re.compile(r"^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:px|em|rem)$")
TOKEN_REF_RE = re.compile(r"^\{([A-Za-z0-9_.-]+)\}$")
BAD_DOLLAR_REF_RE = re.compile(r"\$[A-Za-z0-9_.-]+")
WEAK_TOKEN_NAME_RE = re.compile(r"^(?:blue|gray|grey|red|green|yellow|purple|orange)\d+$|^(?:big|small|new)", re.I)


class Reporter:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def extract_frontmatter(text: str) -> tuple[str | None, str]:
    match = re.match(r"^---\n(.*?)\n---\n?", text, flags=re.DOTALL)
    if not match:
        return None, text
    return match.group(1), text[match.end() :]


def normalize_heading(value: str) -> str:
    normalized = re.sub(r"\s+", " ", value.strip().lower())
    return SECTION_ALIASES.get(normalized, normalized)


def headings(body: str) -> list[str]:
    return [normalize_heading(m.group(1)) for m in re.finditer(r"^##\s+(.+?)\s*$", body, flags=re.MULTILINE)]


def is_dimension(value: Any) -> bool:
    return isinstance(value, str) and bool(DIMENSION_RE.match(value.strip()))


def is_number(value: Any) -> bool:
    return isinstance(value, int | float) and not isinstance(value, bool)


def resolve_ref(data: dict[str, Any], ref: str) -> bool:
    node: Any = data
    for part in ref.split("."):
        if not isinstance(node, dict) or part not in node:
            return False
        node = node[part]
    return True


def walk_values(value: Any) -> list[Any]:
    values = [value]
    if isinstance(value, dict):
        for child in value.values():
            values.extend(walk_values(child))
    elif isinstance(value, list):
        for child in value:
            values.extend(walk_values(child))
    return values


def check_section_order(section_names: list[str], reporter: Reporter) -> None:
    seen = [name for name in section_names if name in STANDARD_SECTIONS]
    positions = [STANDARD_SECTIONS.index(name) for name in seen]
    if positions != sorted(positions):
        reporter.error(
            "Standard Markdown sections are out of order. Expected: "
            + " -> ".join(title.title() for title in STANDARD_SECTIONS)
        )

    duplicates = sorted({name for name in section_names if section_names.count(name) > 1})
    for name in duplicates:
        reporter.warn(f"Duplicate section heading: {name}")


def check_yaml(data: dict[str, Any], reporter: Reporter) -> None:
    for field, message in BAD_TOP_LEVEL.items():
        if field in data:
            reporter.error(f"Top-level `{field}` is not Google core schema. {message}")

    if "name" not in data:
        reporter.error("Front matter should include `name`.")

    for recommended in ["colors", "typography", "rounded", "spacing", "components"]:
        if recommended not in data:
            reporter.warn(f"Recommended Google core field missing: `{recommended}`.")

    for field in data:
        if field not in OFFICIAL_TOP_LEVEL and field not in BAD_TOP_LEVEL:
            reporter.warn(f"Top-level `{field}` is a team extension, not Google core schema.")

    colors = data.get("colors")
    if isinstance(colors, dict):
        if "primary" not in colors:
            reporter.warn("`colors` exists but lacks `primary`.")
        for name, value in colors.items():
            if WEAK_TOKEN_NAME_RE.match(str(name)):
                reporter.warn(f"Color token `{name}` is weakly named; prefer semantic roles.")
            if not isinstance(value, str):
                reporter.warn(f"Color token `{name}` should usually be a CSS color string.")

    typography = data.get("typography")
    if isinstance(typography, dict):
        for name, spec in typography.items():
            if WEAK_TOKEN_NAME_RE.match(str(name)):
                reporter.warn(f"Typography token `{name}` is weakly named; prefer role/size names.")
            if not isinstance(spec, dict):
                reporter.error(f"Typography token `{name}` should be a mapping.")
                continue
            for required in ["fontFamily", "fontSize"]:
                if required not in spec:
                    reporter.warn(f"Typography token `{name}` lacks `{required}`.")
            if "fontSize" in spec and not is_dimension(spec["fontSize"]):
                reporter.error(f"Typography token `{name}.fontSize` should use px, em, or rem.")

    rounded = data.get("rounded")
    if isinstance(rounded, dict):
        for name, value in rounded.items():
            if not is_dimension(value):
                reporter.error(f"`rounded.{name}` should use px, em, or rem.")

    spacing = data.get("spacing")
    if isinstance(spacing, dict):
        for name, value in spacing.items():
            if not (is_dimension(value) or is_number(value)):
                reporter.error(f"`spacing.{name}` should be a number or px/em/rem dimension.")

    components = data.get("components")
    if isinstance(components, dict):
        for component, spec in components.items():
            if not isinstance(spec, dict):
                reporter.error(f"Component `{component}` should be a mapping.")
                continue
            for prop, value in spec.items():
                if prop in BAD_COMPONENT_PROPS:
                    reporter.error(f"Component `{component}` property `{prop}` is non-canonical. {BAD_COMPONENT_PROPS[prop]}")
                elif prop not in OFFICIAL_COMPONENT_PROPS:
                    reporter.warn(f"Component `{component}` property `{prop}` is an extension.")
                for nested in walk_values(value):
                    if isinstance(nested, str):
                        if BAD_DOLLAR_REF_RE.search(nested):
                            reporter.error(f"Component `{component}` uses non-official `$token` reference: {nested}")
                        match = TOKEN_REF_RE.match(nested.strip())
                        if match and not resolve_ref(data, match.group(1)):
                            reporter.error(f"Component `{component}` has broken token reference: {nested}")


def check_ultimate_sections(section_names: list[str], strict: bool, reporter: Reporter) -> None:
    missing = [name for name in ULTIMATE_SECTIONS if name not in section_names]
    for name in missing:
        message = f"Ultimate-design continuity section missing: {name}"
        if strict:
            reporter.error(message)
        else:
            reporter.warn(message)


def section_text(body: str, heading: str) -> str | None:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*$\n(?P<body>.*?)(?=^##\s+|\Z)",
        flags=re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    match = pattern.search(body)
    return match.group("body") if match else None


def check_request_anchor(body: str, strict: bool, reporter: Reporter) -> None:
    anchor = section_text(body, "Request Anchor")
    if anchor is None:
        message = "Request Anchor section missing."
        if strict:
            reporter.error(message)
        else:
            reporter.warn(message)
        return

    for field in REQUEST_ANCHOR_FIELDS:
        match = re.search(rf"(?mi)^\s*[-*]\s+{re.escape(field)}\s*:\s*(.*)$", anchor)
        if not match:
            message = f"Request Anchor field missing: {field}"
            if strict:
                reporter.error(message)
            else:
                reporter.warn(message)
            continue
        value = match.group(1).strip()
        if strict and not value:
            reporter.error(f"Request Anchor field is empty: {field}")


def check_okf_preflight(body: str, strict: bool, reporter: Reporter) -> None:
    preflight = section_text(body, "OKF Preflight")
    if preflight is None:
        message = "OKF Preflight section missing."
        if strict:
            reporter.error(message)
        else:
            reporter.warn(message)
        return

    for field in OKF_PREFLIGHT_FIELDS:
        match = re.search(rf"(?mi)^\s*[-*]\s+{re.escape(field)}\s*:\s*(.*)$", preflight)
        if not match:
            message = f"OKF Preflight field missing: {field}"
            if strict:
                reporter.error(message)
            else:
                reporter.warn(message)
            continue
        value = match.group(1).strip()
        if strict and not value:
            reporter.error(f"OKF Preflight field is empty: {field}")


def validate(path: Path, require_frontmatter: bool, strict_ultimate: bool) -> tuple[int, Reporter, dict[str, Any]]:
    reporter = Reporter()
    text = path.read_text(encoding="utf-8")
    fm_text, body = extract_frontmatter(text)
    data: dict[str, Any] = {}

    if fm_text is None:
        message = "No YAML front matter found. It is officially optional, but strongly recommended for AI/tooling."
        if require_frontmatter:
            reporter.error(message)
        else:
            reporter.warn(message)
    else:
        if yaml is None:
            reporter.error(f"PyYAML is unavailable: {YAML_IMPORT_ERROR}")
        else:
            try:
                parsed = yaml.safe_load(fm_text) or {}
            except Exception as exc:
                reporter.error(f"YAML front matter failed to parse: {exc}")
                parsed = {}
            if not isinstance(parsed, dict):
                reporter.error("YAML front matter must parse to a mapping.")
            else:
                data = parsed
                check_yaml(data, reporter)

    section_names = headings(body)
    check_section_order(section_names, reporter)
    check_ultimate_sections(section_names, strict_ultimate, reporter)
    check_request_anchor(body, strict_ultimate, reporter)
    check_okf_preflight(body, strict_ultimate, reporter)

    summary = {
        "path": str(path),
        "has_frontmatter": fm_text is not None,
        "sections": section_names,
        "errors": len(reporter.errors),
        "warnings": len(reporter.warnings),
    }
    return (1 if reporter.errors else 0), reporter, summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a DESIGN.md design contract.")
    parser.add_argument("path", nargs="?", default="DESIGN.md", help="Path to DESIGN.md")
    parser.add_argument("--require-frontmatter", action="store_true", help="Treat missing YAML front matter as an error.")
    parser.add_argument("--strict-ultimate", action="store_true", help="Treat missing ultimate-design extension sections as errors.")
    parser.add_argument("--json", action="store_true", help="Print JSON summary.")
    args = parser.parse_args()

    path = Path(args.path).resolve()
    if not path.exists():
        print(f"ERROR file not found: {path}", file=sys.stderr)
        return 2

    status, reporter, summary = validate(path, args.require_frontmatter, args.strict_ultimate)

    if args.json:
        print(json.dumps({**summary, "error_messages": reporter.errors, "warning_messages": reporter.warnings}, indent=2))
        return status

    for message in reporter.errors:
        print(f"ERROR {message}")
    for message in reporter.warnings:
        print(f"WARN {message}")

    print("DESIGN CONTRACT VALIDATION " + ("PASS" if status == 0 else "FAIL"))
    print(f"Checked: {path}")
    print(f"Errors: {len(reporter.errors)}")
    print(f"Warnings: {len(reporter.warnings)}")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
