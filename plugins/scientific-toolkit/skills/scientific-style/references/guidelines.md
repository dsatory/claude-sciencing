# Reporting Guideline Checklists

Quick-reference checklists for common study types in biotech and life sciences.

## CONSORT — Randomized Controlled Trials

- [ ] Trial design described (parallel, crossover, factorial)
- [ ] Eligibility criteria for participants
- [ ] Interventions described with enough detail for replication
- [ ] Primary and secondary outcomes defined a priori
- [ ] Sample size calculation with assumptions
- [ ] Randomization method (sequence generation, allocation concealment)
- [ ] Blinding: who was blinded (participants, investigators, assessors)
- [ ] Participant flow diagram (enrollment, allocation, follow-up, analysis)
- [ ] Baseline demographic and clinical characteristics table
- [ ] Intention-to-treat analysis stated
- [ ] Effect size with confidence interval for primary outcome
- [ ] Adverse events reported
- [ ] Trial registration number and protocol access

## ARRIVE 2.0 — Animal Research

Essential items:
- [ ] Species, strain, sex, age/weight, source
- [ ] Number of animals per group with sample size justification
- [ ] Housing and husbandry conditions
- [ ] Experimental procedures in sufficient detail for replication
- [ ] Randomization method for group allocation
- [ ] Blinding during conduct and assessment
- [ ] Outcome measures defined
- [ ] Statistical methods with unit of analysis
- [ ] Results for each outcome with effect size and precision
- [ ] Adverse events, unexpected findings, humane endpoints applied

Recommended items:
- [ ] Inclusion/exclusion criteria and number excluded
- [ ] Acclimatization period
- [ ] Welfare assessments performed
- [ ] Baseline characteristics of animals
- [ ] Protocol registration

## STROBE — Observational Studies

- [ ] Study design stated (cohort, case-control, cross-sectional)
- [ ] Setting and locations described
- [ ] Eligibility criteria and sources of participants
- [ ] Variables defined: exposures, outcomes, confounders
- [ ] Data sources and measurement methods
- [ ] Bias: efforts to address sources of bias
- [ ] Study size: how determined, power calculation if applicable
- [ ] Statistical methods including confounding control
- [ ] Participant flow: numbers at each stage
- [ ] Descriptive data: demographics, exposures, follow-up time
- [ ] Main results: unadjusted and adjusted estimates with precision
- [ ] Subgroup and interaction analyses
- [ ] Limitations discussed including bias direction

## PRISMA — Systematic Reviews

- [ ] Structured summary (abstract) with PICO
- [ ] Protocol registration (PROSPERO or equivalent)
- [ ] Eligibility criteria with PICO framework
- [ ] Information sources: databases, date ranges, language limits
- [ ] Search strategy: full electronic search for at least one database
- [ ] Study selection process (independent reviewers, consensus)
- [ ] Data extraction process
- [ ] Risk of bias assessment tool named
- [ ] Synthesis methods: meta-analysis approach if used
- [ ] Results of search: PRISMA flow diagram
- [ ] Study characteristics table
- [ ] Risk of bias across studies
- [ ] Results of synthesis with forest plots if meta-analysis
- [ ] Certainty of evidence (GRADE or equivalent)

## STARD — Diagnostic Accuracy Studies

- [ ] Index test and reference standard described
- [ ] Participant eligibility and recruitment
- [ ] Sample size justification
- [ ] Test execution details (who, blinded, order)
- [ ] How indeterminate results handled
- [ ] Cross-tabulation of results (2x2 table)
- [ ] Sensitivity, specificity, likelihood ratios with CIs
- [ ] Flow diagram of participant enrollment and test results

## Common Statistical Reporting Issues

### Choosing the right test
- Two independent groups, continuous, normal: unpaired t-test
- Two independent groups, non-normal or ordinal: Mann-Whitney U
- Paired observations: paired t-test or Wilcoxon signed-rank
- Three or more groups: ANOVA (with post-hoc specified) or Kruskal-Wallis
- Categorical outcomes: chi-squared or Fisher's exact test
- Time-to-event: Kaplan-Meier with log-rank, Cox regression
- Multiple comparisons: Bonferroni, Tukey, Benjamini-Hochberg correction

### SEM vs SD
- **SD** describes the spread of the data. Use in descriptive statistics.
- **SEM** describes precision of the mean estimate. Use when comparing means.
- Common error: using SEM in bar graphs to make variability appear smaller.

### Effect sizes
- Report alongside p-values. Common measures:
  - Cohen's d (mean difference / pooled SD)
  - Odds ratio, relative risk (binary outcomes)
  - R-squared (regression)
  - Hazard ratio (survival analysis)
