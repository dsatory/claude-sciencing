# Experimental Planning

Designing rigorous experiments with appropriate controls, statistical power, and efficient use of resources.

## Experiment Design Checklist

Every experiment plan should address:

1. **Hypothesis:** What specific claim are you testing?
2. **Variables:**
   - Independent (what you're changing)
   - Dependent (what you're measuring)
   - Controlled (what you're keeping constant)
3. **Controls:**
   - Positive control (known to work — proves the assay is functional)
   - Negative control (known to fail — proves specificity)
   - Vehicle/mock control (carrier without active component)
4. **Replicates:**
   - Biological replicates (independent cultures/preps) — minimum 3
   - Technical replicates (same sample measured multiple times) — 2-3
5. **Sample size / statistical power:** Can you detect a meaningful difference?
6. **Randomization:** Random assignment of samples to conditions, positions, time points
7. **Blinding:** Where possible, blind the person analyzing data to the conditions
8. **Readout:** What are you measuring, how, and when?
9. **Analysis plan:** What statistical test will you use? Decide before collecting data.
10. **Timeline:** What happens on each day?

## Design of Experiments (DOE)

For multi-factor optimization (media components, induction conditions, process parameters):

### When to Use DOE vs. One-Factor-at-a-Time (OFAT)
- **OFAT:** ≤2 factors, or when you need to understand one factor deeply
- **DOE:** ≥3 factors, interactions matter, want to minimize total experiments

### Common DOE Designs

**Full Factorial (2^k)**
- k factors, each at 2 levels (high/low)
- 2^3 = 8 experiments for 3 factors
- Detects all main effects and interactions
- Use when: ≤5 factors, interactions are important

**Fractional Factorial (2^(k-p))**
- Reduces experiments by confounding higher-order interactions
- 2^(6-3) = 8 experiments for 6 factors (instead of 64)
- Use when: screening many factors, willing to sacrifice interaction information

**Plackett-Burman**
- Screening design: identifies important factors from many candidates
- N+1 experiments for N factors (e.g., 12 experiments for 11 factors)
- Use when: >6 factors, need to narrow down before optimization

**Central Composite Design (CCD)**
- Optimization design: finds optimal levels after screening
- Includes center points and axial points
- Use when: 2-5 factors identified as important, want to find optimum

**Definitive Screening Design (DSD)**
- Newer: screens and estimates curvature simultaneously
- 2k+1 experiments for k factors
- Use when: want screening and some optimization in one round

### DOE for Fermentation (Example)
Factors: temperature (25-37°C), IPTG (0.01-1 mM), OD at induction (0.4-1.2)
- Screening: 2^3 full factorial = 8 conditions + 3 center points = 11 shake flasks
- Each in triplicate = 33 flasks (fits in one incubator)
- Readout: soluble protein yield (mg/L) by SDS-PAGE densitometry + activity assay
- Analysis: main effects plot, interaction plot, Pareto chart of effect sizes

## Controls Reference

### Cloning Controls
| Control | Purpose |
|---------|---------|
| Uncut vector | Tests transformation efficiency |
| Cut + religated vector | Tests ligation efficiency |
| Cut vector only (no insert) | Tests background from uncut/self-ligated |
| Water/no DNA | Tests for contamination |
| Known positive plasmid | Validates competent cells are working |

### Expression Controls
| Control | Purpose |
|---------|---------|
| Uninduced culture | Baseline expression / leaky expression |
| Empty vector induced | Host response to inducer |
| Known expressing clone | Validates induction system works |
| Pre-induction sample | Time zero reference |

### Purification Controls
| Control | Purpose |
|---------|---------|
| Load (crude lysate) | Total protein before purification |
| Flow-through | What didn't bind — target should be absent |
| Wash fractions | Are contaminants being removed? |
| Elution fractions | Where is the target? |
| Blank (buffer only) | System peaks, baseline |

### Assay Controls
| Control | Purpose |
|---------|---------|
| No enzyme / no substrate | Baseline signal |
| Known inhibitor + enzyme | Validates assay can detect inhibition |
| Substrate only | Non-enzymatic background reaction |
| Standard curve | Quantification reference |
| Internal standard | Controls for matrix effects (LC-MS) |

## Statistical Planning

### Sample Size Estimation
Before the experiment, estimate the minimum n to detect a meaningful effect:
- What effect size matters? (2-fold change? 20% improvement?)
- What's the expected variability? (use pilot data or literature)
- What significance level? (α = 0.05 standard)
- What power? (β = 0.80 minimum, 0.90 preferred)

### Pre-Registration
For important experiments, document the analysis plan before collecting data:
- Primary endpoint
- Statistical test
- Multiple comparison correction (if applicable)
- Stopping rules (for sequential experiments)
- What constitutes success/failure
