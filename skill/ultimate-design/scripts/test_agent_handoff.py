#!/usr/bin/env python3
"""Deterministic structural tests for validate_agent_handoff.py.

Uses on-disk fixtures plus temp mutations for adversarial cases A-E and more.
Does not score design quality or enforce Active OKF count limits.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
import validate_agent_handoff as vah  # noqa: E402


SKILL_ROOT = SCRIPT_DIR.parent
FIXTURES = SKILL_ROOT / "test-fixtures" / "agent-handoff"


def run_case(path: Path, *, require_hashes: bool = False) -> tuple[int, list[str]]:
    code, summary = vah.validate_tree(
        path, require_hashes=require_hashes, skill_root=SKILL_ROOT
    )
    return code, list(summary.get("errors") or [])


def expect_fail(name: str, path: Path, needle: str, *, require_hashes: bool = False) -> None:
    code, errors = run_case(path, require_hashes=require_hashes)
    joined = "\n".join(errors)
    if code == 0:
        raise AssertionError(f"{name}: expected failure, got pass")
    if needle.lower() not in joined.lower():
        raise AssertionError(
            f"{name}: expected error containing {needle!r}, got:\n{joined}"
        )
    print(f"PASS fail:{name} ({needle})")


def expect_pass(name: str, path: Path, *, require_hashes: bool = False) -> None:
    code, errors = run_case(path, require_hashes=require_hashes)
    if code != 0:
        raise AssertionError(f"{name}: expected pass, got errors:\n" + "\n".join(errors))
    print(f"PASS pass:{name}")


def mutate_copy(src: Path) -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="ud-handoff-"))
    shutil.copytree(src, tmp / "bb")
    return tmp / "bb"


def main() -> int:
    failures = 0

    def guard(fn):
        nonlocal failures
        try:
            fn()
        except Exception as exc:  # noqa: BLE001
            failures += 1
            print(f"FAIL {fn.__name__}: {exc}")

    def test_valid_normal():
        expect_pass("valid-normal", FIXTURES / "valid")

    def test_valid_hashes():
        expect_pass("valid-require-hashes", FIXTURES / "valid", require_hashes=True)

    def test_static_invalids():
        cases = [
            ("invalid-missing-result", "Work order has no specialist result"),
            ("invalid-incomplete-binding", "Incomplete binding"),
            ("invalid-duplicate-ownership", "Duplicate accountable ownership"),
            ("invalid-partial-bindings", "no complete matching binding"),
            ("invalid-missing-ledgers", "Required blackboard artifact missing: integration-ledger.md"),
            ("invalid-wrong-owner", "not the accountable work-order"),
            ("invalid-missing-manifest", "okf-read-manifest.json"),
            ("invalid-absolute-path", "absolute paths are forbidden"),
            ("invalid-missing-schema-fields", "missing status"),
            ("invalid-provenance-as-binding", "Binding proposals section missing"),
            ("invalid-duplicate-ids", "Duplicate work-order id"),
        ]
        for folder, needle in cases:
            expect_fail(folder, FIXTURES / folder, needle)

    def test_manifest_hash_mismatch():
        expect_fail(
            "invalid-manifest-hash",
            FIXTURES / "invalid-manifest",
            "Hash mismatch",
            require_hashes=True,
        )

    # --- Codex second-round A-E ---

    def test_A_blank_provenance_cells():
        """A. Owned provenance row blank path/sha/role must fail under --require-hashes."""
        bb = mutate_copy(FIXTURES / "valid")
        res = bb / "specialist-results" / "wo-narrative.md"
        text = res.read_text()
        text = text.replace(
            "| `design-okf/content/message-model.md` | `references/design-okf/content/message-model.md` | d50ccbae698c30356ef21ed70d261de7813c2701627ce9dca31defcf82d0d82a | owned |",
            "| `design-okf/content/message-model.md` |  |  |  |",
        )
        res.write_text(text)
        expect_fail(
            "A-blank-provenance",
            bb,
            "Provenance manifest path not exact",
            require_hashes=True,
        )
        shutil.rmtree(bb.parent)

    def test_B_garbage_binding_reference():
        """B. Binding Reference with prefix/suffix garbage must fail."""
        bb = mutate_copy(FIXTURES / "valid")
        res = bb / "specialist-results" / "wo-narrative.md"
        text = res.read_text()
        text = text.replace(
            "| `design-okf/content/message-model.md` | Lead with outcome, then proof |",
            "| garbage design-okf/content/message-model.md trailing | Lead with outcome, then proof |",
        )
        res.write_text(text)
        expect_fail("B-garbage-binding-ref", bb, "Malformed or non-exact binding reference")
        shutil.rmtree(bb.parent)

    def test_C_non_hex_manifest_sha_normal():
        """C. Manifest sha256 not 64 hex must fail in normal mode."""
        bb = mutate_copy(FIXTURES / "valid")
        man = json.loads((bb / "okf-read-manifest.json").read_text())
        man[0]["sha256"] = "definitely-not-a-sha256"
        (bb / "okf-read-manifest.json").write_text(json.dumps(man, indent=2))
        expect_fail("C-non-hex-sha-normal", bb, "64 lowercase hex")
        shutil.rmtree(bb.parent)

    def test_D_undeclared_manifest_read():
        """D. Extra real OKF manifest entry not declared by work order must fail."""
        bb = mutate_copy(FIXTURES / "valid")
        man = json.loads((bb / "okf-read-manifest.json").read_text())
        color = (
            SKILL_ROOT / "references/design-okf/systems/color-system.md"
        ).read_bytes()
        import hashlib

        man.append(
            {
                "path": "references/design-okf/systems/color-system.md",
                "sha256": hashlib.sha256(color).hexdigest(),
                "owner": "wo-narrative",
            }
        )
        (bb / "okf-read-manifest.json").write_text(json.dumps(man, indent=2))
        expect_fail(
            "D-undeclared-manifest-read",
            bb,
            "undeclared by owner work order",
            require_hashes=True,
        )
        shutil.rmtree(bb.parent)

    def test_E_missing_h1_and_primary_read():
        """E. Remove H1 headings and Primary / read section must fail."""
        bb = mutate_copy(FIXTURES / "valid")
        wo = bb / "work-orders" / "wo-narrative.md"
        wtext = wo.read_text()
        wtext = re.sub(r"^# Work Order:.*\n", "", wtext, count=1, flags=re.M)
        # Remove Primary / read section body through next H2
        wtext = re.sub(
            r"## Primary / read OKF references\n.*?(?=^## )",
            "",
            wtext,
            count=1,
            flags=re.M | re.S,
        )
        wo.write_text(wtext)
        res = bb / "specialist-results" / "wo-narrative.md"
        rtext = res.read_text()
        rtext = re.sub(r"^# Specialist Result:.*\n", "", rtext, count=1, flags=re.M)
        res.write_text(rtext)
        code, errors = run_case(bb, require_hashes=True)
        joined = "\n".join(errors).lower()
        if code == 0:
            raise AssertionError("E expected failure")
        if "missing exact h1" not in joined and "work order missing exact h1" not in joined:
            raise AssertionError(f"E missing H1 error, got:\n{joined}")
        if "primary / read" not in joined:
            raise AssertionError(f"E missing Primary/read error, got:\n{joined}")
        print("PASS fail:E-missing-h1-and-primary-read")
        shutil.rmtree(bb.parent)

    def test_short_provenance_row():
        bb = mutate_copy(FIXTURES / "valid")
        res = bb / "specialist-results" / "wo-narrative.md"
        text = res.read_text()
        text = text.replace(
            "| `design-okf/content/message-model.md` | `references/design-okf/content/message-model.md` | d50ccbae698c30356ef21ed70d261de7813c2701627ce9dca31defcf82d0d82a | owned |",
            "| `design-okf/content/message-model.md` | `references/design-okf/content/message-model.md` |",
        )
        res.write_text(text)
        expect_fail("short-provenance-row", bb, "exactly 4 columns")
        shutil.rmtree(bb.parent)

    def test_short_binding_row():
        bb = mutate_copy(FIXTURES / "valid")
        res = bb / "specialist-results" / "wo-narrative.md"
        text = res.read_text()
        text = text.replace(
            "| `design-okf/content/message-model.md` | Lead with outcome, then proof | Hero headline + support line | Request Fit gate + first-viewport screenshot |",
            "| `design-okf/content/message-model.md` | Lead with outcome, then proof |",
        )
        res.write_text(text)
        expect_fail("short-binding-row", bb, "exactly 4 columns")
        shutil.rmtree(bb.parent)

    def test_noncanonical_alias_path():
        bb = mutate_copy(FIXTURES / "valid")
        man = json.loads((bb / "okf-read-manifest.json").read_text())
        # Noncanonical alias that old substring parsers would accept
        man[0]["path"] = "design-okf/content/message-model.md"
        (bb / "okf-read-manifest.json").write_text(json.dumps(man, indent=2))
        expect_fail("noncanonical-alias-path", bb, "exact canonical")
        shutil.rmtree(bb.parent)

    def test_duplicate_schema_fields():
        bb = mutate_copy(FIXTURES / "valid")
        wo = bb / "work-orders" / "wo-narrative.md"
        text = wo.read_text()
        text = text.replace(
            "- **status:** done\n",
            "- **status:** done\n- **status:** blocked\n",
        )
        wo.write_text(text)
        expect_fail("duplicate-schema-fields", bb, "Duplicate schema field")
        shutil.rmtree(bb.parent)

    def test_wrong_owner_temp():
        bb = mutate_copy(FIXTURES / "valid")
        man = json.loads((bb / "okf-read-manifest.json").read_text())
        for entry in man:
            if "message-model" in entry["path"]:
                entry["owner"] = "not-the-accountable-work-order"
        (bb / "okf-read-manifest.json").write_text(json.dumps(man, indent=2))
        expect_fail("adv-wrong-owner", bb, "not the accountable work-order")
        shutil.rmtree(bb.parent)

    def test_absolute_path_temp():
        bb = mutate_copy(FIXTURES / "valid")
        man = json.loads((bb / "okf-read-manifest.json").read_text())
        man[0]["path"] = "/external/not-in-repo/references/design-okf/content/message-model.md"
        (bb / "okf-read-manifest.json").write_text(json.dumps(man, indent=2))
        expect_fail("adv-absolute-path", bb, "absolute paths are forbidden")
        shutil.rmtree(bb.parent)

    def test_traversal_temp():
        bb = mutate_copy(FIXTURES / "valid")
        man = json.loads((bb / "okf-read-manifest.json").read_text())
        man[0]["path"] = "references/design-okf/../../../etc/passwd"
        (bb / "okf-read-manifest.json").write_text(json.dumps(man, indent=2))
        expect_fail("adv-traversal", bb, "path traversal is forbidden")
        shutil.rmtree(bb.parent)

    def test_missing_manifest_temp():
        bb = mutate_copy(FIXTURES / "valid")
        (bb / "okf-read-manifest.json").unlink()
        expect_fail("adv-missing-manifest", bb, "okf-read-manifest.json")
        shutil.rmtree(bb.parent)

    def test_provenance_as_binding_temp():
        bb = mutate_copy(FIXTURES / "valid")
        res = bb / "specialist-results" / "wo-narrative.md"
        text = res.read_text()
        marker = "## Binding proposals"
        head, _sep, _rest = text.partition(marker)
        res.write_text(head + "## Explicit non-claims\n\n- none\n")
        expect_fail("adv-provenance-as-binding", bb, "Binding proposals section missing")
        shutil.rmtree(bb.parent)

    def test_spoofed_findings_heading():
        """Substring 'findings' in a wrong H2 must not satisfy Findings."""
        bb = mutate_copy(FIXTURES / "valid")
        res = bb / "specialist-results" / "wo-narrative.md"
        text = res.read_text()
        text = text.replace("## Findings\n", "## Not findings\n")
        res.write_text(text)
        expect_fail("spoofed-findings-heading", bb, "missing findings")
        shutil.rmtree(bb.parent)

    # --- Codex exact-parser false-positive regressions ---

    def test_uppercase_manifest_sha():
        bb = mutate_copy(FIXTURES / "valid")
        man = json.loads((bb / "okf-read-manifest.json").read_text())
        man[0]["sha256"] = man[0]["sha256"].upper()
        (bb / "okf-read-manifest.json").write_text(json.dumps(man, indent=2))
        expect_fail("uppercase-manifest-sha", bb, "64 lowercase hex")
        shutil.rmtree(bb.parent)

    def test_uppercase_provenance_sha():
        bb = mutate_copy(FIXTURES / "valid")
        res = bb / "specialist-results" / "wo-narrative.md"
        text = res.read_text()
        m = re.search(r"(d50ccbae698c30356ef21ed70d261de7813c2701627ce9dca31defcf82d0d82a)", text)
        assert m
        res.write_text(text.replace(m.group(1), m.group(1).upper(), 1))
        expect_fail(
            "uppercase-provenance-sha",
            bb,
            "64 lowercase hex",
            require_hashes=True,
        )
        shutil.rmtree(bb.parent)

    def test_cross_read_trailing_garbage():
        bb = mutate_copy(FIXTURES / "valid")
        wo = bb / "work-orders" / "wo-narrative.md"
        text = wo.read_text()
        text = text.replace("— reason: hierarchy veto", "TRAILING GARBAGE")
        wo.write_text(text)
        expect_fail("cross-read-trailing-garbage", bb, "Non-exact Primary / read line")
        shutil.rmtree(bb.parent)

    def test_double_backtick_okf_cell():
        bb = mutate_copy(FIXTURES / "valid")
        res = bb / "specialist-results" / "wo-narrative.md"
        text = res.read_text()
        text = text.replace(
            "`design-okf/content/message-model.md`",
            "``design-okf/content/message-model.md``",
            1,
        )
        res.write_text(text)
        expect_fail("double-backtick-okf-cell", bb, "not exact")
        shutil.rmtree(bb.parent)

    def test_json_path_with_markdown_backticks():
        bb = mutate_copy(FIXTURES / "valid")
        man = json.loads((bb / "okf-read-manifest.json").read_text())
        man[0]["path"] = "`" + man[0]["path"] + "`"
        (bb / "okf-read-manifest.json").write_text(json.dumps(man, indent=2))
        expect_fail("json-path-markdown-backticks", bb, "Markdown backticks are forbidden")
        shutil.rmtree(bb.parent)

    def test_duplicate_normative_h2():
        bb = mutate_copy(FIXTURES / "valid")
        res = bb / "specialist-results" / "wo-narrative.md"
        text = res.read_text()
        res.write_text(text + "\n## Findings\n\n- second findings section\n")
        expect_fail("duplicate-normative-h2", bb, "duplicate H2 section")
        shutil.rmtree(bb.parent)

    def _wrap_all_md(bb: Path, kind: str) -> None:
        for p in bb.rglob("*.md"):
            text = p.read_text()
            if kind == "backtick":
                p.write_text("```markdown\n" + text + "\n```\n")
            elif kind == "tilde":
                p.write_text("~~~\n" + text + "\n~~~\n")
            elif kind == "comment":
                p.write_text("<!--\n" + text + "\n-->\n")
            else:
                raise ValueError(kind)

    def test_A_whole_doc_backtick_fence():
        bb = mutate_copy(FIXTURES / "valid")
        _wrap_all_md(bb, "backtick")
        expect_fail(
            "A-whole-doc-backtick-fence",
            bb,
            "empty structural content",
            require_hashes=True,
        )
        shutil.rmtree(bb.parent)

    def test_B_whole_doc_tilde_fence():
        bb = mutate_copy(FIXTURES / "valid")
        _wrap_all_md(bb, "tilde")
        expect_fail(
            "B-whole-doc-tilde-fence",
            bb,
            "empty structural content",
            require_hashes=True,
        )
        shutil.rmtree(bb.parent)

    def test_C_whole_doc_html_comment():
        bb = mutate_copy(FIXTURES / "valid")
        _wrap_all_md(bb, "comment")
        expect_fail(
            "C-whole-doc-html-comment",
            bb,
            "empty structural content",
            require_hashes=True,
        )
        shutil.rmtree(bb.parent)

    def test_D_fenced_evidence_h2_not_duplicate():
        """Legitimate fenced sample H2 inside a real section must not spoof structure."""
        bb = mutate_copy(FIXTURES / "valid")
        res = bb / "specialist-results" / "wo-narrative.md"
        text = res.read_text()
        old = "## Local verification evidence\n\n- fixture evidence\n"
        if old not in text:
            raise AssertionError("fixture Local verification text changed")
        new = (
            "## Local verification evidence\n\n"
            "- fixture evidence\n"
            "- Evidence sample:\n"
            "```md\n"
            "## Findings\n\n"
            "- sample finding inside fence\n"
            "```\n"
        )
        res.write_text(text.replace(old, new))
        expect_pass("D-fenced-evidence-h2-ok", bb, require_hashes=True)
        shutil.rmtree(bb.parent)

    def test_h1_not_first_structural_line():
        bb = mutate_copy(FIXTURES / "valid")
        wo = bb / "work-orders" / "wo-narrative.md"
        text = wo.read_text()
        wo.write_text("Note: preamble\n\n" + text)
        expect_fail("h1-not-first-line", bb, "first nonblank structural line")
        shutil.rmtree(bb.parent)

    def test_duplicate_h1():
        bb = mutate_copy(FIXTURES / "valid")
        wo = bb / "work-orders" / "wo-narrative.md"
        text = wo.read_text()
        wo.write_text(text + "\n# Work Order: wo-narrative\n")
        expect_fail("duplicate-h1", bb, "multiple H1")
        shutil.rmtree(bb.parent)

    def test_inline_comment_cannot_split_polluted_h1():
        """Closed HTML comment must not insert a newline that sanitizes a bad H1."""
        bb = mutate_copy(FIXTURES / "valid")
        wo = bb / "work-orders" / "wo-narrative.md"
        text = wo.read_text()
        first = text.splitlines()[0]
        # Polluted H1: valid-looking heading chars + inline comment + trailing junk
        polluted = "# Work Order: wo-narrative <!--inline--> TRAILING"
        wo.write_text(text.replace(first, polluted, 1))
        expect_fail(
            "inline-comment-polluted-h1",
            bb,
            "H1 must match",
            require_hashes=True,
        )
        shutil.rmtree(bb.parent)

    def test_unclosed_html_comment_masks_through_eof():
        """Unclosed <!-- after H1 must hide remaining fields/sections."""
        bb = mutate_copy(FIXTURES / "valid")
        wo = bb / "work-orders" / "wo-narrative.md"
        lines = wo.read_text().splitlines()
        wo.write_text(lines[0] + "\n<!-- unclosed hides rest\n" + "\n".join(lines[1:]) + "\n")
        code, errors = run_case(bb, require_hashes=True)
        joined = "\n".join(errors).lower()
        if code == 0:
            raise AssertionError("unclosed comment should not leave structure parseable")
        # Fields after the opener must be masked; missing id/status are expected families.
        if "missing explicit id" not in joined and "missing status" not in joined and "missing request_anchor" not in joined:
            raise AssertionError(f"expected masked fields after unclosed comment, got:\n{joined}")
        print("PASS fail:unclosed-html-comment-through-eof")
        shutil.rmtree(bb.parent)

    def test_unclosed_comment_inside_fence_does_not_swallow_structure():
        """Fences first: unclosed <!-- inside fenced evidence must not hide later sections."""
        bb = mutate_copy(FIXTURES / "valid")
        res = bb / "specialist-results" / "wo-narrative.md"
        text = res.read_text()
        old = "## Local verification evidence\n\n- fixture evidence\n"
        if old not in text:
            raise AssertionError("fixture Local verification text changed")
        new = (
            "## Local verification evidence\n\n"
            "- fixture evidence\n"
            "- Evidence sample:\n"
            "```md\n"
            "<!-- unclosed inside fence\n"
            "## Findings\n"
            "- spoof\n"
            "```\n"
            "\n"
            # Real sections after the fence must remain structural.
        )
        # Keep the rest of the document (Unresolved, Conflicts, Binding, ...) intact.
        res.write_text(text.replace(old, new))
        expect_pass(
            "unclosed-comment-inside-fence-ok",
            bb,
            require_hashes=True,
        )
        shutil.rmtree(bb.parent)

    for fn in (
        test_valid_normal,
        test_valid_hashes,
        test_static_invalids,
        test_manifest_hash_mismatch,
        test_A_blank_provenance_cells,
        test_B_garbage_binding_reference,
        test_C_non_hex_manifest_sha_normal,
        test_D_undeclared_manifest_read,
        test_E_missing_h1_and_primary_read,
        test_short_provenance_row,
        test_short_binding_row,
        test_noncanonical_alias_path,
        test_duplicate_schema_fields,
        test_wrong_owner_temp,
        test_absolute_path_temp,
        test_traversal_temp,
        test_missing_manifest_temp,
        test_provenance_as_binding_temp,
        test_spoofed_findings_heading,
        test_uppercase_manifest_sha,
        test_uppercase_provenance_sha,
        test_cross_read_trailing_garbage,
        test_double_backtick_okf_cell,
        test_json_path_with_markdown_backticks,
        test_duplicate_normative_h2,
        test_A_whole_doc_backtick_fence,
        test_B_whole_doc_tilde_fence,
        test_C_whole_doc_html_comment,
        test_D_fenced_evidence_h2_not_duplicate,
        test_h1_not_first_structural_line,
        test_duplicate_h1,
        test_inline_comment_cannot_split_polluted_h1,
        test_unclosed_html_comment_masks_through_eof,
        test_unclosed_comment_inside_fence_does_not_swallow_structure,
    ):
        guard(fn)

    if failures:
        print(f"AGENT HANDOFF TESTS FAILED ({failures})")
        return 1
    print("AGENT HANDOFF TESTS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
