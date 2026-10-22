# Domain A — Area 3: UX Research and Interface Design (AI-assisted)

*How AI assists product teams with user research synthesis, wireframing, visual design, prototyping-in-design-tools, and accessibility checks — AI used in the process of designing the interface.*

> Read-only research. No installation, ranking, or recommendations. Accessed 2026-10-10 unless noted.

## 1. What teams demonstrably do

### In-file AI assistance (Figma AI)
- **Claim (Verified):** Figma ships AI actions inside the design file: find assets/designs, replace content, add interactions, rename layers, rewrite/translate/shorten text, and image operations (generate/edit images, remove background, boost resolution, expand images, isolate/erase objects, vectorize). Figma AI and Figma Make moved from beta to general availability on **24 July 2025**. "First Draft" (text-to-editable-layout) was moving to Figma's agent as its entry point as of May 2026 (beta, gradual rollout).
- Source: https://merge.rocks/blog/top-ai-design-tools-for-ux-ui-designers-in-2025 (Merge Rocks practitioner blog; evidence class: corroborating; updated ~Aug 2026)
- **What actually sticks in daily use (first-hand practitioner):** shortening text that doesn't fit a layout, removing backgrounds, prompt-based image editing — i.e., production chores, not design decisions.

### Prompt-to-UI exploration tools
- **Claim (Corroborated):** Teams use prompt-to-screen tools (Uizard: prompts/sketches/screenshots → editable multi-screen concepts; Google Stitch: text/image/wireframe → UI variations; Paper: open-question creative partner for flow structure) for the "blank canvas" phase, then rebuild the winning direction in Figma for precision.
- **Concrete example:** A documented realistic workflow: PM adds user needs (ticket volume, response time, urgent cases, agent workload) to Paper; designer asks for three dashboard structures; ~45 minutes to rough flows; winning direction rebuilt in Figma where the design system, responsive rules, error/empty states, and clickable prototype are applied; engineers comment on edge cases.
- Source: https://woahtech.com/paper-design-ai-paper-vs-figma-for-ai-assisted-product-design/ (Woahtech; evidence class: first-hand practitioner; Sep 2026)

### AI-assisted UX research operations
- **Claim (Corroborated):** UX research platforms embed AI for study analysis: Maze (research studies + automated analysis; AI summaries still need source-level review), Userbrain (unmoderated testing with real users; AI-assisted findings; participant quality and task wording still matter), Attention Insight (predictive visual-attention maps; prediction is not usability evidence).
- Source: https://design-rise.com/top-ai-tools-for-ui-ux-designers-in-2026-from-prototyping-to-user-research/ (DesignRise; evidence class: corroborating; ~Aug 2026)

### Accessibility automation
- **Claim (Corroborated):** Stark runs accessibility checks across design and dev with issue detection and suggested fixes — but automated compliance does not guarantee accessibility; manual testing remains required. Custom-GPT-style design assistants' accessibility suggestions "do not establish WCAG conformance."
- Source: https://design-rise.com/top-ai-tools-for-ui-ux-designers-in-2026-from-prototyping-to-user-research/ and https://www.therundown.ai/tools/ui-designer-gpt (evidence class: corroborating / vendor-adjacent)

### Academic evaluation of AI design tools
- **Claim (Corroborated):** A 2025 thesis (Theseus.fi) testing Uizard, Figma AI, and Adobe Firefly found: efficiency gains are real (rapid ideation, task automation), but human supervision must remain essential to protect brand standards; tools are weak at genuine artistic expression, emotional quality, and diverse situations. Uizard: low–moderate creative freedom, low customization flexibility. Figma AI: moderate–high creative freedom, limited contextual awareness.
- Source: https://www.theseus.fi/bitstream/handle/10024/891768/Obanya_Chukwuemeka.pdf (academic thesis; evidence class: primary technical; 2025)

## 2. Tools and workflows
| Tool | Role | Main limitation (as documented) |
|---|---|---|
| Figma AI / Figma Make | In-file assistance; prompt-to-code interactive prototype | Generated work still needs design-system + UX review; Make publishing in beta |
| Uizard | Rapid multi-screen prototypes | Polished screens can hide weak interaction logic |
| Google Stitch | Prompt-to-UI exploration | Generated code and UX decisions require validation |
| Locofy | Design-to-code handoff | Poorly structured design files → poor code |
| Maze / Userbrain | Research studies, unmoderated testing | AI summaries need source-level review |
| Attention Insight | Predictive attention maps | Prediction ≠ usability evidence |
| Stark | Accessibility checks | Automated compliance ≠ actual accessibility |
| Relume | Sitemaps, wireframes, style guides | Optimized for marketing-site workflows |

