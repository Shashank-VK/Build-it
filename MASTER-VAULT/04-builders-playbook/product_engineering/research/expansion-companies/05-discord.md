# Discord — product engineering case study

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Discord's engineering blog is one of the most candid scaling archives in the industry (Elixir at 5M concurrent, Rust NIFs at 11M, ScyllaDB, voice SFUs). This file covers backend/scale; product-design material is thinner. Community sources add the contrarian product view.

## Findings

### Architecture
- Claim: One Erlang process per connection on the BEAM VM carries the gateway WebSocket tier (11M concurrent users); guild isolation means one guild's crash spike doesn't spill into others. Label: **Corroborated** — Discord eng blog titles + secondary architecture summaries (insidethestack, handbook-academy).
- Claim: Voice is a separate fleet: C++ SFU (Selective Forwarding Unit) servers with signalling over the Elixir gateway; ~850 servers across 13 regions, 2.6M+ concurrent voice users, 220+ Gbps egress. They skip standard WebRTC ICE negotiation — the endpoint is assigned by service discovery (etcd) — which also hides client IPs from each other (DDoS defence). Label: **Corroborated** — handbook-academy synthesis of Discord's voice blog.
- Claim: Voice DDoS mitigation is automated and routine: on traffic spikes, remove the node from etcd, migrate voice state to a new server, push the new endpoint to clients over the gateway WebSocket. Label: **Corroborated** (same).

