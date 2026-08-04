#!/usr/bin/env python3
"""Structural validation for Portable Specialist handoff blackboards.

Exact schema parsing only: no fuzzy substring OKF extraction, no heading spoofing
via contains-match, no last-one-wins field ambiguity. Does not score design quality
and does not enforce Active OKF count limits.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


SCHEMA = "ultimate-design.agent-handoff.v1"
EMPTY_VALUES = {"", "-", "none", "n/a", "na", "tbd", "todo", "placeholder", "…", "..."}
NULLABLE_NONE_OK = {"none"}
WO_STATUS = {"open", "in_progress", "done", "blocked"}
WO_EXECUTION = {"serial", "parallel"}
RESULT_STATUS = {"complete", "blocked", "waived"}
PROV_ROLES = {"owned", "cross-read"}

# Exact canonical segments: no dot segments, no absolute/backslash/traversal aliases.
_SEG = r"[A-Za-z0-9][A-Za-z0-9_-]*"
_OKF_BODY = rf"design-okf/(?:{_SEG}/)*{_SEG}\.md"
_PATH_BODY = rf"references/design-okf/(?:{_SEG}/)*{_SEG}\.md"
EXACT_OKF_RE = re.compile(rf"^{_OKF_BODY}$")
EXACT_MANIFEST_PATH_RE = re.compile(rf"^{_PATH_BODY}$")
# Exactly 64 lowercase hex characters. Uppercase is rejected (no case normalization).
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")

FIELD_RE = re.compile(
    r"(?m)^\s*[-*]\s+\*\*(?P<key>[^*:\n]+?):?\*\*:?\s*(?P<value>.*)$"
)
HEADING_WO_RE = re.compile(r"(?m)^# Work Order: (?P<id>\S+)\s*$")
HEADING_RESULT_RE = re.compile(r"(?m)^# Specialist Result: (?P<id>\S+)\s*$")
HEADING_INTEGRATION_RE = re.compile(r"(?m)^# Integration Ledger\s*$")
HEADING_VERIFICATION_RE = re.compile(r"(?m)^# Verification Ledger\s*$")
SECTION_RE = re.compile(
    r"(?ms)^## (?P<title>.+?)\s*$\n(?P<body>.*?)(?=^## |\Z)"
)

# Bare token OR one balanced backtick pair around the exact token (full line for lists).
OWNED_LIST_LINE_RE = re.compile(
    rf"^\s*[-*]\s+(?:`(?P<okf_t>{_OKF_BODY})`|(?P<okf_b>{_OKF_BODY}))\s*$"
)
PRIMARY_OWNED_LINE_RE = re.compile(
    rf"^\s*[-*]\s+Owned:\s+(?:`(?P<okf_t>{_OKF_BODY})`|(?P<okf_b>{_OKF_BODY}))\s*$",
    re.IGNORECASE,
)
# Full-bullet Cross-read: optional reason suffix only; no trailing garbage.
PRIMARY_CROSS_LINE_RE = re.compile(
    rf"^\s*[-*]\s+Cross-read(?:\s*/\s*reviewer)?(?:\s*\(not ownership\))?:\s+"
    rf"(?:`(?P<okf_t>{_OKF_BODY})`|(?P<okf_b>{_OKF_BODY}))"
    rf"(?:\s+—\s+reason:\s+\S.*)?\s*$",
    re.IGNORECASE,
)

INTEGRATION_H2 = [
    "Ownership map",
    "Conflict matrix",
    "Co-constraint pass",
    "Integration gates",
    "Final write authority",
]
VERIFICATION_H2 = [
    "Binding verification",
    "Request Anchor checks",
    "Rendered / production checks",
    "Structural validators",
    "Remaining risks",
    "Delivery decision",
]

# Neutral non-structural sentinel for fenced evidence inside a real section body.
# Counts as substance for section_has_substance but is not a heading/table/list schema.
FENCED_EVIDENCE_SENTINEL = "fenced-evidence-substance"

FENCE_OPEN_RE = re.compile(r"^(?P<indent>[ \t]{0,3})(?P<fence>(`{3,}|~{3,}))(?P<info>[^\n]*)$")


def strip_html_comments(text: str) -> str:
    """Mask HTML comments without changing line boundaries.

    - Closed ``<!-- ... -->`` spans: non-newline characters become spaces; CR/LF kept.
    - Unclosed ``<!--`` through EOF: same masking (comment continues to end of text).
    - Never inserts a newline, so inline comments cannot split a polluted H1 into a
      clean heading line plus trailing junk on the next line.
    """
    out: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        if text.startswith("<!--", i):
            close = text.find("-->", i + 4)
            end = n if close < 0 else close + 3
            for k in range(i, end):
                ch = text[k]
                out.append(ch if ch in "\r\n" else " ")
            i = end
            continue
        out.append(text[i])
        i += 1
    return "".join(out)


def strip_fenced_blocks(text: str) -> str:
    """Replace CommonMark backtick/tilde fenced blocks with a non-structural sentinel.

    Opening fences of 3+ ` or ~ close only with a matching fence of the same character
    and at least the same length (CommonMark-style, lightweight).
    """
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Match without trailing newline for the open regex.
        bare = line[:-1] if line.endswith("\n") else line
        if bare.endswith("\r"):
            bare = bare[:-1]
        m = FENCE_OPEN_RE.match(bare)
        if not m:
            out.append(line)
            i += 1
            continue
        fence = m.group("fence")
        marker = fence[0]
        min_len = len(fence)
        i += 1
        closed = False
        while i < len(lines):
            close_bare = lines[i][:-1] if lines[i].endswith("\n") else lines[i]
            if close_bare.endswith("\r"):
                close_bare = close_bare[:-1]
            close_m = re.match(
                rf"^[ \t]{{0,3}}{re.escape(marker)}{{{min_len},}}[ \t]*$",
                close_bare,
            )
            if close_m:
                closed = True
                i += 1
                break
            i += 1
        # Whether or not closed, structural content inside the fence is discarded.
        out.append(f"- {FENCED_EVIDENCE_SENTINEL}\n")
        if not closed:
            # Unclosed fence: remainder already consumed; leave a note via sentinel only.
            pass
    return "".join(out)


def structure_safe_view(text: str) -> str:
    """Structure-safe Markdown view for H1/H2/fields/lists/tables.

    Content inside HTML comments and CommonMark fenced blocks does not count as
    structural headings, metadata fields, list schemas, or tables. Fenced regions
    become a neutral substance sentinel so legitimate evidence remains non-empty.

    Order: fenced blocks first, then HTML comments. That way an unclosed comment
    token inside legitimate fenced evidence cannot swallow real structure after
    the closing fence.
    """
    return strip_html_comments(strip_fenced_blocks(text))


def first_nonblank_structural_lines(view: str) -> list[str]:
    return [ln.strip() for ln in view.splitlines() if ln.strip()]


def is_only_fence_sentinels(view: str) -> bool:
    """True when the structural view has no real content beyond fence placeholders."""
    lines = first_nonblank_structural_lines(view)
    if not lines:
        return True
    sentinel_line = f"- {FENCED_EVIDENCE_SENTINEL}"
    return all(ln == sentinel_line for ln in lines)


def is_atx_h1(line: str) -> bool:
    return bool(re.match(r"^#\s+\S", line)) and not line.startswith("##")


def require_leading_h1(
    text: str,
    pattern: re.Pattern[str],
    *,
    label: str,
    expected_h1: str,
) -> tuple[str | None, list[str]]:
    """Require exactly one matching H1 as the first structural nonblank line."""
    errors: list[str] = []
    view = structure_safe_view(text)
    lines = first_nonblank_structural_lines(view)
    if not lines or is_only_fence_sentinels(view):
        return None, [
            f"{label}: empty structural content after removing fences/comments "
            f"(document may be wholly fenced or commented out)"
        ]
    h1_lines = [ln for ln in lines if is_atx_h1(ln)]
    if len(h1_lines) == 0:
        errors.append(f"{label} missing exact H1 '{expected_h1}'")
        return None, errors
    if len(h1_lines) > 1:
        errors.append(f"{label} has multiple H1 headings: {h1_lines!r}")
    if not is_atx_h1(lines[0]):
        errors.append(
            f"{label}: H1 must be the first nonblank structural line, found {lines[0]!r}"
        )
    match = pattern.match(lines[0]) if is_atx_h1(lines[0]) else None
    if match is None:
        # Also try the first H1 if first line failed pattern but was H1-shaped.
        if is_atx_h1(lines[0]):
            errors.append(
                f"{label} H1 must match '{expected_h1}', found {lines[0]!r}"
            )
        return None, errors
    return match.groupdict().get("id") or lines[0], errors


def unwrap_md_token(cell: str) -> str | None:
    """Accept bare token or exactly one balanced backtick pair; reject fences otherwise."""
    text = cell.strip()
    if not text:
        return None
    if text.startswith("`"):
        if len(text) >= 2 and text.endswith("`") and text.count("`") == 2:
            return text[1:-1]
        return None
    if "`" in text:
        return None
    return text


