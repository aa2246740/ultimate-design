#!/usr/bin/env python3
"""Repo-level Design Maturity regressions (not shipped in the npm package)."""

from __future__ import annotations

import importlib.util
import re
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "skill" / "ultimate-design" / "scripts" / "validate_design_contract.py"
DESIGN_CONTRACT_MD = (
    REPO_ROOT / "skill" / "ultimate-design" / "references" / "design-contract.md"
)


def _load_validator():
    spec = importlib.util.spec_from_file_location("ud_validate_design_contract", VALIDATOR)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _minimal_body(mod, maturity_block: str | None) -> str:
    base = (
        "# Design System\n\n"
        "## Overview\nProbe.\n\n"
        "## Colors\nok\n\n"
        "## Typography\nok\n\n"
        "## Layout\nok\n\n"
        "## Elevation & Depth\nok\n\n"
        "## Shapes\nok\n\n"
        "## Components\nok\n\n"
        "## Do's and Don'ts\nok\n"
    )
    if maturity_block:
        return base + "\n" + maturity_block + "\n"
    return base


def _locked_file_body(authority: str = "User accepted after Codex review", axes: str = "color, type") -> str:
    return (
        "# Design System\n\n## Overview\nLocked sibling.\n\n"
        "## Design Maturity\n\n"
        f"- Status: Locked\n- Lock authority: {authority}\n"
        f"- Locked axes: {axes}\n"
    )


