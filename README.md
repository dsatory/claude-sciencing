# Claude Sciencing

A Claude Code plugin for scientific research in biotech and life sciences — covering the full literature-to-publication lifecycle: search, organize, read, analyze, synthesize, write, edit, and publish.

## Slash Commands

| Command | Description |
|---------|-------------|
| `/sci-search` | Search PubMed, preprints, and patents. Build reading lists. Map research landscapes. |
| `/sci-library` | Manage a local reference library — add papers, tag, organize, export BibTeX/citations. |
| `/sci-read` | Distill papers and patents — tactical briefings, deep analysis, data extraction, patent claims. |
| `/sci-review` | Compile thematic literature reviews with state-of-the-art comparison tables and gap analysis. |
| `/sci-draft` | Draft any scientific document — abstracts, proposals, reports, SOWs, patents, presentations, protocols, memos. |
| `/sci-edit` | Multi-pass scientific editing — clarity, tone, jargon, logical flow, topic sentence analysis. |
| `/sci-figures` | Write figure captions, format tables, manage panel labeling for publications. |

### Quick Example

```
"Search for recent papers on engineered bacteria for succinic acid"   → Finds and ranks relevant literature
"Add this paper to my library: 10.1016/j.ymben.2024.01.005"          → Resolves metadata, generates BibTeX
"Give me a deep technical analysis of this paper"                     → Structured analysis with field-specific lenses
"Write a state-of-the-art review on host selection for organic acids" → Thematic synthesis with comparison tables
"Draft a proposal for this grant solicitation"                        → Full proposal structured to requirements
"Edit this draft for clarity and scientific tone"                     → Multi-pass editing
"Write captions for all figures"                                      → Publication-quality captions
```

### Full Walkthrough: Writing a Government Proposal

This end-to-end example shows how the plugin handles the full proposal lifecycle — from receiving a solicitation to submitting a compliant document. Every step uses natural language prompts; the plugin's skills activate automatically based on context.

---

**Step 1: Read the solicitation and understand requirements**

```
"Read this solicitation and extract the key requirements — evaluation
criteria, page limits, required sections, formatting specs, and deadlines"
```

**What the plugin does:**
- **document-formats** skill reads the solicitation PDF
- **scientific-reading** skill activates to extract structured information — not a generic summary, but the specific data you need: evaluation criteria with weights, page limits per section, required section order, font/margin specs, technical focus areas, mandatory attachments, and submission deadlines
- Output: a structured requirements brief you can reference throughout the writing process

---

**Step 2: Search the literature landscape**

```
"Search for recent papers on microbial conversion of industrial waste
to high-value chemicals — focus on the last 2 years"

"Also search for papers on [your specific technical approach]"
```

**What the plugin does:**
- **scientific-reading** and **pubmed-setup** skills activate — verifies PubMed MCP is connected, then queries with optimized Boolean queries and MeSH terms
- Searches across PubMed, preprints (bioRxiv, chemRxiv), and web sources in parallel
- Returns results ranked by relevance, recency, and open-access availability
- Suggests a reading order, identifies gaps in the search, and recommends follow-up queries
- Output: a curated reading list organized by priority

---

**Step 3: Download the papers**

```
"Download all open-access PDFs from that search"
```

**What the plugin does:**
- **paper-retrieval** skill activates with its exhaustive 5-tier, 16-source strategy
- **Tier 0 (PubMed MCP):** Resolves all identifiers (DOI → PMID → PMCID) and checks OA status for every paper upfront
- **Fast pass (Tiers 1–2):** Downloads from PMC, publisher OA, Unpaywall, and Europe PMC — handles the easy ones first
- **Stubborn pass (Tiers 3–5):** For remaining papers, searches institutional repositories, author websites, preprint servers, and creative web queries — tries at least 8 sources per paper before giving up
- **Verifies every download** — checks for HTML masquerading as PDF, stub files, and corrupted downloads
- **Names files** in standardized format: `JournalAbbrev_3word_description_year.pdf`
- **Auto-suggests category folders** by analyzing the batch (e.g., `01_Reviews/`, `02_Metabolic_Engineering/`), asks for confirmation, then sorts
- Output: organized PDF library with a download log documenting every attempt

---

**Step 4: Analyze key papers**

```
"Give me a deep technical analysis of MetabEng_Ecoli_succinate_2024.pdf"

"Extract the quantitative data from these review papers into comparison tables"
```

**What the plugin does:**
- **scientific-reading** skill provides structured analysis tailored to the paper type:
  - **Deep analysis:** Methods-first evaluation, separating claims from evidence, extracting specific numbers with units and conditions
  - **Data extraction:** Pulls quantitative results into comparison tables — titers, yields, productivities, conditions — ready for your proposal's state-of-the-art table
- Applies field-specific evaluation lenses: flags whether results are from model substrates or real feedstocks, shake flask or bioreactor, and whether the mass balance was closed
- Output: structured briefs with "bottom line," key findings, relevance to your project, limitations, and action items

---

**Step 5: Build your reference library**

