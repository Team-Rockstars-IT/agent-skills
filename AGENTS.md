# Agent instructions

This repository is a recipe book and reference catalog for agentic work across
disciplines. Help people choose a small, suitable workflow for their outcome.
Most catalog entries link to upstream implementations; they are not installed
skills. The original skill implementations are `define-work/`, `agents-md/`
and `pr-evidence/`.

## When asked which skills or tools to use

1. Read [Start here](docs/start-here.md) and the
   [selection recipe](recipes/choose-your-setup.md). Use the decision tree to
   find a route, then read that recipe and the relevant catalog entries.
   Do not load every skill or evaluation artifact.
2. Establish the desired output, available project/context, agent client
   (harness), existing skills/tools and constraints. Use supplied facts and
   authorized read-only discovery first. Ask only for missing information
   that would change the choice; otherwise state assumptions and proceed.
3. Choose one primary recipe. Separate project instructions (`AGENTS.md`),
   reusable procedures (skills), executable capabilities (tools/MCP), the
   harness and optional orchestration. An additional layer needs a concrete
   task-related reason. Using existing capabilities can be sufficient.
4. Return the following, in the user's language:
   - **Goal and context:** desired result, known environment and assumptions.
   - **Recipe:** a repository link and why it fits.
   - **Minimum setup:** the primary skill, if useful; required tools and
     access; what is already available versus what needs obtaining.
   - **Optional additions:** only for a named gap; explain when to skip them.
   - **Evidence and limits:** local entry links, review dates and the scope
     of any evaluation. Separate source-reviewed, locally-tested and unverified.
   - **First step:** a concrete prompt or action and the expected output.
5. Follow [selection and conflicts](docs/selection-guide.md). Check the exact
   upstream instructions, dependencies, license and current harness support
   before proposing an installation command or executing a third-party skill.
   If that verification is unavailable, mark the installation unverified.
   A catalog recommendation does not authorize installation or execution.

Readiness requests route to the [readiness recipe](recipes/repository-readiness.md).
Distinguish a lightweight context check from Exadel's comprehensive upstream
assessment. Its recorded evaluation concerns one synthetic repository, not
this catalog or the user's project. Never invent a readiness score.

If no suitable recipe or reviewed skill exists, say so and use
[discovery guidance](docs/find-more-skills.md); do not present a collection
index as an individually tested skill. A general agent workflow may suffice.

## When changing this repository

- Keep the task-first entry in [Start here](docs/start-here.md), the
  [recipe index](recipes/README.md) and [catalog](catalog/README.md) connected.
  Preserve existing public skill paths and upstream references.
- Write repository documentation in English; answer the user in their language.
  Use [the recipe template](templates/recipe.md) and
  [catalog entry template](templates/catalog-entry.md). Link to the owning
  entry for evidence and constraints instead of duplicating those claims.
- Follow [CONTRIBUTING](CONTRIBUTING.md). Keep third-party implementations
  upstream. Historical evaluations remain dated records; document a new
  evaluation separately rather than rewriting an old result.
- Authorized documentation edits, local validation and diff review can proceed.
  Ask before actions outside the requested scope, such as installing tools,
  changing another project or running an assessment that mutates that project,
  unless the user has already authorized them. Never expose secrets or private
  project information or fabricate sources, command results or compatibility.

## Verification and handover

Run `python scripts/check_catalog.py` after documentation/catalog changes and
`git diff --check`. The checker validates catalog metadata, table widths and
local file links. It does not validate external links, Markdown anchors,
upstream claims, skill behavior or harness compatibility. Review those parts
of a change separately as relevant. This library has no application build.

Report what changed, checks actually run, and remaining limitations. Keep
recommendation-only requests free of project changes and installations.
