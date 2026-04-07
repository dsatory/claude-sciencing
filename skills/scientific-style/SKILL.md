---
name: scientific-style
description: This skill should be used when the user is writing or editing .tex, .md, .bib, .pdf, .docx, .pptx, or .xlsx files that contain scientific content such as methods sections, citations, figure references, experimental results, or statistical analyses. It auto-activates to provide background guidance on scientific writing best practices for biotech and life sciences documents. Trigger when file content includes patterns like "\cite", "\ref", "Figure", "Table", "p-value", "et al.", "Methods", "Results", "Discussion", section headers typical of scientific papers, or when the user mentions writing a paper, manuscript, protocol, or grant.
version: 1.0.0
---

# Scientific Style Guide

Provide background scientific writing guidance when the user is working on scientific documents. This skill operates passively — apply these principles when assisting with scientific text without requiring explicit invocation.

## When This Skill Applies

Activate when editing or writing files that contain scientific content indicators:
- File extensions: `.tex`, `.md`, `.bib`, `.Rmd`, `.pdf`, `.docx`, `.pptx`, `.xlsx`
- Content patterns: citation commands, figure/table references, statistical values, section headers matching IMRaD structure, reagent or organism names, methodology descriptions

## Core Principles

### Precision Over Elegance

Scientific writing prioritizes accuracy and reproducibility. When choosing between a more elegant phrasing and a more precise one, choose precision. Every claim should be traceable to evidence.

### Active Voice as Default

Use active voice in Introduction and Discussion sections. Active voice clarifies who did what and strengthens arguments.

- Prefer: "We measured cell viability using the MTT assay"
- Over: "Cell viability was measured using the MTT assay"

Exception: passive voice is standard in Methods sections when the actor is irrelevant to reproducibility.

### Tense Conventions

- **Present tense:** Established facts, general truths, and conclusions of the current study ("These results demonstrate that...")
- **Past tense:** Specific actions performed and specific results obtained ("Cells were incubated for 24 h", "Expression levels increased by 40%")
- **Present perfect:** Work leading up to the current study ("Several groups have reported...")

### Hedging Calibration

Match confidence language to evidence strength:
- Strong evidence (direct, replicated): "demonstrates", "establishes", "shows"
- Moderate evidence (single study, indirect): "suggests", "indicates", "is consistent with"
- Preliminary or speculative: "may", "could potentially", "it is possible that"

Avoid double hedging ("it might possibly suggest").

## Formatting Conventions

### Numbers and Units

- Spell out numbers below 10 when not paired with a unit: "three replicates" but "3 mL"
- Use SI units with standard abbreviations; no period after abbreviation (mL, kg, nm)
- Use a space between number and unit: "10 mM", "37 C"
- Report exact p-values to two or three significant figures: "p = 0.032" not "p < 0.05" (except when p < 0.001)

### Abbreviations

- Define at first use in the abstract AND again at first use in the body text
- Do not abbreviate terms used fewer than three times
- Do not begin sentences with abbreviations

### Citations

**Source integrity rule:** Every citation in a generated document must be traceable to a real, verified paper. Prefer papers from the project's `literature/` folder or search results — these are confirmed to exist. Well-known landmark papers and foundational references are acceptable even if not in the search results, but flag them with `<!-- citation: not from search results -->` for user verification. If no verified source supports a claim, insert `[CITATION NEEDED]` — never fabricate a reference.

- When inserting citations, follow the existing citation style in the document
- In author-year styles, use "et al." for three or more authors
- Place citations before punctuation in most styles
- For narrative citations: "Smith et al. (2023) demonstrated..."
- For parenthetical citations: "...as previously reported (Smith et al., 2023)"

### Species and Gene Nomenclature

- Italicize genus and species names: *Escherichia coli*, *Mus musculus*
- After first full mention, abbreviate genus: *E. coli*
- Gene names: italicized (*TP53*, *BRCA1* for human; *Tp53*, *Brca1* for mouse)
- Protein names: roman (non-italic), capitalized (TP53, BRCA1)

## Reporting Guidelines Awareness

When the document describes specific study types, keep these reporting standards in mind:

- **Randomized controlled trials:** CONSORT checklist
- **Observational studies:** STROBE checklist
- **Animal studies:** ARRIVE guidelines (species, strain, sex, age, housing, sample size justification, randomization, blinding, humane endpoints)
- **Systematic reviews:** PRISMA (search strategy, inclusion/exclusion, risk of bias, PICO framework)
- **Diagnostic accuracy:** STARD guidelines

Do not enforce these prescriptively. Instead, note when a study type would benefit from adherence and suggest missing elements.

## Statistical Reporting

When text includes statistical results, verify these elements are present:
- The statistical test used and why it was appropriate
- Sample sizes for each group
- Central tendency (mean or median) and dispersion (SD, SEM, IQR)
- Effect sizes when relevant
- Exact p-values (not just significance thresholds)
- Correction for multiple comparisons if applicable

Flag common issues:
- SEM used to describe variability (SD is more appropriate for describing data spread; SEM is for precision of the mean estimate)
- Parametric tests applied to non-normal or small-sample data without justification
- "Significant" used without specifying statistical vs. biological significance

## References

For detailed reporting guideline checklists, consult `references/guidelines.md`.
