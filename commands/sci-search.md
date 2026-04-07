---
description: Search scientific literature — PubMed, preprints, patents, and web sources. Also scans internal sources (Slack, Confluence, Google Drive, Glean) for related past/current/future projects. Find papers, build reading lists, map landscapes.
argument-hint: [query or topic] [optional flags: --recent, --reviews, --no-patents, --clinical, --no-internal, --limit N]
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch, mcp__claude_ai_PubMed__search_articles, mcp__claude_ai_PubMed__get_article_metadata, mcp__claude_ai_PubMed__get_full_text_article, mcp__claude_ai_PubMed__find_related_articles, mcp__claude_ai_PubMed__lookup_article_by_citation, mcp__claude_ai_PubMed__convert_article_ids, mcp__claude_ai_PubMed__get_copyright_status, mcp__claude_ai_Slack__slack_search_public, mcp__claude_ai_Slack__slack_search_public_and_private, mcp__claude_ai_Slack__slack_read_channel, mcp__claude_ai_Slack__slack_read_thread, mcp__claude_ai_Atlassian__searchConfluenceUsingCql, mcp__claude_ai_Atlassian__getConfluencePage, mcp__claude_ai_Atlassian__getConfluencePageDescendants, mcp__claude_ai_Atlassian__getAccessibleAtlassianResources, mcp__claude_ai_Atlassian__searchAtlassian, mcp__claude_ai_Atlassian__getConfluenceSpaces
---

# Scientific Literature Search

Search, discover, and compile scientific literature. Parse $ARGUMENTS for the search query and any flags.

## Search Strategy

When the user provides a topic or question, build a systematic search:

### Pre-Flight: PubMed MCP Health Check (ALWAYS run first)

Before any search, test PubMed MCP with a simple call:

```
mcp__claude_ai_PubMed__search_articles with query="test" max_results=1
```

**If it succeeds:** PubMed MCP is operational. Use it as the primary search engine for all biomedical queries. Proceed to Step 0.

**If it fails (token expired, tool not found, authorization error):**

1. **Tell the user immediately.** Do not silently fall back to web search. Say:
   > "PubMed MCP is not available ([specific error]). This significantly reduces search quality — PubMed MCP provides structured metadata, MeSH terms, related articles, full-text access, and ID conversion that web search cannot replicate. Re-authorize at claude.ai/settings/connectors to restore full functionality."

2. **Ask if they want to re-auth now or proceed with degraded search.** Use AskUserQuestion:
   - Option 1: "I'll re-auth now" → wait, then re-test
   - Option 2: "Proceed without PubMed" → use compensating strategy below

3. **Compensating strategy — use NCBI E-utilities API directly.** Read `skills/pubmed-setup/references/eutils-api.md` for full API documentation. Key calls:

   **Search PubMed (replaces `search_articles`):**
   ```
   WebFetch: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={URL_ENCODED_QUERY}&retmax=50&retmode=json&sort=relevance
   ```
   Returns PMIDs. Then fetch metadata:

   **Get metadata (replaces `get_article_metadata`):**
   ```
   WebFetch: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={PMID1,PMID2,...}&retmode=xml&rettype=abstract
   ```

   **Convert IDs (replaces `convert_article_ids`):**
   ```
   WebFetch: https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids={DOI_or_PMID}&format=json
   ```
   If response contains `pmcid` → paper is in PMC → free PDF available.

   **Find related articles (replaces `find_related_articles`):**
   ```
   WebFetch: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pubmed&id={PMID}&cmd=neighbor_score&retmode=json
   ```

   These four API calls provide the same core functionality as PubMed MCP. The only gap is the MCP's convenience wrappers — the raw data is identical.

   Additionally, supplement with:
   - Semantic Scholar API for OA PDF detection
   - Unpaywall API for every DOI found

**Never silently degrade.** The user must know when they're getting a web-search-quality result instead of a PubMed-quality result.

---

### Step 0: Internal Project Discovery (runs first unless `--no-internal`)

