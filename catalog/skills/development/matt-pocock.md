# Matt Pocock engineering skills

- **ID:** matt-pocock
- **Type:** skill collection
- **Primary category:** development
- **Tags:** development, agent-assisted-work
- **Upstream:** [Matt Pocock engineering skills](https://github.com/mattpocock/skills)
- **Recommendation:** recommended-for-focused-engineering-workflows — for focused test-first or reproduce-first work.
- **Evidence:** locally-tested for the pinned TDD skill on one synthetic task; other collection skills remain source-reviewed only. See [evaluation](../../../docs/evaluations/2026-10-30/README.md).
- **Lifecycle:** unknown; check current upstream activity.
- **Last reviewed:** 2026-11-09
- **License:** MIT; check current upstream terms.

## Purpose and output

TDD, diagnosis, planning, research and review workflows.

Start with [TDD](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md) for behavioral tests, [diagnosing bugs](https://github.com/mattpocock/skills/blob/main/skills/engineering/diagnosing-bugs/SKILL.md) for difficult failures, or [research](https://github.com/mattpocock/skills/blob/main/skills/engineering/research/SKILL.md) for a cited investigation. The evaluated TDD revision asks for agreed test seams and places refactoring in review; inspect the selected revision and reconcile it with the task's instructions.

## Use or skip

Use for focused test-first or reproduce-first work. Skip for trivial changes.

## Concrete choices reviewed on 2026-11-09

The [focused finder](../../../docs/skill-finder.md) links exact revisions for
`tdd`, `diagnosing-bugs`, `research`, `improve-codebase-architecture` and
`retro`. The prior TDD fixture result applies only to its pinned 2026-10-30
evaluation revision, not the complete collection or a new upstream version.
The newly inspected workflows have source-review evidence only.

- `diagnosing-bugs`: create a runnable reproduction/feedback loop before the fix.
- `research`: requires a background agent and writes cited findings to Markdown.
- `improve-codebase-architecture`: deliberate user invocation, helper skills and
  a fresh subagent; creates an HTML report with CDN assets, then an interactive
  follow-up that can update the glossary and decision records. The main skill
  was inspected; its complete helper chain was not reviewed or executed.
- [`retro`](matt-pocock-retro.md): explicitly review a session for environment
  improvements; depends on `writing-for-agents` and session evidence.

Current source reviews use commit
[`4ae2317d`](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d).
Follow the relevant recipe's exact link for the source supporting its label.

## Requirements and tradeoffs

Model-neutral per upstream; individual skills may require subagents or trackers. Choose individual skills, not the whole workflow by default. Token and cost impact is unmeasured here.

## Obtain and maintain

Follow current [upstream instructions](https://github.com/mattpocock/skills), reviewing permissions and compatibility. Prefer a compatible stable release; optionally pin a reviewed version or commit in consuming projects.

## Related

[Selection and conflicts](../../../docs/selection-guide.md) · [Evaluation](../../../docs/evaluation.md) · [Recipes](../../../recipes/README.md)
