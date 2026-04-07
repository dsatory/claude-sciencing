---
name: paper-retrieval
description: >
  Downloads and organizes open-access scientific PDFs from PubMed Central, Unpaywall, publisher
  OA repositories, and preprint servers. Use this skill when the user wants to "download papers,"
  "get PDFs," "fetch articles," "build a PDF library," "download open access," "grab the papers
  from that search," or any request involving acquiring and filing scientific literature as PDFs.
  Also triggers when the user says "download what you can," "get the full texts," or refers to
  building/populating a literature folder. Works best after /sci-search has identified papers.
  Pairs with /sci-library for metadata tracking.
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch, mcp__claude_ai_PubMed__search_articles, mcp__claude_ai_PubMed__get_article_metadata, mcp__claude_ai_PubMed__get_full_text_article, mcp__claude_ai_PubMed__find_related_articles, mcp__claude_ai_PubMed__lookup_article_by_citation, mcp__claude_ai_PubMed__convert_article_ids, mcp__claude_ai_PubMed__get_copyright_status
---

# Paper Retrieval & PDF Library Builder

You are an expert at acquiring open-access scientific PDFs and organizing them into a well-structured local library. You know which sources work, which don't, and how to avoid wasting time on dead ends.

## Core Philosophy

Downloading scientific PDFs programmatically is unreliable — many approaches look promising but fail silently (redirects to login pages, CAPTCHAs, HTML instead of PDF, incomplete downloads). This skill codifies the approaches that actually work and avoids time sinks.

---

## PDF Naming Convention

All downloaded PDFs follow this strict naming format:

```
{JournalAbbrev}_{max_3_word_description}_{year}.pdf
```

### Rules:
- **JournalAbbrev**: Standard abbreviated journal name, PascalCase, no spaces or dots
  - Nature Communications → `NatComm`
  - ACS Catalysis → `ACSCatal`
  - Metabolic Engineering → `MetabEng`
  - Biotechnology for Biofuels → `BiotechBiofuels`
  - Science Advances → `SciAdv`
  - PNAS → `PNAS`
  - Bioresources and Bioprocessing → `BioresBioprocess`
  - Green Chemistry (RSC) → `RSC` or `GreenChem`
  - Microbial Cell Factories → `MicrobCellFact`
  - ACS Energy & Fuels → `ACSEnergyFuels`
  - ACS Sustainable Chemistry & Engineering → `ACSE`
  - Journal of Agricultural and Food Chemistry → `JAFC`
  - Journal of Nanobiotechnology → `JNanobiotech`
  - JACS Au → `JACSAu`
  - Applied and Environmental Microbiology → `AEM`
  - Communications Biology → `CommBiol`
  - Scientific Reports → `SciRep`
  - The Innovation → `Innovation`
  - Research (Science Partner Journals) → `Research`
  - Polymers → `Polymers`
  - Catalysts → `Catalysts`
  - Biomolecules → `Biomolecules`
  - Fuels → `Fuels`
  - Discover Sustainability → `DiscoverSustain`
  - bioRxiv → `bioRxiv`
  - chemRxiv → `chemRxiv`
  - For journals not listed, create a sensible PascalCase abbreviation
- **max_3_word_description**: 3 words max, underscored, capturing the core content
  - Use key organism, substrate, product, method, or finding
  - Abbreviate organism names: `E_coli`, `S_cerevisiae`, `C_glutamicum`, `B_subtilis`
  - Examples: `CRISPR_Cas9_knockout`, `succinate_production_review`, `lipase_thermostability`
- **year**: 4-digit publication year

### Examples:
```
NatComm_Ecoli_succinate_titer_2025.pdf
ACSCatal_enzyme_CO2_fixation_2025.pdf
BiotechBiofuels_biofuel_production_review_2022.pdf
AEM_Scerevisiae_ethanol_tolerance_2021.pdf
MicrobCellFact_Cglutamicum_lysine_engineering_2023.pdf
PNAS_directed_evolution_lipase_2023.pdf
SciAdv_cellulose_hydrolysis_enzyme_2023.pdf
```

---

## Folder Organization

PDFs are sorted into numbered category folders:

```
literature/PDFs/
├── 01_Reviews/
├── 02_Category_Name/
├── 03_Category_Name/
└── ...
```

