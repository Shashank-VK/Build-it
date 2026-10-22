# Cross-company lessons (cases-product)

Workstream: cases-product · 2026-10-10 · Synthesised from the 11 company files. Each lesson is labelled; sources are the per-company files and their evidence IDs.

## Lessons

### 1. Optimise deeply before re-architecting
OpenAI ran 800M users on a single-primary Postgres; Shopify scaled Rails+MySQL via pods rather than switching stacks. Both treated the proven system as the default and re-architected only at measured walls. [Verified as their stated lesson; applicability varies] (01-openai, 05-shopify)

### 2. Put overload control at the edge and rehearse the spike
Shopify's playbook: leaky-bucket throttle + waiting room at the edge, load tests at 150% of last year's peak, year-round rehearsal calendar. Predictable spikes are a testing problem, not an emergency. [Corroborated] (05-shopify)

### 3. Alert on latency distributions, not just uptime
Stripe's gray failure (green uptime, <1% errors, p95 >4s) and Anthropic's weeks-long quality degradation both hid behind healthy-looking top-line metrics. [Corroborated] (04-stripe, 02-anthropic)

### 4. Agent output volume lands on CI first
OpenAI's build-test-deploy load grew ~10× in ~6 months as Codex-generated PRs multiplied; GitHub's long-running agent migration leaned on 96% prompt-cache hits to stay economical. Capacity-plan the pipeline, and cache aggressively, before scaling agents. [Corroborated; single-source each] (01-openai, 03-github)

### 5. For agents: parallelise reading, serialise writing
Anthropic's orchestrator–worker guidance and Cognition's rebuttal converge: parallel subagents for breadth (3–5, bounded), single-threaded writes, generator-verifier loops, shared scratchpad. [Corroborated] (02-anthropic)

### 6. Judge agent end states, not processes
Anthropic: evaluate final environment outcomes with deterministic graders where possible; small (~20-case) LLM-judge eval sets catch regressions; accept a latency/quality trade-off explicitly (GitHub accepted +16% latency for +8.1pp review quality). [Verified/Corroborated] (02-anthropic, 03-github)

### 7. Make permissions systemic, not prose
Replit: a verbal "don't" is not a permission boundary — destructive actions need automatic environment separation and real approval gates. Anthropic: privacy controls that slow debugging are a feature with a cost — budget for it. [Corroborated] (11-replit, 02-anthropic)

### 8. Postmortems must name the system, not the model
" The AI did it" explains nothing; Replit's and Anthropic's incidents were decided by tool scope, routing, compilers, and environment design. [Corroborated] (11-replit, 02-anthropic)

### 9. Docs are now agent input — write them that way
OpenAI moved docs into code so Codex could consume them; Stripe's Sorbet and Airbnb's RN write-ups show interface clarity is a cross-team multiplier. Machine-consumable docs are infrastructure. [Corroborated] (01-openai, 04-stripe)

### 10. Gradual typing pays via interface clarity
Stripe's Sorbet story is about cross-team contracts (user vs user_id), not just bug counts; the TS migration was justified partly by hiring/toolchain fit. [Corroborated] (04-stripe)

### 11. Don't copy hyperscale architecture pre-scale
Uber's microservice/Kafka/Schemaless stack encodes Uber's load; Spotify's Backstage only became inevitable after cognitive-load overflow (the spreadsheet signal). Build platforms from scaled products, not ahead of them. [Corroborated] (06-uber, 08-spotify)

### 12. Check maintenance status before adopting "canonical" tools
Netflix/SimianArmy is retired; Security Monkey archived 2021; Codex CLI is open-licence but closed-governance. Widely-cited ≠ maintained. [Verified] (07-netflix, 12-tool-intelligence)

### 13. Cross-platform bets are organisational bets
Airbnb's RN sunset was about 3-platform support burden and debugging outside expertise as much as the bridge; and old postmortems can mislead once the stack evolves (Fabric-era RN ≠ bridge-era RN). [Verified/Corroborated] (09-airbnb)

### 14. Dogfood as the iteration loop; publish verifiable numbers
Cursor and OpenAI both iterate by being their own heaviest users; GitHub published session-level telemetry with its agent-productivity claims, while Cursor's unverifiable figures drew criticism. Evidence quality is part of the product story. [Corroborated] (10-cursor, 01-openai, 03-github)

### 15. Cost observability is reliability-adjacent for AI
Uber's AI-cost programme (MCP gateway, prompt caching, real-time cost visibility, −34%/1k requests) and the CTO's budget-burn admission show AI spend needs the same instrumentation as uptime. [Corroborated; single source] (06-uber)

### 16. Banal failures are total failures
Expired TLS certificates (Spotify) and clock drift (Stripe) took down or degraded production with no "interesting" cause. Monitor the boring things: cert expiry, NTP drift, pool configs. [Corroborated] (08-spotify, 04-stripe)
