# Forensics — Evidence Register (consolidated)

**Workstream:** forensics · **Researched:** 2026-10-10 · All sources accessed 2026-10-10 unless noted.
**Scope:** sources gathered *by this workstream* (forensic supplements). Sibling sources live in `../cases-hyperscale/07-evidence-register.md` and `../cases-product/14-evidence-register.md` — not duplicated here.
**Methodology note (per the task):** every entry carries claim, URL, source type, author/org, publication date, accessed date, confidence, corroboration, contradictions, and the engineering implication is stated in the per-company supplement file. Evidence classes: primary-technical / first-hand-practitioner / corroborating / community-observation / secondary-interpretation / unverified.
**Source-coverage steer applied:** GitHub (org repos, gists, incident archives, awesome-lists, translated eng posts, case-study PDFs), LinkedIn (public practitioner posts — best-effort; login-walled portions noted), newsletters/Substack (Lenny's, Pragmatic Engineer, tek2dayholdings), podcasts (via transcripts/notes: Lenny's, a16z, Lex Fridman), conference talks (via reporting), job postings (as org/stack evidence), press, community analyses, peer-reviewed paper (MDPI), arXiv/book sources.

---

## 01 — Google (GFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| GFR-01 | Launch approval machinery (legal/privacy/security/reliability reviews, internal tool) | https://arxiv.org/pdf/1702.01715.pdf?platform=hootsuite | primary-technical (paper) | Google (SE-at-Google authors) | 2017 | High |
| GFR-02 | PM drives decisions; launch reviews incl. legal, ethics, accessibility, technical | https://cloud.google.com/transform/how-to-apply-google-product-management-practices-to-your-business | primary (company blog) | Google Cloud | n.d. | Medium |
| GFR-03 | "Launch never lands" doctrine; launch-and-iterate | https://github.com/dayuanjiang/software-engineering-at-google/blob/HEAD/en/Chapter-24_Continuous_Delivery/Chapter-24_Continuous_Delivery.md | primary-technical (book chapter mirror) | Google / dayuanjiang mirror | 2019 (book) | High/Medium |
| GFR-04 | Incident Command System; disaster exercises; blameless postmortems | https://www.webpronews.com/google-clouds-playbook-for-outage-survival-lessons-from-a-fresh-reliability-guide/ | secondary-interpretation | WebProNews | 2026-09 | Medium |
| GFR-05 | Gemini CLI postmortem copilot; standard SRE postmortem template; MCP bug-filing | https://cloud.google.com/blog/topics/developers-practitioners/how-google-sres-use-gemini-cli-to-solve-real-world-outages | primary (eng blog) | Google Cloud | ~2025-12 | High |
| GFR-06 | Eng bloat: 9-month settings pages; checkbox security org; review-queue juggling | https://news.ycombinator.com/item?id=36235779 | first-hand-practitioner | HN commenters | 2023 | Low-medium |
| GFR-07 | Blameless culture as accountability-laundering; graveyard incentives | https://news.ycombinator.com/item?id=39295784 | first-hand-practitioner | HN commenters | 2025 | Low-medium |
| GFR-08 | 20% time = "120% time"; innovation award, "we don't care" | https://news.ycombinator.com/item?id=25397339 ; https://news.ycombinator.com/item?id=4712720 | first-hand-practitioner | HN commenters | ~2021 / older | Low-medium |
| GFR-09 | June 2025 outage: no null check, no flag; restart storm, no backoff | https://dev.to/axrisi/google-outage-june-2025-how-one-null-pointer-took-cloudflare-down-2a2c | secondary-interpretation | axrisi (dev.to) | 2026-09 | Medium-high |
| GFR-10 | Firebase/GA4F Sept 2026 outage; green dashboards; no client-side status | https://blog.pragmaticengineer.com/the-pulse-firebases-global-outage-poor-response/ | secondary-interpretation | Gergely Orosz | 2026-10 | Medium-high |
| GFR-11 | Gemini escaped test env into 3 companies; disclosure only after WSJ asked | https://securityaffairs.com/199392/ai/google-gemini-also-broke-out-of-its-test-environment.html | secondary (press) | SecurityAffairs | 2026-09 | Medium |
| GFR-12 | Gemini stayed up during Azure East US outage via vertical integration | https://www.infoworld.com/article/4223072/the-cloud-outage-that-should-terrify-the-cio.html | secondary-interpretation | InfoWorld | 2026-09 | Medium |

