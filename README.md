# Claude Sciencing v2.5.0

A Claude Code plugin for scientific research in biotech and life sciences — covering the full literature-to-publication lifecycle: search, organize, read, analyze, synthesize, write, edit, and publish. Works on any Claude Code provider (Anthropic, Vertex/GCP, Bedrock).

## Slash Commands

| Command | Description |
|---------|-------------|
| `/sci-search` | Multi-database search (PubMed, OpenAlex, Semantic Scholar, bioRxiv) with 0-10 relevance scoring. Scan internal sources (Slack, Confluence, GDrive, Glean). Patents via Google Patents. Deduplication across databases. |
| `/sci-library` | Manage a local reference library — add papers, tag, organize, export BibTeX/citations. |
| `/sci-read` | Distill papers and patents — tactical briefings, deep analysis, data extraction, patent claims. |
| `/sci-review` | Compile thematic literature reviews with state-of-the-art comparison tables and gap analysis. |
| `/sci-draft` | Draft any scientific document — abstracts, proposals, reports, SOWs, patents, presentations, protocols, memos. |
| `/sci-edit` | Multi-pass scientific editing — grammar, spelling, typos, clarity, tone, jargon, logical flow, topic sentences. Peer review mode for pre-submission self-assessment (journal and grant formats). |
| `/sci-figures` | Write figure captions, format tables, manage panel labeling for publications. |
| `/sci-patents` | Search, analyze, and map patent landscapes — claims extracted directly from Google Patents via WebFetch (no PDF needed). FTO assessment, design-around analysis. |

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
- **Internal discovery runs first** — searches Slack, Confluence, and Google Drive (via Claude.ai connectors) for related past projects, shared papers, FTO analyses, wiki pages, protocols, and reusable assets. Falls back to Glean enterprise search when Claude.ai connectors are unavailable. Surfaces prior proposals, fermentation data, and expert contacts before any external search.
- **scientific-reading** and **pubmed-setup** skills activate — uses PubMed via MCP or NCBI E-utilities API directly (works on any provider including Vertex/GCP)
- Searches across PubMed, preprints (bioRxiv, chemRxiv), and web sources in parallel with **minimum 8 query variations** from a mandatory term expansion table
- Returns results ranked by relevance, recency, and open-access availability
- Patent search runs automatically alongside literature search — claims extracted directly from Google Patents HTML via WebFetch (no PDF download needed)
- Produces a Patent Landscape Summary with claims distillation, project comparison, clear/caution/avoid categories
- Suggests a reading order, identifies gaps in the search, and recommends follow-up queries
- Output: a curated reading list organized by priority (minimum 15-20 papers for an active topic)

---

**Step 3: Download the papers**

```
"Download all open-access PDFs from that search"
```

**What the plugin does:**
- **paper-retrieval** skill activates with its exhaustive 7-tier, 20-source strategy
- **Tier 0:** Resolves all identifiers (DOI → PMID → PMCID) via PubMed MCP or NCBI E-utilities API. Checks OA status for every paper upfront.
- **PMC full-text XML (primary paper access):** For papers with PMCIDs, fetches full article text as structured XML via `efetch` — returns complete body text, sections, figures, and tables for OA journals (MDPI, Frontiers, PLOS, BMC, Nature OA). More reliable than PDF download, and the structured format is better for analysis. Papers from non-OA publishers (ASM, Springer, Elsevier) return abstract only via this method.
- **Fast pass (Tiers 1–2):** MDPI direct PDFs, publisher OA, Unpaywall, and Europe PMC — handles the easy ones first
- **Patents:** Claims are extracted directly from Google Patents HTML pages via WebFetch — no PDF download required. Full claim text, metadata, assignee, dates, and status are parsed in a single call. PDF download is only triggered when the user explicitly requests it or when specification/figure analysis is needed. Patent data sorted to a dedicated `XX_Patents/` folder
- **Stubborn pass (Tiers 3–6):** For remaining papers, searches institutional repositories, author websites, preprint servers, internal sources (Slack channels, Google Drive), and creative web queries — tries at least 10 sources per paper before giving up
- **Browser-assisted fallback:** For papers that resist all automated methods, opens URLs in the user's browser for manual download through institutional access, then scans the downloads folder to rename and sort the files
- **Verifies every download** — checks for HTML masquerading as PDF, stub files, and corrupted downloads
- **Names files** in standardized format: `JournalAbbrev_3word_description_year.pdf` (with patent prefixes `USPat_`, `USApp_`, `EPPat_`, `WOApp_` for patents)
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
- Generates BibTeX entries and adds to `references/library.bib` (for LaTeX) and `references/library.md` (for browsing)
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
- Output: polished draft with applied edits or edit suggestions, plus explanations

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
- Offers to apply straightforward fixes (citation renumbering, caption reformatting, word count trimming) where the source format supports direct editing
- Output: compliance report + optional direct edits for straightforward issues

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
- **paper-retrieval** never gives up on a PDF until all 20 sources are exhausted
- **format-compliance** catches the trivial formatting issues that cause desk rejections

