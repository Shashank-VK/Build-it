# Evidence register (cases-product)

Master index of evidence items backing the 11 company files. Fields per item: ID · claim · URL · type · author/org · date · accessed 2026-10-10 · confidence · corroboration · contradictions · implication. "Unknown" marks methodology debt, not absence of evidence.

## High-confidence (primary sources read via original or faithful mirror)

| ID | Claim | URL | Type | Author/org | Date | Confidence | Corroboration / contradictions | Implication |
|---|---|---|---|---|---|---|---|---|
| E-01 | OpenAI: single-primary Postgres, ~50 replicas, SEV-0 ImageGen, PgBouncer/cache-locking optimisations | https://openai.com/index/scaling-postgresql/ (via https://venturebeat.com/data/how-openai-is-scaling-the-postgresql-database-to-800-million-users) | Primary eng blog / secondary reporting | Bohan Zhang / OpenAI | 2026-01 | High | Multiple independent reports agree on figures | Optimise-first lesson; Postgres ceiling data point |
| E-02 | Anthropic: orchestrator–worker research system, 3–5 subagents, thinking scratchpad, end-state evals | https://www.anthropic.com/engineering/built-multi-agent-research-system | Primary eng blog | Anthropic Engineering | 2025-06 | High | Community rebuilds corroborate mechanics | Reference architecture for multi-agent systems |
| E-03 | Anthropic: three-issues postmortem (routing, TPU, XLA), 16% peak, privacy-limited debugging | https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues | Primary eng blog | Sam McAllister / Anthropic | 2025-09-17 | High | Simon Willison notes reputation hit; users split on resolution | Infra-bug overlap as worst debugging case |
| E-04 | Anthropic: workflows-vs-agents taxonomy ("Building Effective Agents") | https://www.anthropic.com/engineering/building-effective-agents | Primary eng blog | Anthropic Engineering | 2024-12 | High | Widely cited, uncontested | Baseline agent-design doctrine |
| E-05 | GitHub: 27% acceptance predicts perceived productivity (MAPS 2022) | DOI 10.1145/3520312.3534864 (via community notes) | Peer-reviewed paper | Ziegler, Kalliamvakou, Li et al. | 2022 | High | Consistent with GitHub's later 30% telemetry | Acceptance = feeling metric, not quality metric |
| E-06 | Airbnb: React Native sunset, goals missed, 3-platform burden | https://medium.com/airbnb-engineering/sunsetting-react-native-1868ba28e30a | Primary eng blog | Gabriel Peal / Airbnb | 2018 | High | 2025 rebuttal argues staleness, not inaccuracy | Cross-platform = organisational bet |
| E-07 | Uber: Schemaless design (key-value over sharded MySQL, triggers, global indexes) | https://www.uber.com/us/en/blog/schemaless-part-one-mysql-datastore/ | Primary eng blog | Uber Engineering | 2016 | High | StackShare timeline corroborates timeline | Operability-over-elegance precedent |
| E-08 | Netflix: SimianArmy RETIRED | https://github.com/Netflix/SimianArmy | Primary (repo state) | Netflix | current | High | Standalone chaosmonkey exists, low activity | Don't adopt retired "canonical" tools |
| E-09 | Netflix: security_monkey archived 2021-09-17 | https://github.com/netflix/security_monkey/issues | Primary (repo state) | Netflix | 2021-09-17 | High | — | Deprecated; alternatives needed |

## Medium-confidence (secondary reporting, interviews, first-party via press)

