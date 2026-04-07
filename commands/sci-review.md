---
description: Compile, synthesize, and write literature reviews from collected papers — thematic synthesis, state-of-the-art tables, gap analysis
argument-hint: [topic or question] [optional: --papers key1,key2,key3] [optional: --format narrative|table|both]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch, mcp__claude_ai_PubMed__search_articles, mcp__claude_ai_PubMed__get_article_metadata, mcp__claude_ai_PubMed__get_full_text_article, mcp__claude_ai_PubMed__find_related_articles
---

# Literature Review Compilation

Synthesize multiple papers into a cohesive literature review. This command takes a topic or question, draws from the reference library and/or new searches, and produces a thematic synthesis — not a paper-by-paper summary.

## Workflow

### Step 1: Define Scope

Ask the user (if not provided in $ARGUMENTS):
1. **Question or topic** — What is this review answering?
2. **Purpose** — Proposal background? Technical report? Standalone review? Competitive analysis?
3. **Scope** — What's included/excluded? Time range? Specific subtopics?
4. **Paper sources** — Use library (`--papers key1,key2,...`), search for new papers, or both?

### Step 2: Gather Sources

- If `--papers` provided, read those from the reference library
- If not, search PubMed and the web for relevant literature (construct Boolean queries, use MeSH terms, search multiple sources)
- Check if the user has reading notes in `references/notes/` — use those for papers already analyzed
- Target 10-30 papers for a focused review, 30-80 for a comprehensive one

### Step 3: Organize Thematically

**Never organize chronologically or paper-by-paper.** Organize by technical challenge, approach, or question.

Good thematic structure:
```
1. [Technical challenge A]
   - Approach 1: [synthesis across papers]
   - Approach 2: [synthesis across papers]
   - Comparison: [what works better and why]

2. [Technical challenge B]
   ...

3. Gap analysis
4. Implications / recommendations
```

Bad structure:
```
1. Smith et al. 2023 found...
2. Chen et al. 2024 reported...
3. Park et al. 2025 showed...
```

### Step 4: Synthesize

For each theme:
- **Draw connections** across multiple papers
- **Identify consensus** — what do most studies agree on?
- **Flag contradictions** — where do studies disagree, and why?
- **Assess quality** — not all published results are equally reliable
- **Build comparison tables** — the most valuable output

### Step 5: Produce Output

Based on `--format`:

**narrative** — Full prose synthesis with citations
**table** — State-of-the-art comparison tables with commentary
**both** (default) — Narrative synthesis with embedded comparison tables

---

## Output Structure

### For Proposal/Report Background Sections

```markdown
## [Topic]: State of the Art

### [Theme 1: e.g., "Host Organism Selection"]

[2-3 paragraph synthesis drawing on multiple papers]

**Table N.** Comparison of [metric] across reported systems.
| Study | Organism | Substrate | Titer (g/L) | Yield (g/g) | Productivity (g/L/h) | Scale | Notes |
|-------|----------|-----------|-------------|-------------|---------------------|-------|-------|

[Interpretive paragraph: what the table reveals]

### [Theme 2]
...

### Gap Analysis

[What hasn't been done, what's contradictory, where data is weak]

### Implications for This Work

[How the review informs the proposed approach]
```

### For Standalone Literature Reviews

```markdown
# [Review Title]

## 1. Scope and Objective
[What this review covers and why]

## 2. [Theme 1]
[Synthesis with comparison tables]

## 3. [Theme 2]
...

## N. Gap Analysis and Future Directions
[Opportunities, unanswered questions, emerging trends]

## References
[Numbered list]
```

---

## Comparison Table Templates

### Organism/Strain Engineering Comparison
| Study | Host | Modifications | Substrate | Product | Titer | Yield | Productivity | Scale | Feedstock |

### Catalyst/Enzyme Comparison
| Study | Catalyst/Enzyme | Substrate | Conditions | Conversion | Selectivity | Stability | Scale |

### Process/TEA Comparison
| Study | Process | Scale | MSP | Key Cost Drivers | Benchmark |

### General Comparison
| Study | Approach | Key Result | Conditions | Advantages | Limitations |

---

## Synthesis Principles

### Synthesize, Don't Summarize
Every paragraph should make an analytical point supported by multiple citations. Don't describe what each paper found — describe what the body of literature means.

**Summary (weak):** "Wang et al. (2024) achieved 87 g/L itaconic acid. The strain was stable for 120 h."

**Synthesis (strong):** "Fed-batch titers for itaconic acid have converged around 80-90 g/L across multiple engineered hosts (Wang 2024, Kim 2023, Liu 2025), suggesting this range may represent a metabolic ceiling imposed by citrate synthase flux limitations rather than engineering shortcomings. Breaking through this ceiling likely requires rewiring central carbon metabolism upstream of the TCA cycle, an approach only attempted by Park et al. (2025) with mixed results (68 g/L but 40% higher productivity)."

### Be Quantitative
Extract and compare numbers. Convert to common units. Note when direct comparison isn't possible.

### Assess Quality
Not all data are equal:
- Model substrate vs. real feedstock
- Shake flask vs. bioreactor
- n=1 vs. replicated
- Published vs. preprint
- Independently reproduced vs. single-lab

### Citation Integrity

Every citation in the review must be traceable to a verified source:
- **Prefer papers from the reference library** (`references/library.md`) or search results — these are confirmed to exist
- **Well-known landmark papers** (seminal methods, foundational discoveries) are acceptable even if not in the library, but flag them with `<!-- citation: not from search results -->` for user verification
- **NEVER fabricate citations.** If a claim needs a citation and no matching paper exists, insert `[CITATION NEEDED]` rather than inventing an author-year-journal combination
- A review with `[CITATION NEEDED]` placeholders is infinitely more trustworthy than one with hallucinated references

### Data Reliability Flags

When building comparison tables, flag the reliability of each data point:

| Flag | Meaning | How to assess |
|------|---------|---------------|
| Model substrate | Result from purified/synthetic substrate | Check methods section for substrate source |
| Real feedstock | Result from crude/industrial/waste feedstock | More industrially relevant but harder to compare |
| Shake flask | Uncontrolled conditions (pH, DO) | Results may not translate to bioreactor |
| Bioreactor | Controlled fermentation | More reliable for scale-up projections |
| n=1 | Single experiment, no replicates | Treat with caution |
| Preprint | Not peer-reviewed | Flag clearly; check if since published |

Include these flags in comparison tables as a "Notes" or "Quality" column so readers can assess data reliability at a glance.

### Track Currency
In fast-moving fields, 3-year-old reviews are ancient. Note publication dates and flag when recent results overturn earlier conclusions.

---

## Integration with Other Commands

- **/sci-search** finds papers → **/sci-library add** stores them → **/sci-review** synthesizes them
- **/sci-read extract** pulls data from individual papers → **/sci-review** compiles into comparison tables
- **/sci-draft proposal** or **/sci-draft report** uses the review as background sections

When the review is complete, offer to:
- Save as a standalone file
- Insert as a section in an existing document
- Update the reference library with any newly found papers
- Generate a formatted reference list

---

## General Guidance

- A 10-paper review should be 2-4 pages; a 30-paper review 8-15 pages
- Every citation should serve the narrative — don't cite for completeness
- Comparison tables are the single most valuable output; prioritize them
- Always end with gap analysis — this is where the review earns its keep
- For proposal backgrounds, tie the gap analysis directly to your proposed approach
- Apply citation integrity rules: every citation must be verifiable. Use [CITATION NEEDED] rather than fabricating references.
