---
description: Generate detailed bench-ready protocols with reagent calculations, timing, and practical notes
argument-hint: [technique or procedure] [optional: --scale N, --format markdown|pdf]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch
---

# Protocol Generation

Generate a detailed, bench-ready protocol. The `lab-workflow` skill provides templates and guidance in `references/protocols.md`.

## Workflow

1. **Identify the technique** from $ARGUMENTS
2. **Ask for specifics** if needed (scale, organism, vector, target protein, equipment available)
3. **Generate the full protocol** with:
   - Materials list with specific quantities, catalog numbers, storage conditions
   - Solution recipes with exact concentrations
   - Numbered steps with volumes, temperatures, times
   - Critical steps in **bold**
   - Practical tips in *italics*
   - PAUSE POINTS marked
   - Expected results
   - Troubleshooting table

## Flags

### --scale N
Calculate all quantities for N reactions/samples:
- Multiply volumes with 10-15% overage for pipetting loss
- Generate master mix tables where appropriate
- Flag steps that change at different scales

### --format
- `markdown` (default) — output as formatted markdown
- Save to file if user specifies a path

## Protocol Quality Checklist

Before outputting, verify:
- [ ] Every reagent has a concentration and volume
- [ ] Every incubation has a temperature and duration
- [ ] Critical steps are flagged
- [ ] Controls are included
- [ ] Expected results are described
- [ ] Safety notes are included where relevant
- [ ] PAUSE POINTS are marked
- [ ] Troubleshooting section covers common failures

## Known Protocols

Generate detailed protocols for (among others):
- **Cloning:** Gibson assembly, Golden Gate, restriction/ligation, TOPO, Gateway, In-Fusion
- **PCR:** Standard, colony, gradient, touchdown, inverse, overlap extension, site-directed mutagenesis
- **Transformation:** Chemical (CaCl₂, TSS), electroporation, heat shock
- **Expression:** IPTG induction, auto-induction, temperature shift
- **Purification:** His-tag IMAC, IEX, SEC, GST pulldown, Strep-tag
- **Analysis:** SDS-PAGE, Western blot, Bradford/BCA assay, Nanodrop
- **Fermentation:** Shake flask setup, bioreactor inoculation, fed-batch feeding
- **Cell culture:** Passaging, transfection, freezing/thawing, mycoplasma testing

For unlisted techniques, search the literature or ask the user for the base protocol to adapt.
