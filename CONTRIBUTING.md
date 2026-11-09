# Contributing

Use the [entry template](templates/catalog-entry.md). Verify canonical owner, focused documentation, license, constraints and intended use against primary sources. State scoped recommendations, evidence and uncertainty. Link upstream; never vendor third-party skills, scripts or prompts. Prefer a suitable upstream skill to inventing an original one; propose an original only after documenting a concrete uncovered need. Avoid private or employer-specific information.

Run `python scripts/check_catalog.py` and inspect the diff and changed upstream links. A reachable URL is not compatibility proof. The [MIT license](LICENSE) applies to original repository contributions; upstream projects have their own terms.

For a specific skill recommendation, record the exact upstream skill path and
reviewed revision, license evidence, required tools and relevant side effects.
Reviewing only a collection index supports discovery-level inclusion; it does
not establish the behavior of each skill in that collection. Record local
execution separately with the task, harness, version, checks and outcome.
Use the [quality review](docs/quality-review.md) to prioritize follow-up work.

Concrete recipe choices live in [recipe-skills.json](catalog/recipe-skills.json).
Record the exact skill/documentation revision, `kind` (skill/tool), goals,
categories, programming languages, runtime needs, aliases and scoped evidence.
`language:any` means no particular source-language requirement, not runtime
acceptance for every stack; a CLI runtime is separate. Dutch aliases support
goal-based searches without changing upstream names.
Keep the core recipes usable with briefs, documents, designs, data or code.
Put specialist requirements behind a clear use condition; do not make a
repository, shell, code diff or extra skill a prerequisite for general work.
The renderer omits default `language:any` badges; the filter and metadata keep
that meaning. Explicit programming-language restrictions remain visible.

Run `python scripts/skill_catalog.py build` after index changes; it generates
the [finder](docs/skill-finder.md) and marked upstream tables in recipes.
`python scripts/check_catalog.py` checks metadata and generated-view drift.
For search/generator changes, run `python -m unittest discover -s scripts -p test_skill_catalog.py`.