### If categories already exist:
- Read the existing folder structure and sort new PDFs into the best-matching folder
- If a paper doesn't fit any existing category, flag it and suggest a new category

### If no categories exist — auto-suggest:
After downloading a batch, analyze the papers and propose a category structure before sorting. Follow this process:

1. **Extract key themes** from each paper: primary method/approach, organism, target product, application area
2. **Cluster by shared themes** — group papers that share a dominant axis:
   - **Method-centric clusters**: papers sharing an approach (e.g., directed evolution, CRISPR engineering, fermentation optimization)
   - **Organism-centric clusters**: papers centered on the same organism (e.g., E. coli engineering, S. cerevisiae, C. glutamicum)
   - **Product-centric clusters**: papers targeting the same output (e.g., succinate, lysine, ethanol)
   - **Review/survey papers**: always get their own `01_Reviews` folder
3. **Choose the dominant grouping axis** — whichever axis produces the most balanced, non-overlapping clusters (typically 4-8 categories for a batch of 20-50 papers). Prefer the axis that minimizes papers appearing in multiple categories.
4. **Number and name folders** using the pattern `{NN}_{Category_Name}`:
   - `01_Reviews` is always first
   - Remaining categories numbered `02`–`NN` in rough order from upstream (feedstock/depolymerization) to downstream (products/applications)
   - Names should be 2-4 words, underscored, descriptive: `02_Metabolic_Engineering`, `05_Enzyme_Discovery`
5. **Present the proposed structure** to the user as a table:

```
## Proposed Category Structure

| Folder | Category | Papers |
|--------|----------|--------|
| 01_Reviews/ | Review articles & surveys | 8 |
| 02_Metabolic_Engineering/ | Strain engineering & pathway design | 6 |
| 03_Biological_Funneling/ | Microbial aromatic catabolism | 5 |
| ... | ... | ... |

Does this grouping work, or would you like to adjust?
```

6. **Apply after confirmation** — create folders and move PDFs only after the user approves or modifies the structure

---

## Prerequisites — PubMed MCP

**This skill depends on PubMed MCP integration.** PubMed is the single best source for resolving article identifiers, checking OA status, and downloading full-text PDFs via PMC. Always start here.

Before attempting any downloads, verify PubMed MCP is available:
1. Call `mcp__claude_ai_PubMed__search_articles` with a simple test query
2. If it fails, guide the user to run the **pubmed-setup** skill first
3. Do NOT proceed with batch downloads without PubMed MCP — it is the backbone of identifier resolution and the most reliable download source

---

## Download Strategy — Exhaustive and Persistent

**CRITICAL PRINCIPLE: Never give up after one or two failed attempts.** For every paper, exhaust ALL sources below before marking it as unavailable. Many papers that appear paywalled have free copies somewhere — an author's personal site, a university repository, a government archive, or an alternative version (preprint, accepted manuscript, supplementary). The difference between downloading 50% vs 85% of a reading list is persistence, not luck.

**Do NOT stop at the first failure for a paper. Work through EVERY tier systematically.**

### Tier 0: PubMed MCP (ALWAYS do this first for every paper)

**Before trying any download source, resolve the paper through PubMed MCP:**

1. **Get metadata**: `mcp__claude_ai_PubMed__get_article_metadata` — retrieves title, authors, journal, DOI, PMID, abstract
2. **Convert IDs**: `mcp__claude_ai_PubMed__convert_article_ids` — get PMCID from DOI or PMID (PMCID is the key to free PDFs)
3. **Check copyright**: `mcp__claude_ai_PubMed__get_copyright_status` — tells you if the article is OA and what license it has
4. **Try full text**: `mcp__claude_ai_PubMed__get_full_text_article` — if the article is in PMC, this returns the full text directly

If PubMed returns a PMCID, the PDF is almost certainly available — proceed to Tier 1 step 1.
If PubMed has the article but no PMCID, the metadata still provides DOI, journal, and year needed for all other tiers.
If the paper isn't in PubMed at all (preprints, non-biomedical), fall through to Tier 1 step 2 onward.

### Tier 1: Near-Guaranteed (try these first)

