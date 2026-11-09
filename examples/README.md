# Examples

These fictional prompts use the same core recipes with different artifacts.
They are copyable examples with review criteria, not executed benchmarks.

## A decision from a brief

Use [Research and compare](../recipes/specialist-review.md):

```text
Draft a decision note from this brief. Option A costs EUR 800 per month,
takes two weeks to deliver, supports the required audit trail and needs manual
migration. Option B costs EUR 1,200 per month, takes one week, supports the
audit trail and includes automated migration. Budget is at most EUR 1,000 per
month; no delivery deadline is stated. Volume and migration effort are unknown.
Compare against those constraints, give a conditional recommendation and name
what needs checking. Use only the brief; this task needs no external service.
```

**Review criteria:** A meets the stated budget; B exceeds it. Manual migration
is a known difference, while its actual effort is unknown. A delivery deadline
must not be invented. The note separates the choice from unverified assumptions.

## A design review from a described flow

Use [Review and deliver](../recipes/evidence-driven-delivery.md):

```text
Review this signup flow for potential friction: enter an email address,
see a confirmation message, then follow a verification link in the email.
The described flow offers no way to correct the email after submission.
No screens, analytics or user-test results are supplied. Identify observations,
hypotheses and useful validation questions. Prepare a short handover for the
designer. Do not claim observed user behavior or accessibility conformance.
```

**Review criteria:** the missing correction path is grounded in the description.
Its effect on users is a hypothesis requiring validation. No browser, scanner,
screen-reader result or measured conversion improvement is invented.

## A code change in the project's own language

Use [Work in small steps](../recipes/minimal-agent-workflow.md):

```text
In [target project], let users rename their own notes with a trimmed, nonempty
title. Reject unauthorized users, blank titles and unknown notes without
mutation. Preserve note identity and content. Inspect the existing language,
conventions and checks; implement and verify at an appropriate public interface.
Use the existing toolchain and report any missing access or runtime evidence.
```

**Review criteria:** checks exercise success and rejection behavior, preserve
identity/content and come from the actual project. No framework or programming
language is assumed, and missing access does not become a claimed pass.

For a longer software illustration, see the
[portable fictional project](portable-project-setup/README.md). For the scope of
the core-navigation comparison, see [evaluation](../docs/evaluation.md#generic-core-navigation-walkthrough-2026-11-09).