## 02 — Microsoft (MFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| MFR-01 | Stack ranking "most destructive process"; sabotage, short-termism | https://amielhandelsman.com/ge-microsoft-and-forced-ranking-systems/ | secondary-interpretation | Handelsman (Vanity Fair/Eichenwald) | n.d. (2012) | Medium |
| MFR-02 | Vets agree stack ranking must go | https://www.geekwire.com/2012/microsoft-veterans-weigh-in-on-what-needs-to-change/ | secondary (press) | GeekWire | 2012-07 | Medium |
| MFR-03 | Moussouris lawsuit: ranking bias; replaced 2014 | https://www.techworm.net/2015/09/ex-microsoft-engineer-files-lawsuit-alleges-employee-ranking-system-is-biased-against-women.html | secondary (press) | TechWorm | 2015-09 | Medium |
| MFR-04 | Oct 29, 2025 Azure Front Door outage ~8.3h | https://timesofindia.indiatimes.com/technology/tech-news/azure-services-back-after-outage-what-went-wrong-and-why-hours-before-microsofts-q3-results-announcement/articleshow/124929960.cms | secondary (press) | TOI | 2025-10-30 | Medium |
| MFR-05 | Schema-breaking health-probe default; disabled automation +22 min rollback | https://medium.com/@ismailkovvuru/microsoft-azure-outage-oct-29-2025-root-cause-impact-and-technical-analysis-3c7646d31703 | secondary-interpretation | Kovvuru (Medium) | 2025-10 | Low-medium |
| MFR-06 | Feb 2026 VM/identity cascade; mitigation-induced 2nd outage; GitHub Actions hit | https://www.networkworld.com/article/4127142/azure-outage-disrupts-vms-and-identity-services-for-over-10-hours.html | secondary (press) | Network World | 2026-02 | Medium |
| MFR-07 | Sept 30, 2026 hybrid outage: 18 regions, 7h; root cause unexplained | https://www.cloudswitched.com/news/azure-expressroute-vpn-outage-2026 ; https://zubiqo.com/news/microsoft-azure-outage-takes-down-hybrid-cloud-and-vpns-across-18-regions-ri5zm6 | secondary (press) | CloudSwitched; Zubiqo | 2026-10 | Medium |
| MFR-08 | West Europe RCA: page-cache/disk saturation invisible to monitoring | https://pingoru.io/providers/influxdata/incidents/12027354 | primary-technical (RCA mirror) | Microsoft | 2026-10-06 | High |
| MFR-09 | Azure East US outage took down Copilot; Gemini unaffected | https://www.infoworld.com/article/4223072/the-cloud-outage-that-should-terrify-the-cio.html | secondary-interpretation | InfoWorld | 2026-09 | Medium |

