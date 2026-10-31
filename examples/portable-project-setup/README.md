# Fictional notes project

**Task:** Allow a user to rename an existing note while preserving content and identity.

## Generic instructions

Read repository instructions first. Limit edits to note editing. Do not install dependencies or perform network actions without authorization. Discover documented checks; report unknown commands rather than guessing.

## Context map

The note list opens the editor, which saves through the existing notes service. Exact files and ownership remain unknown until discovery. Preserve authorization and persistence boundaries.

## Acceptance

- Given an editable note, saving a nonempty title updates the list and editor while preserving content.
- Given an empty title, saving shows a useful validation error and preserves the previous title.
- A user without edit rights cannot rename the note.
- Existing identifiers and unrelated notes remain unchanged.

## Execution and evidence

1. Find actual code, access control and checks; update the map with verified paths.
2. If feasible, add a meaningful failing behavioral test, implement the smallest change and run relevant checks.
3. Inspect the diff and record actual commands, outcomes, risks and unsupported checks.
4. Do not claim deployment or user outcomes without separate evidence.

## Handover

**Outcome:** [observed result]. **Changed:** [verified files]. **Checks:** [commands and results]. **Not verified:** [gaps]. **Review focus:** authorization and persistence. **Next step:** [if any].
