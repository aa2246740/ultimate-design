#!/usr/bin/env python3
"""Static flow proof for the ultimate-design skill.

This script proves only that the published workflow is represented in the
skill bundle. It does not evaluate aesthetic quality.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def read(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")


def frontmatter(text: str) -> str | None:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    return match.group(1) if match else None


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    checks: list[tuple[str, bool, str]] = []

    def require(name: str, condition: bool, evidence: str) -> None:
        checks.append((name, condition, evidence))

    skill = read(root / "SKILL.md")
    phases = [
        "Orient.",
        "Complete the brief.",
        "Build the content contract.",
        "Bootstrap the contract.",
        "Load the branch reference.",
        "Choose a direction.",
        "Make the artifact.",
        "Critique and repair.",
        "Verify.",
        "Govern.",
    ]
    positions: list[int] = []
    for phase in phases:
        index = skill.find(phase)
        positions.append(index)
        require(f"phase present: {phase}", index >= 0, f"index={index}")

    require(
        "phase order",
        all(a >= 0 and a < b for a, b in zip(positions, positions[1:])),
        " -> ".join(str(p) for p in positions),
    )
    require(
        "monitoring is optional",
        "Start a run trace" not in skill
        and "Complete the run trace" not in skill
        and "Do not load it during ordinary design work" in skill,
        "normal Operating Loop has no mandatory trace step",
    )
    require(
        "monitoring reference is routed",
        "references/monitoring.md" in skill and "development/testing evidence" in skill,
        "monitoring reference is gated to dev/eval requests",
    )
    description = frontmatter(skill) or ""
    require(
        "description front-loads leading word",
        "description: \"Contract-driven" in description,
        "model-invoked trigger begins with contract",
    )
    require(
        "quality gates are always loaded",
        "references/quality-gates.md" in skill and "before final delivery, always" in skill,
        "final quality gate pointer is present",
    )
    require(
        "content model reference is routed",
        "references/content-model.md" in skill
        and "Build the content contract" in skill
        and "content contract" in skill,
        "content contract stage and reference are present",
    )
    require(
        "presentation branch is routed",
        "references/branch-presentation.md" in skill
        and "presentation/PPT deck" in skill
        and "slide title/reading order" in skill,
        "PPT and slide-deck tasks load a presentation branch and verify deck-specific concerns",
    )
    require(
        "product sense reference is routed",
        "references/design-okf/methods/product-sense.md" in skill
        and "product/problem framing" in skill
        and "success signal" in skill,
        "product-oriented design tasks load the product sense OKF",
    )
    require(
        "request anchor is created in brief",
        "Request Anchor" in skill
        and "original user request" in skill.lower()
        and "latest user override" in skill.lower()
        and "validation checks" in skill.lower(),
        "brief stage records original request, latest override, and validation checks",
    )
    require(
        "request anchor is checked before delivery",
        "Request Anchor fit" in skill
        and "user-specific success criteria" in skill
        and "How the result maps back" in skill,
        "verify and final response must map back to user request",
    )

    audit = read(root / "references" / "audit-polish.md")
    require(
        "critique repair loop",
        "Build Critique Loop" in audit
        and "P0/P1" in audit
        and "Run one more critique pass" in audit
        and "Do not ship after the first critique" in audit,
        "audit-polish requires severity, repair, and second critique",
    )
    require(
        "content critique loop",
        "Check content contract" in audit
        and "state language" in audit
        and "visual personality" in audit,
        "audit-polish critiques content and expressive color before delivery",
    )

    monitoring = read(root / "references" / "monitoring.md")
    require(
        "monitoring doc is dev-only",
        "development/testing mode" in monitoring
        and "Do not enable this during ordinary design work" in monitoring
        and "Static Flow Proof" in monitoring
        and "Runtime Evidence" in monitoring,
        "monitoring separates static proof from runtime traces",
    )
    require(
        "monitoring includes request anchor trace",
        "| Request Anchor |" in monitoring
        and "no Request Anchor was recorded" in monitoring
        and "checked against the Request Anchor" in monitoring,
        "runtime traces preserve request integrity",
    )

    okf_root = root / "references" / "design-okf"
    concept_files = [p for p in okf_root.rglob("*.md") if p.name != "index.md"]
    missing_types: list[str] = []
    for path in concept_files:
        fm = frontmatter(read(path))
        if not fm or not re.search(r"(?m)^type:\s*\S+", fm):
            missing_types.append(str(path.relative_to(root)))
    require(
        "OKF concepts are typed",
        bool(concept_files) and not missing_types,
        "all typed" if not missing_types else ", ".join(missing_types),
    )
    content_files = [
        okf_root / "content" / "message-model.md",
        okf_root / "content" / "ux-writing.md",
        okf_root / "content" / "state-language.md",
        okf_root / "content" / "semantic-binding.md",
    ]
    missing_content = [str(p.relative_to(root)) for p in content_files if not p.exists()]
    require(
        "content OKF concepts exist",
        not missing_content,
        "content OKF files present" if not missing_content else ", ".join(missing_content),
    )
    product_sense = read(okf_root / "methods" / "product-sense.md")
    require(
        "product sense OKF exists",
        "Problem before solution" in product_sense
        and "Success signal" in product_sense
        and "AI Product UX" in product_sense
        and "Request Anchor Integration" in product_sense
        and "Done Check" in product_sense,
        "PM research is represented as conditional product-design knowledge",
    )
    presentation = read(okf_root / "production" / "presentation-deck.md")
    require(
        "presentation deck OKF exists",
        "Decision Path" in presentation
        and "Density Modes" in presentation
        and "Slide Claim Model" in presentation
        and "Master, Brand, And Delivery" in presentation
        and "Accessibility" in presentation
        and "Done Check" in presentation,
        "PPT research is represented as conditional deck-design knowledge",
    )

    contract = read(root / "references" / "design-contract.md")
    require(
        "contract has request anchor",
        "## Request Anchor" in contract
        and "Original user request" in contract
        and "Validation must check against" in contract
        and "Create a Request Anchor" in contract,
        "DESIGN.md template includes request integrity fields",
    )
    require(
        "contract has content model",
        "## Content Model" in contract
        and "Message hierarchy" in contract
        and "State language rules" in contract,
        "DESIGN.md template includes content model fields",
    )
    require(
        "contract has presentation specs",
        "## Presentation Or Deck Specs" in contract
        and "One-sentence deck conclusion" in contract
        and "Slide claim/evidence/action rule" in contract
        and "Export package" in contract,
        "DESIGN.md template includes presentation/deck continuity fields",
    )
    require(
        "contract has Google-compatible DESIGN.md template",
        "Google-compatible" in contract
        and "version: alpha" in contract
        and "rounded:" in contract
        and '"{colors.primary}"' in contract
        and "Do's and Don'ts" in contract,
        "DESIGN.md template includes official token layer and section order",
    )

    design_md_standard = read(okf_root / "governance" / "design-md-standard.md")
    require(
        "DESIGN.md standard OKF exists",
        "Google Labs" in design_md_standard
        and "Core Front Matter" in design_md_standard
        and "rounded" in design_md_standard
        and "{colors.primary}" in design_md_standard
        and "Extension Boundary" in design_md_standard,
        "official-compatible schema, token refs, and extension boundary present",
    )
    design_md_agent = read(okf_root / "governance" / "design-md-agent-governance.md")
    require(
        "DESIGN.md agent governance OKF exists",
        "Agent Usage Rules" in design_md_agent
        and "Agent Self-Check" in design_md_agent
        and "AGENTS.md Integration" in design_md_agent,
        "agent read/apply/update rules are present",
    )
    request_integrity = read(okf_root / "governance" / "request-integrity.md")
    require(
        "request integrity OKF exists",
        "Request Anchor Fields" in request_integrity
        and "Do not turn every user request into a temporary OKF bundle" in request_integrity
        and "Critique And Verification" in request_integrity
        and "Done Check" in request_integrity,
        "request drift prevention is documented as reusable governance knowledge",
    )

    quality = read(root / "references" / "quality-gates.md")
    require(
        "quality gates include request anchor",
        "## Request Anchor" in quality
        and "latest user override" in quality
        and "User-specific success criteria" in quality
        and "Requirement drift" in quality,
        "quality-gates checks artifact against user-specific request",
    )
    require(
        "quality gates include content",
        "## Content" in quality
        and "CTAs state action plus result" in quality
        and "Critical meaning is not carried only" in quality,
        "quality-gates includes mandatory content gate",
    )
    require(
        "quality gates include product sense",
        "product problem" in quality
        and "success signal" in quality
        and "Tradeoffs and non-goals" in quality,
        "quality-gates checks product fit for product-oriented design",
    )
    require(
        "quality gates include presentation deck",
        "## Presentation Deck" in quality
        and "title-only reading tells the story" in quality
        and "claim, evidence" in quality
        and "PDF stability" in quality,
        "quality-gates checks commercial deck narrative and delivery",
    )

    color = read(root / "references" / "design-okf" / "systems" / "color-system.md")
    require(
        "color system includes expression gate",
        "Expression Before Palette" in color
        and "anti-template check" in color
        and "Color posture" in color,
        "color-system checks scene, posture, and category defaults",
    )

    tokens_branch = read(root / "references" / "tokens-components.md")
    tokens_okf = read(root / "references" / "design-okf" / "systems" / "tokens-components.md")
    require(
        "tokens branch delegates source of truth",
        "source-of-truth model" in tokens_branch
        and "design-okf/systems/tokens-components.md" in tokens_branch
        and "Stable Names" in tokens_okf,
        "tokens branch avoids duplicating the OKF token model",
    )
    graphic_branch = read(root / "references" / "graphic-print.md")
    graphic_okf = read(root / "references" / "design-okf" / "production" / "graphic-print.md")
    require(
        "graphic branch delegates print blockers",
        "source of truth for print caveats" in graphic_branch
        and "design-okf/production/graphic-print.md" in graphic_branch
        and "Blockers For Final Print-Ready Claims" in graphic_okf,
        "graphic branch avoids duplicating print-production caveats",
    )
    presentation_branch = read(root / "references" / "branch-presentation.md")
    require(
        "presentation branch delegates source of truth",
        "source-of-truth commercial deck model" in presentation_branch
        and "design-okf/production/presentation-deck.md" in presentation_branch
        and "Presentations capability" in presentation_branch,
        "presentation branch avoids duplicating file-operation responsibility",
    )

    machine = read(okf_root / "governance" / "machine-verification-ci.md")
    require(
        "machine verification includes DESIGN.md tooling",
        "@google/design.md lint" in machine
        and "validate_design_contract.py" in machine
        and "Broken token references" in machine,
        "official tooling and local fallback validator are routed",
    )
    validator_path = root / "scripts" / "validate_design_contract.py"
    validator = read(validator_path)
    require(
        "DESIGN.md validator script exists",
        "OFFICIAL_TOP_LEVEL" in validator
        and "BAD_DOLLAR_REF_RE" in validator
        and "strict_ultimate" in validator
        and "DESIGN CONTRACT VALIDATION" in validator,
        "local structural validator is present",
    )
    require(
        "DESIGN.md validator checks request anchor",
        "REQUEST_ANCHOR_FIELDS" in validator
        and "Request Anchor field missing" in validator
        and "Request Anchor field is empty" in validator,
        "local validator enforces request anchor in strict mode",
    )

    coverage = read(root / "references" / "design-okf" / "governance" / "research-coverage-map.md")
    coverage_terms = [
        "Requirement drift",
        "Request Anchor",
        "DESIGN.md official definition",
        "Official token reference syntax",
        "DESIGN.md agent execution rules",
        "Content strategy",
        "UX writing",
        "Component state language",
        "Semantic HTML",
        "Design Thinking",
        "Gestalt",
        "Visual hierarchy",
        "Color theory",
        "Typography",
        "WCAG",
        "Token hierarchy",
        "Design review and QA",
        "Machine-verifiable",
        "Data visualization",
        "Product problem framing",
        "Product metrics",
        "MVP scope",
        "AI product UX risks",
        "Business/user value tradeoffs",
        "Commercial PPT",
        "Deck narrative",
        "PPT master/template",
    ]
    for term in coverage_terms:
        require(f"research coverage: {term}", term in coverage, "anchor found" if term in coverage else "missing")

    failed = [item for item in checks if not item[1]]
    for name, ok, evidence in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name} - {evidence}")

    if failed:
        print(f"FLOW CHECK FAIL: {len(failed)} failed check(s)")
        return 1

    print("FLOW CHECK PASS")
    print("Checked flow: " + " -> ".join(p.removesuffix(".") for p in phases))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
