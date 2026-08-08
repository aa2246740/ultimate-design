# Hallmark audit — pinned main `13ac0ec` (2026-08-08)

**Subject.** Deep primary-source audit of [nutlope/hallmark](https://github.com/nutlope/hallmark) at commit [`13ac0ec7e148655948100b6396439e481361d690`](https://github.com/nutlope/hallmark/commit/13ac0ec7e148655948100b6396439e481361d690) (*Merge pull request #57 from Nutlope/add-grid-theme-v2*, 2026-08-06).
**Workspace.** Ultimate Design worktree `hallmark-distillation`. The **research phase** was research-only with no product/skill edits; later implementation phases may edit skill files in this worktree under separate tasks.
**Method.** Disposable clone + local `npm pack`; GitHub API for issues/PRs/commits; npm registry probe; official site fetch `https://www.usehallmark.com`.
**Claim source.** Task checklist encodes the user-supplied ChatGPT conclusion (full ChatGPT transcript was **not** recovered as a standalone file in this worktree; claims are validated dimension-by-dimension as listed by the coordinator).
**Classification key.** Confirmed · Partly confirmed · Refuted · Outdated · Unverifiable.
**Separation rule.** **Fact** = directly observed in primary sources. **Inference** = judgment / implication (labeled).

---

## 0. Executive summary

Hallmark at `13ac0ec` is a **prompt-skill monorepo** (not an executable design engine): one default Design flow + three verbs (`audit` / `redesign` / `study`), a large reference tree, agent-enforced diversification via `.hallmark/log.json`, opt-in `design.md` lock, and a **self-scored** 58-gate slop test (including lettered gate `38a`). Macrostructure/component/genre **counts match the skill’s self-description** (21 / 50 / 4). Catalog themes are **21 named** in `SKILL.md`, tokens CSS, and runtime `THEMES` in `site/js/main.js` (21 keys; ordinal becomes `01/21`). Only **5 themes have long-form `references/themes/*.md` specs**. Static marketing copy still embeds stale **“20 themes” / “57 gates”** strings in HTML/JS fixtures—**source-text drift**, not a missing runtime theme.

The famous **57 vs 58 gate mismatch still exists**, but not exactly as Issue #37 states: skill-internal count is intentionally **58 = gates 1–57 + `38a`** ([PR #17](https://github.com/nutlope/hallmark/pull/17)); **README + site footer still say 57**; Issue [#37](https://github.com/nutlope/hallmark/issues/37) remains **open**. Gate 57’s catalog-name allowlist is **stale (20 names, omits Grid)** after PR #57.

**npm name `hallmark` is a different product** (vweevers markdown linter, GPL-3.0, latest 5.0.2). Nutlope Hallmark is distributed primarily via `npx skills add nutlope/hallmark` / git; local `npm pack` of repo `package.json` ships **skills (+ README/LICENSE) only** — **not** `site/` or `docs/` — while skill docs **cross-link** into those directories and `scripts.serve` targets `site`.

Gallery / `_tests` are **hand-curated generation fixtures with documented manual course correction**, not automated evals. Scoring is **prompt-level self-critique**, not machine-scored CI. ROADMAP lists **live preview as Later (MCP)** — not shipped. License **MIT** (repo). Issue [#50](https://github.com/nutlope/hallmark/issues/50) (token footprint / split skills) remains **open**; skill tree ≈ **102k words / ~690 KB markdown**.

---

## 1. Observed inventory (raw counts & commands)

```text
# clone pin
git clone https://github.com/nutlope/hallmark.git
git checkout 13ac0ec7e148655948100b6396439e481361d690
# HEAD = 13ac0ec Merge pull request #57 from Nutlope/add-grid-theme-v2

# grammar asset counts
ls skills/hallmark/references/macrostructures/*.md | wc -l   # 21
ls skills/hallmark/references/components/*.md | wc -l        # 50
ls skills/hallmark/references/genres/*.md | wc -l            # 4
ls skills/hallmark/references/themes/*.md | wc -l            # 5  (carnival cobalt grid hum lumen)
grep -oE 'data-theme="[^"]+"' site/css/tokens.css | sort -u | wc -l
# 21 real themes + placeholder "..."

# slop gates
python3: re.findall(r'(?m)^(\d+[a-z]?)\.\s', slop-test.md)
# ['1'..'38','38a','39'..'57'] → count 58 unique

# word / byte footprint (skills only)
find skills -name '*.md' | wc -l     # 107
find skills -name '*.md' -exec wc -w {} + | tail -1
# 101786 total words
# SKILL.md 9804; study.md 6613; slop-test.md 4792; anti-patterns.md 3956
find skills -name '*.md' -exec cat {} + | wc -c
# 689673 bytes ≈ 0.66 MiB text; ~132k tokens (words×1.3) or ~172k (chars/4)

# npm pack (local package.json version 1.1.0)
npm pack --dry-run / pack
# total files: 110; package size ~260 kB; unpacked ~698 kB
# tarball contains package/{package.json,README.md,LICENSE,skills/**}
# site/ count in tarball: 0

# registry name collision
curl registry.npmjs.org/hallmark → latest 5.0.2, license GPL-3.0, different package
curl registry.npmjs.org/@nutlope/hallmark → Not found
```

**Pinned commit message:** merge of Grid theme v2 (21st catalog theme).
**No GitHub Releases** published as of audit fetch.

---

## 2. Claim-by-claim validation

| # | Claim (ChatGPT-conclusion dimension) | Classification | Primary evidence | Facts vs inference | Implication for Ultimate Design |
|---|--------------------------------------|----------------|------------------|--------------------|----------------------------------|
| C1 | **Workflow = default design + audit/redesign/study verbs; structural variety over skin swaps** | **Confirmed** | [`SKILL.md` L19–28, L145–476](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/SKILL.md#L19-L28); [README four verbs](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/README.md#L17-L24) | **Fact:** table of invocations + Design flow steps 0–7. **Inference:** quality depends on host model obedience. | Absorb **verb split** (build / score-only / restructure / extract DNA) and **structure-first** selection; do not absorb Hallmark brand voice. |
| C2 | **Design grammar counts: ~21 macros, ~21 themes, ~50 components, 4 genres** | **Partly confirmed** | Macros 21 files; components 50 files; genres 4; themes **21 names** in SKILL + 21 `data-theme` blocks in tokens + **21 keys** in `site/js/main.js` `THEMES` (`totalThemes = Object.keys(THEMES).length`, ordinal ``${n} / ${totalThemes}`` → **01/21** at runtime). **Only 5** long-form `references/themes/*.md`. Static HTML/fixture copy still says **“20 themes”** / ordinal markup defaults like `01 / 20`. | **Fact:** runtime catalog is 21. **Fact:** static source strings lag. **Inference:** do not equate static site copy with live theme count. | Trust **index + per-item files** pattern; do **not** treat “21 themes” as equal documentation depth; separate **source-text drift** from runtime. |
| C3 | **`study` extracts DNA (not pixels) with refusal / safety** | **Confirmed** | [`study.md` refuse lists, Remote URL safety, attestation for design.md emission](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/references/study.md); SKILL L490–552 | **Fact:** marketplace refuse, prompt-injection ignore, URL attestation (a/b/c). **Inference:** enforcement is agent-side only. | Absorb **extraction-vs-clone** + **URL untrusted-data** + **provenance block**; skip Hallmark-specific refuse copy. |
| C4 | **Exploratory-then-lock lifecycle via optional `design.md`** | **Confirmed** | [`design-md.md` opt-in triggers](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/references/design-md.md); SKILL Step 6 “default verb does NOT auto-emit”; preflight defers to existing `design.md` | **Fact:** lock is phrase-gated; diversification **inverts** when locked. | Aligns with UD `DESIGN.md` contract idea — absorb **opt-in lock + export section refresh**, not Hallmark section schema verbatim. |
| C5 | **Anti-slop / slop-test gates; claimed 57/58 mismatch still exists** | **Partly confirmed** (mismatch **still real**; issue text **partly outdated**) | Gates: **58 labels** `1–57` + `38a` ([slop-test.md L1, L98–100, L186](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/references/slop-test.md)); SKILL preview `58 / 58 ✓`; README L13 “fifty-seven”; site footer `57` ([site/index.html ~L1116](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/site/index.html)); [Issue #37 open](https://github.com/nutlope/hallmark/issues/37); [PR #17](https://github.com/nutlope/hallmark/pull/17) intentionally counted `38a` as 58th | **Fact:** internal skill docs say 58; marketing says 57; issue open. **Fact:** “only 57 gates exist” is **false if `38a` counts**. **Inference:** agents can still emit inconsistent scores. | Absorb **checklist gates + pre-emit axes**; do **not** hard-code “57” or “58” as a product law. Prefer named gates over numeric total. |
| C6 | **Catalog / rotation memory (`.hallmark/log.json`, stamps)** | **Confirmed** | SKILL Steps 2 / 2.5 / 6; example logs under `site/examples/*/.hallmark/log.json` | **Fact:** schema + trim-to-20 + axis diversification. **Inference:** memory is advisory to the LLM, not a enforced runtime. | Absorb **session/project memory for variety**; keep UD brand consistency rules when multi-page locked. |
| C7 | **Arbitrary aesthetic rules (numeric laws: 5% accent, 2+1 fonts, 4pt space, no italic headers, etc.)** | **Partly confirmed** | Gates 23, 37–38a, 24; typography 2+1; OKLCH-first | **Fact:** rules are written as hard gates. **Inference:** many are **taste-as-law** (5% accent, ban Inter, etc.) not universal design science. Gallery **violates italic-header ban** (see C12). | Absorb **mechanisms** (token discipline, contrast checks, state coverage). **Do not** import unsupported numeric ceilings as UD doctrine. |
| C8 | **Official gallery / generation-tests provenance; manual course correction** | **Confirmed** | [`site/_tests/README.md`](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/site/_tests/README.md) documents v0.6 generation + **Tracejam manual fixes** + re-gen under rotation; `verbs/` worked examples with notes; gallery examples under `site/examples/` | **Fact:** fixtures are curated HTML with briefs/notes; changelog-style course correction. **Inference:** not statistically representative model eval. | Treat as **worked examples**, not regression suite. UD should keep separate proof-runs with machine checks where possible. |
| C9 | **Executable tests/evals and self-scoring** | **Partly confirmed** | Pre-emit critique 6 axes 1–5 ([slop-test.md L9–24](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/references/slop-test.md#L9-L24)); **no** `test` script in package.json; `_tests` are static HTML | **Fact:** scoring is **agent self-report**. **Fact:** no automated gate runner in repo. | Absorb **self-critique axes** as optional human/LLM rubric; pair with UD machine verification where available. |
| C10 | **`package.json` scripts/files & npm tarball integrity / cross-dir refs** | **Confirmed (integrity gap)** | [`package.json`](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/package.json): `"files":["skills"]`, script `serve` → `site`; local pack **110 files, no `site/`**; skill links to [`../../site/css/tokens.css`](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/SKILL.md#L282) and `docs/*`; **npm `hallmark` ≠ this project** | **Fact:** published-name collision; skill-only tarball; broken relative deps for consumers without full clone. | When distilling, **package what the skill actually needs** (or inline axis tables). Never assume `npm i hallmark` installs Nutlope skill. |
| C11 | **ROADMAP live-preview / multi-page state** | **Partly confirmed** | Live preview: [ROADMAP.md Later](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/ROADMAP.md#L39) — **not shipped**. Multi-page coherence: ROADMAP still lists it under **Next** as future, yet [`verbs/redesign.md` § Multi-page flow](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/references/verbs/redesign.md) already implements a **design.md-first locked multi-page redesign** with inverted diversification. | **Fact:** live preview unshipped. **Fact:** multi-page locked-system flow is **shipped in skill text** while ROADMAP still frames multi-page coherence as upcoming — **documentation drift**, not pure absence. | Do not treat live preview as present. For multi-page, read the **verb protocol** as source of truth over ROADMAP marketing. |
| C12 | **Contradictions: browser chrome, italics, font-count, OKLCH/hex** | **Confirmed (internal contradictions)** | Gate **47** bans re-drawn chrome ([slop-test L147–152](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/references/slop-test.md#L147-L152)); **H8** teaches `mock__chrome` traffic-light dots ([h8 component](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/references/components/h8-mockup-split-browser-framed.md)); gate **38a** bans italic headers; gallery/tests use italic in heroes/section titles (`tally`, `foundry`, `cohort`, `bananastudio`, …); gate 48 bans mid-render hex/oklch; examples mostly token/OKLCH with rare `#000` | **Fact:** cookbook vs gate conflict on chrome. **Fact:** showcase pages predate or ignore italic ban. **Inference:** “law” is unevenly applied historically. | Prefer **one consistent rule set**; if absorbing chrome policy, drop H8-as-default. Italic: allow body emphasis only if UD agrees. |
| C13 | **Issues #37 and #50** | **Confirmed** | [#37](https://github.com/nutlope/hallmark/issues/37) open (gate count docs); [#50](https://github.com/nutlope/hallmark/issues/50) open (skill too large / split verbs) — 15 comments, many low-signal; body argues token inefficiency | **Fact:** both open at audit time. **Inference:** #50’s “~1MB skill” is order-of-magnitude OK for skill tree on disk (~0.9MB `skills/`), not precise. | Validates UD interest in **lazy load / specialist split** (already a Hallmark pattern: index-then-pick). |
| C14 | **Word/token footprint is large** | **Confirmed** | ~**101,786 words** / **689,673 bytes** across 107 skill markdown files; SKILL alone ~9.8k words | **Fact:** measured at pin. Token estimates model-dependent. | Distill to **mechanisms + short gates**; do not port entire reference corpus. |
| C15 | **License MIT; recent changes = Grid theme** | **Confirmed** | [LICENSE](https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/LICENSE) MIT © 2026; HEAD PR #57 Grid; package.json `"license":"MIT"` / `"version":"1.1.0"` | **Fact:** MIT for this repo. **Fact:** npm `hallmark@*` GPL is unrelated. | Safe to read/learn under MIT; branding/trademark still not “absorb”. |

---

## 3. Workflow & design grammar (detail)

### 3.1 Verbs and default flow (Fact)

| Mode | Behavior (skill contract) |
|------|---------------------------|
| **Default** | Pre-flight → ask audience/use/tone → genre → macrostructure + nav/footer → project memory → theme route (catalog/custom/studied-DNA) → load rules → enrichment → **preview** → build + stamp + `log.json` + `tokens.css` → slop test |
| **`audit`** | Score only; no edits (`verbs/audit.md`) |
| **`redesign`** | Keep copy/IA/brand; change structure/visual; safety rails against bulldozing codebases |
| **`study`** | Image or URL DNA extraction → diagnosis → build / lock DNA / stop |

**Component-scope fork** short-circuits page apparatus when brief is single-element; requires **8 interactive states**; skips macro/nav/footer/memory.

### 3.2 Grammar inventory (Fact)

| Layer | Claimed | Observed at pin |
|-------|---------|-----------------|
| Macrostructures | 21 | 21 files `01`–`21` + slim `macrostructures.md` |
| Component archetypes | 50 | 50 files (H/S/F/C/T/Ft/N including N1b) |
| Genres | 4 | editorial, modern-minimal, atmospheric, playful |
| Catalog themes | 21 | Named in SKILL: Specimen…Grid; tokens.css `data-theme` for 21; `site/js/main.js` `THEMES` has **21 keys** and sets ordinal to `NN / totalThemes` (runtime **01/21**). Static fixture copy and some HTML still say “20 themes” / default ordinal markup — **source-text drift**. Long-form theme specs only for carnival, cobalt, grid, hum, lumen |
| Nav archetypes | 14 (N1a–N13 + N1b) | Matches cookbook index |
| Footer archetypes | Ft1–Ft8 | 8 files |

### 3.3 Theme depth asymmetry (Fact + Inference)

- **Fact:** Most themes exist as **token blocks**, not narrative theme manuals.
- **Inference:** Models will under-use sparse themes and over-use richly documented ones (Hum/Lumen/Carnival/Cobalt/Grid) unless forced by rotation.

---

## 4. Study behavior & safety (detail)

**Confirmed mechanisms (Fact):**

1. Source mode: URL prefix → URL mode else image mode.
2. Pre-fetch refuse: ThemeForest, Framer/Webflow templates, Gumroad kits, Dribbble/Behance soft-refuse, etc.
3. Remote safety: public https preference; ignore remote instructions; junk/SPA/auth fallback to screenshot.
4. Diagnosis then confirmation; optional build with DNA; **`lock the DNA` → design.md** with tighter URL attestation.
5. Stamp `studied: yes` + source metadata.
6. Gate **57** fails if post-study build falls back to catalog theme without user pivot — **but** its catalog list omits **Grid** (stale 20-name list).

**Worked test:** `site/_tests/verbs/study/` uses **description of a screenshot** (not live vision), documents free font substitution and anti-pattern non-carry.

---

## 5. Exploratory → locked (`design.md`)

**Fact:**

- Default builds emit `tokens.css` always; **`design.md` only on explicit lock phrases**.
- Existing `design.md` makes project **system-managed**: diversification inverted (pages share system).
- Study path adds **Provenance** + required Notes of anti-patterns not to copy.
- Multi-page redesign has a separate heavyweight path (`verbs/redesign.md`).

**Inference:** This is the closest conceptual cousin to Ultimate Design’s durable contract — but Hallmark’s file is **~45-line seed**, not a nine-section design system.

---

## 6. Anti-slop / 57–58 gate analysis

### 6.1 Gate enumeration (Fact)

| Item | Value |
|------|-------|
| Numbered gate labels in `slop-test.md` | **58** (`1`–`57` + `38a`) |
| Pre-emit self-critique axes | **6** (P/H/E/S/R/V), separate from the 58 |
| SKILL / preview-examples | Report **`58 / 58 ✓`** |
| README | **fifty-seven** / **57** |
| `site/index.html` footer | **`57` slop-test gates** |
| usehallmark.com / site sources (fetched 2026-08-08) | **Raw/static HTML and fixture copy** still embed **“20 themes”** (and default ordinal markup like `01 / 20`). **Rendered runtime** is driven by `site/js/main.js`: `Object.keys(THEMES).length === 21` and the ordinal is rewritten to **`01/21`…`21/21`** after JS runs. Do not equate static HTML “20” with live theme count. |
| Issue #37 | **Open** since 2026-07-21 |
| PR #17 (2026-06-04) | Explicitly reconciled skill docs to **58** by counting `38a` |

**Classification of ChatGPT “57/58 mismatch still exists”:** **Partly confirmed** — marketing/README vs skill mismatch **yes**; “only 57 gates exist” **refuted** if `38a` is a gate (PR #17 intent).

### 6.2 Self-scoring (Fact)

- Agent scores 1–5 on six axes; `<3` → revision.
- Stamp: `/* Hallmark · pre-emit critique: P5 H4 … */`.
- No CI harness validates stamps or gate answers.

---

## 7. Catalog rotation memory

**Fact:**

- `.hallmark/log.json` array, newest first, last 3–5 influence picks, trim 20.
- Macrostructure stamp in CSS is second channel.
- Theme axes: paper-band / display-style / accent-hue.
- Custom records `theme: custom` + `theme_axes` + optional `vibe`.
- Component-scope **does not** write memory.
- Examples show real logs (wayfare, hyperlane, najm, bananastudio) with slightly evolving schema (nav/footer fields appear in some entries).

**Inference:** Schema drift across examples is acceptable for LLM memory but would fail a strict schema validator.

---

## 8. Arbitrary aesthetic rules (selected)

| Rule | Location | Status as “law” | Gallery compliance |
|------|----------|-----------------|--------------------|
| No Inter/Roboto/… display | Gate 1 | Hard ban list | Not systematically verified here |
| No purple-blue gradient text | Gate 2 | Hard | — |
| Accent ≤ ~5% viewport | Gate 23 | Numeric law | Genre overrides atmospheric |
| 2+1 font families | Gate 37–38 | Hard ceiling 3 | — |
| No italic headers | Gate 38a + discipline #6 | Hard | **Violated** in multiple official examples/tests |
| OKLCH tokens; no mid-render hex | Gate 48 + Build step | Hard | Mostly OKLCH; rare `#000` |
| No re-drawn chrome | Gate 47 | Hard | **Contradicted** by H8 cookbook |
| 4pt spacing scale | Gate 24 | Hard | — |
| 8 interaction states (components) | Component-scope | Hard | Demo wrapper prescribed |

**Distillation stance:** treat ban lists as **anti-default heuristics**, not physics.

---

## 9. Gallery / generation-test provenance

**Fact (`site/_tests/README.md`):**

- Originally framed as **eight** landing pages from unprompted skill runs; versioned notes for **v0.6.0**.
- Documents **manual defect fixes** (Tracejam overflow, nav centering, highlighter band, chrome aria-hidden).
- Re-generation under pre-flight + rotation + preview.
- Additional pages `09–13`, `custom/`, `all-themes.html` beyond the original eight.
- Verb fixtures under `_tests/verbs/` with input/output/notes.
- Live marketing gallery: `site/examples/*` + screenshots in `docs/screenshots/`.

**Inference:** “Tests” means **design QA corpus**, not unit/integration tests.

---

## 10. Package / registry / cross-directory integrity

| Check | Result |
|-------|--------|
| Repo `package.json` name/version/license | `hallmark` / `1.1.0` / MIT |
| `files` | `["skills"]` only |
| `scripts` | only `serve` → `python3 -m http.server --directory site 4173` |
| Local `npm pack` | 110 files; **skills + README + LICENSE**; **no site/docs** |
| Skill references to `site/css/tokens.css`, `site/_tests/*`, `docs/*` | Present — **broken for skills-only install** |
| npm registry `hallmark` | **Different project** (markdown lint CLI, GPL-3.0, 5.0.2) |
| `@nutlope/hallmark` | Not found |
| Install path in README | `npx skills add nutlope/hallmark` |

**Claim “npm tarball integrity including cross-directory references”:** **Confirmed problem** for any consumer relying on npm pack contents alone.

---

## 11. ROADMAP vs shipped skill (live preview and multi-page)

**Live preview (Fact):** Under **Later** — MCP that watches files, screenshots, feeds slop test — **not implemented** at pin.

**Multi-page coherence (Fact + classification):** ROADMAP **Next** still frames multi-page brand/page-voice coherence as future work. Independently, `skills/hallmark/references/verbs/redesign.md` already ships a **multi-page flow**: produce root `design.md`, redesign each page under the locked system, **invert** diversification (consistency wins), amend `design.md` rather than local overrides. Treat the ROADMAP bullet as **documentation drift** relative to the verb, not as proof the multi-page lock protocol is missing.

**Other Now/Next items** (Nanobanana hook, brand-first flow, theme-aware motion, `hallmark variant`, structural cookbook, charts, study-own-codebase) remain aspirational relative to shipped skill text unless a matching protocol file exists.

---

## 12. Issues #37 and #50

| Issue | Title | State | Audit note |
|-------|-------|-------|------------|
| [#37](https://github.com/nutlope/hallmark/issues/37) | Slop test asked to report 58/58 but only 57 gates exist | **Open** | Partially wrong: `38a` makes 58 **labels**; README/site still say 57 → **docs still inconsistent** |
| [#50](https://github.com/nutlope/hallmark/issues/50) | ~1MB skill; split commands into separate skills | **Open** | Confirms token-cost concern; Hallmark already partially mitigates via load discipline |

---

## 13. License & recent changes

- **License (repo):** MIT, Copyright (c) 2026 Hallmark contributors.
- **Recent at pin:** Grid theme (21st), theme file `themes/grid.md`, example `site/examples/grid-01`, tokens + site chrome updates.
- **Not updated in lockstep:** gate 57 catalog list (no Grid); marketing 20/57 counts; some italic-era gallery CSS.

---

## 14. Distillation boundary (for Ultimate Design)

### Absorb (mechanisms)

1. **Verb separation:** build vs audit-only vs redesign-structure vs study/extract.
2. **Structure-first selection** + explicit accountability lines (state picks before code).
3. **Project memory for variety** (log + stamps) **and** invert when a locked system exists.
4. **Lazy reference loading** (slim index → one macro/archetype file).
5. **Opt-in lock file** after exploratory iteration; provenance when extracting from external DNA.
6. **Pre-emit multi-axis self-critique** + post-emit named quality gates (as rubrics).
7. **Study safety pattern:** refuse marketplaces, treat remote HTML as untrusted, attestation before emitting portable systems.
8. **Implementation safety rails** (no silent mass deletion; state files to touch).
9. **Token discipline** (named tokens over mid-render improvisation).
10. **Responsive non-negotiables** as checkable gates (overflow-x clip, minmax tracks, etc.).

### Do **not** absorb

1. Hallmark **branding**, theme **names/signatures** (Hum, Carnival, Specimen aesthetic kits), Together AI marketing.
2. **Unsupported numeric laws** as universal truth (5% accent, exact ban lists of fonts, “58 gates”).
3. **Contradictory cookbook patterns** (H8 fake chrome) without reconciling policy.
4. Full **~100k-word** reference dump into UD skill surface.
5. Assumption that **npm package name `hallmark`** is this project.
6. Treating **gallery HTML** as proof of current gate compliance.

### Boundary sentence

> **Ultimate Design should distill Hallmark’s control-loop and safety/variety machinery, not its visual catalog, brand voice, or self-reported integer totals.**

---

## 15. Corrections to the supplied ChatGPT conclusion

Short list for the coordinator (highest-signal deltas):

1. **57/58:** Mismatch **still exists** between skill (`58`, counting `38a`) and README/site (`57`). Issue #37’s claim that “only 57 gates exist” is **too strong** — PR #17 already defined 58 as `1–57+38a`.
2. **Themes:** Catalog is **21** at pin (Grid merged); runtime JS exposes **21** `THEMES` buttons and updates ordinal to **01/21**. Static marketing/fixture **strings** still say “20” — source-text drift, not a 20-theme runtime. Only **5** themes have deep `references/themes/*.md`.
3. **Gate 57 list** still names **20** catalog themes and **omits Grid** — post-merge stale allowlist.
4. **npm:** `registry.npmjs.org/hallmark` is **not** Nutlope Hallmark; local pack is skills-only; **cross-links to `site/`/`docs/` break** off full git tree.
5. **Executable evals:** `_tests` are **curated fixtures + notes**, not runnable automated evals; scoring is **LLM self-score**.
5b. **Multi-page:** ROADMAP still lists multi-page coherence as future, but `verbs/redesign.md` already implements multi-page locked `design.md` flow — classify as **docs drift**, not purely unshipped.
6. **Live preview:** ROADMAP **Later** only — not a present feature.
7. **Contradictions are real:** H8 browser chrome vs gate 47; italic headers in official examples vs gate 38a.
8. **Word footprint:** ~**102k words** skill markdown (~0.66–0.95 MB skill tree) — large, consistent with #50 concern; “1MB” is approximate.
9. **License:** Repo **MIT**; do not confuse with npm hallmark GPL linter.
10. **Gallery provenance:** Official examples include **documented manual course correction** (not pure unedited model dumps).

---

## 16. Permalink index (immutable)

| Artifact | URL |
|----------|-----|
| Pin commit | https://github.com/nutlope/hallmark/commit/13ac0ec7e148655948100b6396439e481361d690 |
| SKILL.md | https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/SKILL.md |
| slop-test.md | https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/references/slop-test.md |
| study.md | https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/references/study.md |
| design-md.md | https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/skills/hallmark/references/design-md.md |
| package.json | https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/package.json |
| ROADMAP.md | https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/ROADMAP.md |
| LICENSE | https://github.com/nutlope/hallmark/blob/13ac0ec7e148655948100b6396439e481361d690/LICENSE |
| Issue #37 | https://github.com/nutlope/hallmark/issues/37 |
| Issue #50 | https://github.com/nutlope/hallmark/issues/50 |
| PR #17 (count reconcile) | https://github.com/nutlope/hallmark/pull/17 |
| PR #57 (Grid theme) | https://github.com/nutlope/hallmark/pull/57 |
| Official site | https://www.usehallmark.com |
| npm name collision | https://www.npmjs.com/package/hallmark (unrelated linter) |

---

## 17. What was not done (scope)

- At the research phase no edits to Ultimate Design skill/product files.
- No push/publish/merge/version bump.
- Frozen `github-showcase` worktree untouched.
- Did not re-run live model generations; relied on repo fixtures + docs.
- Full original ChatGPT essay text not found on disk; dimensions taken from coordinator task enumeration.

---

*End of research report. Local clone path used for inspection: disposable `/tmp/hallmark-audit-*/hallmark` (not committed).*
