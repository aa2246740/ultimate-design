# Ultimate Design

Self-contained OKF design workflow for AI agents.

Official site: https://aa2246740.github.io/ultimate-design/

Ultimate Design is an Agent Skill for Codex, Claude Code, Pi Agent, and other Agent Skills-compatible harnesses. It turns vague design requests into governed design work: a brief, a `DESIGN.md` contract when persistence matters, routed OKF knowledge, a concrete artifact, critique/repair, rendered verification, and reusable design memory for the next agent.

It is not a template pack, a style preset, or a wrapper around another design skill. The skill carries its own contract loop, content model, Taste Checkpoint, OKF references, quality gates, and validators.

## What's New In 0.4.1

- Cross-agent verification clarification: the evidence protocol is agent-neutral. The bundled pinned browser runtime and the cmux + Computer Use procedure are optional implementation adapters, not requirements for using Ultimate Design.

## Development Evidence

Ultimate Design's 0.4 hardening loop used GPT-5.6 SOL Ultra as a high-agency evaluator: it generated and inspected real artifacts, exposed proof-path failures, and drove repair cycles. That model was used during development and evaluation, not as a runtime dependency. Any supported Agent can use the resulting skill and its evidence protocol.

## What's New In 0.4

- Decision-bound OKF: active concepts must change a concrete decision, artifact target, and verification hook; graph and usage validators catch orphaned or decorative knowledge.
- Pro mode hardening: `--pro` freezes a compact decision snapshot, creates the visible artifact early, and requires critique, repair, verification, and governance before delivery.
- Stronger Rendered UI Audit: calibrated semantic-zone spacing, related-zone handling, visibility and occlusion sampling, stale-report rejection, and stricter proof freshness.
- Purpose-led motion proof: display-window timing, scroll-linked completion, reveal behavior, and reduced-motion claims are tied to the same selectors used by the artifact.
- Evidence integrity: fresh automated reports and visible review evidence are recorded separately, so a fallback can never masquerade as deterministic proof.

## What's New In 0.3

- Proof Run Gate: compact HTML proof branch for Pi, weak/local/headless models, CLI evals, and debug runs.
- Unified HTML proof command: `run_html_proof.mjs` runs contract validation, Rendered UI Audit, and motion validation, then writes a repair brief when a gate fails.
- Rendered UI Audit v1: structured browser-measured findings for marked-zone integrity, horizontal overflow, visible interactive target size, missing accessible names, clipping, and occlusion allowances.
- Coupled evidence loop: `data-ud-check`, `data-ud-motion`, contract fields, implementation selectors, and validator reports must describe the same artifact behavior.
- Validation fixtures: small public HTML cases that prove pass/fail coverage for overflow, clipping, occlusion, accessible names, target size, and decorative overlays.

## What's New In 0.2

- Necessary Design Judgment: a philosophy layer for necessity, inevitability, care, craft tolerance, material honesty, and scene fit. It teaches restraint and precision without copying Apple-style surfaces.
- Stronger Taste Engine: taste now passes through necessary judgment before style dials, so expression serves the content instead of becoming decoration.
- Motion Language: purpose-led animation guidance for web pages, HTML decks, scroll storytelling, and microinteractions, with reduced-motion and performance rules.
- Type Personality: clearer font-selection guidance for utility, content, display, CJK/Latin mixed text, fallback, and licensing risk.
- Stricter visual validation: semantic-zone checks, occlusion sampling, spacing checks, and stronger final quality gates for obvious layout mistakes.

Most frontend design skills optimize for styling or code generation. Ultimate Design optimizes the full professional design loop:

1. Preserve the original user request with a Request Anchor.
2. Convert intent, content, visual rules, accessibility, and quality gates into a design contract.
3. Load only the relevant OKF concept files instead of dumping all research into context.
4. Make the artifact across web, product UI, decks, graphics, brand systems, content design, or audits.
5. Critique and repair before final delivery.
6. Verify rendered output, not just source code.
7. Govern the contract so later agents do not have to reverse-engineer the design.

## Why OKF

OKF means the design knowledge is split into small, typed concept files with an index and routing rules. The skill can load product sense for a dashboard, commercial deck knowledge for a PPT, print caveats for a poster, content strategy for dense copy, or visual verification rules for screenshotable artifacts.

That is the core selling point: **the skill behaves like an indexed design operating system, not a giant prompt.**

## Repository Layout

