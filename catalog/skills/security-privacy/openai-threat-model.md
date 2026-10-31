# OpenAI security threat model

- **ID:** openai-threat-model
- **Type:** skill
- **Primary category:** security-privacy
- **Tags:** security-privacy, skills, source-reviewed
- **Upstream:** [OpenAI security threat model](https://github.com/openai/skills/blob/main/skills/.curated/security-threat-model/SKILL.md)
- **Recommendation:** recommended-for-explicit-appsec-threat-modeling — with context validation and expert review.
- **Evidence:** locally-tested with a check-in and scripted follow-up on one synthetic code fixture; no exploitability tests. See [evaluation](../../../docs/evaluations/2026-10-30/README.md).
- **Lifecycle:** unknown; check current upstream activity.
- **Last reviewed:** 2026-10-30
- **License:** Apache-2.0, verified in the [individual skill license at the evaluated commit](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model/LICENSE.txt).

## Purpose and output

repository-grounded threat modeling.

## Use or skip

Use for explicit security threat modeling. Skip for general architecture review or proof of security.

## Requirements and tradeoffs

Codex-oriented; verify target harness and individual skill license. Threat models require security expertise and do not replace testing. Token and cost impact is unmeasured here.

## Obtain and maintain

Consult the current [upstream instructions](https://github.com/openai/skills/blob/main/skills/.curated/security-threat-model/SKILL.md) and inspect individual skill instructions, data access, dependencies and license before use. Select only relevant skills and optionally pin a reviewed version in the consuming project.

## Related

[Selection report](../../../docs/skill-selection-report.md) · [Selection guide](../../../docs/selection-guide.md) · [Evaluation](../../../docs/evaluation.md)
