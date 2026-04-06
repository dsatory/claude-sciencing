---
description: Brainstorm experimental approaches for a research question — generate, evaluate, and prioritize strategies
argument-hint: [research question or goal]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch
---

# Experimental Ideation

Brainstorm experimental approaches for the user's research question. The `lab-workflow` skill provides detailed guidance in `references/ideation.md`.

## Workflow

1. **Restate the question** as a specific, testable goal. Ask for missing details (organism, current performance, constraints, what's been tried).

2. **Generate 4-8 approaches**, each with:
   - **What:** One-sentence description
   - **Why it might work:** Mechanism or rationale
   - **Effort:** Low / Medium / High
   - **Risk:** Low / Medium / High
   - **Timeline:** Days / Weeks / Months
   - **Prerequisites:** What you need first

3. **Prioritize** into a recommended strategy:
   - Start with lowest-effort, highest-information experiments
   - Run independent approaches in parallel where possible
   - Include clear decision points ("if X doesn't work by week 2, try Y")

4. **Identify the "Monday morning" experiment** — something that takes <1 day, costs almost nothing, and could resolve the issue or provide critical information immediately.

## Output Format

```
## Goal: [Restated specific goal]

### Quick Win (try first)
[Lowest-effort experiment that could work immediately]

### Recommended Strategy
| # | Approach | Effort | Risk | Timeline | Rationale |
|---|----------|--------|------|----------|-----------|
| 1 | ... | Low | Low | 1 day | ... |
| 2 | ... | Low | Med | 1 week | ... |

### Decision Tree
- Week 1: Try approaches 1-2
  - If 1 works → scale up, proceed to ...
  - If not → try approach 3
- Week 2-3: ...

### What NOT to Try (and why)
[Common approaches that seem obvious but won't work here, with explanation]
```
