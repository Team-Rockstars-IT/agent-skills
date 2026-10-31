# TokenTelemetry

- **ID:** tokentelemetry
- **Type:** observability tool
- **Primary category:** observability
- **Tags:** observability, agent-assisted-work
- **Upstream:** [TokenTelemetry](https://github.com/VasiHemanth/tokentelemetry)
- **Recommendation:** situational — for understanding supported agent usage.
- **Evidence:** source-reviewed; not locally tested.
- **Lifecycle:** unknown; check current upstream activity.
- **Last reviewed:** 2026-10-30
- **License:** MIT; check current upstream terms.

## Purpose and output

inspects local agent sessions and usage.

## Use or skip

Use for understanding supported agent usage. Skip for assuming logs prove quality or actual billing.

## Requirements and tradeoffs

Supports Codex, Claude Code, Hermes and others; check current upstream. Upstream says usage data stays local; anonymous telemetry is enabled by default and update checks can make outbound calls. Both can be disabled. Token and cost impact is unmeasured here.

## Obtain and maintain

Follow current [upstream instructions](https://github.com/VasiHemanth/tokentelemetry), reviewing permissions and compatibility. Prefer a compatible stable release; optionally pin a reviewed version or commit in consuming projects.

## Related

[Selection and conflicts](../../../docs/selection-guide.md) · [Evaluation](../../../docs/evaluation.md) · [Recipes](../../../recipes/README.md)
