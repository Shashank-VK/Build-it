# expansion-companies — index

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

37 company/team case files. Every file has: forensic reconstruction (how the machine actually works), postmortem record (failures hunted down), narrative audit (polished stories dismantled with receipts), transferable lessons, and a sources table with methodology labels (Verified / Corroborated / Inferred / Proposed / Unknown). Files 01–12 were written first and later retrofitted with narrative audits (marked "retrofit 2026-10-10"); files 13–37 were written with the full three-section structure natively.

Ranked by instructiveness — a judgment call weighing evidence quality, transferability, and how much the case corrects a common misconception.

| Rank | File | Company | One-line why |
|---|---|---|---|
| 1 | [16-knight-capital.md](16-knight-capital.md) | Knight Capital | The most expensive deployment failure on record ($440M, 45 min) — every layer failed, and the SEC's findings dismantle the "one engineer" story. |
| 2 | [18-healthcare-gov.md](18-healthcare-gov.md) | Healthcare.gov rescue | The complete arc: command-vacuum failure → tech-surge rescue (two-minute patch drills) → USDS founded. Failure *and* recovery, documented. |
| 3 | [23-valve.md](23-valve.md) | Valve | The famous flat-org experiment dismantled: hidden hierarchy, stack ranking without managers, and the Steam subsidy that invalidates the experiment. |
| 4 | [01-cloudflare.md](01-cloudflare.md) | Cloudflare | Postmortem-culture exemplar that confesses its own DR theater ("never tested the entire facility") — transparency with receipts. |
| 5 | [31-atlassian.md](31-atlassian.md) | Atlassian | The 2022 outage: a script deleted 775 customers' sites; "backups are not recovery" in a 7,500-word public review. |
| 6 | [09-gitlab.md](09-gitlab.md) | GitLab | The 2017 rm -rf on the primary DB — but the real lesson is the DMARC-bounced backup alert nobody received. |
| 7 | [15-apple.md](15-apple.md) | Apple | Accountability via firings (MobileMe, Maps) — and why strategic deadlines, not talent, predicted both failures. |
| 8 | [17-netscape-mozilla.md](17-netscape-mozilla.md) | Netscape/Mozilla | The canonical rewrite postmortem — plus the audit that "never rewrite" is over-learned dogma (Firefox was the rescope that worked). |
| 9 | [28-tesla.md](28-tesla.md) | Tesla | "Production hell" with a CEO's precise public admission ("my mistake") — automate last, not first, violated by the rule's own author. |
| 10 | [14-spacex.md](14-spacex.md) | SpaceX | Hardware-rich iteration with the FAA enforcing the postmortem loop; commodity Linux + voting redundancy beats rad-hard chips. |
| 11 | [34-vercel.md](34-vercel.md) | Vercel | Vercel's own VP of Engineering admits the App Router "wasn't really finished" when made the default — the rarest artifact: a primary-source self-postmortem. |
| 12 | [19-digg-v4.md](19-digg-v4.md) | Digg v4 | Your governance mechanism *is* the product: removing the bury button killed the community in days. |
| 13 | [21-windows-vista.md](21-windows-vista.md) | Windows Vista | Allchin's "crashing into the ground" memo and the 2004 reset — the honest mid-project postmortem most orgs never write. |
| 14 | [24-riot-games.md](24-riot-games.md) | Riot Games | Behavioral systems as applied science (87% of toxicity from regulars having bad days) + the plugin-architecture/LKG client pipeline. |
| 15 | [35-datadog.md](35-datadog.md) | Datadog | The best build-vs-buy argument in the corpus (Distributed DataFusion) — each rejected alternative named with the requirement it missed. |
| 16 | [13-palantir.md](13-palantir.md) | Palantir | The FDE/ontology machine reconstructed from job postings — and the a16z audit: copying it without the platform makes you an expensive consultancy. |
| 17 | [25-ccp-games.md](25-ccp-games.md) | CCP / EVE Online | Time Dilation: when you can't meet the SLA, change the contract explicitly — genius as consistency mechanism, confession as performance story. |
| 18 | [27-tailwind-labs.md](27-tailwind-labs.md) | Tailwind Labs | Course-funded R&D (get paid to do customer discovery) — and the Sept 2026 Shopify deal that complicates the "bootstrapped forever" story. |
| 19 | [29-framework.md](29-framework.md) | Framework | The transparency playbook (June 2026 delay: "grounding bug in the touchpad PCB") — plus a caught fabrication in my own sources. |
| 20 | [36-slack.md](36-slack.md) | Slack | Flannel (cache by team locality) and the cellular turn — incident-driven architecture, honestly named. |
| 21 | [03-figma.md](03-figma.md) | Figma | Multiplayer's "dumber algorithm" — and the later Rust-port receipt that the simplicity was product-layer only. |
| 22 | [10-etsy.md](10-etsy.md) | Etsy | Blameless postmortems as *information extraction*; deploy culture as downstream of architecture. |
| 23 | [11-basecamp.md](11-basecamp.md) | Basecamp/37signals | The calm-company audit: calm for employees, war footing for marketing — plus HEY vs. the App Store. |
| 24 | [12-jane-street.md](12-jane-street.md) | Jane Street | The black-box audit: you can't learn operations from a company that doesn't narrate them; "hire geniuses" isn't transferable. |
| 25 | [20-google-wave.md](20-google-wave.md) | Google Wave | Demo applause is not validation; invite-only scarcity is self-sabotage for network goods. |
| 26 | [22-firefox-os.md](22-firefox-os.md) | Firefox OS | Values don't compile: define kill criteria in advance, and kill cleanly instead of zombie-pivoting. |
| 27 | [37-lean-outliers.md](37-lean-outliers.md) | WhatsApp/Instagram/Midjourney | It's scope that increases headcount, not users — with the Oct 2021 outage as the counter-postmortem. |
| 28 | [04-notion.md](04-notion.md) | Notion | "Boring Postgres" was the destination after two failed architectures, not the starting position. |
| 29 | [06-linear.md](06-linear.md) | Linear | Craft as moat — and the audit: no public failures found is an epistemic limit, not a clean bill. |
| 30 | [07-tailscale.md](07-tailscale.md) | Tailscale | Data plane decentralized, trust centralized — "decentralized" needs the qualifier. |
| 31 | [05-discord.md](05-discord.md) | Discord | World-class infra, cluttered product — engineering quality and product focus are independent variables. |
| 32 | [08-sourcegraph.md](08-sourcegraph.md) | Sourcegraph | The enterprise-only pivot is the real postmortem: the mission narrowed to fit the revenue. |
| 33 | [30-ibm-carbon.md](30-ibm-carbon.md) | IBM Carbon | Token layers (global→alias→semantic) as the portable idea; repo-forensics (AGENTS.md) as method. |
| 34 | [32-adobe-spectrum.md](32-adobe-spectrum.md) | Adobe Spectrum | React Aria: accessibility is behavior, not markup — plus the $20B Figma-bid as engineering indictment. |
| 35 | [33-salesforce-lightning.md](33-salesforce-lightning.md) | Salesforce Lightning | Density-first philosophy and Trailhead-as-distribution; thinnest evidence in the set. |
| 36 | [02-fastly.md](02-fastly.md) | Fastly | The perfect apology didn't save the business — comms excellence is necessary, not sufficient. |
| 37 | [26-pinboard.md](26-pinboard.md) | Pinboard | The solo-founder audit: optimizes for founder freedom, not user service; thinnest evidence, kept for the model's honesty. |

## How to use this index
- **Postmortem culture:** start with 16, 18, 01, 31, 09.
- **Org design:** 23, 13, 15, 37.
- **Design systems:** 30, 32, 33, 31 (ADS half).
- **Failure classics:** 17, 19, 20, 21, 22.
- **Narrative dismantling (strongest audits):** 23, 13, 34, 11, 12.
- See [evidence-register.md](evidence-register.md) for source statistics, verification debts, and honest limitations.
