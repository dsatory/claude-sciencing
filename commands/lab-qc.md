---
description: Generate QC checklists and acceptance criteria for purification steps, assays, and lab processes
argument-hint: [process or step, e.g., "post-IMAC", "post-cloning", "fermentation harvest"]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write
---

# Quality Control Checklists

Generate QC checklists with specific acceptance criteria. The `lab-workflow` skill provides detailed QC tables in `references/qc.md`.

## Workflow

1. **Identify the process** from $ARGUMENTS (post-IMAC, post-cloning, fermentation, DNA prep, etc.)
2. **Generate a checklist** with:
   - Each QC check as a row
   - Method for each check
   - Specific acceptance criteria (quantitative where possible)
   - What to do if a check fails
3. **Include documentation requirements** (what to record, how to archive)

## Output Format

```
## QC Checklist: [Process]

| # | Check | Method | Acceptance Criteria | If Fail |
|---|-------|--------|-------------------|---------|
| 1 | ... | ... | ... | ... |

### Required Documentation
- [ ] Raw data attached (gel image, chromatogram, spectrum)
- [ ] Results recorded with units
- [ ] Pass/fail marked for each check
- [ ] Analyst signature and date
- [ ] Reviewer signature (if GLP/GMP)

### Notes
[Process-specific notes, common pitfalls, tips]
```

## Common QC Processes

Recognize and generate checklists for:
- **post-IMAC** — purity, identity, concentration, activity, endotoxin
- **post-cloning** — colony PCR, sequencing, restriction digest, miniprep QC
- **post-expression** — SDS-PAGE, solubility, yield estimate
- **post-purification** (any step) — purity, recovery, activity retention
- **DNA/RNA prep** — concentration, purity ratios, integrity
- **fermentation harvest** — OD, titer, pH, viability, sterility
- **competent cells** — transformation efficiency (CFU/µg with pUC19)
- **media/buffer prep** — pH, sterility, component verification
- **instrument calibration** — pipettes, pH meter, spectrophotometer, balance

If the user's process isn't in the list, ask what they're checking and build a custom checklist.