Before searching external literature, scan internal channels for related past, current, or planned projects. Colleagues may have already written proposals, run experiments, or shared papers on closely related topics. This step prevents duplicating work and surfaces reusable assets — prior proposals, shared PDFs, FTO analyses, fermentation data, and expert contacts.

**Minimum effort: 6+ Slack queries + 3+ Confluence queries + 3+ GDrive search axes + 1 local directory scan.** If Slack/Confluence MCP is unavailable, use Glean as fallback. This is not a token search — internal knowledge is often the highest-value discovery.

---

#### 1. Slack — Exhaustive Multi-Query Search (PRIMARY via Claude.ai MCP)

Test Slack MCP availability first with a simple query. If it fails (token expired, not connected, running on Vertex/GCP):

1. **Tell the user:** "Slack MCP is unavailable ([error]). Internal Slack search will be skipped unless you have Glean MCP configured as a fallback."
2. **Check for Glean MCP** — look for tools matching `glean` or `mcp__glean`. If available, use Glean enterprise search (Section 4 below) which indexes Slack alongside other sources.
3. **If neither Slack MCP nor Glean is available:** Tell the user: "No internal search sources available. Consider setting up Glean MCP for unified enterprise search — add your Glean MCP URL to `~/.claude/.mcp.json`. Proceeding with GDrive filesystem search and external sources only."

**When Slack MCP is available**, use `slack_search_public_and_private` with **at least 6 query variations** covering different angles. Use the same term expansion logic as Step 1 — break the topic into concept axes and search each combination.

**Required query types (minimum 6):**

| Query type | Example for "alanine production in E. coli" | What it finds |
|-----------|---------------------------------------------|---------------|
| Direct product | `alanine production fermentation` | Direct project discussions |
| Organism + product class | `"E. coli" "amino acid" fermentation` | Related amino acid projects |
| Method/enzyme names | `"alanine dehydrogenase" OR alaD OR alaE` | Technical discussions, strain designs |
| Pathway/metabolic terms | `"metabolic engineering" alanine` | Broader meteng discussions mentioning alanine |
| IP/patent/FTO | `alanine patent FTO "freedom to operate"` | IP landscape work by legal team |
| Market/commercial | `alanine market demand application MGDA` | Business development, commercial context |

**Additional queries if initial results are thin:**
- Search for **related products** that share pathways: `pyruvate production`, `lactate fermentation`, `succinate "E. coli"` (same central metabolism)
- Search for **key people** identified in early results: `from:@stephen.mccolm alanine` or `from:@frank.wu alanine`
- Search for **project/program codes** found in initial results: `P345`, `LUVS`, `muscle-suit`

**For each query, use these search modifiers as needed:**
- `has:link` — messages with shared URLs (often papers, GDrive docs, or data links)
- `has:file` — messages with attached files (PDFs, data files, slides)
- `in:#tech-papers` — shared literature specifically
- `in:#ginkgo-competitive-intelligence` — competitor/landscape analysis
- `after:2024-01-01` — recent activity

**Slack file search** — search for shared PDFs and documents separately:
```
slack_search_public_and_private with content_types="files" and query="alanine production"
slack_search_public_and_private with content_types="files" and query="alanine" and type:pdf
```

**When a relevant thread is found:**
- **ALWAYS read it fully** with `slack_read_thread` — context and replies contain the most valuable information (links to papers, GDrive docs, raw data, feedback from reviewers, experimental results)
- Extract all URLs shared in the thread (GDrive links, paper DOIs, patent numbers, Confluence links)
- Note the people involved — they are potential collaborators or sources of expertise

---

#### 1b. Confluence — Structured Knowledge Search (via Claude.ai Atlassian MCP)

Confluence contains wiki pages, project documentation, protocols, SOPs, meeting notes, and technical reports that are often more structured and detailed than Slack messages. **Search Confluence alongside Slack** — they contain different types of knowledge.

**Use `searchConfluenceUsingCql`** with CQL queries. You need a `cloudId` — use the site URL (e.g., `ginkgobioworks.atlassian.net`) or find it via `getAccessibleAtlassianResources`.

