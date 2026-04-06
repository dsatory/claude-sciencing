# Protocol Generation

Generating detailed, bench-ready protocols with specific quantities, timing, and practical notes.

## Protocol Format

Every protocol should include:

### Header
- Protocol name and version
- Date and author
- Purpose (one sentence)
- Expected duration
- Safety notes

### Materials
- Reagents with catalog numbers, concentrations, storage conditions
- Equipment needed
- Consumables (tubes, tips, plates, etc.)
- Prepared solutions with recipes

### Procedure
- Numbered steps with specific quantities, temperatures, times
- **Bold** critical steps where deviation causes failure
- *Italic* tips and practical notes
- PAUSE POINTS clearly marked (where you can stop overnight/weekend)
- Timing annotations ("this step takes ~30 min" or "incubate overnight (16-18 h)")

### Expected Results
- What success looks like (e.g., "expect 200-500 ng/µL DNA" or "clear lysate after centrifugation")
- What failure looks like and immediate next steps

### Troubleshooting Table
| Problem | Likely cause | Solution |
|---------|-------------|----------|

## Protocol Templates by Technique

### Molecular Cloning (Gibson Assembly)

**Materials:**
- Gibson Assembly Master Mix (NEB E2611) — store at -20°C, thaw on ice
- Purified vector backbone (linearized, DpnI-treated if from PCR)
- Purified insert(s) (PCR product with 20-40 bp overlaps)
- Competent cells (DH5α or TOP10, ≥10⁸ CFU/µg)
- SOC medium (pre-warmed to 37°C)
- LB + antibiotic plates (pre-warmed to 37°C)

**Critical calculations:**
- Optimal molar ratio: 1:2 (vector:insert) for 2-fragment; 1:1:1 for 3-fragment
- Total DNA: 50-100 ng vector + proportional insert
- pmol = (ng × 1000) / (bp × 650 Da/bp)

**Procedure:**
1. Calculate DNA amounts for desired molar ratio
2. Combine vector + insert(s) in a PCR tube on ice
3. Add Gibson Assembly Master Mix to 10 µL total volume (or 20 µL for ≥4 fragments)
4. **Incubate 50°C for 15 minutes** (60 min for ≥4 fragments)
5. *Can store at -20°C here or proceed immediately*
6. Transform 2 µL into 50 µL competent cells
7. Heat shock 42°C for 30 seconds → ice 2 minutes
8. Add 950 µL SOC, shake 37°C for 1 hour
9. Plate 100 µL on selective plates; spin down remainder, plate concentrated
10. Incubate overnight at 37°C

### Protein Expression (E. coli, T7 system)

**Day 1 — Inoculate:**
1. Pick a single colony into 5 mL LB + antibiotic in a 50 mL tube
2. Grow overnight at 37°C, 220 rpm (14-16 h)

**Day 2 — Express:**
1. Measure OD600 of overnight culture (typically 2-4)
2. Inoculate 1:100 into fresh medium (e.g., 5 mL into 500 mL in 2 L flask)
3. Grow at 37°C, 220 rpm until OD600 = 0.4-0.8 (typically 2-3 h)
4. **Take pre-induction sample** (1 mL, pellet and freeze at -20°C)
5. **Cool culture to induction temperature** (if using low-temp expression: move to 18°C incubator, wait 30 min)
6. Add IPTG to final concentration (typically 0.1-1 mM)
7. Express: 18°C for 16-20 h (soluble) OR 37°C for 3-4 h (high total, may be insoluble)
8. Take post-induction sample (1 mL)
9. Harvest: centrifuge 4000 × g, 20 min, 4°C
10. **PAUSE POINT:** Freeze pellet at -80°C (stable for months)

### Protein Purification (His-tag IMAC)

**Buffers (prepare fresh or use within 1 week):**
- Lysis: 50 mM Tris-HCl pH 8.0, 300 mM NaCl, 10 mM imidazole, 1 mM PMSF (add fresh), 1 mg/mL lysozyme
- Wash: 50 mM Tris-HCl pH 8.0, 300 mM NaCl, 20-40 mM imidazole
- Elution: 50 mM Tris-HCl pH 8.0, 300 mM NaCl, 250 mM imidazole
- Storage: 50 mM Tris-HCl pH 8.0, 150 mM NaCl, 10% glycerol (if freezing)

**Procedure:**
1. Resuspend pellet in Lysis buffer (5 mL per g wet cell weight)
2. Lyse: sonicate on ice (30s on / 30s off × 6 cycles, 40% amplitude) or French press (2 passes, 15,000 psi)
3. Centrifuge 20,000 × g, 30 min, 4°C → save supernatant (= cleared lysate)
4. **Save 50 µL of pellet (insoluble) and lysate (soluble) for SDS-PAGE**
5. Load lysate onto pre-equilibrated Ni-NTA column (1 mL resin per 500 mL culture)
6. Wash with 10 column volumes Wash buffer
7. Elute with 5 column volumes Elution buffer (collect 1 mL fractions)
8. Run SDS-PAGE of load, flow-through, wash, and elution fractions
9. Pool pure fractions, dialyze or buffer exchange into Storage buffer
10. Measure concentration (A280 using theoretical extinction coefficient)
11. Aliquot, snap-freeze in liquid nitrogen, store at -80°C

## Scaling Guidelines

When the user specifies a scale (e.g., "--scale 10 reactions"), calculate all quantities:
- List materials with total amounts needed (include 10-15% overage for pipetting loss)
- Create a master mix table where appropriate
- Note any steps that change at scale (e.g., "for >20 transformations, prepare electrocompetent cells rather than chemical")