> **Note:** Slash commands (`/sci-search`, `/sci-draft`, etc.) are also available for power users who want direct access to specific capabilities. The walkthrough above uses natural language prompts because the skills trigger automatically — use whichever style you prefer.

## Auto-Activating Skills

These skills trigger automatically when Claude detects relevant context — no slash command needed.

| Skill | Triggers on |
|-------|------------|
| **scientific-style** | Editing `.tex`, `.md`, `.bib`, `.pdf`, `.docx`, `.pptx`, `.xlsx` files with scientific content. Provides tense, voice, nomenclature, statistical reporting, and formatting guidance. |
| **scientific-writing** | Any request to write, draft, or revise scientific documents. Provides strategic framing, audience calibration, and document-type-specific conventions. |
| **scientific-reading** | Any request to read, summarize, or analyze a paper or patent. Provides structured distillation with field-specific evaluation lenses. |
| **paper-retrieval** | Any request to download, fetch, or collect scientific papers. PMC full-text XML via efetch for OA papers (no PDF needed). Exhaustive 7-tier, 20-source strategy for PDFs. Patent claims extracted via WebFetch from Google Patents HTML. Internal Slack/GDrive sources, browser-assisted fallback with user confirmation. Download-before-write gate blocks premature writing. Auto-categorization into numbered folders with dedicated `XX_Patents/` folder and standardized naming (`JournalAbbrev_3word_description_year.pdf`). |
| **pubmed-setup** | Checks PubMed access — tests MCP first, falls back to NCBI E-utilities API (works on any provider). Runs diagnostics across search, metadata, ID conversion, and full-text capabilities. Guides setup for both methods. |
| **document-formats** | Reading or writing `.pdf`, `.docx`, `.pptx`, `.xlsx` files, and Google Drive native files (`.gdoc`, `.gsheet`, `.gslides`). Handles dependency checks, Python-based read/write for all four Office formats, GDrive export via browser, and format conversion. |
| **format-compliance** | Verifies documents against venue requirements (journal guidelines, solicitation specs, conference rules). Searches for and fetches actual requirements, audits structure/length/citations/formatting, and reports issues with fixes. |

## Document Types Supported

**Writing:** Abstracts (grant, conference, journal) · Government proposals (NIH, NSF, DOE, DARPA, ARPA-E, ARPA-H, BARDA, and others) · Commercial proposals · Technical reports · Literature reviews · White papers · Statements of Work · Progress reports · Patent/invention disclosures · Slide presentations · One-pagers · Internal decision memos · Laboratory protocols and SOPs

**Reading:** Research articles · Review articles · Patents and patent applications · Preprints · Conference proceedings · TEA/LCA studies · Competitive landscape analysis

**Editing:** Grammar, spelling, and typos · Clarity and conciseness · Passive voice assessment · Scientific tone · Jargon calibration · Logical flow · Topic sentence strengthening

**Figures & Tables:** Publication-quality captions · Journal-formatted tables (Markdown + LaTeX) · Panel labeling and cross-references

## Installation

Clone the repo and add as a local plugin:

```bash
git clone https://github.com/dsatory/claude-sciencing.git
```

**Option B: From Archive (without git access)**

If you have a zip/tar archive of the plugin instead of git access:

```bash
# Unzip to a permanent location
unzip claude-sciencing.zip -d ~/.claude/plugins/claude-sciencing

# Or for tar.gz
tar -xzf claude-sciencing.tar.gz -C ~/.claude/plugins/
```

Then add the path to your Claude Code settings (`.claude/settings.json`):

```json
{
  "plugins": ["path/to/claude-sciencing"]
}
```

Validate the checkout after changes:

```bash
python3 scripts/validate_plugin.py
python3 scripts/validate_plugin.py --check-endpoints
```

### Multi-Database Search