## 3. Failure modes
1. **Polish hiding weak product thinking.** AI-generated screens look finished, which suppresses the critical questioning a rough sketch would invite. Multiple practitioners flag this independently. **Corroborated.**
2. **Generic / off-brand output.** Generated personas and research claims are assumptions unless grounded in real user evidence; UI suggestions can be generic or inconsistent with the brand system. **Corroborated.**
3. **Weak interaction logic under pretty screens.** Multi-screen concepts often lack coherent flow logic, error states, and edge cases. **Corroborated.**
4. **Credit burn on iteration.** Practitioners report burning through AI credit limits quickly, with small tweaks over-consuming credits; policies still evolving and poorly documented. **First-hand practitioner reports.**
5. **Inconsistent interpretation.** The same prompt yields structurally different results across tools — some focus on visuals, some on structure, few balance both. **Corroborated (same-prompt test across 5 tools).**

## 4. Costs / latency / reliability
- Figma AI operates on credit limits (free-tier limits can exhaust quickly); paid tiers vary. v0-style tools: ~$20/month typical. **Corroborated from multiple tool roundups.**
- Latency is seconds-to-minutes per generation; the expensive part is the human rework loop, not inference. **Inferred.**

## 5. Human correction burden
- Designers consistently report the durable pattern: AI gets past the blank screen; the designer still makes hierarchy, interaction, accessibility, and consistency decisions. AI research summaries require source-level review. Accessibility output requires manual testing. **Corroborated across academic + practitioner sources.**

## 6. Where AI genuinely helps vs where it creates rework
- **Genuinely helps:** blank-canvas ideation (multiple directions in <1 hour); production chores (text fitting, background removal, layer renaming, translation); first-pass research synthesis; attention prediction as a *triage* signal.
- **Creates rework:** polished-but-shallow screens that must be rebuilt against the design system; AI "research findings" that must be re-verified against session recordings; accessibility checklists treated as conformance.

## 7. Boundary notes (A vs B vs C)
- **Domain A:** the design team uses AI to design the product. **Domain B** would be AI features *inside* the shipped product's UI (e.g., an in-app "AI assistant" the end user talks to, or AI-generated content the user sees). A Figma plugin that generates screens is A; a chatbot embedded in the released app is B. **Domain C** would be AI generating marketing copy or business reports — adjacent but organizational, not product-building.

## Evidence register (this file)
| # | Claim | URL | Source type | Author/org | Pub date | Confidence | Class |
|---|---|---|---|---|---|---|---|
| 3.1 | Figma AI GA 24 Jul 2025; First Draft → agent entry point May 2026 beta; in-file actions list | https://merge.rocks/blog/top-ai-design-tools-for-ux-ui-designers-in-2025 | Practitioner blog | Merge Rocks | ~Aug 2026 | High (dated product facts) | corroborating |
| 3.2 | Paper-first/Figma-second workflow; 45-min exploration example | https://woahtech.com/paper-design-ai-paper-vs-figma-for-ai-assisted-product-design/ | Practitioner blog | Woahtech | Sep 2026 | Medium | first-hand practitioner |
| 3.3 | Tool comparison table with per-tool limitations | https://design-rise.com/top-ai-tools-for-ui-ux-designers-in-2026-from-prototyping-to-user-research/ | Roundup | DesignRise | ~Aug 2026 | Medium | corroborating |
| 3.4 | Thesis: efficiency gains real; supervision essential; weak on expression/emotion | https://www.theseus.fi/bitstream/handle/10024/891768/Obanya_Chukwuemeka.pdf | Academic thesis | Obanya (Theseus.fi) | 2025 | Medium–High | primary technical |
| 3.5 | Same-prompt test across 5 tools; inconsistent interpretation; AI as support not replacement | https://medium.com/@khushidoshi09/i-tested-the-5-best-ai-tools-for-ui-design-with-the-same-prompt-e5e1bb93a7a3 | Practitioner test | Khushi Doshi | Feb 2026 | Medium | first-hand practitioner |
| 3.6 | Third-party design GPTs: generated personas are assumptions; a11y ≠ WCAG conformance | https://www.therundown.ai/tools/ui-designer-gpt | Tool assessment | TheRundown.ai | 2026 | Medium | secondary interpretation |
