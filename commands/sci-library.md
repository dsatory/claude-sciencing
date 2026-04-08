---
description: Manage a local reference library — add papers, organize by topic, generate bibliographies, export citations, track reading status
argument-hint: [action] [details]. Actions: add, list, tag, find, export, status, stats
allowed-tools: Read, Glob, Grep, Bash, Edit, Write, WebSearch, WebFetch, mcp__claude_ai_PubMed__get_article_metadata, mcp__claude_ai_PubMed__lookup_article_by_citation, mcp__claude_ai_PubMed__convert_article_ids
---

# Reference Library Management

Manage a local, file-based reference library. The library lives as a collection of markdown and BibTeX files in the project, making it version-controllable, searchable, and portable.

## Library Structure

The library uses a simple, flat file structure:

```
references/
├── library.md          — Master index of all references with tags and status
├── library.bib         — BibTeX file for all references (for LaTeX/citation tools)
├── notes/              — Per-paper reading notes (optional)
│   ├── smith-2024-succinic-acid.md
│   └── chen-2025-enzyme-engineering.md
└── lists/              — Curated reading lists by topic
    ├── strain-engineering.md
    └── techno-economics.md
```

Create this structure on first use if it doesn't exist. If the user already has a `references/` directory, adapt to their existing layout.

---

## Actions

### add — Add a reference to the library

The user provides one or more of: DOI, PMID, URL, citation string, or manual entry.

1. **Resolve metadata** — Use PubMed tools or web search to get full bibliographic data
2. **Generate BibTeX entry** — Append to `references/library.bib`
3. **Add to library index** — Append to `references/library.md` with tags and status
4. **Confirm** — Show the user what was added

**Library index entry format:**
```markdown
### [Citation key]
**Title:** Full title
**Authors:** Last, F., Last, F., ... (et al. if >3)
**Journal:** Name (Year) Volume:Pages
**DOI:** https://doi.org/...
**PMID:** if available
**Tags:** #metabolic-engineering #succinic-acid #E-coli
**Status:** unread | reading | read | cited
**Added:** YYYY-MM-DD
**Notes:** [brief note on why it was added, or link to notes file]
```

**BibTeX entry format:**
```bibtex
@article{smith2024succinic,
  author  = {Smith, J. and Chen, L. and Park, S.},
  title   = {Engineering E. coli for high-titer succinic acid production},
  journal = {Metabolic Engineering},
  year    = {2024},
  volume  = {82},
  pages   = {110--121},
  doi     = {10.1016/j.ymben.2024.01.005},
}
```

### Batch Add
When the user provides multiple references (a list of DOIs, a reference section from a paper, or search results from `/sci-search`):
- Process each one
- Add all to the library
- Show a summary table of what was added

---

### list — List references in the library

Display the library contents with optional filters:
- `list` — Show all references, grouped by tag
- `list --tag enzyme-engineering` — Filter by tag
- `list --status unread` — Filter by reading status
- `list --recent` — Sort by date added (newest first)
- `list --year 2024` — Filter by publication year

Output as a clean, scannable table:
```
| Key | Title (shortened) | Year | Tags | Status |
|-----|-------------------|------|------|--------|
```

---

### tag — Add or modify tags on references

- `tag smith2024 #strain-engineering #high-priority` — Add tags
- `tag smith2024 --remove #low-priority` — Remove a tag

Tags are freeform but suggest consistent conventions:
- **Topic tags:** #metabolic-engineering, #enzyme-engineering, #fermentation, #TEA
- **Organism tags:** #E-coli, #S-cerevisiae, #C-glutamicum
- **Use tags:** #for-proposal, #for-lit-review, #benchmark-data
- **Priority tags:** #must-read, #high-priority, #background

---

### find — Search the library

Search across titles, authors, tags, and notes:
- `find succinic acid` — Full-text search
- `find --author Chen` — Search by author
- `find --tag #for-proposal` — Search by tag
- `find --cited` — Show only references marked as cited

---

### export — Export references

