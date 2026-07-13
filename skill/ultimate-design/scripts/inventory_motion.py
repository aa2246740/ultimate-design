#!/usr/bin/env python3
"""Inventory motion implementation signals without turning them into findings."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


EXTENSIONS = {
    ".css", ".scss", ".sass", ".less", ".styl",
    ".html", ".htm", ".js", ".jsx", ".mjs", ".cjs",
    ".ts", ".tsx", ".vue", ".svelte",
}

IGNORED_DIRS = {
    ".git", ".next", ".nuxt", ".svelte-kit", ".turbo",
    "build", "coverage", "dist", "node_modules", "out", "vendor",
}

SIGNALS: list[tuple[str, re.Pattern[str]]] = [
    ("css-transition", re.compile(r"\btransition(?:-(?:property|duration|timing-function|delay))?\s*:", re.I)),
    ("css-animation", re.compile(r"\banimation(?:-(?:name|duration|timing-function|delay|iteration-count|fill-mode|play-state))?\s*:", re.I)),
    ("css-keyframes", re.compile(r"@(?:-webkit-)?keyframes\b", re.I)),
    ("reduced-motion", re.compile(r"prefers-reduced-motion|useReducedMotion\b", re.I)),
    ("waapi", re.compile(r"\.animate\s*\(")),
    ("gsap", re.compile(r"\bgsap(?:\.|/)|\bScrollTrigger\b", re.I)),
    ("motion-library", re.compile(r"(?:from\s+['\"](?:framer-motion|motion(?:/react)?)['\"]|<motion\.|\buseMotionValue\b|\buseAnimation\b)", re.I)),
    ("react-spring", re.compile(r"@react-spring|\buseSpring\b|\buseSprings\b", re.I)),
    ("gesture-input", re.compile(r"\b(?:pointer(?:down|move|up|cancel)|touch(?:start|move|end)|drag(?:start|end|over)?|swipe|pan(?:start|move|end)?)\b", re.I)),
    ("candidate-transition-all", re.compile(r"transition(?:-property)?\s*:[^;\n]*\ball\b", re.I)),
    ("candidate-ease-in", re.compile(r"\bease-in\b", re.I)),
    ("candidate-scale-zero", re.compile(r"scale(?:3d)?\(\s*0(?:\s*[,)]|\s*$)", re.I)),
    ("candidate-layout-property", re.compile(r"(?:transition|animation|animate)[^;\n]{0,180}\b(?:width|height|margin|padding|top|left|right|bottom)\b", re.I)),
    ("candidate-filter", re.compile(r"(?:transition|animation|animate)[^;\n]{0,180}\b(?:filter|backdrop-filter)\b", re.I)),
]

STACK_BY_SIGNAL = {
    "css-transition": "CSS transitions",
    "css-animation": "CSS animations",
    "css-keyframes": "CSS animations",
    "waapi": "Web Animations API",
    "gsap": "GSAP",
    "motion-library": "Motion / Framer Motion",
    "react-spring": "React Spring",
}


def source_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        if any(part in IGNORED_DIRS for part in path.relative_to(root).parts[:-1]):
            continue
        yield path


def excerpt(line: str, limit: int = 220) -> str:
    compact = " ".join(line.strip().split())
    return compact if len(compact) <= limit else compact[: limit - 3] + "..."


def inventory(root: Path, max_hits: int) -> dict[str, object]:
    counts: Counter[str] = Counter()
    hits: list[dict[str, object]] = []
    truncated: set[str] = set()
    stacks: set[str] = set()
    files_scanned = 0

    for path in source_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        files_scanned += 1
        rel = path.relative_to(root).as_posix()
        for line_number, line in enumerate(text.splitlines(), start=1):
            for name, pattern in SIGNALS:
                if not pattern.search(line):
                    continue
                counts[name] += 1
                stack = STACK_BY_SIGNAL.get(name)
                if stack:
                    stacks.add(stack)
                if counts[name] <= max_hits:
                    hits.append({
                        "signal": name,
                        "file": rel,
                        "line": line_number,
                        "excerpt": excerpt(line),
                    })
                else:
                    truncated.add(name)

    hits.sort(key=lambda item: (str(item["file"]), int(item["line"]), str(item["signal"])))
    return {
        "schemaVersion": "ultimate-design.motion-surface.v1",
        "root": root.name or ".",
        "filesScanned": files_scanned,
        "stackHints": sorted(stacks),
        "summary": dict(sorted(counts.items())),
        "truncatedSignals": sorted(truncated),
        "note": "Static signals are inventory only. Vet code context and rendered behavior before assigning findings or severity.",
        "hits": hits,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="Project root to scan")
    parser.add_argument("--out", help="Optional JSON output path; stdout is always available")
    parser.add_argument("--max-hits", type=int, default=200, help="Maximum stored hits per signal")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"Not a directory: {root}")
    if args.max_hits < 1:
        parser.error("--max-hits must be at least 1")

    report = inventory(root, args.max_hits)
    payload = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        out = Path(args.out).expanduser().resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
