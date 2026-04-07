---
description: Search scientific literature — PubMed, preprints, patents, and web sources. Also scans internal channels (Slack, Google Drive) for related past/current/future projects. Find papers, build reading lists, map landscapes.
argument-hint: [query or topic] [optional flags: --recent, --reviews, --patents, --clinical, --no-internal, --limit N]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch, mcp__claude_ai_PubMed__search_articles, mcp__claude_ai_PubMed__get_article_metadata, mcp__claude_ai_PubMed__get_full_text_article, mcp__claude_ai_PubMed__find_related_articles, mcp__claude_ai_PubMed__lookup_article_by_citation, mcp__claude_ai_PubMed__convert_article_ids, mcp__claude_ai_PubMed__get_copyright_status, mcp__claude_ai_Slack__slack_search_public, mcp__claude_ai_Slack__slack_search_public_and_private, mcp__claude_ai_Slack__slack_read_channel, mcp__claude_ai_Slack__slack_read_thread
---

# Scientific Literature Search

Search, discover, and compile scientific literature. Parse $ARGUMENTS for the search query and any flags.

## Search Strategy

When the user provides a topic or question, build a systematic search:

### Step 0: Internal Project Discovery (runs first unless `--no-internal`)

Before searching external literature, scan internal channels for related past, current, or planned projects. Colleagues may have already written proposals, run experiments, or shared papers on closely related topics. This step prevents duplicating work and surfaces reusable assets.

**What to search for:**
- Same or similar target molecules / product classes
- Same or related organisms / strains
- Similar assays, analytical methods, or reaction types
- Related proposals or technical approaches
- Relevant experimental data or preliminary results

**Where to search:**

1. **Slack** — use `slack_search_public_and_private` with multiple query variations:
   - Direct topic terms: `"lignin depolymerization"`, `"muconic acid"`, `"vanillin biosynthesis"`
   - Broader class terms: `"aromatic catabolism"`, `"lignin valorization"`, `"phenolic compounds"`
   - Method terms: `"biological funneling"`, `"reductive catalytic fractionation"`
   - Project/proposal terms: search for specific program names, solicitation numbers, or project keywords
   - Key channels to prioritize: `#tech-papers`, project-specific channels, `#science`, `#proposals`
   - When a relevant thread is found, read it fully with `slack_read_thread` — context and replies often contain the most valuable information (links, data, feedback)

2. **Google Drive (locally synced)** — scan for related documents:
   - Search `~/Library/CloudStorage/GoogleDrive-*/` for matching keywords in filenames
   - Look for `.gdoc`, `.gslides`, `.gsheet`, `.docx`, `.pptx`, `.pdf` files
   - Common locations: shared drives, project folders, proposal drafts
   - For `.gdoc`/`.gslides` files: read the pointer to get the `doc_id`, note the title and path — the user can export and review these later
   - For actual files (`.docx`, `.pdf`, `.pptx`): these can be read directly

3. **Local project directories** — check for existing literature folders, proposals, or reports in the current working directory and nearby project directories that might contain related work

**Output: Internal Discovery Summary**

```markdown
## Internal Project Discovery: [Topic]

### Related Projects Found

| Source | Project/Document | Relevance | Key Assets |
|--------|-----------------|-----------|------------|
| Slack #tech-papers | Thread on [related topic] (2025-11) | High — same product class | 3 shared PDFs, protocol link |
| Slack #project-channel | Proposal draft discussion | High — same program | Draft proposal, reviewer feedback |
| GDrive Shared Drive | "[Topic]_Proposal_v2.gdoc" | High — prior proposal | Reusable lit review, comparison tables |
| GDrive My Drive | "[Related_Topic]_Slides.gslides" | Medium — related approach | Pathway diagrams, strain data |
| Local ./literature/ | Existing PDF library (23 papers) | High — prior search | Already downloaded and categorized |

### Reusable Assets
- **Prior proposals:** [list with paths/links — can reuse lit reviews, comparison tables, preliminary data sections]
- **Existing strain data:** [any experimental results shared in Slack or stored in Drive]
- **Previously shared papers:** [PDFs from Slack that may not be in your library yet]
- **Contacts:** [people who posted about related work — potential collaborators or sources of expertise]

### Recommendation
[Brief assessment: how much of the literature search is already done, what can be reused vs. what needs fresh searching]
```

If no internal results are found, note that and proceed directly to external search. Don't spend excessive time on internal search if the topic is clearly novel to the organization.

---

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
