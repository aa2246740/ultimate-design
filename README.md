# Ultimate Design

OKF-based design skill for contract-driven AI design.

Official site: https://aa2246740.github.io/ultimate-design/

Ultimate Design is an Agent Skill for Codex, Claude Code, Pi Agent, and other Agent Skills-compatible harnesses. It turns vague design requests into governed design work: a brief, a `DESIGN.md` contract when persistence matters, routed OKF knowledge, a concrete artifact, critique/repair, rendered verification, and reusable design memory for the next agent.

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

Install into a common local agent with the helper script:

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

Verify cross-agent installation entrypoints:

```bash
npm run check-integrations
```

Validate a generated `DESIGN.md` contract:

```bash
python3 skill/ultimate-design/scripts/validate_design_contract.py path/to/DESIGN.md --strict-ultimate
```

Validate screenshotable HTML artifacts:

```bash
node skill/ultimate-design/scripts/validate_html_visual.mjs \
  --input path/to/artifact.html \
  --out ultimate-design-visual-check \
  --viewports desktop=1440x900,mobile=390x844 \
  --spacing 36
```

The visual validator uses Playwright when available. Set `PLAYWRIGHT_MODULE` or install `playwright` in the project if your runtime does not provide it.

## License

MIT. You can use, copy, modify, distribute, sublicense, and sell this project, including in commercial or closed-source products, as long as the MIT copyright and license notice stays with the software.

## Non-Affiliation

This project is not an official Google, OpenAI, Anthropic, Figma, or Codex product. OKF references are an implementation pattern for indexed knowledge in agent workflows.
