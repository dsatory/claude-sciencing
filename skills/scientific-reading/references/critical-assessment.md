# Critical Assessment of Scientific Literature

Evaluating whether published results are reliable, reproducible, and relevant. This is the skill that separates reading from analysis — anyone can extract numbers, but assessing their trustworthiness requires domain expertise.

## The Assessment Framework

For every key claim in a paper, evaluate across four dimensions:

### 1. Internal Validity
Does the data support the authors' conclusions?

**Red flags:**
- Conclusions that go beyond what the data show
- Missing controls (especially in catalysis: blank reactions, catalyst-free controls)
- Cherry-picked data points (n=1 "representative" results without replication)
- Figures that look too clean (no scatter, perfect fits, suspiciously low error bars)
- Inconsistencies between text, tables, and figures
- Unclosed mass balance in conversion chemistry (where did the other 30% go?)
- Yields reported without specifying the basis (mass, molar, carbon)

**Green flags:**
- Complete mass balance
- Multiple independent replicates with statistical treatment
- Control experiments that rule out alternative explanations
- Acknowledgment of limitations in the discussion
- Raw data available in SI or repository

### 2. External Validity (Transferability)
Will these results hold outside the authors' specific conditions?

**The model compound trap:** In biocatalysis and bioprocess engineering, the gap between purified substrate and real feedstock performance is enormous. An enzyme that achieves 95% conversion on p-nitrophenyl acetate at 10 mg scale may achieve 15% on crude industrial waste oil. Always note:
- Purified model substrate vs. technical-grade feedstock vs. real crude stream
- Defined media vs. real hydrolysate or waste stream
- Purified substrate vs. crude mixture
- Lab-grade reagents vs. commodity chemicals

**The scale gap:** Results at 100 μL rarely translate linearly to 100 L. In particular:
- Mixing and mass transfer change with scale
- Heat management becomes non-trivial
- Catalyst recovery and recycling matter only at scale
- Contamination control is harder at scale
- Economics are fundamentally different

**The strain context:** An engineered E. coli K-12 strain in rich media does not predict performance of an industrial C. glutamicum in minimal media on real hydrolysate.

### 3. Reproducibility Signals
How likely is it that another group could reproduce these results?

**Strong reproducibility signals:**
- Detailed methods with specific catalog numbers, concentrations, protocols
- Strains deposited in public collections (ATCC, DSMZ, Addgene)
- Data deposited in repositories (GenBank, MetaboLights, Zenodo)
- Multiple groups have published similar results
- Supplementary protocols or video methods available

**Weak reproducibility signals:**
- Vague methods ("standard conditions," "as previously described" without accessible reference)
- Strains/catalysts available only on request (often means never)
- Single-lab result with no independent validation
- Extraordinary claims from groups with no prior work in the area

### 4. Relevance to Your Work
Even valid, reproducible results may not matter for your specific application.

**Relevance filters for industrial biotech:**
- Does this work at industrially feasible conditions? (Exotic solvents, extreme pressures, rare catalysts may be scientifically interesting but impractical)
- Does the substrate match what would actually be processed at scale?
- Is the product recoverable and purifiable with standard downstream methods?
- Does the economics work even in the best case?
- Is the organism something that can be engineered and fermented at industrial scale?
- Does it integrate with existing process infrastructure, or require rebuilding from scratch?

---

## Common Overclaims to Watch For

### "First demonstration of X"
- Check the literature carefully. "First" claims are frequently wrong.
- Even if technically true, ask: is it the first for a reason? (Maybe because it's not useful.)

### "Record titer/yield/productivity"
- Compared to what? The record on that specific substrate? On any substrate? In that organism?
- Context matters: 152 g/L succinic acid from pure glucose is impressive but different from 48 g/L from crude corn stover hydrolysate.

### "Feedstock-agnostic"
- Tested on how many feedstocks? 2? 5? 50?
- Were the feedstocks genuinely diverse (glucose AND xylose AND glycerol AND crude hydrolysate) or just variants of one type?
- "Feedstock-agnostic" with asterisks ("after pretreatment optimization for each feedstock") is really feedstock-specific with a common downstream step.

### "Scalable process"
- Demonstrated at what scale?
- "Scalable" in a paper usually means "we don't see an obvious reason it can't scale" — not "we've demonstrated it at scale."
- Look for: continuous operation, catalyst recycling, product recovery, real feedstock. If all four are missing, scalability is speculative.

### "Competitive with petroleum-derived"
- At what oil price? What feedstock cost? What scale?
- Is the comparison to current market price or production cost?
- Does it include capital amortization or just operating cost?
- Have they accounted for downstream purification to equivalent grade?

### "Atom economy" / "Green chemistry"
- Life cycle assessment (LCA) or just E-factor?
- Does "green" account for solvent production, catalyst synthesis, energy input?
- Solvent-free processes that require 300°C and 50 bar H₂ are not inherently green.

---

## Structured Output: Critical Assessment Card

For each paper assessed in depth, produce:

```
## Critical Assessment: [Short paper identifier]

**Claim validity:**
| Key claim | Evidence strength | Concern |
|-----------|------------------|---------|
| [Claim 1] | Strong / Moderate / Weak | [Specific concern or "none"] |
| [Claim 2] | Strong / Moderate / Weak | [Specific concern or "none"] |

**Transferability:** [High / Medium / Low] — [one sentence explanation]

**Reproducibility:** [High / Medium / Low] — [one sentence explanation]

**Relevance to our work:** [High / Medium / Low] — [specific connection]

**Overall confidence:** [Use with confidence / Use with caveats / Treat as preliminary]
```
