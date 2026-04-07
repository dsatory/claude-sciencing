# NCBI E-utilities API — Direct PubMed Access Without MCP

This reference provides direct HTTP API access to PubMed via NCBI E-utilities. Use these when PubMed MCP is unavailable (e.g., when running Claude Code via Vertex/GCP instead of Anthropic account, or when the MCP token is expired).

All endpoints are free, public, and accessible via `WebFetch` or `curl`. No authentication required for basic use (3 requests/sec). With an API key (free, register at https://www.ncbi.nlm.nih.gov/account/settings/ → API Key), the limit increases to 10 requests/sec.

If the user has an API key, append `&api_key={KEY}` to every request.

---

## Base URL

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
```

---

## 1. Search PubMed (esearch)

Find PMIDs matching a query.

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={QUERY}&retmax={N}&retmode=json&sort=relevance
```

**Parameters:**
- `db=pubmed` — search PubMed
- `term` — URL-encoded search query. Supports Boolean (AND, OR, NOT), field tags ([Title], [Author], [Journal], [MeSH Terms]), date ranges
- `retmax` — max results (default 20, max 10000)
- `retmode=json` — return JSON (easier to parse than XML)
- `sort` — `relevance` (default), `pub_date`, `author`, `journal`
- `mindate` / `maxdate` — date filter (YYYY/MM/DD format)
- `datetype=pdat` — filter by publication date

**Example — search for E. coli alanine production, last 5 years:**
```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=(%22Escherichia+coli%22)+AND+(alanine)+AND+(production+OR+fermentation+OR+%22metabolic+engineering%22)&retmax=50&retmode=json&sort=relevance&mindate=2021&datetype=pdat
```

**Response (JSON):**
```json
{
  "esearchresult": {
    "count": "49",
    "retmax": "50",
    "idlist": ["40724976", "38867465", "37537629", ...],
    "querytranslation": "..."
  }
}
```

The `idlist` contains PMIDs. Feed these to efetch for metadata.

---

## 2. Fetch Article Metadata (efetch)

Get title, authors, journal, DOI, abstract for one or more PMIDs.

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={PMID1,PMID2,...}&retmode=xml&rettype=abstract
```

**Parameters:**
- `id` — comma-separated PMIDs (up to 200 per request)
- `retmode=xml` — XML is the only format with full metadata (JSON not supported for efetch)
- `rettype=abstract` — includes abstract text

**Example — get metadata for PMID 17874321:**
```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=17874321&retmode=xml&rettype=abstract
```

**Key XML elements to extract:**
```xml
<ArticleTitle>Production of L-alanine by...</ArticleTitle>
<Abstract><AbstractText>...</AbstractText></Abstract>
<AuthorList>
  <Author><LastName>Zhang</LastName><ForeName>Xueli</ForeName></Author>
  ...
</AuthorList>
<Journal>
  <Title>Applied microbiology and biotechnology</Title>
  <ISOAbbreviation>Appl Microbiol Biotechnol</ISOAbbreviation>
  <JournalIssue><Volume>77</Volume><Issue>2</Issue>
    <PubDate><Year>2007</Year></PubDate>
  </JournalIssue>
</Journal>
<ArticleIdList>
  <ArticleId IdType="doi">10.1007/s00253-007-1170-y</ArticleId>
  <ArticleId IdType="pubmed">17874321</ArticleId>
  <ArticleId IdType="pmc">PMC2168043</ArticleId>  <!-- if available -->
</ArticleIdList>
```

**When using WebFetch**, use this prompt to extract structured data:
```
Extract from this PubMed XML: title, all author names, journal name, year, volume, issue, pages, DOI, PMID, PMCID (if present), and full abstract text. Return as structured text.
```

---

## 3. Convert IDs (PMC ID Converter)

Convert between DOI, PMID, and PMCID. **This is critical for finding free PMC PDFs.**

```
https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids={ID}&format=json
```

**Parameters:**
- `ids` — one or more identifiers (PMID, PMCID, or DOI), comma-separated
- `format=json` — return JSON

**Example — convert DOI to PMID/PMCID:**
```
https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids=10.1128/AEM.00003-11&format=json
```

**Response:**
```json
{
  "records": [{
    "pmid": "21531828",
    "pmcid": "PMC3131665",
    "doi": "10.1128/AEM.00003-11"
  }]
}
```

If `pmcid` is present → the paper is in PMC → free PDF likely available at:
```
https://pmc.ncbi.nlm.nih.gov/articles/{PMCID}/pdf/
```

**Batch conversion** — up to 200 IDs per request:
```
https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids=17874321,21531828,34681116&format=json
```

---

## 4. Find Related Articles (elink)

Find papers related to a given PMID (PubMed's "similar articles" algorithm).

```
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pubmed&id={PMID}&cmd=neighbor_score&retmode=json
```

**Parameters:**
- `dbfrom=pubmed&db=pubmed` — find related PubMed articles
- `id` — seed PMID
- `cmd=neighbor_score` — return related articles ranked by relevance score

**Response contains** a list of related PMIDs with scores. Feed the top 10-20 to efetch for metadata.

---

## 5. Check OA / Full Text Availability

**Method 1: Check for PMCID via ID converter (above)**
If a paper has a PMCID, it's in PMC and likely has a free PDF.

**Method 2: Check OA status via efetch**
In the efetch XML, look for:
```xml
<ArticleId IdType="pmc">PMC...</ArticleId>
```
If present → free full text available.

**Method 3: Unpaywall API (complements NCBI)**
```
https://api.unpaywall.org/v2/{DOI}?email=user@example.com
```
Returns `is_oa: true/false` and `oa_locations` with direct PDF URLs.

---

## 6. Full Text from PMC (efetch on PMC database) — THE PRIMARY PAPER ACCESS METHOD

**This is the most reliable way to get full paper content without a browser.** PMC blocks PDF downloads via curl, but efetch returns full text as structured XML for OA papers.

```
WebFetch: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={PMCID_NUMBER}&retmode=xml
Prompt: "Extract the full article text from this PMC XML. Return: title, all authors, abstract, and all section headings with their content. Include any tables and figure captions."
```

Note: use the numeric part only (e.g., `3131665` not `PMC3131665`).

**What you get depends on the journal's OA policy:**

| Journal type | efetch returns | Example |
|-------------|---------------|---------|
| Fully OA (MDPI, Frontiers, PLOS, BMC) | **Full text** — body, sections, figures, tables (60-100KB XML) | PMC8533518: 80KB, 17 sections, 4 figures |
| Publisher OA (Nature Comms, Cell Reports) | Usually full text | Varies |
| Embargo deposit (ASM, Springer, Elsevier) | **Abstract only** — no body text (~8KB XML) | PMC3131665: 8KB, abstract only |

**How to tell if you got full text:** Check if the response contains `<body>` tags. If yes → full paper. If no → abstract only, need PDF via browser.

**This is better than PDF for analysis purposes** — the XML is structured, with tagged sections, figure captions, table data, and references. You can parse it directly instead of trying to extract text from a PDF.

**Workflow for batch paper retrieval:**
1. Run idconv on all PMIDs → find which have PMCIDs
2. For papers with PMCIDs: call efetch on PMC database → check for `<body>` content
3. Papers with full body text: done — read and analyze directly from XML
4. Papers with abstract only: fall through to Unpaywall, Semantic Scholar, MDPI direct, or browser fallback for PDF

---

## Workflow: Replacing PubMed MCP with E-utilities

When PubMed MCP is unavailable, execute this workflow using WebFetch:

### For searching:
1. Build query using the term expansion table from sci-search Step 1
2. Call esearch with the query → get PMIDs
3. Call efetch with the PMIDs → get metadata (title, authors, journal, DOI, abstract)
4. Present results in the same format as PubMed MCP would

### For metadata lookup (given a DOI or PMID):
1. Call ID converter to get all IDs (PMID ↔ DOI ↔ PMCID)
2. Call efetch for full metadata
3. Check if PMCID exists → flag as OA

### For downloading:
1. Run ID converter for all papers → find which have PMCIDs
2. Papers with PMCIDs → try PMC PDF download
3. Papers without PMCIDs → fall through to Unpaywall, Semantic Scholar, etc.

### For related articles:
1. Call elink with a seed PMID → get related PMIDs
2. Call efetch on the top results → get metadata

---

## Rate Limiting

- **Without API key:** 3 requests/second. For a batch of 50 papers, this means ~17 seconds for metadata.
- **With API key:** 10 requests/second. Register free at https://www.ncbi.nlm.nih.gov/account/settings/
- **Batch requests:** efetch and idconv accept comma-separated IDs (up to 200), so batch to minimize requests.
- **Be polite:** NCBI will block IPs that exceed rate limits. Space requests by at least 334ms without a key.
