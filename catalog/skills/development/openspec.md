# OpenSpec

- **ID:** openspec
- **Type:** specification workflow tool
- **Primary category:** development
- **Tags:** specification, sdd, workflow, change-management, language-any
- **Upstream:** [OpenSpec README at the reviewed revision](https://github.com/Fission-AI/OpenSpec/blob/0fa4a9705c20ef1c571fe3ded74435733e4b73a1/README.md)
- **Recommendation:** situational — for complex changes requiring shared specifications.
- **Evidence:** source-reviewed on 2026-11-09: README and MIT license; not locally installed, executed or benchmarked here.
- **Lifecycle:** unknown; check current upstream activity.
- **Last reviewed:** 2026-11-09
- **License:** [MIT at the reviewed revision](https://github.com/Fission-AI/OpenSpec/blob/0fa4a9705c20ef1c571fe3ded74435733e4b73a1/LICENSE).

## Purpose and output

Organizes change artifacts in `openspec/`: proposal, requirements/scenarios,
design and tasks, followed by implementation and archival into maintained
specifications. The documented process supports iteration between artifacts.

## Use or skip

Use for complex changes requiring shared specifications. Skip for small well-understood edits.

## Requirements and tradeoffs

CLI and a supported coding assistant. The reviewed README offers standalone
installation and package-manager routes; its npm route requires Node.js
22.12.0 or higher. That runtime does not make the target application
JavaScript-specific. Initialization and updates write project/agent files;
implementation changes the application. Command spellings vary by assistant.
The README documents opt-out usage telemetry; review that policy before use.
Specifications require maintenance and behavioral verification. Token/cost
impact and client compatibility are unmeasured here.

## Obtain and maintain

Follow current [upstream instructions](https://github.com/Fission-AI/OpenSpec), reviewing permissions and compatibility. Prefer a compatible stable release; optionally pin a reviewed version or commit in consuming projects.

## Related

[SDD recipe](../../../recipes/spec-driven-development.md) · [Spec Kit](spec-kit.md) · [Selection and conflicts](../../../docs/selection-guide.md)
