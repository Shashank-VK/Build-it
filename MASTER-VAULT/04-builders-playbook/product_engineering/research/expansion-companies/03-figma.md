# Figma — product engineering case study

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Figma is the standout "did the hard thing simply" case: a custom multiplayer sync engine (not OT, not CRDTs) plus a hybrid C++/WASM rendering architecture, built by a tiny team. The primary source — co-founder Evan Wallace's 2019 engineering blog, fetched in full this pass — is one of the best public distributed-systems write-ups in product engineering.

## Findings

### Product discovery
- Claim: "No one was clamoring for a multiplayer design tool — if anything, people hated the idea. Designers worried that live collaborative editing would result in 'hovering art directors' and 'design by committee' catastrophes." Figma bet anyway because "it just felt wrong not to offer multiplayer as a tool on the web." Label: **Verified** — primary blog (Wallace, 2019). Lesson: the founding product bet was contrarian; discovery here was conviction + taste, not user requests. (Sequoia's retrospective corroborates the early hostility: "I'm changing careers" reactions.)
- Claim: Early public launch (Dec 2015) met skeptical-to-hostile designer reaction; by 2017, when Figma began charging, adoption accelerated and skeptics were won over. Label: **Corroborated** — secondary case study citing Lincoln/Sequoia 2021.

### Architecture
- Claim: Client/server over WebSockets; a separate server process per multiplayer document; clients download a full copy on open, then sync updates bidirectionally. Label: **Verified** — primary blog.
- Claim: The document is modeled as a flat two-level map `Map<ObjectID, Map<Property, Value>>` (equivalently, rows of `(ObjectID, Property, Value)` tuples). Adding features usually means adding new properties — a schema-less-ish design that decouples sync from product evolution. Label: **Verified** — primary blog.
- Claim: Conflict resolution is property-level last-writer-wins with the *server's arrival order* as tiebreaker (no timestamps needed because the server is the central authority) — "inspired by" CRDTs (LWW registers, LWW sets) but deliberately not true CRDTs, avoiding their decentralization overhead. Label: **Verified** — primary blog.
- Claim: They rejected operational transforms — the Google Docs standard — as "unnecessarily complex for our problem space," citing OT's combinatorial state explosion and error-prone formal proofs even for basic insert/delete. Primary goal: "no more complex than necessary to get the job done," because simpler is easier to reason about, implement, debug, test, and maintain. Label: **Verified** — primary blog.
- Claim: Non-document data (comments, users, teams, projects) lives in Postgres and syncs via a *completely separate* system, because of different tradeoffs around performance, offline availability, and security. Lesson: don't force one sync system to serve two masters. Label: **Verified** — primary blog.
- Claim: Hybrid C++/JavaScript architecture: document representation and canvas in C++ (compiled to WebAssembly in 2017, cutting load time 3x), UI chrome in JavaScript/TypeScript + React; all document rendering done in WebGL, bypassing the browser's HTML pipeline, for cross-browser consistency and performance. Label: **Corroborated** — HN synthesis of Evan Wallace's writings (madebyevan.com/figma; the 3x WASM figure also appears in Figma's own WASM blog, cited in secondary sources).
- Claim: The multiplayer server was initially TypeScript, later ported to Rust for performance and stability. Label: **Corroborated** — HN (2025) citing Wallace's site; the port itself is not dated precisely in sources seen — treat date as Unknown.

### Implementation
- Claim: Before committing to the approach, the team built a prototype playground — a web page simulating three clients and a server with full state visualization — to test ideas around offline clients and bandwidth-limited connections, then grafted the validated ideas onto the real codebase. Label: **Verified** — primary blog (includes prototype screenshot). Lesson: prototype the *hard distributed part* in isolation before touching the product codebase.
- Claim: Offline editing works by client-generated unique object IDs (client ID embedded in the ID), so creation never needs the server — this is what makes arbitrary offline editing possible. Reconnect = download fresh copy, reapply offline edits on top. Label: **Verified** — primary blog.
- Claim: Deleted objects' properties are dropped from the server and kept only in the deleting client's undo buffer (which restores them on undo) — this stops long-lived documents growing unboundedly. Label: **Verified** — primary blog. Lesson: bound your data growth explicitly; "tombstones forever" is a choice, not a default.
- Claim: Optimistic local updates + discarding stale server echoes: the client's own unacknowledged change is the best prediction of the eventually-consistent value, so conflicting incoming server changes are suppressed to avoid "flicker." Label: **Verified** — primary blog.

### Testing / reviews
- Claim: Unknown specifics of their test practice for multiplayer. Label: **Unknown**.

### Documented failures
1. No major public Figma engineering failures located this pass — the story is the opposite: a bet that looked wrong and wasn't. The closest to a "failure mode" is the acknowledged limitation that simultaneous same-text editing doesn't merge (AB vs BC → one wins, never ABC) — accepted because "Figma is a design tool, not a text editor." Label: **Verified** (primary).

### Transferable lessons
- Match conflict granularity to your domain, not to the fashionable algorithm: property-level LWW beat OT/CRDTs because Figma's data is a property tree, not text. Label: **Verified**.
- Simplicity is a shipping strategy: "As a startup we value the ability to ship features quickly, and OTs were unnecessarily complex" — the simpler system shipped in 2016 and was still the documented architecture years later. Label: **Verified**.
- Prototype the riskiest subsystem in a sandbox with full state visibility before integrating. Label: **Verified**.
- Separate sync systems by tradeoff profile (documents vs metadata). Label: **Verified**.
- Accept and document the semantic you won't support (text merge) rather than contorting the system to cover it. Label: **Verified**.

## Sources
| ID | Claim area | URL | Type | Author/org | Date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| FI-01 | Multiplayer architecture (primary, fetched) | https://www.figma.com/blog/how-figmas-multiplayer-technology-works/ | Primary eng blog | Evan Wallace / Figma | Oct 2019 | 2026-10-10 | High |
| FI-02 | LWW mechanics explainer | https://daily.dev/posts/qwj3u8dbf | Secondary (explainer) | daily.dev / iocombats | 2026 | 2026-10-10 | Medium |
| FI-03 | "Dumber algorithm" analysis, fractional indexing, undo | https://dev.to/devopsdaily/figma-made-multiplayer-instant-by-picking-the-dumber-algorithm-c5k | Secondary (analysis) | devops-daily | 2026 | 2026-10-10 | Medium |
| FI-04 | Product-bet narrative, hostile early reaction | https://github.com/hatefrad/product-engineer/blob/HEAD/case-studies/figma-multiplayer.md | Secondary (case study) | hatefrad | 2026 | 2026-10-10 | Medium |
| FI-05 | HN: hybrid C++/JS, WASM, Rust port, S-1 metrics | https://news.ycombinator.com/item?id=44437316 | Community (first-hand/secondary) | HN commenters | 2025 | 2026-10-10 | Medium |
| FI-06 | OT-rejection quote corroboration | https://blog.val.town/projects | Secondary (founder blog) | Val Town | 2024 | 2026-10-10 | Medium |

## Narrative audit (retrofit 2026-10-10)
- **"Multiplayer just works" vs. the Rust port.** The founding narrative is simplicity (OT/CRDTs made invisible). The later receipt: Figma hit performance walls requiring a ground-up Rust/WASM rewrite of the render engine. The simple story was true *at the product layer* and false *at the implementation layer* — and the implementation layer is where the headcount went. Copy the willingness to rewrite the engine when the abstraction leaks, not the slogan.
- **The $20B deal as the business postmortem.** Adobe's attempt to buy Figma for $20B (see file 32) was the market's verdict on Adobe's internal tools org — and the collapse left Figma independent. Figma's engineering excellence created a strategic asset so valuable it *couldn't be acquired*: the highest compliment and the strangest curse.
- **From designers' darling to enterprise suite.** The current Figma (Dev Mode, Slides, Sites, AI features) is far from the "simple multiplayer canvas" origin — accreting toward the enterprise feature factory. The open question: does the original engineering culture (small teams, craft) survive it? Unknown; watch the seams.
