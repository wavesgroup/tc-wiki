# Hurricane Wiki Schema

Use this reference only when the repository has no established wiki schema or when you need to normalize inconsistent pages.

## Default Layout

```text
raw/
  papers/
  assets/
wiki/
  papers/
  topics/
  storms/
  basins/
  datasets/
  methods/
  syntheses/
  index.md
  log.md
```

Keep raw sources immutable. All agent-authored work belongs under `wiki/`.

## Link Style

- Prefer standard markdown links with relative paths.
- If the repository already uses Obsidian wikilinks, keep using them instead of converting styles.
- Link narrowly first. A topic page should link to the specific paper, storm, dataset, or method page that supports the claim.

## Optional Frontmatter

Use frontmatter only if the repo already uses it or if you are initializing a new wiki.

```yaml
---
title: "Rapid Intensification"
page_type: "topic"
status: "active"
last_updated: "2026-04-05"
source_count: 12
---
```

For paper pages, also add:

```yaml
source_access: "full_text"  # or metadata_only | citation_network | mixed
```

Useful `page_type` values:

- `paper`
- `topic`
- `storm`
- `basin`
- `dataset`
- `method`
- `synthesis`

## Page Types

### Paper Pages

Suggested sections:

- `# Citation`
- `# Research Question`
- `# Data And Methods`
- `# Key Equations` when the page is equation-central and grounded in direct full-text access
- `# Findings`
- `# Limitations`
- `# Referenced Papers`
- `# Linked Pages`

The paper page is the staging area for source-grounded facts before they propagate elsewhere.

### Topic Pages

Suggested sections:

- `# Definition`
- `# Current Synthesis`
- `# Evidence By Source`
- `# Open Questions`
- `# Related Pages`

Topic pages should synthesize, not merely stack summaries.
Absorb new evidence into these canonical sections rather than appending dated `New Evidence` blocks.

### Storm Pages

Suggested sections:

- `# Storm Summary`
- `# Observations And Analyses`
- `# Broader Relevance`
- `# Related Papers`

Use storm pages for named storms, major field programs, or heavily studied case clusters.

### Synthesis Pages

Suggested sections:

- `# Question`
- `# Short Answer`
- `# Lines Of Evidence`
- `# Disagreement And Caveats`
- `# Implications`

Create synthesis pages for durable research questions such as rapid intensification pathways, ocean coupling, or forecast error sources.

## Citation Keys

If the repo needs stable short identifiers, prefer `surname-year-keyword`, for example:

- `shay-2000-ohc`
- `cione-2013-sst-cooling`
- `zhang-2021-ri-predictors`

Use the DOI in the paper page even if the wiki also keeps a citation key.

## Index Convention

`index.md` should be content-oriented. Organize it by page type and keep one line per page:

```markdown
- [Rapid Intensification](topics/rapid-intensification.md): Multi-paper synthesis of mechanisms, predictors, and uncertainty.
```

The index is the first navigation surface for both users and agents. Keep summaries short and current.
Avoid blurbs that describe edit history rather than content, such as `new`, `seed`, `first-pass`, or `early`.

## Log Convention

`log.md` should be append-only and chronological. Use a stable heading format:

```markdown
## [2026-04-05] ingest | zhang-2021-ri-predictors
## [2026-04-05] query | upper-ocean-cooling-vs-ri
## [2026-04-05] lint | cross-link-and-staleness-pass
```

Each entry should briefly note what changed and which pages were touched.

## When To Create A New Page

Create a new page when one of these is true:

- the concept appears in multiple papers
- the user is likely to ask about it directly
- existing pages are becoming overloaded
- a storm, method, or dataset is repeatedly referenced across topics

Otherwise, update an existing page and add the missing links.
