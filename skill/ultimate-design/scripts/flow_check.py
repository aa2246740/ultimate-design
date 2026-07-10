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
        "Run OKF preflight.",
        "Bootstrap the contract.",
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
    pro_mode = read(root / "references" / "pro-mode.md")
    require(
        "pro mode branch is complete and bounded",
        "references/pro-mode.md" in skill
        and "## Consensus" in pro_mode
        and "## Decision Snapshot" in pro_mode
        and "## Post-Consensus Gate" in pro_mode
        and "at most two directly relevant task-facing OKF concepts" in pro_mode
        and "### Active OKF Concepts" in pro_mode
        and "### Support References" in pro_mode
        and "Support references do not consume the active concept budget" in pro_mode
        and "## Done Criteria" in pro_mode,
        "the conditional consensus branch is loadable without bloating the default workflow",
    )
    require(
        "quality gates are always loaded",
        "references/quality-gates.md" in skill and "before final delivery, always" in skill,
        "final quality gate pointer is present",
    )
    require(
        "OKF preflight is before artifact work",
        "For every meaningful visible design run, treat OKF as **preflight**" in skill
        and "before choosing a direction or making a new artifact" in skill
        and "OKF Decision Bindings" in skill
        and "Reference | Decision | Artifact target | Verification" in skill
        and positions[3] < positions[4] < positions[5] < positions[6],
        "OKF is loaded and bound to decisions before Bootstrap, Choose, and Make",
    )
    require(
        "motion display-window default is in main skill",
        "display-window" in skill
        and "entry-play" in skill
        and "view-entry" in skill
        and "entry-or-view" in skill
        and "scroll-linked only when progress itself carries meaning" in skill,
        "Ultimate Design default motion rule can steer future projects without loading deep OKF first",
    )
    require(
        "proof run gate is machine-checkable for weak/headless agents",
        "### Proof Run Gate" in skill
        and "Pi, a local/weak/headless model" in skill
        and "references/proof-run-html.md" in skill
        and "artifact-first order" in skill
        and "OKF decision bindings" in skill
        and "unified proof command" in skill
        and "rendered UI" in skill
        and "motion reports" in skill,
        "proof runs route to one compact branch with artifact, OKF, rendered, and motion evidence",
    )
    require(
        "light taste checkpoint is default for visible artifacts",
        "For every visible artifact, apply a lightweight **Taste Checkpoint** by default" in skill
        and "keep the checkpoint brief" in skill
        and "If no expressive style is needed" in skill,
        "visible artifacts pass a taste checkpoint without forcing expressive styling everywhere",
    )
    require(
        "necessary judgment is workflow-gated",
        "Necessary Judgment" in skill
        and "necessary-design-judgment.md" in skill
        and "what can be removed or demoted" in skill
        and "necessity/care/material-honesty failure" in skill
        and "necessary judgment when it materially shaped the work" in skill,
        "main workflow applies necessary judgment during direction, critique, repair, and governance",
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
        and "success signal" in skill
        and "Do not load it solely because the artifact is product UI" in skill,
        "product-sense loads for unresolved product judgment rather than every product UI",
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
        "Request Anchor" in skill
        and "user success criteria" in skill
        and "How the result maps back" in skill,
        "verify and final response must map back to user request",
    )

    principles = read(root / "references" / "principles.md")
    direct_route_targets = [
        "design-okf/foundations/gestalt-composition.md",
        "design-okf/foundations/visual-hierarchy.md",
        "design-okf/systems/color-system.md",
        "design-okf/systems/typography-system.md",
        "design-okf/digital/accessibility-usability.md",
        "design-okf/digital/responsive-interaction.md",
        "design-okf/production/data-viz-i18n-legal.md",
        "design-okf/governance/design-to-code-governance.md",
        "design-okf/governance/machine-verification-ci.md",
    ]
    missing_direct_routes = [target for target in direct_route_targets if target not in principles]
    require(
        "high-value OKF concepts have direct routes",
        not missing_direct_routes,
        "all direct routes present" if not missing_direct_routes else ", ".join(missing_direct_routes),
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
    require(
        "necessary judgment critique loop",
        "Check necessary judgment for polished visible artifacts" in audit
        and "design-okf/foundations/necessary-design-judgment.md" in audit
        and "Prefer necessary minimalism" in audit,
        "audit-polish routes fake minimalism, overdecoration, and template-like styling through necessary judgment",
    )

    monitoring = read(root / "references" / "monitoring.md")
    proof_run_html = read(root / "references" / "proof-run-html.md")
    require(
        "HTML proof-run branch exists",
        "HTML Proof Run" in proof_run_html
        and "Required Reading" in proof_run_html
        and "Execution Order" in proof_run_html
        and "data-ud-check" in proof_run_html
        and "data-ud-motion" in proof_run_html
        and "run_html_proof.mjs" in proof_run_html
        and "repair-brief.md" in proof_run_html
        and "Coupled SVG Draw Pattern" in proof_run_html
        and "0% sample would already show a partially drawn path" in proof_run_html
        and 'data-ud-motion-end="bottom 100%"' in proof_run_html
        and "OKF Decision Bindings" in proof_run_html
        and "--require-okf-usage" in proof_run_html
        and "Reduced motion must leave SVG drawing visible and complete" in proof_run_html
        and "Done Signal" in proof_run_html,
        "weak/headless HTML runs have a compact execution branch with coupled marker and proof-run guidance",
    )
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
    require(
        "monitoring measures OKF utilization beyond file reads",
        "OKF Utilization Funnel" in monitoring
        and "indexed -> routed -> read -> decision-bound -> artifact-bound -> verified -> lifted" in monitoring
        and "validate_okf_usage.py" in monitoring
        and "Workflow-only output versus full OKF output" in monitoring,
        "monitoring separates indexing, routing, decision binding, verification, and outcome lift",
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
        and "Necessary Judgment Lens" in taste_engine
        and "../foundations/necessary-design-judgment.md" in taste_engine
        and "Taste Dials" in taste_engine
        and "Anti-Default Locks" in taste_engine
        and "Layout-Family Audit" in taste_engine
        and "Asset Credibility" in taste_engine
        and "Taste Critique" in taste_engine
        and "Contract Fields" in taste_engine
        and "Done Check" in taste_engine,
        "Taste Skill mechanisms are represented as operational OKF rather than copied templates",
    )
    necessary_judgment = read(okf_root / "foundations" / "necessary-design-judgment.md")
    require(
        "necessary design judgment OKF exists",
        "Core Model" in necessary_judgment
        and "Human Value Lens" in necessary_judgment
        and "Purpose:" in necessary_judgment
        and "Agency:" in necessary_judgment
        and "Responsibility:" in necessary_judgment
        and "Delight:" in necessary_judgment
        and "Delete Test" in necessary_judgment
        and "Replace Test" in necessary_judgment
        and "Move Test" in necessary_judgment
        and "Justification Test" in necessary_judgment
        and "Care Test" in necessary_judgment
        and "Material Honesty Test" in necessary_judgment
        and "Scene Fit Test" in necessary_judgment
        and "not an Apple-style preset" in necessary_judgment
        and "Done Check" in necessary_judgment,
        "Apple/Jony Ive/Rams/Hara research is represented as a checkable judgment lens rather than a style preset",
    )
    require(
        "necessary design judgment OKF is routed",
        "foundations/necessary-design-judgment.md" in index
        and "foundations/necessary-design-judgment.md" in principles
        and "references/design-okf/foundations/necessary-design-judgment.md" in skill,
        "OKF index, principles router, and SKILL.md can reach necessary design judgment",
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
    require(
        "taste engine includes necessary judgment",
        "What was removed or demoted because it was not necessary" in taste_engine
        and "Which relationships now feel inevitable rather than arbitrary" in taste_engine
        and "Where did craft tolerance, care, or material honesty improve the design" in taste_engine
        and "Necessary judgment:" in taste_engine,
        "taste-engine must apply necessity before style dials and record the result when durable",
    )
    motion_language = read(okf_root / "systems" / "motion-language.md")
    require(
        "motion language OKF exists",
        "Motion Purpose" in motion_language
        and "Exposure And Response" in motion_language
        and "Fluid Interaction" in motion_language
        and "live presentation state" in motion_language
        and "release velocity" in motion_language
        and "Motion Budget" in motion_language
        and "Choreography Layers" in motion_language
        and "Scroll Motion" in motion_language
        and "Accessibility And Safety" in motion_language
        and "Performance Rules" in motion_language
        and "Contract Fields" in motion_language
        and "Done Check" in motion_language,
        "motion research is represented as purpose-led, conditional OKF",
    )
    require(
        "motion language OKF is routed",
        "systems/motion-language.md" in index
        and "systems/motion-language.md" in principles
        and "references/design-okf/systems/motion-language.md" in skill,
        "OKF index, principles router, and SKILL.md can reach motion-language for meaningful animation",
    )
    require(
        "motion language is conditional, not forced",
        "Do not load this concept for ordinary static layouts" in motion_language
        and "Static communication must work first" in motion_language
        and "If it only says \"this is premium\"" in motion_language,
        "motion-language keeps static-first design and avoids decorative animation by default",
    )
    motion_contract = read(okf_root / "systems" / "motion-contract.md")
    require(
        "motion contract OKF exists",
        "Contract Fields" in motion_contract
        and "Gesture Contract" in motion_contract
        and "Response point" in motion_contract
        and "Interruption model" in motion_contract
        and "Velocity and momentum" in motion_contract
        and "Implementation Routing" in motion_contract
        and "GSAP Pattern Rules" in motion_contract
        and "Scroll-Linked SVG Contract" in motion_contract
        and "Reveal Contract" in motion_contract
        and "Validation" in motion_contract
        and "Done Check" in motion_contract,
        "motion-contract turns animation intent into implementation routing and browser-sampled evidence",
    )
    require(
        "motion contract OKF is routed",
        "systems/motion-contract.md" in index
        and "systems/motion-contract.md" in principles
        and "references/design-okf/systems/motion-contract.md" in skill,
        "OKF index, principles router, and SKILL.md can reach motion-contract for requested animation behavior",
    )
    require(
        "motion contract is verification-oriented",
        "Static screenshots are not motion validation" in motion_contract
        and "data-ud-motion" in motion_contract
        and "visualSubjectFocusProgress -> strokeRevealProgress" in motion_contract
        and "Implementation coupling" in motion_contract
        and "failed evidence loop" in motion_contract
        and "display-window" in motion_contract
        and "entry-play" in motion_contract
        and "view-entry" in motion_contract
        and "entry-or-view" in motion_contract
        and "Timing Bands" in motion_contract
        and "Timing band" in motion_contract
        and "Duration and easing tokens" in motion_contract
        and "focus-complete" in motion_contract
        and "exit-complete" in motion_contract
        and "data-ud-motion-end-trigger" in motion_contract
        and "scripts/validate_motion_contract.mjs" in motion_contract,
        "motion-contract requires display-window trigger choice, explicit markers, focus-complete, exit guard, and a validation script",
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
    require(
        "type personality does not absorb typography mechanics",
        "Do not load it for mixed-script mechanics alone" in skill
        and "use `typography-system.md` for scale" in skill
        and "Mixed-script layout mechanics alone route to `typography-system.md`" in principles,
        "font voice/pairing and typography mechanics have separate triggers",
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
        "contract has OKF preflight",
        "## OKF Preflight" in contract
        and "### Active OKF Concepts" in contract
        and "### Support References" in contract
        and "### Decision Record" in contract
        and "Constraints extracted:" in contract
        and "Deliberate exceptions:" in contract
        and "Verification hooks:" in contract,
        "DESIGN.md template includes a pre-artifact OKF application record",
    )
    require(
        "contract has OKF decision bindings",
        "## OKF Decision Bindings" in contract
        and "| Reference | Decision | Artifact target | Verification |" in contract
        and "A reference that changes no decision is not active knowledge" in contract,
        "DESIGN.md binds active OKF concepts to concrete decisions, targets, and evidence",
    )
    require(
        "contract has taste signature",
        "## Taste Signature" in contract
        and "Necessary judgment:" in contract
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
        "contract has motion strategy",
        "## Motion Strategy" in contract
        and "Motion purpose:" in contract
        and "Motion budget:" in contract
        and "Reduced-motion fallback:" in contract
        and "Performance risks:" in contract,
        "DESIGN.md template can preserve motion purpose, budget, reduced motion, and performance risk",
    )
    require(
        "contract has motion contract",
        "## Motion Contract" in contract
        and "Motion ids and target selectors:" in contract
        and "Implementation route:" in contract
        and "Timing band:" in contract
        and "Duration and easing tokens:" in contract
        and "Progress mapping:" in contract
        and "Acceptance samples and tolerance:" in contract
        and "Validation command and report path:" in contract,
        "DESIGN.md template can preserve executable animation behavior and evidence paths",
    )
    require(
        "contract has rendered UI audit field",
        "Rendered UI Audit:" in contract,
        "DESIGN.md template can preserve rendered browser-measurement verification status",
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
        and "Do not put `clamp()`" in contract
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
        "## Request Fit" in quality
        and "latest override" in quality
        and "success criteria" in quality
        and "Requirement drift" in quality,
        "quality-gates checks artifact against user-specific request",
    )
    require(
        "quality gates include content",
        "## Content And Hierarchy" in quality
        and "CTAs" in quality
        and "Critical meaning is not carried only" in quality,
        "quality-gates includes mandatory content gate",
    )
    require(
        "quality gates include visual communication hierarchy",
        "Message order follows the user's decision or task path" in quality
        and "Primary, secondary, and tertiary information" in quality
        and "size, weight, position, spacing, contrast, or rhythm" in quality,
        "quality-gates check communication priority, attention path, and action path",
    )
    require(
        "quality gates include layout typography composition",
        "## Typography" in quality
        and "Mixed Chinese/English" in quality
        and "optical-size need" in quality
        and "foundations/layout-typography-composition.md" in principles,
        "quality-gates check grid, spacing, type hierarchy, CJK, mixed text, and Swiss method",
    )
    require(
        "quality gates include visual language style system",
        "## Necessary Taste" in quality
        and "owned visual feature" in quality
        and "generic cards" in quality
        and "category defaults" in quality
        and "asset/font/image/icon rights" in quality,
        "quality-gates check visual-language coherence, anti-template specificity, and asset governance",
    )
    require(
        "quality gates include rendered UI audit",
        "## Rendered Integrity" in quality
        and "Rendered UI Audit" in quality
        and "no active fail findings" in quality
        and "data-ud-allow" in quality,
        "quality-gates require non-visual browser-measured UI audit evidence",
    )
    require(
        "quality gates include taste engine",
        "## Necessary Taste" in quality
        and "design read" in quality
        and "type personality" in quality
        and "layout-family budget" in quality
        and "visual memory feature" in quality
        and "category defaults" in quality,
        "quality-gates require dials, anti-defaults, layout-family audit, card justification, and AI-tell repair",
    )
    require(
        "quality gates include necessary judgment",
        "## Necessary Taste" in quality
        and "necessity, replacement, move, justification, care, material honesty, and scene-fit tests" in quality
        and "Delight emerges from clarity, agency, craft, and coherence" in quality,
        "quality-gates check necessity, inevitability, craft tolerance, care, material honesty, scene fit, and non-imitation",
    )
    require(
        "quality gates include type personality",
        "Expressive type is reserved" in quality
        and "Mixed Chinese/English work checks optical size" in quality
        and "WebFont loading" in quality
        and "license status" in quality,
        "quality-gates check font voice, mixed-script fit, and webfont delivery risks",
    )
    require(
        "quality gates include motion language",
        "## Motion" in quality
        and "Static communication and operation work before animation" in quality
        and "one primary purpose" in quality
        and "frequency-appropriate motion budget" in quality
        and "reduced-motion behavior" in quality
        and "Transform/opacity" in quality,
        "quality-gates check motion purpose, budget, do-not-move zones, reduced motion, and performance",
    )
    require(
        "quality gates include motion contract",
        "Gesture-driven motion starts from the live presentation state" in quality
        and "Scroll remains user-controlled" in quality
        and "scripts/validate_motion_contract.mjs" in quality
        and "scroll-linked, SVG drawing, reveal no-flash, or reduced-motion claims" in quality,
        "quality-gates check executable motion contracts, display-window trigger choice, sampled SVG progress, focus-complete, exit guard, reveal flash, and validation evidence",
    )
    require(
        "quality gates include brand identity media production",
        "## Production Integrity" in quality
        and "platform, vendor, printer, supplier, legal, and license facts" in quality
        and "asset/font/image/icon rights" in quality
        and "branch-brand-system.md" in quality
        and "graphic-print.md" in quality,
        "quality-gates check brand identity, media production, current-source caveats, and rights governance",
    )
    require(
        "quality gates include product sense",
        "branch-web-product.md" in quality
        and "intended task" in quality
        and "non-goals" in quality,
        "quality-gates checks product fit for product-oriented design",
    )
    require(
        "quality gates include presentation deck",
        "branch-presentation.md" in quality
        and "title story, claim/evidence/action, density, charts, master, accessibility, export" in quality
        and "selected branch's Done Criteria" in quality,
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
    require(
        "graphic branch routes palette creation without duplicating composition",
        "design-okf/systems/color-system.md" in graphic_branch
        and "creating or materially changing the palette" in graphic_branch
        and "composition rules below own a conventional single-message poster" in graphic_branch
        and "only when grouping" in graphic_branch,
        "graphic work spends OKF budget on color when needed and loads Gestalt only for a real composition problem",
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
    web_branch = read(root / "references" / "branch-web-product.md")
    responsive_interaction = read(okf_root / "digital" / "responsive-interaction.md")
    require(
        "digital branches route motion language",
        "design-okf/systems/motion-language.md" in marketing_branch
        and "design-okf/systems/motion-language.md" in web_branch
        and "design-okf/systems/motion-language.md" in presentation_branch
        and "../systems/motion-language.md" in responsive_interaction,
        "marketing, web-product, presentation, and responsive-interaction references route nontrivial motion to motion-language",
    )
    require(
        "digital branches route motion contract",
        "design-okf/systems/motion-contract.md" in marketing_branch
        and "design-okf/systems/motion-contract.md" in web_branch
        and "design-okf/systems/motion-contract.md" in presentation_branch
        and "../systems/motion-contract.md" in responsive_interaction,
        "marketing, web-product, presentation, and responsive-interaction references route requested animation behavior to motion-contract",
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
    branch_docs = {
        "web-product": web_branch,
        "marketing-site": marketing_branch,
        "presentation": presentation_branch,
        "graphic-print": graphic_branch,
        "brand-system": brand_branch,
        "tokens-components": tokens_branch,
        "audit-polish": audit,
    }
    missing_done = [name for name, text in branch_docs.items() if "## Done Criteria" not in text]
    require(
        "every execution branch owns Done Criteria",
        not missing_done,
        "all branches have local completion criteria" if not missing_done else ", ".join(missing_done),
    )

    machine = read(okf_root / "governance" / "machine-verification-ci.md")
    require(
        "machine verification includes DESIGN.md tooling",
        "@google/design.md lint" in machine
        and "validate_design_contract.py" in machine
        and "Broken token references" in machine,
        "official tooling and local fallback validator are routed",
    )
    visual_verification = read(root / "references" / "visual-verification.md")
    require(
        "visual verification documents rendered UI audit",
        "## Rendered UI Audit" in visual_verification
        and "ultimate-design.rendered-ui-audit.v1" in visual_verification
        and "findings[]" in visual_verification
        and "horizontal overflow" in visual_verification
        and "visible interactive target size" in visual_verification
        and "data-ud-allow" in visual_verification
        and "optional enrichment" in visual_verification,
        "visual-verification defines the non-visual browser-measured audit contract",
    )
    require(
        "visual verification routes motion validation",
        "Motion Integrity" in visual_verification
        and "scripts/validate_motion_contract.mjs" in visual_verification
        and "data-ud-motion" in visual_verification
        and "data-ud-motion-end-trigger" in visual_verification
        and "data-ud-motion-subject" in visual_verification
        and "data-ud-motion-trigger-model" in visual_verification
        and "entry-or-view" in visual_verification
        and "data-ud-motion-focus-at" in visual_verification
        and "display-window" in visual_verification
        and "focus-complete" in visual_verification
        and "strokeDashoffset" in visual_verification
        and "Reduced-motion checks" in visual_verification,
        "visual-verification routes declared motion contracts to browser-sampled display-window and focus-complete checks",
    )
    require(
        "visual verification defines cmux Computer Use fallback",
        "## Cmux + Computer Use Fallback" in visual_verification
        and "ultimate-design.computer-use-visual-fallback.v1" in visual_verification
        and "must not set `reportFresh`" in visual_verification
        and "Restore the user's cmux workspace" in visual_verification
        and "cmux + Computer Use fallback" in read(root / "references" / "pro-mode.md")
        and "visible-browser fallback" in read(root / "references" / "proof-run-html.md"),
        "browser-launch failures route to visible cmux evidence without impersonating machine proof",
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
    require(
        "DESIGN.md validator checks OKF preflight",
        "OKF_PREFLIGHT_FIELDS" in validator
        and "OKF Preflight section missing" in validator
        and "OKF Preflight field missing" in validator
        and "OKF Preflight field is empty" in validator,
        "local validator enforces OKF preflight in strict mode",
    )
    okf_usage_validator_path = root / "scripts" / "validate_okf_usage.py"
    okf_usage_validator = read(okf_usage_validator_path)
    require(
        "OKF usage validator exists",
        okf_usage_validator_path.exists()
        and "ultimate-design.okf-usage.v1" in okf_usage_validator
        and "OKF Decision Bindings" in okf_usage_validator
        and "Active OKF concept has no decision binding" in okf_usage_validator,
        "local validator rejects active OKF concepts that do not bind to a decision, artifact target, and verification hook",
    )
    okf_graph_validator_path = root / "scripts" / "validate_okf_graph.py"
    okf_graph_validator = read(okf_graph_validator_path)
    require(
        "OKF graph validator exists",
        okf_graph_validator_path.exists()
        and "ultimate-design.okf-graph.v1" in okf_graph_validator
        and "missing_from_index" in okf_graph_validator
        and "broken_links" in okf_graph_validator
        and "direct_runtime_route_count" in okf_graph_validator
        and "unexpected_index_only_concepts" in okf_graph_validator,
        "the shipped bundle can prove index completeness, link integrity, metadata, and direct route reachability",
    )
    motion_validator_path = root / "scripts" / "validate_motion_contract.mjs"
    motion_validator = read(motion_validator_path)
    html_validator_path = root / "scripts" / "validate_html_visual.mjs"
    html_validator = read(html_validator_path)
    proof_runner_path = root / "scripts" / "run_html_proof.mjs"
    proof_runner = read(proof_runner_path)
    require(
        "HTML proof runner script exists",
        "run_html_proof.mjs" in str(proof_runner_path)
        and "ultimate-design.html-proof.v1" in proof_runner
        and "validate_design_contract.py" in proof_runner
        and "validate_okf_usage.py" in proof_runner
        and "validate_html_visual.mjs" in proof_runner
        and "validate_motion_contract.mjs" in proof_runner
        and "data-ud-motion" in proof_runner
        and "reportFresh" in proof_runner
        and "rmSync(visualOut" in proof_runner
        and "rmSync(motionOut" in proof_runner
        and "html-proof-report.json" in proof_runner
        and "repair-brief.md" in proof_runner,
        "unified proof runner executes design, rendered UI, and motion validators for weak/headless agents",
    )
    require(
        "HTML proof runner can require OKF usage evidence",
        "--require-okf-usage" in proof_runner
        and "OKF decision binding validation" in proof_runner
        and "requireOkfUsage" in proof_runner,
        "monitored proof runs can fail when routed knowledge is not bound to the artifact",
    )
    require(
        "rendered UI audit validator script exists",
        "validate_html_visual.mjs" in str(html_validator_path)
        and "ultimate-design.rendered-ui-audit.v1" in html_validator
        and "auditKind" in html_validator
        and "findings" in html_validator
        and "horizontal-overflow" in html_validator
        and "missing-accessible-name" in html_validator
        and "target-size" in html_validator
        and "data-ud-allow" in html_validator
        and "pageMinSpacingPx" in html_validator
        and "data-ud-min-gap" in html_validator
        and "allowance-expired" in html_validator,
        "local browser validator emits structured Rendered UI Audit findings",
    )
    fixture_root = root / "test-fixtures" / "rendered-ui-audit"
    require(
        "rendered UI audit fixtures exist",
        (fixture_root / "clean-pass.html").exists()
        and (fixture_root / "horizontal-overflow-fail.html").exists()
        and (fixture_root / "clipping-fail.html").exists()
        and (fixture_root / "occlusion-fail.html").exists()
        and (fixture_root / "occlusion-allowed-warn.html").exists()
        and (fixture_root / "icon-button-missing-name-fail.html").exists()
        and (fixture_root / "small-target-fail.html").exists()
        and (fixture_root / "decorative-overlay-pass.html").exists()
        and (fixture_root / "page-related-zones-pass.html").exists()
        and (fixture_root / "page-tight-spacing-fail.html").exists(),
        "fixture suite covers pass, overflow, clipping, occlusion, allowed occlusion, a11y name, target size, decorative overlay, and page spacing calibration",
    )
    require(
        "motion validator script exists",
        "validate_motion_contract.mjs" in str(motion_validator_path)
        and "data-ud-motion" in motion_validator
        and "data-ud-motion-end-trigger" in motion_validator
        and "data-ud-motion-subject" in motion_validator
        and "data-ud-motion-trigger-model" in motion_validator
        and "entry-or-view" in motion_validator
        and "data-ud-motion-focus-at" in motion_validator
        and "initialVisibilityRatio" in motion_validator
        and "focusTiming" in motion_validator
        and "focusCompleteY" in motion_validator
        and "exitCompleteY" in motion_validator
        and "strokeDashoffset" in motion_validator
        and "reducedMotion" in motion_validator
        and "motion-validation-report.json" in motion_validator,
        "local browser validator samples motion contract markers, display-window timing, SVG stroke progress, focus-complete, exit guard, and reduced motion",
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
        "Apple / Jony Ive / Rams / Hara design judgment philosophy",
        "Necessity, inevitability, delete/replace/move/justification tests",
        "Care, craft tolerance, material honesty, hidden complexity, and emotional precision",
        "Apple visual-surface caveat, brand imitation risk, and source-confidence boundary",
        "Jony Ive influence and Apple product case studies",
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
        "Web motion and animation design",
        "Motion contract, GSAP routing, display-window SVG drawing, focus-complete timing, reveal no-flash behavior, and browser-sampled motion validation",
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
