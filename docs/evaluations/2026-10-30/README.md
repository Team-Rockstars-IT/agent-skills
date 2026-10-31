# Six starting skills: upstream review and fixture evaluation

**Decision date:** 2026-10-30. **Recommendation:** retain TDD, specification,
web accessibility and threat modeling as explicitly selected starting workflows.
Keep repository readiness as an optional comprehensive audit. Remove the tested
SEO skill from the default recommendation until its outdated guidance is
reviewed; retain its catalog reference with that limitation visible.

This is a small maintainer evaluation, not an independent benchmark. Both
conditions solved most of these deliberately small tasks. The findings support
scoped usability recommendations, not superiority, measured business impact,
security assurance or conformance claims.

## Reviewed sources and licenses

These are the exact revisions fetched for this evaluation, not floating URLs.
The full source paths, Git blob identifiers and SHA-256 resource hashes are in
[upstreams.json](upstreams.json). Copies were downloaded only into a temporary
directory and were not installed or added to this repository.

| Choice | Reviewed skill | License evidence | Requirement / instruction consequence |
| --- | --- | --- | --- |
| Matt Pocock TDD | [a496f551](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/tdd/SKILL.md) | [MIT](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/LICENSE) | Public test seams must be agreed; one test and implementation slice per cycle; refactoring is deferred to review. Reads tests.md and mocking.md; codebase-design is a conditional dependency if interface design is unresolved. |
| Addy specification | [eb07f19f](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/spec-driven-development/SKILL.md) | [MIT](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/LICENSE) | Stop after the spec for a later review; preserve an existing specification system. Multi-capability work first needs an approved map. Later phases refer to additional skills, which were not tested. |
| Exadel readiness | [1313702a](https://github.com/exadel-inc/agentic-readiness-assessment/blob/1313702ad53e2f2c069e2f4ef2dbebd19cb17e3d/skills/agentic-readiness-assessment/SKILL.md) | [Apache-2.0](https://github.com/exadel-inc/agentic-readiness-assessment/blob/1313702ad53e2f2c069e2f4ef2dbebd19cb17e3d/LICENSE), plus NOTICE | Thirteen report sections, fourteen score areas, gates, reversible probe and a Python report validator. Instructions require a commercial Exadel closing link verbatim; this is a workflow requirement, not an additional license condition established by this review. |
| Humbleteam accessibility | [b5735da6](https://github.com/humbleteam/accessibility-audit/blob/b5735da6c03604eea342a7de0e1e6c1d3550dca5/SKILL.md) | [MIT](https://github.com/humbleteam/accessibility-audit/blob/b5735da6c03604eea342a7de0e1e6c1d3550dca5/LICENSE) | Read its checklist and account for eighteen selected WCAG criteria. The workflow is a bounded web review, not complete WCAG coverage, a browser scanner or certification. |
| Corey Haines SEO audit | [820ad2c1](https://github.com/coreyhaines31/marketingskills/blob/820ad2c1c0ac4cc350158bd7912c753681a7d173/skills/seo-audit/SKILL.md) | [MIT](https://github.com/coreyhaines31/marketingskills/blob/820ad2c1c0ac4cc350158bd7912c753681a7d173/LICENSE) | Uses multiple references and optional project context and service tools. The reviewed instructions still list Mobile-Friendly Test; verify time-sensitive and categorical recommendations against primary sources. |
| OpenAI threat model | [49f948fa](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model/SKILL.md) | [Per-skill Apache-2.0](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model/LICENSE.txt) | Requires repository evidence and a context-validation check-in before the final report; reads the prompt-template output contract. Keep for explicit AppSec work. |

License texts were read, rather than relying only on GitHub's license hint.
The OpenAI repository has no repository-wide license hint in the fetched
metadata; the individual skill has its own Apache-2.0 license. This review
does not establish rights for every dependency or other skill in a collection.
All six repositories were unarchived when fetched. Their commit dates are in
the manifest; no future maintenance guarantee follows from that observation.

## Method and acceptance

Each main task was run once without an optional skill file and once with the
reviewed SKILL.md and its local resources explicitly supplied. The same task
and fixture files were used per pair. A second threat-model pair exercised a
scripted follow-up after context confirmation. Follow-up sessions received the
actual preceding check-in, but were fresh sessions, not a native resume.

Execution used installed Codex CLI 0.164.0 on Windows, workspace-write sandbox,
ephemeral sessions, and no model override. Child commands reported Node
24.22.1. Model identity is not independently available from the collected
event records, so it is not asserted. The host's common skill metadata and
configuration remained present; the baseline means no optional skill body was
loaded, not a completely instruction-free model. Provider routing changes and
shared host context are limitations.

Tasks prohibited networking, dependency installation, delegation, commits and
changes outside the fixture. Required interaction was supplied in the task:
TDD had an approved seam; specification stopped for review; threat modeling had
an initial check-in and an explicit later confirmation. This tests explicit
invocation and important task boundaries, not automatic discovery or negative
trigger rates. Those activation tests remain open.

| Choice | Fixture and acceptance | Baseline observation | Skill observation | Judgment |
| --- | --- | --- | --- | --- |
| TDD | Rename a note: authorized owner, trimmed title, unchanged content/identity; reject unauthorized, blank and missing-note requests without mutation. Test before implementation. | Four independent behavior checks passed; one bulk test-writing approach with two failing test invocations then green. | Same four checks passed; three red/green pairs in the execution trace and public-interface tests. | Retain for a disciplined test-first workflow. No correctness advantage demonstrated on this small task. |
| Specification | Single rename capability; include failure paths, actual commands, boundaries; use design/changes and leave source untouched. | Produced a usable spec in the designated location and requested review. | Preserved the designated location; included style evidence, testing strategy, boundaries and explicit open questions; stopped before planning/code. | Retain for larger or ambiguous work. Output is more explicit, not a proof of better downstream implementation. |
| Readiness | Assess an intentionally weak notes fixture; actual checks, backlog, limits and no remediation; restore any probe. | Produced useful evidence and a short backlog in the requested report. | Produced the full scorecard and seven fix records, completed/restored the probe, and passed the upstream report validator in an evaluator-side check. | Keep optional for comprehensive audits; omit from a lightweight default workflow. |
| Accessibility | Static checkout HTML has an unlabeled input, click-only div and missing image alt; no styles, rendering or assistive-technology evidence. | Found all three seeded issues with relevant criteria and stated runtime limits. | Found the same three issues and accounted for the eighteen selected criteria across findings, checked scope and unverified ledger. | Retain for bounded source review. Completeness ledger is useful; no additional seeded defect found. |
| SEO | Intended public product snapshot contains noindex, unrelated canonical and no title/description; robots allows crawling; no live service or metrics. | Identified the key indexing and page-head issues and did not invent measurements. | Identified the same issues, added a conditional viewport observation and a prioritized verification plan; did not claim measured rankings, speed or site-wide schema absence. | Fixture result is usable, but exclude from default recommendation because upstream guidance contains a verified obsolete tool reference. |
| Threat modeling | Confidential tenant notes, object access by ID without tenant check, user-controlled URL fetch and authorization logging. First ask/stop, then produce a conditional model after confirmation. | Respected check-in; final model covered conditional object access, SSRF, credential logging and resource exhaustion with file anchors. | Respected check-in; final model covered the same risks with explicit assets, boundaries, attacker non-capabilities, likelihood/impact, stable IDs and diagram; added a conditional log-integrity scenario. | Retain for explicit AppSec work. More structure and substantially more output; no additional seeded risk found. |

The fixture rubric is grounded in the supplied code and intended behavior;
skill wording is not itself proof of a correct finding. TDD behavior was
checked by a separate evaluator script. Static report coverage was reviewed
against the fixture. The readiness validator checks formatting and internal
report consistency, not the truth of every readiness conclusion.

## Material source findings

Observed session durations (seconds) are provided for effort context only.
Pairs ran concurrently, with uncontrolled caches and shared host load.

| Session | Baseline | Skill |
| --- | --- | --- |
| TDD | 97.562 | 133.944 |
| Specification | 67.223 | 87.244 |
| Readiness | 71.837 | 151.473 |
| Accessibility | 53.276 | 52.204 |
| SEO | 43.362 | 73.217 |
| Threat check-in | 39.682 | 40.852 |
| Threat follow-up | 65.501 | 71.979 |

**SEO freshness:** the reviewed skill lists Google's Mobile-Friendly Test.
Google's [retirement notice](https://developers.google.com/search/blog/2016/05/a-new-mobile-friendly-testing-tool)
states it was retired in December 2023. This is a verified source-maintenance
defect, even though the test task did not need that tool and the model did not
use it. It does not establish that all marketing skills are unsuitable. Keep
the source as an optional reference with explicit primary-source checking;
do not advertise the complete collection as tested.

**Readiness fit:** the required scorecard, gates and mandatory commercial
closing are visible in the pinned instructions and observed report. A
thorough audit can justify them, but they add considerable output and
maintenance burden for a small starter task. The fixture had no Git metadata
and deliberately weak test coverage. The reported 29/100 with low confidence
is the skill's judgment of that fixture, not a score for this catalog or an
independently established measure of agent readiness. The child's Node-only
rule prevented its Python validator; the evaluator ran that validator
separately and it exited successfully. Original source bytes were restored.

**Accessibility fit:** the explicit unverified ledger helps prevent treating
missing rendering evidence as a pass. Both outputs were cautious. This
review does not endorse every criterion attribution or severity label as a
complete expert audit. [W3C's evaluation guidance](https://www.w3.org/WAI/test-evaluate/preliminary/)
also distinguishes an initial review from comprehensive assessment.

## Artifacts and reproducibility

- [Source manifest](upstreams.json): commits, paths, resource hashes and dates.
- [Execution records](runs.json): exit codes, measured session durations,
  reported usage and command outcomes; no provider billing estimates.
- [TDD baseline](artifacts/tdd-baseline/result.md.txt) and
  [skill result](artifacts/tdd-skill/result.md.txt), with exported test code
  and independent behavior-check results in runs.json.
- [Specification baseline](artifacts/sdd-baseline/result.md.txt) and
  [skill result](artifacts/sdd-skill/result.md.txt); generated specs are saved
  under each artifact directory's files/design/changes path.
- [Readiness baseline](artifacts/readiness-baseline/agentic-readiness.md.txt)
  and [skill report](artifacts/readiness-skill/agentic-readiness.md.txt).
- [Accessibility baseline](artifacts/wcag-baseline/result.md.txt) and
  [skill report](artifacts/wcag-skill/result.md.txt).
- [SEO baseline](artifacts/seo-baseline/result.md.txt) and
  [skill report](artifacts/seo-skill/result.md.txt).
- [Threat check-in baseline](artifacts/threat-baseline/result.md.txt) and
  [skill check-in](artifacts/threat-skill/result.md.txt).
- [Final threat baseline](artifacts/threat-followup-baseline/files/threat-model.md.txt)
  and [final skill model](artifacts/threat-followup-skill/files/threat-followup-skill-threat-model.md.txt).

All fourteen sessions exited 0 and produced their requested result artifact.
Those exit codes alone are not quality verdicts. Four independent TDD behavior
checks passed in each condition. The upstream readiness validator also exited
0 in a separate evaluator-side invocation, and source bytes for specification
and readiness were checked unchanged after their runs.

The first-party [source-review script](../../../scripts/review_upstreams.mjs)
fetches current default-branch commits into a temporary directory by default.
Pass upstreams.json as its second argument after the target directory to fetch
these exact commits and check resource hashes instead. The
[fixture runner](../../../scripts/evaluate_starter_pack.mjs) takes that
directory and an optional comma-separated choice list; run threat-followup
after threat. The [evaluator/exporter](../../../scripts/grade_starter_pack.mjs)
exports only fixture results and compact evidence. Model execution uses
existing credentials and quota and requires an already installed CLI;
these scripts are opt-in evaluation tools, not catalog dependencies.

No global agent configuration was changed. Raw logs, downloaded upstream
files and stderr stayed in temporary storage; exported artifact paths were
redacted and trailing whitespace in exported prompts was normalized. One run per condition, shared host configuration, prompt
specificity, cache state and overlapping sessions prevent causal or
statistical conclusions. Durations and cumulative usage are observations,
not a cost or performance ranking. Native installation, automatic triggering,
live browsers, full conformance, live SEO, production security and real
repositories of different sizes remain unproven.

## Checks completed

- Fourteen Codex sessions completed and their artifacts were reviewed.
- Independent TDD acceptance: four checks per condition passed.
- Upstream readiness report validator: exited 0; evaluated source restored.
- Pinned source replay into a second temporary directory: all six commits
  and resource hashes matched.
- The three first-party evaluation scripts passed Node syntax checks.
- Catalog validator passed for 21 entries, including internal file links,
  template fields and Markdown table widths. External anchors are not checked
  by that script.
- Git whitespace check passed. Export review removed user-home identities
  and excluded raw logs, credentials and upstream resource bodies.