**Run at least 3 CQL queries:**

```
CQL: text ~ "alanine production" AND type = page
CQL: text ~ "alanine" AND text ~ "fermentation" AND type = page
CQL: text ~ "beta-alanine" OR text ~ "amino acid production" AND type = page
```

**CQL query patterns for different search needs:**
- Topic search: `text ~ "alanine" AND type = page`
- Title search: `title ~ "alanine"` (narrower — finds pages with topic in the title)
- Recent content: `text ~ "alanine" AND lastmodified > "2024-01-01"`
- Specific space: `text ~ "alanine" AND space = "SCIENCE"` or `space = "PROPOSALS"`
- By author: `text ~ "alanine" AND creator = "user@company.com"`

**What to look for in Confluence:**
- **Project pages** — technical approaches, experimental plans, strain designs
- **Protocols / SOPs** — existing procedures for related work
- **Meeting notes** — design reviews, project updates with decisions and data
- **Proposals** — prior grant/commercial proposals with reusable lit reviews and comparison tables
- **Technical reports** — completed work with results and conclusions
- **IP/FTO pages** — patent landscape analyses, freedom-to-operate assessments

**When a relevant page is found:**
- Read it with `getConfluencePage` using `contentFormat: "markdown"` for easy parsing
- Check child pages with `getConfluencePageDescendants` — project pages often have sub-pages with detailed data
- Note the page authors — they are subject matter experts on this topic

**If Confluence MCP is unavailable** (same Claude.ai managed MCP limitation as Slack): fall back to Glean (Section 4), which also indexes Confluence content.

---

#### 2. Google Drive — Multi-Axis Content Search

Google Drive for Desktop syncs files to `~/Library/CloudStorage/GoogleDrive-*/`. Search systematically across **multiple term variations and file types**.

**Filename search (fast — covers all synced files):**
```bash
# Search with multiple term variations — don't stop at the first
find ~/Library/CloudStorage/GoogleDrive-*/ -iname "*alanine*" -type f 2>/dev/null
find ~/Library/CloudStorage/GoogleDrive-*/ -iname "*amino*acid*" -type f 2>/dev/null
find ~/Library/CloudStorage/GoogleDrive-*/ -iname "*alaD*" -o -iname "*alaE*" 2>/dev/null

# Search for project codes found in Slack
find ~/Library/CloudStorage/GoogleDrive-*/ -ipath "*P345*" -type f 2>/dev/null
find ~/Library/CloudStorage/GoogleDrive-*/ -ipath "*LUVS*" -type f 2>/dev/null

# Search for common document types with related terms
find ~/Library/CloudStorage/GoogleDrive-*/ \( -iname "*proposal*" -o -iname "*report*" -o -iname "*review*" \) -type f 2>/dev/null | xargs grep -li "alanine" 2>/dev/null
```

**Content search (slower — searches inside files for keyword matches):**
```bash
# Search inside synced .docx, .pptx, .pdf, .txt, .md files for topic terms
# This catches documents where the topic is in the content but not the filename
grep -rli "alanine" ~/Library/CloudStorage/GoogleDrive-*/ --include="*.txt" --include="*.md" --include="*.csv" 2>/dev/null
```

For `.docx`/`.pptx`/`.pdf` — these are binary formats, so filename + path search is the primary method. If specific GDrive folders look relevant (e.g., a `Proposals/` or `Literature/` folder), list their contents and read promising files.

**Google Drive native files (.gdoc, .gsheet, .gslides):**
- These are JSON pointer files — they don't contain document content locally
- Read the pointer to get the `doc_id` and title
- Note the title and path for the user — they can export/review these later
- If a title looks highly relevant, offer to open it: `open "https://docs.google.com/document/d/{doc_id}/edit"`

**GDrive links from Slack threads:**
- When Slack threads contain `drive.google.com` URLs, note these — they often point to shared proposals, data sheets, or literature folders that aren't in the user's local sync
- These require browser access to download, but knowing they exist is valuable

---

#### 3. Local Project Directories

Check the current working directory and nearby project directories for existing work:

