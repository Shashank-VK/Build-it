# Domain A — Area 10: Documentation and Maintenance (AI-assisted)

*How AI assists with writing and maintaining product documentation, and with ongoing codebase maintenance (dependency updates, refactoring, onboarding) — AI used in the process of sustaining the product.*

> Read-only research. No installation, ranking, or recommendations. Accessed 2026-10-10 unless noted.

## 1. What teams demonstrably do

### Docs as agent context (Microsoft ISE — first-party practice)
- **Claim (Verified — Microsoft engineering blog, Sep 2026):** Microsoft's Industrial Software Engineering team treats documentation as the agent's source code: date long-lived docs (`Last reviewed: 2026-05`) so humans and models can judge staleness; link don't duplicate (top-level instructions point to ADRs); be the source of truth not a pointer outward (agents can't follow links to private wikis/SharePoint/Slack — needed info must live in the repo); encode negatives; **keep it current or delete it** — "stale docs are worse than none — they actively mislead the model"; treat doc drift as a CI bug (link-check every PR, grep gates failing when renamed symbols persist in `docs/**`, warnings when env-var names in instruction files no longer exist in code); write docs for the model's observed mistakes (every recurring AI mistake is a missing line of documentation).
- Source: https://devblogs.microsoft.com/ise/documentation-is-the-new-source-code/ (evidence class: primary technical; Sep 2026)

### AI agents vs documentation quality — the DoGBench result
- **Claim (Corroborated):** DoGBench (a benchmark judging agent-written docs against real maintainer rubrics) audited 1,267 submissions: 45.5% had task-completion gaps (missed prerequisites, steps, verification paths), 36.6% technical inaccuracies, 32.5% omitted core concepts, 6.1% fabricated content (invented classes, flags, endpoints). Agents guess, hallucinate plausible-but-breaking details, or overwrite stable sections. Vendors already sell "automated documentation updates" — the benchmark suggests the feature is liability-grade until staleness-detection and invention-avoidance improve.
- Source: https://www.webpronews.com/ai-agents-struggle-to-write-usable-software-docs/ (WebProNews; Oct 2026; evidence class: secondary interpretation of benchmark)

### AI won't fix documentation debt
- **Claim (Corroborated):** Practitioner consensus (SD Times, Oct 2026): AI-generated content increases volume and often reduces clarity; AI lacks the narrative context (the why, intent, fit in the broader UX) for great docs; output is "fast, plausible, and wrong" ("AI slop"). Humans add narrative context; AI needs structure. Quality-over-volume: auto-generated changelogs ≠ reliable docs.
- Source: https://sdtimes.com/softwaredev/great-documentation-takes-more-than-ai/ (SD Times; ~Mar 2026)

