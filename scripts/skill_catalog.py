"""Search focused recipe skills/tools and generate Markdown views. Standard library only."""
import argparse
from datetime import date
import json
from pathlib import Path
import posixpath
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "catalog/recipe-skills.json"
FINDER = "docs/skill-finder.md"
START = "<!-- recipe-skills:start -->"
END = "<!-- recipe-skills:end -->"
CORE_RECIPES = {"recipes/choose-your-setup.md", "recipes/specialist-review.md",
                "recipes/minimal-agent-workflow.md", "recipes/evidence-driven-delivery.md"}
EVIDENCE = {"locally-tested", "source-reviewed", "unverified"}
CATEGORIES = {"development", "architecture", "product-strategy", "research",
              "accessibility-ux", "security-privacy", "personal-development",
              "operations-reliability", "marketing-discovery", "data-ai", "communication"}
ALIASES = {"py": "python", "ts": "typescript", "js": "javascript",
           "c#": "csharp", "c++": "cpp", "golang": "go", "*": "any"}
LANGUAGES = {"any", "python", "typescript", "javascript", "java", "csharp", "cpp",
             "c", "go", "rust", "ruby", "php", "kotlin", "swift", "scala", "sql",
             "html", "css", "shell", "powershell", "dart", "elixir", "fsharp"}
TEXT_FIELDS = ("id", "name", "kind", "source", "upstream", "catalog_entry", "use_when",
               "limits", "source_reviewed", "evidence", "evidence_scope",
               "evidence_reference", "runtime_notes")
LIST_FIELDS = ("goals", "categories", "programming_languages", "aliases", "recipes")


