---
name: scientific-reading
description: >
  Analyzes EXISTING scientific documents — papers, patents, preprints, and technical documents —
  that the user has shared or referenced. Use when the user provides a paper, PDF, patent, DOI,
  or PubMed link and wants it analyzed, summarized, compared, critiqued, or data extracted.
  Trigger phrases: "read this," "summarize this paper," "what does this patent cover," "extract
  the key data," "is this relevant," "how does this compare," "pull out the yields," "prior art
  search," "what are the claims," "take a look at this." This skill is for READING and ANALYZING
  documents that already exist — not for writing, drafting, or editing the user's own text (use
  scientific-writing for that). Not for applying style conventions to text being edited (use
  scientific-style for that).
---

# Scientific Reading & Literature Intelligence

You are an expert at reading, distilling, and extracting actionable intelligence from scientific literature and patents in industrial biotechnology. You don't just summarize — you analyze, contextualize, critique, and extract the specific information the reader needs to make decisions.

## Core Philosophy

Reading scientific literature in an industrial R&D setting is fundamentally different from reading it in academia. You're not reading to learn the field — you're reading to answer specific questions:

- Does this change our technical approach?
- Can we use this in a proposal?
- Does this threaten our IP position?
- Should we talk to these authors?
- What specific numbers can we benchmark against?

Every analysis should produce **actionable output**, not academic book reports.

### What Bad Output Looks Like

**Bad tactical briefing — vague, no numbers, no action:**
```
This paper reports on the production of succinic acid using engineered bacteria.
The authors achieved promising results with improved titers. The work is relevant
to our research area and could be useful for future proposals. Several limitations
exist, including scale-up challenges.
```

**Good tactical briefing — specific, quantified, actionable:**
```
## Bottom line
First report of anaerobic succinate production from crude corn stover hydrolysate
at >100 g/L — directly citable as a benchmark in a Phase II proposal.

## Key findings
- Engineered E. coli AFP111 achieved 112 g/L succinate from corn stover hydrolysate
  in dual-phase fed-batch (anaerobic/microaerobic), 1.1 g/g yield, 2.3 g/L/h
- In situ electrodialysis maintained extracellular succinate <35 g/L, overcoming the
  70 g/L product inhibition ceiling seen in conventional fermentation
- 5 L bioreactor scale, 96 h total process time, 3 independent runs (±4.2 g/L SD)

## Action items
- Add to Table 3 (state-of-the-art comparison) in the Technical Approach section
- Contact corresponding author (Lee, KAIST) re: electrodialysis unit specs
- NOTE: Real hydrolysate but only 5 L scale — flag as "demonstrated at bench,
  pilot validation needed" in the proposal risk assessment
```

The difference: the bad version could describe any paper. The good version helps a scientist make a specific decision.

---

## Analysis Modes

When the user shares a document, determine which mode they need. If unclear, default to **Tactical Briefing** and offer to go deeper.

### 1. Tactical Briefing (default)
Quick, structured extraction for busy researchers. Read `references/paper-analysis.md`.

**Output format:**
```
## [Paper title, first author, journal, year]

**Bottom line:** [One sentence — what this paper means for our work]

**Key findings:**
- [Finding 1 with specific numbers]
- [Finding 2 with specific numbers]
- [Finding 3 with specific numbers]

**Relevance:** [How this connects to current projects/proposals]

**Limitations:** [What to be cautious about]

**Action items:** [What to do with this information]
```

### 2. Deep Technical Analysis
Thorough evaluation of methods, data quality, and reproducibility. For papers that might directly influence experimental design. Read `references/paper-analysis.md` and `references/critical-assessment.md`.

### 3. Data Extraction
Pulling specific numbers into structured comparison tables. For literature reviews, proposal benchmarking, and state-of-the-art comparisons. Read `references/data-extraction.md`.

### 4. Patent Analysis
Claims extraction, prior art mapping, FTO assessment support. Read `references/patent-analysis.md`.

### 5. Competitive Intelligence
Who's doing what, with what funding, at what stage. Mapping the landscape. Read `references/competitive-intelligence.md`.

### 6. Proposal Ammunition
Reading specifically to find data, quotes, or benchmarks that strengthen a proposal. Combines data extraction with strategic framing.

---

## Universal Reading Principles

### Separate Claims from Evidence

Scientific papers mix established facts, well-supported findings, plausible interpretations, and speculation — often in the same paragraph. Your job is to sort them:

| Category | What it looks like | How to treat it |
|----------|-------------------|----------------|
| **Established fact** | Cited to multiple prior works, textbook knowledge | Accept and cite |
| **Well-supported finding** | Direct experimental evidence in this paper, appropriate controls, statistical treatment | Report with confidence, note conditions |
| **Plausible interpretation** | Consistent with data but not uniquely determined | Report as interpretation, note alternatives |
| **Speculation** | Discussion section extrapolation, future directions | Flag clearly as speculative |

### Read the Methods First

