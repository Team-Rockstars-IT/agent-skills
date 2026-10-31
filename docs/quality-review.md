# Quality review and next delivery

**Review date:** 2026-10-30. **Verdict:** usable as a discovery library;
not yet a validated recommended skill pack. This is a maintainer self-review,
including a small fresh upstream sample, not an independent audit.

**Follow-up completed:** the [six-choice evaluation](evaluations/2026-10-30/README.md)
adds pinned sources, license evidence, baseline comparisons and resulting
recommendations. The findings below describe the earlier review baseline;
they do not mean those six choices remain completely untested. Broader
catalog validation, automatic activation and production acceptance remain open.

## Findings

| Priority | Finding and evidence | Consequence | Resolution / next action |
| --- | --- | --- | --- |
| P1 | Most rows in the [selection report](skill-selection-report.md) link to parent collection entries; per-skill revision, license and requirements are incomplete. | Readers cannot infer that an individual skill's complete workflow was reviewed. | Keep discovery-level status visible. Review exact skill files for a small starting set before promoting them. |
| P1 | No local behavioral evaluations are recorded; the [evaluation worksheet](evaluation.md) is blank. | Successful Markdown checks do not demonstrate skill effectiveness, activation, safe side effects or harness compatibility. | Evaluate the starting set with representative tasks in an authorized isolated environment. Record failures and compare with a no-skill baseline. |
| P2 | The README led with the original Claude Code skills and presented discovery behavior as universal. | The public library's scope and installation expectations were unclear. | Fixed: lead with the reference library, retain the original skills in a separate section, scope installation to those skills and remove unsupported watcher/restart claims. |
| P2 | Seven discipline tables labeled scope words such as general or web as limitations. | The column obscured actual constraints and exaggerated technology neutrality. | Fixed: relabel as Scope and explain that it is a domain label, not a portability claim. |
| P2 | Forty-two selection rows include analytics twice across disciplines. | Reporting 42 distinct skills would overstate breadth. | Fixed: report 42 rows / 41 distinct source-and-skill pairs and explain the cross-listing. |
| P2 | All catalog lifecycles are unknown and several licenses remain unspecified. | A review date alone cannot establish maintenance health or permitted adoption. | Resolve exact license and lifecycle evidence for the starting set. Preserve unknown elsewhere until reviewed; do not auto-promote. |
| P2 | Local checks originally validated structure and file targets, but not templates or table widths. | A green check could be read as stronger assurance than it supplies. | Fixed: added template and table-width checks and explicit limits in the output. External links, anchors, claims, licenses and behavior remain outside these checks. |
| P3 | Personal development and data coverage are thin; many selections come from two engineering sources. | Broad navigation does not mean balanced or complete coverage. | Retain documented gaps and seek different public sources only for demonstrated needs. |

## Fresh source sample

The [Matt Pocock TDD file](https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md),
[Accessibility Audit file](https://github.com/humbleteam/accessibility-audit/blob/main/SKILL.md)
and [Marketing Skills schema file](https://github.com/coreyhaines31/marketingskills/blob/main/skills/schema/SKILL.md)
were accessible during this review. This sample checks source identity and
availability; it does not revalidate all catalog claims, licenses or every
selection. No candidate was executed.

## Next delivery, in order

1. Review the six task-oriented choices in [start here](start-here.md).
   For each, record the exact upstream file and commit, applicable license,
   actual requirements, authority boundaries, side effects and conflicting
   workflow rules. Select one SDD variant for evaluation.
2. Evaluate one representative task per choice with explicit acceptance.
   Include a negative trigger and an incompatible-instructions case. Use the
   same task and review standard without the skill as a baseline. Record
   exact harness/model versions, outputs, quality failures, effort and cost
   where available.
3. Publish the evaluation results in this repository and set the recommendation
   per use case. A failed or limited result is useful evidence; do not promote
   based on popularity or a valid SKILL.md structure.
4. Extend validation to the next highest-value discipline only after the first
   results show what users gain. Keep the broader candidate list available
   for later selection and pruning.

Completion means a reader can choose one starting skill, inspect its source,
understand its limits and reproduce the evaluation evidence. It does not
require installing the entire catalog or creating an original skill.

## Checks executed for this review

- Catalog validator: passed for 21 entries, including fields, IDs, categories,
  dates, template consistency, table widths and local file targets.
- `git diff --check`: passed.
- The PATH Python launcher was inaccessible and no `py` launcher was present.
  The validator ran successfully with an existing uv-managed Python 3.14.
  That is an environment detail, not a repository dependency.
- Candidate skill behavior and independent reviewer acceptance: not tested.