def run_maturity_self_tests() -> list[str]:
    mod = _load_validator()
    failures: list[str] = []

    def errors_for(
        maturity_block: str | None,
        *,
        strict: bool = True,
        contract_path: Path | None = None,
    ) -> list[str]:
        reporter = mod.Reporter()
        mod.check_design_maturity(
            _minimal_body(mod, maturity_block),
            reporter,
            strict=strict,
            contract_path=contract_path,
        )
        return list(reporter.errors)

    def warns_for(maturity_block: str | None, *, strict: bool = False) -> list[str]:
        reporter = mod.Reporter()
        mod.check_design_maturity(
            _minimal_body(mod, maturity_block),
            reporter,
            strict=strict,
        )
        return list(reporter.warnings)

    def expect_ok(name: str, block: str | None, **kwargs) -> None:
        errs = errors_for(block, **kwargs)
        if errs:
            failures.append(f"{name}: expected pass, got {errs}")

    def expect_fail(name: str, block: str | None, *subs: str, **kwargs) -> None:
        errs = errors_for(block, **kwargs)
        if not errs:
            failures.append(f"{name}: expected errors, got none")
            return
        blob = " | ".join(errs)
        for sub in subs:
            if sub.lower() not in blob.lower():
                failures.append(f"{name}: expected {sub!r} in {errs}")

    # missing section
    expect_ok("missing section compatible", None)

    # Draft non-strict vs strict
    draft = "## Design Maturity\n\n- Status: Draft\n"
    if errors_for(draft, strict=False):
        failures.append(f"Draft non-strict: expected 0 errors, got {errors_for(draft, strict=False)}")
    if not warns_for(draft, strict=False):
        failures.append("Draft non-strict: expected warning")
    expect_fail("Draft strict", draft, "exactly Exploratory", strict=True)

    # lean template Status Exploratory
    expect_ok(
        "lean template Exploratory",
        "## Design Maturity\n\n- Status: Exploratory\n- Lock authority:\n"
        "- Locked axes:\n- Allowed variation:\n",
    )

    # source-of-truth: extract fenced template from design-contract.md
    contract_text = DESIGN_CONTRACT_MD.read_text(encoding="utf-8")
    fence = re.search(r"```md\n(.*?)```", contract_text, re.S)
    if not fence:
        failures.append("design-contract.md missing ```md fenced lean template")
    else:
        fenced = fence.group(1)
        maturity = re.search(
            r"(?ms)^##\s+Design Maturity\s*$\n(.*?)(?=^##\s+|\Z)", fenced
        )
        if not maturity:
            failures.append("fenced template missing Design Maturity section")
        else:
            statuses = re.findall(
                r"(?mi)^[ \t]*(?:[-*+][ \t]+)?Status[ \t]*:[ \t]*([^\n]*)$",
                maturity.group(0),
            )
            if len(statuses) != 1 or statuses[0].strip() != "Exploratory":
                failures.append(
                    f"fenced template must have exactly one Status Exploratory, got {statuses}"
                )
            rep = mod.Reporter()
            mod.check_design_maturity(fenced, rep, strict=True)
            if rep.errors:
                failures.append(f"fenced template strict validate: {rep.errors}")

    # valid authorities — four documented forms only
    for auth in [
        "User accepted after Codex review",
        "Design owner approved",
        "Accepted by user",
        "Approved by design owner",
    ]:
        expect_ok(
            f"valid {auth}",
            "## Design Maturity\n\n- Status: Locked\n"
            f"- Lock authority: {auth}\n- Locked axes: color, type\n",
        )

    # negative axes language allowed; unresolved tokens anywhere fail
    expect_ok(
        "axes negative design constraints",
        "## Design Maturity\n\n- Status: Locked\n"
        "- Lock authority: User accepted after Codex review\n"
        "- Locked axes: no gradients, no motion, motion without parallax, never use shadows\n",
    )
    for axes in ["color, TBD", "color, placeholder", "no gradients, pending motion"]:
        expect_fail(
            f"axes unresolved {axes!r}",
            "## Design Maturity\n\n- Status: Locked\n"
            "- Lock authority: Design owner approved\n"
            f"- Locked axes: {axes}\n",
            "Locked axes",
        )

    # reject non-fixed authority forms
    for auth in [
        "User accepted",
        "User approved",
        "Design owner accepted",
        "Accepted by the user",
        "Approved by the design owner",
        "User accepted after AI guess",
        "User accepted?",
        "User accepted if QA passes",
        "User accepted conditionally",
        "User accepted by Codex",
        "User accepted (AI inference)",
        "User never approved",
        "User has not accepted",
        "User acceptance",
        "User reports Codex approved",
        "approved by Codex",
        "Codex approved",
        "Wu approved",
        "Client signed off",
        "Stakeholder accepted",
    ]:
        expect_fail(
            f"reject {auth}",
            "## Design Maturity\n\n- Status: Locked\n"
            f"- Lock authority: {auth}\n- Locked axes: color\n",
            "Lock authority",
        )

    # empty axes must not absorb Allowed variation
    expect_fail(
        "empty axes before Allowed variation",
        "## Design Maturity\n\n- Status: Locked\n"
        "- Lock authority: Accepted by user\n"
        "- Locked axes:\n"
        "- Allowed variation: no gradients\n",
        "Locked axes",
    )
    # + bullet duplicate
    expect_fail(
        "plus bullet duplicate Status",
        "## Design Maturity\n\n- Status: Candidate\n"
        "+ Status: Locked\n"
        "- Lock authority: User accepted after Codex review\n"
        "- Locked axes: color\n",
        "duplicate Status",
    )

    def _leaf_locked():
        return _locked_file_body("User accepted after Codex review", "color")

    # pre-existing path resolution with temp dirs
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        locked = root / "design-system" / "locked.md"
        locked.parent.mkdir(parents=True)
        locked.write_text(_leaf_locked(), encoding="utf-8")
        # legitimate directory names that used to be blacklisted
        ai_locked = root / "ai" / "DESIGN.md"
        ai_locked.parent.mkdir(parents=True)
        ai_locked.write_text(_leaf_locked(), encoding="utf-8")
        repo_locked = root / "repo" / "locked.md"
        repo_locked.parent.mkdir(parents=True)
        repo_locked.write_text(_leaf_locked(), encoding="utf-8")

        design = root / "DESIGN.md"
        design.write_text(
            _minimal_body(
                mod,
                "## Design Maturity\n\n- Status: Locked\n"
                "- Lock authority: Pre-existing locked contract: design-system/locked.md\n"
                "- Locked axes: color\n",
            ),
            encoding="utf-8",
        )
        rep = mod.Reporter()
        mod.check_design_maturity(
            design.read_text(encoding="utf-8"),
            rep,
            strict=True,
            contract_path=design,
        )
        if rep.errors:
            failures.append(f"valid pre-existing relative path: {rep.errors}")

        for rel, label in [
            ("ai/DESIGN.md", "ai/DESIGN.md"),
            ("repo/locked.md", "repo/locked.md"),
        ]:
            rep = mod.Reporter()
            mod.check_design_maturity(
                _minimal_body(
                    mod,
                    "## Design Maturity\n\n- Status: Locked\n"
                    f"- Lock authority: Pre-existing locked contract: {rel}\n"
                    "- Locked axes: color\n",
                ),
                rep,
                strict=True,
                contract_path=design,
            )
            if rep.errors:
                failures.append(f"valid path {label} should pass: {rep.errors}")

        # absolute path rejected
        rep = mod.Reporter()
        mod.check_design_maturity(
            _minimal_body(
                mod,
                "## Design Maturity\n\n- Status: Locked\n"
                f"- Lock authority: Pre-existing locked contract: {locked}\n"
                "- Locked axes: color\n",
            ),
            rep,
            strict=True,
            contract_path=design,
        )
        if not rep.errors:
            failures.append("absolute pre-existing path should fail")

        # traversal rejected
        rep = mod.Reporter()
        mod.check_design_maturity(
            _minimal_body(
                mod,
                "## Design Maturity\n\n- Status: Locked\n"
                "- Lock authority: Pre-existing locked contract: ../etc/passwd\n"
                "- Locked axes: color\n",
            ),
            rep,
            strict=True,
            contract_path=design,
        )
        if not rep.errors:
            failures.append("traversal pre-existing path should fail")

        # nonexistent rejected
        rep = mod.Reporter()
        mod.check_design_maturity(
            _minimal_body(
                mod,
                "## Design Maturity\n\n- Status: Locked\n"
                "- Lock authority: Pre-existing locked contract: missing.md\n"
                "- Locked axes: color\n",
            ),
            rep,
            strict=True,
            contract_path=design,
        )
        if not rep.errors:
            failures.append("missing pre-existing file should fail")

        # non-Markdown suffix rejected
        other = root / "locked.json"
        other.write_text("{}", encoding="utf-8")
        rep = mod.Reporter()
        mod.check_design_maturity(
            _minimal_body(
                mod,
                "## Design Maturity\n\n- Status: Locked\n"
                "- Lock authority: Pre-existing locked contract: locked.json\n"
                "- Locked axes: color\n",
            ),
            rep,
            strict=True,
            contract_path=design,
        )
        if not rep.errors:
            failures.append("non-Markdown pre-existing path should fail")

        # non-UTF-8 target
        binary = root / "binary.md"
        binary.write_bytes(b"\xff\xfe\x00 not utf-8")
        rep = mod.Reporter()
        mod.check_design_maturity(
            _minimal_body(
                mod,
                "## Design Maturity\n\n- Status: Locked\n"
                "- Lock authority: Pre-existing locked contract: binary.md\n"
                "- Locked axes: color\n",
            ),
            rep,
            strict=True,
            contract_path=design,
        )
        if not rep.errors:
            failures.append("non-UTF-8 pre-existing target should fail")

        # referenced file not Locked
        bad_ref = root / "not-locked.md"
        bad_ref.write_text(
            _minimal_body(mod, "## Design Maturity\n\n- Status: Exploratory\n"),
            encoding="utf-8",
        )
        rep = mod.Reporter()
        mod.check_design_maturity(
            _minimal_body(
                mod,
                "## Design Maturity\n\n- Status: Locked\n"
                "- Lock authority: Pre-existing locked contract: not-locked.md\n"
                "- Locked axes: color\n",
            ),
            rep,
            strict=True,
            contract_path=design,
        )
        if not rep.errors:
            failures.append("pre-existing Exploratory sibling should fail")

        # recursion loop A -> B -> A
        a = root / "a.md"
        b = root / "b.md"
        a.write_text(
            _minimal_body(
                mod,
                "## Design Maturity\n\n- Status: Locked\n"
                "- Lock authority: Pre-existing locked contract: b.md\n"
                "- Locked axes: color\n",
            ),
            encoding="utf-8",
        )
        b.write_text(
            _minimal_body(
                mod,
                "## Design Maturity\n\n- Status: Locked\n"
                "- Lock authority: Pre-existing locked contract: a.md\n"
                "- Locked axes: color\n",
            ),
            encoding="utf-8",
        )
        rep = mod.Reporter()
        mod.check_design_maturity(
            a.read_text(encoding="utf-8"),
            rep,
            strict=True,
            contract_path=a,
        )
        if not rep.errors:
            failures.append("pre-existing reference loop should fail")

        # deep acyclic chain > MAX depth without RecursionError
        n = mod.MAX_PREEXISTING_DEPTH + 8
        for i in range(n - 1, -1, -1):
            pth = root / f"d{i}.md"
            if i == n - 1:
                body = _leaf_locked()
            else:
                body = _minimal_body(
                    mod,
                    "## Design Maturity\n\n- Status: Locked\n"
                    f"- Lock authority: Pre-existing locked contract: d{i + 1}.md\n"
                    "- Locked axes: color\n",
                )
            pth.write_text(body, encoding="utf-8")
        rep = mod.Reporter()
        try:
            mod.check_design_maturity(
                (root / "d0.md").read_text(encoding="utf-8"),
                rep,
                strict=True,
                contract_path=root / "d0.md",
            )
        except RecursionError:
            failures.append("deep acyclic chain raised RecursionError")
        else:
            if not rep.errors:
                failures.append("deep acyclic chain must fail at max depth")
            if not any("depth exceeds" in e for e in rep.errors):
                failures.append(f"deep chain should report depth bound: {rep.errors}")

    # installable smoke suite must pass without depending on this file's presence
    smoke = mod.run_maturity_smoke_tests()
    if smoke:
        failures.append(f"runtime smoke suite failed: {smoke}")

    # retain core invalid/valid status cases
    expect_fail(
        "illegal multi status",
        "## Design Maturity\n\n- Status: Exploratory | Candidate | Locked\n",
        "exactly Exploratory",
    )
    expect_fail(
        "duplicate Status bullets",
        "## Design Maturity\n\n- Status: Candidate\n- Status: Locked\n"
        "- Lock authority: User accepted after Codex review\n- Locked axes: color\n",
        "duplicate Status",
    )
    expect_fail(
        "mixed bullet/prose Status",
        "## Design Maturity\n\n- Status: Candidate\nStatus: Locked\n"
        "- Lock authority: User accepted after Codex review\n- Locked axes: color\n",
        "duplicate Status",
    )

    return failures


def main() -> int:
    failures = run_maturity_self_tests()
    if failures:
        print("DESIGN MATURITY SELF-TEST FAIL")
        for item in failures:
            print(f"FAIL {item}")
        return 1
    print("DESIGN MATURITY SELF-TEST PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
