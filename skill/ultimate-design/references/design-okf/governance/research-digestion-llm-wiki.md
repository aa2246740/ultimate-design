---
type: Governance Concept
title: Research Digestion And LLM Wiki Layer
description: Build-time workflow for turning raw research into a persistent wiki digestion layer, then promoting stable operational knowledge into OKF and runtime skill references.
tags: [research-digestion, llm-wiki, okf, knowledge-governance, coverage]
---

# Purpose

Use this concept only when updating the skill or absorbing deep research into the OKF bundle. Do not load it during ordinary design execution.

The goal is to prevent raw research from being pasted directly into runtime references. Raw sources should be digested into a persistent wiki-like layer first, then only stable, operational, checkable knowledge should be promoted into OKF.

# Layer Model

```text
raw research
-> source summaries
-> LLM wiki digestion
-> OKF candidates
-> OKF bundle
-> skill runtime
-> design artifacts
```

Layer roles:

- Raw research: original reports, pasted text, PDFs, official docs, papers, examples, and links.
- Source summaries: concise provenance records, stable claims, volatile claims, caveats, and source confidence.
- LLM wiki digestion: interlinked concept notes, terms, contradictions, gaps, examples, and synthesis pages.
- OKF candidates: proposed operational concepts with trigger, boundary, rules, quality gates, and Done Check.
- OKF bundle: stable, typed, agent-consumable knowledge under `references/design-okf/`.
- Skill runtime: `SKILL.md`, branch references, quality gates, scripts, and validators used in real tasks.

LLM wiki is a build-time compilation layer. OKF is the runtime knowledge layer.

# Wiki Page Types

Use these page types when digesting research:

- Source summary: what this source says, why it matters, confidence, volatility, and provenance.
- Concept page: one reusable design or governance concept with links to related concepts.
- Term page: terminology, preferred wording, avoided synonyms, and translation notes.
- Pattern page: repeatable method, checklist, or workflow found across sources.
- Conflict page: conflicting advice, source disagreement, or unresolved tradeoff.
- Gap page: missing research, weak confidence, or user follow-up needed.
- Synthesis page: compressed conclusion that may become an OKF candidate.

Keep wiki pages outside normal runtime unless the user explicitly asks to inspect research digestion. They may live in a project workspace, not necessarily inside the skill.

# Digest Workflow

1. Register sources.
   - Record title, path or URL, date accessed, author or origin when known, source type, and confidence.
   - Mark volatile domains: laws, platform specs, software APIs, pricing, product rules, social-media dimensions, print/vendor specs, font EULAs, and legal requirements.

2. Summarize each source.
   - Extract stable principles.
   - Extract volatile claims.
   - Extract examples separately from rules.
   - Record source limitations and caveats.
   - Avoid long verbatim quotes.

3. Build wiki digestion.
   - Create or update concept, term, pattern, conflict, gap, and synthesis pages.
   - Link related concepts explicitly.
   - Separate "known", "assumed", "current-source required", and "not yet researched".

4. Map against existing OKF.
   - Existing OKF concept: update in place if the idea already has a home.
   - New OKF concept: create only when it introduces a reusable branch, foundation, system, production, or governance concept.
   - Quality gate: add only if the idea must be checked before delivery.
   - Branch reference: add only if it changes task routing or medium-specific behavior.
   - Wiki only: keep examples, long pedagogy, source archaeology, and weak-confidence notes out of runtime.

5. Promote OKF candidates.
   - Write a typed OKF concept with purpose, trigger, boundary, core model, rules, caveats, and Done Check.
   - Add it to `design-okf/index.md`.
   - Route it from `references/principles.md` or a branch reference when agents need to find it.
   - Add relevant quality gates, design-contract fields, or validation hooks.
   - Update `governance/research-coverage-map.md`.
   - Extend `scripts/flow_check.py` when the new knowledge must be proven wired.

6. Validate.
   - Run skill validation.
   - Run static flow proof.
   - Run package/release scan when maintaining the open-source copy.
   - Forward-test only when the new knowledge changes real task behavior enough to justify the cost.

# Promotion Criteria

Promote wiki digestion into OKF only when the knowledge is:

- Reusable across multiple design tasks or future agents.
- Operational: it changes decisions, workflow, routing, quality checks, or verification.
- Checkable: it can produce a Done Check, quality gate, script assertion, or review criterion.
- Stable enough: it is not only a current platform number, vendor setting, or legal detail.
- Non-duplicative: it has a clear single source of truth or updates an existing one.
- Branch-relevant: it belongs to a method, foundation, content, system, digital, production, or governance branch.

If the knowledge is useful but not stable or operational, keep it in wiki digestion and reference it from coverage or source notes.

# Do Not Promote

Do not promote these directly into OKF:

- Full research reports.
- Long teaching exposition.
- One-off examples that do not generalize.
- Platform sizes, ad specs, social safe zones, legal thresholds, print presets, or package regulations that require current official sources.
- Unsupported source claims.
- Duplicate versions of a rule already represented in an OKF concept.
- Personal taste statements without a decision rule.

# OKF Candidate Template

```md
---
type: Governance Concept | Design System Concept | Foundation Concept | Production Concept | Content Concept | Method Concept
title:
description:
tags: []
---

# Purpose

# Trigger

# Boundary

# Core Model

# Rules

# Current-Source Caveats

# Done Check

# Source Notes
```

# Coverage Protocol

Every promoted concept needs traceability:

- Add a row to `governance/research-coverage-map.md`.
- Point to the OKF concept and any branch/quality gate affected.
- Mark coverage honestly: covered, conditional, caveated, wiki-only, or not yet covered.
- Record known limits when official, vendor, legal, or stakeholder review remains authoritative.

Coverage is not a claim that the design output is excellent. It only proves the research has an indexed home and routing path.

# Runtime Boundary

Ordinary design runs should not load raw research or wiki digestion. They should load:

- `SKILL.md` for the process.
- Branch references for the surface.
- OKF concepts selected by the router.
- Quality gates and visual verification references before delivery.

Use wiki digestion only for skill development, research absorption, audits of missing knowledge, or user-requested proof of how research became OKF.

# Done Check

This digestion pass is done when:

1. Raw sources have provenance and confidence notes.
2. Stable principles, volatile claims, examples, conflicts, and gaps are separated.
3. Existing OKF concepts were updated instead of duplicated.
4. New OKF concepts exist only where a reusable operational concept is needed.
5. Index, router, branch references, quality gates, design-contract fields, and flow proof are updated when affected.
6. Coverage map records what was promoted, caveated, or left wiki-only.
7. Validation passes.

# Source Notes

Research basis includes the LLM Wiki pattern of incrementally compiling raw documents into persistent interlinked Markdown knowledge, plus OKF and Knowledge Catalog ideas of curated, governed, agent-consumable context. Treat LLM wiki as a digestion layer and OKF as the skill's runtime knowledge layer.
