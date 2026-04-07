# Multi-Database Search APIs

This reference documents the APIs for searching across multiple scientific databases. Use these alongside PubMed (via MCP or E-utilities) to get comprehensive literature coverage.

---

## 1. OpenAlex (FREE, no auth, no rate limit concerns)

The most comprehensive open scholarly metadata source. 250M+ works, all open.

**Search:**
```
WebFetch: https://api.openalex.org/works?search={QUERY}&per_page=25&select=id,doi,title,publication_year,cited_by_count,open_access,authorships,primary_location&sort=relevance_score:desc
```

**Filter by year:**
```
&filter=publication_year:2022-2026
```

**Filter by OA only:**
```
&filter=open_access.is_oa:true
```

**Filter by type (journal article, review, etc.):**
```
&filter=type:journal-article
```

**Response fields:**
- `title` — paper title
- `doi` — DOI URL
- `publication_year` — year
- `cited_by_count` — citation count (useful for relevance scoring)
- `open_access.is_oa` — boolean
- `open_access.oa_url` — direct link to free version
- `authorships[].author.display_name` — author names
- `primary_location.source.display_name` — journal name

**Get by DOI:**
```
WebFetch: https://api.openalex.org/works/doi:{DOI}
```

**Advantages over PubMed:** Covers ALL disciplines (not just biomedical), includes citation counts, OA URLs, and institutional affiliations. No rate limits for polite use.

---

## 2. Semantic Scholar (FREE, no auth for low volume)

AI-powered academic search with embedding-based relevance.

**Search:**
```
WebFetch: https://api.semanticscholar.org/graph/v1/paper/search?query={QUERY}&fields=title,year,authors,citationCount,openAccessPdf,externalIds,abstract&limit=25
```

**Get by ID (DOI, PMID, or S2 ID):**
```
WebFetch: https://api.semanticscholar.org/graph/v1/paper/DOI:{DOI}?fields=title,year,authors,citationCount,openAccessPdf,externalIds,abstract
WebFetch: https://api.semanticscholar.org/graph/v1/paper/PMID:{PMID}?fields=title,year,authors,citationCount,openAccessPdf,externalIds,abstract
```

**Response fields:**
- `title`, `year`, `abstract`
- `authors[].name` — author names
- `citationCount` — number of citations
- `openAccessPdf.url` — direct OA PDF URL (very useful for downloads)
- `externalIds.DOI`, `.PubMed`, `.ArXiv` — cross-reference IDs

**Rate limits:** 1 request/second without API key. 10/sec with free key from semanticscholar.org.

**Advantages over PubMed:** Embedding-based search finds semantically related papers even with different terminology. OA PDF URLs are pre-resolved. Covers CS/AI/ML papers better than PubMed.

---

## 3. CrossRef (FREE, no auth required)

Metadata for 150M+ DOIs. Best for resolving DOIs to full metadata.

**Search:**
```
WebFetch: https://api.crossref.org/works?query={QUERY}&rows=25&sort=relevance&order=desc
```

**Get by DOI:**
```
WebFetch: https://api.crossref.org/works/{DOI}
```

**Response fields:**
- `title`, `DOI`
- `author[].given`, `author[].family` — author names
- `container-title` — journal name
- `published-print.date-parts` or `published-online.date-parts` — publication date
- `is-referenced-by-count` — citation count
- `link[].URL` — full-text links (may include OA versions)

**Advantages:** Most reliable DOI → metadata resolution. Good for batch DOI lookups.

---

## 4. bioRxiv/medRxiv API (FREE, no auth)

Direct API access to preprints (in addition to the bioRxiv MCP server).

**Search recent preprints:**
```
WebFetch: https://api.biorxiv.org/details/biorxiv/2024-01-01/2026-04-07/0/25
```

**Search by DOI:**
```
WebFetch: https://api.biorxiv.org/details/biorxiv/{DOI_SUFFIX}
```

**Response fields:**
- `title`, `authors`, `date`, `doi`, `abstract`
- `category` — subject area
- `published` — DOI of final published version (if published)
- `jatsxml` — link to full XML

---

## 5. Unpaywall (FREE, email required)

Finds open-access versions of paywalled papers.

```
WebFetch: https://api.unpaywall.org/v2/{DOI}?email=user@example.com
```

**Response fields:**
- `is_oa` — boolean
- `best_oa_location.url_for_pdf` — direct PDF URL
- `oa_locations[]` — all known OA copies (check all, not just best)

---

## Multi-Database Search Workflow

For comprehensive literature coverage, query databases in this order:

### Step 1: PubMed (biomedical primary source)
- Via MCP or E-utilities esearch → efetch
- Returns PMIDs, abstracts, MeSH terms

### Step 2: OpenAlex (broadest coverage + citation counts)
- `api.openalex.org/works?search={query}&per_page=50`
- Returns DOIs, citation counts, OA URLs, author affiliations
- Covers journals PubMed doesn't index

### Step 3: Semantic Scholar (semantic matching + OA PDFs)
- `api.semanticscholar.org/graph/v1/paper/search?query={query}`
- Finds semantically related papers even with different terminology
- Pre-resolved OA PDF URLs

### Step 4: bioRxiv (preprints)
- Via MCP or direct API
- Catches papers not yet peer-reviewed/indexed

### Deduplication
After collecting results from all sources, deduplicate by:
1. **DOI match** (exact) — most reliable
2. **Title similarity** (Jaccard similarity > 0.8 on word sets) — catches DOI variations
3. **PMID match** — cross-reference via idconv

Keep the richest metadata record (prefer OpenAlex for citation counts, PubMed for MeSH terms, Semantic Scholar for OA PDF URLs).

---

## Relevance Scoring (0-10)

Score each paper on a 0-10 scale using this formula:

| Component | Weight | Scoring |
|-----------|--------|---------|
| **Keyword relevance** | 40% | Full title match = 4, partial = 2, abstract only = 1 |
| **Recency** | 25% | Current year = 2.5, -1yr = 2.0, -2yr = 1.5, -3yr = 1.0, older = 0.5 |
| **Citation impact** | 20% | Top 10% in results = 2.0, top 25% = 1.5, top 50% = 1.0, bottom 50% = 0.5 |
| **Open access** | 15% | OA with PDF = 1.5, OA abstract only = 1.0, paywalled = 0.5 |

**Score interpretation:**
- **8-10:** Must-read — directly relevant, recent, well-cited, accessible
- **5-7:** Important — relevant but older, less cited, or paywalled
- **3-4:** Background — tangentially relevant or very old
- **0-2:** Skip unless completeness needed

Present results sorted by relevance score with the score visible:

```
### [1] Score: 9.2 — "Dynamic overflow metabolism for L-alanine in E. coli" (2025)
Li et al. | Bioresour Technol | DOI: 10.1016/j.biortech.2025.132446
OA: No | Citations: 3 | **195.2 g/L, 88.6% yield — current record**
```
