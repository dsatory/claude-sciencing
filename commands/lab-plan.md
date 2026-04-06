---
description: Design rigorous experiments — controls, replicates, statistical power, DOE, timelines
argument-hint: [experiment description] [optional: --doe, --controls, --timeline]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch
---

# Experimental Planning

Design a rigorous experiment with appropriate controls, replicates, and statistical planning. The `lab-workflow` skill provides detailed guidance in `references/planning.md`.

## Workflow

1. **Define the experiment:** What hypothesis or question? What variables?
2. **Design controls:** Positive, negative, vehicle/mock for every condition
3. **Plan replicates:** Biological (minimum 3) and technical replicates
4. **Choose readout:** What are you measuring? How? When?
5. **Plan statistics:** What test will you use? Is n sufficient?
6. **Build timeline:** Day-by-day plan with milestones

## Flags

### --doe (Design of Experiments)
Generate a DOE matrix for multi-factor optimization:
- Identify factors and levels
- Recommend design type (full factorial, fractional, Plackett-Burman, CCD)
- Generate the experimental matrix with randomized run order
- Specify analysis plan (main effects, interactions, response surface)

### --controls
Focus on control design — generate a comprehensive controls table for the experiment.

### --timeline
Generate a day-by-day Gantt-style timeline with all steps, incubation times, and decision points.

## Output Format

```
## Experiment: [Title]

### Hypothesis
[Specific, testable statement]

### Variables
- Independent: [what you're changing]
- Dependent: [what you're measuring]
- Controlled: [what you're keeping constant]

### Experimental Design
| Condition | Description | n | Controls |
|-----------|-------------|---|----------|

### Controls
| Control | Type | Purpose |
|---------|------|---------|

### Statistical Plan
- Test: [specific test]
- Power analysis: [minimum n to detect X effect at α=0.05, power=0.80]
- Multiple comparison correction: [if applicable]

### Timeline
| Day | Activity | Duration | Notes |
|-----|----------|----------|-------|

### Materials Needed
[Itemized list with quantities]

### Success Criteria
- Primary: [quantitative threshold]
- Secondary: [additional endpoints]
```
