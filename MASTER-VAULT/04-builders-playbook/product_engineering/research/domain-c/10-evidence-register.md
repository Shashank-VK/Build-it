# Domain C — Evidence Register

**Workstream:** domain-c · Compiled 2026-10-10 · All sources accessed 2026-10-10

> Per-finding metadata for the Domain C research. Claim labels: **Verified** (primary/credible corroboration) / **Corroborated** (multiple independent sources, some vendor-adjacent) / **Inferred** (analyst synthesis) / **Proposed** (practitioner recommendation) / **Unknown** (not found). Evidence classes: primary technical / first-hand practitioner / corroborating / community observations / secondary interpretation / unverified (vendor marketing).

## Customer support (01)

| # | Claim | URL | Source type / author | Pub date | Confidence | Corroboration / contradictions | Engineering implication |
|---|---|---|---|---|---|---|---|
| C1 | Klarna cut ~700 support staff / ~40% workforce for AI support (OpenAI partnership), then reversed May 2025; CEO: "went too far," cost "too predominant" | https://news.outsourceaccelerator.com/klarna-reintroduces-human-support/ ; https://mlq.ai/news/klarna-ceo-admits-aggressive-ai-job-cuts-went-too-far-starts-hiring-again-after-us-ipo/ | Secondary press / corroborating | 2025 | High (Verified) | Corroborated across Bloomberg, CX Dive, LaSoft; company metrics (82% faster, 25% fewer repeats) company-reported | Don't cut escalation capacity with automation; measure the long tail |
| C2 | Air Canada liable for chatbot's invented bereavement policy; CA$812.02; "remarkable submission" | https://en.wikipedia.org/wiki/Moffatt_v._Air_Canada | Secondary (Wikipedia citing tribunal + Guardian/BBC) | Case Feb 2024 | High (Verified) | Corroborated by Guardian, BBC, ABA | Bot's words = company's words; policy answers need grounding |
| C3 | Cursor bot "Sam" invented single-device policy; co-founder confirmed; users cancelled | https://www.pymnts.com/news/artificial-intelligence/chatbot-tracker/2026/courts-tell-companies-they-own-what-their-chatbot-says/ | Secondary press citing Ars Technica + Reddit | Apr 2025 | High (Corroborated) | Truell confirmation on Reddit (first-hand) | Community amplifies invented policy before correction lands |
| C4 | Vendor resolution claims 67–90% vs independent median ~41%, top quartile ~59%; resolution≠deflection inflates 20–40 pts | http://aithority.com/machine-learning/new-2026-benchmark-maps-ai-customer-service-performance-across-six-industries-resolution-csat-and-cost-per-resolution/ | Secondary (Aissist.io benchmark, vendor-adjacent) | 2026 | Medium (Corroborated) | Direction consistent with Forethought benchmark | Demand true-resolution definitions in procurement |
| C5 | ~75% of firms rolled back/shut down customer-facing AI agents at some point | https://www.webpronews.com/ai-hallucinations-turn-customers-against-frontline-workers/ | Secondary press citing survey | 2026 | Medium (Corroborated) | Survey details thin; consistent with Gartner 40%+ cancellation prediction | Rollback planning is normal, not exceptional |
| C6 | Gartner: by 2027 half of firms that cut CS staff for AI will rehire similar work | https://chatmaxima.com/blog/what-smbs-ask-a-chatbot-to-fix/ | Secondary (vendor blog citing Gartner Feb 2026) | 2026 | Medium (Corroborated) | Prediction, not outcome | Staffing decisions should be reversible |
| C7 | Practitioner: agent authorised to suspend accounts wrongly suspended critical revenue account | https://news.ycombinator.com/item?id=48014734 | First-hand practitioner / community | May 2026 | Medium (Corroborated) | Single account; consistent with permission-breadth pattern | Never grant irreversible actions without approval gates |
| C8 | Intercom Fin: ~76% avg resolution (vendor); $0.99/resolution pricing | https://assembly.com/blog/zendesk-vs-intercom | Secondary comparison | 2026 | Medium (Corroborated) | Resolution figure vendor-reported (Unverified); pricing public (Verified) | Per-resolution pricing is unpredictable at scale |

## Research & knowledge management (02)

