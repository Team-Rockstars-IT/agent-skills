# Skill selection report

**Reviewed:** 2026-10-30. **Goal:** provide a broad, technology-agnostic navigation model with explicit labels for web, operational, scientific and codebase-specific workflows. The list is intentionally broad to support later pruning; it is not a recommendation to install everything. Existing skills and upstream implementations remain in place.

**Evidence:** the selected upstream project indexes and several individual files were source-reviewed. Rows drawn from a collection index are discovery-level: the complete instructions and license of each listed skill have not all been checked individually. No skill was installed, run, benchmarked or security-tested in this repository. Selection rationale is editorial, not a claim of effectiveness.

**Inventory:** 42 selection rows, representing 41 distinct source-and-skill
pairs. The analytics skill is cross-listed for marketing and data work.
These counts describe breadth, not validation depth. See the
[quality review](quality-review.md) and [starting workflows](start-here.md).

The [six-choice evaluation](evaluations/2026-10-30/README.md) supersedes the
source-only status for the tested revisions and tasks. In particular, the
SEO audit is excluded from default recommendations and readiness is optional.
Other collection skills retain their original evidence limits.

**How to read:** the skill name is upstream terminology; the source links to the canonical local catalog entry or upstream page. The last column makes scope explicit. Verify the exact current skill path, version, harness, requirements, permissions, license and actual behavior before adoption. Model-agnostic and harness-portable are separate claims.

