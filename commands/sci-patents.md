---
description: Search, download, analyze, and map patent landscapes — find active and pending patents, distill claims, assess freedom-to-operate, and compare against project objectives
argument-hint: [mode] [query or patent number]. Modes: search, download, analyze, landscape
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch, mcp__claude_ai_PubMed__get_article_metadata, mcp__claude_ai_PubMed__convert_article_ids
---

# Patent Search, Download & Landscape Analysis

Unified patent workflow: search → download → analyze → landscape report. Parse $ARGUMENTS for the mode and query.

## Modes

### search — Find relevant patents

Search for patents related to a topic, compound, method, or organism.

**Sources (query ALL of them):**
- **Google Patents** (`patents.google.com`) — broadest coverage, full text, US/EP/WO/CN/JP/KR
- **USPTO** — US granted patents and published applications
- **Espacenet** — European Patent Office, international coverage
- **WIPO PatentScope** — PCT applications
- **Lens.org** — uniquely cross-references patents ↔ scholarly literature

**Search strategy:**
1. **Keyword search:** Start broad, then narrow. Use key technical terms, compound names, organism names, method names.
2. **CPC classification codes** for precision:
   - C12P — fermentation/bioprocessing
   - C12N — microorganisms/enzymes/genetic engineering
   - C07C/C07D — organic chemistry (specific compound classes)
   - C08G/C08L — polymers
   - B01J — catalysis
3. **Assignee/inventor search:** Track specific competitors or academic groups
4. **Citation search:** Find patents that cite or are cited by a known relevant patent

**Filter results by:**
- **Active patents** — granted and in force (maintenance fees paid). These constrain your work.
- **Pending applications** — published but not yet granted. Claims may change during prosecution. Signal intent.
- **Expired/abandoned** — note for prior art purposes only. They don't constrain your work.
- Default to last 20 years unless the field has older foundational patents.

**Output:**

```markdown
## Patent Search Results: [Topic]

### Active Patents (Granted, In Force)
| # | Patent No. | Title | Assignee | Filed | Granted | Expiry | Key Claims Summary |
|---|-----------|-------|----------|-------|---------|--------|-------------------|

### Pending Applications
| # | Pub. No. | Title | Applicant | Filed | Key Claims (may change) |
|---|---------|-------|-----------|-------|------------------------|

### Recently Expired (Prior Art Reference)
| # | Patent No. | Title | Former Assignee | Expired |
|---|-----------|-------|-----------------|---------|

Found [N] active patents, [N] pending applications, [N] expired.
```

---

### download — Retrieve Patent Claims and Metadata

Patents are **always free** — they are public documents. The claims (the only legally enforceable part) are available directly from Google Patents HTML pages. **Do not waste time downloading patent PDFs unless the user specifically asks for them.** Claims text from the web page is sufficient for FTO analysis, landscape mapping, and design-around work.

#### Primary method: WebFetch from Google Patents (preferred)

For any patent number, fetch the claims and metadata directly:

```
WebFetch: https://patents.google.com/patent/{PATENT_NUMBER}/en
Prompt: "Extract from this patent page: (1) patent number, (2) title, (3) assignee, (4) all inventor names, (5) filing date, (6) grant date if granted, (7) estimated expiry date, (8) status (active/pending/expired/abandoned), (9) ALL independent claims (full text), (10) key dependent claims, (11) abstract. Return structured text."
```

**This single call provides everything needed for patent analysis.** No PDF required.

**Examples:**
```
WebFetch: https://patents.google.com/patent/US10047364B2/en
WebFetch: https://patents.google.com/patent/WO2016198529A1/en
WebFetch: https://patents.google.com/patent/US20160304917A1/en
```

#### When to download the PDF

Only download the full patent PDF when:
- The user explicitly requests it ("download the patent PDF")
- You need to read the specification/examples in detail (not just claims)
- The patent has figures or sequence listings you need to examine

**PDF download sources (if needed):**
1. **Browser fallback** — `open "https://patents.google.com/patent/{number}/en"` → user downloads from the page
2. **USPTO** — `https://pdfpiw.uspto.gov/.piw?docid={number}`
3. **Espacenet** — "Original document" PDF link
4. **Google Patents PDF API** — `https://patentimages.storage.googleapis.com/pdfs/{number}.pdf` (often blocked by curl; use browser)

**Naming convention (when PDFs are downloaded):**
```
USPat_description_year.pdf      — US granted patent
USApp_description_year.pdf      — US published application
EPPat_description_year.pdf      — European patent
WOApp_description_year.pdf      — WIPO/PCT application
```

**Storage:** Always sort into the dedicated `XX_Patents/` folder in the literature directory (numbered last in the category structure). Do not mix patents with research papers.

#### Metadata to capture for each patent (from WebFetch)

- Patent/publication number
- Title
- Assignee and inventors
- Filing date, grant date (if granted), estimated expiry
- Status: Active / Pending / Expired / Abandoned
- **All independent claims (full text)** — this is the most important field
- Key dependent claims that narrow scope
- CPC classification codes (useful for broadening patent searches)

---

### analyze — Analyze a specific patent

Read a patent and produce a structured analysis. Follows the patent-analysis protocol from the `scientific-reading` skill.

