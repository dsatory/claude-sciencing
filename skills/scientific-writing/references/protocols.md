# Protocols & Standard Operating Procedures

## What Makes Protocols Different

Protocols are imperative documents — they tell someone exactly what to do, in what order, with what materials. Unlike reports or proposals, every sentence must be actionable. Ambiguity doesn't just weaken the document — it causes wasted reagents, failed experiments, and unreproducible results.

**Cardinal rule:** A competent scientist who has never done this procedure should be able to execute it successfully by following the protocol alone, without asking questions.

---

## Protocol Types

### Experimental Protocols
Step-by-step procedures for laboratory experiments: assays, reactions, fermentations, transformations, extractions, analytical methods.

### Standard Operating Procedures (SOPs)
Formalized protocols with version control, approval signatures, and regulatory context. Required for GLP, GMP, ISO, and CLIA environments.

### Quick Protocols / Bench Cards
Condensed single-page references for routine procedures. Assume the user has done it before and just needs the key parameters.

---

## Structure

### 1. Title and Metadata
```
# Protocol: [Descriptive Title]
Version: [X.Y]
Date: [YYYY-MM-DD]
Author: [Name]
Reviewed by: [Name, if applicable]
```

### 2. Purpose
One to two sentences. What does this protocol accomplish and why?

**Bad:** "This protocol describes a qRT-PCR procedure."
**Good:** "Quantify relative mRNA expression of target genes in HEK293T cells using SYBR Green-based qRT-PCR, normalized to GAPDH and ACTB housekeeping genes."

### 3. Safety and Regulatory Notes
Up front, not buried. Include:
- PPE requirements (gloves, goggles, fume hood)
- Hazardous materials and their SDS locations
- BSL requirements for organisms
- Waste disposal requirements

### 4. Materials and Equipment

**Materials table format:**
| Reagent/Material | Catalog # | Supplier | Concentration/Amount | Storage |
|-----------------|-----------|----------|---------------------|---------|
| SYBR Green Master Mix | A25742 | Thermo Fisher | 2X | -20C |
| Random hexamers | N8080127 | Invitrogen | 50 uM | -20C |

**Critical details:**
- Include catalog numbers — "SYBR Green master mix" alone is insufficient (vendors sell 5+ variants)
- Specify lot-sensitive reagents where batch variation matters
- Note items that need advance preparation (e.g., "thaw on ice 30 min before use")
- Include equipment model numbers for instrument-specific protocols (qPCR machines, centrifuges, plate readers)

### 5. Reagent Preparation
Separate section for buffers, media, working solutions. Include:
- Final concentrations AND how to make them (e.g., "10X buffer: dissolve 12.1 g Tris in 80 mL water, pH to 7.4 with HCl, bring to 100 mL")
- Shelf life and storage conditions
- Sterilization requirements (autoclave, filter)
- Volume to prepare (scale to experiment)

### 6. Procedure

**Step formatting rules:**

1. **One action per step.** "Add 5 uL template, mix by pipetting, and spin briefly" is three steps masquerading as one. Split them.

2. **Lead with the verb.** "Add," "Incubate," "Centrifuge," "Transfer," "Discard" — not "The sample is then centrifuged."

3. **Specify everything quantitatively.**
   - **Bad:** "Add some enzyme and incubate for a while."
   - **Good:** "Add 1 uL SuperScript IV reverse transcriptase (200 U/uL). Incubate at 50C for 10 min."

4. **Include timing and conditions.**
   - Temperature (C, not "room temperature" — specify 22-25C if ambient)
   - Time (exact: "15 min" not "briefly"; range if acceptable: "10-15 min")
   - Speed (RPM and g for centrifugation, specify rotor if g conversion matters)
   - Atmosphere (aerobic, anaerobic, N2 blanket, CO2 incubator %)

5. **Mark critical steps.** Use a consistent notation:
   - **CRITICAL:** Steps where deviation causes failure
   - **CAUTION:** Safety-related warnings
   - **NOTE:** Helpful context that isn't strictly required
   - **PAUSE POINT:** Where the protocol can be safely stopped (with storage conditions)

6. **Include expected observations.** "The pellet should be white; a brown pellet indicates oxidation — discard and repeat from Step 3."

**Example:**