def is_empty_or_placeholder(value: str) -> bool:
    return value.strip().lower() in EMPTY_VALUES


def is_filled(value: str) -> bool:
    return not is_empty_or_placeholder(value)


def is_none_token(value: str) -> bool:
    return value.strip().lower() in NULLABLE_NONE_OK


def parse_exact_okf(cell: str) -> str | None:
    text = unwrap_md_token(cell)
    if text is None:
        return None
    if EXACT_OKF_RE.fullmatch(text):
        return text
    return None


def parse_exact_manifest_path(cell: str) -> str | None:
    text = unwrap_md_token(cell)
    if text is None:
        return None
    if EXACT_MANIFEST_PATH_RE.fullmatch(text):
        return text
    return None


def parse_sha256_md(cell: str) -> str | None:
    """Markdown table SHA: bare or one backtick pair; must already be lowercase hex."""
    text = unwrap_md_token(cell)
    if text is None:
        return None
    if SHA256_RE.fullmatch(text):
        return text
    return None


def parse_sha256_json(value: object) -> str | None:
    """JSON manifest SHA: raw string only; exact 64 lowercase hex; no Markdown."""
    if not isinstance(value, str):
        return None
    if SHA256_RE.fullmatch(value):
        return value
    return None


def parse_manifest_path_json(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    if EXACT_MANIFEST_PATH_RE.fullmatch(value):
        return value
    return None


def parse_manifest_owner_json(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    if not value or any(ch.isspace() for ch in value) or "`" in value:
        return None
    return value


def okf_to_manifest_path(okf: str) -> str:
    return f"references/{okf}"


def parse_fields(text: str) -> tuple[dict[str, str], list[str]]:
    """Parse metadata fields from the structure-safe view only."""
    view = structure_safe_view(text)
    fields: dict[str, str] = {}
    duplicates: list[str] = []
    for match in FIELD_RE.finditer(view):
        key = match.group("key").strip().lower().replace(" ", "_")
        value = match.group("value").strip()
        if key in fields:
            duplicates.append(key)
        fields[key] = value
    return fields, duplicates


def sections_exact(text: str) -> tuple[dict[str, str], list[str]]:
    """Exact H2 map on structure-safe view; reject last-one-wins duplicates."""
    view = structure_safe_view(text)
    out: dict[str, str] = {}
    duplicates: list[str] = []
    for match in SECTION_RE.finditer(view):
        title = match.group("title").strip()
        key = title.lower()
        if key in out:
            duplicates.append(title)
            continue
        out[key] = match.group("body")
    return out, duplicates


def require_section(bodies: dict[str, str], exact_title: str) -> str | None:
    return bodies.get(exact_title.lower())


def table_data_rows(body: str) -> list[list[str]]:
    """Return raw whitespace-stripped cells (no Markdown fence stripping)."""
    rows: list[list[str]] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if not cells:
            continue
        if all(set(c) <= {"-", ":"} for c in cells):
            continue
        first = unwrap_md_token(cells[0])
        first_l = (first or cells[0]).lower()
        if first_l in {
            "reference",
            "okf reference",
            "active okf",
            "conflict",
            "constraint pair",
            "check",
            "validator",
        }:
            continue
        rows.append(cells)
    return rows


def section_has_substance(body: str | None, *, allow_none: bool = False) -> bool:
    if body is None:
        return False
    lines: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("<!--"):
            continue
        content = re.sub(r"^[-*+]\s+", "", stripped)
        content = content.strip("| ").strip()
        if not content or set(content) <= {"-", ":"}:
            continue
        lines.append(content)
    if not lines:
        return False
    if allow_none and any(is_none_token(line) for line in lines) and all(
        is_none_token(line) or is_empty_or_placeholder(line) for line in lines
    ):
        return True
    return any(is_filled(line) for line in lines)


def _line_okf(match: re.Match[str]) -> str:
    return match.group("okf_t") or match.group("okf_b")


def parse_owned_section(body: str | None) -> tuple[list[str], list[str]]:
    """Return (owned_okfs, errors)."""
    errors: list[str] = []
    if body is None:
        return [], ["Active OKF ownership section missing"]
    owned: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("<!--"):
            continue
        if not stripped.startswith(("-", "*")):
            continue
        m = OWNED_LIST_LINE_RE.match(stripped)
        if not m:
            if re.match(r"^\s*[-*]\s+\S", stripped):
                errors.append(f"Non-exact Active ownership line: {stripped}")
            continue
        okf = _line_okf(m)
        if okf in owned:
            errors.append(f"Duplicate owned Active OKF: {okf}")
        else:
            owned.append(okf)
    if not owned:
        errors.append("Active OKF ownership is empty")
    return owned, errors


def parse_primary_read_section(body: str | None) -> tuple[list[str], list[str], list[str]]:
    """Return (owned_listed, cross_reads, errors)."""
    errors: list[str] = []
    if body is None:
        return [], [], ["Primary / read OKF references section missing"]
    owned: list[str] = []
    cross: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("<!--"):
            continue
        if not stripped.startswith(("-", "*")):
            continue
        mo = PRIMARY_OWNED_LINE_RE.match(stripped)
        if mo:
            okf = _line_okf(mo)
            if okf in owned:
                errors.append(f"Duplicate Owned line in Primary / read: {okf}")
            else:
                owned.append(okf)
            continue
        mc = PRIMARY_CROSS_LINE_RE.match(stripped)
        if mc:
            okf = _line_okf(mc)
            if okf in cross or okf in owned:
                errors.append(f"Duplicate Primary / read OKF: {okf}")
            else:
                cross.append(okf)
            continue
        if re.match(r"^\s*[-*]\s+\S", stripped):
            errors.append(f"Non-exact Primary / read line: {stripped}")
    if not owned and not cross:
        errors.append("Primary / read OKF references is empty")
    return owned, cross, errors


def parse_binding_section(body: str | None) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    if body is None:
        return [], ["Binding proposals section missing"]
    rows_out: list[dict[str, str]] = []
    for cells in table_data_rows(body):
        if len(cells) != 4:
            errors.append(
                f"Binding row must have exactly 4 columns, got {len(cells)}: {cells!r}"
            )
            continue
        reference, decision, target, verification = cells
        okf = parse_exact_okf(reference)
        if okf is None:
            errors.append(f"Malformed or non-exact binding reference: {reference!r}")
            continue
        if not is_filled(decision) or not is_filled(target) or not is_filled(verification):
            errors.append(f"Incomplete binding: {okf}")
            continue
        rows_out.append(
            {
                "okf": okf,
                "decision": decision,
                "artifact_target": target,
                "verification": verification,
            }
        )
    return rows_out, errors


def parse_provenance_section(body: str | None) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    if body is None:
        return [], ["OKF / hash provenance section missing"]
    rows_out: list[dict[str, str]] = []
    for cells in table_data_rows(body):
        if len(cells) != 4:
            errors.append(
                f"Provenance row must have exactly 4 columns, got {len(cells)}: {cells!r}"
            )
            continue
        okf_cell, path_cell, sha_cell, role_cell = cells
        okf = parse_exact_okf(okf_cell)
        path = parse_exact_manifest_path(path_cell)
        sha = parse_sha256_md(sha_cell)
        role = unwrap_md_token(role_cell)
        if okf is None:
            errors.append(f"Provenance OKF not exact: {okf_cell!r}")
            continue
        if path is None:
            errors.append(f"Provenance manifest path not exact canonical: {path_cell!r}")
            continue
        if sha is None:
            errors.append(
                f"Provenance sha256 must be exactly 64 lowercase hex characters: {sha_cell!r}"
            )
            continue
        if role not in PROV_ROLES:
            errors.append(f"Provenance role must be owned|cross-read: {role_cell!r}")
            continue
        if path != okf_to_manifest_path(okf):
            errors.append(
                f"Provenance path/reference disagreement for {okf}: path={path}"
            )
            continue
        rows_out.append({"okf": okf, "path": path, "sha256": sha, "role": role})
    if not rows_out and not errors:
        errors.append("OKF / hash provenance is empty")
    return rows_out, errors


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_skill_root(blackboard: Path, skill_root: Path | None) -> Path | None:
    if skill_root is not None:
        return skill_root.resolve()
    for parent in [blackboard.resolve(), *blackboard.resolve().parents]:
        if (parent / "SKILL.md").exists() and (parent / "references" / "design-okf").is_dir():
            return parent
    return None


def resolve_canonical_file(skill_root: Path, canonical_path: str) -> tuple[Path | None, str | None]:
    if not EXACT_MANIFEST_PATH_RE.fullmatch(canonical_path):
        return None, f"non-canonical path: {canonical_path}"
    okf_tree = (skill_root / "references" / "design-okf").resolve()
    target = (skill_root / canonical_path).resolve()
    try:
        target.relative_to(okf_tree)
    except ValueError:
        return None, f"path escapes design-okf tree: {canonical_path}"
    if target.is_symlink():
        real = target.resolve()
        try:
            real.relative_to(okf_tree)
        except ValueError:
            return None, f"symlink escapes design-okf tree: {canonical_path}"
        target = real
    if not target.exists():
        return None, f"missing file: {canonical_path}"
    if not target.is_file():
        return None, f"not a regular file: {canonical_path}"
    return target, None


def ledger_ok(path: Path, *, h1_re: re.Pattern[str], h1_label: str, required_h2: list[str]) -> list[str]:
    errors: list[str] = []
    name = path.name
    if not path.exists():
        return [f"Required blackboard artifact missing: {name}"]
    if not path.is_file():
        return [f"Required blackboard artifact is not a regular file: {name}"]
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return [f"Required blackboard artifact is empty: {name}"]
    _h1_id, h1_errs = require_leading_h1(
        text, h1_re, label=name, expected_h1=h1_label
    )
    errors.extend(h1_errs)
    bodies, dups = sections_exact(text)
    for title in dups:
        errors.append(f"{name} has duplicate H2 section: {title}")
    for title in required_h2:
        if title.lower() not in bodies:
            errors.append(f"{name} missing required H2 heading: {title}")
    return errors


def validate_tree(
    root: Path,
    require_hashes: bool = False,
    skill_root: Path | None = None,
) -> tuple[int, dict[str, object]]:
    errors: list[str] = []
    warnings: list[str] = []
    root = root.resolve()
    resolved_skill_root = resolve_skill_root(root, skill_root)
    if resolved_skill_root is None:
        errors.append("skill root could not be resolved; pass --skill-root")

    work_orders_dir = root / "work-orders"
    results_dir = root / "specialist-results"
    if not work_orders_dir.is_dir():
        errors.append("work-orders/ directory missing")
    if not results_dir.is_dir():
        errors.append("specialist-results/ directory missing")

    errors.extend(
        ledger_ok(
            root / "integration-ledger.md",
            h1_re=HEADING_INTEGRATION_RE,
            h1_label="# Integration Ledger",
            required_h2=INTEGRATION_H2,
        )
    )
    errors.extend(
        ledger_ok(
            root / "verification-ledger.md",
            h1_re=HEADING_VERIFICATION_RE,
            h1_label="# Verification Ledger",
            required_h2=VERIFICATION_H2,
        )
    )

    work_orders: dict[str, dict[str, object]] = {}
    seen_wo_ids: dict[str, str] = {}
    wo_files = sorted(work_orders_dir.glob("*.md")) if work_orders_dir.is_dir() else []
    if work_orders_dir.is_dir() and not wo_files:
        errors.append("work-orders/ contains no work order files")

    for path in wo_files:
        text = path.read_text(encoding="utf-8")
        fields, dups = parse_fields(text)
        for key in dups:
            errors.append(f"Duplicate schema field '{key}' in work order {path.name}")
        heading_id, h1_errs = require_leading_h1(
            text,
            HEADING_WO_RE,
            label=f"Work order {path.name}",
            expected_h1="# Work Order: <id>",
        )
        errors.extend(h1_errs)
        order_id = fields.get("id", "").strip()
        if not order_id:
            errors.append(f"Work order missing explicit id field: {path.name}")
            continue
        if heading_id and order_id != heading_id:
            errors.append(
                f"Work order id field '{order_id}' does not match H1 '{heading_id}'"
            )
        if order_id != path.stem:
            errors.append(
                f"Work order id field '{order_id}' does not match file stem '{path.stem}'"
            )
        if order_id in seen_wo_ids:
            errors.append(
                f"Duplicate work-order id '{order_id}': {seen_wo_ids[order_id]} and {path.name}"
            )
            continue
        seen_wo_ids[order_id] = path.name

        if not is_filled(fields.get("owner", "")):
            errors.append(f"Work order missing owner: {order_id}")
        status = fields.get("status", "").strip().lower().replace(" ", "_")
        if status not in WO_STATUS:
            errors.append(
                f"Work order has invalid or missing status (open|in_progress|done|blocked): {order_id}"
            )
        execution = fields.get("execution", "").strip().lower()
        if execution not in WO_EXECUTION:
            errors.append(
                f"Work order has invalid or missing execution (serial|parallel): {order_id}"
            )
        for key in (
            "request_anchor_ref",
            "request_anchor_digest",
            "artifact_path",
            "artifact_version",
            "artifact_hash",
            "manifest_path",
        ):
            if not is_filled(fields.get(key, "")):
                errors.append(f"Work order missing {key}: {order_id}")
        if is_filled(fields.get("manifest_path", "")) and fields.get(
            "manifest_path", ""
        ).strip() not in {"okf-read-manifest.json", "./okf-read-manifest.json"}:
            errors.append(
                f"Work order manifest_path must be okf-read-manifest.json: {order_id}"
            )

        bodies, section_dups = sections_exact(text)
        for title in section_dups:
            errors.append(f"Work order has duplicate H2 section '{title}': {order_id}")
        contract = require_section(bodies, "Applicable design-contract constraints")
        if not section_has_substance(contract):
            errors.append(
                f"Work order missing non-placeholder design-contract constraints: {order_id}"
            )

        owned, owned_errs = parse_owned_section(
            require_section(bodies, "Active OKF ownership (accountable)")
        )
        for err in owned_errs:
            errors.append(f"{err} ({order_id})")

        primary_owned, cross_reads, primary_errs = parse_primary_read_section(
            require_section(bodies, "Primary / read OKF references")
        )
        for err in primary_errs:
            errors.append(f"{err} ({order_id})")

        # Every owned Active must be explicitly repeated under Primary as Owned.
        for okf in owned:
            if okf not in primary_owned:
                errors.append(
                    f"Owned Active {okf} not repeated as Owned in Primary / read ({order_id})"
                )
        for okf in primary_owned:
            if okf not in owned:
                errors.append(
                    f"Primary Owned {okf} is not in Active OKF ownership ({order_id})"
                )
        for okf in cross_reads:
            if okf in owned:
                errors.append(
                    f"OKF {okf} cannot be both owned and cross-read ({order_id})"
                )

        declared_reads = sorted(set(owned) | set(cross_reads))
        if not declared_reads:
            errors.append(f"Work order has no declared read OKF references: {order_id}")

        forbidden = require_section(bodies, "Explicit forbidden / out-of-scope")
        if not section_has_substance(forbidden):
            errors.append(
                f"Work order missing explicit forbidden/out-of-scope content: {order_id}"
            )
        expected = require_section(bodies, "Expected result / return schema")
        if not section_has_substance(expected):
            errors.append(f"Work order missing expected result/return schema: {order_id}")
        targets = require_section(bodies, "Artifact targets")
        if not section_has_substance(targets):
            errors.append(f"Work order missing artifact targets: {order_id}")
        verify = require_section(bodies, "Verification obligations")
        if not section_has_substance(verify):
            errors.append(f"Work order missing verification obligations: {order_id}")

        work_orders[order_id] = {
            "path": str(path.relative_to(root)),
            "owner": fields.get("owner", ""),
            "active_okf": owned,
            "primary_owned": primary_owned,
            "cross_reads": cross_reads,
            "declared_reads": declared_reads,
            "fields": fields,
        }

    results: dict[str, dict[str, object]] = {}
    seen_result_ids: dict[str, str] = {}
    result_files = sorted(results_dir.glob("*.md")) if results_dir.is_dir() else []

    for path in result_files:
        text = path.read_text(encoding="utf-8")
        fields, dups = parse_fields(text)
        for key in dups:
            errors.append(f"Duplicate schema field '{key}' in specialist result {path.name}")
        heading_id, h1_errs = require_leading_h1(
            text,
            HEADING_RESULT_RE,
            label=f"Specialist result {path.name}",
            expected_h1="# Specialist Result: <id>",
        )
        errors.extend(h1_errs)
        work_order_id = fields.get("work_order_id", "").strip()
        if not work_order_id:
            errors.append(f"Specialist result missing explicit work_order_id: {path.name}")
            continue
        if heading_id and work_order_id != heading_id:
            errors.append(
                f"Specialist result work_order_id '{work_order_id}' does not match H1 '{heading_id}'"
            )
        if work_order_id != path.stem:
            errors.append(
                f"Specialist result work_order_id '{work_order_id}' does not match file stem '{path.stem}'"
            )
        if work_order_id in seen_result_ids:
            errors.append(
                f"Duplicate specialist-result id '{work_order_id}': "
                f"{seen_result_ids[work_order_id]} and {path.name}"
            )
            continue
        seen_result_ids[work_order_id] = path.name

        if work_order_id not in work_orders:
            errors.append(f"Specialist result has no matching work order: {work_order_id}")

        if not is_filled(fields.get("specialist", "")):
            errors.append(f"Specialist result missing specialist: {work_order_id}")
        status = fields.get("status", "").strip().lower()
        if status not in RESULT_STATUS:
            errors.append(
                f"Specialist result has invalid or missing status "
                f"(complete|blocked|waived): {work_order_id}"
            )
        source = fields.get("source_work_order", "").strip()
        if not source:
            errors.append(f"Specialist result missing source_work_order: {work_order_id}")
        elif source != work_order_id:
            errors.append(
                f"Specialist result source_work_order '{source}' must equal work_order_id "
                f"'{work_order_id}'"
            )

        bodies, section_dups = sections_exact(text)
        for title in section_dups:
            errors.append(
                f"Specialist result has duplicate H2 section '{title}': {work_order_id}"
            )
        for title, label, allow_none in (
            ("Findings", "findings", False),
            ("Proposed changes", "proposed changes", False),
            ("Dependencies on other clusters", "dependencies on other clusters", True),
            ("Local verification evidence", "local verification evidence", False),
            ("Unresolved questions", "unresolved questions", True),
            ("Conflicts / risks", "conflicts/risks", True),
        ):
            body = require_section(bodies, title)
            if not section_has_substance(body, allow_none=allow_none):
                errors.append(f"Specialist result missing {label}: {work_order_id}")

        prov_rows, prov_errs = parse_provenance_section(
            require_section(bodies, "OKF / hash provenance")
        )
        for err in prov_errs:
            errors.append(f"{err} in result {work_order_id}")

        bind_rows, bind_errs = parse_binding_section(
            require_section(bodies, "Binding proposals")
        )
        for err in bind_errs:
            errors.append(f"{err} in result {work_order_id}")

        owned = list(work_orders.get(work_order_id, {}).get("active_okf", []))
        cross = list(work_orders.get(work_order_id, {}).get("cross_reads", []))
        declared = list(work_orders.get(work_order_id, {}).get("declared_reads", []))

        # Provenance: every declared read exactly once; roles agree; no extras.
        prov_by_okf: dict[str, dict[str, str]] = {}
        for row in prov_rows:
            okf = row["okf"]
            if okf in prov_by_okf:
                errors.append(
                    f"Duplicate provenance row for {okf} in result {work_order_id}"
                )
                continue
            prov_by_okf[okf] = row
            expected_role = "owned" if okf in owned else "cross-read" if okf in cross else None
            if expected_role is None:
                errors.append(
                    f"Provenance undeclared OKF {okf} in result {work_order_id}"
                )
            elif row["role"] != expected_role:
                errors.append(
                    f"Provenance role for {okf} is {row['role']}, expected {expected_role} "
                    f"in result {work_order_id}"
                )
        for okf in declared:
            if okf not in prov_by_okf:
                errors.append(
                    f"Declared read {okf} missing from provenance in result {work_order_id}"
                )

        # Bindings: only owned Actives; every owned Active has >=1 complete row.
        bound_counts: dict[str, int] = {}
        for row in bind_rows:
            okf = row["okf"]
            if okf not in owned:
                errors.append(
                    f"Binding for non-owned OKF {okf} in result {work_order_id} "
                    f"(cross-read decisions are not accountable binding rows)"
                )
                continue
            bound_counts[okf] = bound_counts.get(okf, 0) + 1
        for okf in owned:
            if bound_counts.get(okf, 0) < 1:
                errors.append(
                    f"Owned Active OKF has no complete matching binding in result "
                    f"{work_order_id}: {okf}"
                )

        results[work_order_id] = {
            "path": str(path.relative_to(root)),
            "bound_counts": bound_counts,
            "provenance": prov_rows,
            "fields": fields,
        }

    for order_id in work_orders:
        if order_id not in results:
            errors.append(f"Work order has no specialist result: {order_id}")

    ownership: dict[str, list[str]] = {}
    for order_id, order in work_orders.items():
        for concept in order["active_okf"]:  # type: ignore[index]
            ownership.setdefault(str(concept), []).append(order_id)
    for concept, owners in ownership.items():
        if len(owners) > 1:
            errors.append(
                f"Duplicate accountable ownership of Active OKF {concept}: {owners}"
            )

    # --- Manifest (always required) ---
    manifest_path = root / "okf-read-manifest.json"
    hash_report: dict[str, object] | None = None
    pair_index: dict[tuple[str, str], dict[str, object]] = {}

    if not manifest_path.exists():
        errors.append("Required blackboard artifact missing: okf-read-manifest.json")
    elif not manifest_path.is_file():
        errors.append("okf-read-manifest.json is not a regular file")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"okf-read-manifest.json is not valid JSON: {exc}")
            manifest = None

        if manifest is not None and not isinstance(manifest, list):
            errors.append(
                "okf-read-manifest.json must be a nonempty JSON array of {path, sha256, owner}"
            )
        elif isinstance(manifest, list):
            if len(manifest) == 0:
                errors.append("okf-read-manifest.json is empty")
            hash_report = {
                "checked": 0,
                "mismatches": [],
                "entries": [],
                "require_hashes": require_hashes,
            }
            for index, entry in enumerate(manifest):
                if not isinstance(entry, dict):
                    errors.append(f"Manifest entry {index} is not an object")
                    continue
                rel = entry.get("path")
                expected = entry.get("sha256")
                owner = entry.get("owner")
                if not is_filled(str(rel or "")):
                    errors.append(f"Manifest entry {index} missing path")
                    continue
                if not is_filled(str(expected or "")):
                    errors.append(f"Manifest entry {index} missing sha256: {rel}")
                    continue
                if not is_filled(str(owner or "")):
                    errors.append(f"Manifest entry {index} missing owner: {rel}")
                    continue

                # JSON values are raw schema values: strings only, no Markdown fences.
                if not isinstance(rel, str) or not isinstance(expected, str) or not isinstance(owner, str):
                    errors.append(
                        f"Manifest entry {index} path/sha256/owner must be JSON strings"
                    )
                    continue
                owner_str = parse_manifest_owner_json(owner)
                if owner_str is None:
                    errors.append(
                        f"Manifest entry {index} owner must be a non-empty string without "
                        f"whitespace or Markdown: {owner!r}"
                    )
                    continue
                sha = parse_sha256_json(expected)
                if sha is None:
                    errors.append(
                        f"Manifest entry {index} sha256 must be exactly 64 lowercase hex "
                        f"characters: {expected!r}"
                    )
                    continue
                path_exact = parse_manifest_path_json(rel)
                if path_exact is None:
                    if rel.startswith("/") or re.match(r"^[A-Za-z]:[\\/]", rel):
                        errors.append(
                            f"Manifest entry {index}: absolute paths are forbidden: {rel}"
                        )
                    elif ".." in Path(rel).parts or "\\" in rel:
                        errors.append(
                            f"Manifest entry {index}: path traversal is forbidden: {rel}"
                        )
                    elif "`" in rel:
                        errors.append(
                            f"Manifest entry {index}: Markdown backticks are forbidden in "
                            f"JSON path: {rel!r}"
                        )
                    else:
                        errors.append(
                            f"Manifest entry {index}: path must be exact canonical "
                            f"references/design-okf/...md: {rel}"
                        )
                    continue

                okf = path_exact[len("references/") :]
                key = (path_exact, owner_str)
                if key in pair_index:
                    errors.append(
                        f"Duplicate manifest entry for path/owner ({path_exact}, {owner_str})"
                    )
                    continue

                target = None
                if resolved_skill_root is not None:
                    target, path_err = resolve_canonical_file(resolved_skill_root, path_exact)
                    if path_err:
                        errors.append(f"Manifest entry {index}: {path_err}")
                        continue

                pair_index[key] = {
                    "path": path_exact,
                    "sha256": sha,
                    "owner": owner_str,
                    "okf": okf,
                    "target": str(target) if target else None,
                }

                if require_hashes and target is not None:
                    actual = sha256_file(target)
                    hash_report["checked"] = int(hash_report["checked"]) + 1
                    hash_report["entries"].append(  # type: ignore[index]
                        {"path": path_exact, "owner": owner_str, "okf": okf}
                    )
                    if actual != sha:
                        hash_report["mismatches"].append(  # type: ignore[index]
                            {"path": path_exact, "expected": sha, "actual": actual}
                        )
                        errors.append(f"Hash mismatch for {path_exact}")

            # Bidirectional agreement: declared reads <-> manifest entries.
            for order_id, order in work_orders.items():
                for okf in order["declared_reads"]:  # type: ignore[index]
                    canonical = okf_to_manifest_path(str(okf))
                    key = (canonical, order_id)
                    if key not in pair_index:
                        errors.append(
                            f"Manifest missing read coverage for ({canonical}, owner={order_id})"
                        )
                    else:
                        if okf in order["active_okf"] and pair_index[key]["owner"] != order_id:
                            errors.append(
                                f"Manifest owner for owned Active {canonical} must equal "
                                f"accountable work-order id '{order_id}', got "
                                f"'{pair_index[key]['owner']}'"
                            )

            for (canonical, owner_str), entry in pair_index.items():
                okf = str(entry["okf"])
                if owner_str not in work_orders:
                    if okf in ownership:
                        errors.append(
                            f"Manifest owner '{owner_str}' is not the accountable work-order "
                            f"for {canonical} (accountable: {ownership[okf]})"
                        )
                    else:
                        errors.append(
                            f"Manifest owner '{owner_str}' is not a known work-order id "
                            f"for {canonical}"
                        )
                    continue
                declared = set(work_orders[owner_str]["declared_reads"])  # type: ignore[arg-type]
                if okf not in declared:
                    errors.append(
                        f"Manifest entry undeclared by owner work order {owner_str}: {canonical}"
                    )

            # Provenance agrees with manifest path+sha in normal mode.
            for order_id, result in results.items():
                for row in result.get("provenance", []):  # type: ignore[union-attr]
                    if not isinstance(row, dict):
                        continue
                    okf = row.get("okf") or ""
                    canonical = okf_to_manifest_path(str(okf))
                    key = (canonical, order_id)
                    if key not in pair_index:
                        # already covered by declared/provenance checks
                        continue
                    entry = pair_index[key]
                    if row.get("path") != entry["path"]:
                        errors.append(
                            f"Provenance path disagrees with manifest for {okf} "
                            f"in result {order_id}"
                        )
                    if row.get("sha256") != entry["sha256"]:
                        errors.append(
                            f"Provenance sha256 disagrees with manifest for {okf} "
                            f"in result {order_id}"
                        )

    summary: dict[str, object] = {
        "schemaVersion": SCHEMA,
        "path": str(root),
        "skill_root": str(resolved_skill_root) if resolved_skill_root else None,
        "require_hashes": require_hashes,
        "work_orders": work_orders,
        "specialist_results": results,
        "ownership": ownership,
        "manifest_entries": [
            {k: v for k, v in e.items() if k != "target"} for e in pair_index.values()
        ],
        "hash_report": hash_report,
        "warnings": warnings,
        "errors": errors,
        "status": "pass" if not errors else "fail",
    }
    return (0 if not errors else 1), summary


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Portable Specialist work-order/result blackboard structure."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Blackboard root containing work-orders/, specialist-results/, ledgers, and manifest",
    )
    parser.add_argument(
        "--require-hashes",
        action="store_true",
        help=(
            "Additionally verify exact sha256 of every manifest path against files under "
            "--skill-root (or auto-detected skill root)."
        ),
    )
    parser.add_argument(
        "--skill-root",
        default=None,
        help="Skill package root containing SKILL.md and references/design-okf.",
    )
    parser.add_argument("--json", action="store_true", help="Print the full JSON report.")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        print(f"ERROR path not found: {root}", file=sys.stderr)
        return 2

    skill_root = Path(args.skill_root).resolve() if args.skill_root else None
    code, summary = validate_tree(root, require_hashes=args.require_hashes, skill_root=skill_root)
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"AGENT HANDOFF VALIDATION {str(summary['status']).upper()}")
        print(f"Checked: {root}")
        if summary.get("skill_root"):
            print(f"Skill root: {summary['skill_root']}")
        print(f"Work orders: {len(summary['work_orders'])}")  # type: ignore[arg-type]
        print(f"Specialist results: {len(summary['specialist_results'])}")  # type: ignore[arg-type]
        for warning in summary["warnings"]:  # type: ignore[union-attr]
            print(f"WARN {warning}")
        for error in summary["errors"]:  # type: ignore[union-attr]
            print(f"ERROR {error}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