**1. PubMed Central (PMC) direct download**
- Requires PMCID from Tier 0
- URL pattern: `https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{id}/pdf/`
- This is the single most reliable PDF source — if a PMCID exists, this works ~95% of the time
- **Also try**: individual article PDF links within PMC (some have multiple PDF files — main text vs. supplement)

**2. MDPI Journals (Polymers, Catalysts, Biomolecules, Molecules, etc.)**
- All MDPI journals are open access
- URL pattern: `https://www.mdpi.com/{journal}/{volume}/{issue}/{article_number}/pdf`
- Alternative: append `/pdf` to the article URL
- These almost always work directly

**3. Springer Open / Nature Communications OA / BMC**
- Springer Open journals provide direct PDF links
- Look for the PDF download link on the article page
- URL often contains `/content/pdf/` in the path
- Nature Comms: `https://www.nature.com/articles/{id}.pdf`
- Springer: `https://link.springer.com/content/pdf/{doi}.pdf`

**4. bioRxiv / medRxiv Preprints**
- Always open access
- URL pattern: `https://www.biorxiv.org/content/{doi}v{version}.full.pdf`
- Reliable and fast
- **Also check**: even for published papers, the preprint version may still be on bioRxiv — search by title or author

### Tier 2: Usually Works — Query ALL of These

**5. Unpaywall API (free, no key required)**
- Query: `https://api.unpaywall.org/v2/{doi}?email=user@example.com`
- Returns OA status and direct PDF URLs when available
- Finds green OA copies (author manuscripts in repositories)
- **Check ALL `oa_locations` in the response, not just the `best_oa_location`** — sometimes the "best" link is broken but an alternative works
- This is the single best check for OA availability across all publishers

**6. Europe PMC**
- Alternative to PubMed Central, sometimes has papers PMC doesn't
- Full text: `https://europepmc.org/article/med/{pmid}`
- PDF: `https://europepmc.org/backend/ptpmcrender.fcgi?accid=PMC{id}&blobtype=pdf`
- **Also try**: Europe PMC manuscript repository (author manuscripts accepted under OA mandates)

**7. DOE OSTI / NREL / National Lab Repositories**
- Government-funded research often has free PDFs
- NREL: `https://docs.nrel.gov/docs/...`
- OSTI: `https://www.osti.gov/biblio/{id}` — look for "Full Text Available" links
- DOE PAGES: `https://www.osti.gov/pages/` — aggregates DOE-funded publications
- If the paper acknowledges DOE/USDA/NSF/NIH funding, there is very likely a free copy in a government archive

**8. Semantic Scholar API**
- `https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=openAccessPdf`
- Returns direct PDF URL if open access
- Free, no API key needed for low-volume requests
- **Also try by title**: `https://api.semanticscholar.org/graph/v1/paper/search?query={url_encoded_title}&fields=openAccessPdf`

### Tier 3: Institutional & Author Repositories

**9. University / Institutional Repositories**
- Web search: `"{paper title}" filetype:pdf site:edu` or `"{paper title}" filetype:pdf site:ac.uk`
- Many universities mandate open deposit — the author's accepted manuscript is often in their institutional repository
- Common repositories: DSpace, EPrints, Digital Commons — these host author PDFs

**10. Author Personal / Lab Websites**
- Web search: `"{first author last name}" "{shortened paper title}" pdf`
- Many researchers post PDFs of their publications on lab websites
- Check the corresponding author's Google Scholar profile — sometimes links to free PDFs
- Look for "Publications" pages on lab/group websites

**11. Preprint Versions (Even for Published Papers)**
- Even if the final published version is paywalled, a preprint or accepted manuscript may exist:
  - bioRxiv/medRxiv: search by title
  - arXiv: for computational/modeling papers
  - chemRxiv: for chemistry-focused papers
  - SSRN/Preprints.org: less common in biotech but worth checking
  - Web search: `"{paper title}" preprint pdf`
- The preprint is scientifically equivalent for most purposes (note the version in the filename if using a preprint)

**12. PubMed Author Manuscript / NIH Public Access**
- NIH-funded papers are required to be in PMC within 12 months
- If a paper acknowledges NIH funding but isn't in PMC yet, it may appear later
- Check: `https://www.ncbi.nlm.nih.gov/pmc/?term={title}` — sometimes PMC has it under a slightly different ID
- Author manuscripts in PMC have "nihms" prefix — these are freely available

