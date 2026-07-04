# Agent Integrations

Ultimate Design is packaged as an Agent Skill: a folder named `ultimate-design` with a required `SKILL.md`, optional `references/`, optional `scripts/`, and optional UI metadata. The same skill directory can be installed into Codex, Claude Code, Pi Agent, and any agent that implements the Agent Skills convention.

## Quick Installer

From the repository root:

```bash
node scripts/install-agent-skill.mjs --target codex
node scripts/install-agent-skill.mjs --target claude-code
node scripts/install-agent-skill.mjs --target pi-agent
```

Check all common project-level entrypoints without touching global agent folders:

```bash
npm run check-integrations
```

Use `--link` during development so changes in this repository are picked up by the target agent:

```bash
node scripts/install-agent-skill.mjs --target codex --link
node scripts/install-agent-skill.mjs --target claude-code --scope project --link
node scripts/install-agent-skill.mjs --target pi-agent --scope shared --link
```

## Codex

Codex skills are directories with `SKILL.md` plus optional `scripts/`, `references/`, `assets/`, and `agents/openai.yaml`. Codex can invoke skills explicitly with `$skill-name` or implicitly from the `description`.

Install for your user:

```bash
mkdir -p ~/.agents/skills
cp -R skill/ultimate-design ~/.agents/skills/ultimate-design
```

Install for one repository:

```bash
mkdir -p .agents/skills
cp -R skill/ultimate-design .agents/skills/ultimate-design
```

Legacy/local Codex setups may also scan `~/.codex/skills`. Use this only if your Codex skill list shows that directory:

```bash
mkdir -p ~/.codex/skills
cp -R skill/ultimate-design ~/.codex/skills/ultimate-design
```

Invoke:

```text
$ultimate-design redesign this report as a visual executive page. Create or update DESIGN.md and verify rendered output.
```

Useful checks:

```bash
python3 skill/ultimate-design/scripts/flow_check.py skill/ultimate-design
python3 skill/ultimate-design/scripts/validate_design_contract.py DESIGN.md --strict-ultimate
node skill/ultimate-design/scripts/validate_html_visual.mjs --input artifact.html
```

## Claude Code

Claude Code loads personal skills from `~/.claude/skills/<skill-name>/SKILL.md` and project skills from `.claude/skills/<skill-name>/SKILL.md`. The directory name becomes the slash command, so this skill is invoked as `/ultimate-design`.

Install for your user:

```bash
mkdir -p ~/.claude/skills
cp -R skill/ultimate-design ~/.claude/skills/ultimate-design
```

Install for one repository:

```bash
mkdir -p .claude/skills
cp -R skill/ultimate-design .claude/skills/ultimate-design
```

Invoke:

```text
/ultimate-design create a 9-image Xiaohongshu carousel that explains this product, then render and inspect every image.
```

Claude Code can follow symlinked skill folders, which is useful for local development:

```bash
mkdir -p ~/.claude/skills
ln -s "$PWD/skill/ultimate-design" ~/.claude/skills/ultimate-design
```

## Pi Agent

Pi implements the Agent Skills standard and loads skills from several places:

- Global: `~/.pi/agent/skills/`
- Shared global: `~/.agents/skills/`
- Project: `.pi/skills/`
- Project/shared: `.agents/skills/` in the current working directory and ancestors
- Package: `skills/` directories or `pi.skills` entries in `package.json`
- Runtime: repeated `--skill <path>` flags

Install for your user:

```bash
mkdir -p ~/.pi/agent/skills
cp -R skill/ultimate-design ~/.pi/agent/skills/ultimate-design
```

Install into the shared Agent Skills folder used by Pi and Codex:

```bash
mkdir -p ~/.agents/skills
cp -R skill/ultimate-design ~/.agents/skills/ultimate-design
```

Install for one project:

```bash
mkdir -p .pi/skills
cp -R skill/ultimate-design .pi/skills/ultimate-design
```

Invoke:

```text
/skill:ultimate-design audit this landing page for request drift, visual hierarchy, content clarity, and rendered verification.
```

For one-off use without installing:

```bash
pi --skill ./skill/ultimate-design
```

This package also declares:

```json
{
  "pi": {
    "skills": ["skill/ultimate-design"]
  }
}
```

That lets Pi package installs discover the skill when the package is installed through Pi or npm-based workflows.

## Generic Agent Skills

For any Agent Skills-compatible harness:

1. Copy `skill/ultimate-design/` to that harness's skills directory.
2. Ensure the final path is `ultimate-design/SKILL.md`.
3. Verify the harness supports relative files under `references/` and executable helper files under `scripts/`.
4. Invoke using the harness's explicit skill syntax, or ask for "Ultimate Design" by name.

Prompt fallback when a harness has no native skill loader:

```text
Read skill/ultimate-design/SKILL.md. Follow its operating loop for this design request. Load only the referenced branch files that apply. Use Request Anchor, DESIGN.md when persistence matters, critique/repair, and rendered verification before final delivery.
```

## Sources

- Codex Agent Skills documentation: https://developers.openai.com/codex/skills
- Claude Code Skills documentation: https://code.claude.com/docs/en/skills
- Pi Agent Skills documentation: https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md
- Pi package catalog: https://pi.dev/packages
