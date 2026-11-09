# Review a question in a specialist discipline

**Outcome:** a scoped assessment, design or research report with traceable
evidence, limitations and next actions.
**Use when:** the output concerns architecture, security, accessibility,
research, product, operations, data or communication rather than a code change.
**Prerequisites:** the question, source material and agreed review scope.

## Ingredients

- **Instructions:** applicable project rules and the expected report format.
- **Skill:** one focused procedure selected from the discipline below, when
  suitable. A collection entry is a discovery route; inspect the exact skill.
- **Tools and access:** sources needed to support the specific question.
  Static source access may suffice for a limited review; browser, runtime or
  service access is required for claims about behavior those sources cannot show.
- **Harness:** your existing client with the required access and permissions.

## Choose a discipline

| Desired output | Catalog route | Selection boundary |
| --- | --- | --- |
| Architecture views, boundaries or decisions | [Architecture](../catalog/skills/architecture/README.md) | Tie choices to stakeholder concerns and constraints |
| Security design review or threat model | [Security](../catalog/skills/security-privacy/README.md) | Distinguish threat modeling from runtime security testing |
| Web accessibility findings | [Accessibility and UX](../catalog/skills/accessibility-ux/README.md) | Source review alone cannot establish full conformance |
| Research or source comparison | [Research](../catalog/skills/research/README.md) | Verify source quality and fit outside a scientific context |
| Product framing or experiment plan | [Product and strategy](../catalog/skills/product-strategy/README.md) | Check the exact procedure and domain assumptions |
| Operational review | [Operations](../catalog/skills/operations-reliability/README.md) | Separate advice from authorized changes to running systems |
| Evaluation or measurement plan | [Data and AI](../catalog/skills/data-ai/README.md) | Require representative tasks and explicit success measures |
| Documentation or explanation | [Communication](../catalog/skills/communication/README.md) | Preserve source meaning and verify factual claims |
| SEO or marketing review | [Marketing](../catalog/skills/marketing-discovery/README.md) | The tested SEO revision is excluded from default recommendations |
| Learning or reflection | [Personal development](../catalog/skills/personal-development/README.md) | Coverage is limited; report gaps instead of inventing a skill |

<!-- recipe-skills:start -->
## Upstream choices

Choose one when it fits; these are optional choices, not an install bundle. [Tag meanings](../docs/skill-finder.md#tags-and-programming-languages).

| Use when | Skill and source | Tags | Evidence |
| --- | --- | --- | --- |
| Create architecture views, decision records or an enterprise model. | [Gaurav Sharma · /enterprise-architecture](https://github.com/gauravs19/enterprise-architecture-skill/blob/898fca2b7aa75a725284411f8f125861245f15a8/SKILL.md) | `goal:architecture` `goal:decision-records` `category:architecture` `language:any` | [source-reviewed](../catalog/skills/architecture/enterprise-architecture.md): Exact instruction file reviewed; not locally executed. |
| Explore codebase friction and opportunities to deepen modules. | [Matt Pocock · /improve-codebase-architecture](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/improve-codebase-architecture/SKILL.md) | `goal:architecture` `goal:maintainability` `category:architecture` `category:development` `language:any` | [source-reviewed](../catalog/skills/development/matt-pocock.md): Main SKILL.md reviewed; helper chain not fully reviewed or executed. |
| Investigate a question using primary sources and produce cited findings. | [Matt Pocock · /research](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/research/SKILL.md) | `goal:research` `category:research` `language:any` | [source-reviewed](../catalog/skills/development/matt-pocock.md): Exact instruction file reviewed; not locally executed. |
| Review supplied web markup or visuals against a bounded accessibility checklist. | [Humbleteam · /accessibility-audit](https://github.com/humbleteam/accessibility-audit/blob/b5735da6c03604eea342a7de0e1e6c1d3550dca5/SKILL.md) | `goal:accessibility` `category:accessibility-ux` `language:any` | [locally-tested](../docs/evaluations/2026-10-30/README.md): One static HTML fixture on 2026-10-30; no full conformance assessment. |
| Model repository-grounded assets, trust boundaries, abuse paths and mitigations. | [OpenAI · /security-threat-model](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model/SKILL.md) | `goal:security` `goal:threat-modeling` `category:security-privacy` `language:any` | [locally-tested](../docs/evaluations/2026-10-30/README.md): One synthetic threat-model task and follow-up on 2026-10-30. |
<!-- recipe-skills:end -->

## Steps

1. Define the question, audience, expected artifact and what evidence is needed.
2. Read the discipline index and candidate entry. Select the exact skill only
   after checking its evidence, requirements, scope and upstream instructions.
   If coverage is insufficient, use [discovery](../docs/find-more-skills.md)
   or a bounded general workflow and state the gap.
3. Identify available sources and access. Label any conclusion that needs
   additional evidence as conditional or unverified.
4. Perform the authorized review. Separate observed facts, interpretation,
   proposals and unanswered questions.
5. Deliver prioritized findings, source references, limitations and next steps.

## Ask an agent

```text
Use the specialist-review recipe for [question and discipline]. My sources
are [paths/links] and the output is for [audience]. Select one suitable
procedure, explain what the available evidence can establish and identify
missing access before making claims that depend on it. Produce [artifact]
with source-backed findings, uncertainty and prioritized next steps.
```

## Optional enhancements and tradeoffs

Add another discipline only for a distinct question. Use an independent review
when its value warrants the cost and delegation is authorized. Additional
tools and reviewers do not turn a limited assessment into certification.

## Evidence and checks

Each finding has supporting evidence or an explicit assumption. State what
was inspected, tested and left unverified, and preserve the selected skill's
review date and evaluation scope.
