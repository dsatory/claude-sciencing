---
description: Structure and draft scientific documents — abstracts, proposals, reports, SOWs, protocols, memos, presentations, patents, and more
argument-hint: [type] [optional details]. Types: outline, abstract, grant, proposal, report, sow, progress, patent, presentation, memo, one-pager, white-paper, protocol, flow
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch
---

# Scientific Drafting

Generate structured scientific content. Parse the first argument from $ARGUMENTS to determine the drafting mode.

## File Input Support

When the user provides a file to work with (outline, existing draft, solicitation, etc.):
- **`.md`, `.tex`, `.txt`** — read directly
- **`.docx`, `.pptx`, `.xlsx`** — read via python-docx/python-pptx/openpyxl (document-formats skill)
- **`.pdf`** — read via Claude Code's native PDF reader
- **`.gdoc`, `.gsheet`, `.gslides`** — these are Google Drive pointer files. Read the JSON to extract the `doc_id`, then open the export URL in the user's browser to download as `.docx`/`.xlsx`/`.pptx`. Ask the user to confirm the download location before proceeding.

## Argument Routing

- **outline** — Generate a document outline (IMRaD, review, protocol, or custom)
- **abstract** — Write or refine an abstract (grant, conference, or journal)
- **grant** — Draft grant-specific sections (Specific Aims, Significance, Innovation, Approach)
- **proposal** — Draft a government or commercial proposal section
- **report** — Draft a technical report or report section
- **sow** — Draft a Statement of Work with tasks, deliverables, milestones
- **progress** — Draft a progress/milestone report
- **patent** — Draft an invention disclosure or patent technical section
- **presentation** — Outline a slide deck or generate speaker notes
- **memo** — Draft an internal decision memo
- **one-pager** — Draft an executive summary / one-pager
- **white-paper** — Draft a thought leadership white paper
- **protocol** — Draft a laboratory protocol or SOP
- **flow** — Analyze argument flow in existing text
- If no argument or unrecognized, ask which mode to use

Before drafting, the `scientific-writing` skill provides additional strategic guidance for each document type. If it is loaded, its reference files contain detailed conventions — trust that context and apply its principles.

**PRE-DRAFT SOURCE CHECK — mandatory for proposals, reports, and reviews:**

Before writing any document that cites scientific literature, check the project's `literature/PDFs/` folder and `references/library.md`. Count verified sources (downloaded PDFs you have read). If the count is low:

- **0-2 verified sources:** STOP. Tell the user: "I don't have enough source material to write a credible [document type]. Run `/sci-search` and download papers first."
- **3-5 verified sources:** Warn: "I have [N] verified sources. I can draft, but the literature coverage will be thin. Unverified claims will be marked `[NOT IN LIBRARY]`. Want to proceed or download more papers first?"
- **6+ verified sources:** Proceed. Still mark any unverified citations clearly.

This gate prevents the failure mode where a proposal or review gets written from web search abstracts and looks authoritative but isn't backed by actual paper reading.

---

## Mode: Outline

Generate a structured outline appropriate to the document type.

### For Research Papers (IMRaD)

**Introduction:**
- Opening context (broad field significance)
- Knowledge gap or unresolved question
- Study rationale and objectives
- Hypothesis or central claim (if applicable)

**Methods:**
- Study design and approach
- Materials, reagents, model systems
- Experimental procedures (chronological or logical grouping)
- Data collection and analysis plan
- Statistical methods with justification
- Ethical approvals, biosafety, or regulatory considerations

**Results:**
- Primary findings organized by experimental aim
- Key data points and statistical outcomes
- Logical progression building toward the central claim
- Negative results that inform interpretation

**Discussion:**
- Summary of principal findings
- Comparison with existing literature
- Mechanistic interpretation or model
- Limitations and alternative explanations
- Future directions
- Concluding statement tying back to the knowledge gap

### For Review Articles
Background → Current State (organized thematically) → Gaps and Controversies → Future Directions → Conclusions.

### For Protocols
Purpose → Safety → Materials and Equipment → Step-by-Step Procedure → Expected Results → Troubleshooting → References.

When generating an outline, ask the user for:
1. Document type
2. Working title or topic
3. Key findings or objectives (2-3 sentences)
4. Target journal or audience (if known)

