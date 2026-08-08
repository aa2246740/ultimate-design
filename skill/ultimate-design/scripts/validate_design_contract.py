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
    "okf decision bindings",
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



VALID_MATURITY_STATUS = re.compile(r"^(Exploratory|Candidate|Locked)$", re.I)
EMPTY_OR_PUNCT_FIELD = re.compile(r"^(?:n/?a|none|\.+|—|-|–|\(required.*\))$", re.I)

# Unresolved tokens anywhere in Locked axes (design negatives like "no gradients" stay valid).
AXES_UNRESOLVED_TOKEN = re.compile(
    r"(?i)\b(?:tbd|todo|unknown|placeholder|pending|awaiting|n/?a|none)\b"
)

# Four fixed Lock authority forms only (case-insensitive; flexible horizontal space).
VALID_LOCK_AUTHORITY_FORMS = (
    re.compile(r"(?i)^[ \t]*user[ \t]+accepted[ \t]+after[ \t]+codex[ \t]+review[ \t]*$"),
    re.compile(r"(?i)^[ \t]*design[ \t]+owner[ \t]+approved[ \t]*$"),
    re.compile(r"(?i)^[ \t]*accepted[ \t]+by[ \t]+user[ \t]*$"),
    re.compile(r"(?i)^[ \t]*approved[ \t]+by[ \t]+design[ \t]+owner[ \t]*$"),
)

PREEXISTING_LOCKED_CONTRACT = re.compile(
    r"(?i)^[ \t]*pre-existing[ \t]+locked[ \t]+contract[ \t]*"
    r"(?::[ \t]*|[ \t]+in[ \t]+)([^\n]+?)[ \t]*$"
)
MARKDOWN_CONTRACT_SUFFIXES = {".md", ".markdown"}

# Bound pre-existing reference walk well below sys.getrecursionlimit() (~1000).
MAX_PREEXISTING_DEPTH = 32

MATURITY_KEY_FIELDS = ("Status", "Lock authority", "Locked axes")
MATURITY_HEADING_RE = re.compile(r"(?mi)^##[ \t]+Design Maturity[ \t]*$")


def _maturity_field_values(maturity: str, field: str) -> list[str]:
    """Line-safe field parse: horizontal space only; bullets -, *, +; no cross-line capture."""
    pattern = re.compile(
        rf"(?mi)^[ \t]*(?:[-*+][ \t]+)?{re.escape(field)}[ \t]*:[ \t]*([^\n]*)$"
    )
    return [match.group(1).rstrip() for match in pattern.finditer(maturity)]


def _maturity_issue(reporter: "Reporter", strict: bool, message: str) -> None:
    if strict:
        reporter.error(message)
    else:
        reporter.warn(message)


def _is_invalid_locked_axes(value: str) -> bool:
    text = value.strip()
    if not text:
        return True
    if EMPTY_OR_PUNCT_FIELD.match(text):
        return True
    if AXES_UNRESOLVED_TOKEN.search(text):
        return True
    return False


def _resolve_preexisting_target(
    target: str, contract_path: Path | None
) -> tuple[Path | None, str | None]:
    """Return (resolved_path, error_message).

    Security is structural only: controlled relative Markdown path, no absolute path,
    no parent traversal, resolved within the DESIGN.md directory, and is_file().
    Directory vocabulary (ai/, repo/, codex/, pending/) is not blacklisted.
    """
    raw = target.strip().strip("`\"'")
    if not raw:
        return None, "empty pre-existing contract path"
    if raw.startswith("/") or re.match(r"^[A-Za-z]:[\\/]", raw):
        return None, "absolute pre-existing contract path is not allowed"
    path = Path(raw)
    if ".." in path.parts:
        return None, "pre-existing contract path must not traverse parent directories"
    if path.suffix.lower() not in MARKDOWN_CONTRACT_SUFFIXES:
        return None, "pre-existing contract path must be a Markdown file (.md or .markdown)"
    if contract_path is None:
        return None, "pre-existing contract path requires validating a real DESIGN.md path"
    base = contract_path.resolve().parent
    resolved = (base / path).resolve()
    try:
        resolved.relative_to(base)
    except ValueError:
        return None, "pre-existing contract path escapes the DESIGN.md directory"
    if not resolved.is_file():
        return None, f"pre-existing contract file does not exist: {raw}"
    return resolved, None


