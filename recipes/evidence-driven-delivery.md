# Review a result and hand it over

**Outcome:** findings and a handover tied to observable results.
**Use when:** assessing an artifact or preparing work for another person.
**Input:** the artifact, intended outcome, acceptance criteria and available evidence.

## Ingredients

- The relevant brief, document, design, analysis or code and its constraints.
- Existing evidence and appropriate review tools. Publication or changes to
  the reviewed artifact require their own authorized scope.

## Steps

1. Establish the audience, intended result and acceptance criteria.
2. Inspect the artifact and its supporting evidence. Run relevant checks when
   authorized; do not assume every artifact needs a shell or automated tests.
3. Report findings with evidence, impact and a practical next action. Distinguish
   confirmed defects, proposals and questions requiring more information.
4. Prepare a short handover: result, what changed, checks actually performed,
   remaining risks or unknowns and the next action or decision.
5. Keep operational and user outcomes separate until observed. A review or
   polished handover does not itself prove acceptance.

## Ask an agent

```text
Review [artifact] against [intended outcome and criteria]. Use the available
evidence, identify material gaps and prepare a concise handover for [audience].
Separate checks that passed, failed and were not performed. Do not publish or
modify the artifact unless that action is part of the request.
```

## Optional enhancements and tradeoffs

For a software pull request, [pr-evidence](../pr-evidence/SKILL.md) provides an
evidence-bundle format. Matt Pocock's retro is a separate, deliberately selected
review of a coding session's environment. Neither is required for a document,
decision or design handover.

<!-- recipe-skills:start -->
<details>
<summary>Optional specialist workflows</summary>

## Upstream choices

Select only for a matching need and scope. [Tag meanings](../docs/skill-finder.md#tags-and-programming-languages).

| Use when | Skill and source | Tags | Evidence |
| --- | --- | --- | --- |
| After session friction, identify improvements to navigation, checks, steering files or tools. | [Matt Pocock · /retro](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/retro/SKILL.md) | `goal:retrospective` `goal:workflow-improvement` `category:development` `category:personal-development` | [source-reviewed](../catalog/skills/development/matt-pocock-retro.md): retro, writing-for-agents, README and license reviewed; no local execution. |

</details>
<!-- recipe-skills:end -->

## Evidence and checks

Findings refer to the actual artifact and criteria. Evidence may include source
checks, calculations, scenario reviews, human observations or executable tests.
Missing runtime or user evidence stays unknown.
