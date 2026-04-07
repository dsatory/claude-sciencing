---
name: pubmed-setup
description: >
  Checks PubMed MCP integration status and guides users through setup. Use when the user says
  "set up PubMed," "configure PubMed," "PubMed not working," "can't search PubMed," "enable
  PubMed," or when any sci- command fails because PubMed tools are unavailable. Also triggers
  on "setup," "configure," or "check dependencies" in the context of the claude-sciencing plugin.
allowed-tools: Bash, Read, Write, Edit, WebFetch, mcp__claude_ai_PubMed__search_articles, mcp__claude_ai_PubMed__get_article_metadata, mcp__claude_ai_PubMed__get_full_text_article, mcp__claude_ai_PubMed__find_related_articles, mcp__claude_ai_PubMed__lookup_article_by_citation, mcp__claude_ai_PubMed__convert_article_ids, mcp__claude_ai_PubMed__get_copyright_status
---

# PubMed MCP Setup & Diagnostics

This skill checks whether PubMed MCP tools are available and guides the user through enabling them if not. PubMed MCP is a core dependency for the claude-sciencing plugin — it powers literature search, article metadata retrieval, full-text access, and citation management.

---

## Step 1: Check Current Status

Run a diagnostic to determine if PubMed MCP is available and functional.

**Test the connection** by attempting a simple search:

```
Use mcp__claude_ai_PubMed__search_articles with a simple test query like "CRISPR" with max_results: 1
```

### If the tool call succeeds:
Report to the user:

```
PubMed MCP is connected and working.

Available tools:
  - search_articles: Search PubMed for papers by keyword, MeSH term, or Boolean query
  - get_article_metadata: Get full metadata (title, authors, journal, DOI, abstract) for a PMID
  - get_full_text_article: Retrieve full text for open-access articles in PMC
  - find_related_articles: Find papers related to a given PMID
  - lookup_article_by_citation: Find a paper from partial citation info (author, title, journal)
  - convert_article_ids: Convert between PMID, DOI, and PMCID
  - get_copyright_status: Check open-access and copyright status of an article

All claude-sciencing commands (/sci-search, /sci-library, /sci-read) are ready to use.
```

### If the tool call fails or the tool is not found:
Guide the user through setup:

```
PubMed MCP is not currently available. This is required for literature search
and article retrieval in the claude-sciencing plugin.

To enable PubMed MCP:

1. Go to Claude.ai settings:
   - Open https://claude.ai/settings/connectors
   - (Or: Claude.ai → Settings → Connectors / Integrations)

2. Find "PubMed" in the available integrations and enable it

3. Grant the requested permissions (read-only access to PubMed/NCBI)

4. Restart Claude Code or start a new conversation to sync the integration

5. Run this check again to verify: /pubmed-setup
```

---

## Step 2: Verify Tool Capabilities

If PubMed MCP is connected, run a quick functional check across key capabilities:

### Search test
```
Search for: "lignin depolymerization" with max_results: 1
Expected: Returns at least one result with PMID, title, authors
```

### Metadata test
```
Get metadata for a known PMID (e.g., PMID 38000000 or a recent well-known paper)
Expected: Returns title, authors, journal, DOI, abstract
```

### ID conversion test
```
Convert a known DOI to PMID/PMCID
Expected: Returns corresponding IDs
```

### Report results:
```
PubMed MCP Diagnostic Results:
  Search:        ✅ Working
  Metadata:      ✅ Working
  ID Conversion: ✅ Working
  Full Text:     ✅ Working (for OA articles)

All systems operational.
```

If any test fails, report which specific capability is broken and suggest:
- Checking Claude.ai connector settings for permission issues
- Disconnecting and reconnecting the PubMed integration
- Starting a new Claude Code session

---

## Step 3: Integration with claude-sciencing Commands

Explain how PubMed MCP powers the plugin:

| Command | PubMed Tools Used |
|---------|-------------------|
| `/sci-search` | `search_articles`, `get_article_metadata`, `find_related_articles` |
| `/sci-library add` | `get_article_metadata`, `convert_article_ids`, `lookup_article_by_citation` |
| `/sci-read` | `get_full_text_article`, `get_copyright_status` |
| `paper-retrieval` skill | `convert_article_ids`, `get_full_text_article`, `get_copyright_status` |

---

## PubMed MCP Tool Names

The canonical list of PubMed MCP tool names used across this plugin is maintained in `CLAUDE.md` at the project root. If tool names change due to a Claude.ai integration update, update them in CLAUDE.md first, then propagate to the `allowed-tools` field in each command and skill file listed there.

---

## Two Access Methods

### Method 1: PubMed MCP (Claude.ai managed integration)

The preferred method when available. Provides convenience wrappers around NCBI APIs with automatic authentication.

**Requirements:** Claude Code running via Anthropic account (not Vertex/GCP). PubMed connector enabled at claude.ai/settings/connectors.

**Limitation:** Does NOT work when Claude Code runs via Vertex, AWS Bedrock, or any non-Anthropic provider. The MCP integration syncs from your Claude.ai account session, which doesn't exist on third-party providers.

### Method 2: NCBI E-utilities API (direct HTTP — always works)

Direct HTTP calls to NCBI's public API. Works on **any provider** (Vertex, Bedrock, Anthropic, or local). No authentication required for basic use. Same underlying database as PubMed MCP.

See `references/eutils-api.md` for complete API documentation with examples.

**Quick test — verify E-utilities access:**
```
WebFetch: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=CRISPR&retmax=1&retmode=json
```
If this returns a JSON response with an `idlist`, E-utilities is working.

**When to use which:**
- PubMed MCP available → use MCP (more convenient, same data)
- PubMed MCP unavailable → use E-utilities directly (same data, slightly more verbose calls)
- Both access the same NCBI/PubMed database. The results are identical.

---

## Troubleshooting

### PubMed MCP: "Tool not found" or "requires re-authorization"
- **If using Vertex/GCP:** PubMed MCP will never work on Vertex. Use E-utilities API instead (Method 2). This is not a bug — managed MCP integrations require an Anthropic account session.
- **If using Anthropic account:** Re-authorize at claude.ai/settings/connectors. Disconnect and reconnect PubMed.
- If tools aren't appearing, try: `/mcp` in Claude Code to list connected servers

### "Permission denied" or "unauthorized" errors
- Re-authorize the PubMed connector in Claude.ai settings
- Ensure your Claude.ai account has the integration enabled (not just the organization)

### "Rate limited" or "too many requests" (applies to both methods)
- NCBI rate limits: ~3 requests/second without an API key, ~10/second with one
- Register for a free API key at https://www.ncbi.nlm.nih.gov/account/settings/
- For large batch operations, the paper-retrieval skill automatically paces requests
- If persistent, wait 60 seconds and retry

### Tools appear but return empty results
- Try a known working query (e.g., "CRISPR Cas9")
- Check if the search terms use correct PubMed syntax
- Some very recent papers may not be indexed yet (PubMed indexing can lag 1-2 days)
