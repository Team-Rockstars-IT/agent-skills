# Work definition + session card template

Use this as a fill-in-the-blanks template. Each field has three valid states:
filled in with something real (from a search you ran, a file you read, or
what the user said), explicitly deleted because it doesn't apply, or marked
`unknown — needs input` because you don't actually know it yet. Never fill a
field with a plausible-sounding guess just to avoid leaving it incomplete —
"unknown — needs input" is a better answer than a specific-looking invention.

```
Intent: <one sentence — what effect, for whom, why it matters>

Scope: <flow / module / endpoint / component / files you may touch>

Out of scope: <what must not change, even if related>

Acceptance criteria:
  Given <precondition>
  When <action>
  Then <observable outcome>

  Given <edge case precondition>
  When <action>
  Then <observable outcome>

Stop rules: <concrete conditions that mean "pause and ask", e.g. dependency
  change, auth/payment impact, more files affected than scoped, same check
  failing twice without a new diagnosis>

Evidence expected: <what the handover must contain — summary, checks, risks,
  review focus>

--- execution budget (when executing now) ---

Context: <the specific files/docs/AGENTS.md sections relevant to this task>
Read budget: <e.g. max 5 files; no broad repo scan without a stated reason>
Loop budget: <e.g. max 2 implementation attempts>
Checks: <the exact command(s) that must pass>
Stop at: <short restatement of the stop rules above>
```

## Worked example

A vague request ("fix the validation") turned into a work definition, from a
real session-timeout handling task:

```
Intent: Redirect users with an expired session to the login flow, with a
  clear message, instead of showing a generic error.

Scope: Check-in process and session validation only.

Out of scope: Price calculation, document validation, layout, or any other
  authorisation behaviour.

Acceptance criteria:
  Given an expired session
  When the user opens a protected page
  Then the user is redirected to the login page

  Given a session that has just expired
  When the user performs an action
  Then the session is validated and, if necessary, the user is directed to
  the login page

Stop rules: Stop if the fix would require a change to dependencies, or if it
  affects authentication behaviour beyond session redirection. Explain why
  the current scope is insufficient and wait for a decision.

Evidence expected: Brief summary, checks, risks, review focus.

--- execution budget ---

Context: AGENTS.md, ticket #123, session-validator.ts, session-validator.test.ts
Read budget: max 5 files; no broad repo scan without a stated reason
Loop budget: max 2 execution attempts
Checks: npm test -- session-validator.test.ts
Stop at: dependency change, auth/security impact, more than 5 files affected
```

Notice what this buys you: the reviewer (or a teammate picking this up cold)
can tell at a glance what the change is supposed to do, what it must leave
alone, and what "done" looks like — without reading a chat transcript.

## Sizing signals — when to split before starting

Split the task into smaller pieces, each fit for its own reviewable pull
request, when any of these are true before you begin:

- The scope statement needs "and" more than once to describe unrelated areas.
- The acceptance criteria span more than one bounded context or service.
- You can't name a single stop rule that would catch the change growing out
  of control, because the boundary itself is fuzzy.
- The out-of-scope list is longer than the scope list — that usually means the
  task wasn't well bounded to begin with, not that the list is thorough.
