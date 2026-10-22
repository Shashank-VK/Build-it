# Domain A — Area 2: Requirements and Technical Specifications (AI-assisted)

*How AI assists product/engineering teams in writing, reviewing, evolving, and reconstructing PRDs and technical specs — AI used in the process of specifying what to build.*

> Read-only research. No installation, ranking, or recommendations. Accessed 2026-10-10 unless noted.

## 1. What teams demonstrably do

### AI PRD workflows from four starting points
- **Claim (Corroborated):** Practitioners build AI workflows that produce requirements from: (A) a raw product idea, (B) an existing PRD, (C) a requested change, or (D) an existing system whose documentation has fallen behind. The defining feature of the serious tools is **recovery from implementation** — reconstructing a current-state spec from code, tests, config, and observable output *before* discussing changes.
- **Concrete example:** bboysky/prd-studio (GitHub) defines four workflows — Shape (idea → approved brief + implementation PRD), Audit (measure PRD coherence/completeness/readiness), Change (trace and merge a requirement change without stale sections), Recover (reconstruct current behavior). Its recovery workflow maintains explicit evidence states: `VERIFIED` (corroborated by execution/tests/behavior), `DECLARED` (stated by docs, unconfirmed), `INFERRED` (reasoned from partial evidence), `OPEN`, `PLANNED`. This creates an As-Is baseline reviewed separately from the To-Be plan.
- Source: https://github.com/bboysky/prd-studio (GitHub; evidence class: primary technical; active 2026)

### Multi-stage PRD generation pipelines
- **Claim (Corroborated):** A common pattern is a 10–13 stage pipeline: executive summary → problem analysis → personas → functional/non-functional requirements → user stories (Gherkin acceptance criteria) → architecture → API spec → UX planning → security review → test planning → DevOps planning → risk assessment → assembly. Each stage builds on prior outputs for internal consistency.
- **Concrete example:** krosebrook/flashfusionwebsite's `PRD_GENERATOR_README.md` documents exactly this 13-step chain, with best-practice guidance that input quality dominates output quality ("be specific, add context, define scope, mention constraints").
- Source: https://github.com/krosebrook/flashfusionwebsite/blob/HEAD/docs/PRD_GENERATOR_README.md (GitHub; evidence class: primary technical; ~Feb 2026)

### Agent-enforced PRD discipline
- **Claim (Corroborated):** Teams encode PRD rules as agent instruction files that *require* clarifying questions before drafting ("DO NOT GENERATE THE PRD WITHOUT FIRST ASKING CLARIFYING QUESTIONS"), forbid implementation details in the PRD ("focus on WHAT and WHY, not HOW"), cap length (e.g. 2,000 words), and mandate numbered functional requirements.
- **Concrete example:** orionth1/ai-orchestrator's `docs/spec/create-prd.md` codifies: clarify (problem, feature, constraints, what is NOT in scope) → plan (section-by-section, research business rules via web search, assumptions) → draft (template-standard, English, ≤2000 words).
- Source: https://github.com/orionth1/ai-orchestrator/blob/HEAD/docs/spec/create-prd.md (GitHub; evidence class: primary technical; 2026)

### Full greenfield scaffolding: PRD → agent behavior files → plan → tasks
- **Claim (Corroborated):** A newer "spec-driven development" pattern generates a whole collaboration framework from a conversation: `PRD.md` + `CLAUDE.md` (Claude behavior spec) + `AGENTS.md` (Codex behavior spec) + plan + decision log (ADRs) + task list + verification scripts (`check.sh`/`build.sh`/`test.sh`).
- **Concrete example:** zc8163623/dualforge-workflow generates a 13-file framework in ~15 minutes of conversation for a small project, e.g. a TodoApp PRD with 7 functional requirements, 10 explicit out-of-scope items, 13 tasks across 4 stages, and ready verification scripts for a TypeScript+React+Vite stack.
- Source: https://github.com/zc8163623/dualforge-workflow (GitHub; evidence class: primary technical; ~Aug 2026)

### Role-simulating multi-agent spec workflows
- **Claim (Corroborated):** Open-source "context-aware coding agent" frameworks simulate analyst → PM → UX designer → product owner → architect → scrum master → orchestrator chains: the Analyst captures domain/personas, PM writes the PRD, PO refines epics, Architect records decisions, Scrum Master breaks epics into stories, Orchestrator runs implementation with quality gates. For brownfield, a `/codebase-detection` step precedes PRD generation.
- **Concrete example:** mazoonfahmi/coacoa documents the full command chain (`/analyst init` → `/pm new-prd` → `/ux-designer make-ui` → `/po refine-epics` → `/architect finalize-arch` → `/scrum-master create` → `/orchestrator run`).
- Source: https://github.com/mazoonfahmi/coacoa (GitHub; evidence class: primary technical; ~Mar 2026)

### The "Prompt Requirements Document" concept
- **Claim (Proposed):** A 2025 essay proposes the PRD itself evolve for the "vibe coding" era: requirements are clarified in collaboration with AI, translated into machine-friendly "magic prompts," code is co-created and verified, refactored, and lessons are fed *back into the living PRD* — the document updates at the same tempo as the code.
- Source: https://medium.com/@takafumi.endo/prompt-requirements-document-prd-a-new-concept-for-the-vibe-coding-era-0fb7bf339400 (Medium essay; evidence class: secondary interpretation; ~Apr 2025)

