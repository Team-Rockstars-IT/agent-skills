# Clarify what you need

**Outcome:** a bounded task, an expected result and a useful first step.
**Use when:** the intent, boundaries or way forward are unclear.
**Input:** your goal and any available brief, document, design, data or project.

## Ingredients

- Use the context already supplied and applicable project rules.
- No additional skill or tool is required by this recipe. Select one only
  if a specific missing capability affects the next step.

## Steps

1. State the desired result, who will use it and how they could assess it.
2. Identify the binding constraints, available evidence and what is outside
   the task. Ask a focused question only when its answer changes the approach.
3. Match the next output to a [core goal](README.md#core-goals). Use existing
   capabilities; do not assume a repository, shell or particular agent client.
4. Give one first action and the expected output. Keep assumptions explicit
   rather than turning them into domain facts.

## Ask an agent

```text
I want to [goal]. Use the supplied context to clarify the intended result,
boundaries and how to check success. Ask only about a missing fact that would
change the approach, then give me one useful first step.
```

## Optional enhancements and tradeoffs

Use [discovery](../docs/find-more-skills.md) for a genuine gap. Before proposing
installation commands or executing a third-party skill, verify its exact
upstream artifact and [client compatibility](../docs/portability.md).
Recommendation-only requests do not authorize installs or project changes.

## Evidence and checks

The task names a result, constraints, a success check and remaining assumptions.
For a setup recommendation, use **Use**, **Need**, **Start** as described in
[AGENTS.md](../AGENTS.md). No availability or compatibility is implied by a catalog listing.
