# Define a change with a specification

**Outcome:** a reviewable specification with observable acceptance criteria.
**Use when:** a larger change has unclear requirements, several stakeholders
or independently testable capabilities. For a small, clear fix, use the
[minimal workflow](minimal-agent-workflow.md) instead.
**Prerequisites:** the intended outcome, repository context and a human reviewer.

## Ingredients

- **Instructions:** existing specification conventions, project boundaries
  and actual build/test commands.
- **Procedure or toolkit:** use the project's existing system, a Markdown
  procedure such as Addy's skill, or one toolkit from the choices below.
  OpenSpec and Spec Kit are example implementations of SDD, not mandatory
  dependencies of the method. Select one primary workflow.
- **Tools and access:** repository reading and permission to save the spec;
  additional runtime/integration requirements depend on the chosen toolkit.
- **Harness:** your existing client, subject to the skill's review gates.

<!-- recipe-skills:start -->
## Upstream choices

Select only for a matching need and scope. [Tag meanings](../docs/skill-finder.md#tags-and-programming-languages).

| Use when | Skill and source | Tags | Evidence |
| --- | --- | --- | --- |
| Specify a larger or ambiguous change before planning and coding. | [Addy Osmani · /spec-driven-development](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/spec-driven-development/SKILL.md) | `goal:specification` `category:development` `category:product-strategy` | [locally-tested](../docs/evaluations/2026-10-30/README.md): Specification phase only, one synthetic task on 2026-10-30. |
| Use a change-centric SDD toolkit with proposals, specs, design, tasks and archival. | [Fission-AI · OpenSpec (tool)](https://github.com/Fission-AI/OpenSpec/blob/0fa4a9705c20ef1c571fe3ded74435733e4b73a1/README.md) | `goal:specification` `category:development` | [source-reviewed](../catalog/skills/development/openspec.md): README and license reviewed; no local execution or comparative benchmark. |
| Use a maintained SDD toolkit with project principles, specification, plan, tasks and implementation/convergence. | [GitHub · Spec Kit (tool)](https://github.com/github/spec-kit/blob/c43849408ac0de2ca6a52f14eaae71449776057b/README.md) | `goal:specification` `category:development` | [source-reviewed](../catalog/skills/development/spec-kit.md): README and license reviewed; no local execution or comparative benchmark. |
<!-- recipe-skills:end -->

## Steps

1. Preserve an existing spec system before adding one. Surface assumptions and
   open questions. If the request contains several
   independent capabilities, first propose a small capability/dependency map
   for review; a single capability does not need this extra hierarchy.
2. Draft the spec from the repository: objective, scope, boundaries, observable
   acceptance, failure cases and unresolved questions. Record actual project
   commands and testing context; use the chosen workflow's templates.
3. Save it using that system's conventions. OpenSpec organizes change proposals,
   specs, design and tasks in `openspec/`; Spec Kit's documented SDD path starts
   with project principles and proceeds through specification, plan and tasks.
   Consult the pinned source for client-specific commands rather than mixing them.
4. For a spec-only task, summarize and stop for human review. The reviewed Addy workflow
   explicitly ends the turn here, before planning or writing implementation code.
5. After approval, continue through separately reviewed planning, task and
   implementation phases. The local evaluation covers specification drafting
   only; later phases and their helper skills were not evaluated.

## Ask an agent

```text
Use the spec-driven-development recipe to specify [change] in [repository].
Inspect existing conventions, state assumptions and write a reviewable spec
with acceptance criteria and actual check commands. Preserve any existing
specification system. Stop after the specification for review; do not plan
implementation or change application code yet.
```

## Optional enhancements and tradeoffs

A plain Markdown spec can be enough. OpenSpec offers change-oriented artifacts;
[Spec Kit](../catalog/skills/development/spec-kit.md) offers templates and agent
integrations for its SDD process. These are selection cues from documentation,
not a tested ranking. Keep the system the project already uses when it fits.
A spec establishes intended behavior; implementation still needs verification.

## Evidence and checks

The spec links requirements to acceptance and identifies assumptions and
unknowns. Check command names against the project. See the
[pinned evaluation](../docs/evaluations/2026-10-30/README.md) for the single
synthetic specification task; it does not establish downstream correctness.