```bash
# Current project's literature folder
find . -type d -name "literature" -o -name "references" -o -name "papers" 2>/dev/null

# Related project directories (check parent directory for sibling projects)
ls -d ../*/literature/ 2>/dev/null
ls -d ../*alanine*/ ../*amino*/ 2>/dev/null

# Any existing BibTeX or reference files
find . -name "*.bib" -o -name "library.md" -o -name "reading_list.md" 2>/dev/null
```

If existing literature folders or reference libraries are found, read them — don't rebuild from scratch.

---

#### 4. Glean Enterprise Search (FALLBACK — when Slack MCP is unavailable)

If Slack MCP failed in Section 1, check if Glean MCP is connected. Glean indexes Slack, Google Drive, Confluence, Jira, Gmail, and other sources in a single unified search — it can replace individual Slack queries.

**Check if Glean MCP is available** by looking for tools matching `glean` or `mcp__glean`. The tool names may vary by configuration but typically include `search`, `chat`, and `read_document`.

**If Glean is available, run at least 3 queries with different term angles:**

```
Glean search: "alanine production E. coli fermentation"
Glean search: "alanine metabolic engineering patent FTO"
Glean search: "beta-alanine market nylon MGDA proposal"
```

Glean returns results across ALL connected sources ranked by relevance with user-level permission filtering. For each result:
- Note the **source type** (Slack thread, GDrive doc, Confluence page, etc.)
- For Slack threads: note permalink — user can open and read the full thread
- For documents: use `read_document` to access content directly through Glean if available
- For GDrive links: note for later retrieval

