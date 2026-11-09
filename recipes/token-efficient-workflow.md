# Token-efficient workflow

**Outcome:** improve cost per successful task without quality loss. **Prerequisites:** representative tasks and baseline observations.

**Use when:** context volume, retries or execution cost cause an observed problem.

## Ingredients

- **Instructions:** identical task acceptance for the baseline and comparison.
- **Skill:** none required; scope context and measure the existing workflow first.
- **Tools and access:** actual check results, usage records if available and
  the [evaluation worksheet](../docs/evaluation.md). Do not invent unavailable metrics.
- **Harness:** the client being evaluated, with its version and context recorded.

<!-- recipe-skills:start -->
## Upstream choices

Select only for a matching need and scope. [Tag meanings](../docs/skill-finder.md#tags-and-programming-languages).

| Use when | Skill and source | Tags | Evidence |
| --- | --- | --- | --- |
| After session friction, identify improvements to navigation, checks, steering files or tools. | [Matt Pocock · /retro](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/retro/SKILL.md) | `goal:retrospective` `goal:workflow-improvement` `category:development` `category:personal-development` | [source-reviewed](../catalog/skills/development/matt-pocock-retro.md): retro, writing-for-agents, README and license reviewed; no local execution. |
<!-- recipe-skills:end -->

## Steps

1. Record a baseline with the [worksheet](../docs/evaluation.md).
2. Scope searches and logs; retain raw errors.
3. Retrieve targeted context, use concise handovers and compare quality.
4. Include cold and warm retrieval costs, retries and manual effort.

## Ask an agent

```text
Use the token-efficient-workflow recipe to investigate [observed problem].
Record a baseline on [representative task], identify the likely cause and
propose one change to compare under the same acceptance criteria. Include
setup, retries and manual effort. State any unavailable measurements and
do not install tools as part of the diagnosis.
```

## Optional enhancements and tradeoffs

[RTK](../catalog/tools/token-economy/rtk.md),
[Graphify](../catalog/tools/context-and-retrieval/graphify.md) and
[TokenTelemetry](../catalog/tools/observability/tokentelemetry.md) address
different mechanisms and add setup/privacy costs. Read their entries and
current upstream requirements before selecting one for a demonstrated gap.

## Evidence and checks

Matched task outcomes and measured usage, with missing data labeled. Compare
cost per successful task rather than assuming smaller output means less cost.