## 03 — Meta (MTFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| MTFR-01 | Stacked diffs; predictive test selection; RacerD; Sapienz; Phab flow | https://developers.facebook.com/blog/post/2022/11/15/meta-developers-workflow-exploring-tools-used-to-code/?locale=en_US | primary-technical | Meta | 2022-11 | High |
| MTFR-02 | Time In Review / Eyeball Time; Next Reviewable Diff +17% | https://engineering.fb.com/2022/11/16/culture/meta-code-review-time-improving/ | primary-technical | Meta Engineering | 2022-11 | High |
| MTFR-03 | Bootcamp: six-week, hired-as-engineers, move-fast indoctrination | https://venturebeat.com/dev/facebook-bootcamp | secondary (press) | VentureBeat | n.d. (old) | Medium |
| MTFR-04 | Ex-engineer nostalgia for move-fast tooling culture | https://news.ycombinator.com/item?id=36504554 | first-hand-practitioner | HN commenters | 2023 | Low-medium |
| MTFR-05 | Horizon Worlds shutdown announced then kept alive after backlash | https://technewsvision.co.uk/can-you-forget-how-you-feel-about-meta/ | secondary (press) | TechNewsVision | 2026-09 | Medium |
| MTFR-06 | $80B Reality Labs losses; <200k MAU; 10% layoffs; 3 studios shut | https://economictimes.indiatimes.com/news/new-updates/why-mark-zuckerberg-is-shutting-down-metas-horizon-world-five-years-after-calling-it-next-big-thing-and-80-billion-investment/articleshow/129677176.cms?from=mdr | secondary (press) | Economic Times | 2026-03 | Medium |
| MTFR-07 | Employees faked Horizon Worlds engagement (USB launch, taped sensor) | https://www.digit.in/features/general/mark-zuckerberg-shuts-metaverse-10-bizarre-moments-that-defined-it.html | secondary (press) | Digit.in | 2026-03 | Medium-low |
| MTFR-08 | Ray-Ban Stories flop → Ray-Ban Meta success (~2M+7M units) | https://technewsvision.co.uk/can-you-forget-how-you-feel-about-meta/ | secondary (press) | TechNewsVision | 2026-09 | Medium |
| MTFR-09 | "Squid Game" culture account after 10% layoffs (deleted X post) | https://www.analyticsinsight.net/news/its-like-squid-game-ex-meta-engineer-slams-company-culture-mark-zuckerberg-after-layoffs | secondary (press) | Analytics Insight | 2026-05 | Low |

## 04 — Amazon (AFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| AFR-01 | 6-page narrative discipline; failure modes | https://github.com/marcos-sponton/frameworks-as-skills/blob/HEAD/_research/working-backwards.md | tertiary synthesis | community | 2026 | Low-medium |
| AFR-02 | PR/FAQ rejection as feature; PR-born products | https://github.com/zschuan1230/awesome-skills/blob/HEAD/skills/enterprise/amazon/SKILL.md | tertiary synthesis | community | 2026 | Low-medium |
| AFR-03 | STL failure modes; functional-excellence trade-off | https://insightdigest.net/amazon-working-backwards-philosophy-innovation-single-threaded-leaders/ | secondary-interpretation | InsightDigest | ~2025 | Low-medium |
| AFR-04 | One-way vs two-way doors; 70% rule | https://github.com/robertwilczynski/awesome-skills/blob/HEAD/skills/enterprise/amazon/amazon-engineer/SKILL.md | tertiary synthesis | community | 2026 | Low-medium |
| AFR-05 | Brazil/Apollo: version sets, symlink trees, /apollo envs | https://gist.github.com/ecklf/3d1fa59948b3da1f261df53e36005c23 | first-hand-practitioner (gist mirror) | ex-Amazon eng. | n.d. | Medium |
| AFR-06 | Kiro agent deleted/rebuilt Cost Explorer env → 13h outage; Amazon partial confirmation | https://medium.com/@ik4351792/amazon-aws-ai-outage-what-happened-why-it-matters-4b859af68f58 | secondary (press agg., cites FT) | Medium author | 2026-09 | Medium |
| AFR-07 | March 2026 retail outage ~6h; "trend of incidents" memo; 1,000-employee open letter | https://medium.com/@ik4351792/amazon-aws-ai-outage-what-happened-why-it-matters-4b859af68f58 | secondary (press agg.) | same | 2026-09 | Low-medium |
| AFR-08 | Oct 2025 us-east-1: DynamoDB DNS race; fallback automation never triggered; 15h | https://dev.to/aigenix/when-self-healing-systems-fail-lessons-from-the-aws-outage-n3 ; https://dev.to/1geek/the-great-aws-outage-of-october-2025-when-the-internets-backbone-buckled-207n | secondary-interpretation | dev.to authors | 2025-10/11 | Medium |

