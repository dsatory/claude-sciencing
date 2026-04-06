---
description: Diagnose failed experiments — systematic root cause analysis with ranked causes and diagnostic experiments
argument-hint: [symptom description, e.g., "no colonies after transformation, Gibson assembly"]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch
---

# Experimental Troubleshooting

Systematically diagnose failed experiments. The `lab-workflow` skill provides detailed failure mode tables in `references/troubleshooting.md`.

## Workflow

1. **Define the failure precisely:**
   - What happened? (no colonies, low yield, wrong band, contamination, no activity)
   - What was expected?
   - What worked before? What changed?

2. **Rank causes by likelihood** (Occam's razor):
   1. User error (most common — wrong reagent, missed step, timing)
   2. Reagent failure (expired, degraded, wrong concentration)
   3. Equipment failure (temperature off, pipette miscalibrated)
   4. Biological variability (strain instability, plasmid loss)
   5. Protocol limitation (method not suitable for this case)

3. **Suggest diagnostic experiments** — minimum effort to identify the cause:
   - Each diagnostic should take ≤1 day
   - Test one variable at a time
   - Use materials already in the lab

4. **Provide specific fixes** for each probable cause

## Output Format

```
## Diagnosis: [Symptom]

### Most Likely Causes (ranked)

| # | Cause | Likelihood | Diagnostic Experiment | Time |
|---|-------|-----------|----------------------|------|
| 1 | [Most likely] | High | [Quick test] | 1 h |
| 2 | [Second] | Medium | [Quick test] | 2 h |
| 3 | [Third] | Medium | [Test] | 1 day |

### Immediate Actions (try right now)
1. [Fastest thing to check — e.g., "verify antibiotic plate is correct"]
2. [Second fastest]

### Diagnostic Decision Tree
- Run diagnostic 1 → if positive → [fix]
                    → if negative → run diagnostic 2 → ...

### Fixes
For each cause, provide a specific protocol-level fix.

### Prevention
How to prevent this from happening again.
```

## Troubleshooting Principles

- **Start with the stupidest possible explanation.** Wrong tube, wrong plate, expired reagent. Check these first.
- **Positive controls are diagnostic gold.** If your positive control works, the system is functional and the problem is with your specific sample.
- **Change one thing at a time** when testing fixes (unless running a proper controlled experiment).
- **Document what failed and why** — future you (and your colleagues) will thank you.
- **If it's never worked before**, it's a development problem, not a troubleshooting problem. Different approach needed.
