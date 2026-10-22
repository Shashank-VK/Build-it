# Domain A — Area 11: Domain Boundaries (A vs B vs C)

*Explicit distinctions between Domain A (AI used to build products), Domain B (products built using AI — LLM features inside shipped products), and Domain C (AI automating organisational/business work).*

> Read-only research. Accessed 2026-10-10.

## The one-sentence test

Ask: **who is the user of the AI, and what is the work?**

| Domain | The AI user | The work | Example |
|---|---|---|---|
| **A — AI used to build products** | The builders (engineers, PMs, designers, SREs) | Making the product: research, spec, design, code, test, secure, deploy, operate, document | Claude Code editing your repo; an agent skill generating a PRD draft |
| **B — Products built using AI** | The end customer | Using the shipped product whose feature *is* AI | The "AI assistant" inside the released app; Lovable-the-SaaS as a product |
| **C — AI automating organisational work** | The business operator | Running the business: sales, support ops, HR, finance, marketing | AI triaging support tickets as an ops workflow; AI drafting contracts |

## Why the confusion happens (observed in sources)

1. **The same model family powers both A-tools and B-features.** Claude/Cursor-stack models write code (A) and also answer customer questions inside shipped apps (B). Sources routinely blur "coding agent" with "customer-facing assistant." **Note it explicitly when a source does this.**
2. **Tools that are B-products used in A-workflows.** Lovable, v0, CodeRabbit are *products built using AI* (B) that teams *use to build products* (A). The correct record: the product is B; the usage described in this workstream is A. Both labels apply — to different things.
3. **"AI agents" as an undifferentiated buzzword.** Vendor blogs say "AI agents" for: a coding agent (A), an in-product copilot (B), and a business workflow automator (C) — sometimes in one paragraph (e.g., multi-agent "scrum team as code" repos that mix builder-agents with business-role agents). Disambiguate per-agent: which role does *this* agent play?
4. **AIOps vs AI-SRE-agent vs AI-support-agent.** An AI SRE agent touching production systems is A (operating the product). An AI support agent answering customers is C (business ops) — or B if it's the shipped product's headline feature. Common blur; label by user + work.

## Boundary decisions made in this workstream

| Case | Ruling | Rationale |
|---|---|---|
| Coding agents (Claude Code, Cursor, Copilot, Codex, Aider, Devin) | **A** | Builders using AI to make software |
| Agent instruction files (AGENTS.md, CLAUDE.md, skills) | **A** | Builder workflow artifacts |
| AI PRD/roadmap generators used internally | **A** | Specifying what to build |
| A SaaS "AI PRD generator" sold to customers | **B** (product); using it is **A** | Product vs process |
| v0 / Lovable / Bolt as SaaS products | **B** (products); using them to prototype is **A** | Product vs process |
| AI code review SaaS (CodeRabbit etc.) | **B** (product); using it in your pipeline is **A** | Product vs process |
| In-session `/security-review` agent | **A** | Securing the build |
| AI firewall / AI vuln-scanner SaaS | **B** (product); using it in CI is **A** | Product vs process |
| AI SRE incident-investigation agent | **A** | Operating the product |
| AIOps platform as a purchased product (BigPanda etc.) | **B** (product); using it is **A** | Product vs process |
| AI auto-triaging customer support tickets | **C** | Business operations |
| AI drafting contracts/HR docs/marketing copy | **C** | Business operations |
| AWS "CI/CD for serverless AI" guidance | **A** (process) for **B** (products) | Build process for AI products — label both roles |
| "Scrum team as code" (PO/SM/dev/QA agents) | **A**, with C-edge flagged | Builder roles simulated; note if any agent does business work |
| Figma AI used by designers | **A** | Designing the product |
| In-app AI assistant the end user talks to | **B** | Shipped feature |
| AI-generated marketing site copy | **C** (usually) | Business content, not product-building |

## Rules for future work
- When a source blurs domains, record the blur and assign per the one-sentence test — never silently file a B-product claim as A-evidence or vice versa.
- Metrics don't transfer across the boundary: "80% faster incident investigation" for an A-tool says nothing about a B-feature's quality, and B-product marketing says nothing about A-workflow reliability.
- Failure modes don't transfer either: insecure AI-generated *code* (A) is a different problem from an AI *feature* leaking data (B) or an AI *ops workflow* misrouting tickets (C) — different mitigations, different owners.
