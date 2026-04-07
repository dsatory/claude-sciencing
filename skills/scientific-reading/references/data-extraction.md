# Structured Data Extraction

## Priority Rules

1. **Always specify the substrate type.** Model compound vs. real feedstock is the single most important context for any biotechnology result.
2. **Always include units and conditions.** A yield number without temperature, substrate, and scale is not comparable.
3. **Use "NR" for missing data, never blank cells.** Empty cells are ambiguous; NR is explicit.
4. **Extract from tables and figures, not text.** Text may round or cherry-pick; the raw data is in the figures/tables and SI.
5. **Add quality flags.** A ★★★ result from a bioreactor on real biomass is not the same as a ★☆☆ result from a microplate on pure glucose.

---

Extracting quantitative data from literature into standardized, comparable formats. This is the bridge between reading a paper and using its data — in comparison tables, proposals, TEA models, and experimental planning.

## Extraction Templates by Domain

### Catalysis / Depolymerization Results

| Field | Description | Why it matters |
|-------|-------------|---------------|
| Catalyst | Composition, loading, support | Reproducibility; cost |
| Substrate | Model compound or real biomass (specify!) | Transferability of results |
| Conditions | T, P, time, solvent, atmosphere | Feasibility at scale |
| Conversion | % of substrate consumed | Not the same as yield |
| Yield | Product yield with basis (wt%, mol%) | The headline number |
| Selectivity | Yield / conversion (or product distribution) | Quality of conversion |
| TON / TOF | Turnover number, turnover frequency | Catalyst efficiency |
| Stability | Recycles, time on stream | Practical viability |
| Mass balance | % accounted for | Trustworthiness of yield data |
| Scale | mg, g, kg | Readiness level |

**Example extraction:**

| Parameter | Value | Notes |
|-----------|-------|-------|
| Enzyme | Engineered CalB lipase variant M3 (Novozym 435 scaffold) | 4 mutations in active site lid region |
| Substrate | Waste cooking oil (real feedstock) | Also tested palm, soybean, rapeseed, and olive oils |
| Conditions | 50°C, solvent-free, 1:3 oil:methanol molar ratio, 24 h | Industrially relevant conditions |
| Conversion | 97.2% (waste cooking oil) | Refined oils 95.8-98.4%; crude oils 89.1-93.6% |
| Specific activity | 342 U/mg protein | 8x wild-type CalB (42 U/mg) |
| Stability | 15 recycles (>90% retained activity); 500 h continuous at 50°C | Industrially relevant stability |
| Glycerol purity | >95% | Enables co-product valorization |
| Mass balance | 98.3% accounted | Excellent closure |
| Scale | 2 L stirred-tank reactor | Check methods for mixing details |

### Fermentation / Bioproduction Results

| Field | Description | Why it matters |
|-------|-------------|---------------|
| Organism | Species, strain, genetic modifications | Reproducibility |
| Substrate | Carbon source (model vs. real feedstock) | Transferability |
| Product | Target chemical | — |
| Titer | g/L at harvest | Scale indicator |
| Yield | mol/mol or g/g (specify basis) | Efficiency |
| Productivity | g/L/h | Rate — critical for economics |
| Mode | Batch, fed-batch, continuous, MBR | Comparability |
| Volume | mL (shake flask) vs. L (bioreactor) | Scale readiness |
| Duration | Hours of fermentation | Throughput |
| pH, T, DO | Process conditions | Reproducibility |
| Key genetic modifications | Knockouts, insertions, overexpressions | Engineering complexity |

### Enzyme / Biocatalysis Results

| Field | Description |
|-------|-------------|
| Enzyme | Name, source organism, expression host |
| Substrate | Natural vs. model, concentration range |
| kcat | Turnover rate (s⁻¹) |
| KM | Michaelis constant (mM or μM) |
| kcat/KM | Catalytic efficiency (M⁻¹ s⁻¹) |
| Ki | Inhibition constant (product, substrate, other) |
| pH optimum | And pH range for >80% activity |
| T optimum | And thermostability (Tm, half-life) |
| Cofactors | Required cofactors, recycling demonstrated? |
| Structure | Crystal structure available? Resolution? |
| Conversion | On practical substrates, at practical loadings |

### TEA / Economic Data

| Field | Description |
|-------|-------------|
| Process | What's being modeled |
| Scale | Capacity (tons/day or tons/year) |
| MSP | Minimum Selling Price ($/kg or $/ton) |
| CAPEX | Capital cost estimate |
| OPEX | Operating cost breakdown |
| Key cost drivers | Which parameters dominate |
| Sensitivity | Which assumptions matter most |
| IRR | Internal rate of return assumed |
| Benchmark | Comparison to petroleum-derived equivalent |
| Software | ASPEN, SuperPro, custom model |

---

## Cross-Study Comparison Tables

The most valuable output of data extraction. When building comparison tables across multiple papers:

### Standardization Rules
1. **Convert to common units.** If one paper reports wt% and another mol%, convert to one basis. State which and show your math.
2. **Note substrate differences prominently.** A table comparing model compound results with real biomass results without flagging the difference is misleading.
3. **Include the conditions.** A yield number without temperature, pressure, and time is not comparable.
4. **Flag missing data.** Use "NR" (not reported) rather than leaving cells blank. Empty cells are ambiguous; NR is explicit.
5. **Order meaningfully.** By yield (descending), by chronology, by substrate type — not randomly.
6. **Include your own data** (if available) in the same table for direct comparison.

### Quality Flags

Add a quality/confidence column when appropriate:

| Flag | Meaning |
|------|---------|
| ★★★ | Real biomass, bioreactor scale, replicated, published in peer-reviewed journal |
| ★★☆ | Real biomass but small scale, or large scale but model compounds |
| ★☆☆ | Model compounds, small scale, limited replicates, or preprint |
| ⚠️ | Potential issues (unclosed mass balance, no error bars, contradicts other reports) |

---

## Extraction Workflow

### For a Single Paper
1. Read the abstract for orientation
2. Go straight to methods — understand what was actually done
3. Extract data from results (tables and figures, not just text — text may round or cherry-pick)
4. Check SI for additional data points, conditions, or failed experiments
5. Fill in the appropriate template
6. Note anything missing or ambiguous

### For a Batch of Papers (Literature Review)
1. Define the comparison table columns first (what fields matter for this question?)
2. Extract from each paper using the same template
3. Standardize units and bases
4. Identify outliers and investigate (real improvement, or different conditions/substrate?)
5. Add quality flags
6. Sort and present with narrative commentary

### For Proposal Benchmarking
1. Identify the program metrics (e.g., DOE target: ≥90% theoretical yield, titer ≥50 g/L, productivity ≥1.0 g/L/h)
2. Extract data specifically mapped to those metrics
3. Create a "state of the art vs. program targets" table
4. Identify where your approach meets/exceeds targets and where gaps remain
5. Use this table directly in the proposal's Technical Approach section