def _is_valid_role_authority_statement(text: str) -> bool:
    """True only for the four documented fixed authority forms."""
    cleaned = text.strip()
    if not cleaned:
        return False
    return any(pattern.fullmatch(cleaned) for pattern in VALID_LOCK_AUTHORITY_FORMS)


def _referenced_contract_is_locked(
    path: Path,
    *,
    strict: bool,
    reporter: "Reporter",
    visited: set[Path],
    depth: int,
) -> bool:
    """Referenced contract must itself be Locked with valid User/Design owner authority.

    ``depth`` counts pre-existing hops; fails with a normal finding at
    MAX_PREEXISTING_DEPTH (32), well below the interpreter recursion limit.
    """
    if depth >= MAX_PREEXISTING_DEPTH:
        _maturity_issue(
            reporter,
            strict,
            f"Pre-existing locked contract reference depth exceeds "
            f"{MAX_PREEXISTING_DEPTH}.",
        )
        return False
    resolved = path.resolve()
    if resolved in visited:
        _maturity_issue(
            reporter,
            strict,
            "Pre-existing locked contract reference loop detected.",
        )
        return False
    visited = set(visited)
    visited.add(resolved)
    try:
        text = resolved.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        _maturity_issue(
            reporter,
            strict,
            f"Pre-existing locked contract file unreadable or invalid encoding: "
            f"{resolved.name} ({exc})",
        )
        return False
    _, body = extract_frontmatter(text)
    nested = Reporter()
    check_design_maturity(
        body,
        nested,
        strict=True,
        contract_path=resolved,
        _visited=visited,
        _depth=depth + 1,
    )
    if nested.errors:
        structural = [
            e
            for e in nested.errors
            if any(
                key in e
                for key in (
                    "depth exceeds",
                    "loop detected",
                    "unreadable",
                    "invalid encoding",
                )
            )
        ]
        if structural:
            for message in structural:
                _maturity_issue(reporter, strict, message)
        else:
            _maturity_issue(
                reporter,
                strict,
                "Pre-existing locked contract must declare Status Locked with valid "
                f"User/Design owner authority and locked axes ({resolved.name}).",
            )
        return False
    maturity = section_text(body, "Design Maturity") or ""
    statuses = _maturity_field_values(maturity, "Status")
    if not statuses or statuses[0].strip().lower() != "locked":
        _maturity_issue(
            reporter,
            strict,
            f"Pre-existing locked contract is not Status Locked: {resolved.name}",
        )
        return False
    return True


def _is_valid_lock_authority(
    value: str,
    *,
    contract_path: Path | None,
    strict: bool,
    reporter: "Reporter",
    visited: set[Path],
    depth: int,
) -> bool:
    text = value.strip()
    preexisting = PREEXISTING_LOCKED_CONTRACT.match(text)
    if preexisting:
        target = preexisting.group(1).strip()
        resolved, err = _resolve_preexisting_target(target, contract_path)
        if err or resolved is None:
            return False
        return _referenced_contract_is_locked(
            resolved,
            strict=strict,
            reporter=reporter,
            visited=visited,
            depth=depth,
        )
    if re.match(r"(?i)^[ \t]*pre-existing[ \t]+locked[ \t]+contract[ \t]*$", text):
        return False
    return _is_valid_role_authority_statement(text)


