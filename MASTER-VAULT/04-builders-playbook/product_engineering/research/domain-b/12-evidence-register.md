# Domain B — 12: Evidence Register

> Every source consulted for the Domain B workstream, with classification. All accessed 2026-10-10. Claim labels: Verified / Corroborated / Inferred / Proposed / Unknown. Evidence classes: primary technical (vendor engineering blog/docs/paper, first-party) / first-hand practitioner (named person describing their own build) / corroborating (independent outlet confirming) / community observations (forums, Reddit/HN-style, social) / secondary interpretation (analysis of others' material) / unverified (single uncorroborated claim).

## Reading guide

- **Confidence** reflects the *claim as used in the files*, not the source in general.
- Vendor-published numbers (benchmarks, resolution rates, savings) are capped at **Corroborated** unless independently reproduced; company-run benchmarks are labeled as such.
- Where a source's date is approximate (search-result "Last Updated"), it is marked ~.

---

## E1. Duolingo Max launch (GlobeNewswire press release)

- **URL:** https://www.globenewswire.com/news-release/2023/03/14/2627053/0/en/index.html
- **Type:** primary technical (company press release) | **Author/org:** Duolingo | **Pub:** 2023-03-14 | **Accessed:** 2026-10-10
- **Claims used:** Max launched Mar 2023 with Explain My Answer + Roleplay; built with OpenAI from Sept 2022; GPT-4; prompt tuning + guardrails + accuracy verification
- **Confidence:** Verified | **Class:** primary technical
- **Corroboration:** widely re-reported; launch facts uncontested
- **Contradictions:** none on launch facts
- **Implication:** canonical "frontier API + post-training + guardrails" product pattern

## E2. Duolingo case study (Medium, Kay J)

- **URL:** https://medium.com/insightful-data-stories/the-duolingo-case-study-how-to-launch-ai-without-breaking-your-brand-91e195176775
- **Type:** secondary interpretation | **Author:** Kay J | **Pub:** ~2026-07-17 | **Accessed:** 2026-10-10
- **Claims used:** subscription revenue +50% 2024 to $607M; 10.3M paid subscribers Q1 2025; Video Call expansion; April 2025 "AI-first" memo
- **Confidence:** Corroborated | **Class:** secondary interpretation
- **Corroboration:** revenue figures match company earnings reporting
- **Implication:** separates product-feature success from org-policy controversy (B vs C)

## E3. Notion AI simplification (VentureBeat interview)

- **URL:** https://venturebeat.com/infrastructure/why-notions-biggest-ai-breakthrough-came-from-simplifying-everything
- **Type:** secondary w/ first-hand interview | **Author:** VentureBeat; interviewee Ryan Nystrom (Notion AI eng lead) | **Pub:** ~2026 | **Accessed:** 2026-10-10
- **Claims used:** simple prompts/human-readable representations beat complex schemas; V3 customizable agents = most successful AI tool ("step function improvement")
- **Confidence:** Corroborated | **Class:** first-hand practitioner (via interview)
- **Implication:** complexity ≠ quality in prompt/model design

## E4. Notion "brain vs body" architecture (YouTube deep-dive)

- **URL:** https://www.youtube.com/watch?v=we4n_u2Jtfc
- **Type:** secondary interpretation (video essay) | **Pub:** ~2026-08 | **Accessed:** 2026-10-10
- **Claims used:** LLM as intent-translator ("brain"), deterministic Notion Workers as executors ("body"); token savings from deterministic execution
- **Confidence:** Inferred | **Class:** secondary interpretation
- **Caveat:** not Notion-official; architecture described from public behavior
- **Implication:** the brain/body split as the central reliability pattern for LLM features

## E5. Intercom Fin Apex 1.0 (VentureBeat)

- **URL:** https://venturebeat.com/technology/intercoms-new-post-trained-fin-apex-1-0-beats-gpt-5-4-and-claude-sonnet-4-6
- **Type:** secondary (company benchmarks via press) | **Pub:** ~2026-03 | **Accessed:** 2026-10-10
- **Claims used:** 73.1% resolution vs ~71% GPT-5.4/Claude Opus 4.5; 65% hallucination reduction vs Sonnet 4.6; 3.7s response; ~1/5 inference cost; 2M+ conversations/week
- **Confidence:** Corroborated (company-run benchmark — not independent) | **Class:** corroborating
- **Contradictions:** independent case studies put real-world Fin resolution at 42–50% vs vendor's ~76% — marketing-vs-measured gap
- **Implication:** task-shaped small models can beat frontier models on task metrics + cost; vendor metrics aren't comparable

## E6. Fin pricing/comparison (Pluno, competitor)

- **URL:** https://pluno.ai/blog/intercom-fin-ai-vs-ada
- **Type:** secondary (competitor-authored) | **Pub:** ~2026-10 | **Accessed:** 2026-10-10
- **Claims used:** $0.99/outcome pricing; ~76% vendor-reported resolution; resolution definitions differ per vendor
- **Confidence:** Corroborated on pricing; Inferred on the comparability gap | **Class:** community observations
- **Caveat:** competitor source — treat product comparisons skeptically, pricing facts as corroborated

## E7. Fin corporate arc (LiveAgent comparison)

- **URL:** https://www.liveagent.com/blog/liveagent-vs-intercom-fin-ai-chatbot-comparison/
- **Type:** secondary (competitor-authored) | **Pub:** ~2026 | **Accessed:** 2026-10-10
- **Claims used:** Intercom renamed to Fin (May 2026); Salesforce acquisition ~$3.6B agreed June 2026, not closed
- **Confidence:** Corroborated | **Class:** corroborating
- **Implication:** "assistant as product" taken to its limit — the agent became the company

## E8. Intercom FDE interview (Gainsight)

- **URL:** https://www.gainsight.com/episode/18-months-7000-customers-67-support-resolution-inside-intercoms-fde-strategy-ft-diego-ballona-intercom/
- **Type:** first-hand practitioner (interview) | **Interviewee:** Diego Ballona, Intercom | **Pub:** ~2026-02 | **Accessed:** 2026-10-10
- **Claims used:** ~7,000 Fin customers; 67% average resolution rate (at that time); forward-deployed engineering model
- **Confidence:** Corroborated | **Class:** first-hand practitioner
- **Implication:** resolution rates move over time; date-stamp every metric

## E9. Klarna launch (Intelligent Fin.tech / press)

- **URL:** https://www.intelligentfin.tech/2024/04/09/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
- **Type:** primary technical (company announcement via press) | **Pub:** 2024-04-09 | **Accessed:** 2026-10-10
- **Claims used:** 2.3M conversations first month; 2/3 of chats; 700-agent workload equivalence; 11→<2 min; −25% repeats; satisfaction on par; 35+ languages; ~$40M projected
- **Confidence:** Verified | **Class:** primary technical
- **Corroboration:** OpenAI companion case study; Gizmodo contemporaneous coverage
- **Critical nuance:** "700" = workload equivalence, not layoffs (2022 layoffs were separate/macro)

## E10. Klarna reversal (IrisAgent, cites Bloomberg)

- **URL:** https://irisagent.com/blog/klarna-ai-reversal-mid-market-lessons/
- **Type:** secondary interpretation | **Pub:** ~2026-10 | **Accessed:** 2026-10-10
- **Claims used:** CEO May 2025 "gone too far"; rehiring humans; complex-tail accumulation; brand-metric softening
- **Confidence:** Verified (CEO on record via Bloomberg) | **Class:** corroborating
- **Implication:** the definitive "AI worked, strategy failed" case; automate-the-head/staff-the-tail

## E11. Klarna deep analysis (Twig)

- **URL:** https://www.twig.so/blog/klarna-ai-customer-support-efficiency
- **Type:** secondary interpretation | **Pub:** ~2026-06 | **Accessed:** 2026-10-10
- **Claims used:** Q3 2025: ~$60M savings, ~853 agent-equivalents, NPS 73, hybrid strategy retained
- **Confidence:** Corroborated | **Class:** secondary interpretation
- **Implication:** efficiency numbers kept growing even as strategy reversed — one metric can't carry the decision

## E12. Klarna analysis (ivanmisic.net)

- **URL:** https://ivanmisic.net/blog/ways-of-working/klarna-ai-u-turn-isnt-failure-story
- **Type:** secondary interpretation | **Author:** Ivan Misic | **Pub:** 2026-03-11 | **Accessed:** 2026-10-10
- **Claims used:** 2025 annual report: 80% of chats, no satisfaction drop, 49% headcount reduction since 2022, 3.6× revenue/employee; "47% satisfaction increase" and "15-min baseline" figures are unsourced myths
- **Confidence:** Corroborated | **Class:** secondary interpretation
- **Implication:** myth-busting matters — unsourced numbers circulate as fact

## E13. Moffatt v. Air Canada (tribunal decision via coverage)

- **URL:** https://www.youtube.com/watch?v=wXP4mR0JOeM (cites: 2024 BCCRT 149; CBC; ABA; McCarthy Tétrault)
- **Type:** secondary w/ primary citations | **Pub:** ~2026-08 | **Accessed:** 2026-10-10
- **Claims used:** chatbot invented bereavement-refund policy; tribunal awarded C$812.02; "separate legal entity" defense rejected — chatbot is the company
- **Confidence:** Verified | **Class:** corroborating (primary decision cited)
- **Implication:** hallucination rate is a legal liability metric; "beta" labels don't shield

## E14. Chevrolet $1 Tahoe (CTech)

- **URL:** https://m.calcalistech.com/Article.aspx?guid=b1gco00ioc
- **Type:** secondary | **Pub:** ~2024-01 | **Accessed:** 2026-10-10
- **Claims used:** Watsonville chatbot "sold" 2024 Tahoe for $1.00 via injected instruction; copycat 2-for-1 at Quirk Chevrolet; bot removed
- **Confidence:** Verified | **Class:** corroborating
- **Corroboration:** VentureBeat; AI Incident Database #622; TIME
- **Note:** MSRP cited as ~$58,195 or ~$76,000–81,395 across sources — use "~$58k+" or note variance

## E15. AI Incident Database (referenced)

- **URL:** https://incidentdatabase.ai/cite/622/ (cited, not directly opened)
- **Type:** incident registry | **Accessed:** 2026-10-10
- **Confidence:** Corroborated | **Class:** corroborating
- **Note:** listed for traceability; incident #622 = Chevy chatbot

## E16. Healthcare RAG failure (Medium, Sunil Kumar)

- **URL:** https://medium.com/@ailoittetech/we-shipped-a-rag-system-that-worked-perfectly-then-production-happened-53f366af55f2
- **Type:** first-hand practitioner | **Pub:** 2026-04-01 | **Accessed:** 2026-10-10
- **Claims used:** 94% demo accuracy → 38% production failure over 40k docs; root cause retrieval, not generation
- **Confidence:** Corroborated | **Class:** first-hand practitioner
- **Implication:** "retrieval failures wearing a generation costume"

## E17. RAG failure modes (Stackademic, Kawal Jain)

- **URL:** https://blog.stackademic.com/why-most-rag-pipelines-fail-in-production-6dd343b10454?gi=741475b7fea5
- **Type:** practitioner analysis | **Pub:** ~2026-05 | **Accessed:** 2026-10-10
- **Claims used:** demo/prod gap across ingestion, lifecycle, queries, concurrency; p99 <2s + token-cost targets
- **Confidence:** Corroborated | **Class:** corroborating

## E18. RAG dev-to-prod gap (Medium, Subhasish)

- **URL:** https://medium.com/@subhasishpraharaj52/why-your-rag-system-crushes-it-in-dev-but-craters-in-production-d32578fd68dd
- **Type:** practitioner analysis | **Pub:** ~2026-03 | **Accessed:** 2026-10-10
- **Claims used:** 90%→60% accuracy with green dashboards; ANN "slightly worse neighbors" mechanism
- **Confidence:** Corroborated | **Class:** corroborating
- **Implication:** monitor quality signals, not just uptime

## E19. Enterprise RAG platform (LinkedIn, Fortune-500 practitioner)

- **URL:** https://www.linkedin.com/pulse/making-enterprise-rag-platform-project-what-broke-when-atiqul-islam-bdftc
- **Type:** first-hand practitioner | **Pub:** ~2026-08 | **Accessed:** 2026-10-10
- **Claims used:** 20+ production workflows; incidents were retrieval failures; fix = platform infrastructure not bigger models
- **Confidence:** Corroborated | **Class:** first-hand practitioner
- **Caveat:** employer details withheld (generalized patterns only)

## E20. markcrawl postmortem (GitHub)

- **URL:** https://github.com/aimlpm/markcrawl/blob/HEAD/docs/POSTMORTEM_v0.10-v0.11.md
- **Type:** primary technical (project's own postmortem) | **Pub:** 2026-05 | **Accessed:** 2026-10-10
- **Claims used:** six releases in 72h driven by benchmark-surfaced silent ingestion failures
- **Confidence:** Verified | **Class:** primary technical
- **Implication:** ingestion needs diagnostics as a first-class feature; benchmarks surface real failure modes

## E21. First RAG production build (DEV, Blessing)

- **URL:** https://dev.to/blessedefem/i-built-a-production-rag-system-in-3-weeks-heres-what-actually-broke-556m
- **Type:** first-hand practitioner | **Pub:** ~2026-01 | **Accessed:** 2026-10-10
- **Claims used:** first-hour crashes (migrations, quotas, CORS); path from "no relevant info" to 90% success
- **Confidence:** Corroborated | **Class:** first-hand practitioner

## E22. Glean enterprise copilot (Glean blog)

- **URL:** https://www.glean.com/blog/the-enterprise-ai-copilot-playbook-for-business-leaders
- **Type:** primary technical (vendor) | **Pub:** ~2026 | **Accessed:** 2026-10-10
- **Claims used:** connectors → index/chunk → knowledge graph → hybrid retrieval → cited answers; real-time permission-aware indexing; fine-tuning rejected for enterprise knowledge
- **Confidence:** Corroborated (vendor-described) | **Class:** primary technical
- **Implication:** permission-awareness is a security control; "it's a search problem"

## E23. Glean architecture interview (tessl.io podcast)

- **URL:** https://tessl.io/podcast/enterprise-ai-solutions-need-to-be-different-glean-and-ex-slack-cpo-tamar-yehoshua-on-rag-changing-behavior-and-bring-your-own-model
- **Type:** first-hand practitioner (interview) | **Interviewee:** Tamar Yehoshua, ex-Slack CPO | **Pub:** ~2024 | **Accessed:** 2026-10-10
- **Claims used:** query→planning→search-query translation→retrieval→LLM; LLM-as-judge and LLM-jury evals; multi-LLM approach
- **Confidence:** Corroborated | **Class:** first-hand practitioner

## E24. Perplexity Photon (Perplexity engineering blog)

- **URL:** https://www.perplexity.ai/hub/blog/photon
- **Type:** primary technical (vendor engineering blog, full text fetched) | **Pub:** 2026-09-24 | **Accessed:** 2026-10-10
- **Claims used:** in-house Rust retrieval engine; compact posting lists; WAND-style traversal; docblob records; io_uring batch reads; 160ms p50/230ms p95; −68% cost at comparable quality; old system p99 800ms–1.2s; built by small team + coding-agent swarm
- **Confidence:** Verified (with company's own measurement caveats) | **Class:** primary technical
- **Implication:** at AI-search scale, retrieval infra is the cost/latency battleground

## E25. Artificial Analysis Search Index (via CryptoBriefing)

- **URL:** https://cryptobriefing.com/perplexity-tops-artificial-analysis-search-index/
- **Type:** secondary | **Pub:** ~2026-08 | **Accessed:** 2026-10-10
- **Claims used:** 1,700 questions, fixed model + harness; Perplexity 80, Parallel 75, Exa 74, no-search baseline 33
- **Confidence:** Corroborated | **Class:** corroborating
- **Implication:** third-party evidence that the search layer carries the quality

## E26. Algolia AI-search architecture (Algolia docs)

- **URL:** https://www.algolia.com/resources/asset/architecture-data-foundations-for-ai-powered-search
- **Type:** primary technical (vendor docs) | **Pub:** ~2026 | **Accessed:** 2026-10-10
- **Claims used:** constraints → hybrid retrieval → business tuning → rerank only within p95; LLM decides, index is source of truth
- **Confidence:** Verified | **Class:** primary technical

## E27. Google "What People Suggest" shutdown (Android Authority)

- **URL:** https://www.androidauthority.com/google-discontinues-what-people-suggest-feature-3649683/
- **Type:** secondary | **Pub:** ~2026-03 | **Accessed:** 2026-10-10
- **Claims used:** AI health-tips feature removed; Google framed as simplification; critics cite safety/accuracy evidence
- **Confidence:** Corroborated on shutdown; Inferred on motivations | **Class:** corroborating
- **Implication:** some domains need expert-source constraints, not better retrieval

## E28. Invoice extraction pipeline (Medium, practitioner)

- **URL:** https://medium.com/@vaidehivasudev3082/how-i-built-an-invoice-extraction-pipeline-with-google-vision-api-gpt-4-1-aa9fd95e7981
- **Type:** first-hand practitioner | **Pub:** ~2026-04 | **Accessed:** 2026-10-10
- **Claims used:** PDF→image→Vision OCR→GPT-4.1→JSON; 98.7% clean / 92.3% handwritten OCR (n=500); OCR accuracy caps extraction accuracy
- **Confidence:** Corroborated | **Class:** first-hand practitioner

## E29. Extraction cost optimization (DEV)

- **URL:** https://dev.to/avneet_bansal_a65b3f31fc4/cut-llm-document-extraction-cost-by-85-without-losing-accuracy-34ip
- **Type:** practitioner | **Pub:** ~2026-10-08 | **Accessed:** 2026-10-10
- **Claims used:** −85–93% per-document cost via adaptive fields + tiered routing + field caching + scale-to-zero
- **Confidence:** Inferred (workload-specific) | **Class:** community observations

## E30. Netflix GenRec (Netflix Technology Blog, syndicated)

- **URL:** https://noise.getoto.net/author/netflix-technology-blog/ (original: netflixtechblog.com)
- **Type:** primary technical | **Authors:** Ying Li, Arjun Rao, Shradha Sehgal | **Pub:** ~2026 | **Accessed:** 2026-10-10
- **Claims used:** off-the-shelf LLMs fail as recommenders (popularity bias, catalog hallucination, weak personalization); GenRec = domain-adapted foundation LLM + ranking post-training; verbalized histories; vLLM prefill-only scoring; matches/exceeds production with fewer labels
- **Confidence:** Verified (existence/design); Corroborated (results — company-run) | **Class:** primary technical
- **Implication:** LLM rankers over closed catalogs — the catalog constraint is the safety mechanism

## E31. Netflix recommendations deep-dive (systems-design synthesis)

- **URL:** https://github.com/lourdhu02/systems-design/blob/HEAD/14-case-studies-deep-dives/netflix-recommendations-deep-dive.md
- **Type:** secondary synthesis | **Pub:** ~2026-09 | **Accessed:** 2026-10-10
- **Claims used:** multi-retriever fan-out → multi-objective ranker → bandit post-processing; personalization at every surface; experimentation as infrastructure
- **Confidence:** Corroborated | **Class:** secondary interpretation

## E32. Recommender funnel (DEV, Daniel Samfdo)

- **URL:** https://dev.to/danielsamfdo/the-10-millisecond-trick-how-recommenders-search-millions-of-items-before-you-blink-4dkp
- **Type:** practitioner explainer | **Pub:** ~2026-10-06 | **Accessed:** 2026-10-10
- **Claims used:** retrieval (~10ms) → ranking (~30ms) → re-rank (~10ms); funnel widths trade quality for latency
- **Confidence:** Corroborated | **Class:** corroborating

## E33. Two-tower retrieval (Google Cloud blog)

- **URL:** https://cloud.google.com/blog/products/ai-machine-learning/scaling-deep-retrieval-tensorflow-two-towers-architecture
- **Type:** primary technical | **Authors:** Jeremy Wortz, Jordan Totten | **Pub:** ~2023 | **Accessed:** 2026-10-10
- **Claims used:** two-tower encoders for candidate retrieval; ANN serving; Spotify playlist worked example
- **Confidence:** Verified | **Class:** primary technical

## E34. TikTok recommender anatomy (LinkedIn, J.K. Bergum)

- **URL:** https://www.linkedin.com/pulse/anatomy-large-scale-recommender-systems-jo-kristian-bergum-a3eef
- **Type:** practitioner | **Pub:** 2025-01-20 | **Accessed:** 2026-10-10
- **Claims used:** real-time feedback loop; two-tower retrieval; frozen item embeddings + live user embeddings; ms-scale multi-stage serving
- **Confidence:** Corroborated | **Class:** first-hand practitioner

## E35. Multimodal production guide (channel.tel)

- **URL:** https://www.channel.tel/blog/multimodal-ai-agents-voice-vision-text-production
- **Type:** practitioner guide | **Pub:** ~2026-03 | **Accessed:** 2026-10-10
- **Claims used:** temporal sync as hardest fusion problem; per-modality health checks/fallbacks; cost ranges ($0.01–0.05 text conv; +$0.02–0.10 voice min; +$0.01–0.05/image)
- **Confidence:** Corroborated (ranges) | **Class:** first-hand practitioner

## E36. Multimodal production practices (devthread.in handbook)

- **URL:** https://github.com/rajsekharalluri/devthread.in/blob/HEAD/content/genai-engineer/multimodal.md
- **Type:** practitioner handbook | **Pub:** ~2026-09 | **Accessed:** 2026-10-10
- **Claims used:** cost/latency/accuracy/storage/privacy/security/eval/file-handling practices; visual prompt injection warning
- **Confidence:** Corroborated | **Class:** corroborating

## E37. Realtime voice API (ai-coding-guide)

- **URL:** https://github.com/forhow134/ai-coding-guide/blob/HEAD/docs/08-multimodal/video-realtime.md
- **Type:** practitioner guide | **Pub:** 2026-02-20 | **Accessed:** 2026-10-10
- **Claims used:** realtime speech-to-speech ~320ms; 10–20× cost of regular API
- **Confidence:** Corroborated | **Class:** community observations

## E38. Humane AI Pin failure (Digital Trends)

- **URL:** https://www.digitaltrends.com/phones/i-knew-the-humane-ai-pin-would-fail/
- **Type:** secondary | **Pub:** ~2025 | **Accessed:** 2026-10-10
- **Claims used:** 100k projected, ~10k sold; bricked Feb 28 2025; fundamental error = replacing the phone screen
- **Confidence:** Verified | **Class:** corroborating

## E39. Rabbit R1 reviews (Dexerto/MKBHD)

- **URL:** https://www.Dexerto.com/tech/marques-brownlee-slams-another-ai-product-as-barely-reviewable-after-humane-ai-pin-controversy-2669843/
- **Type:** secondary (reviewer) | **Pub:** 2024 | **Accessed:** 2026-10-10
- **Claims used:** 100k pre-orders; demo exceeded shipped product; "barely reviewable"; LAM without training data
- **Confidence:** Corroborated | **Class:** community observations

## E40. Tony Fadell on AI gadgets (WebProNews)

- **URL:** https://www.webpronews.com/why-tony-fadell-says-the-ai-gadget-experiment-already-failed/
- **Type:** secondary (on-record quotes) | **Pub:** 2026-10-08 | **Accessed:** 2026-10-10
- **Claims used:** Gen-1 AI gadgets failed; solved no genuine problem; exec-assistant projection fallacy
- **Confidence:** Verified (quotes) | **Class:** corroborating

## E41. Meta Muse Image removal (iHeart/WRKO; Campaign Asia)

- **URLs:** https://wrko.iheart.com/content/2026-07-13-new-meta-ai-app-disabled-after-pushback/ ; https://www.campaignlive.com/article/meta-removes-controversial-ai-feature-within-days-launch/1964439
- **Type:** secondary | **Pub:** 2026-07-13 | **Accessed:** 2026-10-10
- **Claims used:** removed days after July 7 launch; auto-opt-in backlash; SAG-AFTRA/CAA objections; non-consensual digital replicas
- **Confidence:** Verified | **Class:** corroborating
- **Implication:** consent architecture is the safety architecture for generative visual features

## E42. tau-bench / MCP-Universe (via production-llm-patterns synthesis)

- **URL:** https://github.com/kchia/production-llm-patterns/blob/HEAD/patterns/orchestration/tool-call-reliability/README.md
- **Type:** practitioner synthesis citing Sierra + Salesforce | **Pub:** ~2026-04 | **Accessed:** 2026-10-10
- **Claims used:** tau-bench GPT-4o 61% single-trial → ~25% across 8 trials; MCP-Universe best 43.7%; structured outputs <40%→100% syntactic; 85%-per-step → ~20% over 10 steps
- **Confidence:** Corroborated | **Class:** corroborating
- **Implication:** the harness does the reliability work, not the model

## E43. Tool-call failure modes (techsy.io)

- **URL:** https://techsy.io/en/blog/llm-function-calling-guide
- **Type:** practitioner guide | **Pub:** ~2026-03 | **Accessed:** 2026-10-10
- **Claims used:** five failure modes; return errors to the model as structured messages; boundary-layer principle (auth/timeouts/retries outside the model)
- **Confidence:** Corroborated | **Class:** first-hand practitioner

## E44. Zapier Agents (digitalapplied; gmtasoftware; techintelpro)

- **URLs:** https://www.digitalapplied.com/blog/ai-workflow-automation-agentkit-make-zapier ; https://www.gmtasoftware.com/blog/top-ai-workflow-automation-tools/ ; https://techintelpro.com/news/ai/enterprise-ai/zapier-launches-copilot-ai-and-governance-upgrades
- **Type:** secondary | **Pub:** 2025–2026 | **Accessed:** 2026-10-10
- **Claims used:** 8k+ integrations; autonomous agents (2025); Copilot; MCP; HITL; 1.2M agent-step workflows H1 2026 (+340%); enterprise 34% of revenue; limitations (layered-on AI, unpredictable task pricing, per-workflow secrets)
- **Confidence:** Corroborated (features); Inferred (vendor-reported stats via third parties) | **Class:** secondary interpretation

## E45. $63 runaway loop (devtalk forum)

- **URL:** https://forum.devtalk.com/t/a-63-mistake-in-production-how-an-ai-agents-loop-escaped-without-guards/250506
- **Type:** first-hand practitioner postmortem | **Pub:** 2026-10-09 | **Accessed:** 2026-10-10
- **Claims used:** 31M tokens / $63 overnight; disarmed attempt counter; unreachable freshness check; spend-ceiling lesson
- **Confidence:** Verified | **Class:** first-hand practitioner

## E46. Polly Harness (GitHub)

- **URL:** https://github.com/jonnydubowsky/polly_harness
- **Type:** primary technical (reference build + postmortem) | **Pub:** ~2026-08 | **Accessed:** 2026-10-10
- **Claims used:** 9-layer harness; 229-case eval; 8 judges; 98.7% injection / 100% jailbreak resistance; honest non-passing axes (policy 60%, tool-safety 42% stress)
- **Confidence:** Corroborated (self-reported, public methodology) | **Class:** primary technical
- **Implication:** "production-grade" as measured per-axis thresholds

## E47. Layered agent defense (DEV)

- **URL:** https://dev.to/hosseinhezami/when-an-ai-agent-makes-a-mistake-in-production-which-layer-should-stop-it-4m0b
- **Type:** practitioner | **Pub:** ~2026-09 | **Accessed:** 2026-10-10
- **Claims used:** refund-the-subscription-instead-of-add-on failure; earliest-deterministic-layer doctrine; 8-layer defense
- **Confidence:** Corroborated | **Class:** first-hand practitioner

## E48. Agent postmortem method (kubaik.github.io)

- **URL:** http://kubaik.github.io/fix-ai-agent-failures-postmortem-guide/
- **Type:** practitioner guide | **Pub:** ~2026-10-04 | **Accessed:** 2026-10-10
- **Claims used:** timeline via template-hash grouping; cost arithmetic for template changes; rollback + regression-check + length-alert action items
- **Confidence:** Corroborated | **Class:** first-hand practitioner

## E49. Agent reliability ops (vibereference)

- **URL:** https://github.com/data-advantage/vibereference/blob/HEAD/content/ai-development/agent-reliability-production-operations.md
- **Type:** practitioner ops doc | **Pub:** ~2026-09 | **Accessed:** 2026-10-10
- **Claims used:** SEV-1 kill-switch/containment playbook; team roles (on-call, eval owner, cost owner, quality owner, IC); 48–72h post-deploy monitoring
- **Confidence:** Corroborated | **Class:** first-hand practitioner

## E50. Prompt-injection incident catalog (awesome-agent-failures)

- **URL:** https://github.com/travisbreaks/awesome-agent-failures/blob/HEAD/docs/failure-modes/prompt-injection.md
- **Type:** community catalog | **Pub:** ~2026-03 | **Accessed:** 2026-10-10
- **Claims used:** Notion AI PDF exfiltration (2025); Chevy $1 Tahoe; "lethal trifecta" framing
- **Confidence:** Corroborated | **Class:** community observations

## E51. Injection TTPs (tryhackme notes)

- **URL:** https://github.com/anatoli308/tryhackme_stuff/blob/HEAD/ai_security_learnings/prompt_injectionNICE.md
- **Type:** practitioner notes | **Pub:** ~2026-05 | **Accessed:** 2026-10-10
- **Claims used:** ingestion surfaces (web, email, docs, repos); Bing Chat pirate-persona demo; EchoLeak zero-click mechanics
- **Confidence:** Corroborated | **Class:** community observations

## E52. CVE/injection roundup (kelacyber)

- **URL:** https://www.kelacyber.com/blog/prompt-injection-attack/
- **Type:** security vendor | **Pub:** ~2026-09 | **Accessed:** 2026-10-10
- **Claims used:** EchoLeak CVE-2025-32711 (CVSS 9.3, fixed Jun 2025); ChatGPT memory exploit (Rehberger, Sep 2024); attacker objectives taxonomy
- **Confidence:** Verified (CVE records) | **Class:** corroborating

## E53. Injection CVE table (cyberdesserts)

- **URL:** https://blog.cyberdesserts.com/prompt-injection-attacks/
- **Type:** practitioner | **Pub:** ~2026-09 | **Accessed:** 2026-10-10
- **Claims used:** CVE-2025-59944 (Cursor), CVE-2026-24307 Reprompt, OpenClaw/ClawHavoc supply-chain (1,184 skills, ~4k machines), Gemini/Jira injection bounty
- **Confidence:** Corroborated | **Class:** community observations
- **Caveat:** fast-moving; some 2026 CVEs single-sourced — treat as Corroborated, not Verified

## E54. Samsung ChatGPT ban (DEV, Eyal Doron)

- **URL:** https://dev.to/eyal_doron_aisec/prompt-injection-what-security-managers-need-to-know-1ba4
- **Type:** practitioner | **Pub:** 2025-11 | **Accessed:** 2026-10-10
- **Claims used:** Apr 2023 engineers pasted confidential code → emergency internal GenAI ban; Bing "Sydney" extraction; Chevy; resume-screening white-text attack
- **Confidence:** Verified (ban widely documented) | **Class:** corroborating

## E55. AKR-Evals (GitHub)

- **URL:** https://github.com/rbabbell/akr-evals
- **Type:** primary technical | **Pub:** ~2026-04 | **Accessed:** 2026-10-10
- **Claims used:** 15% silent regression found weeks later; $200K+ impact claim; regression detection + cost tracking + CI gates as the fix
- **Confidence:** Corroborated (impact figure self-reported) | **Class:** primary technical

## E56. LLM observability + evals (mehaisi.com)

- **URL:** https://mehaisi.com/blog/llm-observability-tracing-and-evals
- **Type:** practitioner | **Pub:** ~2026-08 | **Accessed:** 2026-10-10
- **Claims used:** p95 chains add (2s×3 → 6–8s); production-to-eval loop; judge–human correlation 80–85%; $0.02–0.05/eval call (~$3 per 100-Q suite)
- **Confidence:** Corroborated | **Class:** first-hand practitioner
- **Caveat:** 80–85% figure practitioner-cited; no primary study located

## E57. Evals explainer (explainx.ai)

- **URL:** https://www.explainx.ai/blog/ai-evals-for-engineers-and-pms-explained-2026
- **Type:** practitioner synthesis | **Pub:** 2026-10-01 | **Accessed:** 2026-10-10
- **Claims used:** 60/30/10 scoring mix; dataset is 90% of the problem; never judge-alone; Livenerf/LangSmith updates
- **Confidence:** Corroborated | **Class:** corroborating

## E58. Golden-dataset practices (claude-exam-prep)

- **URL:** https://github.com/hareli26/claude-exam-prep/blob/HEAD/subjects/evals.md
- **Type:** practitioner handbook | **Pub:** ~2026-04 | **Accessed:** 2026-10-10
- **Claims used:** size guidance (50/200–500/1000+); holdout 20–30%; regression testing per prompt change; judge calibration
- **Confidence:** Corroborated | **Class:** corroborating

## E59. Eval pipeline minimum (dev-best-practices)

- **URL:** https://github.com/gerfru/dev-best-practices/blob/HEAD/plugins/dev/skills/design-llm/references/evaluation-framework.md
- **Type:** practitioner reference | **Pub:** ~2026-09 | **Accessed:** 2026-10-10
- **Claims used:** golden → offline (RAGAS) → gate (≥ baseline −3%) → online 10% judge-sample → feedback loop; benchmark types
- **Confidence:** Corroborated | **Class:** corroborating

## E60. Observability landscape (awesome-llm-observability)

- **URL:** https://github.com/devilking7x/awesome-llm-observability
- **Type:** curated list | **Pub:** ~2026-09 | **Accessed:** 2026-10-10
- **Claims used:** tool inventory (Langfuse, Braintrust, Galileo, Helicone, LangSmith, etc.); OTel convergence
- **Confidence:** Verified (existence of tools) | **Class:** secondary interpretation

## E61. LLM cost optimization (CloudZero)

- **URL:** https://www.cloudzero.com/blog/llm-cost-optimization/
- **Type:** practitioner (FinOps) | **Pub:** 2026-10-01 | **Accessed:** 2026-10-10
- **Claims used:** routing 40–70%; prompt caching ~90% on cached input; batch 50%; stacking to ~95%; cheapest token = unsent
- **Confidence:** Corroborated (ranges) | **Class:** first-hand practitioner

## E62. Inference optimization (interview-prep synthesis)

- **URL:** https://github.com/sanigam/ai-ml-interview-prep/blob/HEAD/43_LLM_Inference_Optimization/LLM_Inference_Optimization.md
- **Type:** practitioner synthesis | **Pub:** ~2026-05 | **Accessed:** 2026-10-10
- **Claims used:** routing/cascading with fallback; 80/20 → ~72% worked example; spot/quantization/batch levers
- **Confidence:** Inferred (illustrative math) | **Class:** community observations

## E63. AI gateway cost controls (NeuralTrust)

- **URL:** https://neuraltrust.ai/blog/ai-gateway-llm-cost-optimization
- **Type:** vendor-practitioner | **Pub:** ~2026-09 | **Accessed:** 2026-10-10
- **Claims used:** a16z framing (inference = largest AI-app cost line); gateway: routing, semantic caching, budgets, attribution
- **Confidence:** Corroborated | **Class:** corroborating

## E64. Cost/latency engineering (aws_book Ch.50)

- **URL:** https://github.com/dhyanendrasinghsikarwar/aws_book/blob/HEAD/Ch50_LLM_Cost_and_Latency_Engineering.md
- **Type:** practitioner handbook | **Pub:** ~2026-08 | **Accessed:** 2026-10-10
- **Claims used:** semantic caching definition; routing economics; "streaming doesn't reduce cost"; provisioned vs batch; evaluate every optimization
- **Confidence:** Corroborated | **Class:** corroborating

## E65. Cost-optimization techniques (DEV)

- **URL:** https://dev.to/dishant_sethi/llm-cost-optimization-cut-ai-inference-costs-47-80-without-sacrificing-quality-6f4
- **Type:** practitioner | **Pub:** ~2026-06 | **Accessed:** 2026-10-10
- **Claims used:** technique table (routing 40–70%, prompt cache 60–90%, semantic cache 31–47%, quantization 30–60%, batch 50%); OSS-for-narrow-tasks caveat
- **Confidence:** Inferred (ranges) | **Class:** community observations

## E66. LLMOps release checklist (QuashBugs)

- **URL:** https://quashbugs.com/blog/llmops-what-it-is-and-how-to-do-it
- **Type:** practitioner | **Pub:** 2026-10-02 | **Accessed:** 2026-10-10
- **Claims used:** 12-point release/ops checklist; version the bundle; canary/shadow; test rollback of full bundle
- **Confidence:** Corroborated | **Class:** first-hand practitioner

## E67. MLOps vs LLMOps (DEV)

- **URL:** https://dev.to/robert_kawoski_20bd638fd2/mlops-and-llmops-keep-your-ai-reliable-after-launch-17ch
- **Type:** practitioner | **Pub:** 2026-10-07 | **Accessed:** 2026-10-10
- **Claims used:** versioning/eval/cost/rollback-unit contrasts; per-call logging schema; three drift lenses incl. behavioral drift
- **Confidence:** Corroborated | **Class:** corroborating

## E68. LLMOps production scenario (ai-engineering-handbook)

- **URL:** https://github.com/psssnikhil/ai-engineering-handbook/blob/HEAD/docs/production/module-10-llmops-production-systems/lessons/01-Introduction-to-LLMOps.md
- **Type:** practitioner handbook | **Pub:** ~2026-07 | **Accessed:** 2026-10-10
- **Claims used:** RAG-legal-summarizer go-live checklist (prompt registry, eval suite, token logging, fallbacks, caching, alerts, shadow test)
- **Confidence:** Corroborated | **Class:** corroborating

## E69. Monitoring rules (frp agent rules)

- **URL:** https://github.com/snowdreamtech/frp/blob/HEAD/.agent/rules/llm-prompt.md
- **Type:** practitioner ruleset | **Pub:** ~2026-09 | **Accessed:** 2026-10-10
- **Claims used:** alert thresholds (cost 2×, p95 3×p50, errors 2%, format 0.5%); fallback ladder; weekly 1–5% audits; quarterly red-teams
- **Confidence:** Corroborated | **Class:** community observations

## E70. Prompts-fail-as-guardrails (DEV)

- **URL:** https://dev.to/rcortez056/why-prompts-fail-as-ai-agent-guardrails-and-how-to-fix-it-47j5
- **Type:** practitioner | **Pub:** ~2026-09-30 | **Accessed:** 2026-10-10
- **Claims used:** $50 auto/escalate pattern; tool-scope isolation; state rollbacks; human approval loops
- **Confidence:** Corroborated | **Class:** first-hand practitioner

## E71. AI UX trust patterns (Standard Beagle)

- **URL:** https://standardbeagle.com/designing-trust-in-ai-products/
- **Type:** practitioner (design studio) | **Pub:** ~2025-11 | **Accessed:** 2026-10-10
- **Claims used:** label AI; set expectations; communicate uncertainty; contextual explanations; HITL; co-creation; Waymo/Netflix/DeepMind examples
- **Confidence:** Corroborated | **Class:** corroborating

## E72. Hallucination-proof UX (Medium, Werkmeister)

- **URL:** https://medium.com/design-bootcamp/hallucination-proof-design-ux-patterns-for-untrustworthy-ai-output-a9e255b9c07c
- **Type:** practitioner | **Pub:** ~2026-09-26 | **Accessed:** 2026-10-10
- **Claims used:** five patterns (receipts, visible uncertainty, loud failure in high-stakes zones, human verification loop, graceful "I don't know")
- **Confidence:** Corroborated | **Class:** first-hand practitioner

## E73. AI product metrics + agentic UX (ai-expert SKILL.md)

- **URL:** https://github.com/felixgeelhaar/skills/blob/HEAD/ai-expert/SKILL.md
- **Type:** practitioner reference | **Pub:** ~2026-06 | **Accessed:** 2026-10-10
- **Claims used:** task completion rate 75–80% healthy (85–95% high-stakes); intervention/regenerate/copy/hallucination rates; cost per task; streaming; approval gates
- **Confidence:** Corroborated (benchmarks are practitioner norms) | **Class:** community observations

## E74. AI-native UX uncertainty design (buzzi.ai)

- **URL:** https://buzzi.ai/insights/ai-native-applications-ux-design-patterns
- **Type:** practitioner (design studio) | **Pub:** ~2026 | **Accessed:** 2026-10-10
- **Claims used:** confidence buckets (>0.8/0.5–0.8/<0.5); "needs review" queues; clarification prompts; source buttons
- **Confidence:** Corroborated | **Class:** corroborating

## E75. LLM features production skill (skill-forge)

- **URL:** https://github.com/byshahriar/skill-forge/blob/HEAD/skills/llm-features/SKILL.md
- **Type:** practitioner playbook | **Pub:** ~2026-08 | **Accessed:** 2026-10-10
- **Claims used:** validate-before-act; failure-path design; temperature discipline; cost/latency budgets; evals in CI; quality-signal instrumentation
- **Confidence:** Corroborated | **Class:** community observations

## E76. Production agent patterns (juanlara18 field notes)

- **URL:** https://github.com/juanlara18/portfolio/blob/HEAD/front/public/blog/posts/field-notes/production-llm-agents-patterns.md
- **Type:** practitioner field notes | **Pub:** ~2026-09 | **Accessed:** 2026-10-10
- **Claims used:** tracing/evals/monitoring triad; cost-per-successful-task; iteration-budget alerts; escalation counts
- **Confidence:** Corroborated | **Class:** first-hand practitioner

---

## Negative-evidence log (claims of failure/removal/cost overrun found)

| # | Claim | Source | Confidence |
|---|---|---|---|
| N1 | Klarna: AI cost-cutting "gone too far"; humans rehired May 2025 | E10 | Verified |
| N2 | Healthcare RAG: 94% demo → 38% production failure | E16 | Corroborated |
| N3 | RAG accuracy 90%→60% with green dashboards | E18 | Corroborated |
| N4 | markcrawl: benchmark forced 6 releases in 72h over silent ingestion failures | E20 | Verified |
| N5 | Air Canada: C$812 liability for hallucinated policy | E13 | Verified |
| N6 | Chevy $1 Tahoe; DPD bot; both pulled | E14 (+TIME) | Verified |
| N7 | NYC MyCity bot: illegal advice → 2026 shutdown (The Markup) | secondary (YouTube E13's source list) | Corroborated |
| N8 | Google "What People Suggest" shut down Mar 2026 | E27 | Corroborated |
| N9 | Google AI Overviews: glue-pizza/rocks failures → scaled back | widely reported 2024 | Corroborated |
| N10 | Humane AI Pin: 100k projected → ~10k sold → bricked Feb 2025 | E38 | Verified |
| N11 | Rabbit R1: demo exceeded shipped product; "barely reviewable" | E39 | Corroborated |
| N12 | Meta Muse Image: removed days after launch (consent backlash) | E41 | Verified |
| N13 | $63/31M-token runaway agent loop | E45 | Verified |
| N14 | EchoLeak: zero-click Copilot exfiltration, CVSS 9.3 | E52 | Verified |
| N15 | OpenClaw/ClawHavoc: 1,184 malicious skills, ~4k machines | E53 | Corroborated |
| N16 | Samsung: confidential code pasted → internal GenAI ban | E54 | Verified |
| N17 | AKR: 15% silent regression, $200K+ claimed impact | E55 | Corroborated |
| N18 | tau-bench: 61% → 25% across 8 trials; MCP-Universe best 43.7% | E42 | Corroborated |
| N19 | Google Assistant: 17 features cut (Jan 2024) | digitaltrends.com | Corroborated |
| N20 | AI companions: 29 agents, none met full crisis-response criteria (2025 eval) | webpronews.com | Corroborated |

## Honest gaps (Unknown)

1. No vendor publishes per-feature inference costs, full golden datasets, judge prompts, or training-data composition (Fin Apex, Klarna, Duolingo, Glean, Perplexity ranking signals).
2. No AI-quality SLO published by any assistant vendor (only uptime SLAs).
3. No public third-party safety audit of a commercial assistant's injection defenses.
4. Judge–human correlation (80–85%) is practitioner-cited; no primary study located.
5. Whether undisclosed injection breaches have occurred at major vendors is unknowable from public sources.
6. Exact MSRP in the Chevy incident varies by source ($58,195–$81,395); the $1.00 figure is consistent.
7. The "47% satisfaction increase" Klarna figure circulating online is unsourced (per E12) — do not repeat.
