---
description: Scientific editing and revision — grammar, spelling, typos, clarity, tone, logical flow, jargon reduction. Works on any document type including .md, .docx, .tex, .txt, and pasted text.
argument-hint: [file path or paste text] [optional focus: grammar | clarity | tone | jargon | flow | topic-sentences]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write
---

# Scientific Editing and Revision

Review and improve scientific text for clarity, conciseness, tone, and logical flow. Read the target file or text from $ARGUMENTS.

## Input Handling

1. If $ARGUMENTS contains a file path, read that file
2. If $ARGUMENTS contains a focus keyword (clarity, tone, jargon, flow, topic-sentences), apply that lens
3. If no focus specified, perform a comprehensive review covering all areas
4. If no file or text provided, ask the user what to edit

### Supported File Formats

- **`.md`, `.tex`, `.txt`** — read and edit directly
- **`.docx`** — read via python-docx, apply edits, save back
- **`.pdf`** — read for review/feedback only (cannot write back to PDF)
- **`.gdoc`** — Google Drive pointer file. Extract `doc_id` from JSON, open export URL in browser to download as `.docx`. Edit the exported `.docx`.

## Editing Passes

Apply the following passes. When a specific focus is requested, prioritize that pass but still flag critical issues from other categories.

### Pass 0: Grammar, Spelling, and Typos

Always run this pass first, regardless of the requested focus.

- Fix spelling errors and typos (including scientific terms: species names, chemical names, gene names)
- Correct grammar: subject-verb agreement, dangling modifiers, comma splices, run-on sentences, incorrect prepositions
- Fix punctuation: missing or misplaced commas, semicolons used as commas, inconsistent serial comma usage
- Flag homophones and near-misses common in scientific writing: effect/affect, principal/principle, compliment/complement, discrete/discreet, elicit/illicit, ensure/insure, than/then
- Check hyphenation: compound modifiers before nouns ("well-characterized enzyme" but "the enzyme is well characterized"), standard prefixes (non-, pre-, post-, co-)
- Verify number-word consistency: spell out numbers below 10 except with units (see scientific-style guidelines)
- Check for accidental word repetition ("the the", "of of") and missing words

### Pass 1: Clarity and Conciseness

- Identify sentences longer than 35 words and suggest splitting or tightening
- Flag nominalizations (e.g., "the utilization of" to "using", "the determination of" to "determining")
- Remove filler phrases: "it is well known that", "it is important to note that", "interestingly", "it should be noted"
- Eliminate redundancies: "completely abolished", "novel and new", "future plans"
- Replace weak verb constructions with direct verbs: "carried out an analysis" to "analyzed"
- Flag stacked prepositional phrases (three or more in sequence)

### Pass 2: Passive Voice Assessment

Apply context-sensitive passive voice evaluation:

- **Methods section:** Passive voice is standard and acceptable. Do not flag passive constructions in Methods unless they create genuine ambiguity about who performed an action.
- **Results section:** Prefer active voice for describing findings ("We observed..." or "The assay revealed...") but passive is acceptable for established procedures.
- **Introduction and Discussion:** Flag excessive passive voice. These sections benefit from active constructions that clarify attribution and strengthen arguments.
- **When flagging passive voice:** Provide the active alternative and explain why it improves the sentence, rather than applying a blanket rule.

### Pass 3: Scientific Tone Consistency

- Flag informal language that undermines credibility (e.g., "a lot of", "pretty much", "stuff")
- Identify overclaiming: "proves" (in most biological contexts, use "demonstrates" or "suggests"), "the first" (unless verifiably true), "breakthrough"
- Flag underclaiming: Excessive hedging that buries findings ("it might perhaps be possible that there could be an effect")
- Balance appropriate hedging ("these data suggest") with confident statements where evidence warrants them
- Check for consistent tense usage: present tense for established facts and the current study's conclusions, past tense for methods and specific results

### Pass 4: Jargon and Audience Calibration

- Identify technical terms that could be replaced or defined for broader audiences
- Flag acronyms used before definition
- Suggest parenthetical definitions for specialized terms on first use
- When the user specifies a target audience (e.g., "general science audience" vs "specialist reviewers"), calibrate accordingly
- Note: some jargon is necessary and efficient for specialist audiences. Do not simplify terms that would lose precision for the intended readership.

### Pass 5: Logical Flow Between Paragraphs

- Check that each paragraph begins with a topic sentence that signals its role in the argument
- Verify that the last sentence of each paragraph connects to the first sentence of the next
- Flag paragraphs that introduce multiple unrelated ideas
- Identify paragraphs where the topic sentence promises one thing but the body delivers another
- Suggest transitional phrases or bridging sentences where the connection between paragraphs is unclear

### Pass 6: Topic Sentence Strengthening

When invoked with the "topic-sentences" focus:

- Extract all topic sentences (first sentence of each paragraph)
- Present them as a sequential list — this list alone should tell the story of the paper
- Flag topic sentences that are:
  - Too vague ("Several factors are involved")
  - Backward-looking rather than forward-looking ("As mentioned above")
  - Missing a claim or assertion (purely descriptive without advancing the argument)
- Suggest stronger alternatives that state the paragraph's contribution to the overall argument

## Output Format

Present edits in this structure:

1. **Summary:** 2-3 sentence overview of the text's current strengths and main areas for improvement
2. **Line-by-line edits:** For each suggested change, show:
   - The original text
   - The suggested revision
   - A brief rationale (1 sentence)
3. **Structural suggestions:** Any higher-level recommendations about paragraph order, missing content, or section organization
4. **Priority ranking:** Order suggestions from most impactful to least

