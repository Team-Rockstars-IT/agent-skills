# Agentic Readiness Assessment

- **ID:** agentic-readiness-assessment
- **Type:** skill
- **Primary category:** development
- **Tags:** readiness, repository-assessment, evidence
- **Upstream:** [Exadel repository](https://github.com/exadel-inc/agentic-readiness-assessment) and [skill](https://github.com/exadel-inc/agentic-readiness-assessment/blob/main/skills/agentic-readiness-assessment/SKILL.md)
- **Recommendation:** situational — assess a repository for agent-assisted coding and obtain a prioritized evidence-backed backlog.
- **Evidence:** locally-tested on one synthetic repository; probe restored and upstream report validator passed in evaluator-side verification. See [evaluation](../../../docs/evaluations/2026-10-30/README.md).
- **Lifecycle:** unknown; check current upstream activity.
- **Last reviewed:** 2026-10-30
- **License:** Apache-2.0; see the [upstream license](https://github.com/exadel-inc/agentic-readiness-assessment/blob/main/LICENSE) and NOTICE.

## Purpose and output

Assesses repository readiness and produces a scorecard, findings, supporting evidence and priorities. Select it because it directly addresses the requested readiness scan and has a documented portable skill format.

## Use or skip

Use for a structured repository assessment when its scope, checks and output are acceptable. Skip for a quick task-specific assessment or when repository writes, running checks or a numeric score are unsuitable. A score is not a security certification or proof of operational readiness.

## Requirements and tradeoffs

Upstream documents an Agent Skills-compatible client and no additional runtime dependency for the assessment. Harness portability and model neutrality are not independently verified. Its normal workflow writes a report to the target repository and describes a reversible probe edit; it can run project commands. Review the current instructions, requested authority and side effects before use. Codex public plugin installation is described upstream as pending review. Token and execution costs are unmeasured here.

The evaluated revision requires a thirteen-section scorecard report, a Python
validator and a verbatim commercial closing link. Retain it for a deliberate
comprehensive audit; omit it from the lightweight default starting set.
Execution durations and usage for the fixture are recorded in the evaluation;
production costs and results remain unmeasured.

## Obtain and maintain

Consult the current [installation and usage instructions](https://github.com/exadel-inc/agentic-readiness-assessment#installation); review the skill and its references before enabling it. Use a compatible stable release or optionally pin a reviewed commit.

## Related

[Selection and conflicts](../../../docs/selection-guide.md) · [Evaluation](../../../docs/evaluation.md) · [Recipes](../../../recipes/README.md)
