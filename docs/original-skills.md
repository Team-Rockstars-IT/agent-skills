# Original skills and handbook background

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
see [portability](../docs/portability.md).

## Original skills

| Skill | Handbook chapter | What it does |
|---|---|---|
| [`define-work`](../define-work/) | Ch. 3 (Prompt engineering), Ch. 6 (Execution budgets) | Turns a vague coding request ("fix the validation", "make search faster") into a bounded work definition — intent, scope, out-of-scope, Given/When/Then acceptance criteria, stop rules — plus a small execution budget, before any code is touched. |
| [`agents-md`](../agents-md/) | Ch. 4 (Context engineering), Ch. 5 (Harness engineering) | Investigates a real repository and drafts or updates its `AGENTS.md`: architecture boundaries, conventions, test/build/lint commands, domain terms, and explicit allowed/ask-first/never permission tiers. |
| [`pr-evidence`](../pr-evidence/) | Ch. 7 (The evidence bundle) | Assembles a pull request description as an evidence bundle — objective, approach, modified files, checks *actually run* and their real result, known risks, and review focus — instead of a bare diff or an invented summary. |

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

MIT — see [LICENSE](../LICENSE).