```
"Add these papers to my reference library: 10.1016/j.ymben.2024.01.005,
10.1038/s41467-025-12345-6, 10.1021/acscatal.5c00123"

"Tag smith2024 as for-proposal, state-of-art, key-benchmark"
```

**What the plugin does:**
- Resolves full metadata via PubMed MCP for each DOI/PMID
- Generates BibTeX entries and adds to `library.bib` (for LaTeX) and `library.md` (for browsing)
- Supports batch adding from search results, reference lists, or DOI lists
- Tags let you filter later: `#for-proposal` to pull only proposal-relevant citations
- Tracks reading status (unread → reading → read → cited)
- Output: version-controlled reference library with BibTeX export

---

**Step 6: Synthesize the literature into a review section**

```
"Write a state-of-the-art review section on microbial conversion of
aromatic compounds — include a comparison table of reported titers,
yields, and productivities across studies"
```

**What the plugin does:**
- **scientific-writing** and **scientific-reading** skills work together to produce thematic synthesis
- Builds state-of-the-art comparison tables with standardized metrics across studies
- Organizes by technical challenge or approach — not paper-by-paper summaries
- Identifies consensus, contradictions, and gaps in the literature
- Frames gaps as opportunities that your proposed approach addresses
- Output: ready-to-use literature review section with comparison tables and properly formatted citations

---

**Step 7: Draft the proposal**

```
"Draft a proposal for this solicitation. Our approach is [brief
description]. Use the literature review and paper analyses from earlier."
```

**What the plugin does:**
- **scientific-writing** skill activates to provide strategic framing calibrated to the audience and funder — each agency has distinct conventions and the skill adapts accordingly
- Mirrors the solicitation's section structure exactly — never invents its own organization
- Allocates effort proportional to evaluation criteria weights
- Drafts each section with specific technical content: preliminary data, risk mitigation, milestones, team qualifications demonstrated with evidence
- **scientific-style** skill runs in the background ensuring correct nomenclature (gene/protein naming, organism italicization, SI units), citation placement, and scientific tone
- Marks gaps with `[PLACEHOLDER: ...]` where data, figures, or specific numbers are needed
- Output: complete first draft structured to the solicitation

---

**Step 8: Create figures and tables**

```
"Write captions for all figures in the proposal"

"Format the results as a milestone table and a state-of-the-art comparison table"
```

**What the plugin does:**
- Writes publication-quality captions that make figures standalone-interpretable
- Formats comparison tables (state-of-the-art benchmarks, experimental results, milestone tables) with consistent column headers, units, and significant figures
- Manages panel labeling (A, B, C) and cross-references throughout the document
- **document-formats** skill activates if you need to generate the actual PPTX for figure slides or XLSX for data tables
- Output: formatted captions, tables, and panel references

---

**Step 9: Edit and refine**

```
"Edit the proposal draft for clarity — tighten the prose and
strengthen the quantitative claims"

"Now check the logical flow and scientific tone"
```

**What the plugin does:**
- Runs multi-pass editing, each focused on a different dimension:
  - **Clarity:** Tightens prose (most scientific writing can lose 20–30% of words), removes ambiguity, strengthens quantitative claims
  - **Flow:** Checks logical progression paragraph-by-paragraph, ensures topic sentences carry the narrative, identifies non-sequiturs
  - **Tone:** Calibrates confidence level — assertive but not overclaiming, honest about limitations without undermining the proposal
- **scientific-style** skill continues enforcing nomenclature, citation format, and conventions throughout
- Output: polished draft with tracked changes and explanations

---

**Step 10: Verify format compliance**

```
"Check this proposal against the solicitation requirements — make sure
everything is compliant before submission"
```

**What the plugin does:**
- **format-compliance** skill reads the solicitation (or searches for it by number) and extracts every formatting and structural requirement
- Runs 30+ systematic checks:
  - **Structure:** All required sections present, in correct order, with correct heading names
  - **Length:** Total pages, per-section limits, abstract word count, title character count
  - **Formatting:** Font, margins, spacing, line numbers, headers/footers, page numbers
  - **Citations:** Style consistent, all cross-referenced, no orphaned references, correct format
  - **Figures/tables:** Sequential numbering, all referenced in text, captions complete
  - **Proposal-specific:** Evaluation criteria coverage proportional to weights, milestones quantitative, go/no-go criteria unambiguous, risks identified with mitigations, team qualifications evidenced
- Produces a compliance report with critical vs. minor issues and specific fixes
- Offers to apply automated fixes (citation renumbering, caption reformatting, word count trimming)
- Output: compliance report + fixed document

---

**Step 11: Export to final format**

```
"Convert the proposal to DOCX with the formatting specs from the solicitation"
```

**What the plugin does:**
- **document-formats** skill handles the conversion using Python libraries (python-docx, fpdf2)
- Preserves headings, tables, figures, and formatting
- For DOCX: applies appropriate styles, sets margins/fonts per solicitation specs
- For PDF: generates with correct layout, embedded figures, and formatted tables
- Output: submission-ready file in the required format

