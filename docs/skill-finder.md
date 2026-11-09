# Find a concrete skill or workflow tool

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
  consists of these cross-language procedures. Web accessibility remains web-scoped.
- Runtime requirements are separate: a Python validator does not make a skill
  Python-specific. Each JSON record includes `runtime_notes` and constraints.
- Tags use English tokens; Dutch search aliases include `terugblik`,
  `specificatie`, `architectuur`, `toegankelijkheid` and `beveiliging`.
- `/name` is upstream skill naming; actual invocation depends on installation
  and client. Toolkits such as OpenSpec and Spec Kit are labeled `(tool)`.

## Upstream choices

| Use when | Skill and source | Tags | Evidence |
| --- | --- | --- | --- |
| Implement behavior test-first at agreed public interfaces. | [Matt Pocock · /tdd](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/tdd/SKILL.md) | `goal:testing` `category:development` `language:any` | [locally-tested](evaluations/2026-10-30/README.md): One synthetic TDD task on 2026-10-30; this pinned revision only. |
| Investigate a difficult bug or performance regression with a repeatable feedback loop. | [Matt Pocock · /diagnosing-bugs](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/diagnosing-bugs/SKILL.md) | `goal:debugging` `category:development` `language:any` | [source-reviewed](../catalog/skills/development/matt-pocock.md): Exact instruction file reviewed; not locally executed. |
| Specify a larger or ambiguous change before planning and coding. | [Addy Osmani · /spec-driven-development](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/spec-driven-development/SKILL.md) | `goal:specification` `category:development` `category:product-strategy` `language:any` | [locally-tested](evaluations/2026-10-30/README.md): Specification phase only, one synthetic task on 2026-10-30. |
| Create architecture views, decision records or an enterprise model. | [Gaurav Sharma · /enterprise-architecture](https://github.com/gauravs19/enterprise-architecture-skill/blob/898fca2b7aa75a725284411f8f125861245f15a8/SKILL.md) | `goal:architecture` `goal:decision-records` `category:architecture` `language:any` | [source-reviewed](../catalog/skills/architecture/enterprise-architecture.md): Exact instruction file reviewed; not locally executed. |
| Explore codebase friction and opportunities to deepen modules. | [Matt Pocock · /improve-codebase-architecture](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/improve-codebase-architecture/SKILL.md) | `goal:architecture` `goal:maintainability` `category:architecture` `category:development` `language:any` | [source-reviewed](../catalog/skills/development/matt-pocock.md): Main SKILL.md reviewed; helper chain not fully reviewed or executed. |
| Investigate a question using primary sources and produce cited findings. | [Matt Pocock · /research](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/research/SKILL.md) | `goal:research` `category:research` `language:any` | [source-reviewed](../catalog/skills/development/matt-pocock.md): Exact instruction file reviewed; not locally executed. |
| Review supplied web markup or visuals against a bounded accessibility checklist. | [Humbleteam · /accessibility-audit](https://github.com/humbleteam/accessibility-audit/blob/b5735da6c03604eea342a7de0e1e6c1d3550dca5/SKILL.md) | `goal:accessibility` `category:accessibility-ux` `language:any` | [locally-tested](evaluations/2026-10-30/README.md): One static HTML fixture on 2026-10-30; no full conformance assessment. |
| Model repository-grounded assets, trust boundaries, abuse paths and mitigations. | [OpenAI · /security-threat-model](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model/SKILL.md) | `goal:security` `goal:threat-modeling` `category:security-privacy` `language:any` | [locally-tested](evaluations/2026-10-30/README.md): One synthetic threat-model task and follow-up on 2026-10-30. |
| Run a deliberate comprehensive repository-readiness assessment. | [Exadel · /agentic-readiness-assessment](https://github.com/exadel-inc/agentic-readiness-assessment/blob/1313702ad53e2f2c069e2f4ef2dbebd19cb17e3d/skills/agentic-readiness-assessment/SKILL.md) | `goal:readiness` `category:development` `language:any` | [locally-tested](evaluations/2026-10-30/README.md): One synthetic repository on 2026-10-30; validator run separately by evaluator. |
| After session friction, identify improvements to navigation, checks, steering files or tools. | [Matt Pocock · /retro](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/retro/SKILL.md) | `goal:retrospective` `goal:workflow-improvement` `category:development` `category:personal-development` `language:any` | [source-reviewed](../catalog/skills/development/matt-pocock-retro.md): retro, writing-for-agents, README and license reviewed; no local execution. |
| Use a change-centric SDD toolkit with proposals, specs, design, tasks and archival. | [Fission-AI · OpenSpec (tool)](https://github.com/Fission-AI/OpenSpec/blob/0fa4a9705c20ef1c571fe3ded74435733e4b73a1/README.md) | `goal:specification` `category:development` `language:any` | [source-reviewed](../catalog/skills/development/openspec.md): README and license reviewed; no local execution or comparative benchmark. |
| Use a maintained SDD toolkit with project principles, specification, plan, tasks and implementation/convergence. | [GitHub · Spec Kit (tool)](https://github.com/github/spec-kit/blob/c43849408ac0de2ca6a52f14eaae71449776057b/README.md) | `goal:specification` `category:development` `language:any` | [source-reviewed](../catalog/skills/development/spec-kit.md): README and license reviewed; no local execution or comparative benchmark. |

`locally-tested` applies only to the linked revision, task and phase; it is not
a whole-collection endorsement. `source-reviewed` is a source inspection, not
execution evidence; `unverified` means neither has been established here.
Exact sources, source-review dates, constraints and evaluation scope live in
[recipe-skills.json](../catalog/recipe-skills.json). The linked catalog entries
hold license and adoption guidance. Historic evaluations retain their own dates.

Maintainers: edit that JSON, then run `python scripts/skill_catalog.py build`.
The finder and marked recipe tables are generated from the same records.
