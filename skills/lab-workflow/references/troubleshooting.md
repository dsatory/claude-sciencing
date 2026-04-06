# Troubleshooting

Systematic diagnosis of failed experiments. The goal is to identify the most likely cause quickly and suggest the minimal experiment to confirm it.

## Troubleshooting Framework

### Step 1: Define the Failure
- What exactly happened? (no colonies, low yield, wrong band, contamination, no activity)
- What was expected?
- What changed since the last time it worked? (if it ever worked)

### Step 2: Rank Causes by Likelihood
Use Occam's razor — the simplest explanation is usually right. Common ordering:
1. **User error** (wrong reagent, missed step, timing error) — most common
2. **Reagent failure** (expired, degraded, contaminated, wrong concentration)
3. **Equipment failure** (incubator temperature off, pipette miscalibrated)
4. **Biological variability** (strain instability, plasmid loss, mutation)
5. **Protocol limitation** (method isn't suitable for this specific case)

### Step 3: Diagnostic Experiments
Suggest the minimum experiment to distinguish between causes. The diagnostic should:
- Take ≤1 day
- Test one variable at a time (unless using appropriate controls)
- Give a clear yes/no answer
- Use materials already in the lab

### Step 4: Solution
Once the cause is identified, provide a specific fix with protocol details.

---

## Common Failure Modes

### No Colonies After Transformation
**Ordered by likelihood:**

| Cause | Diagnostic | Fix |
|-------|-----------|-----|
| Competent cells dead | Transform positive control plasmid (pUC19) | Fresh competent cells; check -80°C storage |
| Wrong antibiotic / wrong concentration | Check plate antibiotic and concentration | Re-pour plates; verify stock concentration |
| Ligation / assembly failed | Run assembly product on gel (should see shift) | Check insert:vector ratio; verify fragment quality |
| DNA concentration too low | Quantify assembly product (Nanodrop/Qubit) | Use more DNA; concentrate by ethanol precipitation |
| Heat shock too long/hot | Review protocol — was it exactly 42°C, 30-45 sec? | Use a thermometer in the water bath |
| No recovery period | Was SOC added? Incubated 1 h at 37°C? | Add recovery step; use SOC not LB |
| Incompatible antibiotic resistance + host | Check if host has native resistance | Verify antibiotic marker vs. host genotype |
| Vector is toxic | Check: does empty vector give colonies? | Reduce expression; use tighter promoter; lower growth temp |

### Low Protein Expression
| Cause | Diagnostic | Fix |
|-------|-----------|-----|
| Induction failed | Check OD at induction; compare uninduced vs. induced by SDS-PAGE | Verify IPTG concentration and stock activity |
| Protein is insoluble | Lyse and check pellet vs. supernatant by SDS-PAGE | Lower temperature (18°C), lower IPTG, auto-induction |
| Codon usage issues | Check rare codon content (GenScript analyzer) | Switch to Rosetta/BL21-CodonPlus; codon optimize gene |
| Plasmid loss | Plate overnight culture ± antibiotic; count CFU | Add antibiotic to all stages; check plasmid by miniprep |
| Toxicity / growth inhibition | Compare growth curves ± induction | Leaky expression issue: use tighter promoter, glucose repression |
| Wrong reading frame | Verify sequence of expression construct | Re-sequence; check fusion junction |

### Contamination (Microbial)
| Cause | Diagnostic | Fix |
|-------|-----------|-----|
| Media contamination | Incubate uninoculated media 37°C overnight | Re-autoclave or use fresh media; check sterile technique |
| Water bath / incubator contamination | Swab and streak surfaces | Clean with 70% ethanol + 10% bleach |
| Phage contamination (E. coli) | Cloudy cultures that clear suddenly | Use T1-resistant strain; UV-irradiate media; deep clean |
| Cross-contamination between strains | Streak singles; colony PCR with strain-specific primers | Improve labeling; spatial separation; re-streak from freezer stock |
| Mycoplasma (cell culture) | MycoAlert or PCR-based detection kit | Discard and thaw fresh stock; treat with Plasmocin |

### No/Low Enzyme Activity
| Cause | Diagnostic | Fix |
|-------|-----------|-----|
| Protein is inactive (misfolded) | Circular dichroism or DSF to check fold | Refold; express at lower temp; add cofactors |
| Wrong assay conditions | Check pH, temperature, buffer, cofactors | Optimize systematically; check literature for known conditions |
| Enzyme is inhibited | Test with known substrate + your assay buffer | Identify inhibitor (EDTA chelating metals? Imidazole? DTT?) |
| Substrate concentration too low | Titrate substrate; check KM | Increase substrate; check solubility |
| No cofactor / metal | Add metals (Mg²⁺, Mn²⁺, Zn²⁺); add NAD(P)H/FAD | Screen cofactors systematically |
| Enzyme degraded during purification | Run activity assay at each purification step | Add protease inhibitors; work faster; keep cold |

### PCR Failure (No Product / Wrong Size / Smear)
| Symptom | Cause | Fix |
|---------|-------|-----|
| No product | Primers not binding; extension time too short; polymerase dead | Gradient PCR for Tm optimization; increase extension time; fresh enzyme |
| Wrong size band | Mispriming; wrong template; primer design error | Increase annealing temp; redesign primers; verify template |
| Multiple bands | Non-specific priming; too many cycles | Touchdown PCR; increase annealing temp; reduce to 25-30 cycles |
| Smear | Over-amplification; DNA degradation; secondary structure | Reduce cycles; fresh template; add DMSO (3-5%) or betaine (1 M) |
| Primer dimers only | Primers complementary to each other | Redesign primers; hot-start polymerase; reduce primer concentration |

### Fermentation Issues
| Symptom | Cause | Fix |
|---------|-------|-----|
| No growth | Wrong media; wrong temperature; toxic carbon source | Check media recipe; verify inoculation; test on LB first |
| Growth arrest at low OD | Nutrient limitation; pH crash; toxic metabolite accumulation | Check glucose, nitrogen; monitor pH; analyze metabolites |
| Foaming | Protein expression; cell lysis; media components | Add antifoam (Sigma A8311); reduce aeration |
| DO crash | Too many cells; insufficient aeration | Increase agitation/air flow; reduce inoculum; feed more slowly |
| pH drift | Metabolite production; CO₂ accumulation | Increase buffer capacity; add pH control (NH₃ or NaOH) |
| Phage lysis | See contamination section | Phage-resistant strains; prophage-cured hosts |