| Discipline | Skill | Source | Why use it | Value and limits | Scope |
| --- | --- | --- | --- | --- | --- |
| Product and strategy | idea-refine | [Addy](../catalog/skills/development/addy-osmani.md) | Frame vague ideas into concrete options | Useful before committing to a solution; not user research | general |
| Product and strategy | interview-me | [Addy](../catalog/skills/development/addy-osmani.md) | Clarify intent and constraints through questions | Useful when requirements are unclear; may require interaction | general |
| Product and strategy | spec-driven-development | [Addy](../catalog/skills/development/addy-osmani.md) | Create a durable work specification | Aligns acceptance and boundaries; heavier than a short change | general |
| Product and strategy | customer-research | [Marketing](../catalog/skills/marketing-discovery/marketing-skills.md) | Organize customer research for marketing | Adds audience perspective; validate against real user evidence | marketing |
| Product and strategy | ab-testing | [Marketing](../catalog/skills/marketing-discovery/marketing-skills.md) | Plan an experiment | Makes hypotheses and measurement explicit; requires statistical review | marketing |
| Architecture | enterprise-architecture | [Enterprise](../catalog/skills/architecture/enterprise-architecture.md) | Structure architecture views and decisions | Provides C4, ADR and enterprise views; avoid unnecessary framework overhead | general |
| Architecture | api-and-interface-design | [Addy](../catalog/skills/development/addy-osmani.md) | Shape API or module boundaries | Makes contracts and error semantics explicit | general |
| Architecture | improve-codebase-architecture | [Matt](../catalog/skills/development/matt-pocock.md) | Investigate code structure improvement opportunities | Surfaces maintainability candidates; verify against actual code | codebase |
| Development and testing | tdd | [Matt](../catalog/skills/development/matt-pocock.md) | Test behavior through short cycles | Useful at behavioral seams; upstream asks to agree test seams | general |
| Development and testing | test-driven-development | [Addy](../catalog/skills/development/addy-osmani.md) | Apply red-green-refactor | Alternative TDD workflow; select one when instructions overlap | general |
| Development and testing | diagnosing-bugs | [Matt](../catalog/skills/development/matt-pocock.md) | Reproduce and investigate a difficult failure | Adds a feedback loop before fixes | general |
| Development and testing | code-review-and-quality | [Addy](../catalog/skills/development/addy-osmani.md) | Review change quality and scope | Supports review against intent; does not replace reviewers | general |
| Development and testing | debugging-and-error-recovery | [Addy](../catalog/skills/development/addy-osmani.md) | Reproduce and localize errors | Useful for failures and broken feedback loops | general |
| Security and privacy | security-threat-model | [Threat](../catalog/skills/security-privacy/openai-threat-model.md) | Identify assets, trust boundaries and threats | Provides a structured security perspective; not an audit certification | general |
| Security and privacy | differential-review | [Trail](../catalog/skills/security-privacy/trail-of-bits.md) | Review changes for security-sensitive effects | Adds a focused security perspective to ordinary review | codebase |
| Security and privacy | audit-context-building | [Trail](../catalog/skills/security-privacy/trail-of-bits.md) | Build context before security analysis | Improves traceability of security review; adds effort | codebase |
| Security and privacy | security-and-hardening | [Addy](../catalog/skills/development/addy-osmani.md) | Review common security controls | Covers input, auth and integrations; expert review still required | general |
| Security and privacy | security-review | [DevOps](../catalog/skills/operations-reliability/devops-skills.md) | Review infrastructure security posture | Covers permissions and exposure; live access may be sensitive | operations |
| Accessibility and UX | accessibility-audit | [A11y](../catalog/skills/accessibility-ux/humbleteam-accessibility.md) | Review web inputs against WCAG criteria | Produces prioritized findings; not a full conformance assessment | web |
| Accessibility and UX | web-design-guidelines | [Vercel](https://github.com/vercel-labs/agent-skills#web-design-guidelines) | Review web interface quality | Covers accessibility, UX and performance checks; complements manual testing | web |
| Accessibility and UX | frontend-ui-engineering | [Addy](../catalog/skills/development/addy-osmani.md) | Design or modify a user-facing interface | Adds interaction and accessibility concerns; frontend-specific | web |
| Marketing and discovery | seo-audit | [Marketing](../catalog/skills/marketing-discovery/marketing-skills.md) | Diagnose technical and on-page SEO | Helps prioritize crawl and on-page problems; no ranking guarantee | web |
| Marketing and discovery | schema | [Marketing](../catalog/skills/marketing-discovery/marketing-skills.md) | Review or add structured data | Supports search understanding; verify applicable search-engine requirements | web |
| Marketing and discovery | site-architecture | [Marketing](../catalog/skills/marketing-discovery/marketing-skills.md) | Plan page hierarchy and navigation | Adds discoverability and information architecture perspective | web |
| Marketing and discovery | ai-seo | [Marketing](../catalog/skills/marketing-discovery/marketing-skills.md) | Examine AI-search discoverability | Useful as an experiment; outcomes and citations cannot be guaranteed | web |
| Marketing and discovery | analytics | [Marketing](../catalog/skills/marketing-discovery/marketing-skills.md) | Plan or audit analytics measurement | Connects outcomes to measurements; consent and privacy require review | web |
| Operations and reliability | incident | [DevOps](../catalog/skills/operations-reliability/devops-skills.md) | Investigate an incident | Promotes evidence-based diagnosis; requires incident authority | operations |
| Operations and reliability | observability | [DevOps](../catalog/skills/operations-reliability/devops-skills.md) | Review metrics, logs, traces and alerts | Shows whether failures are detectable; access and sensitive data matter | operations |
| Operations and reliability | release-readiness | [DevOps](../catalog/skills/operations-reliability/devops-skills.md) | Review readiness for release | Surfaces outstanding risks; never replaces an authorized release decision | operations |
| Operations and reliability | dr-review | [DevOps](../catalog/skills/operations-reliability/devops-skills.md) | Review recovery and backup posture | Adds restore and recovery evidence; no proof without a restore test | operations |
| Operations and reliability | ci-cd-and-automation | [Addy](../catalog/skills/development/addy-osmani.md) | Design or review delivery pipelines | Connects feedback, deployment and checks; verify tool-specific setup | operations |
| Operations and reliability | shipping-and-launch | [Addy](../catalog/skills/development/addy-osmani.md) | Plan launch and rollback | Helps prepare a release; must not imply deployment authorization | operations |
| Research and evidence | research | [Matt](../catalog/skills/development/matt-pocock.md) | Investigate a question using primary sources | Makes cited research discoverable; check background-agent requirements | general |
| Research and evidence | literature-survey | [AI4S](../catalog/skills/research/ai4s-skills.md) | Produce a scientific literature survey | Supports deeper scientific research; sources need independent verification | science |
| Research and evidence | integrity-auditor | [AI4S](../catalog/skills/research/ai4s-skills.md) | Examine research output for integrity issues | Adds a focused review of research evidence; expert judgment remains necessary | science |
| Data and AI evaluation | agentic-eval | [Awesome](../catalog/skills/development/awesome-copilot.md) | Design evaluations for agent outputs | Adds evaluation rubrics and feedback; validate metrics against real cases | general |
| Data and AI evaluation | experiment-suite | [AI4S](../catalog/skills/research/ai4s-skills.md) | Design scientific experiment artifacts | Highlights reproducibility and provenance; requires technical and scientific review | science |
| Data and AI evaluation | analytics | [Marketing](../catalog/skills/marketing-discovery/marketing-skills.md) | Review measurement events and tracking | Helps connect goals to data; analytics tooling and privacy constraints vary | web |
| Documentation and communication | documentation-and-adrs | [Addy](../catalog/skills/development/addy-osmani.md) | Write decision records and project documentation | Preserves reasoning for later readers; verify facts and audience | general |
| Documentation and communication | copy-editing | [Marketing](../catalog/skills/marketing-discovery/marketing-skills.md) | Improve existing marketing copy | Adds editorial clarity; human review of claims and tone required | marketing |
| Documentation and communication | runbook | [DevOps](../catalog/skills/operations-reliability/devops-skills.md) | Draft or assess an operational runbook | Makes failure response discoverable; exercise it before relying on it | operations |
| Personal development | retro | [Matt](../catalog/skills/development/matt-pocock.md) | Retrospect on the agent environment after a session | Suggests workflow improvements; not a general personal-coaching solution | general |

## Selection and overlap

- Pick one specification workflow per change: existing define-work, Addy SDD, OpenSpec or a separately evaluated toolkit. TDD complements specifications but does not replace them.
- Pick a TDD variant deliberately. Matt's current skill asks for agreed seams and locates refactoring in review; Addy describes red-green-refactor. Incompatible instructions must not silently override the user's request or harness rules.
- A threat model, code review, operational security review and specialist security audit answer different questions. None establishes that a system is secure.
- WCAG is applicable beyond one framework, but the cited accessibility skill is explicitly scoped to web inputs. Review actual interaction, keyboard and assistive technologies with qualified people; a generated finding is not a conformance certificate.
- SEO and structured-data skills are for web discovery; recommendations require current search-engine documentation and actual crawl evidence. AI-search and traffic results cannot be guaranteed.
- Observability tooling and operational review differ from token telemetry. Read-only claims by an upstream do not replace checking the actual commands and access rights.
- Automated claims, privacy or regulatory claims need human assessment and the applicable standards. No legal or clinical advice is inferred from a skill name.

## Why these sources

[Addy Osmani](https://github.com/addyosmani/agent-skills) and [Matt Pocock](https://github.com/mattpocock/skills) cover complementary lifecycle and engineering workflows. [Marketing Skills](https://github.com/coreyhaines31/marketingskills) provides SEO and marketing; current names include `schema` and `analytics`, replacing older names. [Humbleteam](https://github.com/humbleteam/accessibility-audit) explicitly scopes its WCAG audit to web inputs. [Trail of Bits](https://github.com/trailofbits/skills) and [OpenAI threat modeling](https://github.com/openai/skills/blob/main/skills/.curated/security-threat-model/SKILL.md) provide different security perspectives. [DevOps Skills](https://github.com/NotHarshhaa/devops-skills) adds incident and recovery review, while [AI4S](https://github.com/ai4s-research/ai4s-skills) addresses scientific work. [Awesome Copilot](https://github.com/github/awesome-copilot/blob/main/docs/README.skills.md) supplies additional community candidates; individual entries need independent review.

## Gaps and evidence needed

Non-web accessibility, generic quantitative data analysis, broad learning and reflection, and non-software professional disciplines need additional public sources and expert input. Some listed skills are intentionally specialized; a broad discipline index does not make them technology-neutral. For evaluation, use representative tasks, positive and negative triggers, a no-skill baseline, exact versions, permission boundaries and [the evaluation worksheet](evaluation.md). Document failures and user impact rather than only token savings.
