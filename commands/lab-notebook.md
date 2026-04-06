---
description: Generate formatted lab notebook entries with proper documentation for reproducibility and IP protection
argument-hint: [experiment description or context] [optional: --ip, --eln, --template]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write
---

# Lab Notebook Entry Generation

Generate properly formatted lab notebook entries. The `lab-workflow` skill provides detailed guidance in `references/notebook.md`.

## Workflow

1. **Gather experiment details** from the conversation context or ask the user
2. **Format the entry** using the standard template
3. **Flag missing information** that should be recorded
4. **Output** as markdown (default) or ELN format

## Flags

### --ip
Add IP-sensitive documentation sections:
- **Conception record:** When was this idea first conceived? By whom? What problem does it solve?
- **Reduction to practice:** First successful demonstration with data
- **Prior art awareness:** What existing methods were you aware of?
- **Diligence records:** Continuous effort between conception and reduction to practice
- Remind the user about witness signatures and filing timelines

### --eln
Format for electronic lab notebook systems:
- Structured fields instead of free text
- Metadata tags (project code, experiment type, organism, technique)
- Cross-reference links to related entries
- Attachment placeholders for data files

### --template
Output a blank template the user can fill in, rather than generating from context.

## Entry Format

```markdown
# Lab Notebook Entry

**Date:** YYYY-MM-DD
**Project:** [Project name / code]
**Experiment:** [Descriptive title]
**Objective:** [What you're doing and why, one sentence]
**Reference:** [Protocol SOP#, previous entry, or literature ref]

## Materials
| Reagent | Catalog # | Lot # | Concentration | Amount |
|---------|-----------|-------|--------------|--------|

## Procedure (as executed)
1. [Step with specific volumes, temperatures, times]
2. [Note any deviations from protocol and why]
3. ...

## Observations
- [Real-time notes: appearance, timing, unexpected events]

## Results
- [Quantitative results with units]
- [Attach: gel image, chromatogram, plate reader data]

## Conclusions
- [What worked / didn't work / what was learned]
- **Next steps:** [Specific actions]

---
Recorded by: _________________ Date: ___________
Witnessed by: _________________ Date: ___________
```

## From Conversation Context

When generating entries from an ongoing conversation:
- Extract all experimental details mentioned
- Organize chronologically
- Include all quantitative data
- Flag any gaps: `[NOTE: Record lot number of X]` or `[NOTE: Attach gel image]`
- If the user discussed troubleshooting, include the diagnosis and resolution

## IP Documentation Addendum (--ip)

```markdown
## IP Documentation

### Conception
- **Date of conception:** [When the idea was first documented]
- **Inventors:** [Names of all who contributed to the inventive concept]
- **Problem solved:** [What limitation of existing methods does this address?]
- **Novel aspect:** [What is new about this approach?]

### Reduction to Practice
- **Date of first successful experiment:** [Date]
- **Key result demonstrating the invention works:** [Data]
- **Inventor recognized success:** [Yes — describe the moment/context]

### Prior Art
- **Known existing methods at time of conception:**
  - [Method 1 — limitation]
  - [Method 2 — limitation]
- **How this invention differs:** [Specific technical distinction]

### Disclosure Status
- **Public disclosures:** [None / List with dates and venues]
- **Filing deadline:** [1 year from first public disclosure (US); ASAP for international]
```
