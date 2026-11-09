# Improve the agent environment after a session

**Outcome:** a short, prioritized list of changes that could make the next run easier.
**Use when:** a session involved repeated corrections, hard-to-find context,
missing checks or expensive tool calls. Skip a routine retro when there is no
useful session evidence or recurring friction.
**Prerequisites:** the relevant session history and access to the project context.

## Ingredients

- **Instructions:** project rules and the boundaries for reading session logs.
- **Skill:** Matt Pocock's `retro`, explicitly invoked when installed and
  supported by your client; its `writing-for-agents` reference is also needed.
- **Tools and access:** the specified session's primary evidence and repository
  files. Use only logs within the authorized scope; redact sensitive material.
- **Harness:** a client that can load the selected skill and its dependency.

<!-- recipe-skills:start -->
## Upstream choices

Select only for a matching need and scope. [Tag meanings](../docs/skill-finder.md#tags-and-programming-languages).

| Use when | Skill and source | Tags | Evidence |
| --- | --- | --- | --- |
| After session friction, identify improvements to navigation, checks, steering files or tools. | [Matt Pocock · /retro](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/retro/SKILL.md) | `goal:retrospective` `goal:workflow-improvement` `category:development` `category:personal-development` | [source-reviewed](../catalog/skills/development/matt-pocock-retro.md): retro, writing-for-agents, README and license reviewed; no local execution. |
<!-- recipe-skills:end -->

## Steps

1. Name the session to inspect; the upstream defaults to the current session.
2. Find concrete friction: navigation, automated checks, review rules,
   oversized steering files, tool economy or missing information access.
3. Connect each candidate improvement to an observed event and an existing
   convention or check. Avoid proposing a second tool/check for one already present.
4. Return candidates in severity order. Separate deterministic checks from
   judgment-based review guidance; do not expand `AGENTS.md` for every incident.
5. Select a worthwhile improvement for a separate authorized change and define
   how a later run would show whether it helped.

## Ask an agent

```text
Use Matt Pocock's retro workflow to review [this session/session reference].
Which changes to context, navigation, checks or tools would help the next run?
Use session evidence, prioritize the findings and propose at most three useful
actions. This request is for recommendations; do not apply fixes or install tools.
```

## Optional enhancements and tradeoffs

For a measured cost problem, follow the
[token-efficient workflow](token-efficient-workflow.md). Retro is about the
coding agent's environment, not a general personal or team retrospective.
`/retro` is upstream naming, not a promise that every client exposes that command.

## Evidence and checks

Findings cite session events and project files; proposed benefits remain
hypotheses until checked in a later run. The linked revision is source-reviewed,
not locally executed here. See the [catalog entry](../catalog/skills/development/matt-pocock-retro.md).
