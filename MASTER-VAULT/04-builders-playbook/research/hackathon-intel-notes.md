# Hackathon Intel — Raw Research Notes (Workstream 1)

**Project:** The Builder's Playbook — workstream "hackathon-intel"
**Researched:** 2026-10-10
**Scope:** What actually wins hackathons, from public evidence. Stack-agnostic.
**Assumption:** User is a solo builder; stack/experience unknown. Notes flag where evidence is team-oriented.

## Evidence labels used
- **Verified** — directly documented in a named primary source (organizer guide, judge interview, winner's own postmortem).
- **Corroborated** — same claim appears in 2+ independent sources.
- **Inferred** — plausible pattern from limited/single secondary sources; treat as hypothesis.
- **Proposed** — my synthesis, not sourced.
- **Unknown** — insufficient evidence; listed at the end.

No winner names, project names, prize amounts, or statistics are stated below unless they appeared in the source. Where a source gives a number, it is attributed.

---

## 1. Judging criteria patterns

### 1a. What organizers publish (Verified)
Devpost's organizer-facing guide lists the most common criteria across Devpost hackathons: **technological implementation, ease of use, demonstration (video), potential impact, quality of the idea, design.** Individual hackathons set their own, but most draw from this pool. Devpost explicitly warns that many submissions get disqualified for missing baseline eligibility/requirements — "you'd be surprised how many submissions are disqualified simply because they didn't meet the baseline criteria."

Example published rubrics found:
- Microsoft "Code; Without Barriers" (Devpost rules): Quality of the Idea, Implementation of the idea (incl. Azure use), Potential Impact — equally weighted; tie-break goes to the first criterion.
- IBM-platform hackathon workshop notes (GitHub, a2tech360): 5 criteria × 5 pts = 25 total — completeness/feasibility, creativity/innovation, design/usability, effectiveness/efficiency, local impact.
- Future of Work Hackathon (Devpost update): Customer/Problem Validation, UX, Speed of Implementation, Immediate Impact/Value Add.
- CockroachDB × AWS "Build with Agentic Memory" (2026, ~3,700 registered, 600+ submitted, 78 finalists): scored on **agentic memory design, technical implementation, real-world impact and production readiness.**

### 1b. What judges say they actually do (Verified — Devpost interviewed 5 working judges)
Source: Devpost blog "How to win a hackathon: Advice from 5 seasoned judges" — judges from Square (Richard Moot), Databricks (Karen Bajza-Terlouw), Google (Kelvin Boateng), NEAR Foundation (Maria Yarotska), Atlassian (Warren Marusiak). Key points, paraphrased:
- **Requirements first.** Karen (Databricks): first pass is checking the hackathon's requirements; "surprising how many submissions did not fulfill the basic requirements." Creativity/enthusiasm signals effort and quality.
- **The demo video is the primary artifact in online judging.** Richard (Square): "The demo video gives the most amount of scope" — with many submissions, the video is the first indicator of time invested; video + text description must complement each other. Kelvin (Google): for a visual product they look at visual appeal first, then play the video or use the demo; "we're not necessarily looking at the best-written code, we're looking to see what the end-user experience is."
- **Storytelling keeps judges engaged.** Karen: "Presentation and storytelling matters and it can be a huge part of your success." Thoroughness in video (even demoing code/voiceover walkthroughs) helps with technical judges.
- **Non-technical wins happen.** Maria (NEAR): "We have awarded great projects that were not great from the technical side of things, but we saw potential in the team." Judges look for startup mindset: does the team see the problem behind the solution, or are they fitting a solution to this hackathon?
- **Balance across criteria beats spiking one.** Richard: the biggest negative is "over-indexed on one particular criteria at the detriment of the rest" — e.g., extremely backend-heavy with no UI. Standout projects "balance across all the judging criteria."
- **Score killers (each Verified, attributed):**
  - Ambiguity + thin repos: slick video/homepage but light GitHub (Karen).
  - Template resubmission: barely changed from provided starter (Kelvin).
  - Rehashed/already-in-market/extremely simple ideas (Warren).
  - Recycling the same project across hackathons with a new label — Maria checks Devpost profile history.
  - Shoehorning a pre-existing idea to fit the contest (Richard).
  - Big teams are "pinkish, not a red flag": unequal contribution is assumed (Maria).
- **Process detail:** multi-round judging is normal — technical screening, then top ~30 to final judges (Maria: NEAR; Warren: Atlassian does 3 rounds incl. install-check prelim). Kelvin: every project seen by 2 judges, then a second round.

### 1c. MLH's official line (Verified — mlh/mlh-policies, standard-hackathon-rules.md)
- "You are not judged on the quality of your pitch or the quality of your idea. As you are judged on what you built" — pitches/presentations discouraged; **demo what you built**.
- Demo even if broken/unfinished: "It's okay if you didn't finish your hack — that happens all the time! Completion is only one part of the judging criteria."
- MLH organizer guide recommends science-fair style judging + 2-minute submission videos ("a demo of their hack, not a presentation").

### 1d. Cross-cutting pattern (Corroborated)
Published criteria skew toward **impact + idea quality + demo**, while judge interviews reveal the real filter order: (1) meets requirements, (2) demo/video communicates clearly, (3) balanced across criteria, (4) story/enthusiasm signals effort. Technical depth matters most at technical hackathons (Atlassian runs AI-SME technical screening; CockroachDB×AWS scored "production readiness").

---

## 2. Winner postmortems and build logs

### Philip Nisevich — 1st place, Bay Builders Hackathon @ AWS Builder Loft, SF (Verified — author's LinkedIn post)
- Team built "Scout": text message → fully automated email marketing campaign (ran on Nimble, Kylon, BAND, InsForge, You.com).
- Venue was 18+; team wasn't allowed in the building. Built the entire thing from a Philz Coffee next door — no live demo, no mentors, no judges. Video was the only shot.
- Treated the video "like the whole product": scripted, storyboarded, cut to be watchable, because "judges were about to watch dozens of these back to back with zero context and zero patience."
- Won 1st place for Nimble. Takeaway (paraphrased): everyone afterward mentioned the video, nobody mentioned the code — "the product opened the door, the video is what stuck."

### Caroline Ang — 3rd prize + Best UX/UI, TalentLabs/Superteam Malaysia dual hackathon (Verified — author's LinkedIn post)
- At 1:15 PM she **killed the build**, rebuilt and submitted in 3 hours. Won 3rd + Best UX/UI.
- Lesson (paraphrased): if a product fails to communicate the quality of the underlying idea, rebuilding isn't overreacting — it's the responsible call. Team: product architecture/PRD reset/governance direction (Ang), research/slides (Clement Teo), technical co-creation + pressure-testing (Ruben Krishnan).

### Martina Dianda Rodríguez-Villar — 1st prize, first hackathon (Verified — author's LinkedIn post)
- Two tracks; most teams picked one; her team did both. Won Track A and Judges' Favourite for Track B — in ~6 hours.
- Method: two parallel builds, clear ownership, fast decisions, constant iteration. "No overthinking, just execution." Prize amounts not stated — not claimed here.

### Designer-turned-builder account — first hackathon (Verified — Medium, Popoola Abdussalam)
- Observed winners: "Skillverse" (immersive space theme, fully working prototype with recommendations + progress tracking); two-person team "Housr" winners built **both** student and partner dashboards with real-time discount-code creation; "Memoral" (minimal UI for dementia patients).
- Sting lesson: "We had a nice UI. They had a complete platform." Design alone wasn't enough.

### faadil1 / CALLSHEET ZERO — JigJoy hackathon postmortem, did NOT place (Verified — GitHub postmortem doc)
- Notable for method: explicitly separates **confirmed evidence vs inference** about why they lost — good model of evidence discipline.
- Rules weighted "genuine concurrency" alongside technical execution, creativity, clarity of demo. Team proved real concurrency (three agent loops overlapping 8.4s) and a meaningful shared-resource failure (schedule/talent/logistics producing an impossible plan) — but didn't place; no judge scorecards published, so reasons are inference.

### "The Hackathon Playbook: What Actually Works" — Medium, Kartikey Pandey (Verified as self-reported winner account)
- Winning demo = simple to understand, memorable (judges see 20+ projects), shows real-world impact beyond the event, features **working** functionality, delivered with confidence. Common mistake: showing every feature — show 2–3 strongest.
- Devpost presence: demo video, UI/team/process images, logo. "Don't obsess over Devpost, but don't ignore it either."
- Sponsor networking: a win led to follow-on funding and a student accelerator invite — via relationships with sponsor engineers, not just the build.
- "Most teams don't allocate roles based on strengths and don't practice their story. Winners build, practice, refine their pitch, and design their demo around what judges care about."

### Elastic "Forge the Future" 2026 Mumbai — winner announcement (Verified — elastic.co blog)
- Grand winner: "Vigil" by Team Frustrated Engineers — automated compliance auditing of sales-call audio against SEBI/AMFI regulations (multilingual transcription, timestamped violation flags matched to regulation clauses). Pattern: big, specific, regulated real-world problem.

### HN thread "How to win a hackathon without coming in first place" (Verified — community testimony, news.ycombinator.com)
- 3-time winner (incl. ~$5,000 team cash prize): (1) teammates matter most — "at least one 10X programmer on each of my winning teams"; (2) easy-to-explain idea that captures imagination; (3) frameworks/toolkits, NOT a new language; (4) awesome demo — "seen someone win a hackathon with an amazing presentation and zero working code."
- Seconded: "coding has very little to do with winning... writing just enough code to make everything look good."
- Nick Singh mentioned: 1st at HackUVA (24h), then judged the next year for Facebook — his writeup linked but not retrieved; content Unknown.

---

## 3. Idea-selection patterns

### Spend real time on the idea — the dominant pattern (Corroborated)
- Palash Taneja (10+ hackathons, 4 wins; freeCodeCamp): **spend 25% of the time on ideation** — or arrive with ideas ready. API prizes: "most people don't pay attention to smaller API prizes," so they're easier to win. Example: "BPatient" (NLP symptom search) won via an obscure API.
- LinkedIn "Ideation Hackathons" top content — founder, 8 hackathon wins incl. UofTHacks and Anthropic: **"a good idea beats fast execution every time."** At Hack the North he + Satyam Singh spent **more than half the time** brainstorming/exploring/prototyping, finished the build in under 8 hours — and won. Framework: (1) start with the judges — "what would make a judge stop and lean in during a 3-minute demo?"; (2) generate widely 30–60 min, then filter with one question: "can we demo this compellingly in 3 minutes?"; (3) pick the best story — clearest problem→solution→impact beats muddled narrative; (4) scope ruthlessly before building. "With AI, coding is no longer the bottleneck — ideas are."
- Devpost webinar tips: read the site thoroughly before starting — required tools, judging criteria, sponsor inspiration/problem statements, bonus tracks.

### What wins: problem-first, big, explainable (Corroborated)
- Taneja: solve a BIG problem; impact can be up to ~25% of score. Winner examples: Dubit (video dubbing for education access in developing countries), MLSI (sign language interpreter), TalkToMe (assistant for visually impaired Chrome users).
- BizThon "10 Winning Hacks": start brainstorming with **problems, not technologies** — "What frustrated me this week?" Litmus test: "Can you explain the problem to a non-technical person in one sentence, and will they immediately understand why it matters?"
- dev.to "The Subtle Art of Hackathon Ideation": bigger-scale problem = more solution value; pick a **self-sustainable** solution (not dependent on people/systems you lack); evaluate multiple solution approaches before building to avoid mid-event discovery that the approach is wrong.

### Technical innovation that wins vs doesn't (Verified — BizThon analysis; principle Corroborated)
- Wins: novel combinations, clever measurable optimizations, first implementations of a new capability, creative architecture. Example given: "Compressed NFT Marketplace" at Solana Hyperdrive 2023 — used state compression to mint 10,000 NFTs in one transaction for under $5 (1000x improvement); the demo made jaws drop.
- Doesn't win: over-engineering ("built our own Layer 2 from scratch — in 48 hours? No, you didn't"), buzzword bingo without implementation, complexity without purpose (15 protocols where 3 suffice).

### Sponsor-track arbitrage (Corroborated)
- Taneja: smaller API prizes are less competitive — plan for them.
- Hackathon-Starter-Pack guide: map sponsor→visible tech (Google→Gemini, Microsoft→Azure/OpenAI, MongoDB→MongoDB visibly).
- Kelvin (Google judge): incorporate provided resources — "we're likely really interested in seeing [our product] used with that product."
- Medium BizThon 101: "If you're not competitive for the main prize, sponsor tracks are your best shot."

---

## 4. Stack choices: boring vs shiny

### The consensus: boring stack, familiar tools (Corroborated)
- HN 3-time winner: "Make use of frameworks and toolkits. Now is NOT the time to learn a new language (if you want to win). The faster you can stand up a functioning prototype, the better."
- Jeremy Kintana (Substack guide): you need a minimum *presentable* product, not an MVP — "If you have errors flashing in the console, but the live demo looks fine, you're doing it right." Don't build production-grade infra unless that's what's being judged.
- Skills-repo synthesis (crisiswastaken): "use familiar tooling (novelty belongs in the idea, not the stack); set up environments and clone boilerplate before the event where rules allow."
- dev.to "Top 5 Lessons" (solo/team competitor): ignore unit tests and complex branching when solo — commit to main; "building a race car — during the race isn't the time to polish the hood ornament." Ran into trouble with unfamiliar tech (AWS Amplify) mid-event.
- PrismJudge build log (dev.to, 72h competition): "Boring Architecture Wins" — in-process SQLite/WAL inside Node beat multi-container setups on speed and reliability.
- Medium "Stop Chasing Shiny Frameworks" (2026): AI coding assistants are dramatically better at mainstream languages/frameworks; choosing obscure tech now also costs AI-assistance effectiveness — a reinforcing cycle favoring established tools.

### The caveat: match technical depth to the rubric (Corroborated)
- Kintana's own caveat: unless impressing judges *is* the technical depth (very technical hackathon).
- Atlassian: AI subject-matter experts do deep technical screening. Google/Flutter: performance and visual polish are the product. CockroachDB×AWS: "technical implementation" + "production readiness" scored.
- BizThon: judges want impact + execution; "technical impressiveness alone rarely wins."

### Proposed synthesis (Proposed)
Default: the most boring stack you already know, deployed to a URL in the first hours. Spend novelty budget on exactly one thing — the idea's core differentiator — and only if the rubric rewards technical depth.

---

## 5. Demo strategies

### Video is the highest-leverage artifact (Corroborated)
- Richard (Square judge): video gives "the most amount of scope" — first indicator of effort across many submissions.
- Nisevich: won 1st with **video only** (no live demo possible) — scripted, storyboarded, cut for watchability.
- Devpost webinar: plan the demo video — cover the idea + problem, key features built, future potential.
- MLH fellowship guide: record the video a day before demos; structure: name/purpose → team → problem → demo → contributions.

### Always have a backup video (Corroborated)
- wafi574 "30 Days of Hackathon" guide: "Record a short demo video before you present — ideally before the deadline crunch. This is the single most underrated safety move." Live demos fail (wifi dies, servers hiccup, laptops freeze); the video is also usually a submission requirement; recording *is* rehearsal. If live breaks: "Let me show you our recorded demo." Keep it open in a tab.
- Kurzweil Library (iPhoneDevCamp winner account): chose **edited video over live demo** — let them tell a story, control the 3-minute slot, share the full vision. Won.
- Skills-repo timing table: 5× live rehearsals, 2 backup videos (Inferred numbers — single source; the practice itself is Corroborated).

### Demo craft details (Verified per source)
- Show 2–3 strongest features, not everything (Pandey); 7-minute slot lost to feature-rushing kept a team in Top 10 instead of Top 3 (dev.to CodeZero account).
- Use realistic sample data ("Sam," real deadlines — not "asdf"/"test123") (wafi574).
- Make it interactive/memorable when possible: Dubit translated a judge's YouTube video into their native language **on stage** → backstage conversation with judges (Taneja).
- Move deliberately; pause on the "wow" moment (wafi574).
- Pitch shape from skills synthesis (Inferred): ~30% problem / 70% solution; 3-min pitch = 0–30s hook+problem, 30–100s demo, 100–150s build (name sponsors), 150–180s what's next.
- MLH organizer guide: budget **10 min per live demo** at closing (3 min demo + setup/questions/swap) — recommends against live demos at closing; show videos instead.

### "Demo gods" failure recovery (Corroborated)
- The recovery playbook across sources: backup video in a tab, realistic mock-data fallback when APIs rate-limit (LinkedIn 24h blueprint explicitly: "add fallback mock JSON data in case live API rate limits get hit during judging"), don't demo broken things (Pandey), rehearse until deliverable sleep-deprived.

---

## 6. Team formation and role splits (incl. solo)

### Team size patterns (Verified per source; overall pattern Corroborated)
- HN 3-time winner: teammates are the #1 factor; "at least one 10X programmer on each of my winning teams."
- Hackathon-Starter-Pack (GitHub guide): solo = fast prototype/small scope/tiny-but-polished; 2 people = split frontend/backend or build/pitch; 3–4 = most stable, clear roles + strict sync points; 5+ = only with disciplined leads.
- Maria (NEAR judge): big teams "pinkish" — unequal contribution assumed.
- Martina's 6-hour double-track win: "two parallel builds, clear ownership, fast decisions, constant iteration."
- brandminds (team with 20 combined wins): know the context/judges/criteria; manage time **and emotions** — "every member of the team is essential."

### Role splits that recur (Inferred from multiple accounts)
Builder(s) + pitch/demo owner is the minimal viable split (2-person pattern). For 3–4: frontend, backend/integrations, demo/pitch + Devpost submission. Non-coders can own research, testing, data, demo recording, writeup — but tasks need checkable outputs ("prepare five user-error examples by lunchtime," not "help with product") (dev.to Stavleak guide).

### Solo-hacker notes (Verified per source)
- Solo is viable but scope must shrink: "tiny scope, polished output" (Starter-Pack). Solo RetroAI Hackathon win (dev.to, sanjaysah): understand theme → milestone plan → leverage AI tools → polished demo.
- "30 Solo Dev Hackathon Lessons" (listsof30): solve your own immediate problems first (be the domain expert); depth over breadth — "AI can already do everything mediocre"; find people with taste; network anyway (solo doesn't mean isolated).
- BizThon 101 lists "solo grinding" (isolating) as a first-timer mistake — talk to teams, attend workshops (hints/starter code drop there).
- Dev.to first-hackathon guide: if alone, use team-matching channels; describe skills honestly; don't promise all-nighters to get invited.
- Solo win-rate vs teams: **Unknown** — no data found.

### Pre-agreed ground rules (Verified — Kurzweil Library winner account)
Agree code ownership/reuse rules **before** major design work. Have a backup location with internet (their venue closed 11pm; they moved to a residence and merged until 4am).

---

## 7. 24/48-hour time management

### The 24-hour blueprint pattern (Inferred — structure Corroborated across sources)
LinkedIn "Developer's Guide to Shipping Complete MVPs in 24 Hours" gives the most explicit hour-by-hour plan found:
- 00:00–02:00 Ideation & scope lock — 1 hero feature; **no new features after hour 2**
- 02:00–04:00 Hello-world deployment — repo + live URL immediately
- 04:00–14:00 Core build
- 14:00–18:00 UI polish + **mock-data fallbacks** for live APIs
- 18:00–21:00 Code freeze & bug fixes — stop adding code
- 21:00–24:00 Pitch video + slide deck + demo practice

Corroborating fragments: Taneja (25% on ideation); skills table (working skeleton by ~25% of clock ≈ hour 6 of 24; code freeze last ~15% ≈ 4h; submit 30 min before deadline — the 30-min rule is Corroborated by Devpost webinar + hackathonstarterkit: "Devpost deadlines are hard cutoffs"); Pandey (practice demo, refine pitch as a phase, not an afterthought).

### Sleep (Corroborated)
- Taneja: 3–4 hours was the sweet spot; "most top teams I observed including my own weren't coding all the time"; sleeping on a big bug → solved on waking.
- BizThon 101: one 4-hour block beats 48h straight of degrading productivity.
- Skills synthesis: "hackathons aren't marathons, they're relay races"; sleep before pitching.

### The danger zones (Verified per source)
- **Hours 3–6 ("the boring middle")**: rush fades, bugs aren't fun, imagined-vs-built gap feels huge — projects die here. Counter: 30-min focus windows, pair when stuck, switch tasks after 20 min on one bug, eat/walk (andomo3 skills doc).
- **Scope creep arrives ~hour 2** as "what if we also added…" (Medium protegeigdtuw; BizThon).
- **The final 2 hours** become a death march without a plan; first 8 hours get eaten by setup/API debugging/architecture arguments (protegeigdtuw).

### Pivot rules (Inferred — andomo3 skills doc, single source)
Pivot when: the core problem stopped being real; a technical blocker has no simpler approach; 4 hours pass with no clear path; the demo needs >2 min of explanation; the team can't say what it's building. Do NOT pivot when: the blocker is setup not concept; 6+ hours in with a partial demo working; frustration is the only evidence. "The worst outcome is not a bad idea, it is no finished project."

### 48-hour pattern
**Unknown** — sources skew 24h; the 24h blueprint likely stretches (more polish/robustness, same phase order), but no hour-by-hour 48h winner account was found. (Inferred: treat as 24h × 2 with a real sleep in the middle.)

---

## 8. The most common failure modes

Ranked by how often sources independently name them:

1. **Over-scoping / scope creep** (Corroborated — the #1 killer). BizThon: "Overscoping is the #1 killer"; simple tool becomes "cross-chain protocol with AI, DAO and token launch" → half-finished features, broken demo, exhausted team, confused judges. Fix: one core feature; "Demo Test" — if you can't demo it clearly in 3 minutes, it's too complex; scope down, then scope down again.
2. **Unfinished/broken demo with nothing to show** (Corroborated). Judges can tell "ran out of time" from "chose to keep it focused" — a half-built thing is worse than a simple thing that works (protegeigdtuw). MLH: completion is only one part of criteria — but you must demo *something*.
3. **No/inadequate demo prep** (Corroborated). "Code is 60% of the battle. Presentation is the other 60%." Teams that can't explain the build in plain language to non-technical judges leave points on the table. No backup when the demo fails.
4. **Tech that dies live** (Corroborated). Wifi/servers/laptops; API rate limits during judging; unfamiliar tech breaking mid-event (Amplify example). Fixes: backup video, mock-data fallbacks, boring stack, deploy early.
5. **Ignoring the rubric/requirements** (Verified). Judges report many submissions fail basic requirements; over-indexing one criterion; shoehorning a pet idea.
6. **Building for builders, not users** (Corroborated). Showing off tech choices; judges care whether someone's life gets better. Buzzword bingo without implementation.
7. **Poor time management** (Corroborated). 8h on setup; death-march final 2h; no plan. Submitting at the last minute vs hard Devpost cutoffs.
8. **Repository doesn't build for judges** (Verified — empirical). dev.to author ran all 164 submissions from one event: 69% built end-to-end; 33 installed deps then failed to compile; 8 wouldn't install; 9 had nothing to build. Most common: the hard part compiled, the ordinary part broke (TS error, missing artifact, unresolved package). "At the judging table they looked identical to the ones that would" build.
9. **Rehashed/recycled ideas** (Verified). Already-in-market, template resubmission, same project relabeled across hackathons.
10. **Team dysfunction** (Corroborated). Skill mismatch, no ground rules, emotional blowups under pressure, 5+ without leads.

---

## 9. What I could NOT verify (honest gaps)

- **Solo vs team win rates.** No dataset found comparing placement by team size. Solo wins exist (documented) but relative odds are Unknown.
- **Live demo vs video: which scores higher, systematically.** Evidence is mixed and format-dependent (online judging runs on video; in-person science-fair judging is live). No controlled comparison found.
- **Statistical claims about score weights** (e.g., "impact is up to 25%") beyond single-author assertions. Treat as one winner's experience, not a measured fact.
- **Prize amounts** for most winner anecdotes (Nisevich, Ang, Martina posts don't state them; not claimed).
- **48-hour hour-by-hour winner schedule.** Sources skew 24h.
- **Nick Singh's HackUVA guide** — mentioned on HN with a truncated URL; content not retrieved.
- **Identity of the "8 wins" LinkedIn author** (name not visible in snippet) — claims attributed generically.
- **The $35K funding / Snap accelerator claim** in the Medium playbook — single self-reported source, not independently verified.
- **Whether judges watch full videos** vs skimming — judges say video is primary, but watch-completion behavior is Unknown.
- **Judge bribery/gaming specifics** beyond legitimate prep (reading rubrics, targeting sponsor tracks) — out of scope, not researched.