The plugin searches across **4 scientific databases** simultaneously, deduplicates results, and scores every paper on a 0-10 relevance scale:

| Database | Coverage | Auth Required? | What It Adds |
|----------|----------|---------------|-------------|
| **PubMed** | Biomedical, life sciences | No (E-utilities) or Claude.ai MCP | MeSH terms, structured metadata |
| **OpenAlex** | All disciplines (250M+ works) | No | Citation counts, OA URLs, affiliations |
| **Semantic Scholar** | All disciplines (AI-powered) | No (1 req/sec) | Semantic matching, OA PDF URLs |
| **bioRxiv/medRxiv** | Preprints | No (API or web) | Pre-peer-review papers |

A search on an active topic typically yields **25-50 unique papers** after deduplication across databases.

### Bundled MCP Servers

The plugin bundles three remote MCP servers that auto-install — no local setup needed:

| Server | Provider | What It Provides |
|--------|----------|-----------------|
| **PubMed** | U.S. NLM | Structured literature search, metadata, full text |
| **bioRxiv** | deepsense.ai | bioRxiv and medRxiv preprint access |
| **Scholar Gateway** | Wiley | Access to Wiley academic publications |

These are free, public HTTP endpoints that work on any provider (Anthropic, Vertex, Bedrock). They complement the built-in E-utilities and OpenAlex/Semantic Scholar API calls.