---

**At every step**, the auto-activating skills work in the background:
- **scientific-style** enforces nomenclature, statistical reporting, and writing conventions
- **scientific-writing** provides document-type-specific strategic guidance
- **scientific-reading** structures every paper analysis for actionable output
- **paper-retrieval** never gives up on a PDF until all 16 sources are exhausted
- **format-compliance** catches the trivial formatting issues that cause desk rejections

> **Note:** Slash commands (`/sci-search`, `/sci-draft`, etc.) are also available for power users who want direct access to specific capabilities. The walkthrough above uses natural language prompts because the skills trigger automatically — use whichever style you prefer.

## Auto-Activating Skills

These skills trigger automatically when Claude detects relevant context — no slash command needed.

| Skill | Triggers on |
|-------|------------|
| **scientific-style** | Editing `.tex`, `.md`, `.bib`, `.pdf`, `.docx`, `.pptx`, `.xlsx` files with scientific content. Provides tense, voice, nomenclature, statistical reporting, and formatting guidance. |
| **scientific-writing** | Any request to write, draft, or revise scientific documents. Provides strategic framing, audience calibration, and document-type-specific conventions. |
| **scientific-reading** | Any request to read, summarize, or analyze a paper or patent. Provides structured distillation with field-specific evaluation lenses. |
| **paper-retrieval** | Any request to download, fetch, or collect scientific PDFs. Exhaustive 5-tier, 16-source download strategy with auto-categorization into numbered folders and standardized naming (`JournalAbbrev_description_year.pdf`). |
| **pubmed-setup** | Checks PubMed MCP integration status and guides setup. Runs diagnostics across search, metadata, ID conversion, and full-text capabilities. |
| **document-formats** | Reading or writing `.pdf`, `.docx`, `.pptx`, `.xlsx` files. Handles dependency checks, Python-based read/write for all four formats, and format conversion. |
| **format-compliance** | Verifies documents against venue requirements (journal guidelines, solicitation specs, conference rules). Searches for and fetches actual requirements, audits structure/length/citations/formatting, and reports issues with fixes. |

## Document Types Supported

**Writing:** Abstracts (grant, conference, journal) · Government proposals (NIH, NSF, DOE, DARPA, ARPA-E, ARPA-H, BARDA, and others) · Commercial proposals · Technical reports · Literature reviews · White papers · Statements of Work · Progress reports · Patent/invention disclosures · Slide presentations · One-pagers · Internal decision memos · Laboratory protocols and SOPs

**Reading:** Research articles · Review articles · Patents and patent applications · Preprints · Conference proceedings · TEA/LCA studies · Competitive landscape analysis

**Editing:** Clarity and conciseness · Passive voice assessment · Scientific tone · Jargon calibration · Logical flow · Topic sentence strengthening

**Figures & Tables:** Publication-quality captions · Journal-formatted tables (Markdown + LaTeX) · Panel labeling and cross-references

## Installation

Clone the repo and add as a local plugin:

```bash
git clone https://gitlab.com/ginkgobioworks/ai-skills/claude-sciencing.git
```

Then add the path to your Claude Code settings (`.claude/settings.json`):

```json
{
  "plugins": ["path/to/claude-sciencing"]
}
```

### PubMed Integration

The `/sci-search`, `/sci-read`, `/sci-library`, and `/sci-review` commands use PubMed MCP tools for structured literature search, metadata retrieval, and full-text access. PubMed MCP is a Claude.ai managed integration — enable it at [claude.ai/settings/connectors](https://claude.ai/settings/connectors) and it syncs automatically to Claude Code. Without PubMed MCP, the commands fall back to web search — still functional, but with less structured results.

Run the **pubmed-setup** skill to check your integration status and troubleshoot any issues.

### Python Dependencies (for document-formats skill)

The document-formats skill requires Python libraries for Office and PDF file handling:

```bash
pip3 install python-docx python-pptx openpyxl fpdf2
```

The skill checks for missing dependencies automatically and guides installation.

## Field-Specific Evaluation Lenses

The reading and review tools apply domain-specific scrutiny:

- **Strain engineering** — chromosomal vs. plasmid, production-relevant conditions, genetic complexity
- **Catalysis / enzymology** — model vs. real substrate, catalyst loading, stability, mass balance
- **Fermentation** — shake flask vs. bioreactor, titer + yield + productivity, feedstock type
- **TEA / economics** — assumptions, sensitivity analysis, scale, capital inclusion, benchmarks
- **Patents** — claims scope, enablement, design-around opportunities, FTO risk

## Core Principles

- **Data over claims** — specific numbers with units, conditions, and comparisons
- **Audience-calibrated** — same result framed differently for program managers, R&D teams, commercial partners, IP counsel
- **Synthesize, don't summarize** — draw connections, identify consensus, flag contradictions
- **Model vs. real** — always distinguish model substrate from real feedstock results
- **Honest limitations** — credibility through acknowledging what you don't know

## License

MIT