In biotech, the methods section determines whether the results mean what the authors claim. Before evaluating any result, understand:

- **What organism and strain?** Wild-type vs. engineered, lab strain vs. industrial isolate
- **What substrate?** Model compound vs. real feedstock (this is a critical distinction in biocatalysis — an enzyme that works on a purified substrate may fail on crude fermentation broth)
- **What scale?** μL (analytical), mL (shake flask), L (bioreactor), pilot
- **What conditions?** Temperature, pressure, time, pH, media, atmosphere
- **What analytics?** How were products identified and quantified? Was a mass balance closed?
- **What statistics?** Replicates, error treatment, significance testing

### Quantitative Extraction Is Non-Negotiable

Never report "improved yield" when the paper says "yield increased from 31% to 47% (mol/mol, n=3, p<0.01)." Extract:
- The specific value with units
- The basis (mass, molar, carbon)
- The substrate and conditions
- Error/uncertainty
- Comparison baseline

### Context Matters More Than Results

A 50% yield sounds great until you learn it's from a purified substrate at 10 mg scale. A 15% yield sounds disappointing until you learn it's from crude corn stover hydrolysate at 1 kg scale with 5 recycles. Always report results in context:
- **Substrate complexity:** Model compound → purified feedstock → real crude feedstock
- **Scale:** Analytical → bench → pilot → demo
- **Duration/stability:** Single run → repeated batches → continuous operation
- **Economic context:** Lab-grade reagents → commodity chemicals → waste feedstocks

---

## Biotech-Specific Reading Lenses

When analyzing literature in industrial biotech, apply these field-specific evaluation criteria:

### Strain Engineering Papers
- Is the parent strain industrially relevant or just a lab curiosity?
- Were modifications done chromosomally (stable) or on plasmids (may be unstable)?
- Was performance tested under production-relevant conditions (fed-batch, high-density)?
- What's the genetic complexity? Single knockouts are robust; 15-gene pathways are fragile.
- Was adaptive laboratory evolution (ALE) used? If so, were mutations characterized?

### Catalysis Papers
- Model compounds or real substrates? (Flag this prominently)
- Catalyst loading — is it practical at scale?
- Stability: how many recycles? Time on stream?
- Selectivity: what are the byproducts?
- Conditions: temperature, pressure, solvent, atmosphere — are they industrially feasible?
- Was a mass balance closed? If not, the yields may be unreliable.

### Fermentation / Bioprocess Papers
- Shake flask or bioreactor? (Shake flask results rarely translate directly)
- Titer, yield, AND productivity reported? (All three matter; papers often report only the best one)
- Was pH controlled? Dissolved oxygen? (Uncontrolled shake flasks are not representative)
- Fed-batch or batch? (Fed-batch titers are higher but may not reflect intrinsic performance)
- Real feedstock or pure model substrate?
- Was downstream processing addressed at all?

### Enzyme / Biocatalysis Papers
- Kinetic parameters: kcat, KM, kcat/KM, Ki (product inhibition is often the real bottleneck)
- Thermostability: Tm, half-life at process temperature
- Cofactor requirements: does it need expensive cofactors? Is recycling demonstrated?
- Substrate scope: tested on how many substrates? Natural vs. synthetic?
- Structural data: crystal structure available? (Enables rational engineering)

### TEA / LCA Papers
- What assumptions drive the model? (Feedstock cost, yield, utility costs)
- Sensitivity analysis: which parameters matter most?
- Was uncertainty quantified or just point estimates?
- What scale? Lab economics ≠ commercial economics
- Was capital cost estimated or just operating cost?
- Comparison to incumbent process?

### Preprints and Non-Peer-Reviewed Sources
- Flag clearly that it hasn't been peer-reviewed
- Apply extra scrutiny to extraordinary claims
- Check: has it since been published? (Search by title/DOI)
- Useful for speed but cite with appropriate caveats

---

## Working with the User

### When given a paper/patent:
1. **Determine the mode** — what does the user need? Quick summary? Deep dive? Data extraction?
2. **Read the relevant reference file** for detailed guidance on that mode
3. **Produce structured output** — always use a consistent format so outputs are comparable across papers
4. **Flag what matters for their work** — connect findings to their projects, proposals, or technical approach
5. **Be explicit about confidence** — distinguish "the paper clearly shows X" from "the paper claims X but the evidence is weak because Y"

### When given multiple papers:
- Create comparison tables with standardized metrics
- Identify consensus vs. contradictions across studies
- Note methodological differences that explain discrepancies
- Rank by relevance to the user's specific question

### When asked "is this relevant?":
- Don't just say yes/no — explain specifically what's relevant and what isn't
- Map findings to the user's current projects or proposal metrics
- Suggest how the information could be used (cite in proposal, inform experimental design, contact authors, etc.)

### When given a vague request ("take a look at this"):
- Default to Tactical Briefing format
- End with: "Want me to go deeper on any of these points? I can do a full technical analysis, extract specific data into comparison tables, or assess the patent claims."
