---
description: Read, distill, and extract intelligence from scientific papers, patents, and technical documents
argument-hint: [mode] [file path, DOI, PMID, or URL]. Modes: brief, deep, extract, patent, compare, relevant
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch, mcp__claude_ai_PubMed__search_articles, mcp__claude_ai_PubMed__get_article_metadata, mcp__claude_ai_PubMed__get_full_text_article, mcp__claude_ai_PubMed__find_related_articles
---

# Scientific Reading & Distillation

Analyze scientific papers, patents, and technical documents. Parse $ARGUMENTS for mode and source.

## Argument Routing

- **brief** — Tactical briefing: bottom line, key findings, relevance, action items (~2 min read)
- **deep** — Deep technical analysis: methods scrutiny, data quality, reproducibility assessment
- **extract** — Structured data extraction into comparison tables
- **patent** — Patent claims analysis, FTO assessment support
- **compare** — Side-by-side comparison of 2+ papers or approaches
- **relevant** — Assess relevance of a paper to a specific project or proposal
- If no mode specified, default to **brief**

## Input Handling

The user may provide:
- A file path to a PDF or document → read it
- A DOI → fetch the paper via web
- A PMID → use PubMed tools to fetch metadata and full text if available
- A URL → fetch the content
- Pasted text or abstract → analyze directly
- Multiple sources (for compare mode)

If the source is unclear, ask.

---

## Mode: Brief (Tactical Briefing)

Quick, structured extraction for busy researchers. This is the default mode.

**Output format:**

```
## [Paper title, first author, journal, year]

**Bottom line:** [One sentence — what this paper means for the reader's work]

**Key findings:**
- [Finding 1 with specific numbers]
- [Finding 2 with specific numbers]
- [Finding 3 with specific numbers]

**Methods snapshot:** [Organism/catalyst, substrate, scale, key conditions]

**Relevance:** [How this connects to current work, if context available]

**Limitations:** [What to be cautious about — model vs. real substrate, scale, missing controls]

**Action items:**
- [Cite in X section of Y document]
- [Add to comparison table]
- [Contact authors / monitor / check patent status]
```

### Bottom Line Guidance
The bottom line requires understanding both the paper AND the reader's context. Examples:
- "First demonstration of one-pot enzymatic PET depolymerization + microbial conversion to PHA — directly validates cascade bioprocess approaches."
- "New thermostable ketoreductase with 3× higher activity than LbADH, but only tested on model ketones — worth monitoring, not ready for production."
- "TEA shows bio-succinic acid at $1,086/ton with membrane separation — competitive with petroleum-derived, directly citable for DOE cost projections."

---

## Mode: Deep (Technical Analysis)

Everything in Brief, plus:

### Methods Scrutiny
- Reproduce the experimental logic mentally — given these methods, would you expect these results?
- Identify missing controls
- Assess whether analytical methods are appropriate
- Check if the mass balance closes (unclosed = hidden byproducts or losses)
- Note unusual or non-standard procedures

### Data Quality Assessment
For each key result:
- Number of replicates and error treatment
- Internal consistency (text vs. figures vs. tables)
- Outlier handling
- Appropriate statistical tests
- Whether figures look too clean (suspiciously low scatter)

### Reproducibility Assessment
- Methods detailed enough to reproduce?
- Strains/plasmids/catalysts publicly available?
- Data deposited in repositories?
- Independent reproduction by other groups?

### State-of-the-Art Positioning
- Where does this result sit relative to best published benchmarks?
- Is the improvement meaningful (2× better) or marginal (5%)?
- Are they comparing to the right baselines?

### Critical Assessment Card
```
**Claim validity:**
| Key claim | Evidence strength | Concern |
|-----------|------------------|---------|

**Transferability:** [High/Medium/Low] — [reason]
**Reproducibility:** [High/Medium/Low] — [reason]
**Overall confidence:** [Use with confidence / Use with caveats / Treat as preliminary]
```

---

## Mode: Extract (Structured Data Extraction)

Pull specific numbers into standardized tables. Ask what domain:

### For Catalysis / Enzyme Results
| Enzyme/Catalyst | Substrate | Conditions | Conversion/Yield | Selectivity | kcat or TON | Stability | Scale |

### For Fermentation / Bioproduction
| Organism (strain) | Substrate | Product | Titer (g/L) | Yield (g/g or mol/mol) | Productivity (g/L/h) | Mode | Volume |

### For TEA / Economics
| Process | Scale | MSP | Key cost drivers | Benchmark comparison |

### Standardization Rules
- Convert to common units across studies
- Flag model vs. real substrate prominently
- Mark missing data as "NR" (not reported)
- Add quality flags (★★★ real substrate + bioreactor + replicated; ★★☆ mixed; ★☆☆ model + small scale)

When extracting from multiple papers, produce a single comparison table with all entries.

---

## Mode: Patent

Analyze patent claims and scope.

### Claims Analysis
1. Find independent claims (the broadest scope of protection)
2. Parse each element — assess scope (broad vs. narrow)
3. Map dependent claims (fallback positions)
4. Identify design-around opportunities

### Output Format
```
**Patent:** [Number] | **Assignee:** [Company] | **Status:** [Granted/Pending/Expired]

**Independent Claim 1 — Element Analysis:**
| Element | Scope | Notes |
|---------|-------|-------|

**Design-around opportunities:** [What could be changed to avoid infringement]

**FTO risk:** [High/Medium/Low] — [reason]
```

### For FTO Assessment
Create an element-by-element comparison of your process to the patent's claims. Flag matches, partial matches, and clear non-matches.

---

## Mode: Compare

Side-by-side comparison of 2+ papers, approaches, or methods.

Output a unified comparison table with:
- Common metrics across all papers
- Conditions normalized to comparable basis
- Quality flags for each entry
- Summary of which approach wins on which dimension
- Overall assessment: "Paper A is stronger for X because... Paper B is better for Y because..."

---

## Mode: Relevant

Assess whether a paper matters for a specific project or proposal.

Ask: "What project or proposal should I assess relevance against?"

Then evaluate:
- **Direct relevance:** Does this work on the same problem/organism/method?
- **Benchmarking value:** Does this provide comparison data for proposals or reports?
- **IP implications:** Could this affect freedom-to-operate?
- **Collaboration signal:** Should we contact these authors?
- **Threat assessment:** Does this compete with or undermine our approach?

Output a relevance score (High / Medium / Low / Not relevant) with specific reasoning.

---

## Reading Lenses by Domain

Apply field-specific scrutiny automatically based on the paper's content:

**Strain engineering:** Parent strain industrially relevant? Chromosomal or plasmid? Production-relevant conditions? Genetic complexity?

**Catalysis:** Model compounds or real substrates? Catalyst loading practical? Stability (recycles, time on stream)? Mass balance closed?

**Fermentation:** Shake flask or bioreactor? Titer AND yield AND productivity all reported? pH/DO controlled? Real feedstock?

**Enzymes:** kcat, KM, Ki reported? Thermostability? Cofactor recycling? Substrate scope?

**TEA:** What assumptions drive the model? Sensitivity analysis? What scale? Capital included? Comparison to incumbent?

---

## General Guidance

- Always read the methods section first — it determines whether results mean what authors claim
- Extract specific numbers, never report vague "improved performance"
- Distinguish model compound from real substrate results prominently
- Flag preprints as not yet peer-reviewed
- When given multiple papers, default to a comparison table
- Check supplementary information — it often contains the most important data
