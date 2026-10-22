# Appendix C — Expansion Practices Digest

**Source:** `research/expansion-practices/` (7 theme files + index + evidence register), researched 2026-10-10. Read-only research; neutral records — no rankings, no recommendations. 57 practices catalogued: contrarian methodologies, abandoned approaches, unwritten rules, extreme practices, indie/bootstrapper wisdom, AI-era fringe, and craft culture. Each item below carries the research's own verdict; labels follow the Atlas convention (Verified = read in primary this pass; Corroborated = ≥2 independent sources; Inferred = confident consensus not re-verified; Proposed = author synthesis; Unknown = gap).

---

## The 10 most surprising / useful fringe findings

### 1. The viral "42%" monolith statistic is fabricated (→ 01-contrarian-methodologies.md)
The monolith revival is real — Prime Video cut costs ~90% consolidating a microservices workload, and Segment, InVision, and Istio each reversed premature distribution (Corroborated named cases). But the industry's favorite proof-point — a widely-shared "42% of companies are moving back to monoliths" statistic — was fabricated; the discourse outran the evidence. **Verdict: Named cases corroborated; the viral statistic is fabricated; the real rule is "never *big-bang* rewrite" — strangler migrations succeed.** The failure is premature distribution, not distribution.

### 2. Open-plan offices produced the opposite of their stated purpose (→ 02-abandoned-approaches.md)
The peer-reviewed finding (Bernstein & Turban, 2018): moving to open-plan caused face-to-face interaction to *drop* ~70%, while email rose +67% and instant messaging +75% — employees put on headphones and messaged instead. **Verdict: Peer-reviewed; the opposite of the stated purpose.** A canonical case of an intervention whose measured effect inverted its intent — relevant to any org-design argument made from first principles rather than evidence.

### 3. AI's productivity paradox is convergent, not anecdotal (→ 06-ai-era-fringe.md)
Five independent lines of evidence point the same way: METR's RCT (16 developers, 19% *slower* with early AI tools, with a 39-percentage-point perception gap between felt speed and measured speed); DORA 2024 (39k respondents: a 25pp AI-adoption increase associated with −7.2% stability); Uplevel (800 developers: +41% bugs with no throughput gain); GitClear (refactoring share 25%→<10%); Stack Overflow 2025 (84% use AI tools, 46% distrust the output). **Verdict: Convergent — AI raises code volume and perceived speed while degrading stability/trust signals; typing was never the bottleneck.** This is the single most important counterweight in the corpus to "AI makes developers faster" claims.

### 4. "Vibe coding" was coined for throwaway projects — the qualifier was erased in retelling (→ 06-ai-era-fringe.md)
Karpathy's Feb 2025 coinage explicitly described throwaway weekend projects; as the term went viral, that qualifier disappeared and the term now means three different things (throwaway prototypes, serious development with AI assistance, and fully autonomous agent-built production code). **Verdict: Coinage verified; track which meaning a claim uses.** Almost every "vibe coding in production" argument in the corpus commits an equivocation the coinage itself warns against.

### 5. Resume-Driven Development is now empirically documented (→ 03-unwritten-rules.md)
What was folk slang — choosing technology for resumes rather than systems — became a peer-reviewed paper (arXiv:2101.12703, n=591): 60% of hiring influenced by trends, 82% of developers believe trendiness aids hiring. **Verdict: Empirically corroborated; the pathology is selection on trendiness *instead of* fit.** This reframes "boring technology" advocacy from taste to risk management — and pairs with Alex Payne's "nobody ever got fired for picking Java" (the cynical twin: boring choices are career-risk management, which also explains why they outlive their justification).

### 6. YC W25: 25% of codebases were 95% AI-generated — existence proof, misused beyond it (→ 06-ai-era-fringe.md)
YC's W25 batch: a quarter of startups had codebases ~95% AI-generated (Friedman via TechCrunch, Mar 2025; Tan's caveat: early-stage). **Verdict: Corroborated with caveats; self-reported, unaudited.** The finding is an existence proof at *seed* stage — it says nothing about maintainability, security review, or what happens at 100 engineers, which is exactly how it gets misused.

### 7. Stack ranking was abandoned — and is creeping back (→ 02-abandoned-approaches.md)
Microsoft abandoned stack ranking Nov 2013; Amazon dropped its OLR variant in 2016 — it incentivizes sabotage-by-inaction (withholding help improves your relative position). Yet the research found 2025 reporting of its quiet return in AI-era performance systems. **Verdict: Abandonment corroborated; the 2025 return is single-source.** Read alongside the Valve case (Appendix A): peer stack ranking with no managerial calibration is the most political evaluation design known — and it's being reintroduced into the same companies now running AI-usage mandates.