**If Glean is NOT available and Slack MCP also failed:**
Tell the user: "No internal search sources available. To enable internal discovery, either:
1. Re-authorize Slack at [claude.ai/settings/connectors](https://claude.ai/settings/connectors) (requires Anthropic account), or
2. Set up Glean MCP by adding your Glean server URL to `~/.claude/.mcp.json`:
```json
{
  \"mcpServers\": {
    \"glean-mcp\": {
      \"url\": \"https://YOUR-ORG.glean.com/mcp/default\"
    }
  }
}
```
Then restart Claude Code."

Proceed with GDrive filesystem search (Section 2) and external sources only.

---

#### Output: Internal Discovery Summary

```markdown
## Internal Project Discovery: [Topic]

### Related Projects Found

| Source | Project/Document | Relevance | Key Assets |
|--------|-----------------|-----------|------------|
| Slack #channel | [Thread/message description] | High/Medium/Low | [PDFs, links, data, contacts] |
| GDrive path | [Document title and path] | High/Medium/Low | [Reusable content] |
| Local directory | [Folder/file] | High/Medium/Low | [Existing work] |

### Shared Documents to Retrieve
- [GDrive links from Slack threads that need browser access to download]
- [PDF attachments shared in Slack channels]

### Reusable Assets
- **Prior proposals:** [list with paths/links — reusable lit reviews, comparison tables, prelim data]
- **Existing strain/experimental data:** [results shared in Slack or stored in Drive]
- **Previously shared papers:** [PDFs from Slack not yet in library]
- **FTO/IP analyses:** [patent searches, freedom-to-operate assessments]
- **Market data:** [commercial context, market size, pricing]
- **Contacts:** [people who posted about related work — collaborators, subject matter experts]

### Recommendation
[Brief assessment: how much of the literature search is already done, what can be reused vs. what needs fresh searching]
```

If no internal results are found after the minimum 6 Slack + 3 GDrive searches, note that and proceed to external search.

---

### Step 1: Query Design — MANDATORY Term Expansion

**DO NOT skip this step. DO NOT fire off 2-3 generic web searches and call it done.**

Before running ANY search, decompose the topic into an explicit term expansion table. Write this table out — it is the search plan.

| Concept | Primary term | Synonyms / alternatives | MeSH terms (if PubMed) |
|---------|-------------|------------------------|----------------------|
| Product | [e.g., "L-alanine"] | [e.g., "alanine", "Ala", "alpha-alanine"] | [e.g., Alanine [MeSH]] |
| Method | [e.g., "metabolic engineering"] | [e.g., "strain engineering", "pathway engineering", "synthetic biology"] | [Metabolic Engineering [MeSH]] |
| Organism | [e.g., "Escherichia coli"] | [e.g., "E. coli", "coliform"] | [Escherichia coli [MeSH]] |
| Sub-topics | [e.g., "exporter", "dehydrogenase"] | [e.g., "AlaE", "ygaW", "alaD", "AlaDH"] | — |

**Minimum requirements:**
- At least **3 concept axes** with **2+ synonyms each**
- At least **8 distinct search queries** combining different axes and synonyms
- Queries must include: (1) broad topic, (2) specific gene/enzyme names, (3) specific organism, (4) review-specific, (5) recent years filter, (6) key author/lab names, (7) related products/pathways, (8) patent/IP terms
- If PubMed MCP is unavailable, compensate with **more web search queries, not fewer** — use `site:pubmed.ncbi.nlm.nih.gov` queries to maintain structured results

**Example — topic: "alanine production in E. coli":**
1. `"Escherichia coli" alanine production metabolic engineering` (broad)
2. `"E. coli" "L-alanine" fermentation titer yield` (quantitative focus)
3. `"E. coli" "beta-alanine" biosynthesis panD aspartate decarboxylase` (β-alanine specific)
4. `"alanine dehydrogenase" alaD overexpression "E. coli"` (enzyme-specific)
5. `"alanine" "E. coli" exporter transporter alaE ygaW` (transport — often missed)
6. `"L-alanine" production review microorganism 2022 2023` (reviews)
7. `"alanine" fermentation "E. coli" site:pubmed.ncbi.nlm.nih.gov 2024 2025` (recent)
8. `patent "L-alanine" "E. coli" fermentation production` (IP landscape)

**The difference between a 7-paper search and a 33-paper search is query diversity, not luck.**

### Step 2: Multi-Source Search

**Run ALL of the following for every search. Do not stop after the first source returns results.**

1. **PubMed** (default) — use PubMed MCP tools for peer-reviewed biomedical/life science literature. If PubMed MCP is unavailable, use `site:pubmed.ncbi.nlm.nih.gov` web searches as fallback — run at least 5 separate queries with different term combinations.
2. **Web search** — for preprints (bioRxiv, chemRxiv), conference proceedings, theses, and grey literature
3. **Patent search** — when `--patents` flag or when query involves commercial methods, compositions, or processes
4. **Citation chasing** — when a review is found, extract its reference list and identify the 5-10 most-cited primary sources. Search for those specifically.
5. **Author tracking** — identify the 2-3 most prolific labs/groups from initial results. Search for their other recent publications.

**Minimum result count:** A well-executed search on an active biotech topic should identify **20-40 papers**. If you have fewer than 15, your queries are too narrow — go back to Step 1 and add more term variations.

### Step 3: Filter and Rank

Apply filters:
- `--recent` → last 2 years only
- `--reviews` → filter to review articles
- `--clinical` → filter to clinical trials or clinical data
- `--limit N` → return top N results (default: 10)
- `--no-patents` → skip patent search (default: patents are always included)
- `--no-internal` → skip internal project discovery via Slack/GDrive

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

## Download Persistence

When papers or patents are found during search, a `download_log.md` is maintained in the `literature/` folder tracking every download attempt — source tried, success/failure, and filename. This log:
- Prevents re-attempting sources that already failed for a specific paper
- Survives across sessions — future searches check the log before re-downloading
- Provides transparency on what was tried and what remains paywalled

## When Automated Downloads Fail

If all automated download tiers are exhausted for a paper, the **browser-assisted fallback** activates:
1. Known PDF URLs are opened in the user's default browser (works cross-platform: macOS, Linux, Windows)
2. The user's browser session leverages institutional access, VPN, or saved credentials
3. Multiple tabs are opened at once for batch failures
4. After the user confirms downloads are complete, files are automatically picked up from the Downloads folder, renamed per naming convention, and sorted into the library

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