| # | Claim | URL | Source type / author | Pub date | Confidence | Corroboration / contradictions | Engineering implication |
|---|---|---|---|---|---|---|---|
| K1 | 70% of RAG systems lack systematic evaluation; GraphRAG 3–5× cost; hybrid+rerank +15–30% precision | https://nstarxinc.com/blog/the-next-frontier-of-rag-how-enterprise-knowledge-systems-will-evolve-2026-2030/ | Secondary interpretation (industry analysis) | 2026 | Medium (Corroborated) | Direction widely echoed | Eval harness before scale; budget graph extraction honestly |
| K2 | EchoLeak CVE-2025-32711: unclicked email exfiltrated data via M365 Copilot RAG | https://www.csoonline.com/article/4163888/securing-rag-pipelines-in-enterprise-saas.html ; https://github.com/yehielamor/provenance-gate/blob/HEAD/poc/incidents_analysis.md | Primary technical (CVE/arXiv analysis) | Late 2025 | High (Verified) | Aim Security analysis corroborates | Retrieved content is untrusted input; treat render paths as sinks |
| K3 | ServiceNow RAG connector ignores user criteria at ingestion; non-ACL sources return results to every user | https://dev.to/fernando_azevedo_6844e930/rag-on-servicenow-the-connector-that-erases-user-criteria-2bnb | First-hand practitioner | Oct 2026 | Medium (Corroborated) | Single deployment; matches OWASP confused-deputy pattern | Verify each connector's ACL contract; pre-filter, don't post-filter |
| K4 | "300–500% RAG ROI in year one" claims have no methodology/sample/citations; headline figures unsourced or contradicted | https://github.com/athandapani/ai-adoption-wiki/blob/HEAD/wiki/sources/rag-knowledge-management-roi.md | Secondary (source audit) | Jul 2026 | High (Verified as audit) | — | Demand sample+method+baseline for any ROI claim |
| K5 | Production RAG: 94.7% accuracy vs 67% baseline; $0.0003/query vs $0.08 naive | https://github.com/jhondados/rag-enterprise-pipeline | First-hand builder | 2025 | Medium (Corroborated) | Single deployment | Existence proof of achievable engineering |
| K6 | Gartner Dec 2024: 30% of genAI projects abandoned after PoC by end 2025; retrieval quality is top failure cause | https://www.beehivestrategy.com/blog/articles/rag-retrieval-augmented-generation-knowledge-management | Secondary citing Gartner | 2024 | Medium (Corroborated) | Prediction | Fund retrieval quality, not model upgrades |

## Internal operations (03)

| # | Claim | URL | Source type / author | Pub date | Confidence | Corroboration / contradictions | Engineering implication |
|---|---|---|---|---|---|---|---|
| O1 | Raleigh NC + ServiceNow agentic IT helpdesk; "train them, build trust, verify" rollout | https://www.govtech.com/artificial-intelligence/this-new-raleigh-n-c-it-help-desk-agent-is-well-agentic | Primary press / corroborating | Oct 2026 | High (Verified) | ServiceNow GVP on record | Graduated-trust rollout is the documented-good pattern |
| O2 | 52% of ITSM practitioners: workload INCREASED after AI; 47% validating outputs, 33% handling AI errors | https://itsm.tools/ai-is-helping-itsm-teams-so-why-does-the-work-still-feel-heavier/ | Verified survey | ~Sep 2026 | High (Verified) | Contradicts "AI frees the team" narrative | Price validation/maintenance labour in ROI models |
| O3 | AI-native ops: onboarding 60d→3wk; "less repetitive work, more decision validation" | https://github.com/e-fricke/ai-native-ops-case-study/blob/HEAD/casestudy.md | First-hand builder | 2026 | Medium (Corroborated) | Revenue 4× explicitly not solely AI-attributed | Workload shifts composition; humans stay at decision nodes |
| O4 | UMMS: 80% helpdesk overload reduction; 45min→1.1min turnaround | https://automationedge.com/home-health-care-automation/case-study/reducing-manual-helpdesk-overload-with-automationedges-intelligent-automation/ | Vendor case study (unverified) | 2026 | Low (Unverified) | — | Password resets = canonical automatable workflow |

## Sales & customer success (04)

