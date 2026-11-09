# Make or improve something

**Outcome:** a bounded result checked against the intended outcome.
**Use when:** creating or improving a document, design, analysis, process or code.
**Input:** the desired change, relevant material, constraints and authority to act.

## Ingredients

- Applicable instructions and the smallest set of sources needed for the task.
- Existing tools that can produce and check the artifact. A repository, shell,
  test framework or additional skill is needed only if the actual work requires it.

## Steps

1. State the expected result and an observable acceptance check. For unclear
   intent, first [clarify the task](choose-your-setup.md).
2. Inspect the relevant material and identify boundaries that the change must preserve.
3. Make one useful, bounded improvement at a time.
4. Check it using evidence appropriate to the artifact: source consistency,
   calculations, a scenario walkthrough, human feedback or executable tests.
5. Report what changed, the actual check outcomes and remaining uncertainty.

## Ask an agent

```text
Create or improve [artifact] using [supplied material], within [scope].
Identify the intended result and how to check it. Work in small steps, preserve
the relevant constraints and report actual checks and remaining gaps.
```

## Optional enhancements and tradeoffs

For software work, [define-work](../define-work/SKILL.md) can bound a coding
task; TDD and bug diagnosis fit their specific triggers. Use the
[SDD recipe](spec-driven-development.md) when a larger software change needs
durable specifications. [Repository readiness](repository-readiness.md) is
useful when missing repository context blocks the task.

<!-- recipe-skills:start -->
<details>
<summary>Optional specialist workflows</summary>

## Upstream choices

Select only for a matching need and scope. [Tag meanings](../docs/skill-finder.md#tags-and-programming-languages).

| Use when | Skill and source | Tags | Evidence |
| --- | --- | --- | --- |
| Implement behavior test-first at agreed public interfaces. | [Matt Pocock · /tdd](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/tdd/SKILL.md) | `goal:testing` `category:development` | [locally-tested](../docs/evaluations/2026-10-30/README.md): One synthetic TDD task on 2026-10-30; this pinned revision only. |
| Investigate a difficult bug or performance regression with a repeatable feedback loop. | [Matt Pocock · /diagnosing-bugs](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/diagnosing-bugs/SKILL.md) | `goal:debugging` `category:development` | [source-reviewed](../catalog/skills/development/matt-pocock.md): Exact instruction file reviewed; not locally executed. |
| Specify a larger or ambiguous change before planning and coding. | [Addy Osmani · /spec-driven-development](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/spec-driven-development/SKILL.md) | `goal:specification` `category:development` `category:product-strategy` | [locally-tested](../docs/evaluations/2026-10-30/README.md): Specification phase only, one synthetic task on 2026-10-30. |

</details>
<!-- recipe-skills:end -->

## Evidence and checks

Choose checks that can detect a wrong result. Keep reviewed, calculated, tested
and unverified outcomes distinct. A plausible draft alone does not establish
user acceptance or operational success.
