# Review a question in a specialist discipline

**Outcome:** a scoped assessment, design or research report with traceable
evidence, limitations and next actions.
**Use when:** the output concerns architecture, security, accessibility,
research, product, operations, data or communication rather than a code change.
**Prerequisites:** the question, source material and agreed review scope.

## Ingredients

- **Instructions:** applicable project rules and the expected report format.
- **Skill:** one focused procedure selected from the discipline below, when
  suitable. A collection entry is a discovery route; inspect the exact skill.
- **Tools and access:** sources needed to support the specific question.
  Static source access may suffice for a limited review; browser, runtime or
  service access is required for claims about behavior those sources cannot show.
- **Harness:** your existing client with the required access and permissions.

## Choose a discipline

| Desired output | Catalog route | Selection boundary |
| --- | --- | --- |
| Architecture views, boundaries or decisions | [Architecture](../catalog/skills/architecture/README.md) | Tie choices to stakeholder concerns and constraints |
| Security design review or threat model | [Security](../catalog/skills/security-privacy/README.md) | Distinguish threat modeling from runtime security testing |
| Web accessibility findings | [Accessibility and UX](../catalog/skills/accessibility-ux/README.md) | Source review alone cannot establish full conformance |
| Research or source comparison | [Research](../catalog/skills/research/README.md) | Verify source quality and fit outside a scientific context |
| Product framing or experiment plan | [Product and strategy](../catalog/skills/product-strategy/README.md) | Check the exact procedure and domain assumptions |
| Operational review | [Operations](../catalog/skills/operations-reliability/README.md) | Separate advice from authorized changes to running systems |
| Evaluation or measurement plan | [Data and AI](../catalog/skills/data-ai/README.md) | Require representative tasks and explicit success measures |
| Documentation or explanation | [Communication](../catalog/skills/communication/README.md) | Preserve source meaning and verify factual claims |
| SEO or marketing review | [Marketing](../catalog/skills/marketing-discovery/README.md) | The tested SEO revision is excluded from default recommendations |
| Learning or reflection | [Personal development](../catalog/skills/personal-development/README.md) | Coverage is limited; report gaps instead of inventing a skill |

## Steps

1. Define the question, audience, expected artifact and what evidence is needed.
2. Read the discipline index and candidate entry. Select the exact skill only
   after checking its evidence, requirements, scope and upstream instructions.
   If coverage is insufficient, use [discovery](../docs/find-more-skills.md)
   or a bounded general workflow and state the gap.
3. Identify available sources and access. Label any conclusion that needs
   additional evidence as conditional or unverified.
4. Perform the authorized review. Separate observed facts, interpretation,
   proposals and unanswered questions.
5. Deliver prioritized findings, source references, limitations and next steps.

## Ask an agent

```text
Use the specialist-review recipe for [question and discipline]. My sources
are [paths/links] and the output is for [audience]. Select one suitable
procedure, explain what the available evidence can establish and identify
missing access before making claims that depend on it. Produce [artifact]
with source-backed findings, uncertainty and prioritized next steps.
```

## Optional enhancements and tradeoffs

Add another discipline only for a distinct question. Use an independent review
when its value warrants the cost and delegation is authorized. Additional
tools and reviewers do not turn a limited assessment into certification.

## Evidence and checks

Each finding has supporting evidence or an explicit assumption. State what
was inspected, tested and left unverified, and preserve the selected skill's
review date and evaluation scope.
