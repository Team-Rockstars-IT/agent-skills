# skills.sh and the skills CLI

- **ID:** skills-sh
- **Type:** discovery directory and optional CLI
- **Primary category:** context-and-retrieval
- **Tags:** discovery, skills, directory, find-skills
- **Upstream:** [skills.sh directory](https://skills.sh/), [CLI repository](https://github.com/vercel-labs/skills) and [find-skills skill](https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md)
- **Recommendation:** recommended-for-discovering-public-skills — search by capability, then assess the actual upstream.
- **Evidence:** source-reviewed; not locally tested.
- **Lifecycle:** unknown; check current upstream activity.
- **Last reviewed:** 2026-10-30
- **License:** [CLI repository is MIT](https://github.com/vercel-labs/skills#license); each discovered skill has its own terms. Directory terms are not assessed.

## Purpose and output

The directory helps discover public agent skills; the separate CLI supports finding and installing skills. The upstream also publishes a find-skills skill. Use discovery to produce a shortlist, not to endorse or install every result.

## Use or skip

Use when an existing catalog entry does not cover a particular task. Skip additional discovery when a suitable, reviewed skill is already available. Search and popularity rankings do not establish provenance, trustworthiness, maintained status or fitness for a task.

## Requirements and tradeoffs

The directory is a website; the CLI has its own runtime and network requirements, and installation changes agent configuration. [Upstream documents anonymous CLI telemetry and security-audit requests](https://github.com/vercel-labs/skills#telemetry), including options to disable them. Find-skills is a skill, the directory is a discovery service, and the CLI is a tool; these are not interchangeable. Model and harness compatibility depend on the candidate. Costs and behavior are not measured here.

## Obtain and maintain

Browse the [directory](https://skills.sh/) and follow candidates to their canonical source and exact skill path. Inspect skill instructions, supporting scripts, permissions, outbound connections, license, compatibility and overlap before adoption. Review [current CLI documentation](https://github.com/vercel-labs/skills) before any execution. Installing or updating is optional; a consuming project can pin a reviewed version.

## Related

[Find more skills](../../../docs/find-more-skills.md) · [Awesome Copilot](../../skills/development/awesome-copilot.md) · [Selection guide](../../../docs/selection-guide.md)
