# Technical Reports

Technical reports are the most detailed document type in industrial biotech R&D. They serve as the permanent record of what was done, what was found, and what it means. Future team members, partners, and your future self will rely on them.

## When to Write a Technical Report

- After a significant experimental campaign or milestone
- To consolidate knowledge before a pivot or project phase transition
- As a deliverable for a funded program
- To document a technology, process, or capability for internal knowledge management
- As a comprehensive reference for proposal writing (the report feeds abstracts, proposals, and presentations)

## Structure

### Title Page
- Descriptive title (not clever — searchable and specific)
- Authors with affiliations
- Date and version
- Distribution/confidentiality marking
- Program reference if applicable (e.g., "DOE BioEnergy Program, Award #DE-SC0021432")

### Executive Summary (1-2 pages)
- Self-contained summary for readers who won't read the full report
- Problem → approach → key findings → implications
- Include 2-3 headline numbers
- State the main conclusion explicitly — don't make the reader hunt for it

### Table of Contents
- Include for any report >10 pages
- Number sections hierarchically (1, 1.1, 1.2, 2, etc.)
- List tables and figures separately if >5 of each

### 1. Introduction / Background
- Context: why this work matters
- State of the art: what's known, what the gaps are
- Objective: what this report addresses
- Scope: what's included and excluded
- Keep proportional — background should be ≤15% of the report for internal audiences, up to 25% for external

### 2. Materials and Methods
- Sufficient detail for reproduction by a competent scientist
- For established protocols: cite the reference and note any modifications
- For novel methods: full detail including reagents, equipment, conditions
- Organize by experiment type, not chronologically
- Include a process flow diagram if the workflow has >3 steps

**Biotech-specific methods sections should include:**
- Strain construction (parent strain, genetic modifications, selection markers)
- Growth conditions (media composition, temperature, aeration, induction)
- Fermentation parameters (mode, feeding strategy, pH control, dissolved oxygen)
- Analytical methods (HPLC conditions, LC-MS parameters, NMR protocols)
- Statistical treatment (replicates, error calculation, significance tests)

### 3. Results
- Organize by research question or hypothesis, not by experiment number
- Lead each subsection with the finding, then present the supporting data
- Tables and figures carry the primary data; text interprets and contextualizes
- Report negative results — they inform the path forward

**Results writing pattern:**
> [Finding sentence] — what you observed
> [Data sentence] — the specific numbers, referencing a table/figure
> [Context sentence] — how this compares to literature, expectations, or targets
> [Implication sentence] — what this means for the next step or the bigger picture

### 4. Discussion
- Interpret results in context of the literature and project goals
- Compare to published benchmarks with specific numbers
- Discuss unexpected results — propose explanations
- Identify limitations and caveats honestly
- Suggest mechanistic explanations where data supports them
- Connect findings to practical implications (process design, strain engineering targets, etc.)

### 5. Conclusions and Recommendations
- Summarize key findings (3-5 bullet points for a typical report)
- State conclusions firmly — this is not the place for hedging
- Recommend next steps with specificity: what experiments, what timeline, what resources
- For program reports: map findings to milestones and metrics

### 6. References
- Use consistent citation format throughout
- Cite primary sources for specific claims
- Include DOIs for all journal articles
- For internal references: include document numbers and dates

### Appendices
- Raw data tables, supplementary figures, detailed protocols
- Material that supports but doesn't drive the narrative

## Tables and Figures

Tables and figures are not decoration — they are the structural backbone of the report. A reader should be able to understand the key findings by reading only the executive summary and scanning the tables and figures.

### Table Design
- Column headers include units
- Significant figures match measurement precision
- Bold or highlight key values the reader should notice
- Include benchmark/literature comparisons in the same table
- Caption is a complete sentence describing what the table shows

### Figure Design
- Axis labels with units
- Legend inside or adjacent (not requiring page-flipping)
- Error bars with description (SD, SEM, 95% CI) in caption
- Consistent color/symbol coding across related figures
- Caption describes what's shown AND the key takeaway

**Example good caption:**
> **Table 3.** Succinic acid titers from fed-batch fermentation of *E. coli* KJ134 on diverse carbon sources (mineral salts medium, 37°C, pH 7.0, 0.1 vvm CO₂, 72 h). Crude glycerol achieves the highest titer (146 ± 3.2 g/L), consistent with its favorable redox balance for the reductive TCA pathway. Glucose-based titers (98-112 g/L) reflect NADH limitation under anaerobic conditions. Values are mean ± SD of triplicate experiments.

## Tone and Voice

- Active voice dominant, passive acceptable in methods
- Third person for formal reports, first person plural ("we") acceptable for internal
- Confident but precise — state what the data show, not what you hope it shows
- Technical vocabulary without jargon. "Dynamic pathway regulation" is technical vocabulary (precise term for a specific strategy). "Synergistic leveraging of metabolic conversion paradigms" is jargon (vague words that obscure rather than clarify).

---

## Real-World Technical Report Patterns (Sanitized Examples)

### Pattern: State-of-the-Art Comparison Tables

Every technical report in industrial biotech should include at least one comparison table benchmarking your results against published literature. Structure:

```
**Table N.** State of the art in [target compound] production via [approach].

| Catalyst/Strain | Feedstock | Yield | Conditions | Scale | Ref |
|-----------------|-----------|-------|------------|-------|-----|
| Literature baseline 1 | Model substrate | XX% | Lab conditions | Shake flask | [1] |
| Literature baseline 2 | Real feedstock | XX% | Pilot conditions | 5 L bioreactor | [2] |
| **This work** | **Real feedstock** | **XX%** | **Optimized** | **1 kg batch** | — |
```

Bold your own results. Always include: (1) the substrate type (model vs. real), (2) scale, (3) conditions. These three factors determine whether results are truly comparable.

### Pattern: Risk Assessment Matrix

For proposal-supporting reports, include a structured risk table:

```
| Risk | Severity | Likelihood | Mitigation | Evidence |
|------|----------|------------|------------|----------|
| Feedstock variability reduces yield | High | Medium | HTP screening platform enables rapid parameter optimization per feedstock (240 conditions/experiment) | Demonstrated on 50+ feedstock variants [Ref] |
| Catalyst deactivation over time | Medium | Medium | Regeneration protocol restores >95% activity; 20+ recycle demonstrations | Continuous flow stability data (100 h on-stream) [Ref] |
```

The "Evidence" column is what separates credible risk assessment from hand-waving. Every mitigation should cite data.

### Pattern: Hierarchical Section Numbering with Program Alignment

When the report supports a funded program, mirror the program's Focus Area / Task structure:

```
## 4. FA1: [Focus Area 1 Title from Program]

### 4.1 [Subtopic aligned with Task 1.1]
### 4.2 [Subtopic aligned with Task 1.2]

## 5. FA2: [Focus Area 2 Title from Program]

### 5.1 [Subtopic aligned with Task 2.1]
```

This makes it trivial for a program manager to map your report to their tracking system.

### Pattern: Executive Summary with Headline Numbers

The executive summary should contain 2-3 "headline numbers" that a reader remembers even if they read nothing else:

```
## 1. Executive Summary

[Problem in 1-2 sentences, using the program's language]

[Approach in 2-3 sentences]

Key results:
- [Method A] achieves XX% yield from real [feedstock] — a Y-fold improvement 
  over the state of the art
- [Method B] demonstrates Z metric, the highest reported for [compound class]
- Integrated pipeline validated at [scale] across [N] feedstock types
```
