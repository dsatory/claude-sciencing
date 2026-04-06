---
description: Search scientific literature — PubMed, preprints, patents, and web sources. Find papers, build reading lists, map landscapes.
argument-hint: [query or topic] [optional flags: --recent, --reviews, --patents, --clinical, --limit N]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch, mcp__claude_ai_PubMed__search_articles, mcp__claude_ai_PubMed__get_article_metadata, mcp__claude_ai_PubMed__get_full_text_article, mcp__claude_ai_PubMed__find_related_articles, mcp__claude_ai_PubMed__lookup_article_by_citation, mcp__claude_ai_PubMed__convert_article_ids, mcp__claude_ai_PubMed__get_copyright_status
---

# Scientific Literature Search

Search, discover, and compile scientific literature. Parse $ARGUMENTS for the search query and any flags.

## Search Strategy

When the user provides a topic or question, build a systematic search:

### Step 1: Query Design

Construct effective search queries:
- Break the topic into key concepts
- Identify synonyms and alternative terms for each concept
- Combine with Boolean operators (AND, OR, NOT)
- Use MeSH terms for PubMed when appropriate

**Example:**
User: "engineered bacteria for succinic acid production"
→ PubMed: `("succinic acid" OR "succinate") AND ("metabolic engineering" OR "engineered" OR "recombinant") AND ("Escherichia coli" OR "Corynebacterium" OR "bacteria")`

### Step 2: Multi-Source Search

Search across sources based on the query and flags:

1. **PubMed** (default) — use PubMed MCP tools for peer-reviewed biomedical/life science literature
2. **Web search** — for preprints (bioRxiv, chemRxiv), conference proceedings, theses, and grey literature
3. **Patent search** — when `--patents` flag or when query involves commercial methods, compositions, or processes

### Step 3: Filter and Rank

Apply filters:
- `--recent` → last 2 years only
- `--reviews` → filter to review articles
- `--clinical` → filter to clinical trials or clinical data
- `--limit N` → return top N results (default: 10)

Rank results by:
1. Relevance to the query
2. Recency (newer = higher, in fast-moving fields)
3. Impact (journal, citation count if available)
4. Open access availability

### Step 4: Present Results

For each result, present:
```
### [N]. [Title]
**Authors:** First Author et al. | **Journal:** Name (Year) | **DOI:** link
**Open Access:** Yes/No
**Summary:** 2-3 sentence summary of key findings and relevance
**Key data:** [Most important quantitative result]
```

After listing results, provide:
- **Suggested reading order** (which papers to read first based on relevance)
- **Gaps identified** (what the search didn't find — terms to try next)
- **Related searches** (adjacent queries that might be useful)

---

## Search Modes

### Topic Search (default)
Broad search on a topic. Returns a curated reading list.

### Question-Driven Search
When the user asks a specific question ("What's the highest reported titer of succinic acid from E. coli?"), focus the search on finding the direct answer with supporting evidence.

### Landscape Search
When the user wants to understand "who's doing what":
- Search broadly, then organize by research group/institution
- Map active groups, their focus areas, and recent output
- Identify key labs, funding sources, and publication trends

### Prior Art Search
When the user needs to assess novelty for a patent or proposal:
- Search for the closest prior work
- Include both papers AND patents
- Focus on methods and compositions, not just results
- Note publication/filing dates (critical for priority)

### Citation Chasing
When the user provides a key paper and wants related work:
- Use PubMed's related articles feature
- Find papers that cite the key paper (forward citation)
- Find key references cited by the paper (backward citation)
- Identify the "citation network" around a core finding

---

## Building Structured Reading Lists

When the search produces many results, organize into a structured reading list:

```markdown
# Reading List: [Topic]
Generated: [Date]

## Must-Read (directly relevant)
1. [Paper] — [why it's essential]
2. [Paper] — [why it's essential]

## Important Context (background, methods, benchmarks)
3. [Paper] — [what it provides]
4. [Paper] — [what it provides]

## Worth Scanning (adjacent, emerging, or speculative)
5. [Paper] — [why it's interesting]

## Reviews (for overview)
6. [Review] — [scope and recency]
```

Save reading lists as markdown files when the user requests it.

---

## PubMed-Specific Features

When using PubMed MCP tools:

### Metadata Extraction
For each paper, extract:
- Title, authors, journal, year, DOI, PMID
- Abstract
- MeSH terms (useful for finding related papers)
- Publication type (research article, review, clinical trial, etc.)
- Open access / full text availability

### Full Text Access
- Check copyright status before attempting full text retrieval
- If open access, fetch and provide full text
- If not open access, work with the abstract and suggest the user access through their institution

### Related Articles
- Use PubMed's related articles algorithm to find similar papers
- Useful for expanding a reading list from a seed paper

### Citation Lookup
- Convert between PMID, DOI, and PMC IDs as needed
- Look up articles by citation details when the user provides partial information

---

## Output Options

- **In conversation** — present results directly (default)
- **Save to file** — `--save path/to/reading-list.md` saves a formatted reading list
- **Feed to /sci-read** — suggest the user run `/sci-read brief` on specific papers from the results
- **Feed to /sci-library** — suggest adding key papers to the reference library

---

## General Guidance

- Start with PubMed for biomedical/life science queries
- Add web search for preprints, theses, and non-indexed sources
- Always note open access status — the user needs to know if they can get full text
- For fast-moving fields, prioritize recency — a 3-year-old paper may be obsolete
- When results are thin, suggest broadening terms or trying alternative databases
- Flag review articles — they're good for orientation but cite primary sources for specific claims
