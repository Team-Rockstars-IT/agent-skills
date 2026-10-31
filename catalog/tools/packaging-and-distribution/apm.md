# Agent Package Manager

- **ID:** apm
- **Type:** package manager
- **Primary category:** packaging-and-distribution
- **Tags:** packaging-and-distribution, agent-assisted-work
- **Upstream:** [Agent Package Manager](https://github.com/microsoft/apm)
- **Recommendation:** candidate — for repeatable project dependency distribution.
- **Evidence:** source-reviewed; not locally tested.
- **Lifecycle:** unknown; check current upstream activity.
- **Last reviewed:** 2026-10-30
- **License:** See upstream license; check current upstream terms.

## Purpose and output

optional distribution of agent configuration and dependencies.

## Use or skip

Use for repeatable project dependency distribution. Skip for small projects where direct reviewed retrieval suffices.

## Requirements and tradeoffs

Check current CLI and agent integrations. Adds dependency and update management; optional for this catalog. Token and cost impact is unmeasured here.

## Obtain and maintain

Follow current [upstream instructions](https://github.com/microsoft/apm), reviewing permissions and compatibility. Prefer a compatible stable release; optionally pin a reviewed version or commit in consuming projects.

## Related

[Selection and conflicts](../../../docs/selection-guide.md) · [Evaluation](../../../docs/evaluation.md) · [Recipes](../../../recipes/README.md)
