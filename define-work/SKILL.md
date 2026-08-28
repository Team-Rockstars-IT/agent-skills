---
name: define-work
description: Turn a vague or open-ended coding request into a bounded work definition (intent, scope, out-of-scope, acceptance criteria, stop rules) plus an execution budget, before writing any code. Use this whenever a coding task is ambiguous, spans multiple files or components, touches shared/sensitive code (auth, payments, migrations, public APIs), or was handed over as a single vague sentence like "fix the validation", "clean up the auth flow", "make search faster", or "improve error handling". Also use it when the user explicitly asks to "scope this task", "write a work definition", "plan this before you build", "define acceptance criteria", or wants to hand off a task with clear guardrails. Skip it for genuinely trivial, single-line, unambiguous fixes where there's nothing to scope.
---

# Define Work

## Why this exists

The gap between "fix the validation" and a pull request that touches sixty files
almost never comes from a lack of model capability — it comes from a lack of
explicit agreement about what "fixed" means, what must stay untouched, and when
to stop and ask. A human developer fills these gaps unconsciously from context
stored in their head. An agent — and often a teammate reading the request cold —
cannot. Writing the agreement down first is cheap; discovering it was missing
after a large diff already exists is not.

This skill turns an intent into a **work definition**: a short, explicit
contract that a developer, an agent, and a reviewer can all read the same way.
For work you're about to execute yourself in this session, pair it with an
**execution budget** — a small set of limits (how much to read, how many
attempts, which checks) that keep a task from quietly growing past what anyone
agreed to.

## When to use this, and how far to take it

Match the effort to the risk and size of the task:

- A one-line, unambiguous fix (typo, off-by-one, a clearly-specified rename)
  doesn't need this — just do it.
- A normal feature or bugfix confined to a known area benefits from the short
  form: a few lines covering intent, scope, out-of-scope, and acceptance
  criteria, written inline in your response or the ticket/issue.
- A task that's large, touches authentication/payments/migrations/public APIs,
  or was described ambiguously deserves the full work definition below,
  presented to the user for confirmation *before* any code changes.
- A task that's too big for one reviewable pull request should be split before
  execution starts, not discovered mid-diff. If you can't state the scope in a
  sentence or two, that's the signal to split it.
- A task that names an area you can't actually locate in the codebase (wrong
  repo, doesn't exist yet, or the description doesn't match anything real)
  isn't ready to be scoped at all — ask before drafting, rather than
  producing a definition built on a guess about where the code lives.

## The work definition

Before filling anything in: if you can't state the intent, locate the
relevant area of the codebase, or ground the scope in something real (the
user's words, a search you actually ran, files you actually read), that's
your cue to ask targeted questions *first* — not to draft a plausible-looking
definition and hope it's close enough. A named file, module, or acceptance
criterion should come from something you verified or the user stated, never
from what would merely be a reasonable guess. An unfilled field you flagged
as unknown is far more useful to everyone downstream than a specific-sounding
one that turns out to be invented. If the area the user describes doesn't
seem to exist in the codebase at all, say so and ask before drafting even the
short form — don't paper over the gap with placeholders.

Work through the fields below. Skip a field only when it genuinely doesn't
apply — don't pad it with filler, and don't fill it with a guess either; mark
it "unknown — needs input" instead.

1. **Intent** — one sentence: what effect are we after, for whom, and why does
   it matter? This is the thing that must survive even as implementation
   details change.
2. **Scope** — which flow, module, endpoint, component, or files are you
   permitted to touch?
3. **Out of scope** — what must explicitly *not* change, even if it looks
   related or tempting to "fix while you're in there"? This is what prevents a
   small task from becoming a refactor nobody asked for.
4. **Acceptance criteria** — describe observable behaviour, not implementation
   ("redirect to the login page with a clear message" rather than "add an
   if-check in the middleware"). Write them as Given/When/Then scenarios where
   practical — this is what makes them directly usable as tests later, and it
   forces edge cases into the open. Explicitly include: the unhappy path, a
   user without rights, expired/invalid input, and any existing behaviour that
   must be preserved.
5. **Stop rules** — the specific conditions under which you pause and ask
   instead of continuing. Vague stop rules ("stop if something seems wrong")
   don't work; concrete ones do. Good starting points: the change would cross
   into a new dependency, migration, or public API; it touches auth, payment,
   or privacy-sensitive code; it would affect more files than the scope
   implied; the same check has now failed twice without a new diagnosis; or
   completing the task would require weakening a test or acceptance criterion
   rather than meeting it.
6. **Evidence expected** — what should the eventual handover (chat reply or
   pull request) contain so a reviewer doesn't have to reconstruct the session?
   Normally: a short summary, which checks ran and their result, known risks,
   and where a reviewer's judgement is specifically needed. (The `pr-evidence`
   skill produces this at handover time — this field just sets the
   expectation up front.)

If you cannot fill in intent, scope, and acceptance criteria with confidence,
that's a signal the definition isn't ready — ask the user targeted questions
rather than guessing. Useful questions to ask yourself or the user before
starting: What assumptions am I making? Which edge cases are still
unaddressed? Is this small enough for a single reviewable pull request? What
would make me stop and ask rather than continue?

Present the completed work definition back to the user for a quick look before
you start changing code, unless the task is small enough that the definition
is effectively a one-line restatement they've already confirmed by asking for
it. Confirmation doesn't need to be a formal approval step — a "yep, go ahead"
is enough. If you're operating unattended (no one to confirm with), state the
work definition plainly, note the assumptions you made explicitly as
assumptions, and proceed.

## The execution budget (session card)

When you're about to execute the task yourself in this session, add a compact
budget on top of the work definition. This keeps effort proportional to the
task rather than letting a stuck agent quietly burn tokens searching and
retrying:

- **Read budget** — roughly how many files or how much log/search output is
  reasonable to look at. Prefer five specifically relevant files over fifty
  semi-relevant ones; if you find yourself wanting to scan broadly, first
  articulate what specific uncertainty that scan would resolve.
- **Loop budget** — how many independent implementation attempts or retries on
  the same failing check are reasonable (two is a sensible default) before you
  stop and report back rather than trying a third variation.
- **Checks** — the specific command(s) that must pass, stated concretely
  (e.g. `npm test -- session-validator.test.ts`), not "run the tests."
- **Stop at** — pull the concrete stop rules from above into one line.

Full template and a worked example: `references/template.md`.

## After the definition is set

Work in small, logical steps and keep the diff aligned to the scope you wrote
down. If you hit a stop-rule condition, don't route around it — surface it and
explain why the current scope is insufficient, then wait for a decision rather
than expanding scope on your own judgement. If the task turns out to need
changes outside the agreed scope, that's new information: revise the work
definition explicitly (and get it re-confirmed) rather than letting the diff
drift past what anyone agreed to.

When the work is done, use the `pr-evidence` skill (if available) to turn this
work definition plus what actually happened into a reviewable handover.