### Writing docs so AI can use them
- **Claim (Corroborated):** Four silent doc failures that break AI consumption (present in ~90% of dev docs per practitioner): context-dependent sections ("as mentioned above" — references vanish when chunked); visual-only explanations (critical details in screenshots AI can't see); incomplete code examples (missing imports/config/error handling); JavaScript-rendered content (crawlers see blank pages). Fixes: self-contained sections, text descriptions of visuals, copy-paste-runnable examples, SSR/static generation.
- Source: https://medium.com/@buildwithcodeclarity/your-documentation-is-invisible-to-ai-and-its-killing-your-adoption-eb8256ffa73c (Medium; Nov 2025)

### Maintenance workflows
- **Claim (Corroborated):** Agents are routinely used for maintenance-class work: dependency updates, bug-backlog routine fixes, test creation for legacy modules, and codebase Q&A for onboarding (Anthropic reports Claude Code "particularly effective at explaining how projects work, tackling bug backlogs with routine fixes"). PRD Studio's "Recover" workflow (file 02) reconstructs specs from existing systems — a maintenance-enabling practice. Git-history-aware agents answer "why is it this way" from commits/PRs.
- Sources: https://www.eweek.com/news/anthropic-claude-code-launch/ ; https://github.com/bboysky/prd-studio
- **Negative evidence:** silently-failing tests left for two weeks by an agent (recovery cost more than original implementation); agents overwriting stable doc sections that needed no touch (DoGBench). **Corroborated.**

## 2. Tools and workflows
| Tool/pattern | Role |
|---|---|
| Doc-generation agents / Doc-E.ai | Draft docs from code + community discussions; suggest updates |
| CI doc-drift gates | Link-check per PR; grep for renamed symbols; env-var consistency checks |
| Dated docs + ADRs in repo | Staleness signals for humans and models |
| "Recover" spec workflows | Reconstruct current-state docs from implementation |
| Codebase Q&A agents | Onboarding; "explain this module" |

## 3. Failure modes
1. **Fabrication in docs.** 6.1% invented classes/flags/endpoints; 36.6% technical inaccuracies (DoGBench). **Corroborated.**
2. **Staleness amplification.** AI confidently runs stale commands from stale docs; stale docs actively mislead models — worse than none. **Verified (Microsoft ISE).**
3. **Volume without clarity.** Auto-generated docs increase noise; "fast, plausible, and wrong." **Corroborated.**
4. **Overwriting stable sections.** Agents "fix" docs that weren't broken. **Corroborated (DoGBench).**
5. **Private-context blindness.** Agents can't reach wikis/SharePoint/Slack — docs that point outward are dead ends. **Verified (Microsoft ISE).**

## 4. Costs / latency / reliability
- Doc generation is cheap (chat-scale inference); the cost is verification — every generated doc needs a maintainer-grade review against the DoGBench-style rubric. **Inferred.**
- CI drift-gates are cheap to run (grep/link-check) and prevent the expensive failure (misled agents). **Inferred from Microsoft practice.**

## 5. Human correction burden
- Documentation is where the correction burden is most visible: 45.5% task-completion gaps mean nearly half of agent doc output needs substantive repair. The durable practice is docs-as-code with CI gates + human ownership, not "AI maintains the docs." **Corroborated.**

## 6. Where AI genuinely helps vs where it creates rework
- **Genuinely helps:** first drafts from code; keeping API references in sync via CI-detected drift; answering codebase questions for onboarding; reconstructing As-Is specs.
- **Creates rework:** plausible-but-wrong conceptual docs; invented APIs; stale-command propagation; doc volume that buries the narrative.

## 7. Boundary notes (A vs B vs C)
- **Domain A:** AI helping *your team* document/maintain *your* product. **Domain B:** a shipped docs *product* with AI inside (e.g., an AI docs-search SaaS — the product is B; using it is A). **Domain C:** AI writing business documentation (policies, reports) — organizational. The "docs invisible to AI" problem is A-flavored (docs as agent context); "AI answers support questions from docs" is B or C depending on who the user is.

## Evidence register (this file)
| # | Claim | URL | Source type | Author/org | Pub date | Confidence | Class |
|---|---|---|---|---|---|---|---|
| 10.1 | Docs-as-source-code; doc drift as CI bug; stale docs worse than none | https://devblogs.microsoft.com/ise/documentation-is-the-new-source-code/ | Vendor eng blog | Microsoft ISE | Sep 2026 | High | primary technical |
| 10.2 | DoGBench: 45.5% gaps, 36.6% inaccuracies, 6.1% fabrication (n=1,267) | https://www.webpronews.com/ai-agents-struggle-to-write-usable-software-docs/ | News on benchmark | WebProNews | Oct 2026 | Medium | secondary interpretation |
| 10.3 | AI won't fix docs debt; "fast, plausible, and wrong" | https://sdtimes.com/softwaredev/great-documentation-takes-more-than-ai/ | Trade press | SD Times | ~Mar 2026 | Medium | corroborating |
| 10.4 | Four silent doc failures (chunking, visuals, examples, JS rendering) | https://medium.com/@buildwithcodeclarity/your-documentation-is-invisible-to-ai-and-its-killing-your-adoption-eb8256ffa73c | Practitioner essay | Code & Clarity | Nov 2025 | Medium | first-hand practitioner |
| 10.5 | Agents for bug backlogs, legacy test creation, codebase explanation | https://www.eweek.com/news/anthropic-claude-code-launch/ | News | eWeek | ~Oct 2025 | Low–Medium (vendor-adjacent) | secondary interpretation |
