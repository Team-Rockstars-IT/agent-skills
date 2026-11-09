# Orchestration selection

**Outcome:** choose coordination with minimal overhead. **Prerequisites:** task scope, budget and harness authority.

**Use when:** separable work might benefit from coordinated agents and the
existing workflow has a concrete coordination bottleneck.

## Ingredients

- **Instructions:** task ownership, integration boundaries and acceptance.
- **Skill:** none required to make the selection.
- **Tools and access:** the current agent's coordination capabilities, if any;
  compare external orchestrators only when they fill a demonstrated gap.
- **Harness:** check the actual client, supported edition and delegation rules.

## Steps

1. Start with a single agent for bounded work and manageable context.
2. Consider parallelism for separable work with ownership, outputs and a reason to pay coordination costs.
3. Evaluate task claims, durable state, worktree isolation, review, recovery, budgets and steering channels against current upstream sources and a safe representative task. These are criteria, not assertions about product capabilities.
4. Compare [FirstMate](../catalog/tools/orchestration/firstmate.md), requiring a supported primary harness, Git, authenticated GitHub CLI and backend, with [Oh My OpenAgent](../catalog/tools/orchestration/oh-my-openagent.md), which documents native, OpenCode and Codex editions separately. Verify the selected edition, version and platform.

## Ask an agent

```text
Use the orchestration-selection recipe for [work]. Identify whether tasks
are separable, what outputs and ownership they need, and how integration
would be checked. Compare the existing single-agent workflow with the
smallest useful coordination option. Give advice only; do not launch agents
or install an orchestrator.
```

## Optional enhancements and tradeoffs

Independent review can help when its value justifies the effort and delegation
is authorized. Account for duplicated context, setup and integration costs.
No orchestrator is required by the other recipes.

## Evidence and checks

Task success, cost and failures on a representative task; separate documented
capabilities from observed results. Choosing this recipe does not itself
authorize delegation.
