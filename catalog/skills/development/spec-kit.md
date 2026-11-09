# GitHub Spec Kit

- **ID:** spec-kit
- **Type:** specification workflow tool
- **Primary category:** development
- **Tags:** specification, sdd, workflow, templates, language-any
- **Upstream:** [Spec Kit README at the reviewed revision](https://github.com/github/spec-kit/blob/c43849408ac0de2ca6a52f14eaae71449776057b/README.md)
- **Recommendation:** situational — a concrete SDD implementation when its templates, agent integration and workflow fit the project.
- **Evidence:** source-reviewed on 2026-11-09: README, CLI package metadata and license; no local installation, execution or comparison benchmark.
- **Lifecycle:** unknown; verify the current release before adoption.
- **Last reviewed:** 2026-11-09
- **License:** [MIT at the reviewed revision](https://github.com/github/spec-kit/blob/c43849408ac0de2ca6a52f14eaae71449776057b/LICENSE).

## Purpose and output

Provides the Specify CLI, agent integrations, templates and processes. Its
documented SDD path creates project principles, a specification, plan and tasks,
then implementation and convergence records. Review results before continuing.
It also offers other processes; selecting SDD does not require adopting them.

## Use or skip

Consider it when a team wants a maintained toolkit for the specification
lifecycle and is willing to maintain the resulting project artifacts. Compare
with [OpenSpec](openspec.md), or a plain Markdown spec for a smaller need.
Keep an existing specification system when it already fits; do not install
both just to follow this library's recipe.

## Requirements and tradeoffs

The reviewed README requires Python 3.11+, uv and a supported coding agent;
the [CLI metadata](https://github.com/github/spec-kit/blob/c43849408ac0de2ca6a52f14eaae71449776057b/pyproject.toml)
confirms Python >=3.11. These are tooling runtimes, not a requirement that the
target application use Python. `specify init` creates project files and agent
integration material; later phases generate artifacts and application changes.
Invocation syntax depends on the selected integration. Community components
need their own review. Client compatibility and costs are unverified here.

## Obtain and maintain

Read the pinned README and follow the current
[canonical project](https://github.com/github/spec-kit) for installation and
upgrade guidance. Select a supported release and integration. This catalog
does not install Spec Kit or copy its templates.

## Related

[SDD recipe](../../../recipes/spec-driven-development.md) ·
[OpenSpec](openspec.md) · [Focused finder](../../../docs/skill-finder.md)
