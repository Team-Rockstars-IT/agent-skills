# Choose skills and tools for your task

**Outcome:** a small, justified setup and a concrete first step.
**Use when:** you know the work you want to do but not which recipe, skill or
tool fits. This recipe applies across disciplines.
**Prerequisites:** a desired result and an agent that can read this library.

## Ingredients

- **Instructions:** this library's [AGENTS.md](../AGENTS.md) guides selection;
  the target project's own instructions govern work in that project.
- **Skill:** none required for selection. Read relevant catalog entries first.
- **Tools and access:** repository or supplied document access as needed;
  access to current upstream documentation before installation advice.
- **Harness:** your existing agent client; discovery and execution support
  must be checked in that client. No orchestrator is required.

## Steps

1. State the result you need: a change, assessment, design, report or handover.
   Include your experience and any time, privacy, budget or access constraints.
2. Establish the target environment and existing capabilities. Identify a
   missing fact only if it could change the recommendation.
3. Follow the [decision tree](../docs/start-here.md#decision-tree) and read one
   primary recipe. For specialist work, use the
   [review recipe](specialist-review.md) to select a focused discipline.
4. List the minimum ingredients. Add a skill for a useful repeatable procedure;
   add a tool only for an action or information source the agent lacks.
   Separate already available, required to obtain and optional components.
5. Read the linked catalog evidence and constraints. Before installation or
   execution, verify the exact upstream artifact and harness support using
   [portability guidance](../docs/portability.md).
6. Give one first action with an expected output. When the user asks for
   advice, return advice; installation and execution require their own scope.

## Ask an agent

```text
Read AGENTS.md in the Team Rockstars agent-skills repository and help me
choose a recipe for my work.

Goal/output: [what I need]
Project or source material: [path, link or description]
Agent client and existing tools: [what I use, or unknown]
Experience and constraints: [what matters]

Recommend one primary recipe and the minimum skills/tools. Separate what is
already available from what I would need to obtain. Explain optional additions,
evidence and limitations, and give me a concrete first step. Do not install
anything or change my project as part of this recommendation.
```

## Optional enhancements and tradeoffs

Use [discovery](../docs/find-more-skills.md) if the catalog has a genuine gap.
A simple task can need no extra skill. More installed components add setup,
overlap and maintenance; identify the benefit before adding them.

## Evidence and checks

The recommendation names the intended output, one primary recipe, required
capabilities, availability and unresolved assumptions. Each selected component
links to a local entry or original skill. Historical evidence retains its date
and scope; unverified compatibility remains explicit.
