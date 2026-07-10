#!/usr/bin/env python3
"""Validate OKF index integrity and report runtime routing reachability."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
EXPECTED_INDEX_ONLY = {
    "governance/okf-taxonomy-digestion-map.md",
    "governance/research-coverage-map.md",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def local_links(path: Path) -> list[str]:
    links: list[str] = []
    for raw in LINK_RE.findall(read(path)):
        href = raw.strip().strip("<>").split("#", 1)[0]
        if not href or re.match(r"^[a-z][a-z0-9+.-]*://", href, flags=re.I):
            continue
        links.append(href)
    return links


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Ultimate Design OKF graph.")
    parser.add_argument("root", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    okf_root = root / "references" / "design-okf"
    index_path = okf_root / "index.md"
    concepts = sorted(path for path in okf_root.rglob("*.md") if path != index_path)
    index_targets = {(index_path.parent / href).resolve() for href in local_links(index_path)}

    missing_from_index = [str(path.relative_to(okf_root)) for path in concepts if path.resolve() not in index_targets]
    metadata_errors: list[str] = []
    duplicate_titles: list[str] = []
    title_owners: dict[str, str] = {}
    for path in concepts:
        rel = str(path.relative_to(okf_root))
        meta = frontmatter(read(path))
        missing = [field for field in ("type", "title", "description") if not meta.get(field)]
        if missing:
            metadata_errors.append(f"{rel}: missing {', '.join(missing)}")
        title = meta.get("title", "").casefold()
        if title and title in title_owners:
            duplicate_titles.append(f"{title_owners[title]} <-> {rel}")
        elif title:
            title_owners[title] = rel

    broken_links: list[str] = []
    markdown_files = sorted(root.rglob("*.md"))
    for path in markdown_files:
        for href in local_links(path):
            target = Path(href) if href.startswith("/") else path.parent / href
            if not target.exists():
                broken_links.append(f"{path.relative_to(root)} -> {href}")

    runtime_files = [root / "SKILL.md", *sorted((root / "references").glob("*.md"))]
    runtime_text = "\n".join(read(path) for path in runtime_files if path.exists())
    routed: list[str] = []
    index_only: list[str] = []
    for path in concepts:
        rel = str(path.relative_to(okf_root))
        if f"design-okf/{rel}" in runtime_text:
            routed.append(rel)
        else:
            index_only.append(rel)
    unexpected_index_only = sorted(set(index_only) - EXPECTED_INDEX_ONLY)

    errors = [
        *[f"Missing from index: {item}" for item in missing_from_index],
        *[f"Broken link: {item}" for item in broken_links],
        *[f"Metadata: {item}" for item in metadata_errors],
        *[f"Duplicate title: {item}" for item in duplicate_titles],
        *[f"No direct runtime route: {item}" for item in unexpected_index_only],
    ]
    report = {
        "schemaVersion": "ultimate-design.okf-graph.v1",
        "status": "pass" if not errors else "fail",
        "root": str(root),
        "concept_count": len(concepts),
        "indexed_count": len(concepts) - len(missing_from_index),
        "direct_runtime_route_count": len(routed),
        "direct_runtime_routes": routed,
        "index_only_concepts": index_only,
        "expected_index_only_concepts": sorted(EXPECTED_INDEX_ONLY),
        "unexpected_index_only_concepts": unexpected_index_only,
        "errors": errors,
    }

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"OKF GRAPH VALIDATION {report['status'].upper()}")
        print(f"Concepts: {report['concept_count']}")
        print(f"Indexed: {report['indexed_count']}")
        print(f"Direct runtime routes: {report['direct_runtime_route_count']}")
        print(f"Index-only concepts: {len(index_only)}")
        print(f"Unexpected index-only concepts: {len(unexpected_index_only)}")
        for error in errors:
            print(f"ERROR {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
