# Outcome

**Use when:** the situation that makes this recipe useful.
**Input:** required material, intent and constraints.

## Ingredients

- Applicable instructions and evidence sources.
- Existing capabilities first. List additional skills, tools or access only
  when the work requires them; name any programming-language/client limitation.

## Steps

1. Define the result and how to assess it.
2. Perform the smallest useful actions using relevant context.
3. Check the result and report remaining uncertainty.

## Ask an agent

```text
Describe the goal, inputs, scope, expected output and relevant constraints.
```

## Optional enhancements and tradeoffs

## Evidence and checks

Define the observable result and verification limits. Link relevant entries
for evidence, review dates and requirements; do not imply a catalog reference
is installed, current or tested on the reader's project.
Checks must fit the artifact: a brief, design or analysis need not have a
repository, shell, diff or test suite.

For concrete upstream choices, add records to
[recipe-skills.json](../catalog/recipe-skills.json) with this recipe's path.
Run `python scripts/skill_catalog.py build` to insert the source/tag/evidence
table before Steps. Edit the JSON rather than the generated table.
