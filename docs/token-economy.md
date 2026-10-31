# Token economy without losing evidence

Measure representative tasks: correctness, input/output tokens, retries, latency, cost and manual intervention. Separate measured usage, estimates and provider billing.

1. Bound searches, diffs and logs; retain raw errors. [RTK](../catalog/tools/token-economy/rtk.md) is optional.
2. Retrieve relevant context with progressive disclosure and targeted reads. Count [Graphify](../catalog/tools/context-and-retrieval/graphify.md) indexing and freshness and [Context7](../catalog/tools/context-and-retrieval/context7.md) network costs.
3. Scope sessions with acceptance criteria, checkpoints and durable handovers.
4. Use deterministic parsing, formatting and checks when judgment is unnecessary.
5. Route models by difficulty and verify outputs; cheapest tokens need not mean cheapest successful task.
6. Delegate selectively with bounded roles, budgets and stop conditions; parallelism duplicates context.
7. Inspect traces with [TokenTelemetry](../catalog/tools/observability/tokentelemetry.md); logs may be incomplete, estimates are not bills and usage does not establish quality.

Use the [evaluation worksheet](evaluation.md), including failures and regressions.