```text
.
├── skill/ultimate-design/        # Installable Agent Skill
│   ├── SKILL.md                  # Core operating loop and routing rules
│   ├── agents/openai.yaml        # UI metadata
│   ├── references/               # Branch references and OKF bundle
│   └── scripts/                  # Flow, contract, and visual validators
├── docs/                         # Bilingual official site for GitHub Pages
├── integrations/                 # Codex, Claude Code, and Pi Agent usage notes
└── scripts/                      # Install and integration helpers
```

## Install

Install from npm:

```bash
npx ultimate-design-skill@latest --target codex
npx ultimate-design-skill@latest --target claude-code
npx ultimate-design-skill@latest --target pi-agent
```

Or install into a common local agent from a cloned repo:

```bash
npm run install:codex
npm run install:claude
npm run install:pi
```

Or copy the installable skill folder manually.

For Codex, use the Agent Skills user folder:

```bash
mkdir -p ~/.agents/skills
cp -R skill/ultimate-design ~/.agents/skills/ultimate-design
```

For Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R skill/ultimate-design ~/.claude/skills/ultimate-design
```

For Pi Agent:

```bash
mkdir -p ~/.pi/agent/skills
cp -R skill/ultimate-design ~/.pi/agent/skills/ultimate-design
```

Then invoke it in your agent:

```text
Use $ultimate-design to turn this report into a visual page. Create or update DESIGN.md if needed, keep the original request anchored, and verify the rendered output.
```

Claude Code uses slash commands for skills:

```text
/ultimate-design turn this report into a visual page. Create or update DESIGN.md if needed and verify the rendered output.
```

Pi Agent uses skill commands when enabled:

```text
/skill:ultimate-design turn this report into a visual page. Create or update DESIGN.md if needed and verify the rendered output.
```

See [integrations/README.md](integrations/README.md) for Codex, Claude Code, Pi Agent, package, symlink, project-scoped, and prompt-only integration options.

## Prompt Examples

```text
Use $ultimate-design to redesign this dense validation report as a visual web page for executives.
```

```text
Use $ultimate-design to create a 10-slide HTML PPT deck from this research memo. Make it board-room credible and run deck-level validation before delivery.
```

```text
Use $ultimate-design to audit this landing page. Find requirement drift, visual slop, copy issues, accessibility issues, and fix the high-severity problems.
```

## Validation

Run the static flow proof:

```bash
python3 skill/ultimate-design/scripts/flow_check.py skill/ultimate-design
```

Check that every OKF concept is indexed, linked, and reachable from an execution route:

```bash
npm run okf-graph-check
```

Verify cross-agent installation entrypoints:

```bash
npm run check-integrations
```

Validate a generated `DESIGN.md` contract:

```bash
python3 skill/ultimate-design/scripts/validate_design_contract.py path/to/DESIGN.md --strict-ultimate
python3 skill/ultimate-design/scripts/validate_okf_usage.py path/to/DESIGN.md
```

The second command rejects an active OKF concept unless the contract binds it to a concrete decision, artifact target, and verification hook.

Validate screenshotable HTML artifacts:

```bash
node skill/ultimate-design/scripts/validate_html_visual.mjs \
  --input path/to/artifact.html \
  --out ultimate-design-visual-check \
  --viewports desktop=1440x900,mobile=390x844 \
  --spacing 36
```

The bundled deterministic HTML validators are one optional implementation. They require a separately provisioned pinned runtime: Playwright `1.61.1` with Chromium Headless Shell revision `1228`. They resolve `ULTIMATE_DESIGN_PLAYWRIGHT_RUNTIME`, then `CODEX_PLAYWRIGHT_RUNTIME`, then `~/.codex/playwright-runtime`. The selected directory must expose `runtime.mjs` with `pinnedRuntime` metadata and `launchPinnedChromium()`.

Ultimate Design itself does not require this runtime or Codex. In another Agent environment, use that Agent's approved renderer, browser, screenshot, or accessibility capability and record its visible-review evidence and limits separately. The bundled validators never install a browser, create a project-local Playwright copy, or fall back to system Chrome. A missing compatible runtime blocks only that deterministic proof path; it never turns a visible review into a fresh machine-audit pass.

For monitored HTML proof runs, use the coupled gate so the artifact, contract, OKF usage, rendered layout, and applicable motion evidence fail together:

```bash
node skill/ultimate-design/scripts/run_html_proof.mjs \
  --html path/to/artifact.html \
  --design path/to/DESIGN.md \
  --require-okf-usage
```

## License

MIT. You can use, copy, modify, distribute, sublicense, and sell this project, including in commercial or closed-source products, as long as the MIT copyright and license notice stays with the software.

## Non-Affiliation

This project is not an official Google, OpenAI, Anthropic, Figma, or Codex product. OKF references are an implementation pattern for indexed knowledge in agent workflows.