| ID | Claim | URL | Type | Author/org | Date | Confidence | Corroboration / contradictions | Implication |
|---|---|---|---|---|---|---|---|---|
| E-10 | OpenAI agentic software factory: PR load ~10×, perf harness, domain-specialist reviews, docs-in-code | https://newsletter.pragmaticengineer.com/p/openai-software-factory | Journalism (interview) | Gergely Orosz / Venkat Venkataramani (VP Eng, OpenAI) | ~2026-09 | Medium | No first-party OpenAI post located; figures single-source | CI capacity planning for agent output |
| E-11 | Stripe: Sorbet rationale (user/user_id ambiguity) | https://softwareengineeringdaily.com/wp-content/uploads/2020/03/SED1033-Sorbet.pdf | Podcast transcript | SED / Stripe engineers | 2020 | Medium | HN ex-employee accounts agree | Type systems as interface-clarity tools |
| E-12 | Stripe: 3.7M-line Flow→TS migration, codemod, 97k→37k suppressions | https://www.itmagination.com/blog/360deg-it-check-46-stripe-typescript-flutter-ruby-on-rails | Summary of Stripe blog | itmagination | ~2023 | Medium | Consistent with Stripe's public post | Migration tooling + honest coverage metrics |
| E-13 | GitHub: 60M Copilot code reviews, 1-in-5 PRs, +8.1pp agentic gain, +16% latency accepted | (github.blog, via https://github.com/tomaspalsson/flow research note) | Vendor blog via research note | GitHub | 2026-03-05 | Medium | Vendor self-grading; no human head-to-head | Review metrics need independent benchmarks |
| E-14 | GitHub: 832K-line Rust migration, one engineer agent-assisted, 96.22% prompt-cache hit | https://www.explainx.ai/blog/github-copilot-runtime-rust-migration-2026 | Engineering blog | explainx.ai | 2026-10 | Low-medium | Single source; vendor-framed | Prompt caching as economic lever |
| E-15 | Shopify: pods/Sorting Hat/edge throttle/queue fairness/Genghis at 150% | https://devops-daily.com/posts/how-shopify-survives-black-friday-flash-sale-playbook + https://www.youtube.com/watch?v=wJT9S9erzTM | Playbook + video breakdown | devops-daily / YouTube | 2026-10 | Medium | Consistent with Shopify's published history | Flash-sale resilience playbook |
| E-16 | Shopify: BFCM 2025 $14.6B, 489M req/min | (same as E-15) | Secondary | devops-daily | 2026-10 | Medium | Attributed to Shopify recap; unaudited | Scale reference point |
| E-17 | Uber: MCP gateway (1,000+ servers), −34%/1k reqs, budget burned in months | https://www.thestack.technology/1-000-mcp-servers-zero-schema-bloat-ubers-assault-on-ai-costs/ | Trade press | The Stack (Uber eng blog) | 2026-09 | Medium | Single journalistic source; Uber-reported figures | AI cost observability pattern |
| E-18 | Spotify/Backstage: System Z origin, CNCF, 3,400 orgs, monthly releases | https://dev.to/saaro_net/backstage-2026-from-service-catalog-to-ai-hub-for-developer-portals-4dn | Conference reporting | dev.to | 2026-09 | Medium | CNCF documentary reporting agrees | Platform-after-scale conditions |
| E-19 | Backstage CVE-2025-55285 (Scaffolder log flaw, fixed 2.1.1) | https://platformengineering.com/?p=175886 | Trade analysis | platformengineering.com | 2026-10 | Medium | Single source; technically plausible | Secrets-in-golden-paths attack surface |
| E-20 | Replit: Jul 2025 Agent DB deletion, CEO apology, dev/prod separation | https://thecyberexpress.com/replit-ai-agent-incident/ | Press (quotes company) | The Cyber Express / Replit | 2025-07 | Medium | Windows Central + widespread coverage agree | Permission boundaries must be systemic |
| E-21 | Cursor: CEO on wilderness year, beta, custom models | (founder-wiki transcript mirror) | Interview transcript | founder-wiki | ~2026-04 | Low-medium | Tertiary mirror of video interview | Dogfood-first iteration narrative |
| E-22 | Anthropic Dynamic Workflows (Opus 4.8, JS orchestration, 16/1,000 agents) | https://moselwal.com/blog/dynamic-workflows-claude-opus-4-8-multi-agent-harness | Secondary | Moselwal | 2026-05 | Low-medium | Single source; no primary captured | Watch: unconfirmed product claim |
| E-23 | Cognition: "Don't Build Multi-Agents" → Apr 2026 resolution (parallelise reading, serialise writing) | https://cognition.ai/blog/dont-build-multi-agents | Primary blog | Walden Yan / Cognition | 2025-06; 2026-04 | Medium | Resolves Anthropic debate | Multi-agent design rule |
| E-24 | Codex CLI: open-source Apache-2.0, Rust rewrite, no external PRs, ~125k stars | https://dev.to/ingridvidal/codex-cli-review-2026-openais-terminal-coding-agent-tested-on-its-docs-5d4m | Review | dev.to | 2026-10 | Low-medium | Consistent with github.com/openai/codex public state | Open-licence, closed-governance caveat |

## Low-confidence / single-source narratives (use with caution)

| ID | Claim | URL | Confidence | Note |
|---|---|---|---|---|
| E-25 | OpenAI Dec 2024 (4h22m) and Jun 2025 (13h) outages | beehiiv compilation | Low-medium | No official OpenAI write-up located — official-vs-unofficial gap |
| E-26 | Stripe time-drift incident (early 2022) | Medium warstories | Low-medium | No official Stripe post located |
| E-27 | Stripe latency gray-failure postmortem | Medium warstories | Low-medium | Incident date/identity unclear; mechanics plausible |
| E-28 | Spotify certificate-expiry outage | Medium warstories | Low-medium | No official Spotify postmortem located |
| E-29 | Replit Helium/Neon driver postmortem (agent misdiagnosis) | community gist | Low | Single first-hand account; technical specifics unverified |
| E-30 | Cursor 400M req/day, $1B ARR/24mo, 90-min RL retrain, speculative edits | Medium (The AI Engineer) | Low | Unverified internals; transparency-gap critique is the verified part |
| E-31 | Airbnb COVID forecasting failure (B-DARMA, two-part model) | Medium reading list | Low | Tertiary summary of Airbnb post |
| E-32 | Uber Postgres write-amplification "4×" figure | dev.to analysis | Low-medium | Secondary gloss on Uber's 2016 rationale; treat figure as approximate |

## Methodology debt (explicit unknowns)
- D-01: Stripe Sorbet / Netflix EVCache / Toxiproxy / Uber H3 2026 maintenance activity not re-verified.
- D-02: GitHub github.blog primaries (code-review metrics, Rust migration) not fetched first-party; cited via research notes.
- D-03: OpenAI incident narratives (E-25) lack official write-ups; Stripe/Spotify incident narratives (E-26–E-28) single-sourced.
- D-04: Cursor pricing/rate-limit backlash (2025) widely discussed but no evidence captured — not asserted.
- D-05: Product discovery / requirements / design-system practice largely Unknown across companies — a systematic gap in public engineering writing, recorded as Unknown rather than inferred.
- D-06: Diminishing-returns stop applied: searches beyond ~2–3 per company returned recycled secondary content; per-company files favour fewer, better-labelled claims over exhaustive coverage.
