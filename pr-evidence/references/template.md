# PR evidence bundle template and worked example

```markdown
## Objective
<intent, one or two sentences, linked to an issue/spec if one exists>

## Approach
- <key decision or choice, and why>
- <key decision or choice, and why>

## Modified files
- `<path>` (+X -Y)
- `<path>` (+X -Y)

## Checks
- Lint: <passed / failed / not run> — `<command>`
- Type check: <passed / failed / not run> — `<command>`
- Unit tests: <passed / failed / not run> — `<command>`, <result summary>
- Build: <passed / failed / not run> — `<command>`
- Security scan: <passed / failed / not run>
- CI: <link, commit SHA>

## Risks
- <what remains uncertain, untested, or a deliberate trade-off>

## Review focus
- <the specific thing a human should look at closely, and why>

## Out of scope
- <what was deliberately not touched>
```

## Worked example

From a real change that redirects users with an expired session to the login
flow:

```markdown
## Objective
Redirect expired sessions in the check-in process to the login page, with a
clear message, instead of a generic error.

## Approach
- Detect expired/invalid sessions on both server and client.
- Redirect to `/login` using the `redirect_to` parameter so the original
  destination is preserved after re-authentication.
- Show a toast notification explaining why the user was redirected.

## Modified files
- `app/middleware/session.ts` (+48 -12)
- `app/utils/auth-guard.ts` (+36 -8)
- `app/pages/login.tsx` (+18 -4)
- `app/components/SessionExpiredToast.tsx` (+32 -0)
- `app/hooks/useSession.ts` (+22 -6)
- `app/types/session.ts` (+6 -0)

## Checks
- Lint: passed
- Type check: passed
- Unit tests: passed — `npm test -- session-validator.test.ts`, exit 0
- E2E tests: passed
- Build: passed
- Security scan: not run — no scanner configured in this repo
- Dependency check: passed
- CI: <run-link> on <commit-SHA>

## Risks
- No full regression run against document validation (out of scope, but
  worth knowing it wasn't re-verified).
- Possible redirect loop if `redirect_to` is misconfigured — mitigated with a
  max-one-redirect-per-request guard.
- Loss of original destination if `redirect_to` is missing — falls back to `/`.

## Review focus
- Correctness of session detection on both server and client.
- Security of the `redirect_to` parameter (validate against open redirect).
- Whether original intent is preserved through the login round-trip.
- UX of the toast (display duration, frequency).

## Out of scope
- Layout, price calculation, and document validation.
- "Remember me" / refresh token behaviour.
- Multi-session management and logout-on-other-devices.
```

Notice this is reviewable at a glance: what changed, what was verified, what
wasn't, and exactly where to look. That's the point — it should be faster to
review this bundle than to reconstruct the same information from the diff and
commit log.