## 2. Tools and workflows
| Tool/pattern | Role |
|---|---|
| prd-studio (GitHub) | Shape/Audit/Change/Recover PRD workflows with evidence states |
| dualforge-workflow | PRD + agent behavior files + plan + verification scripts |
| coacoa | Role-simulating multi-agent spec chain |
| orionth1/ai-orchestrator `create-prd.md` | Agent-enforced PRD discipline (clarify → plan → draft) |
| PRD generator pipelines | 13-stage structured generation |
| Gherkin acceptance criteria | Testable requirements the agent can later verify against |

## 3. Failure modes
1. **PRD-implementation conflation.** AI happily writes implementation into requirements; the better workflows ban it explicitly ("UNDER NO CIRCUMSTANCES"). **Corroborated.**
2. **Shipped-behavior vs wishlist mixing.** Teams build before writing PRDs; a later PRD that mixes the two misleads everyone — the evidence-state system (VERIFIED/DECLARED/INFERRED/OPEN/PLANNED) exists precisely for this. **Corroborated.**
3. **Stale sections after changes.** Requirement changes leave stale sections behind; the "Change" workflow exists to trace and merge without residue. **Corroborated.**
4. **Generic, untestable requirements.** Without numbered, testable requirements and explicit out-of-scope lists, generated PRDs read well and specify nothing. **Inferred from the discipline rules documented.**
5. **Marketing-vs-measured gap.** "Generated in 15 minutes" examples are toy projects (TodoApp); no evidence found of these pipelines producing specs that survived a real enterprise review unchanged. **Unknown — no negative or positive evidence located.**

## 4. Costs / latency / reliability
- PRD generation is a low-token, chat-scale task: minutes of conversation, dollars at most via API. **Inferred.**
- Reliability hinges on the clarify-before-draft gate; agents that skip clarification produce plausible-sounding but wrong requirements. **Corroborated by the hard "DO NOT GENERATE without clarifying questions" rules.**

## 5. Human correction burden
- The workflow *is* the correction burden: clarify → review draft → audit coherence → trace changes. Teams that skip the audit step inherit the rework later in implementation. The prd-studio "Audit" workflow explicitly measures whether a PRD is coherent, complete, and ready to build — i.e., the human review is formalized, not eliminated. **Corroborated.**

## 6. Where AI genuinely helps vs where it creates rework
- **Genuinely helps:** turning rough notes into a structured, consistently formatted draft; enforcing completeness checklists (personas, NFRs, risks); reconstructing an As-Is baseline from a real codebase (evidence-backed recovery); keeping decision logs (ADRs) in the same pass.
- **Creates rework:** when the draft is accepted without the audit pass; when "recovered" specs are INFERRED but treated as VERIFIED; when requirements stay at the level of plausible prose instead of testable acceptance criteria.

## 7. Boundary notes (A vs B vs C)
- **Domain A:** AI helping the team write the spec. **Domain B** would be a shipped product whose feature *is* AI spec-writing sold to customers (e.g., a SaaS "AI PRD generator" product — the tool itself, as a product, is B; using it internally is A). **Domain C** would be AI drafting business documents like contracts or HR policies. Keep the three separate: who is the user of the AI (the builders = A; the end customer = B; the business operator = C).

## Evidence register (this file)
| # | Claim | URL | Source type | Author/org | Pub date | Confidence | Class |
|---|---|---|---|---|---|---|---|
| 2.1 | Four-workflow PRD studio with VERIFIED/DECLARED/INFERRED/OPEN/PLANNED evidence states | https://github.com/bboysky/prd-studio | GitHub repo | bboysky (community) | 2026 | Medium | primary technical |
| 2.2 | 13-stage PRD generation pipeline; input quality dominates | https://github.com/krosebrook/flashfusionwebsite/blob/HEAD/docs/PRD_GENERATOR_README.md | GitHub repo docs | krosebrook | ~Feb 2026 | Medium | primary technical |
| 2.3 | Agent-enforced PRD rules: clarify first, no implementation, ≤2000 words | https://github.com/orionth1/ai-orchestrator/blob/HEAD/docs/spec/create-prd.md | GitHub repo docs | orionth1 | 2026 | Medium | primary technical |
| 2.4 | 13-file framework generation (PRD + CLAUDE.md + AGENTS.md + plan + scripts) | https://github.com/zc8163623/dualforge-workflow | GitHub repo | zc8163623 | ~Aug 2026 | Medium | primary technical |
| 2.5 | Role-simulating multi-agent spec chain (analyst→PM→PO→architect→SM→orchestrator) | https://github.com/mazoonfahmi/coacoa | GitHub repo | mazoonfahmi | ~Mar 2026 | Medium | primary technical |
| 2.6 | "Prompt Requirements Document" living-PRD concept | https://medium.com/@takafumi.endo/prompt-requirements-document-prd-a-new-concept-for-the-vibe-coding-era-0fb7bf339400 | Essay | takafumi.endo | ~Apr 2025 | Low | secondary interpretation |
