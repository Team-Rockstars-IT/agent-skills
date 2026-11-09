# Team Rockstars Agent Skills

A recipe book and reference catalog for agentic work across disciplines.
Start with the result you need, choose a recipe, then select the skills and
tools that help you deliver it. Third-party implementations stay upstream;
this catalog does not install them.

## Find your starting point

| What do you need? | Start here |
| --- | --- |
| Help choosing skills and tools | [Ask your agent](docs/start-here.md#ask-your-agent-to-help-choose) to read [AGENTS.md](AGENTS.md) |
| A route through the options | [Decision tree, experience routes and layers](docs/start-here.md) |
| Steps for a concrete type of work | [Recipe book](recipes/README.md) |
| An agent readiness scan | [Readiness recipe](recipes/repository-readiness.md): lightweight context check or comprehensive upstream assessment |
| A specific discipline or tool | [Catalog](catalog/README.md) |
| Evidence behind a recommendation | [Selection report](docs/skill-selection-report.md) and [dated evaluations](docs/evaluations/2026-10-30/README.md) |

For example, ask your agent:

```text
Read AGENTS.md in this repository. I want to [goal] on [project/source]
using [agent client]. Recommend one recipe, the minimum skills and tools,
and a concrete first step. Explain evidence and limitations. Give advice
only; do not install anything or change my project.
```

The readiness scan is included as a
[catalog reference](catalog/skills/development/agentic-readiness-assessment.md)
to Exadel's skill, with an evaluation on one synthetic repository. Its
implementation is retrieved upstream when deliberately selected.

## Background

The three original Claude Code skills operationalize the engineering discipline described in
[Team Rockstars IT](https://www.teamrockstars.nl)'s *AI-Assisted Development
Handbook: From Intent to Pull Request* (July 2026, by Roel van Bergen, Javier
Rennola, and Timo Koole).

The handbook's core claim: AI-assisted development becomes reliable only when
it's treated as an engineering process, not a prompting skill. That process
rests on three disciplines — **prompt engineering** (turning intent into a
bounded task), **context engineering** (giving an agent the right repository
and session context, not all of it), and **harness engineering** (permissions,
execution budgets, and a reconstructable audit trail) — closed out by an
**evidence bundle** in the pull request so a reviewer never has to reconstruct
a session from chat history.

Skills package reusable instructions and may include scripts and resources.
Discovery paths, triggering and invocation depend on the chosen harness;
see [portability](docs/portability.md).

## Browse references and evidence

This repository combines original skills with a technology-agnostic,
reference-first starter catalog. Third-party implementations stay upstream.
Start with the [selection and conflict guide](docs/selection-guide.md), browse
the [disciplines and tools](catalog/README.md), [recipes](recipes/README.md),
or the [portable example](examples/portable-project-setup/README.md). Assess
repository readiness with the [upstream assessment](catalog/skills/development/agentic-readiness-assessment.md). See
[portability](docs/portability.md), [evaluation](docs/evaluation.md), and
[contributing](CONTRIBUTING.md).

The [skill selection report](docs/skill-selection-report.md) explains each
candidate, its value and its discipline-specific limitations.

The [quality review](docs/quality-review.md) records current gaps and the
next steps toward a validated starting set.

The [six-choice evaluation](docs/evaluations/2026-10-30/README.md) records pinned
upstreams and licenses, representative task results, baseline comparisons,
and the advice to retain four workflows, keep readiness optional and exclude
the tested SEO audit from default recommendations.

## Original skills

| Skill | Handbook chapter | What it does |
|---|---|---|
| [`define-work`](define-work/) | Ch. 3 (Prompt engineering), Ch. 6 (Execution budgets) | Turns a vague coding request ("fix the validation", "make search faster") into a bounded work definition — intent, scope, out-of-scope, Given/When/Then acceptance criteria, stop rules — plus a small execution budget, before any code is touched. |
| [`agents-md`](agents-md/) | Ch. 4 (Context engineering), Ch. 5 (Harness engineering) | Investigates a real repository and drafts or updates its `AGENTS.md`: architecture boundaries, conventions, test/build/lint commands, domain terms, and explicit allowed/ask-first/never permission tiers. |
| [`pr-evidence`](pr-evidence/) | Ch. 7 (The evidence bundle) | Assembles a pull request description as an evidence bundle — objective, approach, modified files, checks *actually run* and their real result, known risks, and review focus — instead of a bare diff or an invented summary. |

Together they cover the handbook's practical workflow: **intent → work
definition → context setup → harnessed execution → verification → pull
request review.**

## Use the original skills in Claude Code

The catalog itself needs no installation. These Bash examples apply only to
the three original skills and assume the target skills directory exists.
Follow the selected upstream and harness documentation for other skills.

**Personal (all your projects):**

```bash
cp -r {define-work,agents-md,pr-evidence} ~/.claude/skills/
```

**Project-only (commit alongside a repo so your team shares the same skills):**

```bash
cp -r {define-work,agents-md,pr-evidence} <your-repo>/.claude/skills/
```

Run these commands from this checkout, then verify discovery and invocation
in the installed version of your harness before relying on the skills.

## How the skills fit together

A typical session: `define-work` turns a vague ask into a written contract
before you touch code and sets an execution budget for the session. You (or
Claude) implement within that budget, stopping at the stop rules it defined.
`agents-md` is a separate, occasional-use skill — run it once per repo (or
whenever conventions drift) to give every future session the repository
context it needs, independent of any single task. When the work is done,
`pr-evidence` turns the diff and the real check results into a reviewable
handover, ideally referencing the work definition `define-work` produced
earlier in the same session.

None of the three depend on the others being installed — each is useful on
its own — but they're designed to compose.

## Customizing

These skills are intentionally generic about tech stack and team-specific
conventions. `agents-md` in particular produces a *draft* meant for your
review before it's written — the permission tiers (allowed / ask first /
never) especially are judgment calls about risk tolerance that belong to your
team, not to Claude.

## Source

Derived from *AI-Assisted Development Handbook: From Intent to Pull Request*
(Team Rockstars IT, July 2026). All handbook content is the property of Team
Rockstars IT; these skills are an independent, practical translation of its
recommendations into Claude Code tooling.

## License

MIT — see [LICENSE](LICENSE).
