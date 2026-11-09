# Research a question and compare options

**Outcome:** evidence-backed findings or a reasoned recommendation.
**Use when:** answering a question, comparing alternatives or preparing a decision.
**Input:** the question, available sources, constraints and intended audience.

## Ingredients

- Supplied briefs, documents, data, observations or project material.
- Source access appropriate to the claims. Use your existing agent and tools;
  add a specialist workflow only for a question within its documented scope.

## Steps

1. State the question and the decision it supports. Define comparison criteria
   before choosing a preferred option.
2. Gather the evidence that can establish each material claim. Keep supplied
   facts, external facts, interpretation and proposals separate.
3. Compare alternatives against the same constraints and look for evidence
   that could change the initial recommendation.
4. Mark missing information and unsupported claims explicitly. Ask only when
   an unanswered question would materially change the result.
5. Deliver findings, sources, tradeoffs, uncertainty and a concrete next action.

## Ask an agent

```text
Investigate [question] using [sources]. Compare the options against [constraints]
and explain which evidence supports the conclusion. Separate facts, assumptions
and proposals. Give a recommendation when the evidence supports one and state
what still needs checking.
```

## Optional enhancements and tradeoffs

Browse the [catalog](../catalog/README.md) for a specific discipline. Architecture,
web accessibility, AppSec and codebase skills retain their own scope; they are
not universal review procedures. A general agent can work directly from the
supplied evidence when no specialist procedure is needed.

<!-- recipe-skills:start -->
<details>
<summary>Optional specialist workflows</summary>

## Upstream choices

Select only for a matching need and scope. [Tag meanings](../docs/skill-finder.md#tags-and-programming-languages).

| Use when | Skill and source | Tags | Evidence |
| --- | --- | --- | --- |
| Create architecture views, decision records or an enterprise model. | [Gaurav Sharma · /enterprise-architecture](https://github.com/gauravs19/enterprise-architecture-skill/blob/898fca2b7aa75a725284411f8f125861245f15a8/SKILL.md) | `goal:architecture` `goal:decision-records` `category:architecture` | [source-reviewed](../catalog/skills/architecture/enterprise-architecture.md): Exact instruction file reviewed; not locally executed. |
| Explore codebase friction and opportunities to deepen modules. | [Matt Pocock · /improve-codebase-architecture](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/improve-codebase-architecture/SKILL.md) | `goal:architecture` `goal:maintainability` `category:architecture` `category:development` | [source-reviewed](../catalog/skills/development/matt-pocock.md): Main SKILL.md reviewed; helper chain not fully reviewed or executed. |
| Investigate a question using primary sources and produce cited findings. | [Matt Pocock · /research](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/research/SKILL.md) | `goal:research` `category:research` | [source-reviewed](../catalog/skills/development/matt-pocock.md): Exact instruction file reviewed; not locally executed. |
| Review supplied web markup or visuals against a bounded accessibility checklist. | [Humbleteam · /accessibility-audit](https://github.com/humbleteam/accessibility-audit/blob/b5735da6c03604eea342a7de0e1e6c1d3550dca5/SKILL.md) | `goal:accessibility` `category:accessibility-ux` | [locally-tested](../docs/evaluations/2026-10-30/README.md): One static HTML fixture on 2026-10-30; no full conformance assessment. |
| Model repository-grounded assets, trust boundaries, abuse paths and mitigations. | [OpenAI · /security-threat-model](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model/SKILL.md) | `goal:security` `goal:threat-modeling` `category:security-privacy` | [locally-tested](../docs/evaluations/2026-10-30/README.md): One synthetic threat-model task and follow-up on 2026-10-30. |

</details>
<!-- recipe-skills:end -->

## Evidence and checks

Each substantive finding has a source or an explicit assumption. State what was
inspected and what the available material cannot establish. Record the selected
upstream revision and evidence scope when a specialist skill is used.
