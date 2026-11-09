# Minimal agent workflow

**Outcome:** a bounded change with evidence. **Prerequisites:** repository access, instructions and authority.

**Use when:** the desired behavior and scope can fit a small change. For an
unclear task, first use [Choose your setup](choose-your-setup.md).
For a larger change needing an agreed specification, use the
[SDD recipe](spec-driven-development.md).

## Ingredients

- **Instructions:** the target project's conventions and documented checks.
- **Skill:** [define-work](../define-work/SKILL.md) if the task needs bounding;
  [TDD](../catalog/skills/development/matt-pocock.md) for explicit test-first
  work. Existing instructions can suffice for a simple, clear task.
- **Tools and access:** file editing, a shell and the project's relevant checks.
- **Harness:** your existing agent client with authorized project access.

<!-- recipe-skills:start -->
## Upstream choices

Choose one when it fits; these are optional choices, not an install bundle. [Tag meanings](../docs/skill-finder.md#tags-and-programming-languages).

| Use when | Skill and source | Tags | Evidence |
| --- | --- | --- | --- |
| Implement behavior test-first at agreed public interfaces. | [Matt Pocock · /tdd](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/tdd/SKILL.md) | `goal:testing` `category:development` `language:any` | [locally-tested](../docs/evaluations/2026-10-30/README.md): One synthetic TDD task on 2026-10-30; this pinned revision only. |
| Investigate a difficult bug or performance regression with a repeatable feedback loop. | [Matt Pocock · /diagnosing-bugs](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/diagnosing-bugs/SKILL.md) | `goal:debugging` `category:development` `language:any` | [source-reviewed](../catalog/skills/development/matt-pocock.md): Exact instruction file reviewed; not locally executed. |
| Specify a larger or ambiguous change before planning and coding. | [Addy Osmani · /spec-driven-development](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/spec-driven-development/SKILL.md) | `goal:specification` `category:development` `category:product-strategy` `language:any` | [locally-tested](../docs/evaluations/2026-10-30/README.md): Specification phase only, one synthetic task on 2026-10-30. |
<!-- recipe-skills:end -->

## Steps

1. Read relevant instructions and state observable acceptance.
2. Choose a relevant procedure only where it helps; avoid overlapping planning workflows.
3. Implement and run appropriate deterministic checks; inspect failures.
4. Report actual results and limitations.

## Ask an agent

```text
Use the minimal-agent-workflow recipe to [change] in [repository]. Read its
instructions, identify acceptance and actual checks, implement within [scope],
then report the diff, check results and remaining gaps. Use existing tools
unless a missing capability prevents the work.
```

## Optional enhancements and tradeoffs

Use the [readiness recipe](repository-readiness.md) when missing context is a
real obstacle. A comprehensive assessment adds time and has documented write
and probe effects; it is not a prerequisite for every change.

## Evidence and checks

Actual checks, the diff and unmet acceptance criteria. Tests should verify
meaningful behavior; choose verification appropriate to the change.
