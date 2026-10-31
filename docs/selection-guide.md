# Selection and conflict guide

Select by outcome, authority and constraints; start with one workflow and add another for a distinct gap.

| Need | Start | Add when needed |
| --- | --- | --- |
| Unclear work | [define-work](../define-work/SKILL.md) | [OpenSpec](../catalog/skills/development/openspec.md) for durable specifications |
| Readiness | [Agentic Readiness Assessment](../catalog/skills/development/agentic-readiness-assessment.md) | [agents-md](../agents-md/SKILL.md) to draft instructions |
| Behavioral change | [Matt Pocock TDD](../catalog/skills/development/matt-pocock.md) | reproduce-first diagnosis for hard bugs |
| Architecture | [enterprise architecture](../catalog/skills/architecture/enterprise-architecture.md) | codebase architecture workflow |
| Research | [research](../catalog/skills/research/README.md) | [Context7](../catalog/tools/context-and-retrieval/context7.md) for supported documentation |
| Handover | [pr-evidence](../pr-evidence/SKILL.md) | independent review when risk warrants |
| Coordination | [orchestration selection](../recipes/orchestration-selection.md) | orchestrator for demonstrated need |
| Discover more skills or instructions | [Discovery guide](find-more-skills.md) | compare upstream instructions and harness compatibility |

## Conflicts and overlap

- Explicit user instructions and higher-priority harness rules govern. Skills and repository guidance do not grant authority. Follow the higher-priority instruction; surface consequential equal-priority conflicts.
- Define-work, OpenSpec and planning skills overlap. Choose one primary work definition; avoid conflicting plans. An explicit stop-after-planning request takes precedence over a skill that proceeds.
- Test-first and implement-first can conflict. Follow the requested method; if test-first is impossible, explain and agree an alternative where necessary. Specifications define behavior; TDD supplies feedback.
- Review evaluates changes; pr-evidence reports checks. Generated prose is not execution evidence.
- Broad skill triggers can duplicate gates, reviews or subagents. Inspect instructions, narrow triggers where supported and choose one. Skills cannot override a harness forbidding delegation.
- The upstream readiness assessment examines a repository and can write a report and run a reversible probe; agents-md drafts instructions. Neither certifies security or authorizes changes.
- Skills are instructions, tools act, MCP exposes capabilities, harnesses execute and orchestrators coordinate. They are not interchangeable.

TDD is useful at meaningful behavioral seams, not for tests mirroring implementation. Use lightweight scope for modest changes and durable specifications when dependencies, stakeholders or change over time justify them. Reproduce failures before debugging; record important architecture decisions.

## Why these sources

The starter pack favors a few complementary public sources over comprehensive coverage. Exadel's assessment directly addresses repository readiness; its writes and checks must fit the task's authority. Matt Pocock supplies discrete engineering workflows, including the TDD skill also available in the contributor's environment; Addy Osmani offers lifecycle-oriented alternatives to compare, not a requirement to install both collections. Enterprise Architecture supplies architecture views and decisions. OpenSpec adds durable specifications where a short work definition is insufficient. The Agent Skills specification helps authors assess packaging. RTK, Graphify, Context7 and TokenTelemetry address different output, retrieval and measurement needs. FirstMate and Oh My OpenAgent are candidates only when coordination justifies their operational costs; APM is optional distribution. Local or personal skills without a verified public upstream are not copied or presented as public recommendations.