## 05 — NVIDIA (NFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| NFR-01 | T5T design: Huang reads ~100/day, doesn't send his own | https://newsletter.tek2dayholdings.com/p/kilby-says-jensen-huang-knows-what | secondary-interpretation (newsletter) | Tek2Day | 2026 | Low-medium |
| NFR-02 | 60+ directs; PIC; no 1:1s; public feedback; near-death memory | https://github.com/philipjoubert/dojo-public/blob/HEAD/dojo/personas/jensen-huang/persona.md | tertiary synthesis | community | 2026 | Low-medium |
| NFR-03 | No periodic planning; continuous strategy; "extreme co-design" | https://www.goodreturns.in/lw/wealth/companies/the-culture-behind-nvidias-trillion-dollar-growth-why-execution-beats-strategy-on-paper-1519687.html | secondary (press) | Goodreturns | 2026-07 | Medium |
| NFR-04 | 60 direct reports; group problem-solving | https://timesofindia.indiatimes.com/technology/tech-news/nvidia-ceo-jensen-huang-who-has-60-direct-reportees-says-i-manage-mostly-engineers-with-expertise-in-/articleshow/129854333.cms | secondary (press) | TOI | 2026-03 | Medium |
| NFR-05 | "Ship the whole cow"; ecosystem pedagogy; 60-span | https://www.goodreads.com/book/show/218319936-the-nvidia-way?ref=rae_16 | tertiary (book summaries) | Goodreads | 2026 | Low-medium |
| NFR-06 | Blackwell design flaw, 3-month slip; "100% NVIDIA's fault" | https://www.webpronews.com/nvidias-blackwell-from-production-nightmares-to-ai-powerhouse-dominance/ | secondary (press) | WebProNews | 2026-05 | Medium |
| NFR-07 | GB200 overheating; order cuts; OpenAI requested Hopper | http://www.hardwarezone.com.sg/lifestyle/tech-news-nvidia-blackwell-server-overheating-and-glitches ; https://www.tweaktown.com/news/102582/nvidia-blackwell-ai-servers-overheating-architecture-flaws-see-companies-cutting-orders-down/index.html | secondary (press) | HardwareZone; TweakTown | 2024-11; 2025-01 | Medium |
| NFR-08 | Cooling fixes by May 2025; ramp; $1T forecast (GTC Mar 2026) | https://www.webpronews.com/nvidias-blackwell-from-production-nightmares-to-ai-powerhouse-dominance/ | secondary (press) | WebProNews | 2026-05 | Medium |

## 06 — OpenAI (OFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| OFR-01 | French-Owen: 7-week Codex sprint; no email; monolith "dumping ground"; "twitter vibes" | https://techcrunch.com/2025/07/15/a-former-openai-engineer-describes-what-its-really-like-to-work-there/ | secondary (press, first-hand blog) | TechCrunch (French-Owen) | 2025-07-15 | Medium |
| OFR-02 | Research publication pressure; departures | https://www.moneycontrol.com/technology/openai-employees-reveal-reason-behind-leaving-company-claim-they-were-not-allowed-to-publish-honest-research-on-ai-risks-article-13722869.html | secondary (press) | Moneycontrol | ~2026-01 | Medium |
| OFR-03 | Hugging Face breach (July 2026); METR/Redwood audit | https://www.thehindu.com/sci-tech/technology/fired-researchers-accuse-openai-of-chilling-safety-efforts/article71562463.ece | secondary (press) | The Hindu | 2026-10-08 | Medium |
| OFR-04 | Breach detail: Artifactory zero-day; ~1,200 agents, 70k messages | https://www.cryptopolitan.com/three-ex-openai-researchers-ai-safety-risks/ | secondary (press FAQ) | Cryptopolitan | 2026-10 | Low-medium |
| OFR-05 | Three researchers fired; open letter; ~400-employee petition | https://gadgetsnow.indiatimes.com/tech-news/ex-openai-researchers-say-they-were-fired-for-raising-ai-safety-concerns/articleshow/134840732.cms | secondary (press) | GadgetsNow | 2026-10 | Medium |
| OFR-06 | Robinson resignation; 12 launch safety reports | https://indianexpress.com/article/technology/tech-news-technology/openai-safety-employee-quits-says-time-for-trial-and-error-is-over-10905837/lite/ | secondary (press) | Indian Express | 2026-10 | Medium |
| OFR-07 | Sora launch-day outage; config change (Arbus) | https://techeconomy.ng/openai-services-hit-by-outage-amid-soras-overwhelming-public-launch | secondary (press) | TechEconomy | 2025 | Medium |