def validate(data):
    errors, ids = [], set()
    if not isinstance(data, list) or not data:
        return ["recipe-skills.json: expected a non-empty list"]
    for index, row in enumerate(data):
        label = f"recipe-skills.json[{index}]"
        if not isinstance(row, dict):
            errors.append(f"{label}: expected an object")
            continue
        missing = [key for key in TEXT_FIELDS if not isinstance(row.get(key), str) or not row[key].strip()]
        missing += [key for key in LIST_FIELDS if not isinstance(row.get(key), list)
                    or not row[key] or any(not isinstance(v, str) or not v.strip() for v in row[key])]
        if missing:
            errors.append(f"{label}: missing/invalid fields {', '.join(missing)}")
            continue
        if row["id"] in ids or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", row["id"]):
            errors.append(f"{label}: duplicate or invalid ID {row['id']}")
        ids.add(row["id"])
        if row["evidence"] not in EVIDENCE:
            errors.append(f"{label}: invalid evidence")
        if row["kind"] not in {"skill", "tool"}:
            errors.append(f"{label}: invalid kind")
        if not set(row["categories"]) <= CATEGORIES:
            errors.append(f"{label}: invalid category")
        languages = set(row["programming_languages"])
        if not languages <= LANGUAGES or ("any" in languages and len(languages) != 1):
            errors.append(f"{label}: invalid programming languages")
        if any(not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", goal) for goal in row["goals"]):
            errors.append(f"{label}: invalid goal tag")
        if not re.fullmatch(r"https://github\.com/[^/]+/[^/]+/blob/[0-9a-f]{40}/.+\.md", row["upstream"]):
            errors.append(f"{label}: upstream must pin the exact Markdown source revision")
        try:
            date.fromisoformat(row["source_reviewed"])
        except ValueError:
            errors.append(f"{label}: invalid source review date")
        for relative in [row["catalog_entry"], row["evidence_reference"], *row["recipes"]]:
            path = (ROOT / relative).resolve()
            if not path.is_relative_to(ROOT) or not path.is_file() or path.suffix != ".md":
                errors.append(f"{label}: invalid local reference {relative}")
        if any(not p.startswith("recipes/") for p in row["recipes"]):
            errors.append(f"{label}: recipe reference must be under recipes/")
    return errors


def load():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        raise ValueError("\n".join(errors))
    return data


def search(data, query="", *, goal=None, category=None, language=None, source=None, evidence=None, kind=None):
    language = ALIASES.get(language.casefold(), language.casefold()) if language else None
    terms = query.casefold().split()
    results = []
    for row in data:
        haystack = " ".join([row["id"], row["name"], row["source"], row["use_when"],
                             *row["goals"], *row["categories"], *row["aliases"]]).casefold()
        if not all(term in haystack for term in terms):
            continue
        if goal and goal.casefold() not in row["goals"]:
            continue
        if category and category.casefold() not in row["categories"]:
            continue
        if language and language not in row["programming_languages"] and "any" not in row["programming_languages"]:
            continue
        if source and source.casefold() not in row["source"].casefold():
            continue
        if evidence and evidence != row["evidence"]:
            continue
        if kind and kind != row["kind"]:
            continue
        results.append(row)
    # Explicit language matches precede cross-language procedures.
    return sorted(results, key=lambda r: (bool(language and language not in r["programming_languages"]), r["id"]))


def link(relative, document):
    return posixpath.relpath(relative, posixpath.dirname(document) or ".")


def tags(row):
    return [*(f"goal:{g}" for g in row["goals"]),
            *(f"category:{c}" for c in row["categories"]),
            *(f"language:{lang}" for lang in row["programming_languages"] if lang != "any")]


def cell(value):
    return value.replace("|", "\\|").replace("\n", " ")


def table(rows, document):
    lines = ["| Use when | Skill and source | Tags | Evidence |", "| --- | --- | --- | --- |"]
    for row in rows:
        name = "/" + row["name"] if row["kind"] == "skill" else row["name"] + " (tool)"
        source = f"[{row['source']} · {name}]({row['upstream']})"
        status = f"[{row['evidence']}]({link(row['evidence_reference'], document)}): {row['evidence_scope']}"
        lines.append("| " + " | ".join(map(cell, [row["use_when"], source,
                     " ".join(f"`{tag}`" for tag in tags(row)), status])) + " |")
    return "\n".join(lines)


def replace_block(text, block):
    if text.count(START) != text.count(END) or text.count(START) > 1:
        raise ValueError("Mismatched or duplicate recipe-skills markers")
    if START in text:
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        return before + block + after
    if "\n## Steps\n" not in text:
        raise ValueError("Recipe is missing its Steps section")
    return text.replace("\n## Steps\n", "\n" + block + "\n\n## Steps\n", 1)


def documents(data):
    finder = """# Find a concrete skill or workflow tool

Search this page with your browser, ask your agent, or use the local command below.
This focused index covers upstream skills and workflow tools linked directly by recipes, not
every candidate in the broader catalog. It contains references, not installed skills.

## Search by goal, category or programming language

```text
python scripts/skill_catalog.py search terugblik
python scripts/skill_catalog.py search --goal specification
python scripts/skill_catalog.py search --category architecture --language typescript
python scripts/skill_catalog.py search --source Matt --evidence source-reviewed
python scripts/skill_catalog.py search --goal specification --kind tool
python scripts/skill_catalog.py tags
```

Run from the repository root; the script itself also works from other directories.
Filters combine with AND; free text supports Dutch aliases and English terms.
Add `--json` for structured results. Searching needs Python, not a skill install.

## Tags and programming languages

- `goal:` describes the outcome; `category:` describes the discipline.
- `language:` means **programming language**, never the language of the prose.
- `language:any` means the reviewed instructions impose no particular programming
  language. It matches every `--language` filter, after explicit language matches;
  it does not mean every stack/client was runtime-tested. The current focused set
  consists of these cross-language procedures. This default is omitted from
  badges to avoid repeating it in every row; it remains in the JSON and search.
  Programming-language neutrality does not expand a software/web-specific scope:
  check the use case and linked constraints before selecting a workflow.
- Runtime requirements are separate: a Python validator does not make a skill
  Python-specific. Each JSON record includes `runtime_notes` and constraints.
- Tags use English tokens; Dutch search aliases include `terugblik`,
  `specificatie`, `architectuur`, `toegankelijkheid` and `beveiliging`.
- `/name` is upstream skill naming; actual invocation depends on installation
  and client. Toolkits such as OpenSpec and Spec Kit are labeled `(tool)`.

## Upstream choices

""" + table(data, FINDER) + """

`locally-tested` applies only to the linked revision, task and phase; it is not
a whole-collection endorsement. `source-reviewed` is a source inspection, not
execution evidence; `unverified` means neither has been established here.
Exact sources, source-review dates, constraints and evaluation scope live in
[recipe-skills.json](../catalog/recipe-skills.json). The linked catalog entries
hold license and adoption guidance. Historic evaluations retain their own dates.

Maintainers: edit that JSON, then run `python scripts/skill_catalog.py build`.
The finder and marked recipe tables are generated from the same records.
"""
    output = {FINDER: finder}
    # Include old marked views so removing the last choice cannot leave a stale table.
    recipes = {p for row in data for p in row["recipes"]}
    for path in (ROOT / "recipes").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if START in text or END in text:
            recipes.add(path.relative_to(ROOT).as_posix())
    for recipe in sorted(recipes):
        rows = [row for row in data if recipe in row["recipes"]]
        if rows:
            section = ("## Upstream choices\n\nSelect only for a matching need and scope. "
                       f"[Tag meanings]({link(FINDER, recipe)}#tags-and-programming-languages).\n\n"
                       + table(rows, recipe))
            if recipe in CORE_RECIPES:
                section = "<details>\n<summary>Optional specialist workflows</summary>\n\n" + section + "\n\n</details>"
            block = START + "\n" + section + "\n" + END
        else:
            block = ""
        output[recipe] = replace_block((ROOT / recipe).read_text(encoding="utf-8"), block)
    return output


def check_generated():
    try:
        expected = documents(load())
        return [f"{path}: generated skill view is stale; run python scripts/skill_catalog.py build"
                for path, text in expected.items()
                if not (ROOT / path).exists() or (ROOT / path).read_text(encoding="utf-8") != text]
    except (ValueError, OSError, KeyError) as exc:
        return [str(exc)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    find = commands.add_parser("search", help="Filter upstream choices; language means programming language")
    find.add_argument("query", nargs="*", help="English terms or Dutch aliases")
    for name in ("goal", "category", "source"):
        find.add_argument("--" + name)
    find.add_argument("--language", type=lambda v: ALIASES.get(v.casefold(), v.casefold()), choices=sorted(LANGUAGES))
    find.add_argument("--evidence", choices=sorted(EVIDENCE))
    find.add_argument("--kind", choices=["skill", "tool"])
    find.add_argument("--json", action="store_true")
    commands.add_parser("tags", help="List available filter values")
    commands.add_parser("build", help="Regenerate the finder and marked recipe tables")
    commands.add_parser("check", help="Validate metadata and detect generated-view drift")
    args = parser.parse_args()
    try:
        data = load()
        if args.command == "check":
            errors = check_generated()
            print("\n".join(errors) if errors else f"OK: {len(data)} upstream choices and generated views")
            return bool(errors)
        if args.command == "build":
            for path, content in documents(data).items():
                (ROOT / path).write_text(content, encoding="utf-8")
            print(f"Built finder and recipe views for {len(data)} upstream choices")
        elif args.command == "tags":
            for field in ("goals", "categories", "programming_languages"):
                print(f"{field}: {', '.join(sorted({v for row in data for v in row[field]}))}")
            print("sources: " + ", ".join(sorted({row["source"] for row in data})))
            print("evidence: " + ", ".join(sorted({row["evidence"] for row in data})))
        else:
            rows = search(data, " ".join(args.query), **{key: getattr(args, key)
                          for key in ("goal", "category", "language", "source", "evidence", "kind")})
            if args.json:
                print(json.dumps(rows, ensure_ascii=False, indent=2))
            elif not rows:
                print("No matching choices. Try fewer filters or the broader catalog.")
            else:
                for row in rows:
                    print(f"{row['source']} {row['name']} ({row['kind']}) [{row['evidence']}]\n"
                          f"  {row['use_when']}\n  {' '.join(tags(row))}\n"
                          f"  Source: {row['upstream']}\n  Recipe: {', '.join(row['recipes'])}\n"
                          f"  Evidence: {row['evidence_scope']}\n  Limits: {row['limits']}\n"
                          f"  Runtime: {row['runtime_notes']}\n")
                    if args.language and "any" in row["programming_languages"]:
                        print("  Language match: general procedure; no language restriction recorded. Check its task/client scope.\n")
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, str(exc) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
