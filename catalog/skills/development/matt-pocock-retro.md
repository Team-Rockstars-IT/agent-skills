# Matt Pocock: retro

- **ID:** matt-pocock-retro
- **Type:** skill
- **Primary category:** development
- **Tags:** retrospective, agent-environment, workflow-improvement, feedback
- **Upstream:** [retro SKILL.md at the reviewed revision](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/retro/SKILL.md)
- **Recommendation:** situational — after session friction worth addressing in the agent environment.
- **Evidence:** source-reviewed on 2026-11-09: exact SKILL.md, writing-for-agents dependency, collection README and MIT license; no local execution or measured benefit.
- **Lifecycle:** unknown; check current upstream activity before adoption.
- **Last reviewed:** 2026-11-09
- **License:** [MIT at the reviewed revision](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/LICENSE).

## Purpose and output

Uses session evidence to propose improvements to the coding agent's working
environment. Output is a severity-ordered set of candidates covering file
navigation, automated checks, coding/review guidance, steering files, tool
economy and information access.

## Use or skip

Use after repeated corrections, navigation problems, missing feedback or costly
tool calls. For example, repeated searches for an undocumented entry point may
justify a navigation pointer; a recurring mechanical error may justify a check.
These are examples of candidate improvements, not observed effectiveness.
Skip when no meaningful session evidence exists. This is not a general
personal-coaching or team-retrospective skill.

## Requirements and tradeoffs

The reviewed file sets `disable-model-invocation: true`: this is a deliberate
user-invoked workflow. It depends on
[writing-for-agents](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/writing-for-agents/SKILL.md)
and access to the specified session's primary sources, potentially local logs.
It defaults to the current session when unspecified. Treat session data as
sensitive and keep access within the task's authority.

The instruction file imposes no particular programming language. That is the
meaning of `language:any` in the [finder](../../../docs/skill-finder.md), not a
claim of runtime verification for every stack. Changes suggested by the retro
still need their own authorized scope. Costs and benefits are unmeasured here.

## Obtain and maintain

Follow the [canonical collection](https://github.com/mattpocock/skills) and
inspect the exact skill and dependency before enabling them. Slash-command
discovery and invocation depend on installation and client support.

## Related

[Session retro recipe](../../../recipes/session-retrospective.md) ·
[Collection entry](matt-pocock.md) · [Selection guide](../../../docs/selection-guide.md)
