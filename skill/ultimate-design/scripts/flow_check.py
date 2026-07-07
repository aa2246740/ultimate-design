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
    require(
        "research ingestion reference is dev-only",
        "## Research Ingestion" in skill
        and "research-digestion-llm-wiki.md" in skill
        and "not ordinary design execution" in skill
        and "promote only stable, operational, checkable knowledge into OKF" in skill,
        "LLM wiki digestion is gated to research absorption and OKF updates",
    )
    description = frontmatter(skill) or ""
    require(
        "description front-loads leading word",
        "description: \"Contract-driven" in description,
        "model-invoked trigger begins with contract",
    )
    branch_triggers = [
        "DESIGN.md contracts",
        "product UI",
        "marketing pages",
        "presentation decks",
        "graphic/print assets",
        "brand systems",
        "content/UX writing",
        "design critique",
        "rendered verification",
    ]
    missing_triggers = [term for term in branch_triggers if term not in description]
    require(
        "description has one trigger per branch",
        not missing_triggers and len(description) <= 320,
        "all branch triggers present and concise" if not missing_triggers else ", ".join(missing_triggers),
    )
    require(
        "yolo mode is default",
        "Default to **YOLO mode**" in skill
        and "Ask only for blockers" in skill
        and "complete first pass" in skill,
        "ordinary design requests run low-interruption by default",
    )
    require(
        "pro mode builds consensus",
        "Use **Pro mode**" in skill
        and "`--pro`" in skill
        and "build consensus before making high-impact choices" in skill
        and "update the Request Anchor after each decision" in skill,
        "--pro turns the loop into explicit design agreement",
    )
    require(
        "quality gates are always loaded",
        "references/quality-gates.md" in skill and "before final delivery, always" in skill,
        "final quality gate pointer is present",
    )
    require(
        "light taste checkpoint is default for visible artifacts",
        "For every visible artifact, apply a lightweight **Taste Checkpoint** by default" in skill
        and "keep the checkpoint brief" in skill
        and "If no expressive style is needed" in skill,
        "visible artifacts pass a taste checkpoint without forcing expressive styling everywhere",
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
        "contract is default for non-trivial artifacts",
        "For any non-trivial design artifact" in skill
        and "create or update `DESIGN.md` by default" in skill
        and "compact contract or review note only for one-off" in skill,
        "agent creates DESIGN.md unless the design is small and low-risk",
    )
    require(
        "semantic zones are marked during implementation",
        "mark major semantic zones during implementation" in skill
        and "`data-ud-check`" in skill
        and "against the semantic zones created during implementation" in skill,
        "HTML verification markers are created before final verification",
    )
    require(
        "professional bar is behavior-based",
        "Professional quality is observable behavior" in skill
        and "Frame the real problem" in skill
        and "Shape content structure" in skill
        and "Leave a contract that explains" in skill,
        "professionalism is defined as checkable design behavior",
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
    require(
        "taste critique loop",
        "Check taste for visible artifacts" in audit
        and "design-okf/systems/taste-engine.md" in audit
        and "Taste Critique" in audit,
        "audit-polish routes stiff or generic work through taste-engine before delivery",
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
        "monitoring covers research ingestion proof",
        "research-ingestion boundary" in monitoring,
        "static proof includes the research-ingestion boundary",
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
    visual_communication = read(okf_root / "foundations" / "visual-communication-hierarchy.md")
    require(
        "visual communication OKF exists",
        "Design intent" in visual_communication
        and "information priority" in visual_communication
        and "message hierarchy" in visual_communication
        and "visual hierarchy" in visual_communication
        and "attention" in visual_communication
        and "reading path" in visual_communication
        and "understanding" in visual_communication
        and "action" in visual_communication
        and "Ethics" in visual_communication
        and "Done Check" in visual_communication,
        "first graphic-design research block is represented as a foundation coordination layer",
    )
    index = read(okf_root / "index.md")
    principles = read(root / "references" / "principles.md")
    require(
        "visual communication OKF is routed",
        "foundations/visual-communication-hierarchy.md" in index
        and "foundations/visual-communication-hierarchy.md" in principles,
        "OKF index and principles router can reach visual communication hierarchy",
    )
    layout_typography = read(okf_root / "foundations" / "layout-typography-composition.md")
    require(
        "layout typography composition OKF exists",
        "composition model" in layout_typography
        and "Grid And Type Area" in layout_typography
        and "Alignment" in layout_typography
        and "Spacing Rhythm" in layout_typography
        and "Typography" in layout_typography
        and "Chinese And Mixed-Language Typesetting" in layout_typography
        and "Editorial And Multi-Page Systems" in layout_typography
        and "Swiss Style" in layout_typography
        and "Done Check" in layout_typography,
        "second graphic-design research block is represented as a layout/type/composition coordination layer",
    )
    require(
        "layout typography composition OKF is routed",
        "foundations/layout-typography-composition.md" in index
        and "foundations/layout-typography-composition.md" in principles,
        "OKF index and principles router can reach layout typography composition",
    )
    visual_language = read(okf_root / "systems" / "visual-language-style-system.md")
    require(
        "visual language style OKF exists",
        "visual vocabulary" in visual_language
        and "Style Versus Decoration" in visual_language
        and "Perceptual" in visual_language
        and "Photography" in visual_language
        and "Illustration" in visual_language
        and "Iconography" in visual_language
        and "Symbols And Motifs" in visual_language
        and "Texture And Material" in visual_language
        and "Art Direction Workflow" in visual_language
        and "Anti-Template Check" in visual_language
        and "Done Check" in visual_language,
        "third graphic-design research block is represented as a visual-language/style-system coordination layer",
    )
    require(
        "visual language style OKF is routed",
        "systems/visual-language-style-system.md" in index
        and "systems/visual-language-style-system.md" in principles,
        "OKF index and principles router can reach visual language and style system",
    )
    taste_engine = read(okf_root / "systems" / "taste-engine.md")
    require(
        "taste engine OKF exists",
        "Design Read" in taste_engine
        and "Taste Dials" in taste_engine
        and "Anti-Default Locks" in taste_engine
        and "Layout-Family Audit" in taste_engine
        and "Asset Credibility" in taste_engine
        and "Taste Critique" in taste_engine
        and "Contract Fields" in taste_engine
        and "Done Check" in taste_engine,
        "Taste Skill mechanisms are represented as operational OKF rather than copied templates",
    )
    require(
        "taste engine OKF is routed",
        "systems/taste-engine.md" in index
        and "systems/taste-engine.md" in principles
        and "references/design-okf/systems/taste-engine.md" in skill,
        "OKF index, principles router, and SKILL.md can reach taste-engine for generic/stiff visual work",
    )
    require(
        "taste engine is default-gated, not template-forced",
        "Every visible artifact should pass a lightweight Taste Checkpoint" in taste_engine
        and "Use Levels" in taste_engine
        and "Quiet Taste" in taste_engine
        and "Type expressiveness" in taste_engine,
        "taste-engine defines light/full/quiet levels and includes type expressiveness",
    )
    type_personality = read(okf_root / "systems" / "type-personality.md")
    require(
        "type personality OKF exists",
        "Task Mode" in type_personality
        and "Type Roles" in type_personality
        and "CJK Voice Map" in type_personality
        and "Latin Voice Map" in type_personality
        and "Mixed Chinese-English Strategy" in type_personality
        and "WebFont, Fallback, And Licensing" in type_personality
        and "Done Check" in type_personality,
        "font-personality research is represented as operational OKF",
    )
    require(
        "type personality OKF is routed",
        "systems/type-personality.md" in index
        and "systems/type-personality.md" in principles
        and "references/design-okf/systems/type-personality.md" in skill,
        "OKF index, principles router, and SKILL.md can reach type-personality",
    )
    brand_identity_media = read(okf_root / "systems" / "brand-identity-media-production.md")
    require(
        "brand identity media production OKF exists",
        "Core Chain" in brand_identity_media
        and "Recognition Mechanisms" in brand_identity_media
        and "Logo System" in brand_identity_media
        and "Brand Guidelines Model" in brand_identity_media
        and "Design System To Delivery" in brand_identity_media
        and "Media Delivery Matrix" in brand_identity_media
        and "Licensing And Rights" in brand_identity_media
        and "Ask Or Proceed" in brand_identity_media
        and "Done Check" in brand_identity_media,
        "fourth graphic-design research block is represented as a brand-identity/media-production bridge",
    )
    require(
        "brand identity media production OKF is routed",
        "systems/brand-identity-media-production.md" in index
        and "systems/brand-identity-media-production.md" in principles,
        "OKF index and principles router can reach brand identity and media production",
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
        "contract has taste signature",
        "## Taste Signature" in contract
        and "Taste dials" in contract
        and "Category defaults avoided" in contract
        and "Layout families or slide archetypes" in contract
        and "Visual memory feature" in contract,
        "DESIGN.md template can preserve taste dials, anti-defaults, layout families, and memory features",
    )
    require(
        "contract has type personality continuity fields",
        "type personality" in contract
        and "fallback stack" in contract
        and "font-rights status" in contract
        and "Type personality:" in contract,
        "DESIGN.md template can preserve type art direction and delivery risks",
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
        "contract has brand identity media specs",
        "## Brand Identity And Media Production Specs" in contract
        and "Brand strategy and recognition anchors" in contract
        and "Logo variants and misuse rules" in contract
        and "Asset naming and delivery package" in contract
        and "Licensing and rights register" in contract
        and "Official platform, vendor, legal, or supplier checks" in contract,
        "DESIGN.md template includes brand identity and cross-media delivery continuity fields",
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
    research_digestion = read(okf_root / "governance" / "research-digestion-llm-wiki.md")
    require(
        "research digestion LLM wiki OKF exists",
        "Layer Model" in research_digestion
        and "LLM wiki digestion" in research_digestion
        and "Wiki Page Types" in research_digestion
        and "Digest Workflow" in research_digestion
        and "Promotion Criteria" in research_digestion
        and "Do Not Promote" in research_digestion
        and "OKF Candidate Template" in research_digestion
        and "Coverage Protocol" in research_digestion
        and "Runtime Boundary" in research_digestion
        and "Done Check" in research_digestion,
        "LLM wiki is represented as a build-time digestion layer before OKF promotion",
    )
    require(
        "research digestion LLM wiki OKF is routed",
        "governance/research-digestion-llm-wiki.md" in index
        and "governance/research-digestion-llm-wiki.md" in principles
        and "governance/research-digestion-llm-wiki.md" in skill,
        "OKF index, principles router, and SKILL.md can reach research digestion when updating knowledge",
    )
    okf_taxonomy = read(okf_root / "governance" / "okf-taxonomy-digestion-map.md")
    require(
        "existing OKF taxonomy digestion map exists",
        "Digestion Status" in okf_taxonomy
        and "Runtime Taxonomy" in okf_taxonomy
        and "Methods" in okf_taxonomy
        and "Foundations" in okf_taxonomy
        and "Content" in okf_taxonomy
        and "Systems" in okf_taxonomy
        and "Digital" in okf_taxonomy
        and "Production" in okf_taxonomy
        and "Governance" in okf_taxonomy
        and "Source-Of-Truth Rules" in okf_taxonomy
        and "Existing OKF Audit" in okf_taxonomy
        and "Gap Handling" in okf_taxonomy,
        "existing OKF concepts are classified by runtime layer with digestion and ownership rules",
    )
    require(
        "existing OKF taxonomy digestion map is indexed",
        "governance/okf-taxonomy-digestion-map.md" in index,
        "OKF index can reach the existing OKF taxonomy and digestion status",
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
        "quality gates include visual communication hierarchy",
        "strongest visual element maps to the most important communication element" in quality
        and "intended first focus, reading path, and action/decision endpoint" in quality
        and "Critical, Important, Useful, and Optional information" in quality
        and "risk, cost, consequence, or trust information" in quality,
        "quality-gates check communication priority, attention path, and action path",
    )
    require(
        "quality gates include layout typography composition",
        "## Layout, Typography, And Composition" in quality
        and "composition model, grid/type-area logic" in quality
        and "Optical alignment" in quality
        and "Chinese text follows one paragraph system" in quality
        and "Mixed Chinese-English text checks" in quality
        and "Swiss Style is used as grid-led clarity" in quality,
        "quality-gates check grid, spacing, type hierarchy, CJK, mixed text, and Swiss method",
    )
    require(
        "quality gates include visual language style system",
        "## Visual Language And Style System" in quality
        and "speak the same concept" in quality
        and "owned visual feature" in quality
        and "deletion test" in quality
        and "Visual vocabulary roles" in quality
        and "Anti-template check" in quality
        and "Asset rights" in quality,
        "quality-gates check visual-language coherence, anti-template specificity, and asset governance",
    )
    require(
        "quality gates include taste engine",
        "## Taste And Anti-Template" in quality
        and "Taste Signature" in quality
        and "light Taste Checkpoint" in quality
        and "category default" in quality
        and "taste dials" in quality
        and "layout-family or slide-archetype audit" in quality
        and "Cards are used because" in quality
        and "what still looks AI-generated" in quality,
        "quality-gates require dials, anti-defaults, layout-family audit, card justification, and AI-tell repair",
    )
    require(
        "quality gates include type personality",
        "Font family choices map to type roles" in quality
        and "Type either recedes for task clarity or stands forward for memory" in quality
        and "Mixed Chinese-English typography checks optical size" in quality
        and "WebFont delivery records WOFF2/fallback strategy" in quality,
        "quality-gates check font voice, mixed-script fit, and webfont delivery risks",
    )
    require(
        "quality gates include brand identity media production",
        "## Brand Identity And Media Production" in quality
        and "recognition anchors" in quality
        and "core rules, application rules, production rules" in quality
        and "Logo variants" in quality
        and "Design tokens and assets map" in quality
        and "Social delivery does not rely on stale memorized dimensions" in quality
        and "Packaging delivery respects supplier dieline" in quality
        and "Licensing and rights register" in quality
        and "final production-ready work" in quality,
        "quality-gates check brand identity, media production, current-source caveats, and rights governance",
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
    marketing_branch = read(root / "references" / "branch-marketing-site.md")
    require(
        "marketing branch routes taste engine",
        "design-okf/systems/taste-engine.md" in marketing_branch
        and "Taste dials" in marketing_branch
        and "layout-family budget" in marketing_branch,
        "marketing pages route distinctive taste and section variety to taste-engine",
    )
    require(
        "presentation branch routes taste engine",
        "design-okf/systems/taste-engine.md" in presentation_branch
        and "slide-archetype variation" in presentation_branch
        and "Do not solve every slide as title plus cards" in presentation_branch,
        "decks route memorable style and slide archetype variety to taste-engine",
    )
    require(
        "presentation branch routes type personality",
        "design-okf/systems/type-personality.md" in presentation_branch
        and "distance readability" in presentation_branch
        and "type roles" in presentation_branch,
        "decks route font memory, device portability, and reading-distance typography to type-personality",
    )
    brand_branch = read(root / "references" / "branch-brand-system.md")
    require(
        "brand branch delegates media production source of truth",
        "design-okf/systems/brand-identity-media-production.md" in brand_branch
        and "cross-media brand kits" in brand_branch
        and "rights registers" in brand_branch,
        "brand branch routes persistent brand identity and media-delivery work to the OKF concept",
    )
    require(
        "graphic branch routes taste engine",
        "design-okf/systems/taste-engine.md" in graphic_branch
        and "Taste dials and anti-default locks" in graphic_branch
        and "vary composition by message role" in graphic_branch,
        "graphic and social work route key visual taste and series variety to taste-engine",
    )
    require(
        "graphic and brand branches route type personality",
        "design-okf/systems/type-personality.md" in graphic_branch
        and "headline type should be the visual memory feature" in graphic_branch
        and "design-okf/systems/type-personality.md" in brand_branch
        and "Type either recedes for utility or creates brand memory" in brand_branch,
        "graphic and brand work route typography art direction and font rights to type-personality",
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
        "Visual communication chain",
        "Information priority",
        "Message hierarchy vs visual hierarchy",
        "Attention and reading path",
        "Understanding and action",
        "Ethical hierarchy",
        "Layout, typography, and composition system",
        "Grid, type area, margins, columns, gutters, baseline, and spacing rhythm",
        "Alignment, optical alignment, visual weight, focal path, and grayscale structure",
        "Typography hierarchy, legibility, readability, line height, line length, and type tone",
        "Font personality, type art direction, conservative-vs-expressive type decisions, and type roles",
        "Chinese typography and mixed Chinese-English typesetting",
        "CJK/Latin voice maps, optical pairing, baseline/weight/size checks, numerals, punctuation, and real-content type testing",
        "Editorial layout and multi-page rhythm",
        "Swiss Style as grid-led method, not style costume",
        "Product problem framing",
        "Product metrics",
        "MVP scope",
        "AI product UX risks",
        "Business/user value tradeoffs",
        "Commercial PPT",
        "Deck narrative",
        "PPT master/template",
        "Visual language and style system",
        "Style versus decoration and anti-template aesthetics",
        "Taste Skill operational mechanisms",
        "Layout variety against card-heavy AI output",
        "Photography, illustration, iconography, symbols, and texture rules",
        "Art direction, moodboard-to-rules, do/do-not examples, and cross-medium style guide",
        "Contextual color/symbol meaning and visual-language ethics",
        "Brand identity, brand image, brand equity, and recognition mechanisms",
        "Logo variants, clear space, minimum size, color/background rules, and misuse examples",
        "Brand guidelines: core, application, production, governance, and do/do-not rules",
        "Design tokens, asset library, naming, delivery package, and DAM-style governance",
        "Screen, print, social, deck, and packaging media delivery",
        "Packaging dieline, barcode, regulatory, supplier, and proofing checks",
        "Licensing, asset rights, copyright, trademark, commissioned work, and rights register",
        "WebFont performance, CJK fallback, font loading, font licensing, and deliverable portability",
        "LLM Wiki digestion layer for raw research before OKF promotion",
        "Raw research, source summaries, wiki synthesis, OKF candidates, and runtime OKF boundary",
        "OKF promotion criteria, do-not-promote rules, coverage protocol, and validation path",
        "Existing OKF taxonomy, runtime-layer classification, and single-source-of-truth boundaries",
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
