# The Complete Product Engineering Intelligence Report

*How world-class companies ideate, design, prototype, build, test, secure, ship, and continuously improve products using AI, agents, automation, and engineering discipline.*

**Research date:** 2026-10-10 · **Method:** 29 parallel research workstreams (20 in the main phase, 9 in a follow-up phase on compulsory disciplines the report missed) across the public internet (official engineering blogs, docs, repos, papers, talks, postmortems **and** Reddit, X, Hacker News, practitioner blogs, GitHub issues/PRs/discussions, podcasts, teardowns, benchmarks, failure reports) · **Evidence discipline:** every major claim labeled **Verified** / **Corroborated** / **Inferred** / **Proposed** / **Unknown** · **1,453 evidence rows** · **1,119 deduped sources**

This is read-only research: discover, inspect, identify, verify, categorize, explain usage, record sources. Nothing here was installed, built, configured, ranked, or recommended.

## How to read this report

- Start with **01** (executive findings) — the 30 most important findings, each evidence-labeled.
- **02** keeps the three AI domains rigorously distinct: **A** = AI used *to build* products · **B** = products *built using* AI · **C** = AI *automating organisational work*. They have different responsibilities, failure modes, and safety requirements — conflating them is one of the most common errors in the literature.
- **03–06** cover the lifecycle, the company forensics, AI/agent architecture, and the automation stack.
- **07–12** cover authenticity/design, functional completeness, accessibility/performance/UX, security/privacy/governance, testing/quality/deployment/ops, and business viability.
- **13–16** cover delivery economics, the rules and anti-pattern catalogues, reference architecture, and the implementation roadmap (labeled Proposed throughout).
- **17** is the checklists/templates index; **18** explains the evidence-label system and lists the load-bearing findings; **19** is the evidence-grounded analysis of important topics the original brief missed; **20** is the follow-up phase — 13 compulsory disciplines the report still missed, researched after the user said to ignore the original prompt and fill the gaps.
- **Appendices A–E** hold the expansion digests (37 more companies, 230 more tools, the fringe-practices menagerie, the 16 forensic verdicts, the merged 252-record tool register).
- **evidence/** holds the merged evidence register (1,081 rows), the deduped source directory (675 sources), unresolved questions, and the coverage matrix (the final research audit input).

Raw per-workstream research (the full depth behind every summary) lives in `../research/` — 29 streams, each with its own evidence register.

## The 20 sections

| # | File | Contents |
|---|---|---|
| 01 | [01-executive-findings.md](01-executive-findings.md) | The 30 most important findings, evidence-labeled |
| 02 | [02-three-ai-domains.md](02-three-ai-domains.md) | Domains A / B / C — definitions, failure modes, economics, boundaries |
| 03 | [03-product-lifecycle.md](03-product-lifecycle.md) | The complete iterative lifecycle, end-to-end with gates |
| 04 | [04-company-case-studies.md](04-company-case-studies.md) | Forensic verdicts, instructive cases, narrative-vs-evidence contradictions |
| 05 | [05-ai-agent-architecture.md](05-ai-agent-architecture.md) | The product is the harness, not the model; evals; agent security |
| 06 | [06-automation-stack-workflows.md](06-automation-stack-workflows.md) | 12-layer stack, reliability mechanics, workflow reconstructions |
| 07 | [07-authenticity-anti-slop.md](07-authenticity-anti-slop.md) | Product authenticity, visual identity, anti-pattern catalogue (condensed) |
| 08 | [08-functional-completeness.md](08-functional-completeness.md) | Route-by-route audit method, automation limits, demo honesty |
| 09 | [09-accessibility-performance-ux.md](09-accessibility-performance-ux.md) | WCAG/EAA, Core Web Vitals, UX state matrix, polish details |
| 10 | [10-security-privacy-governance.md](10-security-privacy-governance.md) | App/agent security, classified controls (§25), privacy law |
| 11 | [11-testing-quality-deployment-ops.md](11-testing-quality-deployment-ops.md) | Testing, quality gates, CI/CD, incident response, feedback loop |
| 12 | [12-business-viability.md](12-business-viability.md) | Adoption, AI unit economics, cautionary cases |
| 13 | [13-bottleneck-analysis.md](13-bottleneck-analysis.md) | Delivery economics; the bottleneck shifts downstream |
| 14 | [14-rules-anti-patterns.md](14-rules-anti-patterns.md) | 34 classified rules; 19 anti-patterns with counterexamples |
| 15 | [15-reference-architecture.md](15-reference-architecture.md) | Minimum-viable + advanced architectures |
| 16 | [16-implementation-roadmap.md](16-implementation-roadmap.md) | Phased roadmap (**Proposed** synthesis) |
| 17 | [17-checklists-templates.md](17-checklists-templates.md) | Full checklists + index of 18 templates |
| 18 | [18-evidence-register.md](18-evidence-register.md) | Label guide, load-bearing findings, unresolved questions |
| 19 | [19-missing-topics.md](19-missing-topics.md) | 11 ranked topics the brief missed, evidence-grounded |
| 20 | [20-compulsory-disciplines.md](20-compulsory-disciplines.md) | 13 compulsory disciplines the report missed (follow-up phase) |

## Appendices & evidence

- [../appendices/A-expansion-companies.md](../appendices/A-expansion-companies.md) — 37 more companies, ranked by instructiveness
- [../appendices/B-expansion-tools.md](../appendices/B-expansion-tools.md) — 230 neutral tool-intelligence records by status
- [../appendices/C-expansion-practices.md](../appendices/C-expansion-practices.md) — the fringe: contrarian, abandoned, and unwritten practices
- [../appendices/D-forensics-digest.md](../appendices/D-forensics-digest.md) — 16 forensic verdicts + narrative contradictions with receipts
- [../appendices/E-tool-intelligence-register.md](../appendices/E-tool-intelligence-register.md) — merged 252-record tool register
- [../evidence/merged-evidence-register.md](../evidence/merged-evidence-register.md) — 1,453 evidence rows
- [../evidence/source-directory.md](../evidence/source-directory.md) — 1,119 deduped sources
- [../evidence/unresolved-questions.md](../evidence/unresolved-questions.md) — 50+ open questions
- [../evidence/coverage-matrix.md](../evidence/coverage-matrix.md) — per-section audit: what each source type established
- [../evidence/final-research-audit.md](../evidence/final-research-audit.md) — the mandatory final research audit

## A note on honesty

This report refuses several common temptations, deliberately:

- **No hagiography.** Every company's polished narrative was audited against practitioner evidence (§04, Appendix D). No company gets a free pass.
- **No invented numbers.** Where the public record has no measurement (AI-era maintenance cost, hyperscaler internal defect rates, commercial agent success rates, agentic workflow ROI), the report says **Unknown** — 50+ such questions are listed in `evidence/unresolved-questions.md`.
- **No label upgrades.** Vendor-published figures are direction-trusted but magnitude-discounted; single-source claims stay single-source; Proposed designs are never presented as company practice.
- **No recommendations-as-advice.** Rules, checklists, and architectures are reported as evidence-backed findings with their classifications and boundary conditions — not as prescriptions to adopt, and never as tool rankings.
