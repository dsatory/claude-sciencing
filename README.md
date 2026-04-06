# Claude Sciencing

A Claude Code plugin for scientific research in biotech and life sciences — covering the full research lifecycle from literature search through wet lab work to publication.

## Slash Commands

### Literature & Writing (`sci-*`)

| Command | Description |
|---------|-------------|
| `/sci-search` | Search PubMed, preprints, and patents. Build reading lists. Map research landscapes. |
| `/sci-library` | Manage a local reference library — add papers, tag, organize, export BibTeX/citations. |
| `/sci-read` | Distill papers and patents — tactical briefings, deep analysis, data extraction, patent claims. |
| `/sci-review` | Compile thematic literature reviews with state-of-the-art comparison tables and gap analysis. |
| `/sci-draft` | Draft any scientific document — abstracts, proposals, reports, SOWs, patents, presentations, memos. |
| `/sci-edit` | Multi-pass scientific editing — clarity, tone, jargon, logical flow, topic sentence analysis. |
| `/sci-figures` | Write figure captions, format tables, manage panel labeling for publications. |

### Lab & Experimental (`lab-*`)

| Command | Description |
|---------|-------------|
| `/lab-ideate` | Brainstorm experimental approaches — generate, evaluate, and prioritize strategies. |
| `/lab-plan` | Design rigorous experiments — controls, replicates, DOE, statistical power, timelines. |
| `/lab-protocol` | Generate detailed bench-ready protocols with reagent calculations and practical notes. |
| `/lab-troubleshoot` | Diagnose failed experiments — ranked root causes with diagnostic experiments. |
| `/lab-analyze` | Analyze experimental data — statistics, visualization, and biological interpretation. |
| `/lab-qc` | Generate QC checklists with acceptance criteria for purification, assays, and processes. |
| `/lab-notebook` | Format lab notebook entries for reproducibility and IP protection. |

### Workflow Examples

```
# Literature workflow
/sci-search engineered bacteria for succinic acid     → Find relevant papers
/sci-library add 10.1016/j.ymben.2024.01.005         → Add to your library
/sci-read deep path/to/paper.pdf                      → Deep technical analysis
/sci-review "host selection for organic acid production" → Synthesize into review

# Lab workflow
/lab-ideate improving recombinant protein yield in E. coli
/lab-plan expression optimization --doe
/lab-protocol Gibson assembly --scale 10 reactions
/lab-troubleshoot no colonies after transformation, cloning
/lab-analyze fermentation_data.csv --stats --viz
/lab-qc post-IMAC
/lab-notebook --ip

# Writing workflow
/sci-draft proposal                                    → Draft the proposal section
/sci-edit path/to/draft.md clarity                     → Polish the writing
/sci-figures caption                                   → Write figure captions
```

## Auto-Activating Skills

These skills trigger automatically when Claude detects relevant context — no slash command needed. You can just describe what you need and the right skill activates.

| Skill | Triggers on |
|-------|------------|
| **scientific-style** | Editing `.tex`, `.md`, `.bib` files with scientific content. Provides tense, voice, nomenclature, statistical reporting, and formatting guidance. |
| **scientific-writing** | Any request to write, draft, or revise scientific documents. Provides strategic framing, audience calibration, and document-type-specific conventions. |
| **scientific-reading** | Any request to read, summarize, or analyze a paper or patent. Provides structured distillation with field-specific evaluation lenses. |
| **lab-workflow** | Any discussion of experimental design, protocols, troubleshooting, data analysis, or hands-on lab work. Covers molecular biology, fermentation, protein science, and analytical chemistry. |

## What's Covered

**Literature:** Search (PubMed, web, patents) · Reference management · Paper distillation · Thematic review synthesis · Competitive intelligence

**Writing:** Abstracts (grant, conference, journal) · Government proposals (DARPA, DOE, ARPA-E, NIH) · Commercial proposals · Technical reports · Literature reviews · White papers · SOWs · Progress reports · Patent disclosures · Presentations · One-pagers · Memos · Protocols

**Lab — Molecular Biology:** Cloning (Gibson, Golden Gate, Gateway) · PCR · Mutagenesis · Transformation · Sequencing prep

**Lab — Microbiology & Fermentation:** Strain construction · Growth characterization · Shake flask optimization · Bioreactor operation · ALE · Contamination

**Lab — Protein Science:** Expression optimization · Lysis · Chromatography (IMAC, IEX, SEC) · SDS-PAGE · Activity assays · Protein engineering

**Lab — Analytical:** HPLC/UPLC · LC-MS · Plate reader assays · Spectrophotometry

**Editing:** Clarity · Passive voice · Scientific tone · Jargon calibration · Logical flow · Topic sentences

**Figures & Tables:** Publication-quality captions · Journal-formatted tables · Panel labeling

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

### Optional: PubMed Integration

The `/sci-search`, `/sci-read`, `/sci-library`, and `/sci-review` commands can use PubMed MCP tools for structured literature search, metadata retrieval, and full-text access. If you have the PubMed MCP server configured in Claude, these tools are used automatically. Without PubMed MCP, the commands fall back to web search — still functional, but with less structured results.

## Core Principles

- **Data over claims** — specific numbers with units, conditions, and comparisons
- **Practical over theoretical** — bench-ready protocols, not textbook summaries
- **Quick wins first** — try the 30-minute experiment before the 3-week one
- **Controls are non-negotiable** — every experiment needs positive, negative, and vehicle controls
- **Model vs. real** — always distinguish model substrate from real feedstock results
- **Honest limitations** — credibility through acknowledging what you don't know

## License

MIT
