# Orchestration selection

**Outcome:** choose coordination with minimal overhead. **Prerequisites:** task scope, budget and harness authority.

1. Start with a single agent for bounded work and manageable context.
2. Consider parallelism for separable work with ownership, outputs and a reason to pay coordination costs.
3. Evaluate task claims, durable state, worktree isolation, review, recovery, budgets and steering channels against current upstream sources and a safe representative task. These are criteria, not assertions about product capabilities.
4. Compare [FirstMate](../catalog/tools/orchestration/firstmate.md), requiring a supported primary harness, Git, authenticated GitHub CLI and backend, with [Oh My OpenAgent](../catalog/tools/orchestration/oh-my-openagent.md), which documents native, OpenCode and Codex editions separately. Verify the selected edition, version and platform.

Optional: independent review for high-risk work. Tradeoffs: duplicated context, setup and integration costs. Evidence: task success, cost and failures. No orchestrator is required by the other recipes.
