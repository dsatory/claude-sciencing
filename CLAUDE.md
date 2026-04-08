# Claude Sciencing Canonical Metadata

This file is the canonical repo-level reference for command names, managed tool names, and on-disk paths that other command and skill files point at.

## Slash Commands

- `/sci-search`
- `/sci-library`
- `/sci-read`
- `/sci-review`
- `/sci-draft`
- `/sci-edit`
- `/sci-figures`
- `/sci-patents`

## Managed Tool Names

These are the managed Claude.ai tool namespaces referenced across the repo today:

- `mcp__claude_ai_PubMed__*`
- `mcp__claude_ai_Slack__*`
- `mcp__claude_ai_Atlassian__*`

Do not add references to new managed tool namespaces in commands or skills unless the target environment actually exposes them.

## Canonical Project Layout

Reference-library and literature paths should stay consistent across the repo:

```text
references/library.md
references/library.bib
references/notes/
references/lists/
literature/PDFs/
literature/download_log.md
```

Use these paths everywhere. Do not refer to root-level library files.

## Provider-Safe Core Path

The provider-agnostic core workflow is:

1. PubMed via managed connector when available, otherwise NCBI E-utilities
2. OpenAlex HTTP API
3. Semantic Scholar HTTP API
4. bioRxiv/medRxiv API or targeted web search
5. Local filesystem + Google Drive sync folders for existing materials

Optional enterprise search or third-party MCP integrations should be documented as optional environment-specific add-ons, not as guaranteed bundled dependencies.
