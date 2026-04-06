# Claude Sciencing

A Claude Code plugin for scientific research in biotech and life sciences — covering the full literature-to-publication lifecycle: search, organize, read, analyze, synthesize, write, edit, and publish.

## Slash Commands

| Command | Description |
|---------|-------------|
| `/sci-search` | Search PubMed, preprints, and patents. Build reading lists. Map research landscapes. |
| `/sci-library` | Manage a local reference library — add papers, tag, organize, export BibTeX/citations. |
| `/sci-read` | Distill papers and patents — tactical briefings, deep analysis, data extraction, patent claims. |
| `/sci-review` | Compile thematic literature reviews with state-of-the-art comparison tables and gap analysis. |
| `/sci-draft` | Draft any scientific document — abstracts, proposals, reports, SOWs, patents, presentations, memos. |
| `/sci-edit` | Multi-pass scientific editing — clarity, tone, jargon, logical flow, topic sentence analysis. |
| `/sci-figures` | Write figure captions, format tables, manage panel labeling for publications. |

### Workflow Example

```
/sci-search engineered bacteria for succinic acid     → Find relevant papers
/sci-library add 10.1016/j.ymben.2024.01.005         → Add to your library
/sci-read deep path/to/paper.pdf                      → Deep technical analysis
/sci-review "host selection for organic acid production" → Synthesize into review
/sci-draft proposal                                    → Draft the proposal section
/sci-edit path/to/draft.md clarity                     → Polish the writing
/sci-figures caption                                   → Write figure captions
```

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

**Writing:** Abstracts (grant, conference, journal) · Government proposals (DARPA, DOE, ARPA-E, NIH, BARDA) · Commercial proposals · Technical reports · Literature reviews · White papers · Statements of Work · Progress reports · Patent/invention disclosures · Slide presentations · One-pagers · Internal decision memos · Protocols

**Reading:** Research articles · Review articles · Patents and patent applications · Preprints · Conference proceedings · TEA/LCA studies · Competitive landscape analysis

**Editing:** Clarity and conciseness · Passive voice assessment · Scientific tone · Jargon calibration · Logical flow · Topic sentence strengthening

**Figures & Tables:** Publication-quality captions · Journal-formatted tables (Markdown + LaTeX) · Panel labeling and cross-references

## Installation

Clone the repo and add as a local plugin:

```bash
git clone https://github.com/dsatory/claude-sciencing.git
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
