# Experimental Ideation

Brainstorming experimental approaches for a research question. The goal is to generate multiple testable strategies, evaluate their trade-offs, and recommend a prioritized path.

## Ideation Framework

### Step 1: Define the Question
Restate the user's question as a specific, testable hypothesis or goal:
- "Improve recombinant protein yield in E. coli" → "Increase soluble expression of [protein X] in E. coli BL21(DE3) from current ~5 mg/L to ≥50 mg/L"
- Ask for specifics if missing: what protein? What's current yield? What's been tried?

### Step 2: Generate Approaches (aim for 4-8)
For each approach:
- **What:** One-sentence description
- **Mechanism:** Why this might work
- **Effort:** Low / Medium / High (time, cost, complexity)
- **Risk:** Low / Medium / High (likelihood of failure)
- **Timeline:** Days / Weeks / Months
- **Prerequisites:** What you need to have or know first

### Step 3: Prioritize
Recommend a strategy that:
1. Starts with the lowest-effort, highest-information experiments
2. Runs independent approaches in parallel where possible
3. Has clear decision points ("if X doesn't work by week 2, switch to Y")
4. Builds on results incrementally

### Step 4: Quick Wins First
Always identify the "try this Monday morning" experiment — something that takes <1 day, costs almost nothing, and could resolve the issue immediately.

## Ideation Patterns by Domain

### Improving Expression
1. Lower induction temperature (37°C → 18-25°C overnight) — free, try first
2. Reduce IPTG concentration (1 mM → 0.1-0.01 mM) — free
3. Try auto-induction media (ZYP-5052) — one day, minimal cost
4. Codon-optimize the gene — 1-2 weeks (synthesis), moderate cost
5. Fusion tags (MBP, SUMO, TrxA) for solubility — 1-2 weeks cloning
6. Co-express chaperones (GroEL/ES, DnaK/J) — 1 week if plasmids available
7. Switch host (SHuffle for disulfide bonds, C41 for membrane proteins, Rosetta for rare codons)
8. Switch expression system entirely (yeast, insect cells, cell-free)

### Improving Metabolite Titer
1. Media optimization (carbon source, nitrogen source, trace metals, pH) — days
2. Feeding strategy optimization (fed-batch, pulse feeding) — days
3. Knockout competing pathways — weeks (if not already constructed)
4. Overexpress rate-limiting enzyme(s) — weeks
5. Balance pathway flux (promoter/RBS libraries) — weeks to months
6. Adaptive laboratory evolution on product tolerance — months
7. Cofactor engineering (NADH/NADPH balance) — weeks
8. Process optimization (temperature, DO, pH profile) — days to weeks

### Improving Enzyme Activity
1. Literature mining for known improved variants — hours
2. Rational mutations at active site (if structure available) — weeks
3. Directed evolution (epPCR or saturation mutagenesis + screen) — months
4. Computational design (Rosetta, machine learning models) — weeks to months
5. Homolog screening (natural diversity) — weeks
6. Substrate engineering (modified substrate more amenable) — case-dependent
7. Reaction condition optimization (pH, temperature, solvent, cofactors) — days
8. Immobilization for stability — weeks