When editing files directly (if the user requests changes be applied), preserve all content that is not being revised. Make changes incrementally and confirm significant restructuring before applying.

## Domain-Specific Conventions

- For clinical studies, verify that reporting aligns with CONSORT (randomized trials) or STROBE (observational studies) guidelines where applicable
- For animal studies, check for ARRIVE guideline compliance: sample sizes, randomization, blinding, exclusion criteria
- For systematic reviews, note PRISMA adherence if relevant
- Flag statistical reporting issues: missing effect sizes, confidence intervals reported without point estimates, misuse of "significant" without specifying statistical significance

---

## Mode: Peer Review (invoked with `review` focus or `--peer-review`)

Generate a structured peer review of the document as if reviewing for a journal or funder. This is a pre-submission self-assessment — identify weaknesses before reviewers do.

### Review Format

Select the venue format based on the document type or user specification:

**For journal manuscripts (default):**

```markdown
## Peer Review: [Document Title]

### Overall Assessment
**Recommendation:** Accept / Minor Revisions / Major Revisions / Reject
**Confidence:** High / Medium / Low (based on reviewer domain expertise match)

### Summary (2-3 sentences)
[What the paper does and its main contribution]

### Strengths
1. [Specific strength with evidence from the text]
2. [Another strength]
3. [...]

### Weaknesses
1. [Specific weakness — what's missing, unclear, or unsupported]
2. [Another weakness]
3. [...]

### Detailed Comments

#### Significance / Novelty
- What is the advance over prior work?
- Is the novelty clearly stated and substantiated?

#### Technical Rigor
- Are methods appropriate and sufficiently described?
- Are controls adequate?
- Are statistical analyses appropriate?
- Is the data quality sufficient to support the conclusions?

#### Presentation / Clarity
- Is the writing clear and concise?
- Are figures and tables effective?
- Is the logical flow sound?

#### Missing Elements
- [Experiments, controls, analyses, or discussions that should be added]

### Minor Comments
- [Line-level suggestions: typos, unclear phrasing, formatting]

### Questions for Authors
1. [Questions that a reviewer would ask]
```

**For grant proposals (DARPA, DOE, NIH, etc.):**

```markdown
## Review: [Proposal Title]

### Overall Score: [1-10]

### Evaluation Criteria Scores
| Criterion | Score (1-10) | Comments |
|-----------|-------------|----------|
| Technical Approach | | |
| Innovation | | |
| Team Qualifications | | |
| Management / Schedule | | |
| Cost Reasonableness | | |

### Strengths
1. [...]

### Weaknesses
1. [...]

### Risk Assessment
- Are risks identified and mitigated?
- Are go/no-go criteria quantitative and unambiguous?

### Recommendations
- [What would make this proposal competitive]
```

### Ensemble Review Mode (inspired by AI Scientist)

For high-stakes documents (proposals before submission, manuscripts before journal submission), run an **ensemble review** with multiple independent perspectives:

**Step 1: Generate 3 independent reviews with different biases:**

1. **Critical reviewer** — "Be a harsh critic. If a claim is unsupported or you're unsure, flag it as a weakness. Look for methodological gaps, missing controls, and unsupported conclusions."
2. **Constructive reviewer** — "Be constructive. Identify both strengths and weaknesses fairly. Focus on what would make this work stronger, not just what's wrong."
3. **Domain expert reviewer** — "Review from the perspective of an expert in [specific field]. Focus on whether the technical approach is sound, the benchmarks are appropriate, and the conclusions are justified by the data."

Each review follows the same structured format (journal or grant format above).

**Step 2: Meta-review (aggregation):**

After generating 3 independent reviews, synthesize them into a single **meta-review**:

```markdown
## Meta-Review: [Document Title]

### Consensus Strengths
[Issues all 3 reviewers agreed are strong]

### Consensus Weaknesses
[Issues flagged by 2+ reviewers — these are the real problems]

### Divergent Opinions
[Issues where reviewers disagreed — discuss why]

### Aggregated Scores
| Dimension | R1 | R2 | R3 | Average |
|-----------|----|----|----| --------|

### Priority Actions (ranked by consensus)
1. [Most critical fix — flagged by all reviewers]
2. [Second priority — flagged by 2 reviewers]
3. [...]

### Overall Recommendation
[Accept / Revise / Reject based on consensus]
```

This catches issues that a single review perspective misses and provides more reliable quality assessment.

### Self-Critique Reflection Loop

After each editing pass (clarity, tone, flow, or peer review), run a **reflection step**:

> "Re-read your edits/review. Is there anything you missed, got wrong, or could improve? Consider: did you miss any errors in the original text? Were your suggestions actually improvements or just different? Are there inconsistencies between your suggestions? Refine your output. If nothing needs changing, state 'I am done.'"

Iterate up to 3 times. Exit early if the reflection produces no changes. This catches errors in the editor's own output — a common failure mode where the editing introduces new problems.

### Review Principles

- **Be specific** — "The statistical analysis is weak" is useless. "Section 3.2 reports p < 0.05 for 12 comparisons without correction for multiple testing" is actionable.
- **Distinguish fatal from fixable** — clearly separate issues that undermine the core contribution from those that can be addressed in revision.
- **Assess the claims against the evidence** — not whether you agree with the hypothesis, but whether the evidence supports the conclusions drawn.
- **Check for missing comparisons** — are the right baselines and benchmarks used? Are state-of-the-art comparisons current?
- **Flag citation gaps** — are key papers in the field cited? Are the citations current?