def check_design_maturity(
    body: str,
    reporter: "Reporter",
    *,
    strict: bool = False,
    contract_path: Path | None = None,
    _visited: set[Path] | None = None,
    _depth: int = 0,
) -> None:
    """Validate Design Maturity when present.

    Missing section is always a no-op. When present, ``strict`` controls
    error vs warning. ``contract_path`` enables pre-existing contract path checks.
    ``_depth`` bounds pre-existing reference walks (max MAX_PREEXISTING_DEPTH).
    """
    visited = _visited if _visited is not None else set()
    heading_count = len(MATURITY_HEADING_RE.findall(body))
    if heading_count == 0:
        return
    if heading_count > 1:
        _maturity_issue(
            reporter,
            strict,
            "Design Maturity has duplicate section headings; keep one authoritative section.",
        )

    maturity = section_text(body, "Design Maturity")
    if maturity is None:
        return

    for field in MATURITY_KEY_FIELDS:
        values = _maturity_field_values(maturity, field)
        if len(values) > 1:
            _maturity_issue(
                reporter,
                strict,
                f"Design Maturity has duplicate {field} fields.",
            )

    statuses = _maturity_field_values(maturity, "Status")
    if not statuses:
        _maturity_issue(
            reporter,
            strict,
            "Design Maturity section present but Status is missing.",
        )
        return

    status = statuses[0].strip()
    if not VALID_MATURITY_STATUS.fullmatch(status):
        _maturity_issue(
            reporter,
            strict,
            "Design Maturity Status must be exactly Exploratory, Candidate, or Locked "
            f"(got {status!r}).",
        )
        return

    if status.lower() != "locked":
        return

    authorities = _maturity_field_values(maturity, "Lock authority")
    axes_list = _maturity_field_values(maturity, "Locked axes")
    auth_val = authorities[0].strip() if authorities else ""
    axes_val = axes_list[0].strip() if axes_list else ""
    issue_count_before = len(reporter.errors) + len(reporter.warnings)
    if not _is_valid_lock_authority(
        auth_val,
        contract_path=contract_path,
        strict=strict,
        reporter=reporter,
        visited=visited,
        depth=_depth,
    ):
        if len(reporter.errors) + len(reporter.warnings) == issue_count_before:
            _maturity_issue(
                reporter,
                strict,
                "Locked Design Maturity requires Lock authority as one of the four "
                "documented forms (User accepted after Codex review; Design owner approved; "
                "Accepted by user; Approved by design owner) or a pre-existing locked "
                "Markdown contract path that itself is Locked under those rules.",
            )
    if _is_invalid_locked_axes(axes_val):
        _maturity_issue(
            reporter,
            strict,
            "Locked Design Maturity requires non-empty Locked axes without unresolved "
            "tokens such as TBD/pending/placeholder (negative design constraints are allowed).",
        )


def _minimal_maturity_probe_body(maturity_block: str | None) -> str:
    base = (
        "# Design System\n\n## Overview\nProbe.\n\n## Colors\nok\n\n"
        "## Typography\nok\n\n## Layout\nok\n\n## Elevation & Depth\nok\n\n"
        "## Shapes\nok\n\n## Components\nok\n\n## Do's and Don'ts\nok\n"
    )
    if maturity_block:
        return base + "\n" + maturity_block + "\n"
    return base


