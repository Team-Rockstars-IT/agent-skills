# Capability map: where does a given rule or capability belong?

Not every repeated need should grow AGENTS.md. Pick the smallest capability
that fits — an oversized AGENTS.md is as much of a problem as a missing one,
because everything in it competes for the agent's attention on every task.

| Question | Practical artefact | Boundary |
|---|---|---|
| Which team rules always apply, everywhere? | AGENTS.md | Concise, repo-wide, guiding rather than task-specific |
| Command output is too large or noisy to read directly? | An output filter/wrapper script | Compact summary plus a path to the full source |
| A task type recurs with its own instructions, scripts, or templates? | A dedicated skill | Small in scope, versionable, clear input/output |
| The agent needs controlled access to something outside the repo (tickets, docs, CI status, a read-only DB)? | An MCP integration | Explicit read/write boundary, credentials, and logging per server |
| A check or action needs to be deterministic and repeatable? | A script/tool with a defined contract | Clear exit codes, timeouts, and output contract |
| A subtask needs its own role, context, or narrower permissions (e.g. a security review, a PR summary)? | A subagent | Its own scope and a smaller permission set than the main agent |
| A whole workflow recurs end-to-end and conventions are proven? | A custom agent | Only after the individual steps have already been validated separately |

A good rule of thumb when drafting AGENTS.md: if a section is becoming a
procedure with steps, inputs, and outputs rather than a standing rule, it's
probably a skill in disguise. Move it out and leave a one-line pointer behind
("see the `release-notes` skill for cutting a release").
