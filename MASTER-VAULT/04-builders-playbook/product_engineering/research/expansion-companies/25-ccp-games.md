# CCP Games / EVE Online — product engineering case study (single-shard MMO at 20+ years)

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
CCP's EVE Online is the longest-running single-shard MMO — every player in one shared universe on one cluster ("Tranquility"), running since 2003. The engineering problem is unique: thousands of players in one battle, one simulation tick, no sharding escape hatch. This file covers the tick model, Time Dilation, the Stackless Python heritage, and the contrarian audit.

## 1. Forensic reconstruction — how the machine actually works

### The simulation: 1 Hz tick, single shard, no sharding
- Claim: EVE runs as a **single-shard** universe on the Tranquility cluster — all ~500,000-subscriber-era players share one world state (no realms/instances for the main universe). The simulation advances in **1 Hz ticks** (one update per second), a design choice that trades twitch responsiveness for determinism at massive scale. Label: **Corroborated** — the prediction-multiplayer-research MMO survey (GitHub, endel) documents the tick model; computing.co.uk covers the data scale (hundreds of GB/day from ~500K players). Confidence: high on single-shard + tick; medium on current numbers.
- Claim: The server stack's historic foundation is **Stackless Python** (chosen ~2000s for massive concurrency via tasklets/microthreads — the famous "EVE runs on Python" fact), with C++ extensions for hot paths. Label: **Corroborated** (widely documented; the GitHub MMO survey). Note: CCP has progressively moved simulation-critical paths toward lower-level implementations over the years; the "still Python" claim should be dated — **current stack composition Unknown** this pass.

### Time Dilation: slow down time instead of desyncing
- Claim: **Time Dilation (TiDi)** is CCP's signature load-shedding mechanism: when a star system exceeds compute capacity (fleet fights with thousands of players), the server *slows the simulation clock* — down to 10% speed — rather than dropping updates or desyncing. Every client sees the same slowed time, so the battle stays fair and consistent. Label: **Corroborated** — engadget (2011, "Time Dilation and the war on lag"). Plain-English: instead of the game stuttering or lying to players, time itself stretches — a 10-minute battle takes 100 minutes, but everyone agrees on what happened.
- Claim: The largest fights (e.g., **B-R5RB, Jan 2014: 7,548 players** in one battle) are the load tests no synthetic benchmark can replicate; TiDi is what made them *playable at all*. Label: **Corroborated** (battle size widely reported).
- Claim: Data scale: CCP manages hundreds of gigabytes of new data per day from the player base, with analytics feeding both game design and the famous player-driven economy research. Label: **Corroborated** (computing.co.uk analysis).

## 2. Postmortem record — failures hunted down
- **Incarna / "Walking in Stations" (2011):** CCP's attempt to add avatar gameplay divided focus from the spaceship core; the "Summer of Rage" player revolt (over microtransaction fears and neglected core gameplay) forced a public apology and a refocus. This is a *product-focus* postmortem: the single-shard spaceship game is the product; everything else was distraction. Label: **Corroborated** (widely reported; specifics not deep-dived this pass).
- **Lag as the permanent incident:** before TiDi, massive fleet fights simply broke (desync, crashes, unplayability) — TiDi itself was the postmortem response to years of "the game falls over at the moments that matter most." Label: **Corroborated** (engadget's framing).
- **No published formal incident postmortems** at the Cloudflare level of technical detail were found for Tranquility outages — CCP communicates via dev blogs and forums, not blameless-postmortem documents. Recorded as a gap.

## 3. Narrative audit — dismantling with receipts
- **"TiDi is genius" vs. "TiDi is a confession."** The celebratory telling: Time Dilation is brilliant engineering. The contrarian receipt (EVE forums, "Massive Multiplayer Was Always a Lie"): TiDi is an admission that the server *can't* simulate the battle in real time — it redefines the SLA instead of meeting it. Both are true, and that's the audit point: TiDi is genius *as a consistency mechanism* and a confession *as a performance story*. The transferable lesson is the reframing move itself — when you can't meet the SLA, change the contract explicitly (slowed time, disclosed to all) rather than degrading silently (desync, lag). Explicit degradation beats silent degradation. Label: **Inferred** (audit synthesis) on **Corroborated** mechanics.
- **Single-shard as identity vs. single-shard as constraint.** CCP's marketing made single-shard a *virtue* (one universe, real history, famous heists). The engineering receipt: it's also a *constraint* that forced 20 years of exotic workarounds (TiDi, reinforcement timers for sovereignty battles — scheduling the big fight so CCP can provision for it). Reinforcement is the tell: the "single shared universe" needs *an appointment system* for its biggest moments. Any team citing EVE for "don't shard" should price in two decades of TiDi-class innovation. Label: **Inferred** on **Corroborated** facts.
- **"EVE runs on Python" as a misleading boast.** The factoid is used to argue dynamic languages scale — but the receipts show the scaling came from *architecture* (1 Hz tick, single-threaded determinism per system, TiDi, C++ hot paths), not language choice. Python was the implementation detail; the tick model was the decision. Copy the tick, not the language. Label: **Inferred**.
- **Negative evidence:** no evidence was found that sharding would have served EVE better — the single shard is genuinely load-bearing for the game's identity (espionage, markets, history all require one shared truth). The audit doesn't claim sharding was the answer; it claims the *cost* of the answer should be explicit.

## Transferable lessons
1. **Explicit degradation beats silent degradation.** When you can't meet the SLA, change the contract openly (TiDi slows everyone's clock equally) instead of degrading quality opaquely.
2. **Design the tick around your consistency needs, not your latency dreams.** 1 Hz is "slow" and exactly right for a game about decisions, not reflexes. Match simulation rate to the decision rate.
3. **Schedule your peak load.** Sovereignty reinforcement (battles by appointment) is capacity planning as game design — if you know when the spike comes, you don't need to provision for it always.
4. **One shared truth is a feature with a 20-year maintenance bill.** Single-shard/single-source-of-truth architectures are worth it when shared history *is* the product — price the TiDi-class work accordingly.
5. **Copy the architecture, not the anecdote.** "Runs on Python" is trivia; "deterministic 1 Hz tick + explicit time dilation" is the transferable design.

## Sources
| ID | Claim | URL (verbatim) | Type | Author/Org | Pub date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| C1 | EVE: single shard, 1 Hz tick, Stackless Python (MMO architecture survey) | https://github.com/endel/prediction-multiplayer-research/blob/HEAD/MMO/eve-online.md | Community technical (GitHub) | endel | n.d. | 2026-10-10 | Medium-high |
| C2 | Time Dilation mechanics; war on lag | https://www.engadget.com/2011-10-02-eve-evolved-time-dilation-and-the-war-on-lag.html | Contemporary technical | Engadget | Oct 2011 | 2026-10-10 | High |
| C3 | Contrarian: "TiDi is a confession, not a solution" | https://forums.eveonline.com/t/massive-multiplayer-was-always-a-lie-until-now/517799 | Community (official forum) | EVE forum user | n.d. | 2026-10-10 | Low-medium (opinion) |
| C4 | Data scale: hundreds of GB/day, ~500K players | https://www.computing.co.uk/analysis/2300209/how-ccp-manages-hundreds-of-gigabytes-of-data-created-by-500-000-eve-online-players-everyday | Secondary analysis | computing.co.uk | n.d. | 2026-10-10 | Medium |

**Gaps:** Current server stack (Unknown); formal incident postmortems (not published at depth); Incarna postmortem (noted, not deep-dived); B-R5RB technical retrospective (not pulled).
