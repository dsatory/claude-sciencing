# Paper Analysis — Detailed Guidance

## Tactical Briefing Protocol

For a quick but rigorous paper distillation (~2-3 minutes of reading time for the user):

### Step 1: Identify the Paper
- Full citation (authors, title, journal, year, DOI)
- Open access status
- Preprint vs. published

### Step 2: Bottom Line (one sentence)
The single most important takeaway for the reader's work. This requires understanding both the paper AND the reader's context.

**Examples:**
- "First demonstration of one-pot enzymatic PET depolymerization + microbial conversion to PHA — directly validates cascade bioprocess approaches."
- "New thermostable ketoreductase with 3× higher activity than LbADH, but only tested on model ketones — worth monitoring, not yet validated on industrial substrates."
- "TEA shows bio-succinic acid at $1,086/ton with integrated membrane separation — competitive with petroleum-derived, directly citable as a cost benchmark in proposals."

### Step 3: Key Findings (3-5 bullets)
Each bullet must contain a specific number or concrete claim. No vague summaries.

**Bad:** "The authors achieved improved itaconic acid production."
**Good:** "Engineered A. terreus ΔcitA/OE-cadA achieved 87.3 ± 2.1 g/L itaconic acid from corn stover hydrolysate (mean of 6 replicates), stable for 120 h in fed-batch at 0.62 g/g glucose yield."

### Step 4: Relevance Assessment
Map findings to the reader's current work:
- Which project or proposal does this relate to?
- Does it support, challenge, or extend their approach?
- Specific sections of their proposals/reports this could strengthen

### Step 5: Limitations & Caveats
What should the reader be cautious about:
- Model compounds vs. real biomass
- Scale limitations
- Missing controls or statistics
- Contradictions with other published work
- Potential conflicts of interest (industry-funded, self-citation heavy)

### Step 6: Action Items
Concrete next steps:
- "Cite in Section 4.2 of the DOE technical approach"
- "Add to comparison table in lit review — biocatalyst benchmarks"
- "Contact corresponding author re: collaboration — they have complementary enzyme engineering capability"
- "Monitor — promising but needs validation on real substrates before we build on it"
- "Check if patent filed — could affect our FTO"

---

## Deep Technical Analysis Protocol

For papers that might directly influence experimental design, strain engineering strategy, or catalytic approach selection.

### Extended Evaluation

Everything in the Tactical Briefing, plus:

#### Methods Scrutiny
- Reproduce the experimental logic in your mind: given these methods, would you expect these results?
- Identify missing controls
- Assess whether analytical methods are appropriate and sufficient
- Check if the mass balance closes (in bioconversion, unclosed mass balances hide byproduct accumulation or uncharacterized metabolites)
- Note any unusual or non-standard procedures

#### Data Quality Assessment
For each key result:
- How many replicates? What error treatment?
- Are the figures and tables internally consistent?
- Do the numbers in the text match the figures?
- Are there obvious outliers that were included or excluded?
- Is the statistical treatment appropriate? (t-test vs. ANOVA vs. non-parametric)

#### Reproducibility Indicators
- Are methods detailed enough to reproduce? Or do they rely on citing other papers for critical steps?
- Are strains/plasmids/catalysts available? (deposited in public repositories, or available on request?)
- Has any part of this work been independently reproduced?
- Are there obvious batch-to-batch or lab-to-lab variability concerns?

#### Comparison to State of the Art
- Where does this result sit relative to the best published benchmarks?
- Is the improvement meaningful (2× better) or marginal (5% better)?
- Are they comparing to the right baselines?
- Build a mini comparison table if there are multiple relevant benchmarks

#### Mechanistic Assessment
- Is the proposed mechanism well-supported by the data?
- Are alternative mechanisms ruled out?
- Do computational results (DFT, MD) match experimental observations?
- Are control experiments sufficient to support causality?

#### Supplementary Information
- Always check the SI — it often contains the most important data
- Look for negative results, failed conditions, and optimization screens buried in SI
- SI tables with full datasets enable better comparison than cherry-picked main text figures

---

## Reading Strategy for Specific Paper Types

### Primary Research Articles
Standard protocol above. Focus on results and methods.

### Review Articles
- Don't read reviews to learn the field — read them to find papers
- Scan the reference list for primary sources you haven't seen
- Note the review's organizational framework — it may reveal how the field thinks about the problem
- Check publication date — reviews in fast-moving fields are outdated within 2 years
- Identify what the review doesn't cover — these are gaps and opportunities

### Perspectives / Commentaries
- Often written by field leaders with strong opinions
- Useful for understanding the political landscape of the field
- Identify which groups are aligned with which approaches
- Note predictions — some will be wrong, and the reasons are informative

### Preprints
- Higher bar for scrutiny — not yet peer-reviewed
- Check if it's been submitted (stated in the preprint) and whether it's since been published
- Valuable for speed, but cite with "preprint, not peer-reviewed" caveat
- Some fields (computational biology) have high-quality preprint culture; others (clinical) less so

### Conference Proceedings / Abstracts
- Often contain preliminary results not yet in full papers
- Limited detail — treat as signals, not evidence
- Useful for competitive intelligence (who is working on what)
