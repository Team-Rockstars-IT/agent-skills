# Before/after evaluation

Compare representative tasks with identical acceptance and review standards. Record versions, context and cache state; count cold indexing, warm queries and refresh. Include failed attempts.

| Measure | Baseline | Candidate | Evidence or uncertainty |
| --- | --- | --- | --- |
| Task and acceptance | | | |
| Correctness and regressions | | | |
| Input / output tokens and source | | | |
| Retries and manual interventions | | | |
| Latency including setup/indexing | | | |
| Estimated cost / actual bill | | | |
| Failures and missing evidence | | | |

A lower token count alone is not success; do not extrapolate from one run.

Completed example: [six starting skills and baseline comparisons](evaluations/2026-10-30/README.md).

## Generic core navigation walkthrough 2026-11-09

**Method:** agent-performed source inspection of the same three
[example tasks](../examples/README.md) against baseline
[`801ad94`](https://github.com/Team-Rockstars-IT/agent-skills/tree/801ad9468bd43bde98d89ab982ef3b62312e8f69)
and the revised README, core recipes and generated views. This compares the
documented paths and requirements, not model-generated task outcomes.

| Task | Baseline instructions | Revised instructions | Inspection result |
| --- | --- | --- | --- |
| Decision from a supplied brief | Available through a broad specialist/research route; evidence and constraints already covered | Direct research/compare goal; supplied facts, common criteria and unknowns determine the recommendation | The core supports a reasoned decision without requiring a repository, install or external service |
| Review a described design flow | Specialist review available; the delivery recipe assumed implementation, diff and software PR evidence | Direct review goal accepts the artifact and relevant criteria; software PR tooling is conditional | Description-backed observations and untested user hypotheses remain distinct; no code or scanner is required |
| Code change in an existing project | Direct software-change workflow with shell/project checks | Generic creation workflow retains optional TDD/debugging/SDD and discovers the actual project toolchain | Programming-language filters and specialist source/evidence links remain available; no new stack default is introduced |

The two non-code cases and the code case have input, intended output and
observable review criteria. Default `language:any` badges are omitted from
generated tables while JSON metadata and search matching retain that meaning.
Core specialist tables use collapsible disclosure for readers; Markdown-reading
agents still receive that text if they read the whole file.

**Not established:** output correctness across agents, independent user acceptance,
token savings, latency, cost or better task success. No isolated before/after
model runs were performed for this walkthrough. Use the worksheet above and
the same acceptance criteria for a future runtime comparison. The older pinned
skill evaluations remain separate, dated evidence.