- `export bibtex` — Output the full BibTeX file path
- `export bibtex --tag for-proposal` — Export a filtered subset as BibTeX
- `export markdown` — Export a formatted reference list in markdown
- `export numbered` — Export as a numbered reference list (for reports/proposals)
- `export apa` — Export in APA format
- `export vancouver` — Export in Vancouver/numbered format

**Numbered export format:**
```
[1] Smith J, Chen L, Park S. Engineering E. coli for high-titer succinic acid
    production. Metab Eng. 2024;82:110-121. doi:10.1016/j.ymben.2024.01.005

[2] ...
```

---

### status — Update reading status

- `status smith2024 read` — Mark as read
- `status smith2024 cited` — Mark as cited (used in a document)
- `status chen2025 reading` — Mark as currently reading

Statuses: `unread` → `reading` → `read` → `cited`

---

### stats — Library statistics

Show a summary:
```
📚 Library: 47 references
   Unread: 12 | Reading: 3 | Read: 28 | Cited: 4

📋 Top tags:
   #metabolic-engineering (18) | #enzyme-engineering (12) | #TEA (8)

📅 Recently added: 5 in last 7 days
```

---

## Reading Notes

When the user runs `/sci-read` on a paper that's in the library, offer to save the analysis as a reading note in `references/notes/`. Link the note from the library index entry.

**Note file format:**
```markdown
---
ref: smith2024succinic
read_date: 2026-04-05
---

# Smith et al. 2024 — Succinic acid in E. coli

## Bottom Line
[From /sci-read output]

## Key Findings
- ...

## Relevance to Our Work
- ...

## Data Extracted
[Tables from /sci-read extract mode]

## Questions / Follow-ups
- ...
```

---

## Integration with Other Commands

- **/sci-search** results can be piped to `/sci-library add`
- **/sci-read** analyses can be saved as reading notes
- **/sci-draft** can pull citations from the library for proposals and reports
- **/sci-review** uses the library as its source of papers to synthesize
- **paper-retrieval** skill handles the actual downloading with a 7-tier, 20-source strategy — sci-library tracks what's been acquired and organizes it

---

## Resuming from a Previous Session

When the user starts a new conversation and the library already exists:

1. **Check for existing library files** — look for `references/library.md` and `references/library.bib` in the project directory
2. **If found, read `references/library.md`** to understand the current state: how many references, which tags are in use, what reading statuses exist
3. **Report status briefly** — "Found your library with 34 references (12 unread, 18 read, 4 cited). Ready to continue."
4. **Do NOT re-add papers already in the library** — check for existing DOIs/PMIDs before adding duplicates
5. **Respect existing tag conventions** — use the tags already in the library rather than inventing new ones

When the user asks to "continue" or "pick up where we left off":
- Check for `download_log.md` in the literature folder for incomplete downloads
- Check `references/library.md` for references with `unread` status
- Check for draft files in the project directory that may be in progress
- Summarize what exists and ask what to work on next

### Download Log

The `paper-retrieval` skill maintains a `download_log.md` in the `literature/` folder. When resuming:
- Read this log to see which papers were successfully downloaded, which failed, and from which sources
- Do NOT re-attempt downloads that already succeeded (verify the PDF still exists at the logged path)
- For previously failed papers, start from the last-attempted tier rather than from scratch
- Append new attempts to the log — never overwrite it

### Patent Library

Patents are stored in a dedicated `XX_Patents/` folder (numbered last in the category structure). When resuming:
- Check for existing patents and their metadata
- Do not re-download patents already in the library
- Patent PDFs follow the naming convention: `USPat_`, `USApp_`, `EPPat_`, `WOApp_` + description + year

---

## General Guidance

- Always resolve full metadata when adding (don't store incomplete entries)
- Keep BibTeX keys consistent: `lastnameyearkeyword` (e.g., `smith2024succinic`)
- When the user shares a reference list from a paper, offer to batch-add all entries
- If the library doesn't exist yet, create it on first `add` command
- Prefer DOIs as the canonical identifier (most reliable for lookup)
- When adding references, check the `download_log.md` to see if the paper has already been attempted
- Patents can be added to the library like papers — use patent numbers as identifiers alongside DOIs