### 8. Google's 20% time died by incentive incompatibility, not decree (→ 02-abandoned-approaches.md)
The timeline is corroborated: 20% time faded ~2013, Area 120 (2016) was the successor, cut back 2022. The mechanism matters more than the date: a perk the promotion process punishes is not a perk — engineers couldn't spend 20% on speculative work while being evaluated on 100%-of-OKRs delivery. **Verdict: Timeline corroborated; lesson: a perk the promo process punishes is not a perk.** The general form — formal policy vs. incentive reality — recurs in the gaps stream's T3 (org design, incentives & performance management).

### 9. Security lives in AI's "last 30%" (→ 06-ai-era-fringe.md)
The security record across independent vendors is directionally convergent even after discounting vendor incentives: Moltbook (Wiz, Feb 2026: 1.5M tokens, missing RLS); Escape.tech (2,038 critical vulnerabilities in 5,600 AI-generated apps); RedAccess (~5k of 380k apps leaking); SonarQube (53% "looks right, hides defects"); Veracode (44% introduce known vulnerabilities). **Verdict: Pattern corroborated across independent vendors; magnitudes discounted for vendor incentive; security lives in the last 30%.** It pairs with Addy Osmani's "70% Problem" (late 2024): AI gets you 70% fast; the last 30% takes as long as ever — corroborated as a practitioner model, with the number illustrative rather than measured.

### 10. "You build it, you run it" cargo-culted without a platform burns teams out (→ 02-abandoned-approaches.md)
Vogels' 2006 dictum (ACM Queue) is verified as a quote; the misuse pattern is corroborated: teams given pager duty without the platform engineering (paved roads, golden paths, cognitive-load limits) to absorb it burn out — and the industry's answer was platform engineering plus Team Topologies' cognitive-load framing. **Verdict: Quote verified; misuse pattern corroborated.** The practice is a socio-technical bundle, not a slogan — the same bundle logic applies to trunk-based development (Google's 2B-line monorepo only works with flags, fast CI, and tests) and blameless postmortems (which degrade into absolution theater without tracked remediation).

---

## The 7 theme files (pointers)

All in `research/expansion-practices/`, 57 practices total:

1. `01-contrarian-methodologies.md` — Choose Boring Technology (3 innovation tokens), "Agile is Dead," monolith revival, #NoEstimates, delete-code movement, "Worse is Better," Grug-brained developer, no-meetings experiments, Working Backwards/PR-FAQ, "disagree and commit," move-fast retirement.
2. `02-abandoned-approaches.md` — SAFe horror stories, microservices reversions, "you build it, you run it" → burnout, 10x engineer myth, open-plan offices, remote-work bans, Holacracy, stack ranking, Google 20% time, unlimited vacation, the Spotify model.
3. `03-unwritten-rules.md` — "never rewrite" (and its limits), Chesterton's Fence vs. deletion, "the demo is the spec" (Apple), Resume-Driven Development, Conway's Law (with its empirical boundary: Colfer & Baldwin, 142 studies), hallway-driven development, "Programming Sucks."
4. `04-extreme-practices.md` — trunk-based development at scale, continuous deployment at scale, chaos engineering, GameDays, blameless postmortems, error budgets, feature flags (and flag debt), on-call compensation.
5. `05-indie-bootstrapper-wisdom.md` — "Do Things That Don't Scale," Maker's vs. Manager's Schedule, Shape Up, the boring-stack manifesto, single-binary deployments, SQLite at scale.
6. `06-ai-era-fringe.md` — "vibe coding," YC W25 95%-AI codebases, the 70% Problem, the productivity paradox, the security record, "agentic engineering," AI codebase bankruptcies, the prompt-as-code controversy.
7. `07-craft-culture.md` — Software Craftsmanship Manifesto, Staff Engineer archetypes (Larson), the seniority collapse (Stanford Digital Economy Lab: devs 22–25 employment −20% from the 2022 peak; AI-as-cause contested), craftsmanship vs. "good enough."

- `00-index.md` — one-line claim + verdict per practice (reproduced in condensed form above).
- `evidence-register.md` — per-finding metadata: claim, URL, source type, author/org, pub date, accessed date, confidence, corroboration, contradictions, engineering implication.

Workspace path: `~/workspace/your_files/atlas/product_engineering/research/expansion-practices/`
