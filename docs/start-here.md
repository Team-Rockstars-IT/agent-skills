# Find a recipe

The [README](../README.md) is the short starting point. Use this tree if you
prefer a visual route; you do not need to choose an experience level first.

## Decision tree

```mermaid
flowchart TD
    A{What do you want to do?}
    A -->|Clarify an outcome| B[Clarify what you need]
    A -->|Research or weigh options| C[Research and compare]
    A -->|Make or improve something| D[Work in small steps]
    A -->|Review or hand over a result| E[Review and deliver]
```

Open the matching [recipe](../recipes/README.md). Each contains ingredients,
steps, a copyable prompt and the expected evidence.
Inputs can be briefs, documents, designs, data or code. The artifact determines
the checks and tool needs; no role, sector or programming-language pack is required.

## Ask your agent to help choose

Describe your goal and ask the agent to read [AGENTS.md](../AGENTS.md).
It should recommend a recipe, identify anything missing and give one first
step. The [selection recipe](../recipes/choose-your-setup.md) explains the
process. Point to the file explicitly if your client does not discover it.

## Specialist context, when needed

For a software repository, consider [readiness](../recipes/repository-readiness.md)
or [SDD](../recipes/spec-driven-development.md) when that specific need arises.

Only explore more tooling when you can name a problem:

- Cost or context volume: [token-efficient workflow](../recipes/token-efficient-workflow.md).
- Coordination of separable tasks: [orchestration selection](../recipes/orchestration-selection.md).
- Recurring session friction: [session retrospective](../recipes/session-retrospective.md).

For ingredient details, browse the [catalog](../catalog/README.md). The
[selection guide](selection-guide.md) explains the layers and conflicts;
[dated evaluations](evaluations/2026-10-30/README.md) record what was actually
tested. These details are available when needed, not prerequisites to start.
