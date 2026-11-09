# Assess a repository before agentic work

**Outcome:** evidence of what an agent can work with and a prioritized list of
gaps before undertaking a task.
**Use when:** onboarding an unfamiliar repository or investigating why agent
work repeatedly stalls.
**Prerequisites:** access to the target repository and a clear assessment scope.

## Ingredients

- **Instructions:** the target repository's instructions and documented checks.
- **Skill:** none required for a lightweight context check. For a deliberate
  comprehensive audit, inspect the
  [Exadel Agentic Readiness Assessment](../catalog/skills/development/agentic-readiness-assessment.md).
  Its implementation stays upstream; this library contains the reference and
  a dated evaluation, not an installed scanner.
- **Tools and access:** file search and reading; a shell and project runtimes
  if running checks is authorized. The evaluated comprehensive workflow also
  uses a Python report validator.
- **Harness:** a client compatible with the selected upstream instructions;
  check actual access and execution support before starting.

<!-- recipe-skills:start -->
## Upstream choices

Choose one when it fits; these are optional choices, not an install bundle. [Tag meanings](../docs/skill-finder.md#tags-and-programming-languages).

| Use when | Skill and source | Tags | Evidence |
| --- | --- | --- | --- |
| Run a deliberate comprehensive repository-readiness assessment. | [Exadel · /agentic-readiness-assessment](https://github.com/exadel-inc/agentic-readiness-assessment/blob/1313702ad53e2f2c069e2f4ef2dbebd19cb17e3d/skills/agentic-readiness-assessment/SKILL.md) | `goal:readiness` `category:development` `language:any` | [locally-tested](../docs/evaluations/2026-10-30/README.md): One synthetic repository on 2026-10-30; validator run separately by evaluator. |
<!-- recipe-skills:end -->

## Steps

1. Choose the scope. A lightweight check reads existing instructions, entry
   points, architecture boundaries and documented build/test commands. It
   reports evidence and unknowns without a numeric score or probe edit.
2. If a comprehensive scorecard is useful, review the exact upstream skill,
   references and effects first. The reviewed version writes a report, runs
   checks and includes a reversible probe. Agree permitted commands, output
   path and probe scope before executing it; existing authorization can cover
   these actions.
3. Record observed facts with file locations and actual command results.
   Distinguish missing evidence from failed checks and confirmed gaps.
4. Return a prioritized backlog tied to the intended work. An assessment
   identifies gaps; remediation is a separate task.
5. If project instructions are missing, use
   [agents-md](../agents-md/SKILL.md) to draft them from the observed repository.

## Ask an agent

```text
Use the repository-readiness recipe for [repository path]. Start with a
lightweight, read-only context check: instructions, structure, boundaries,
documented checks and missing context for [intended task]. Report evidence,
unknowns and the three most useful next actions. Do not edit files, run project
commands or install anything. Explain whether a comprehensive upstream
assessment would add useful evidence and what access it would need.
```

## Optional enhancements and tradeoffs

The [2026-10-30 evaluation](../docs/evaluations/2026-10-30/README.md) keeps
Exadel's assessment optional: the reviewed version has a substantial scorecard,
validator and required commercial closing link. Recheck the current upstream
before adoption. Neither scope establishes security or production readiness.

## Evidence and checks

Deliver file-backed observations, commands actually run (or explicitly none),
assessment limits and an actionable backlog. For a comprehensive run, also
record the upstream revision, report validation and restoration of any probe.
Do not reuse a fixture's score as the target repository's score.