### Implementation
- Claim: Elixir's immutable data structures became the bottleneck at guild scale: adding a member to a 100k-member sorted member list meant rebuilding the whole list. The team tried several Elixir-native data structures, then time-boxed a one-week Rust spike via Rustler (NIFs): worst-case insertion went from 640µs (Elixir OrderedSet) to 2.85µs, and the final Rust SortedSet hit 0.61µs best / 3.68µs worst at up to 1M items — ~160x worst-case improvement. Lesson: keep the concurrency language, replace the hot data structure — don't rewrite the system to fix one structure. Label: **Corroborated** — Discord blog text extensively quoted in secondary sources (timothya.com, changelog); official blog at discord.com located but not fetched this pass.
- Claim: The "Read States" service (tracking which messages each user has read) was the concrete system that got the Rust treatment. Label: **Corroborated** (same sources).
- Claim: Discord later moved "why and how" from Go to Rust for other services. Label: **Corroborated** — Discord blog title listed ("Why Discord is switching from Go to Rust"); details not fetched — Unknown specifics.
- Claim: Message storage moved from Cassandra (177 nodes, p99 read latency 40–125ms) to ScyllaDB (72 nodes, p99 15ms); shard-per-core C++ design eliminated JVM GC pauses. Label: **Corroborated** — handbook-academy synthesis; underlying Discord blog ("How Discord Stores Trillions of Messages") not fetched this pass — treat figures as Medium confidence.
- Claim: Manifold (open source) groups recipient PIDs by remote Erlang node and sends one cross-node copy per node instead of one per PID — halved outgoing packets/sec on deployment. Label: **Corroborated** — handbook-academy (citing Discord's open-source release).
- Claim: Push-request bursts (>1M/min) handled with Elixir GenStage for back-pressure and load-shedding. Label: **Corroborated** — elixir-lang.org case study + Discord blog title.

### Testing / reviews
- Claim: "Why and How Discord Uses Patch to Test Elixir" — they built/used a mocking library (Patch) for Elixir tests. Label: **Corroborated** (blog title only); specifics Unknown.

### Deployment
- Claim: Unknown specifics. Label: **Unknown**.

### Monitoring / operate
- Claim: Discord's eng team is "unusually open" about architecture; ex-community members report direct conversations with Discord engineers in meta communities. Label: **Corroborated** — Fluxer author's first-hand account (web.archive.org).

### User feedback / business outcomes
- Claim (contrarian): an independent developer building a Discord alternative respects the backend engineering but is "less enthusiastic about some of Discord's product management and business decisions." Label: **Corroborated** — first-hand (Fluxer blog, archived).
- Claim: Discord stuck with React Native for mobile despite industry scepticism, and published "How Discord achieves native iOS performance with React Native." Label: **Corroborated** (blog titles).

### Documented failures
1. No single canonical Discord outage postmortem located this pass. Known incident classes from secondary sources: the Elixir read-state latency spikes that motivated the Rust work (pre-fix pain, not an outage). Label: **Unknown** for formal postmortems — gap.

### Transferable lessons
- Right-tool layering: BEAM for concurrency, Rust for CPU-hot structures via NIFs — extend the platform instead of abandoning it. Label: **Corroborated**.
- Time-box the spike ("we set aside a week") and let benchmarks decide. Label: **Corroborated**.
- Separate signalling from media (voice), and make failover a routine automated path, not an emergency procedure. Label: **Corroborated**.
- Publish the scaling journey; it compounds into hiring and ecosystem goodwill (Rustler, Manifold, elixir-lang case study). Label: **Inferred** from the density of community uptake.

## Sources
| ID | Claim area | URL | Type | Author/org | Date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| DI-01 | Rust/Elixir 11M users (official blog, excerpt) | https://discord.com/blog/using-rust-to-scale-elixir-for-11-million-concurrent-users?ref=hackernoon.com | Primary eng blog | Matt Nowack / Discord | May 2019 | 2026-10-10 | High (text quoted) |
| DI-02 | Benchmark walkthrough (0.4µs–640µs figures) | https://timothya.com/learning/using-rust-to-scale-elixir-for-11-million-concurrent-users/ | Secondary (analysis) | Timothy Andrew | 2019 | 2026-10-10 | Medium |
| DI-03 | Elixir at Discord case study (Cowboy, GenStage, Rustler) | https://github.com/elixir-lang/elixir-lang.github.com/blob/HEAD/src/content/blog/real-time-communication-at-scale-with-elixir-at-discord.md | Secondary (language-org case study) | elixir-lang.org | 2024 | 2026-10-10 | Medium |
| DI-04 | Voice SFU, ScyllaDB, Manifold figures | https://github.com/handbook-academy/engineering-handbook/blob/HEAD/content/hld/part-2-building-blocks/10-real-time-communication.md | Secondary (synthesis) | handbook-academy | 2026 | 2026-10-10 | Low-medium |
| DI-05 | Guild-process isolation, Elixir/Rust split | https://github.com/udaykumar-dhokia/insidethestack/blob/HEAD/content/articles/how-discord-works.mdx | Secondary (synthesis) | insidethestack | 2026 | 2026-10-10 | Low-medium |
| DI-06 | Eng-team openness, product-management critique | https://web.archive.org/web/20260421233902/https://blog.fluxer.app/how-i-built-fluxer-a-discord-like-chat-app/ | First-hand (practitioner) | Fluxer author | 2026 | 2026-10-10 | Medium |

## Narrative audit (retrofit 2026-10-10)
- **No postmortems, no problem?** Discord operates at enormous scale with *no* public incident retrospectives found this pass. Either the incident rate is genuinely low (plausible — the Elixir/BEAM choice pays reliability dividends) or the culture doesn't narrate failures. Contrast Cloudflare/GitLab: Discord asks for trust without receipts; the BEAM community supplies the hero narrative instead.
- **Infra excellence, product bloat.** The engineering writing (Elixir, Rust, ScyllaDB migrations) is excellent; the *product* accumulates features (activities, shops, endless Nitro tiers) the infra doesn't need. Engineering quality and product focus are independent variables — Discord proves you can have world-class infra and a cluttered product simultaneously.
- **The Elixir halo.** "Discord runs on Elixir" is used industry-wide to sell the BEAM — but Discord's scale also comes from *operational* excellence (the migration stories in this file), not the language alone. Copy the ops discipline, not just the runtime.
