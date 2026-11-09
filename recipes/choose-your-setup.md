# Choose what you need

**Outcome:** one recipe, any missing essentials and a first step.
**Use when:** you know what you want to achieve but not which skills/tools fit.
**Prerequisites:** your goal and an agent that can read this library.

## Ingredients

- **Instructions:** [AGENTS.md](../AGENTS.md) and relevant target-project rules.
- **Skill:** none required to make the selection.
- **Tools and access:** existing capabilities; source access as needed.
- **Harness:** your existing agent client.

## Steps

1. Describe your goal in your own words. Project, client and constraints can
   be supplied when relevant; there is no required intake form.
2. The agent reads the [task routes](../README.md) and one matching recipe.
   It uses known context and asks only about facts that would change the choice.
3. It recommends the smallest setup, distinguishing observed availability
   from missing requirements. New skills/tools need a specific reason.
4. It gives one concrete first step and the expected output.

## Ask an agent

```text
Read AGENTS.md in this repository. I want to [goal].
Recommend what I need and give me one first step.
```

## Optional enhancements and tradeoffs

Use [discovery](../docs/find-more-skills.md) for a genuine gap. Before proposing
installation commands or executing a third-party skill, verify its exact
upstream artifact and [client compatibility](../docs/portability.md).
Recommendation-only requests do not authorize installs or project changes.

## Evidence and checks

The answer has three parts: **Use**, **Need**, **Start**. It links to the recipe
and states material uncertainty without claiming unverified availability,
compatibility or results. Expand the explanation when the user asks.
