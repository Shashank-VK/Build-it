# Uber — product engineering case study

Workstream: cases-product · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Uber's best-documented engineering stories are data-layer (Schemaless, Postgres→MySQL) and geo (H3); 2026 evidence adds AI-cost engineering (MCP gateway). Discovery/design evidence thin.

## Findings

### Product discovery / requirements / design systems
- Claim: Unknown from public engineering sources this pass. Label: **Unknown**.

### Architecture
- Claim: Schemaless — Uber's internal datastore (eng blog, "Designing Schemaless"): a key-value layer over append-only sharded MySQL, buffered writes to survive master failures, a publish-subscribe "triggers" feature for change notification, and global indexes; design inspired by FriendFeed, operational focus inspired by Pinterest. Built because no existing option met requirements in the timeframe. Label: **Verified** — Uber Engineering blog (uber.com/us/en/blog/schemaless-part-one-mysql-datastore/), via live search result.
- Claim: Postgres→MySQL migration (2014–2016): Postgres pain points cited were write amplification (1 logical write → multiple physical writes), inefficient physical-level replication that blocked cross-version upgrades, and painful schema changes; MySQL/InnoDB offered statement-level replication and better-understood caching/connection pooling for Uber's workload. Label: **Corroborated** — StackShare timeline + community analysis; the decision rationale matches Uber's 2016 engineering post; exact "4×" amplification figures in some retellings are secondary gloss — flag.
- Claim: Geospatial matching built on H3 (open-sourced hexagonal hierarchical spatial index) turning nearest-driver search into a grid lookup; driver GPS pings (every ~4s) buffered through Kafka as a shock absorber (~250k writes/s order of magnitude). Label: **Corroborated** — Medium system-design summaries; H3 open-sourcing is public record.
- Claim: ~1,000 MCP server interactions routed through a single unified gateway for central policy enforcement (2026), as part of an AI-cost programme: cost per 1,000 agent requests −34% and per session −52% from peak, while weekly active AI-coding-tool users rose 7× and agent requests 9.4× (Feb–Aug 2026); total spend roughly flat since April. Levers: vendor-neutral managed agents, prompt caching, MCP/schema efficiency, reusable agent skills, real-time cost visibility. Label: **Corroborated** — The Stack reporting Uber engineering blog posts by CTO Praveen Naga and Distinguished Engineer Uday Medisetty (Sep 2026). Single journalistic source; figures are Uber-reported.

### Implementation
- Claim: Project Mezzanine (Schemaless v1): Python, ~5 months from idea to production (2014). Label: **Corroborated** — StackShare timeline.
- Claim: AI-cost work specifically attacked schema bloat from MCP servers (tool definitions inflating context). Label: **Corroborated** (The Stack).

### AI usage
- Claim: Internal AI coding tools at large scale (7× WAU growth); prompt caching and reusable "agent skills" as efficiency levers; real-time cost visibility given to engineers. Label: **Corroborated** (The Stack/Uber eng blog).
- Claim: Uber's CTO publicly noted the company had "burned" through its annual AI budget in months (early 2026), prompting the cost programme. Label: **Corroborated** (The Stack).

### Automation / testing
- Claim: Unknown specifics this pass. Label: **Unknown**.

### Security
- Claim: MCP gateway exists partly for "central policy enforcement" — a security/control point for agent tool access. Label: **Corroborated** (The Stack). Note: centralised gateways create a single point of policy failure — implied, label **Inferred**.

### Deployment / monitoring
- Claim: Unknown specifics this pass. Label: **Unknown**.

### User feedback / business outcomes
- Claim: Unknown. Label: **Unknown**.

### Documented failures
1. Postgres write-amplification and replication-upgrade pain as the forcing function for the MySQL move (design failure of the original stack at scale, not an incident). Label: **Corroborated**.
2. AI budget overshoot (early 2026) — organisational/process failure triggering the cost-engineering programme. Label: **Corroborated**.
3. Counter-evidence / anti-pattern warning: copying Uber-style microservice/Kafka architecture at startup scale kills velocity (Medium opinion piece, Dec 2025) — useful as an applicability caveat on Uber's architecture. Label: **Corroborated** (opinion; not an Uber failure per se).

### Transferable lessons
- Optimise for operability over elegance once writes dominate ("Performance > feature completeness, Operability > elegance, Stability > purity"). Label: **Corroborated** (community synthesis of Uber's rationale).
- A unified policy gateway for agent tool access (MCP) lets cost and security be managed at one point. Label: **Corroborated** (single source).
- Give engineers real-time cost visibility — cost engineering needs the same observability as reliability. Label: **Corroborated**.
- Don't copy hyperscale architecture pre-scale: complexity without the load that pays for it. Label: **Corroborated** (opinion).

## Sources
| ID | Claim area | URL | Type | Author/org | Date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| UB-01 | Schemaless design | https://www.uber.com/us/en/blog/schemaless-part-one-mysql-datastore/ | Primary (eng blog) | Uber Engineering | 2016 | 2026-10-10 | High |
| UB-02 | Postgres→MySQL timeline, Mezzanine, stack history | https://stackshare.io/stack-history-timeline-uber-tech-stack-evolution | Secondary (timeline) | StackShare | ~2019 | 2026-10-10 | Low-medium |
| UB-03 | Switch lessons, operability framing | https://dev.to/dev_tips/why-uber-ditched-postgres-for-mysql-what-every-developer-can-learn-from-it-j3h | Secondary (analysis) | dev.to | ~2025 | 2026-10-10 | Low-medium |
| UB-04 | MCP gateway, AI cost cuts | https://www.thestack.technology/1-000-mcp-servers-zero-schema-bloat-ubers-assault-on-ai-costs/ | Secondary (trade press) | The Stack | Sep 2026 | 2026-10-10 | Medium (single source, Uber-reported figures) |
| UB-05 | H3, Kafka ingestion sketch | https://medium.com/@frankdotdev/how-uber-handles-millions-of-rides-a-system-design-masterclass-321705543f47 | Secondary (analysis) | Medium author | Feb 2026 | 2026-10-10 | Low |
| UB-06 | Anti-copying-Uber-arch opinion | https://medium.com/@logicoverlatte/why-copying-ubers-architecture-hurts-your-career-dfa33beba178 | Secondary (opinion) | Medium author | Dec 2025 | 2026-10-10 | Low (opinion) |