**Input:** Patent number, PDF path, or URL.

**Output:**

```markdown
## Patent Analysis: [Patent Number]

**Title:** [Full title]
**Assignee:** [Company/university]
**Inventors:** [Names]
**Filed:** [Date] | **Granted:** [Date] | **Expiry:** [Estimated date]
**Status:** Active / Pending / Expired

### Independent Claims

**Claim 1:** [Full text of broadest independent claim]

Element-by-element breakdown:
| Element | Scope | Notes |
|---------|-------|-------|
| [Element A] | [Broad/narrow] | [What it covers] |
| [Element B] | [Broad/narrow] | [What it covers] |

**Claim N:** [Any additional independent claims — method, composition, system]

### Dependent Claims Summary
- Claim 2 (depends on 1): narrows to [specific limitation]
- Claim 3 (depends on 1): narrows to [specific limitation]

### Design-Around Opportunities
For each independent claim, identify elements that could be changed to avoid infringement:
1. [Element X] could be replaced with [alternative] — [feasibility assessment]
2. [Element Y] is narrowly defined to [scope] — using [different approach] would avoid this

### Prior Art Vulnerabilities
- [Published paper/patent that predates this claim and may invalidate it]
- [Enablement concerns — are the claims supported by the examples?]

### Key Takeaway
[One paragraph: what this patent actually protects in practice, and what it doesn't]
```

---

### landscape — Full patent landscape analysis

Combines search + analysis into a comprehensive landscape report. This is the most thorough mode — use for project planning, proposal preparation, or FTO assessments.

**Input:** Topic description, technical approach, or project objectives.

**Output:**

```markdown
# Patent Landscape: [Topic]
Generated: [Date]

## Executive Summary
[2-3 sentences: how crowded is the space, who are the key players, what's the overall risk level]

## Active Patents (Granted, In Force)

### [Patent 1: US XX,XXX,XXX — Title]
**Assignee:** [Company] | **Expiry:** [Date]
**Broadest claim:** [Plain-language summary]
**Key limitations:** [What narrows the scope]
**Design-around openings:** [What could be changed to avoid]

### [Patent 2: ...]
...

## Pending Applications

### [Application 1: US 20XX/XXXXXXX — Title]
**Applicant:** [Company] | **Filed:** [Date]
**Claimed scope:** [Current claims — note: may change during prosecution]
**Prosecution status:** [If known — office actions, amendments]

## Comparison with Project Objectives

If project objectives, a proposal, or technical approach context is available:

| Patent | Overlap with Our Approach | Risk Level | Specific Concern |
|--------|--------------------------|------------|------------------|
| US XX,XXX,XXX | [Which elements match] | High/Medium/Low | [What's problematic] |
| US 20XX/XXXXXXX | [Overlap] | Medium (pending) | [Claims may narrow] |

## Feasibility Assessment

### Clear to Proceed
Aspects of the proposed research that do NOT overlap with any active patent claims:
- [Approach/method/organism that is unencumbered]

### Proceed with Caution
Aspects that overlap with pending applications or narrow claims:
- [Approach] — overlaps with [application], but claims may narrow during prosecution
- [Method] — overlaps with [patent Claim 3], but design-around via [alternative] is feasible

### Approaches to Avoid (or License)
Aspects that fall squarely within active, broadly-claimed patents:
- [Approach] — covered by [Patent, Claim 1]. Alternative: [design-around option]
- [Method] — covered by [Patent, Claim 1]. Note: patent expires [date] — may not be worth designing around

## Key Players
| Assignee | # Active Patents | # Pending Apps | Focus Area |
|----------|-----------------|----------------|------------|

## Recommended Actions
- [ ] Consult IP counsel on [specific patents] before [specific activities]
- [ ] Consider design-around for [approach] by [alternative]
- [ ] Monitor [pending application] — prosecution may narrow claims
- [ ] Review [expired patent] as prior art for [purpose]
```

### When Project Objectives Are Not Available

If no project context exists, still produce the landscape with claims distillation, but replace the comparison and feasibility sections with:

```
## Note: No Project Objectives Available

Comparison and feasibility assessment require knowledge of your specific
technical approach. Provide a project proposal, technical approach document,
or brief description of planned methods to generate these sections.
```

---

## Integration with Other Commands

- **/sci-search** includes patent search by default — `/sci-patents` is for deeper, dedicated patent work
- **/sci-read patent** analyzes individual patents — `/sci-patents analyze` does the same but with more structured output and design-around focus
- **/sci-library** tracks patents alongside papers — use patent numbers as identifiers
- **/sci-draft proposal** uses landscape reports to inform risk assessment and technical approach sections

---

## General Guidance

- Always search multiple patent databases — no single source is complete
- Active patents constrain your work. Pending applications signal intent but aren't enforceable yet.
- Claims are what matter, not the specification. The spec describes everything imaginable; the claims define what's actually protected.
- Patent prosecution history (available via USPTO PAIR) reveals what was argued — this limits claim interpretation and may reveal weaknesses.
- FTO is ultimately a legal determination. This tool provides technical input (claims mapping, design-around analysis, prior art) that IP counsel needs to make the legal call.
- Never fabricate patent numbers or claim text. If you can't find a specific patent, say so.
