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

## Troubleshooting

### "Tool not found" errors
- PubMed MCP is a Claude.ai managed integration, not a local MCP server
- It syncs automatically from Claude.ai to Claude Code when you log in
- If tools aren't appearing, try: `/mcp` in Claude Code to list connected servers

### "Permission denied" or "unauthorized" errors
- Re-authorize the PubMed connector in Claude.ai settings
- Ensure your Claude.ai account has the integration enabled (not just the organization)

### "Rate limited" or "too many requests"
- PubMed/NCBI has rate limits: ~3 requests/second without an API key, ~10/second with one
- For large batch operations, the paper-retrieval skill automatically paces requests
- If persistent, wait 60 seconds and retry

### Tools appear but return empty results
- Try a known working query (e.g., "CRISPR Cas9")
- Check if the search terms use correct PubMed syntax
- Some very recent papers may not be indexed yet (PubMed indexing can lag 1-2 days)
