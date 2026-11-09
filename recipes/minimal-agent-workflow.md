# Minimal agent workflow

**Outcome:** a bounded change with evidence. **Prerequisites:** repository access, instructions and authority.

**Use when:** the desired behavior and scope can fit a small change. For an
unclear task, first use [Choose your setup](choose-your-setup.md).

## Ingredients

- **Instructions:** the target project's conventions and documented checks.
- **Skill:** [define-work](../define-work/SKILL.md) if the task needs bounding;
  [TDD](../catalog/skills/development/matt-pocock.md) for explicit test-first
  work. Existing instructions can suffice for a simple, clear task.
- **Tools and access:** file editing, a shell and the project's relevant checks.
- **Harness:** your existing agent client with authorized project access.

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