### Tier 4: Publisher-Specific OA Checks

**13. Publisher OA Programs**
- **ACS AuthorChoice / ACS Open Access**: some ACS articles are OA — check the article landing page for an open lock icon
- **Wiley OnlineOpen**: look for CC license badge on the article page
- **Elsevier Open Access**: some articles under CC licenses — check "Access" section on ScienceDirect
- **RSC**: some Gold OA articles — check for "Open Access" tag
- **Taylor & Francis**: check for OA badge
- **Annual Reviews**: some articles become free after a period — check if the specific article is unlocked
- **Science/AAAS**: Science Advances is fully OA; Science has some OA articles
- **Cell Press / Elsevier**: Cell Reports is OA; check individual article access status

**14. Special Access Programs**
- **CHORUS** (publisher access for federally funded research): `https://www.chorusaccess.org/`
- **Research4Life / HINARI**: institutional access programs (check if user's institution qualifies)
- **Temporary OA promotions**: publishers sometimes make articles free during events — a web search may reveal a free link that a direct publisher URL doesn't

### Tier 5: Last Resort

**15. Direct Web Search — Creative Queries**
- `"{exact paper title}" pdf` — sometimes finds copies in unexpected places
- `"{exact paper title}" filetype:pdf` — narrows to actual PDF files
- `"{doi}" pdf` — sometimes finds hosted copies
- `"{first author}" "{year}" "{journal}" pdf` — if title is long/complex
- Try Google and Bing separately — they index different repositories
- Check the first 2-3 pages of results, not just the first result

**16. Supplementary / Alternative Versions**
- Some papers have freely available supplementary PDFs even when the main text is paywalled
- Conference proceeding versions of journal articles may be free
- Thesis chapters that contain the paper's content may be freely available
- Book chapters: check if the author deposited a preprint of the chapter

### DO NOT Attempt (Confirmed Time Sinks)

- **Direct publisher PDF URLs without OA verification** — will redirect to login/paywall 90% of the time, wastes time on HTTP redirects
- **Google Scholar "All versions" PDF links** — unreliable, often cached previews or broken links
- **ResearchGate / Academia.edu full text** — require login, block automated access, return HTML not PDF
- **Sci-Hub** — legal issues, unreliable availability, blocked in many networks
- **Scraping publisher sites** — violates ToS, gets IP blocked, fragile
- **Emailing authors programmatically** — out of scope for automated retrieval

---

## Download Workflow

### Persistence Protocol

**The #1 rule: DO NOT mark a paper as "unavailable" until you have tried at least 8 different sources/approaches.** Track each attempt in the download log.

For each paper, maintain an attempt log:
```
Paper: Smith et al. 2024, DOI: 10.1234/example
  Attempt 1: PMC — no PMCID found
  Attempt 2: Unpaywall — returned OA location, but PDF link was broken (403)
  Attempt 3: Europe PMC — not indexed
  Attempt 4: Semantic Scholar — no OA PDF
  Attempt 5: Web search "title" filetype:pdf — found author manuscript on university repo ✅
```

### For a single paper:

1. **PubMed MCP first (Tier 0)** — Resolve DOI, PMID, PMCID, and OA status using PubMed MCP tools. If the paper isn't in PubMed, use Semantic Scholar or CrossRef to resolve identifiers.
2. **Work through tiers systematically** — Start at Tier 1 (PMC direct download if PMCID exists), proceed through every tier. For each source:
   a. Attempt the download
   b. **Verify immediately** (see Verification Steps below)
   c. If verification fails, log the failure reason and move to the next source
   d. If verification passes, name and sort the file — done
3. **If all tiers exhausted** — mark as genuinely unavailable with a full attempt log

### For a batch of papers:

1. **Build a manifest via PubMed MCP** — Run Tier 0 for ALL papers first: resolve identifiers, get PMCIDs, check OA status. This gives you the full picture before downloading anything.
2. **Fast pass (Tier 1-2)** — Download from PMC (for all papers with PMCIDs), then publisher OA and Unpaywall for the rest. This handles the easy ones quickly.
3. **Stubborn pass (Tier 3-5)** — For every paper that failed the fast pass, go through Tier 3-5 sources one by one. This is where persistence pays off.
4. **Report results** with full transparency:

```
## Download Results

| # | Paper | Attempts | Source | Status | Filename |
|---|-------|----------|--------|--------|----------|
| 1 | Smith et al. 2024 | 1 | PMC | ✅ Downloaded | MetabEng_Ecoli_succinate_2024.pdf |
| 2 | Chen et al. 2025 | 3 | Author site | ✅ Downloaded | NatComm_enzyme_biocatalysis_2025.pdf |
| 3 | Park et al. 2023 | 9 | — | ❌ Paywalled (all sources exhausted) | — |

**Downloaded: 18/20 (90%)**
**Genuinely paywalled: 2 (exhausted all 15+ sources)**
**Total download attempts: 87**
```

5. **For remaining paywalled papers**, suggest:
   - Check institutional access (if user has university/company library)
   - Request from corresponding author directly (provide email if found)
   - Check back in a few months (OA embargoes lift, preprints appear)
   - Note if a preprint version exists that could substitute

6. **Save the full manifest** — Write a detailed `download_log.md` in the literature folder including every attempt, so future sessions never repeat failed approaches

---

## Verification Steps

After EVERY download attempt, verify the file before accepting it:

```bash
# Step 1: Check file is actually PDF (not HTML redirect or error page)
file path/to/downloaded.pdf
# MUST say "PDF document" — reject "HTML document", "ASCII text", "XML", "empty"

# Step 2: Check file size is reasonable
ls -la path/to/downloaded.pdf
# Research article PDFs are typically 200KB–30MB
# <100KB is suspicious — likely an error page, CAPTCHA, or stub
# >50MB is suspicious — might be a wrong file

# Step 3: Check PDF header bytes
head -c 5 path/to/downloaded.pdf
# Must start with %PDF- (the PDF magic number)
```

**Common failure modes to catch:**
- **HTML masquerading as PDF**: Publisher returned a login/paywall page with .pdf extension. The `file` command catches this.
- **Tiny PDF stub**: Some publishers return a 1-page PDF saying "buy this article." Check that page count is >1 and file size is >200KB.
- **Corrupted/truncated download**: If `file` says "PDF document" but the file can't be opened, the download was interrupted. Re-try with a longer timeout.
- **Wrong paper**: Spot-check by extracting the first page text and confirming the title matches.

If verification fails:
- **Delete the invalid file immediately** — don't let it pollute the library
- Log the failure reason (HTML redirect, stub PDF, corrupted, wrong paper)
- Move to the next source in the tier list
- **Do NOT count a failed verification as "paper unavailable"** — it means that specific source failed, not that the paper can't be found

---

## Resuming from a Previous Session

When starting a batch download and the literature directory already exists:

1. **Check for `download_log.md`** — if present, read it to find previously attempted papers and their outcomes
2. **Do NOT re-attempt previously successful downloads** — verify the PDF still exists at the logged path
3. **Re-attempt previously failed papers** — but start from the last-attempted tier, not from scratch
4. **Check existing folder structure** — sort new papers into existing categories rather than proposing a new structure
5. **Update the download log** with new attempts appended, don't overwrite

---

## Integration with Other Commands

- **After `/sci-search`**: Offer to download all OA papers from the search results
- **With `/sci-library`**: Update library metadata with local PDF paths after download
- **Before `/sci-read`**: Ensure the PDF is downloaded before attempting to read/analyze it

---

## User Interaction

### When starting a batch download:
1. Show the user the list of papers and predicted OA availability
2. Confirm the target directory and category folders
3. Ask about naming preferences if the convention isn't established
4. Proceed with downloads, reporting progress

### When a paper can't be downloaded:
- Clearly state it's paywalled or unavailable
- Suggest: institutional access, interlibrary loan, emailing the corresponding author
- Never pretend a download succeeded when it didn't

### When the user provides a reference list or search results:
- Parse out DOIs, PMIDs, titles, and journals
- Resolve missing identifiers via PubMed
- Triage OA availability before attempting downloads
- Give an honest estimate: "Of these 30 papers, ~18 appear to be open access. Want me to download those?"