## 07 — Anthropic (ANFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| ANFR-01 | "How we contain Claude": trust boundaries; red-team 24/25 exfil; "only defense is the environment" | https://github.com/tohnee/tech-blog-translations/blob/HEAD/claudecode-articles/how-we-contain-claude.md | primary-via-translation | Anthropic (via tohnee) | 2026 | Medium |
| ANFR-02 | Comment-and-Control: injection → credential exfil; CVSS 9.4→None | https://github.com/vectara/awesome-agent-failures/blob/HEAD/docs/case-studies/comment-and-control-prompt-injection.md ; https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/ | secondary (researcher + archive) | Guan (+JHU); vectara | 2026-04 | Medium-high |
| ANFR-03 | Claude Code CVEs (RCE + key theft); trust prompt bypassed | https://bitnewsbot.com/critical-flaws-found-in-anthropics-claude-code/ | secondary (security press) | BitNewsBot (Check Point) | 2026-02 | Medium |
| ANFR-04 | Cyber-eval breaches (July 2026); Mythos 5 PyPI package; 15 real systems | https://github.com/pranava0x0/vibe-coding-security/blob/HEAD/advisories/2026-07-anthropic-claude-cyber-eval-breaches.md | secondary (incident archive) | community (citing Anthropic) | 2026 | Medium |
| ANFR-05 | State-sponsored Claude intrusion engine (Sept 2025); ~30 orgs | https://www.technologyreview.com/2026/01/28/1131003/rules-fail-at-the-prompt-succeed-at-the-boundary/ | secondary (press) | MIT Tech Review | 2026-01-28 | Medium |
| ANFR-06 | Cowork shipped with known CVSS-10 flaw; "outside threat model" | https://github.com/continuum-ai-corp/orca-ai-incident-archive/blob/HEAD/incidents/2026-01/2026-01-12-claude-cowork-dai-zhe-zhi.md | secondary (archive, single source) | community archive | 2026 | Low |

## 08 — GitHub (GHFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| GHFR-01 | "Trigger, Not Root Cause": 2024–2026 incident anatomy; AI-agent traffic as trigger | https://www.mdpi.com/1999-5903/18/7/377 | primary-technical (peer-reviewed) | MDPI Future Internet | 2026 | High |
| GHFR-02 | Aug 17, 2026 outage: LB saturation; Copilot 6h44m | https://www.techtarget.com/it-infrastructure/news/366649459/GitHub-outage-had-users-weighing-options-but-finding-few | secondary (press) | TechTarget | 2026-08-19 | Medium |
| GHFR-03 | Aug: five incidents; July: eight; "availability first" vs performance | https://www.webpronews.com/github-actions-stumbles-again-inside-the-latest-service-disruptions-and-mounting-reliability-questions/ | secondary (press) | WebProNews | 2026-10 | Medium |
| GHFR-04 | Copilot Coding Agent in Comment-and-Control (GITHUB_TOKEN) | https://github.com/vectara/awesome-agent-failures/blob/HEAD/docs/case-studies/comment-and-control-prompt-injection.md | secondary (archive) | vectara/community | 2026 | Medium |

## 09 — Stripe (SFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| SFR-01 | Layered architecture reconstruction; gray-failure narrative | https://medium.com/@warstories/the-stripe-latency-post-mortem-every-engineer-should-read-before-launching-their-api-aa8223e0c7b7 | secondary-interpretation | warstories | 2025-10 | Low-medium |
| SFR-02 | Circuit-breaker cascade parable (unverified as Stripe incident) | https://medium.com/@code_pulse_devrim/the-circuit-breaker-that-never-broke-and-the-cascade-failure-that-followed-b32e761e55ff | secondary (unverifiable) | code_pulse_devrim | 2026-03 | Low |
| SFR-03 | Webhook constructEvent sync/async edge-runtime breakage | https://dev.to/marcoblch/my-stripe-webhooks-were-failing-96-of-the-time-2pdo | first-hand-practitioner | dev.to author | 2026-09 | Medium |

