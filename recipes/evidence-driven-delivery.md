# Evidence-driven delivery

**Outcome:** reviewable work tied to observed outcomes. **Prerequisites:** a task and authority to act.

**Use when:** handing over completed work or preparing a pull request.

## Ingredients

- **Instructions:** task acceptance and the project's review conventions.
- **Skill:** [pr-evidence](../pr-evidence/SKILL.md) for a structured evidence bundle.
- **Tools and access:** the actual diff and check output; repository hosting
  access only if publishing a pull request is in scope.
- **Harness:** the existing client; no orchestrator is required.

## Steps

1. Define intent, scope and acceptance; map context and ownership.
2. Implement in small steps with checks appropriate to risk.
3. Review the actual diff and report results and gaps with [pr-evidence](../pr-evidence/SKILL.md).
4. Where applicable, compare post-merge observations with intent and feed discrepancies back into planning.

## Ask an agent

```text
Use the evidence-driven-delivery recipe for [completed task/diff]. Prepare
a reviewable handover with the objective, approach, changed files, checks
actually run, results, remaining risks and review focus. Identify missing
evidence explicitly. Preparing the handover does not authorize publishing it.
```

## Optional enhancements and tradeoffs

[OpenSpec](../catalog/skills/development/openspec.md) can support durable
specifications when justified earlier in the work; maintaining artifacts
costs effort. A delivery handover can use existing task records.

## Evidence and checks

Actual acceptance checks, review and separately observed operational outcomes.
Keep checks that passed, failed and were not run distinct.