def run_maturity_smoke_tests() -> list[str]:
    """Compact installable smoke suite — core parser viability only.

    Always available in the published package. Does not load repo-only tests/.
    """
    failures: list[str] = []

    def errs(block: str | None, *, strict: bool = True) -> list[str]:
        reporter = Reporter()
        check_design_maturity(
            _minimal_maturity_probe_body(block), reporter, strict=strict
        )
        return list(reporter.errors)

    def warns(block: str | None) -> list[str]:
        reporter = Reporter()
        check_design_maturity(
            _minimal_maturity_probe_body(block), reporter, strict=False
        )
        return list(reporter.warnings)

    # missing section is a no-op
    if errs(None, strict=True):
        failures.append(f"missing section should be silent: {errs(None)}")

    # Draft: non-strict warn-only; strict error
    draft = "## Design Maturity\n\n- Status: Draft\n"
    if errs(draft, strict=False):
        failures.append(f"Draft non-strict must be 0 errors: {errs(draft, strict=False)}")
    if not warns(draft):
        failures.append("Draft non-strict must warn")
    if not errs(draft, strict=True):
        failures.append("Draft strict must error")

    # valid Locked authority (documented four forms only)
    locked_ok = (
        "## Design Maturity\n\n- Status: Locked\n"
        "- Lock authority: User accepted after Codex review\n"
        "- Locked axes: color, type\n"
    )
    if errs(locked_ok, strict=True):
        failures.append(f"valid User accepted after Codex review should pass: {errs(locked_ok)}")

    # negative axes language allowed; unresolved token anywhere fails
    axes_ok = (
        "## Design Maturity\n\n- Status: Locked\n"
        "- Lock authority: Design owner approved\n"
        "- Locked axes: no gradients, never use shadows\n"
    )
    if errs(axes_ok, strict=True):
        failures.append(f"negative axes language should pass: {errs(axes_ok)}")
    axes_tbd = (
        "## Design Maturity\n\n- Status: Locked\n"
        "- Lock authority: Design owner approved\n"
        "- Locked axes: color, TBD\n"
    )
    if not errs(axes_tbd, strict=True):
        failures.append("axes containing TBD must fail")

    # empty axes must not swallow next field
    empty_axes = (
        "## Design Maturity\n\n- Status: Locked\n"
        "- Lock authority: Accepted by user\n"
        "- Locked axes:\n"
        "- Allowed variation: no gradients\n"
    )
    if not errs(empty_axes, strict=True):
        failures.append("empty Locked axes must fail")

    # + bullet duplicate Status
    plus_dup = (
        "## Design Maturity\n\n- Status: Candidate\n"
        "+ Status: Locked\n"
        "- Lock authority: Approved by design owner\n"
        "- Locked axes: color\n"
    )
    if not any("duplicate Status" in e for e in errs(plus_dup, strict=True)):
        failures.append(f"+ bullet Status duplicate must fail: {errs(plus_dup)}")

    # reject non-fixed authority forms
    for bad in (
        "User accepted",
        "User accepted after AI guess",
        "User accepted?",
        "Client signed off",
        "approved by Codex",
    ):
        block = (
            "## Design Maturity\n\n- Status: Locked\n"
            f"- Lock authority: {bad}\n"
            "- Locked axes: color\n"
        )
        if not errs(block, strict=True):
            failures.append(f"authority must fail: {bad!r}")

    # line-safe field parse: prose + bullet counted together
    mixed = (
        "## Design Maturity\n\n- Status: Candidate\n"
        "Status: Locked\n"
        "- Lock authority: User accepted after Codex review\n"
        "- Locked axes: color\n"
    )
    if not any("duplicate Status" in e for e in errs(mixed, strict=True)):
        failures.append(f"mixed bullet/prose Status duplicate must fail: {errs(mixed)}")

    # depth bound: deep acyclic chain must not RecursionError
    try:
        with __import__("tempfile").TemporaryDirectory() as tmp:
            root = Path(tmp)
            # chain file_0 -> file_1 -> ... -> file_40 each Locked with pre-existing
            n = MAX_PREEXISTING_DEPTH + 5
            for i in range(n - 1, -1, -1):
                p = root / f"c{i}.md"
                if i == n - 1:
                    auth = "Design owner approved"
                    body = (
                        "# Design System\n\n## Overview\nx\n\n## Design Maturity\n\n"
                        f"- Status: Locked\n- Lock authority: {auth}\n"
                        "- Locked axes: color\n"
                    )
                else:
                    body = (
                        "# Design System\n\n## Overview\nx\n\n## Design Maturity\n\n"
                        "- Status: Locked\n"
                        f"- Lock authority: Pre-existing locked contract: c{i + 1}.md\n"
                        "- Locked axes: color\n"
                    )
                p.write_text(body, encoding="utf-8")
            rep = Reporter()
            check_design_maturity(
                (root / "c0.md").read_text(encoding="utf-8"),
                rep,
                strict=True,
                contract_path=root / "c0.md",
            )
            if not rep.errors:
                failures.append("deep acyclic pre-existing chain must fail at max depth")
            if any("RecursionError" in e for e in rep.errors):
                failures.append("deep chain must not surface RecursionError")
    except RecursionError:
        failures.append("deep acyclic pre-existing chain raised RecursionError")

    # non-UTF-8 target must not raise UnicodeDecodeError
    try:
        with __import__("tempfile").TemporaryDirectory() as tmp:
            root = Path(tmp)
            bad = root / "binary.md"
            bad.write_bytes(b"\xff\xfe not utf8 \x00\x01")
            design = root / "DESIGN.md"
            design.write_text(
                _minimal_maturity_probe_body(
                    "## Design Maturity\n\n- Status: Locked\n"
                    "- Lock authority: Pre-existing locked contract: binary.md\n"
                    "- Locked axes: color\n"
                ),
                encoding="utf-8",
            )
            rep = Reporter()
            check_design_maturity(
                design.read_text(encoding="utf-8"),
                rep,
                strict=True,
                contract_path=design,
            )
            if not rep.errors:
                failures.append("non-UTF-8 pre-existing target must fail validation")
    except UnicodeError:
        failures.append("non-UTF-8 pre-existing target raised UnicodeError")

    return failures