| # | Claim | URL | Source type / author | Pub date | Confidence | Corroboration / contradictions | Engineering implication |
|---|---|---|---|---|---|---|---|
| S1 | Gong: AI-using orgs +29% sales growth; +11% GTM efficiency; more aggressive hiring plans | https://salestechstar.com/price-optimization-revenue-management/revenue-organizations-using-ai-in-2024-reported-29-percent-higher-sales-growth-than-their-peers-according-to-new-report-from-gong/ | Vendor-commissioned survey (corroborating) | Nov 2024 | Medium (Corroborated) | Self-selection; correlation≠causation | Direction corroborated; magnitudes vendor-framed |
| S2 | Cold-email reply rates 3.43% (2026) vs 8.5% (2019); 344 emails per meeting (28M analysed) | https://www.explainx.ai/blog/jobs-ai-is-killing-outbound-sales-dead-open-closed-ai-dangers-2026 ; https://garijohnson.substack.com/p/the-sdr-was-never-the-problem | Secondary / vendor analysis | 2026 | Medium (Corroborated) | — | AI SDRs flooded the channel; volume strategy dead |
| S3 | Gmail/Outlook bulk-sender caps (5k/day, <0.1% spam) since 2024/2025 | https://garijohnson.substack.com/p/the-sdr-was-never-the-problem | Practitioner citing published policies | Oct 2026 | High (Verified policies) | Google/Microsoft docs | Infrastructure-layer ceiling, not a people problem |
| S4 | AI health scoring with no playbook/training → no first-year ROI; fixed by narrowing to 3 use cases | https://medium.com/@marcopia.remote/profession-customer-success-eradication-by-ai-e21924121f92 | Practitioner essay (community) | Feb 2026 | Medium (Corroborated) | Consistent with MIT Sloan augmentation finding | Every score ships with owner + playbook + training |
| S5 | LatentView: +15% churn performance, ~$100M retention value (data-backup leader) | https://www.latentview.com/blog/churn-prediction-for-marketing-retention-campaigns/ | Consultancy case study (unverified) | 2026 | Low (Unverified) | — | Embed scores in workflows, not dashboards |

## Analytics & reporting (05)

| # | Claim | URL | Source type / author | Pub date | Confidence | Corroboration / contradictions | Engineering implication |
|---|---|---|---|---|---|---|---|
| A1 | Spider 2.0: NL→SQL ~59% exact match peak, ~40% with complexity on enterprise schemas | https://www.infoworld.com/article/4040909/why-ai-fails-at-business-context-and-what-to-do-about-it.html | Secondary press | ~Aug 2025 | Medium (Corroborated) | Benchmark, not field study | Budget the "almost-right tax" on messy schemas |
| A2 | Looker Conversational Analytics grounded in semantic model "source of truth" | https://www.buildberg.co/blog/ai-business-intelligence | Secondary analysis of product docs | Sep 2026 | High (Corroborated) | Google docs | No semantic layer → the NL interface guesses |
| A3 | Gartner: 50% of orgs adopt zero-trust data governance by 2028 over unverified AI data | https://www.buildberg.co/blog/ai-business-intelligence | Secondary citing Gartner | 2026 | Medium (Corroborated) | Prediction | Label AI-generated figures; verify before trust |
| A4 | Skeptic-agent + reflection-agent oversight pattern (16-node pipeline) | https://github.com/rakshitkaintura/data_analytics_automation | First-hand builder | 2026 | Medium (Corroborated) | Single implementation | Adversarial review + failure-distillation as design pattern |

## Administrative processes (06)

| # | Claim | URL | Source type / author | Pub date | Confidence | Corroboration / contradictions | Engineering implication |
|---|---|---|---|---|---|---|---|
| D1 | Unaautomated baseline: $12.88 and 17.4 days per invoice | https://supalabs.co/en/blog/ai-document-invoice-processing-case-study-93-percent-faster-abbyy-basware-2025/ | Secondary citing Ardent Partners 2024 | 2025 | High (Verified) | Industry standard figure | The anchor for every AP business case |
| D2 | Certas Energy: 30 min → ~1 min/invoice (ABBYY + Blue Prism) | https://supalabs.co/en/blog/ai-document-invoice-processing-case-study-93-percent-faster-abbyy-basware-2025/ | Vendor-published (corroborating) | 2025 | Medium (Corroborated) | — | IDP works on standardised flows |
| D3 | Greek insurer: claims 14 days → ~1 min; 1,500/day; every-case review catches sampled-missed fraud | https://www.indexbox.io/blog/ai-cuts-insurance-claim-processing-from-14-days-to-one-minute-in-greece/ | Press (corroborating) | Oct 2026 | High (Corroborated) | — | Automation can change the assurance model |
| D4 | RPA: ~30% projects abandoned in 12 months; 30–50% budget on maintenance; one hyphen broke a pipeline | http://coasty.ai/blog/why-most-enterprise-rpa-projects-stall-after-the-pilot ; https://medium.com/@rmccain/your-rpa-bots-keep-breaking-heres-why-9781542ae77a | Practitioner (community) | 2026 | Medium (Corroborated) | Direction consistent across sources | Standardise process before automating; prefer IDP over UI-RPA |
| D5 | Undocumented exceptions are the real failure: "automation just made it move faster" | https://www.iteratorshq.com/blog/shared-services-automation-mistakes/ | Practitioner taxonomy | Sep 2026 | Medium (Corroborated) | — | Map the mess before picking the tool |