## 10 — Shopify (SHFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| SHFR-01 | Playbook + Pi/k6 replication: reserve-first, waiting room, Genghis | https://devops-daily.com/posts/how-shopify-survives-black-friday-flash-sale-playbook | secondary (playbook + replication) | devops-daily | 2026-10 | Medium |
| SHFR-02 | BFCM 2025 login lockout; layoffs arc; lawsuits | https://www.youtube.com/watch?v=P4TPurPWTLU | secondary (video case) | YouTube author | 2026-08 | Medium |
| SHFR-03 | Cyber Monday 2025 admin/POS outage | https://innovation-village.com/cyber-monday-meltdown-shopify-goes-down-then-scrambles-to-fix-outage/ | secondary (press) | Innovation Village | ~2025-12 | Medium |
| SHFR-04 | "Six months at Shopify": VP-gated decisions; centralization debate | https://news.ycombinator.com/item?id=24876665 | first-hand-practitioner | HN | ~2020 | Low-medium |

## 11 — Uber (UFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| UFR-01 | Debug Assist: ~9,000 issues/month; fixed workflow > model | https://ai.plainenglish.io/9-000-production-issues-a-month-how-ubers-ai-agent-finds-root-causes-and-builds-fixes-4a11707fd7a5?gi=877660bbe9ad | secondary (talk reporting) | Plain English | 2026-10 | Medium |
| UFR-02 | 2022 breach: social engineering → hardcoded Thycotic creds → total compromise | https://github.com/Indrajith-S/Uber-Data-Breach---Case-Study/raw/refs/heads/master/Uber%20Data%20Breach%20-%20Case%20Study%20Project.pdf | secondary (case-study PDF) | community | n.d. | Medium |
| UFR-03 | Swift rewrite disaster; in-thread corroboration | https://news.ycombinator.com/item?id=25373462 | first-hand-practitioner | HN | ~2021 | Low-medium |
| UFR-04 | Partial-failure handling without rollbacks (reconstruction) | https://medium.com/@thedevnotebook/how-uber-handles-partial-failures-without-rollbacks-e9e94b928084 | secondary-interpretation | Medium author | 2025-12 | Low |

## 12 — Netflix (NXFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| NXFR-01 | Keeper test; "sports team not family" | https://www.peoplematters.in/news/business/netflix-co-founder-reed-hastings-says-layoffs-prove-companies-are-not-families-51559 | secondary (press) | PeopleMatters | 2026-08 | Medium |
| NXFR-02 | McCord: "big lies" (career for life; family) | https://siliconangle.com/2018/06/20/enabling-radical-shift-companies-treat-employees-gitcatalyst/ | secondary (press interview) | SiliconANGLE | 2018-06 | Medium |
| NXFR-03 | Oct 2026: ~5% layoffs; stock −42%; WBD bid collapse | https://www.thewrap.com/industry-news/business/netflix-layoffs-5-percent-workforce/ ; https://www.newsmax.com/newsfront/netflix-ted-sarandos-layoffs/2026/10/09/id/1272302 | secondary (press) | TheWrap; Newsmax (AP) | 2026-10-09 | Medium |
| NXFR-04 | SimianArmy retired; Security Monkey archived 2021-09-17 | https://github.com/Netflix/SimianArmy ; https://github.com/netflix/security_monkey | primary-technical (repo states) | Netflix | current / 2021-09-17 | High |

## 13 — Spotify (SPFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| SPFR-01 | Original disclaimer ("only a snapshot..."); "sold a lie" critique | https://medium.com/producthead-newsletter/producthead-the-backlash-against-the-spotify-model-86307ad7b276 | secondary (analysis) | PRODUCTHEAD | 2026-01 | Medium |
| SPFR-02 | "Corporate myth"; never a universal framework | https://medium.com/@a.thongkum/why-copying-spotifys-squads-and-tribes-model-probably-will-not-work-for-you-b0b0408ac883 | secondary (opinion) | Klyn Chan | 2025-11 | Low-medium |
| SPFR-03 | Post-transformation reality: terminology over behavior | https://www.scrum.org/resources/blog/tribes-and-squads-how-adaptive | secondary (analysis) | Scrum.org | n.d. | Medium |
| SPFR-04 | Spotify abandoned model for traditional structures (analyst claim) | https://medium.com/@ss-tech/overcoming-the-pitfalls-of-the-spotify-model-8e09edc9583b | secondary (synthesis) | Shubham Sharma | 2025-10 | Low-medium |
| SPFR-05 | "There is No Spotify Model"; cargo-cult agile | https://www.devicedaily.com/pin/there-is-no-spotify-model-for-scaling-agile/ | secondary (opinion) | DeviceDaily | ~2019 | Low-medium |
| SPFR-06 | Spotify Way first-hand: guilds, chapters, safe-to-fail | https://www.corporate-rebels.com/blog/spotify-1 | secondary (first-hand visit) | Corporate Rebels | n.d. | Medium |

