---
name: agents-md
description: Investigate a repository and write or update its AGENTS.md — the repo-wide instructions a coding agent reads before doing any work (architecture boundaries, conventions, test/build/lint commands, domain terms, and explicit allowed/ask-first/never permission lists). Use this whenever the user asks to "set up AGENTS.md", "onboard this repo for AI coding agents", "write instructions for Claude/Copilot/coding agents", "document our conventions for the agent", "configure what the agent is allowed to do", or "add guardrails for agentic coding". Also use it proactively when you're about to do significant multi-step agentic work in a repository that has no AGENTS.md, CLAUDE.md, or equivalent agent-instructions file yet, and the user seems to want ongoing agent use rather than a one-off task — mention it as an option rather than silently creating files. Not for writing end-user documentation or README files.
---

# AGENTS.md setup

## Why this exists

An agent can read an entire repository, but reading isn't the same as knowing
which architectural choice is load-bearing, which test strategy actually
matters, or which files are off-limits. Left to guess, it will — and the
result is usually technically-plausible code for the wrong problem, or a diff
that quietly crosses a boundary nobody wrote down. A ban on agent use doesn't
fix this, and neither does a lengthy policy document nobody reads while
coding. What works is a short, concrete file, checked into the repo, that
translates team agreements into day-to-day working rules.

AGENTS.md holds **repository context**: things that are true across sessions
and tasks — architecture, conventions, test strategy, domain terms, security
boundaries. It is deliberately not the place for task-specific detail (that's
session context — a ticket, a work definition, a specific file list). Treat
outdated or contradictory instructions as a real cost: an agent given ten
stale rules and one live one gets worse, not better, from the padding. Curate
this file the way you'd curate onboarding docs for a sharp new hire, not the
way you'd write an exhaustive spec.

## Process

### 1. Survey the repository before writing anything

Don't draft from assumptions — look:

- Package manager, language(s), and framework(s) in use.
- The actual commands for lint, type-check, unit tests, build, and (if
  present) security/dependency scanning. Prefer the single command a human
  would run, not a description of what CI does internally. Read what each
  script actually does, not just its name — a `lint` or `build` script that's
  really a placeholder (`echo ok && exit 0`) is common in early-stage or
  sample projects, and documenting it as a real check would mislead every
  future session into trusting a green result that doesn't mean anything.
- Whether existing docs (README, architecture notes) still match the code.
  Docs describing a component, integration, or behaviour that isn't actually
  there yet is exactly the kind of technically-plausible-but-wrong gap this
  file exists to prevent — note the mismatch in the draft rather than
  silently treating the doc as ground truth.
- Directory and module boundaries — is this a monorepo with multiple
  apps/services that need different rules? A frontend app, a backend service,
  and an infra directory usually don't share one set of conventions.
- Existing documentation worth pointing to rather than duplicating: README,
  CONTRIBUTING, ADRs, runbooks, a glossary. AGENTS.md should link to these as
  authoritative sources, not restate them.
- Anything already agent-oriented: an existing AGENTS.md, CLAUDE.md,
  `.github/copilot-instructions.md`, or path-specific `.instructions.md`
  files. Update and consolidate rather than creating a competing file.

### 2. Identify what actually needs a boundary

Look specifically for: authentication and authorization code, payment or
billing logic, database migrations, anything touching production data or
secrets, and public API contracts. These are the areas where the cost of an
agent guessing wrong is highest, and where an explicit rule pays for itself
fastest.

### 3. Draft the file

Structure the draft around these sections — see `references/template.md` for
a filled-in example:

- **Project objective** — one or two lines of context on what this
  repo/service does.
- **Architecture boundaries** — what depends on what, what must not
  short-circuit (e.g. "use the existing service layer for database writes; no
  direct SQL in controllers").
- **Coding conventions** — the ones that actually cause rework when missed,
  not a restatement of a linter config the linter already enforces.
- **Test / build / lint commands** — exact, copy-pasteable commands. If there
  is one predictable command for "run the relevant tests," say what it is and
  how to scope it to a subset.
- **Domain terms** — a short glossary where the domain vocabulary isn't
  self-evident from the code.
- **Security rules** — the specific things that must never be exposed, bypassed,
  or weakened.
- **Permissions: Allowed / Ask first / Never** — see below.
- **Pull request expectations** — what a handover must contain. If a
  `pr-evidence` skill (or equivalent) is actually installed and available in
  this environment, say the PR should line up with it; otherwise describe the
  expected contents directly rather than pointing to a skill that may not
  exist for whoever reads this file next.

#### The permission tiers

Categorise actions into three groups. The exact list varies by repo, but the
pattern is stable — adapt it, don't skip it:

- **Allowed** (agent may do independently): read the repository; modify code
  within the stated scope on a feature branch; run tests, linting, and type
  checks; read local logs; prepare a pull request.
- **Ask first** (needs explicit approval before proceeding): add or change
  dependencies; write or modify database migrations; add or modify a public
  API; touch authentication, security, or payment code; carry out a large
  refactor.
- **Never** (always prohibited, no exceptions): read or export production
  data; log or expose secrets or tokens; remove or weaken tests to make them
  pass; silently adjust acceptance criteria; disable security checks or scans.

This exists because an agreement inside a chat prompt is not yet a boundary —
it only holds if it's written down somewhere the agent reliably reads, and
ideally also enforced structurally (branch protection, CI gates, an
allowlisted command wrapper), not just requested in prose.

### 4. Choose one file or a layered set

A single global AGENTS.md is fine for a small, single-purpose repo. For a
monorepo, prefer a short root file with universal rules plus path- or
package-specific files for anything that genuinely differs (language,
framework, service boundary). Keep the root file brief and point down to
where the detail lives — don't let it become an encyclopedia that buries the
one rule that matters under twenty that don't.

### 5. Confirm before writing

Show the draft to the user before creating or overwriting the file,
especially the Allowed/Ask first/Never lists — these are judgment calls about
risk tolerance that belong to the team, not to you. Adjust based on their
feedback.

### 6. Keep it alive

An AGENTS.md that never changes after creation drifts out of date exactly
like any other doc. When an agent gets stuck at the same point more than
once, or a review keeps flagging the same missed convention, that's a signal
to add or sharpen a rule — not to route around it silently. Treat this as a
short feedback loop, not a one-time setup task.

## Choosing the right place for a rule

Not every repeated instruction belongs in AGENTS.md. If what you're setting
up is really a reusable procedure with its own scripts or templates (e.g. "how
to prepare a release," "how to run a migration check"), a dedicated skill is
usually a better fit than a growing AGENTS.md section. See
`references/capability-map.md` for the fuller breakdown of when to reach for
AGENTS.md vs. a skill, an MCP integration, a script, or a subagent.
