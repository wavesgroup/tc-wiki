#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
PAPERS = WIKI / "papers"
TOPICS = WIKI / "topics"
METHODS = WIKI / "methods"
SYNTHESES = WIKI / "syntheses"
README = ROOT / "README.md"
AUTHORS = WIKI / "authors.md"
TC_CASES = WIKI / "tc-cases.md"
INDEX = WIKI / "index.md"

REQUIRED_PAPER_SECTIONS = [
    "Citation",
    "Research Question",
    "Data And Methods",
    "Findings",
    "Limitations",
    "Referenced Papers",
    "Linked Pages",
]
ALLOWED_SOURCE_ACCESS = {"full_text", "metadata_only", "citation_network", "mixed"}
STALE_INDEX_PATTERNS = (
    re.compile(r"^new\b", re.IGNORECASE),
    re.compile(r"\bseed\b", re.IGNORECASE),
    re.compile(r"\bfirst-pass\b", re.IGNORECASE),
    re.compile(r"^early page\b", re.IGNORECASE),
)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)")
AUTHOR_ENTRY_RE = re.compile(r"^- \*\*", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
SECTION_RE = re.compile(r"^# (.+)$", re.MULTILINE)
DATE_HEADING_RE = re.compile(r"^# .*\(\d{4}-\d{2}-\d{2}[^)]*\)", re.MULTILINE)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"')
    return result


def find_readme_count(label: str) -> int | None:
    match = re.search(rf"{re.escape(label)} \((\d+)\)", read(README))
    return int(match.group(1)) if match else None


def count_papers() -> int:
    return len(list(PAPERS.glob("*.md")))


def count_authors() -> int:
    return len(AUTHOR_ENTRY_RE.findall(read(AUTHORS)))


def count_storms() -> int:
    return len(AUTHOR_ENTRY_RE.findall(read(TC_CASES)))


def content_files() -> list[Path]:
    files: list[Path] = []
    for directory in (PAPERS, TOPICS, METHODS, SYNTHESES):
        files.extend(sorted(directory.glob("*.md")))
    return files


def build_inbound_counts(files: list[Path]) -> dict[Path, list[Path]]:
    inbound: dict[Path, list[Path]] = {path.resolve(): [] for path in files}
    for src in files:
        for target_raw in LINK_RE.findall(read(src)):
            if target_raw.startswith("http://") or target_raw.startswith("https://"):
                continue
            target_path = (src.parent / target_raw).resolve()
            if target_path in inbound and target_path != src.resolve():
                inbound[target_path].append(src.resolve())
    return inbound


def looks_equation_central(text: str) -> bool:
    lowered = text.lower()
    triggers = (
        "study type: analytical",
        "study type: theoretical",
        "study type: analytical/theoretical",
        "theoretical research article",
        "heat-engine formulation",
        "potential-intensity",
        "analytical manipulation",
        "bulk drag",
        "budget study",
        "diagnostic formulas",
    )
    return any(trigger in lowered for trigger in triggers)


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    expected_counts = {
        "Papers": count_papers(),
        "Authors": count_authors(),
        "Storms": count_storms(),
    }
    for label, expected in expected_counts.items():
        actual = find_readme_count(label)
        if actual is None:
            errors.append(f"README.md is missing `{label} (x)`.")
        elif actual != expected:
            errors.append(
                f"README.md has `{label} ({actual})`, but the repository count is {expected}."
            )

    for paper in sorted(PAPERS.glob("*.md")):
        text = read(paper)
        headings = set(SECTION_RE.findall(text))
        missing = [
            section for section in REQUIRED_PAPER_SECTIONS if section not in headings
        ]
        if missing:
            errors.append(
                f"{paper.relative_to(ROOT)} is missing sections: {', '.join(missing)}."
            )

        frontmatter = parse_frontmatter(text)
        source_access = frontmatter.get("source_access")
        if source_access is None:
            warnings.append(f"{paper.relative_to(ROOT)} is missing `source_access`.")
        elif source_access not in ALLOWED_SOURCE_ACCESS:
            errors.append(
                f"{paper.relative_to(ROOT)} has invalid `source_access: {source_access}`."
            )
        elif source_access == "full_text" and looks_equation_central(text):
            if "Key Equations" not in headings:
                errors.append(
                    f"{paper.relative_to(ROOT)} is `full_text` and equation-central but lacks `# Key Equations`."
                )

    index_text = read(INDEX)
    for lineno, line in enumerate(index_text.splitlines(), start=1):
        match = re.search(r"\]\([^)]+\):\s*(.*)$", line)
        if not match:
            continue
        description = match.group(1).strip()
        if any(pattern.search(description) for pattern in STALE_INDEX_PATTERNS):
            errors.append(
                f"wiki/index.md:{lineno} uses stale change-history language in a blurb: {line.strip()}"
            )

    for directory in (TOPICS, METHODS, SYNTHESES):
        for page in sorted(directory.glob("*.md")):
            text = read(page)
            if re.search(r"^# New Evidence\b", text, re.MULTILINE):
                errors.append(
                    f"{page.relative_to(ROOT)} contains a `# New Evidence` append section."
                )
            elif DATE_HEADING_RE.search(text):
                errors.append(
                    f"{page.relative_to(ROOT)} contains a dated heading instead of integrating the update."
                )

    files = content_files()
    inbound = build_inbound_counts(files)
    for page, refs in sorted(inbound.items(), key=lambda item: str(item[0])):
        rel = page.relative_to(ROOT)
        ref_count = len(refs)
        if ref_count == 0:
            errors.append(f"{rel} has no inbound links from other content pages.")
        elif ref_count == 1:
            warnings.append(
                f"{rel} has only one inbound link from other content pages."
            )

    if errors:
        print("Errors:")
        for entry in errors:
            print(f"- {entry}")
    if warnings:
        print("Warnings:")
        for entry in warnings:
            print(f"- {entry}")

    if not errors and not warnings:
        print("wiki lint passed with no findings.")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