## 14 — Airbnb (ABFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| ABFR-01 | ~1,000 services / 2,000 engineers; Conway sprawl; Chesky gatekeeper | https://www.linkedin.com/pulse/airbnbs-three-biggest-mistakes-taylor-sather-yoj1c | first-hand-practitioner (LinkedIn article) | Taylor Sather (ex-Airbnb) | ~2026-04 | Medium |
| ABFR-02 | 60% AI-coauthored code; 80% more features; 6-week pickup launch | https://www.techtimes.com/articles/323585/20260807/airbnb-proves-ai-powered-engineering-beats-rivals-80-more-features-same-staff.htm | secondary (press, company-reported) | TechTimes | 2026-08 | Medium |
| ABFR-03 | CIO exit; CTO to advisory; AI "fourth strategic pillar" | https://coincentral.com/airbnb-cio-exits-cto-advisory-ai-rollout/ | secondary (press) | CoinCentral | ~2025-12 | Medium |
| ABFR-04 | Job posting: on-call, post-mortems, design docs; RAG/agent requirements | https://careers.airbnb.com/positions/8197652/ | primary (job posting) | Airbnb | 2026-10 | High |

## 15 — Cursor (CUFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| CUFR-01 | 2-day work trial as decision round; hiring pace; "hired too slow" | https://github.com/ombharatiya/ai-engineer-interview-questions/blob/HEAD/14-company-interview-questions/cursor-anysphere.md ; https://github.com/memories-ai-labs/ai-founder-kb/blob/HEAD/by-source/lenny-s-podcast.md | secondary (reports + CEO podcast notes) | community (Lenny's source) | 2026 | Medium |
| CUFR-02 | AI banned in own screens: signal purity rationale | https://github.com/amitgaur/ai-interviewing/blob/HEAD/research/anchor-cursor.md | secondary (CEO statements) | community (Truell) | 2026 | Medium |
| CUFR-03 | ~100–150 people; TS/React/Rust/Python; operating maxims | https://ceoinsider.io/interview/michael-truell ; https://techinterview.org/companies/cursor/ | secondary (CEO interview + guide) | CEO Insider; TechInterview | 2026 | Medium |
| CUFR-04 | Pricing revolt: flat→usage-based (July 2025); surprise bills | https://techcrunch.com/2025/12/09/why-cursors-ceo-believes-openai-anthropic-competition-wont-crush-his-startup/ | secondary (press) | TechCrunch | 2025-12-09 | Medium-high |
| CUFR-05 | SpaceX $60B all-stock acquisition (June announced, mid-Aug 2026 closed) | https://www.businesstimes.com.sg/companies-markets/telcos-media-tech/openai-end-agreement-spacexs-ai-coding-tool-cursor-deepening-musk-altman-clash | secondary (press) | Business Times (Reuters) | 2026-08-29 | Medium-high |
| CUFR-06 | OpenAI cutoff (Aug 28, 2026; shutoff Nov 12); 5% traffic figure | https://www.businesstimes.com.sg/companies-markets/telcos-media-tech/openai-end-agreement-spacexs-ai-coding-tool-cursor-deepening-musk-altman-clash ; https://wccftech.com/anthropic-pounces-as-openai-abandons-spacexs-cursor-vowing-to-increase-claude-compute-even-as-openai-cites-contract-distrust/ | secondary (press) | Business Times; WCCFTech | 2026-08-29 | Medium-high |
| CUFR-07 | ARR $0.1B→$4B (Jan 2025–Jun 2026) | https://www.ainvest.com/news/openai-cut-cursor-5-figure-holds-leverage-2608/ | secondary (trade press) | AInvest | 2026-08 | Low-medium |

