"""Validate local reference entries and Markdown links without dependencies."""
from datetime import date
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ("ID", "Type", "Primary category", "Tags", "Upstream", "Recommendation",
          "Evidence", "Lifecycle", "Last reviewed", "License")
SECTIONS = ("Purpose and output", "Use or skip", "Requirements and tradeoffs",
            "Obtain and maintain", "Related")
CATEGORIES = {"architecture", "development", "research", "personal-development",
              "token-economy", "observability", "orchestration",
              "context-and-retrieval", "packaging-and-distribution",
              "security-privacy", "accessibility-ux", "marketing-discovery",
              "operations-reliability", "product-strategy", "data-ai", "communication"}
errors = []
ids = {}
template = (ROOT / "templates/catalog-entry.md").read_text(encoding="utf-8")
for field in FIELDS:
    if f"**{field}:**" not in template:
        errors.append(f"catalog-entry template: missing field {field}")
for section in SECTIONS:
    if f"## {section}" not in template:
        errors.append(f"catalog-entry template: missing section {section}")
entries = [p for p in (ROOT / "catalog").rglob("*.md") if p.name != "README.md"]
for path in entries:
    content = path.read_text(encoding="utf-8")
    fields = dict(re.findall(r"^- \*\*([^*]+):\*\* (.+)$", content, re.M))
    for field in FIELDS:
        if not fields.get(field):
            errors.append(f"{path}: missing {field}")
    for section in SECTIONS:
        if f"## {section}" not in content:
            errors.append(f"{path}: missing section {section}")
    identifier = fields.get("ID", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", identifier):
        errors.append(f"{path}: invalid ID")
    if identifier in ids:
        errors.append(f"{path}: duplicate ID {identifier} ({ids[identifier]})")
    ids[identifier] = path
    if fields.get("Primary category") not in CATEGORIES or fields.get("Primary category") != path.parent.name:
        errors.append(f"{path}: invalid category")
    try:
        date.fromisoformat(fields.get("Last reviewed", ""))
    except ValueError:
        errors.append(f"{path}: invalid date")
    if not re.match(r"(?:recommended-for-[a-z-]+|situational|candidate|avoid-for-[a-z-]+)\b", fields.get("Recommendation", "")):
        errors.append(f"{path}: invalid recommendation")
    if not re.match(r"(?:source-reviewed|locally-tested|unverified)\b", fields.get("Evidence", "")):
        errors.append(f"{path}: invalid evidence")
    if not re.match(r"(?:active|archived|superseded|unknown)\b", fields.get("Lifecycle", "")):
        errors.append(f"{path}: invalid lifecycle")

for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    content = path.read_text(encoding="utf-8")
    table_width = None
    for line_number, line in enumerate(content.splitlines(), 1):
        if line.startswith("| ") and line.endswith(" |"):
            width = len(re.split(r"(?<!\\)\|", line))
            if table_width is not None and width != table_width:
                errors.append(f"{path}:{line_number}: inconsistent table columns")
            table_width = width
        else:
            table_width = None
    for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", content):
        url = urlsplit(target.strip().split(" ")[0])
        if url.scheme or url.netloc or not url.path or "<" in url.path:
            continue
        if not (path.parent / unquote(url.path)).exists():
            errors.append(f"{path}: broken link {target}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(entries)} catalog entries; fields, IDs, categories, dates, template, table widths and local file links validated")
print("Not checked: external links/anchors, source claims, licenses, skill behavior or harness compatibility")
