# Enterprise architecture

- **ID:** enterprise-architecture
- **Type:** skill
- **Primary category:** architecture
- **Tags:** architecture, agent-assisted-work
- **Upstream:** [Enterprise architecture SKILL.md at the reviewed revision](https://github.com/gauravs19/enterprise-architecture-skill/blob/898fca2b7aa75a725284411f8f125861245f15a8/SKILL.md)
- **Recommendation:** situational — for C4, enterprise mapping or ADRs.
- **Evidence:** source-reviewed on 2026-11-09: exact SKILL.md and MIT license; references and optional linter not fully reviewed or executed here.
- **Lifecycle:** unknown; check current upstream activity.
- **Last reviewed:** 2026-11-09
- **License:** [MIT at the reviewed revision](https://github.com/gauravs19/enterprise-architecture-skill/blob/898fca2b7aa75a725284411f8f125861245f15a8/LICENSE).

## Purpose and output

Architecture diagrams, documentation/decision records, design reviews and
enterprise models using C4, ArchiMate, TOGAF and arc42/ADR as appropriate.

## Use or skip

Use for C4, enterprise mapping or ADRs. Skip for small code changes.

## Requirements and tradeoffs

Claude Code documented; other harnesses unverified. Load only the references
needed for the chosen view. Outputs can include Markdown, Structurizr DSL,
Mermaid or PlantUML. The optional consistency linter needs Python; that is a
tooling runtime, not a restriction to Python applications. Token and cost
impact is unmeasured here.

## Obtain and maintain

Follow current [upstream instructions](https://github.com/gauravs19/enterprise-architecture-skill), reviewing permissions and compatibility. Prefer a compatible stable release; optionally pin a reviewed version or commit in consuming projects.

## Related

[Selection and conflicts](../../../docs/selection-guide.md) · [Evaluation](../../../docs/evaluation.md) · [Recipes](../../../recipes/README.md)
