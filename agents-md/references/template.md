# AGENTS.md template and worked example

The open format lives at https://agents.md/ — this is a practical shape that
covers what a coding agent needs on day one.

```markdown
# AGENTS.md

## Project objective
<one or two lines: what this repo/service does and for whom>

## Architecture boundaries
- <e.g. Use the existing service layer for database writes; no direct SQL
  in controllers.>
- <e.g. The `packages/ui` package has no dependency on `packages/server`.>

## Workflow
- Work only on feature branches or worktrees.

## First read
Before making changes, read: `README.md`, `docs/architecture.md`, and the
test file(s) relevant to the area you're changing.

## Coding conventions
- <the conventions that cause rework when missed, not restatements of what
  the linter already enforces>

## Test / build / lint commands
- Lint: `<command>`
- Type check: `<command>`
- Unit tests (scoped): `<command> -- <relevant-test-path>`
- Full test suite: `<command>`
- Build: `<command>`

Run at least the scoped test command for the area you changed and report
red/green — do not report a check as passing without having run it.

## Domain terms
- **<term>** — <what it means in this codebase>

## Security rules
- <e.g. Never log tokens, credentials, or full request/response bodies for
  authenticated endpoints.>
- <e.g. All new endpoints must go through the existing auth middleware.>

## Permissions

**Allowed** (do this independently):
- Read the repository.
- Modify code within the agreed scope, on a feature branch.
- Run tests, linting, and type checks.
- Read application and build logs.

**Ask first** (get explicit approval before proceeding):
- Add or change dependencies or versions.
- Write or modify database migrations.
- Add or modify a public API.
- Touch authentication, security, or payment code.
- Carry out a large refactor.

**Never** (always prohibited):
- Read or export production data.
- Log or expose secrets, API keys, or tokens.
- Remove, weaken, or skip tests to make a check pass.
- Silently adjust acceptance criteria.
- Disable security scans or checks.

## Pull request expectations
A pull request must include: objective, approach, list of modified files,
checks run and their result, known risks, and where reviewer judgement is
specifically needed. See the `pr-evidence` skill if available.
```

## Worked example (from a Node.js/TypeScript service)

```markdown
# AGENTS.md

Work only on **feature branches or worktrees**.

**First read**: `README.md`, `docs/architecture.md`, and the relevant test
file.

**Allowed**: read the repository, modify code within scope, run
tests/lint/type checks.

**Ask first**: dependencies, migrations, public API, auth/security/payment.

**Never**: production data, logging secrets, deploying, removing tests.

Use **existing services** for database writes; no SQL in controllers.

Run at least `npm test -- <relevant-test>` and report red/green/not run.

**PR output** must include intent, modified files, checks, risks, and review
focus.
```

Notice this shorter version still covers every category — it's the categories
that matter, not the length. Expand a section only when the short version has
genuinely proven insufficient (an agent kept misreading something), not by
default.
