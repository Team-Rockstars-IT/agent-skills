---
name: pr-evidence
description: Assemble a pull request description as an evidence bundle — objective, approach, modified files, checks actually run and their result, known risks, and where reviewer judgement is needed — instead of a bare diff or a vague summary. Use this whenever the user asks to "write the PR description", "prepare this for review", "summarize these changes", "open a pull request", "write a commit/PR summary", or is wrapping up a coding task and about to hand it off for review. Also use it proactively once you've finished implementing a non-trivial change and are about to commit or open a PR, even if the user didn't explicitly ask for a description. Do not use it to fabricate results for checks that were never actually run — the whole point is to report what really happened.
---

# PR Evidence Bundle

## Why this exists

A reviewer opening a pull request with a large diff, a commit message like
"implement feature per spec," and no test results isn't reviewing — they're
doing archaeology, reconstructing what was done and why from the code alone.
That costs real time and it's exactly the situation that makes agent-produced
diffs feel riskier than they need to be. Output is not proof; the pull request
is where a reviewer decides whether the evidence is strong enough to merge.

The fix is a fixed, small shape for the handover, filled in with what
actually happened rather than a summary written from memory or written to
look complete. Reported success on a check that was never run is worse than
admitting it wasn't run — it converts a visible gap into a hidden one.

## Before writing anything: gather the real evidence

Don't compose the bundle from what you remember doing — check:

1. **Modified files** — run `git status` / `git diff --stat` (or your VCS's
   equivalent) to get the actual list of changed files and the size of each
   change. Don't reconstruct this from memory.
2. **Checks** — run the project's actual lint/type-check/test/build/security
   commands (check AGENTS.md or the project config for the exact commands if
   you're unsure) and record, per check: what ran, and whether it passed,
   failed, or wasn't run at all. A check you didn't run belongs under "not
   run," not under a green checkmark, and a check that failed belongs in
   Risks or blocks the handover — it doesn't get quietly omitted. If a
   category of check has no corresponding command in this project at all
   (no type checker configured, no security scanner set up), record it as
   "not run — no such check configured," which is a different, more useful
   signal to a reviewer than "not run — skipped" or "failed." And look at
   what a script actually does before trusting its exit code: a `lint` or
   `build` script that's just `echo ok && exit 0` passing tells you nothing —
   flag it as a placeholder rather than reporting a normal pass.
3. **The original intent** — pull this from the work definition if one exists
   for this task (see the `define-work` skill), the linked ticket/issue, or
   the user's original request. If none of these are available, state the
   objective as you understand it and flag that it wasn't independently
   confirmed.

## The evidence bundle

Fill in each section concretely — a field that just restates the diff isn't
adding information.

- **Objective** — the intent, in one or two sentences, ideally linked to an
  issue or spec. This is what the reviewer checks the diff *against*.
- **Approach** — the key choices made and why, as a short list. Enough for
  someone to understand the shape of the solution without reading every line
  of the diff.
- **Modified files** — the actual list, with a rough sense of size
  (lines/files changed) so the reviewer can gauge where to spend attention.
- **Checks** — each relevant check, its status (passed / failed / not run),
  and how to verify it independently (a command, a CI link, a commit SHA).
  Never state a check passed without having run it.
- **Risks** — what remains uncertain, untested, or a deliberate trade-off.
  This is where you put the honest "we didn't fully verify X" rather than
  letting the reviewer discover it.
- **Review focus** — the specific place(s) where human judgement is most
  needed. Point the reviewer, don't make them find it themselves.
- **Out of scope** — what was deliberately not touched, especially anything
  that looks related but wasn't addressed. This prevents both false
  expectations and scope creep in review comments.

Full template and a worked example: `references/template.md`.

## How to use the result

- If the user is opening the PR through a CLI (e.g. `gh pr create`) and a
  repo with a remote is available, offer to use the evidence bundle as the
  PR body directly.
- Otherwise, hand back the markdown so the user can paste it into their PR,
  commit message, or ticket.
- If a check couldn't be run at all (missing credentials, no CI access,
  environment limitation), say so plainly under Risks rather than leaving
  that section incomplete or silently dropping the check.
- If the diff includes changes that don't map to any stated objective, treat
  that as a signal worth surfacing to the user, not something to smooth over
  in the write-up — that's usually exactly the kind of scope drift this
  bundle exists to catch.
