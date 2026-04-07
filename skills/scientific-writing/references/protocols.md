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

---

## Real-World Protocol Patterns (from Human-Written Lab Protocols)

These patterns are extracted from real laboratory protocols written by bench scientists in industrial biotech. All strain IDs, project numbers, and personnel names have been sanitized.

### Pattern 1: Strain-Specific Inoculation Parameters

Real protocols specify different conditions per strain because organisms behave differently. A generic "inoculate and grow overnight" is insufficient:

```
Evening prior to transformation:

Thaw one glycerol stock and inoculate into 100 mL BHI + 1x trace metals 
(+ appropriate selection) in 500 mL baffled flasks. Incubate at 25°C, 
shaking at 220 rpm (25 mm throw) for ~16 hours.

Strain-specific inoculum volumes:
- Strain A wild type: 50-75 µL initial inoculum
- Strain A helper plasmid: 200 µL initial inoculum
- Strain A single X-over strains: 150 µL initial inoculum
- Strain B wild type: 500 µL initial inoculum (grows clumpy from bullets)
- Strain B helper plasmid: 200 µL initial inoculum, grown at 30°C for 24 h

Claim one of the centrifuges for use the following day — set to 4°C, 
ensure lid is closed.
```

Key features: strain-specific volumes with justification ("grows clumpy"), equipment reservation the night before, temperature and throw specified for the shaker model.

### Pattern 2: Advance Preparation Callout

Experienced protocol writers front-load a preparation block. This prevents the "I need X but it's not ready" problem mid-protocol:

```
Perform as much preparation work in advance. Set up electroporation 
machine at the beginning of the day, aliquot DNA, prepare recovery 
plates, recovery media, etc. Also pre-chill electroporation buffer, 
cuvettes, and centrifuge. Recovery plates should contain appropriate 
selective media.
```

This single paragraph saves hours of delays. It signals to the reader: "read ahead before starting."

### Pattern 3: Wash Steps with Resuspension Logic

Cell washing protocols must specify how tubes are combined, not just "wash 3 times":

```
1. Transfer 100 mL culture to two 50 mL conical tubes. Ice for 10 min.
2. Pellet at 4,122 × g for 10 min at 4°C.
3. Remove supernatant from both tubes. Add 10 mL wash buffer to one tube. 
   Resuspend pellet. Transfer resuspension to the second tube and resuspend 
   that pellet (combining both into one tube).
4. Pellet at 4,122 × g for 10 min at 4°C.
5. Remove supernatant. Resuspend in 10 mL wash buffer.
6. Repeat steps 4-5 once or twice more, for 3-4 total washes.
7. Pellet. Resuspend to OD₆₀₀ ≈ 50 in wash buffer (600 µL per 100 mL 
   original culture). This does not need to be exact, so long as the 
   overnight OD₆₀₀ ≈ 0.3.
```

Key features: explicit tube-combining logic (step 3), target OD with back-calculation from starting volume (step 7), tolerance for imprecision where it's acceptable.

### Pattern 4: Critical Step with Immediate Recovery

For electroporation, transformation, or any step requiring immediate follow-up action:

```
Have 1 mL recovery medium ready in a pipette BEFORE electroporating. 

1. Load cuvette into machine. Close protective cover.
2. Electroporate. Ensure no arcing. If arcing occurs, remake the sample.
   Record peak voltage and time constant.
3. IMMEDIATELY add 1 mL recovery medium to cuvette. Gently pipette 
   up and down to mix.
4. Transfer to recovery plate well. Cover loosely with breathable seal.
5. Recover at 30°C for 1-3 hours, 1000 rpm (3 mm throw).
```

The "have X ready BEFORE" instruction is a hallmark of protocols written by someone who has actually done the procedure. The instruction to record machine output (voltage, time constant) is essential for troubleshooting.

### Pattern 5: Plating with Dilution Strategy

When colony counts will span orders of magnitude:

```
1. While recovering, dry selective plates at 37°C. Label and add glass beads.
2. Plate 100 µL of transformation mixture onto selective medium.
3. ALSO plate 100 µL of 1:10 and 1:100 dilutions on separate plates — 
   high-efficiency transformations can produce confluent lawns.
4. Incubate at 30°C for 2-3 days until colonies form.
5. Record CFU/mL per µg DNA.
```

The dilution plating (step 3) is experience-driven — a novice would plate one concentration and get an uncountable lawn.

### Pattern 6: Formal SOP Document Control

For regulated or institutional protocols, include document control metadata:

```
Document Number: SOP-RES-XX
Revision Number: 00
Version: 1.0

Document Title: [Descriptive procedure name]
Author: [Name]
Owner: [Name]

Associated Documents: [List related SOPs]
Effective Date: [Date]
```

Formal SOPs then follow a standardized section order:
1. PURPOSE & SCOPE
2. ABBREVIATIONS / DEFINITIONS
3. MATERIALS
4. RECIPES
5. PROCESS FLOW (diagram)
6. PROCEDURE DESCRIPTION (numbered subsections per stage)
7. SAFETY AND DISPOSAL
8. VALIDATION REFERENCE

### What Real Protocols Do That AI-Generated Protocols Often Miss

| Element | Real protocol | AI-generated protocol |
|---------|--------------|----------------------|
| Strain-specific parameters | Different volumes, temps, times per organism | Generic "inoculate culture" |
| Equipment details | Shaker throw (25 mm), centrifuge model, cuvette gap width | "Centrifuge" without specs |
| Failure experience | "Grows clumpy from bullets," "if arcing occurs" | Generic cautions |
| Tube logistics | How to combine pellets across tubes | Skips this entirely |
| Recovery timing | "Have medium ready BEFORE electroporation" | Steps listed sequentially without urgency |
| Dilution strategy | Plate 3 dilutions because yields vary | Single plating concentration |
| Night-before prep | "Claim a centrifuge, set to 4°C" | Starts protocol on Day 1 morning |
