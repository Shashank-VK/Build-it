# §30 — Game Engines & Creative Runtimes (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## GE-01 — Godot — ACTIVE (ascendant)
- Purpose / problem: Open-source 2D/3D game engine (GDScript + C#/.NET 8/9, Vulkan/GL Compatibility renderers, XR tools).
- OSS/commercial: OSS **MIT**; zero-install (~100MB standalone).
- Maintenance: Active — 4.7.x line current (4.7.2 referenced in 2026 skill docs); Godot 4.0 brought Vulkan, new tilemap, XR.
- **Ascendance (verified):** **GMTK Game Jam 2026 — Godot #1 for the first time with 47% (4.9k games)**; Unity second at 34% (first time in 9 years Unity didn't lead). Five-year trajectory: 16% (2022) → 19% (2023) → 37% (2024) → 39% (2025) → 47% (2026). Commercial proof: **Slay the Spire 2 moved from Unity to Godot** (2026); Brotato, Buckshot Roulette (millions of copies), Cassette Beasts, Dome Keeper shipped on Godot; growing Steam/itch.io releases (Godot Foundation board).
- Limitations: No official console export (platform SDK NDAs vs open license) — must go through **W4 Games' W4 Consoles** (Switch, Xbox Series X|S, PS5; Switch 2 beta since early 2026; per-title/per-platform negotiated pricing); C# web export unsupported in 4.6 (stay on GDScript for web); mobile ad/IAP/analytics tooling less mature than Unity's; asset library smaller; many tutorials target incompatible Godot 3.x.
- Security: N/A (engine); standard.
- Alternatives: Unity, Unreal, GameMaker, Bevy.
- Switching costs: Medium (engine rewrite; GDScript→C# portable-ish).
- Use: U(Verified) — jam data + commercial titles (gameworldobserver, outlookindia, LinkedIn/Diversion post).

## GE-02 — Unity — ACTIVE (CONTROVERSIAL: trust)
- Purpose / problem: Proprietary cross-platform engine (C#/.NET, IL2CPP); 20-year ecosystem: Asset Store, LevelPlay/AdMob/IAP, AR Foundation, XRI.
- OSS/commercial: Commercial proprietary (Personal/Pro seat subscriptions).
- **CONTROVERSY (runtime fee, 2023):** **Sep 2023: Unity announced per-install runtime fee** — massive backlash; **cancelled Sep 2024**; CEO departed; reported ~15% of US advertisers left. Trust damage persists (the Godot migration wave is its echo).
- Maintenance: Active — **Unity 6.0 LTS reaches end of support Oct 2026** (per itamde 2026 guide — plan upgrades).
- Limitations: Proprietary license; trust overhang; build footprint 8–30GB+ (Hub + modules); older Asset Store content version-rot.
- Alternatives: Godot, Unreal.
- Switching costs: High (ecosystem, ads/IAP stack).
- Use: U(Verified) — still the mobile/console commercial standard (34% of GMTK 2026).

## GE-03 — Unreal Engine — ACTIVE
- Purpose / problem: AAA 3D engine (C++/Blueprints, Nanite/Lumen); Epic.
- OSS/commercial: Proprietary (royalty model; source-available).
- Maintenance: Active (2026). 3% of GMTK 2026 (319 games) — jam-irrelevant, industry-standard for high-end 3D.
- Alternatives: Unity, Godot.
- Use: U(Proposed). (Depth debt.)

## GE-04 — GameMaker — ACTIVE
- Purpose / problem: 2D-focused engine (GML); beginner-friendly.
- OSS/commercial: Commercial (Opera).
- Maintenance: Active (2026); 5% of GMTK 2026 (498 games).
- Alternatives: Godot, Construct.
- Use: U(Proposed). (Depth debt.)

## GE-05 — Bevy — ACTIVE (experimental-adjacent)
- Purpose / problem: Rust ECS game engine (data-driven, mod-friendly).
- OSS/commercial: OSS (MIT/Apache-2.0).
- Maintenance: Active (2026). (Depth debt on releases.)
- Alternatives: Godot, Fyrox.
- Use: U(Proposed).

## Notable status findings (game engines)
- **Godot overtook Unity at GMTK Game Jam 2026 (47% vs 34%)** — first time in 9 years; the runtime-fee backlash (2023–2024) is the causal backdrop.
- Unity 6.0 LTS end of support **Oct 2026**.
- Slay the Spire 2's Unity→Godot move is the commercial-credibility milestone.

---

### Per-record metadata (condensed)
- GMTK 2026 results: gameworldobserver.com (Jul 29, 2026); LinkedIn Diversion post (activity-7490049541698805760) — login-walled but excerpt visible; note limitation. Confidence: High (primary: GMTK organizers).
- Godot commercial titles + Unity exodus: respawn.outlookindia.com (May 2026); itamde.com (Sep 2026); dev.to architecture guide (Oct 2026). Confidence: Medium–High.
- Unity runtime fee saga: summary evidence. Confidence: High.
- Godot 4.7.2: genesis-prime/claude-code-game-studios SKILL.md (GitHub, Sep 2026). Confidence: Medium.