---

## Mode: Abstract

Write or refine an abstract. Determine whether to generate from scratch or revise existing text.

### Structured Abstract Format
For journals requiring structured abstracts:
- **Background/Objective:** 1-2 sentences establishing context and aim
- **Methods:** 2-3 sentences on study design, subjects, interventions, measurements
- **Results:** 2-4 sentences with primary quantitative findings, effect sizes, confidence intervals or p-values
- **Conclusions:** 1-2 sentences stating the main conclusion and its implication

### Unstructured Abstract Format
- Sentence 1-2: Context and gap
- Sentence 3: Study aim or hypothesis
- Sentence 4-5: Approach and methods
- Sentence 6-8: Key results with quantitative data
- Sentence 9-10: Interpretation and significance

### Grant / Proposal Abstract
Compressed narrative optimized for program managers:
1. **Problem + mission alignment** (1-2 sentences)
2. **Gap / limitation of current approaches** (1-2 sentences, with specific numbers)
3. **Proposed approach** (2-4 sentences, name specific methods/organisms/catalysts)
4. **Key preliminary results** (1-2 sentences, most compelling data points)
5. **Impact / deliverables** (1-2 sentences, tied to program metrics)

Match the solicitation's language. Echo their key phrases when describing your approach.

### Abstract Refinement
When revising an existing abstract:
1. Check word count against target (typically 150-500 words)
2. Verify all key results are quantified
3. Remove hedging language that weakens claims without adding nuance
4. Ensure the final sentence conveys significance
5. Flag any claims not supported by the results stated

---

## Mode: Grant

Draft grant-specific sections following NIH or similar funding agency conventions.

### Specific Aims Page
- **Opening paragraph:** Significance and urgency (2-3 sentences), identify the gap, state the long-term goal and project objective
- **Central hypothesis:** One clear, testable statement
- **Rationale:** Why this hypothesis is well-supported
- **Aims (2-3):** Each states what will be done and the expected outcome. Aims should be independent — failure of one should not invalidate others.

### Significance Section
- Burden of the problem (prevalence, economic impact)
- Current state and limitations
- How the proposed work addresses the gap
- Expected positive impact

### Innovation Section
- New concepts, approaches, methods, or technologies
- How the approach differs from alternatives
- Preliminary data supporting feasibility

### Approach Section (per aim)
- Rationale and working hypothesis
- Experimental design with controls
- Methods and analysis plan
- Expected outcomes and interpretation
- Potential pitfalls and alternative strategies
- Timeline and milestones

Ask for the funding mechanism (R01, R21, K award, DARPA, ARPA-E, ARPA-H, DOE, foundation) to calibrate scope and tone.

---

## Mode: Proposal

Draft a government or commercial proposal section. Ask the user:
1. Who is the funder/client?
2. Is there a solicitation? (If so, read it — mirror its structure exactly)
3. What section are they drafting?
4. What are the evaluation criteria?

Key principles:
- **Mirror the solicitation's structure** — never invent your own organization
- **Echo the solicitation's language** when describing your approach
- **Allocate page real estate proportionally** to evaluation criteria ranking
- **Include preliminary data** — the single strongest predictor of success
- **State-of-the-art comparison table** showing how your approach advances beyond current best

---

## Mode: Report

Draft a technical report or section. Structure:
1. Executive Summary (1-2 pages, self-contained)
2. Introduction / Background
3. Materials and Methods
4. Results (organized by research question, not experiment number)
5. Discussion
6. Conclusions and Recommendations
7. References
8. Appendices

Tables and figures carry the primary data; text interprets and contextualizes them.

---

## Mode: SOW

Draft a Statement of Work. For each task, specify:
- Task number and title
- Objective
- Approach (sufficient detail for accountability)
- Inputs and dependencies
- Outputs/deliverables (measurable)
- Duration and timeline

Include a milestones table with go/no-go criteria and a deliverables table with due dates and formats. Be specific enough to be enforceable, flexible enough to accommodate reality.

---

## Mode: Progress

