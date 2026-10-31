# Contributing

Use the [entry template](templates/catalog-entry.md). Verify canonical owner, focused documentation, license, constraints and intended use against primary sources. State scoped recommendations, evidence and uncertainty. Link upstream; never vendor third-party skills, scripts or prompts. Prefer a suitable upstream skill to inventing an original one; propose an original only after documenting a concrete uncovered need. Avoid private or employer-specific information.

Run `python scripts/check_catalog.py` and inspect the diff and changed upstream links. A reachable URL is not compatibility proof. The [MIT license](LICENSE) applies to original repository contributions; upstream projects have their own terms.

For a specific skill recommendation, record the exact upstream skill path and
reviewed revision, license evidence, required tools and relevant side effects.
Reviewing only a collection index supports discovery-level inclusion; it does
not establish the behavior of each skill in that collection. Record local
execution separately with the task, harness, version, checks and outcome.
Use the [quality review](docs/quality-review.md) to prioritize follow-up work.
