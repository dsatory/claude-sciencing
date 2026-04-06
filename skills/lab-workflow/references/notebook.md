# Lab Notebook Documentation

Generating properly formatted lab notebook entries for experimental documentation and IP protection.

## Lab Notebook Principles

A lab notebook is a **legal document**. In patent disputes, it establishes who conceived what, when, and whether the invention was reduced to practice. Even if your organization uses electronic lab notebooks (ELN), the principles are the same.

### Core Requirements
1. **Permanent and tamper-evident** — ink (not pencil), no white-out, no torn pages
2. **Contemporaneous** — written the day the work is done, not weeks later
3. **Complete** — enough detail for another scientist to reproduce the work
4. **Signed and witnessed** — by the experimenter AND a witness who understands the work (for IP)

## Notebook Entry Format

### Entry Header
```
Date: YYYY-MM-DD
Project: [Project name / code]
Experiment: [Descriptive title, e.g., "Gibson assembly of pET28a-GFP-His6"]
Objective: [One sentence: what you're trying to do and why]
Reference: [Protocol SOP number, previous notebook entry, or literature reference]
```

### Materials and Methods
- List all reagents with lot numbers, expiration dates, concentrations
- Note any deviations from standard protocol (and why)
- Include equipment IDs for calibrated instruments
- Record environmental conditions if relevant (room temp, humidity)

### Procedure (as executed)
- Step-by-step what was actually done (not what the protocol says — what YOU did)
- Note exact times, temperatures, volumes
- Record observations in real-time: "culture appeared turbid at 2 h" "pellet was brown, not white"
- Attach or reference raw data: gel images, spectra, chromatograms, plate reader files

### Results
- Quantitative results with units
- Pass/fail against success criteria
- Observations (color, consistency, unexpected findings)
- Attach labeled images (gels, plates, microscopy)

### Conclusions
- What worked, what didn't, why
- What you learned
- Next steps (specific: "repeat with 0.1 mM IPTG" not "optimize expression")

### Signatures
```
Recorded by: _________________ Date: ___________
Witnessed by: _________________ Date: ___________
```

The witness should be someone who can understand the work but is NOT a co-inventor.

## IP-Sensitive Documentation

When the `--ip` flag is used, add these additional elements:

### Conception Record
Document the moment a new idea is formed:
- **What is the invention?** Describe it clearly and completely
- **When was it conceived?** Date of first documentation
- **Who conceived it?** Everyone who contributed to the inventive concept
- **What problem does it solve?** Prior art limitations addressed
- **How does it work?** Mechanism, not just "it works"

### Reduction to Practice
Document that the invention actually works:
- **Constructive reduction:** Filing a patent application with enablement
- **Actual reduction:** Experimental demonstration that it works for its intended purpose
- Record the first successful experiment with full data
- Note that the inventor recognized the result as a success (not just a data point)

### Prior Art Awareness
- Document what you knew about existing methods when you started
- Note how your approach differs
- If you become aware of new prior art during the work, document that too

### Diligence Records
If there's a gap between conception and reduction to practice:
- Document ongoing efforts (failed experiments count!)
- Show continuous work toward realizing the invention
- Gaps with no documented activity weaken patent claims

## Electronic Lab Notebook (ELN) Considerations

If generating entries for an ELN system:
- Follow the system's template structure
- Attach data files in supported formats
- Use the system's built-in witnessing/signing workflow
- Include cross-references to related entries (linked, not just mentioned)
- Tag entries with project codes, keywords for searchability

## Notebook Entry Generation

When generating a notebook entry:
1. Ask the user for the experiment details (or extract from conversation context)
2. Format using the template above
3. Include all quantitative data mentioned
4. Flag any missing information that should be recorded ("[NOTE: Record lot number of competent cells]")
5. If `--ip` flag, add the IP documentation sections
6. Output as markdown or in the user's preferred ELN format
