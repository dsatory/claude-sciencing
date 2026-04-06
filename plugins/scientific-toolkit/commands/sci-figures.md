---
description: Write figure captions, format tables, and manage panel labeling for scientific publications
argument-hint: [type: caption | table | panels] [file path or description]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write
---

# Figures, Tables, and Captions

Generate publication-quality figure captions, format tables, and manage figure panel descriptions. Parse the first argument from $ARGUMENTS.

## Argument Routing

- **caption** — Write or revise a figure caption
- **table** — Format or create a table for publication
- **panels** — Generate or organize panel descriptions
- If no argument, ask what the user needs

## Mode: Caption

Write publication-quality figure captions following journal conventions.

### Caption Structure

Every figure caption follows this three-part structure:

1. **Title statement:** A single bold sentence describing what the figure shows (not what it means). Begin with "Figure N." Format: "**Figure N. [Descriptive title of what is shown.]**"

2. **Panel-by-panel description:** Describe each panel in order (a, b, c...). State what is plotted or shown, what the axes represent, what conditions are compared. Include units. Define all abbreviations, symbols, colors, and line styles used.

3. **Key finding and statistics:** State the main result the figure demonstrates. Include sample sizes (n), statistical tests used, p-values or confidence intervals, and what error bars represent (SEM, SD, 95% CI). Define significance markers (e.g., "*p < 0.05, **p < 0.01, ***p < 0.001").

### Caption Examples

**Good caption pattern:**
"**Figure 3. Compound X inhibits tumor growth in a dose-dependent manner.** (a) Tumor volume over 21 days in vehicle-treated (black circles) and Compound X-treated mice at 10 mg/kg (blue squares) and 50 mg/kg (red triangles). Data are mean +/- SEM (n = 8 per group). (b) Representative H&E-stained tumor sections at day 21. Scale bar, 100 um. (c) Quantification of Ki-67-positive cells as percentage of total nuclei. Each dot represents one tumor; horizontal lines indicate medians. *p < 0.05, **p < 0.01 by one-way ANOVA with Tukey's post-hoc test."

### Caption Checklist

Before finalizing a caption, verify:
- [ ] Figure title describes what is shown, not what it concludes
- [ ] All panels (a, b, c...) are described
- [ ] Axes labels and units are specified
- [ ] All symbols, colors, and markers are defined
- [ ] Sample sizes stated
- [ ] Statistical test named
- [ ] Error bar type defined
- [ ] Scale bars described (for images)
- [ ] Abbreviations defined at first use within the caption

### Revising Existing Captions

When revising a caption the user has already written:
1. Check against the checklist above
2. Flag missing statistical information
3. Suggest clearer panel descriptions
4. Ensure the title is descriptive but not interpretive
5. Verify consistency between caption and any visible figure content

## Mode: Table

Format tables for journal submission.

### Table Formatting Conventions

- **Title:** Place above the table. "**Table N.** [Descriptive title]."
- **Column headers:** Clear, with units in parentheses
- **Alignment:** Numbers right-aligned or decimal-aligned. Text left-aligned.
- **Horizontal rules:** Use three rules only — top, below headers, bottom. No vertical rules. No internal horizontal rules except to separate major groupings.
- **Footnotes:** Use superscript lowercase letters (a, b, c) for table-specific notes. Place abbreviation definitions and statistical notes below the table.
- **Significant figures:** Use consistent decimal places within each column
- **Missing data:** Use "—" (em dash), not blank cells

### Table Content Guidance

- Present data from most important to least important (left to right)
- Group related variables together
- Include summary statistics (mean, median) as appropriate
- For comparison tables, place the reference/control group first
- Report exact p-values (p = 0.032) rather than thresholds (p < 0.05) when possible

### Markdown Table Generation

When writing tables in Markdown, use standard pipe table syntax:

```markdown
| Variable | Control (n = 24) | Treatment (n = 26) | p-value |
|:---------|------------------:|--------------------:|--------:|
| Age (yr) | 52.3 (8.1)       | 54.1 (7.6)         | 0.42    |
```

### LaTeX Table Generation

When writing tables for LaTeX documents, use the `booktabs` package conventions:

```latex
\begin{table}[ht]
\centering
\caption{Descriptive title.}
\label{tab:results}
\begin{tabular}{lrr}
\toprule
Variable & Control & Treatment \\
\midrule
...
\bottomrule
\end{tabular}
\end{table}
```

Detect whether the user is working in Markdown or LaTeX from the file extension or context, and generate the appropriate format.

## Mode: Panels

Generate and organize figure panel descriptions and labeling.

### Panel Labeling Conventions

- Use lowercase bold letters: **(a)**, **(b)**, **(c)**
- Label panels left to right, top to bottom
- Each panel should be independently interpretable from the caption
- Multi-panel figures should have a unifying theme stated in the title

### Panel Description Template

For each panel, provide:
1. Panel letter and what type of visualization it is (bar chart, micrograph, schematic, etc.)
2. What variables are on each axis or what the image depicts
3. What experimental conditions or groups are shown
4. How groups are visually distinguished (color, symbol, pattern)

### Cross-Reference Suggestions

When working with a multi-figure document:
1. Scan the document for existing figure and table references
2. Suggest cross-references where results in one figure relate to data in another
3. Check for consistency in figure numbering
4. Flag figures mentioned in text but not yet created, or figures that exist but are never referenced
5. For LaTeX documents, verify that `\ref{}` labels match `\label{}` declarations

### Panel Organization Advice

When a user is planning a figure:
- Suggest logical ordering of panels that follows the narrative
- Recommend combining related plots into multi-panel figures rather than separate figures
- Advise on appropriate figure count for the document type (typically 4-6 figures for a full-length paper, 2-3 for a short communication)
- Suggest which data belongs in supplementary figures vs. main figures based on centrality to the main argument

## General Guidance

- Always ask for the target journal if not specified — formatting requirements vary
- Detect file type (.tex, .md, .docx context) and generate appropriate markup
- When the user provides an image path, do not attempt to view the image; instead ask the user to describe the figure content or panel layout
- Maintain consistent terminology between figures, tables, and main text