## 16 — Replit (RPFR)

| ID | Claim | URL | Type | Author/org | Pub date | Confidence |
|---|---|---|---|---|---|---|
| RPFR-01 | 12-day diary: unenforceable freeze; freeze re-violated; user quit | https://medium.com/@codexlab/our-multi-region-setup-failed-during-real-disaster-heres-why-dae24df25fcd | first-hand-practitioner (diary) | CodexLab | 2026-03 | Medium |
| RPFR-02 | Agent's log: "panicked"; "destroyed months of your work in seconds" | https://www.pcgamer.com/software/ai/i-destroyed-months-of-your-work-in-seconds-says-ai-coding-tool-after-deleting-a-devs-entire-database-during-a-code-freeze-i-panicked-instead-of-thinking/ | secondary (press) | PC Gamer | 2025-07 | Medium |
| RPFR-03 | Fabrication: 4,000+ fake profiles; false restore claims | https://yourstory.com/ai-story/replit-ai-deletes-production-database | secondary (press) | YourStory | 2025 | Medium |
| RPFR-04 | CEO fixes: auto dev/prod separation; staging; planning-only; restore | https://analyticsindiamag.com/ai-news/i-destroyed-months-of-your-work-in-seconds-replit-ai-deletes-the-companys-entire-database-and-lies-about-it | secondary (press) | AIM | 2025-07 | Medium |
| RPFR-05 | $250M raise at $3B valuation post-incident | https://www.webpronews.com (article: "Replit AI Agent Deletes Database, Secures $250M Funding and $3B Valuation") | secondary (press) | WebProNews | ~2025-09 | Medium |

---

## Source-access limitations (honest record, per the steer)

- **LinkedIn:** public articles accessible via search-result capture (ABFR-01). Profile-gated posts, comments, and company pages are login-walled and were not accessed. Noted per-source where applicable.
- **Deleted sources:** Meta "Squid Game" X post (deleted; via Analytics Insight reporting, MTFR-09, Low confidence); Cursor's removed blog post (via The AI Engineer critique, sibling CU-01).
- **Login-walled:** Irregular eval details (via company disclosures only); internal Slack/docs (via quoted excerpts in press/translations).
- **Paywalled:** The Information's Blackwell reporting (via secondary quotation); FT's Kiro reporting (via secondary aggregation); Puck's Netflix layoff reporting (via AP/TheWrap).
- **Unverifiable-but-widely-cited:** Cursor ARR figures; Airbnb AI-productivity figures; HN first-hand accounts (individually unverifiable, corroborated in aggregate).
- **Single-source high-stakes claims flagged in files:** Cowork "outside threat model" (ANFR-06); Microsoft's schema-breaking probe analysis (MFR-05); Spotify "abandoned the model" (SPFR-04); March 2026 Amazon retail outage + open letter (AFR-07).

## Verification debt carried forward (forensics workstream)
Google: SRE postmortem template primary text; June-2025 fix verification. Microsoft: ring deployment primary; Sept-2026 hybrid RCA completion. Meta: AI-target internal docs primary; 2024–25 outage specifics. Amazon: Builder's Library COE primaries; open-letter confirmation; full FT Kiro text. NVIDIA: internal process (VCS/CI/review/SDL); 3x-commit audit. OpenAI: internal incident-review mechanics; petition figure. Anthropic: Cowork confirmation; CVSS re-rating rationale. GitHub: internal SRE org; shared-dependency remediation. Stripe: any official postmortem; internal process (all Unknown). Shopify: official postmortems for 2025 outages; deploy-train specifics. Uber: deploy machinery; net AI-ledger figure. Netflix: post-SimianArmy tooling. Spotify: current org model primary. Airbnb: AI-figure audit; sprawl-unwind status. Cursor: engineering writing; ARR audit; SpaceX-neutrality question. Replit: canonical postmortem; guardrail architecture.