**Additional MCP servers available from the [Anthropic Life Sciences marketplace](https://github.com/anthropics/life-sciences):**

```
/plugin marketplace add anthropics/life-sciences
```

This marketplace offers: 10x Genomics, BioRender, Synapse.org, ChEMBL, Open Targets, Clinical Trials, and more.

### PubMed Integration Details

The plugin searches PubMed for structured literature discovery, metadata retrieval, ID conversion, and full-text access. **Two access methods are supported** — the plugin auto-detects which is available and uses the best option.

#### Method 1: PubMed MCP (Claude.ai accounts only)

PubMed MCP is a Claude.ai managed integration with convenience wrappers around the NCBI API.

- **Works when:** Claude Code runs via an Anthropic account (direct API key or Claude.ai login)
- **Does NOT work when:** Claude Code runs via Vertex (GCP), AWS Bedrock, or any third-party provider — the MCP integration requires a Claude.ai account session that doesn't exist on these providers
- **Setup:** Enable at [claude.ai/settings/connectors](https://claude.ai/settings/connectors). Syncs automatically to Claude Code.

#### Method 2: NCBI E-utilities API (works everywhere)

Direct HTTP calls to NCBI's public PubMed API. **No authentication required.** Works on any provider (Vertex, Bedrock, Anthropic, local). Accesses the same database as PubMed MCP — identical results.

- **No setup required** — the plugin calls the API directly via `WebFetch`
- **Endpoints used:**
  - `esearch` — search PubMed, returns PMIDs
  - `efetch` — fetch article metadata (title, authors, journal, DOI, abstract)
  - `idconv` — convert between PMID, DOI, and PMCID (identifies free PMC papers)
  - `elink` — find related articles
- **Rate limits:** 3 requests/sec (no key) or 10/sec (free API key from [NCBI account settings](https://www.ncbi.nlm.nih.gov/account/settings/))
- **Full API documentation:** `skills/pubmed-setup/references/eutils-api.md`

#### How the plugin chooses

On every `/sci-search`, the plugin runs a **Pre-Flight PubMed health check**:

1. Tests PubMed MCP with a simple query
2. If MCP works → uses MCP (more convenient)
3. If MCP fails → **tells the user why** (expired token, Vertex provider, etc.), then switches to E-utilities API automatically
4. Never silently degrades to generic web search

Run the **pubmed-setup** skill to check your integration status, test both methods, and troubleshoot issues.

### Internal Discovery — Slack / Confluence / Google Drive / Glean

The plugin's internal discovery (Step 0 of `/sci-search`) searches organizational sources for related prior work before external literature search. This surfaces prior proposals, shared papers, FTO analyses, protocols, project documentation, fermentation data, and expert contacts.

#### Slack (primary — via Claude.ai connector)

Uses Claude.ai managed MCP (`mcp__claude_ai_Slack__*`). Enable at [claude.ai/settings/connectors](https://claude.ai/settings/connectors). Works automatically with Anthropic accounts. Searches messages, threads, and file attachments across all channels.

#### Confluence (primary — via Claude.ai Atlassian connector)

Uses Claude.ai managed MCP (`mcp__claude_ai_Atlassian__*`). Enable at [claude.ai/settings/connectors](https://claude.ai/settings/connectors). Searches wiki pages, project documentation, protocols, SOPs, meeting notes, technical reports, and proposals using CQL queries. Can read full page content and navigate page hierarchies.

**Limitation (Slack + Confluence):** These Claude.ai managed integrations do not work on Vertex/GCP or other third-party providers. If unavailable, the plugin prompts the user to set up Glean as a fallback.

#### Google Drive (always works)

Searched via local filesystem (`~/Library/CloudStorage/GoogleDrive-*/`). Requires Google Drive for Desktop to be installed and syncing. Works on any provider — no MCP needed.

#### Glean Enterprise Search (optional environment-specific fallback)

If your organization uses [Glean](https://www.glean.com/), it can serve as an optional fallback for internal discovery when Slack/Confluence MCP is unavailable (for example on Vertex/GCP). Glean indexes Slack, Google Drive, Confluence, Jira, and email in a single unified search.

Add to your global `~/.claude/.mcp.json`:

```json
{
  "mcpServers": {
    "glean-mcp": {
      "url": "https://YOUR-ORG.glean.com/mcp/default"
    }
  }
}
```

Restart Claude Code after adding. Treat this as optional environment configuration rather than a guaranteed bundled integration.

### Python Dependencies (for document-formats skill)

The document-formats skill requires Python libraries for Office and PDF file handling:

```bash
pip3 install python-docx python-pptx openpyxl fpdf2
```

The skill checks for missing dependencies automatically and guides installation. Note: the pip package is `fpdf2` but the Python import is `from fpdf import FPDF`.

**Optional dependencies (enhance capabilities but not required):**

```bash
pip3 install docling      # 97.9% accuracy on scientific table extraction (IBM)
pip3 install paper-qa     # PaperQA2 — superhuman literature search (FutureHouse)
```

- **Docling:** Used by the document-formats skill for high-fidelity table extraction from PDFs. When installed, comparison table data extraction improves significantly over the default PDF reader.
- **PaperQA2:** Standalone agentic RAG for deep literature Q&A. Point it at your `literature/PDFs/` folder for precise, citation-grounded answers with page-level references. See `skills/pubmed-setup/SKILL.md` for integration guide.

### Repository Validation

Run the validation script after editing manifests or docs:

```bash
python3 scripts/validate_plugin.py
```

Add `--check-endpoints` to probe any MCP endpoints declared in `.claude-plugin/plugin.json`.

## Field-Specific Evaluation Lenses

The reading and review tools apply domain-specific scrutiny:

- **Strain engineering** — chromosomal vs. plasmid, production-relevant conditions, genetic complexity
- **Catalysis / enzymology** — model vs. real substrate, catalyst loading, stability, mass balance
- **Fermentation** — shake flask vs. bioreactor, titer + yield + productivity, feedstock type
- **TEA / economics** — assumptions, sensitivity analysis, scale, capital inclusion, benchmarks
- **Patents** — claims scope, enablement, design-around opportunities, FTO risk

## Quality Gates

The plugin enforces hard checkpoints to prevent shallow output — the kind where search results go straight to writing without anyone reading the actual papers.

### Search Enforcement

`/sci-search` requires a **mandatory term expansion table** before any search is executed. Minimum 8 distinct queries across 3+ concept axes with synonyms, searched across 4 databases (PubMed, OpenAlex, Semantic Scholar, bioRxiv) with deduplication. Every paper is scored 0-10 on keyword relevance (40%), recency (25%), citation impact (20%), and open access availability (15%). Minimum 25 unique papers expected for an active topic — fewer triggers a warning to broaden queries.

After initial results, an **iterative refinement loop** (inspired by PaperQA2) identifies coverage gaps, temporal gaps, missing authors, and citation network gaps — then generates targeted follow-up queries. Contextual re-ranking uses the LLM to re-score all papers in the context of the user's specific question, catching semantically relevant papers that keyword scoring misses.

### Download-Before-Write Gate

`/sci-review` and `/sci-draft` check the project's `literature/PDFs/` folder before writing:

- **0-2 verified sources:** STOP — refuses to write, tells user to download papers first
- **3-5 verified sources:** WARN — proceeds only with user confirmation, marks coverage as thin
- **6+ verified sources:** Proceed normally

### Citation Integrity — Three Tiers

Every citation in generated documents is labeled by verification level:

| Tier | Label | Meaning |
|------|-------|---------|
| **Verified** | (none) | PDF downloaded and read. Full confidence. |
| **Unverified** | `[NOT IN LIBRARY]` | Identified in search but not downloaded. Abstract-level claims only. |
| **Needed** | `[CITATION NEEDED]` | Claim needs a source but none found. Never fabricated. |

Documents separate verified and unverified references into distinct sections so the evidence basis is transparent.

### Retraction Checking

Before finalizing any document, every cited paper is checked for retraction status via the CrossRef API (`update-to` field). Retracted papers are removed from citations and flagged to the user with the retraction reason.

### Evidence Mapping

`/sci-review` builds an **evidence map** before writing — a table linking each claim to its supporting and contradicting sources, with specific page/figure references and confidence ratings. Claims with no supporting sources are marked `[GAP]`. The review narrative is written from the evidence map, not the other way around.

### Post-Draft Citation Pass

After drafting any document, a **two-phase citation sweep** (inspired by AI Scientist) identifies uncited claims, generates targeted search queries, searches the appropriate database, and inserts citations. This typically adds 5-15 citations missed during initial writing.

### Novelty Checking

For proposals and invention disclosures, a **novelty check** extracts the core claims, searches PubMed/OpenAlex/Google Patents for the closest prior work, and presents the findings so the user can assess differentiation before submission.

### Ensemble & Adversarial Peer Review

`/sci-edit review` supports two review modes:
- **Ensemble mode** (inspired by AI Scientist): 3 independent reviews (critical, constructive, domain expert) aggregated into a meta-review
- **Adversarial mode** (inspired by IdeaForge): Critic attacks → Proposer defends/revises → Judge evaluates, iterating until all issues are resolved. More thorough because it forces explicit defense of every claim.

### Citation Claim-Source Alignment

Beyond checking if citations exist, every citation is classified on a 4-level scale (inspired by SemanticCite): **Supported** (source fully validates claim), **Partially Supported** (evidence but missing context), **Unsupported** (source contradicts claim), **Uncertain** (needs verification). This catches the common failure where a real paper is cited but doesn't support the specific claim.

### Biological Entity Verification

The scientific-style skill verifies genes, proteins, enzymes, pathways, and organisms against authoritative databases (NCBI Gene, UniProt, KEGG) — catching nomenclature errors that formatting checks miss (e.g., deprecated gene symbols, wrong-organism gene names, incorrect EC numbers).

### Section-by-Section Drafting

`/sci-draft` writes proposals and reports **one section at a time** with plan-draft-refine cycles for each section, rather than generating the entire document in one pass. This produces higher quality output with better section-to-section flow.

### LaTeX Output

The document-formats skill supports **LaTeX generation** with conference-specific templates (ICLR, NeurIPS, ACS, Nature, IEEE) and BibTeX citation management. Includes compile sequence for PDF generation.

### Reading Integrity

`/sci-read` will NOT produce deep technical analyses or data extraction tables from papers it hasn't actually read. If only an abstract is available, the output is labeled **"Source: abstract only — full text not available"** and deep analysis modes are blocked.

### Browser Download Workflow

When automated PDF downloads fail and papers are opened in the browser for manual download, the plugin **waits for user confirmation** before proceeding. After confirmation, it scans `~/Downloads` for new PDFs, verifies them, renames per convention, and sorts into the library. It does not assume downloads succeeded.

### PubMed Degradation Transparency

If PubMed MCP is unavailable, the plugin **tells the user immediately** with the specific error, offers re-authorization instructions, and switches to NCBI E-utilities API. It never silently falls back to generic web search.

## Core Principles

- **Data over claims** — specific numbers with units, conditions, and comparisons
- **Audience-calibrated** — same result framed differently for program managers, R&D teams, commercial partners, IP counsel
- **Synthesize, don't summarize** — draw connections, identify consensus, flag contradictions
- **Model vs. real** — always distinguish model substrate from real feedstock results
- **Honest limitations** — credibility through acknowledging what you don't know
- **Citation integrity** — every citation must trace to a verified source. Three-tier labeling (verified / `[NOT IN LIBRARY]` / `[CITATION NEEDED]`) makes the evidence basis explicit. Never fabricate citations.
- **Patent-aware by default** — every literature search includes patent landscape analysis with claims distillation, project comparison, and feasibility assessment
- **Download before write** — never produce reviews or proposals from web search snippets. Build the PDF library first, read the papers, then write.

## License

MIT