def run_maturity_self_tests() -> list[str]:
    """Self-test entry used by CLI and flow-check.

    Prefer the comprehensive repo-only suite when ``tests/test_design_maturity.py``
    is present. Fall back to the compact installable smoke suite otherwise so
    published packages never fail solely because tests/ was excluded from pack.
    """
    smoke = run_maturity_smoke_tests()
    repo_root = Path(__file__).resolve().parents[3]
    test_path = repo_root / "tests" / "test_design_maturity.py"
    if not test_path.is_file():
        return smoke

    import importlib.util

    spec = importlib.util.spec_from_file_location("ud_test_design_maturity", test_path)
    if spec is None or spec.loader is None:
        smoke.append(f"unable to load comprehensive maturity tests from {test_path}")
        return smoke
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as exc:  # pragma: no cover - defensive for broken checkout
        smoke.append(f"comprehensive maturity tests failed to import: {exc}")
        return smoke
    if not hasattr(mod, "run_maturity_self_tests"):
        smoke.append("comprehensive suite missing run_maturity_self_tests()")
        return smoke
    # Comprehensive suite is the source of truth in a full checkout.
    return list(mod.run_maturity_self_tests())


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
        if field == "Active references loaded" and not match:
            explicit = re.search(
                r"(?ims)^###\s+Active OKF Concepts\s*$\n(?P<body>.*?)(?=^###\s+|\Z)",
                preflight,
            )
            if explicit:
                if strict and not explicit.group("body").strip():
                    reporter.error("OKF Preflight subsection is empty: Active OKF Concepts")
                if not re.search(r"(?mi)^###\s+Support References\s*$", preflight):
                    message = "OKF Preflight subsection missing: Support References"
                    if strict:
                        reporter.error(message)
                    else:
                        reporter.warn(message)
                continue
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
    check_design_maturity(
        body,
        reporter,
        strict=strict_ultimate,
        contract_path=path,
    )

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
    parser.add_argument(
        "--self-test-maturity",
        action="store_true",
        help="Run Design Maturity regression cases and exit (ignores path).",
    )
    args = parser.parse_args()

    if args.self_test_maturity:
        failures = run_maturity_self_tests()
        if failures:
            print("DESIGN MATURITY SELF-TEST FAIL")
            for item in failures:
                print(f"FAIL {item}")
            return 1
        print("DESIGN MATURITY SELF-TEST PASS")
        return 0

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