Draft a progress/milestone report. Structure per task:
- **Status:** On Track / At Risk / Delayed / Complete (traffic light)
- **Progress this period:** with key quantitative results
- **Planned vs. actual**
- **Issues encountered**
- **Next period plan**

Include milestone status table and risk register update. Lead with results, not activities ("Achieved 47% yield" not "Performed experiments").

---

## Mode: Patent

Draft an invention disclosure. Structure:
1. Title of Invention (descriptive and specific)
2. Inventors
3. Problem Solved
4. Description (broadest version AND best embodiment)
5. Prior Art (what's closest, how yours differs)
6. Experimental Evidence
7. Potential Applications
8. Public Disclosures (dates — critical for filing deadlines)

Describe the broadest version AND the specific best embodiment. Be exhaustive in examples — more examples = broader claim support.

---

## Mode: Presentation

Outline a slide deck. Principles:
- One idea per slide
- Assertion-evidence structure (title = the takeaway, body = the evidence)
- ~1 slide per 1.5-2 minutes of talk time

Structure: Problem (2-3 slides) → Approach → Key Results (strongest data) → Conclusions + Next Steps → Acknowledgments.

Put the most important result in the first third of the talk, not the last slide before conclusions.

---

## Mode: Memo

Draft an internal decision memo:
- **Subject line:** State the decision, not the topic
- **Context:** Why this memo exists (2-3 sentences)
- **The decision needed** with deadline
- **Options with trade-offs** (table format)
- **Recommendation** with reasoning
- **Next steps**

---

## Mode: One-Pager

Draft an executive summary (~400-600 words, one page):
- **Hook** (1-2 sentences — most compelling fact or question)
- **Problem** (2-3 sentences with specific numbers)
- **Solution** (3-5 sentences, one level of technical detail)
- **Key data** (callout box with 3-4 metrics)
- **Path forward / the ask** (2-3 sentences)

---

## Mode: White-Paper

Draft a thought leadership paper (5-15 pages):
1. The Problem (25%)
2. Why Current Approaches Fall Short (15%)
3. The Emerging Solution (35%)
4. Evidence and Benchmarks (15%)
5. Path Forward and Call to Action (10%)

---

## Mode: Protocol

Draft a laboratory protocol or SOP. Ask the user:
1. What procedure? (assay, extraction, fermentation, analytical method, etc.)
2. Target audience? (experienced researcher who needs parameters, or new lab member who needs every detail)
3. Regulated context? (GLP/GMP/ISO requires SOP format with document control)

Structure:
1. **Purpose** — What this protocol achieves and why (specific, not generic)
2. **Safety** — PPE, hazards, waste disposal, BSL requirements
3. **Materials table** — Reagent, catalog #, supplier, concentration, storage
4. **Equipment** — Instruments with model numbers for instrument-specific steps
5. **Reagent preparation** — Buffers, media, working solutions with recipes
6. **Procedure** — Numbered steps, one action per step, lead with verb
7. **Expected results** — What good data looks like, control acceptance criteria
8. **Troubleshooting** — Top failure modes in table format
9. **Version history** — Track changes across protocol iterations

Key principles:
- One action per numbered step — never combine multiple actions
- Specify everything quantitatively (temperature, time, speed, volume)
- Mark **CRITICAL** steps, **CAUTION** warnings, **PAUSE POINT** locations
- Include catalog numbers for all reagents (not just names)
- Include expected observations at key steps ("pellet should be white")
- Include positive, negative, and no-template controls with acceptance criteria

The `scientific-writing` skill's `references/protocols.md` contains detailed conventions — read it when drafting protocols.

---

## Mode: Flow

Analyze argument flow of existing text:
1. **Thesis tracking:** Clear central argument? Each paragraph advances it?
2. **Logical progression:** Ideas follow logically? Flag non-sequiturs.
3. **Transition quality:** Connections between paragraphs explicit?
4. **Evidence integration:** Evidence before or after claims? Link clear?
5. **Counterargument handling:** Limitations addressed?

Present as numbered logical steps, gaps, and specific suggestions.

---

## General Guidance

- Active voice default, passive acceptable in Methods
- Specific, concrete language over vague qualifiers
- Concise first drafts — scientific writing favors brevity
- When the user mentions a specific journal or funder, look up requirements if possible
