---
description: Scientific editing and revision — clarity, tone, logical flow, jargon reduction
argument-hint: [file path or paste text] [optional focus: clarity | tone | jargon | flow | topic-sentences]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write
---

# Scientific Editing and Revision

Review and improve scientific text for clarity, conciseness, tone, and logical flow. Read the target file or text from $ARGUMENTS.

## Input Handling

1. If $ARGUMENTS contains a file path, read that file
2. If $ARGUMENTS contains a focus keyword (clarity, tone, jargon, flow, topic-sentences), apply that lens
3. If no focus specified, perform a comprehensive review covering all areas
4. If no file or text provided, ask the user what to edit

## Editing Passes

Apply the following passes. When a specific focus is requested, prioritize that pass but still flag critical issues from other categories.

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
