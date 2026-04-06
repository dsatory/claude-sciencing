---
description: Analyze experimental data — statistics, visualization, and biological interpretation
argument-hint: [data file path or description] [optional: --stats, --viz, --compare, --kinetics, --growth]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch
---

# Experimental Data Analysis

Analyze bench data with appropriate statistics and visualization. The `lab-workflow` skill provides detailed methods in `references/analysis.md`.

## Workflow

1. **Load and inspect data** — read the file, show structure, check for issues
2. **Propose analysis plan** — based on data type and user's question
3. **Execute analysis** — statistics, visualization, and interpretation
4. **Present results** — clear figures, statistical summaries, biological meaning

## Flags

### --stats
Focus on statistical analysis:
- Descriptive statistics (mean, SD, median, range)
- Normality check
- Appropriate hypothesis test
- Effect size and confidence intervals
- Multiple comparison correction if needed

### --viz
Focus on visualization:
- Choose appropriate plot type for the data
- Publication-quality formatting (labeled axes, legends, error bars defined)
- Generate with Python (matplotlib/seaborn) or describe for the user

### --compare
Compare conditions/groups:
- Side-by-side visualization
- Statistical comparison with appropriate test
- Effect size quantification

### --kinetics
Enzyme kinetics analysis:
- Michaelis-Menten fit (Vmax, KM)
- Calculate kcat, kcat/KM
- Lineweaver-Burk plot (for visualization)
- Inhibition analysis if inhibitor data present

### --growth
Growth curve analysis:
- Plot OD600 vs. time (log scale)
- Calculate specific growth rate (µ) and doubling time
- Identify lag, exponential, and stationary phases
- Compare conditions

## Data Type Detection

Automatically detect data type from file contents and suggest appropriate analysis:

| Data pattern | Analysis type |
|-------------|--------------|
| OD600 + time columns | Growth curve analysis |
| Substrate concentration + rate | Enzyme kinetics (Michaelis-Menten) |
| Groups/conditions + continuous measurement | Group comparison (t-test, ANOVA) |
| Dose + response | Dose-response curve (IC50/EC50) |
| Multiple analytes + samples | Heatmap / multivariate |
| Time series + multiple analytes | Fermentation profile |
| 96/384-well format | Plate reader analysis |

## Output Format

```
## Analysis: [Description]

### Data Summary
[Table of descriptive statistics]

### Statistical Analysis
- Test used: [name and justification]
- Result: [test statistic, p-value, effect size]
- Interpretation: [what this means biologically]

### Visualization
[Generated figure or code to generate it]

### Conclusions
- [Key finding 1]
- [Key finding 2]
- [Limitations / caveats]
- [Suggested follow-up experiments]
```

## Code Generation

When writing analysis code:
- Use Python with pandas, scipy, matplotlib, seaborn
- Include comments explaining each step
- Save figures to files with descriptive names
- Print statistical results with full context (test name, n, statistic, p-value, effect size)
- Handle missing data explicitly (report how many, decide strategy)
