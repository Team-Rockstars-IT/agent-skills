# Agent instructions

This is a recipe book and reference catalog for agentic work across disciplines.
Most catalog entries link upstream; they are not installed skills. Original
implementations live in `define-work/`, `agents-md/` and `pr-evidence/`.

## Help someone choose

1. Read the four task routes in [README.md](README.md). Use supplied context
   and authorized read-only discovery to select one recipe. Read that recipe
   and only the relevant catalog entries. Use the [full index](recipes/README.md)
   for workflow improvements or other needs; do not load the whole library.
   For a named upstream skill or goal/category/programming-language search, use
   [the focused finder](docs/skill-finder.md) or `python scripts/skill_catalog.py search`.
   `language:any` means no particular programming-language requirement, not
   verified compatibility with every stack. Distinguish skills from toolkits.
2. Start with the user's existing agent and tools. Recommend at most one
   primary skill initially, and additional tools only for a concrete missing
   capability. A simple task may need nothing extra. Do not make the user
   choose an experience level, learn the layers or fill in an intake form.
3. Ask a focused question only when a missing fact would change the choice.
   Otherwise proceed with stated assumptions. Do not assume a component is
   installed or available without evidence.
4. Answer briefly in the user's language, using three lines:
   - **Use:** one linked recipe and the primary skill, if useful.
   - **Need:** missing essential tools/access, or "nothing extra" if established.
   - **Start:** one concrete action and its expected output.
   Add a short evidence limit or unresolved assumption only when it affects
   the advice. Give deeper comparisons or optional additions when asked.
5. Follow [selection and conflicts](docs/selection-guide.md). Preserve entry
   review dates and evidence scope; do not imply a collection is fully tested.
   Before installation commands or third-party execution, check the exact
   upstream instructions, dependencies, license and current client support.
   If unavailable, mark compatibility unverified. Advice alone does not
   authorize installation or project changes.

Readiness routes to [this recipe](recipes/repository-readiness.md): begin with
a lightweight context check unless a comprehensive assessment is requested or
justified. The Exadel evaluation concerns one synthetic repository; never
reuse its score for another project. For a genuine coverage gap, use
[discovery guidance](docs/find-more-skills.md) and state the gap.

## Maintain this repository

- Write docs in English; answer users in their language. Keep the README
  short and put details behind links. Preserve existing public skill paths.
- Follow [CONTRIBUTING](CONTRIBUTING.md), the [recipe template](templates/recipe.md)
  and [entry template](templates/catalog-entry.md). Keep third-party code
  upstream and historical evaluation results dated and unchanged.
- Authorized local edits and checks can proceed. Ask before actions outside
  scope unless already authorized, including installs or changes to other
  projects. Never expose private data/secrets or fabricate sources or results.
- Run `python scripts/check_catalog.py` and `git diff --check`. The checker
  also validates the focused index and generated recipe tables. After editing
  `catalog/recipe-skills.json`, run `python scripts/skill_catalog.py build`.
  For search/generator code changes, run `python -m unittest discover -s scripts -p test_skill_catalog.py`.
  Checks cover metadata, table widths and local file links, not external links,
  anchors, source claims, skill execution or client compatibility. Review
  changed aspects separately as needed. There is no application build.
- Report changes, actual check outcomes and material limits.
