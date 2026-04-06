# Data Analysis

Analyzing experimental data from bench experiments — statistics, visualization, and interpretation.

## Analysis Workflow

### Step 1: Data Inspection
Before any analysis:
- What does the data look like? (Load and preview)
- Any obvious errors, outliers, or missing values?
- What are the units? What's the measurement precision?
- Is this raw data or already processed?

### Step 2: Descriptive Statistics
- Mean, median, standard deviation for each group
- Check for normality (Shapiro-Wilk test, Q-Q plot)
- Identify outliers (>3 SD from mean, or Grubbs' test)

### Step 3: Appropriate Statistical Test

| Comparison | Normal data | Non-normal data |
|-----------|-------------|----------------|
| 2 independent groups | Unpaired t-test | Mann-Whitney U |
| 2 paired groups | Paired t-test | Wilcoxon signed-rank |
| ≥3 independent groups | One-way ANOVA + post-hoc | Kruskal-Wallis + Dunn's |
| ≥3 groups × 2+ factors | Two-way ANOVA | Aligned rank transform |
| Correlation | Pearson r | Spearman ρ |
| Dose-response | Nonlinear regression (4PL) | — |
| Survival/time-to-event | Log-rank test | — |

### Step 4: Visualization
Choose the right plot:
- **Bar chart + individual points:** Small n (≤15 per group), comparing means
- **Box plot:** Medium n, showing distribution
- **Violin plot:** Large n, full distribution shape
- **Scatter plot:** Continuous × continuous, correlation
- **Growth curves:** Time series with error bands (mean ± SD or SEM)
- **Heatmap:** Multi-dimensional data, plate reader results, expression levels
- **Dose-response curve:** IC50/EC50 determination with 4-parameter logistic fit

### Step 5: Interpretation
- State what the data show (not what you hoped they'd show)
- Report effect sizes, not just p-values
- Acknowledge limitations (small n, high variability, confounders)
- Connect to the hypothesis: does this support, refute, or require modification?

## Common Biotech Data Types

### Growth Curves
- **Plot:** OD600 vs. time, log scale on y-axis for exponential phase
- **Calculate:** Specific growth rate (µ = ln(OD2/OD1) / (t2-t1) during exponential phase)
- **Calculate:** Doubling time (td = ln(2) / µ)
- **Compare:** Overlay multiple conditions; use mean ± SD of biological replicates
- **Gotchas:** OD600 is nonlinear above ~0.4 (dilute and re-read); some media absorb at 600 nm

### Fermentation Data
- **Plot:** Titer, biomass, substrate consumption, pH, DO on dual y-axis vs. time
- **Calculate:** Yield (g product / g substrate), Productivity (g/L/h), Specific productivity (g/gDCW/h)
- **Carbon balance:** Does consumed carbon = biomass + product + CO₂ + byproducts?
- **Volumetric vs. specific:** Normalize to biomass for fair comparison between conditions

### SDS-PAGE Densitometry
- **Quantification:** ImageJ band intensity relative to known standards
- **Expression level:** Band intensity relative to total protein (Coomassie staining)
- **Solubility:** Compare pellet and supernatant band intensities
- **Report:** Apparent MW, % soluble, estimated purity

### Enzyme Kinetics
- **Michaelis-Menten:** Plot v₀ vs. [S], fit to v = Vmax·[S]/(KM + [S])
- **Lineweaver-Burk:** 1/v₀ vs. 1/[S] (for visualization, not fitting — use nonlinear regression)
- **Calculate:** kcat = Vmax / [E]total; catalytic efficiency = kcat/KM
- **Inhibition:** Compare kinetics ± inhibitor; determine Ki and inhibition type
- **Report:** kcat ± SE, KM ± SE, kcat/KM, R² of fit, n replicates

### Plate Reader Assays
- **Blank subtraction:** Subtract media-only or buffer-only wells
- **Edge effects:** Outer wells may evaporate faster; consider leaving outer wells empty
- **Standard curve:** Fit 4-parameter logistic (for ELISA) or linear (for colorimetric)
- **Z-factor:** For HTS: Z' = 1 - 3(σp + σn)/(|µp - µn|); Z' > 0.5 is excellent

## Code Generation

When the user provides data files (CSV, Excel, etc.) and requests analysis:

1. **Read the data** and show the first few rows
2. **Propose an analysis plan** based on the data structure and user's question
3. **Write and execute Python code** using pandas, scipy, matplotlib/seaborn
4. **Present results** with clear figures and statistical summaries
5. **Interpret** — state what the analysis means in biological terms

Use Python with:
- `pandas` for data manipulation
- `scipy.stats` for statistical tests
- `matplotlib` / `seaborn` for visualization
- `statsmodels` for regression and ANOVA
- `scikit-learn` for multivariate analysis if needed