## Engineering coordination (07)

| # | Claim | URL | Source type / author | Pub date | Confidence | Corroboration / contradictions | Engineering implication |
|---|---|---|---|---|---|---|---|
| E1 | AI triage vs alerting: dynamic severity, root-cause clustering, ownership-aware routing with evidence | https://incident.io/blog/what-is-ai-incident-triage | Vendor docs (corroborating) | 2026 | Medium (Corroborated) | Architecture, not measured outcomes | Keep detection; add interpretation layer |
| E2 | Triage coordinator discipline: 4 questions, human verification before accepting route, revision history | https://dev.to/gateofai/incident-triage-agent-architecture-guide-2n1i | Practitioner guide | Oct 2026 | Medium (Corroborated) | — | Propose-don't-page; log every revision |
| E3 | Read-only-by-default incident agents; mechanical enforcement even if prompt bypassed | https://github.com/ambitioussam/eng-agent-os/blob/HEAD/docs/INCIDENT-RESPONSE.md | First-hand builder | 2026 | Medium (Corroborated) | — | Enforce least privilege in credentials, not just prompts |
| E4 | 30–40% MTTR improvement claims | https://dev.to/sip_mjb/ai-powered-incident-resolution-assistant-reducing-mttr-and-elevating-servicenon-operations-9 | Secondary/vendor | 2025 | Low (Unverified) | No independent audit | Area is widely described, rarely measured |

## Business workflows (08)

| # | Claim | URL | Source type / author | Pub date | Confidence | Corroboration / contradictions | Engineering implication |
|---|---|---|---|---|---|---|---|
| W1 | HR agent bypassed approval, accessed 500 employee profiles via unexpected instruction path | https://hrtechedge.com/ai-in-hr/from-hrtech-to-the-soc-building-a-cross-functional-ai-risk-response-team/ | Practitioner (community) | Sep 2026 | Medium (Corroborated) | Matches confused-deputy pattern | Approval controls tested across systems, not assumed |
| W2 | "Slightly wrong decision made 600 times before anyone sees the pattern" — speed-at-scale risk | https://www.inc.com/hillary-remy/ai-agent-mistake-startup-founders-openai-risk/91414970 | Practitioner reporting | Oct 2026 | Medium (Corroborated) | — | Day-one access must be re-scoped; monitor aggregates |
| W3 | Production reliability checklist: output validation, guardrails, iteration caps, 1-minute failure alerting | https://dev.to/payload-tools/why-your-n8n-ai-agent-workflows-fail-in-production-and-how-to-fix-them-pi8 | Practitioner guide | Oct 2026 | Medium (Corroborated) | — | "Bounded, visible, handled" as the production bar |
| W4 | Rollback plans must cover "succeeded at the wrong task," not just failed runs | https://corranforcedesigns.blog/2026/09/30/ai-agent-rollback-plan/ | Practitioner guide | Sep 2026 | Medium (Proposed→Corroborated) | — | One-page abort plan per agent; stop drills |

## Cross-cutting

| # | Claim | URL | Source type / author | Pub date | Confidence | Notes |
|---|---|---|---|---|---|---|
| X1 | Gartner: 40%+ agentic AI projects cancelled by end 2027 (cost, unclear value, risk controls) | https://aissist.io/insights/ai-hallucinations-customer-service | Secondary citing Gartner | 2026 | Medium (Corroborated) | Prediction; consistent with rollback survey data |
| X2 | Companies using AI to *assist* agents see 36% higher CSAT than full-automation shops | https://www.allaboutai.com/resources/ai-statistics/customer-service/ | Secondary aggregation | 2025 | Low (Unverified) | Direction matches Klarna lesson; number unsourced |
| X3 | OWASP AISVS: retrieve-then-filter leaks via counts/scores/latency; authorisation per expansion | https://github.com/owasp/aisvs/blob/HEAD/1.0/research/chapters/C08-Memory-and-Embeddings/C08-01-Access-Controls-M87-01-Access-Controls-Memory-RAG.md | Standards-track (primary technical) | 2025 | High (Corroborated) | Design control for all RAG/agent retrieval |

*Note: X3's URL is reproduced verbatim from the search-tool result (OWASP AISVS, C08 Memory-and-Embeddings, C08-01 Access Controls chapter on GitHub).*