```
### RNA Extraction

1. Aspirate media from wells. Do not disturb the cell monolayer.

2. Add 500 uL TRIzol reagent directly to each well. Pipette up and down 5 times to lyse cells.
   **CRITICAL:** Complete lysis is essential. The lysate should be homogeneous with no visible clumps.

3. Incubate at 22-25C for 5 min to allow complete dissociation of nucleoprotein complexes.

4. Transfer lysate to a 1.5 mL microcentrifuge tube.
   **PAUSE POINT:** Lysate in TRIzol can be stored at -80C for up to 1 month.

5. Add 100 uL chloroform per 500 uL TRIzol. Cap securely.
   **CAUTION:** Chloroform is volatile and toxic. Work in a fume hood.

6. Shake vigorously by hand for 15 sec. Do NOT vortex.

7. Incubate at 22-25C for 3 min.

8. Centrifuge at 12,000 x g for 15 min at 4C.
   **NOTE:** Three phases will form: clear aqueous (top, contains RNA), white interphase, pink organic (bottom).

9. Carefully transfer the aqueous phase (~250 uL) to a fresh tube. Do NOT disturb the interphase.
   **CRITICAL:** Contamination with the interphase introduces DNA and protein. If unclear, take less rather than more.
```

### 7. Data Analysis / Expected Results
- What the raw data looks like
- How to process it (calculations, software, normalization)
- Expected ranges for positive and negative controls
- Acceptance criteria (when to trust vs. reject a run)

### 8. Troubleshooting

Table format works best:

| Problem | Likely Cause | Solution |
|---------|-------------|----------|
| No amplification | RNA degraded | Check RIN score; use fresh extraction |
| High Ct values (>35) | Low template input | Increase RNA input; check quantification |
| Multiple melt peaks | Non-specific amplification | Redesign primers; increase annealing temp |
| Inconsistent replicates | Pipetting error | Use multichannel; ensure proper mixing |

### 9. Version History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-01-15 | DS | Initial protocol |
| 1.1 | 2026-03-20 | DS | Updated annealing temperature to 62C per optimization results |

---

## Writing Principles for Protocols

### Be Explicit About What NOT to Do
"Do NOT vortex" is as important as "shake for 15 sec." Common mistakes and their consequences should be called out.

**Bad:** "Mix gently."
**Good:** "Mix by inverting the tube 5 times. Do NOT vortex — shearing will fragment the genomic DNA."

### Use Consistent Units
- Volumes: uL, mL, L (not microliters/milliliters in text)
- Temperature: C (always specify, even "room temperature" should be 22-25C)
- Time: sec, min, h (not seconds/minutes/hours)
- Speed: x g preferred over RPM (RPM is rotor-dependent); if RPM, specify rotor
- Mass: mg, g, kg
- Concentration: mM, uM, nM; or mg/mL, ug/mL; or % (w/v) or % (v/v) — always specify basis

### Scale and Adaptation Notes
If the protocol is designed for a specific scale (e.g., 6-well plate, 50 mL flask), include a scaling table or formula for adapting to other formats.

| Format | Surface Area | Media Volume | TRIzol | Cells/Well |
|--------|-------------|-------------|--------|------------|
| 96-well | 0.32 cm2 | 100 uL | 50 uL | ~3x10^4 |
| 24-well | 1.9 cm2 | 500 uL | 250 uL | ~2x10^5 |
| 6-well | 9.6 cm2 | 2 mL | 1 mL | ~1x10^6 |

### Controls Are Not Optional
Every protocol should specify:
- **Positive control:** Known to work — validates the procedure
- **Negative control:** Known to fail — validates specificity
- **No-template control (NTC):** For PCR/qPCR — detects contamination
- Acceptance criteria for controls (what result means the run is valid)

---

## SOP-Specific Additions

For formal SOPs (GLP/GMP/regulated environments), add:

- **Scope:** What this SOP covers and does not cover
- **Responsibilities:** Who is authorized to execute, review, and approve
- **Definitions:** Technical terms and abbreviations defined
- **References:** Related SOPs, regulatory standards, instrument manuals
- **Document control:** Version, effective date, review schedule, approval signatures
- **Deviations:** How to document and handle deviations from the procedure
- **Training requirements:** Who must be trained before executing this SOP

---

## Common Pitfalls

| Pitfall | Why It Fails | Fix |
|---------|-------------|-----|
| "Add buffer" without specifying which | Lab may have 10 buffers on the shelf | Full name, composition, or catalog # |
| "Centrifuge briefly" | 10 sec vs 5 min gives very different pellets | Specify time, speed, and temperature |
| "Room temperature" | Can mean 18C or 28C depending on the building | Specify range: 22-25C |
| Missing pause points | Researcher starts at 4 PM, can't stop at Step 12 | Mark every safe stopping point |
| No troubleshooting section | Same failure debugged from scratch every time | Include the top 5 failure modes |
| Reagent list without catalog #s | Wrong vendor product gives different results | Always include catalog # and supplier |
| Steps that combine actions | Easy to miss one action in a compound step | One verb per numbered step |
