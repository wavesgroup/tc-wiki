---
name: tc-wiki
description: Use this skill when building, expanding, auditing, or answering from a persistent markdown wiki of peer-reviewed tropical cyclone research, especially atmospheric dynamics, air-sea interaction, upper-ocean response, intensity change, structure, hazards, and forecasting.
metadata:
  short-description: Curate a tropical cyclone research wiki
---

# Tropical Cyclone Wiki

## Overview

This skill turns an agent into a maintainer of a persistent markdown wiki for tropical cyclone research. Use it when ingesting peer-reviewed papers, updating synthesis pages, answering questions from the wiki, or linting the wiki for contradictions, stale claims, and missing cross-links.

The raw papers are the source of truth. The wiki is the compiled layer. Prefer durable wiki edits over one-off chat summaries whenever the result would be useful again.

## Scope

Prioritize peer-reviewed literature on tropical cyclones and their atmosphere-ocean system, including:

- structure and intensity change
- rapid intensification and weakening
- track, steering, and predictability
- air-sea fluxes and boundary-layer processes
- upper-ocean cooling, ocean heat content, and coupled feedbacks
- precipitation, surge, waves, and compound hazards
- observations, reanalyses, and model evaluation

Default to peer-reviewed sources. If the user wants to include preprints, reports, operational guidance, or reviews, label them explicitly and do not mix them with primary evidence.

## First Pass In A Repository

1. Find the wiki root, `index.md`, and `log.md`. Read them before changing structure.
2. Reuse the repo's existing folder layout and link style if one already exists.
3. If the repo has no established schema, use [wiki-schema.md](./references/wiki-schema.md) as the default.
4. Never modify raw source files.

## Core Operations

### Ingest A Paper

1. Confirm the source is peer-reviewed or flag uncertainty.
2. Extract the minimum metadata needed for reuse:
   - title, authors, year, journal, DOI
   - basin, region, storms, or sample studied
   - data sources, methods, and variables
   - key findings, limitations, and uncertainty
3. Create or update the paper page first.
4. Add a `# Referenced Papers` section near the end of the paper page as a curated ingest queue:
   - list the most wiki-relevant cited papers, not the full bibliography
   - prioritize papers that support claims already propagated into topic, method, storm, dataset, basin, or synthesis pages
   - when a cited paper later gets its own wiki page, replace the plain citation with a direct wiki link
5. Update every materially affected topic, storm, dataset, method, and synthesis page.
6. Update `index.md`.
7. Append a short chronological entry to `log.md`.
   - Always add new entries at the bottom of the file so `log.md` remains in ascending chronological order (earlier entries first, later entries last).

Do not stop at the paper summary. The point of the wiki is to propagate new evidence into the existing synthesis.

### Query The Wiki

1. Read `index.md` first.
2. Read the narrowest relevant pages before reading broader synthesis pages.
3. Answer from the compiled wiki, citing both wiki pages and underlying papers when possible.
4. If the result is durable, file it back into the wiki as a synthesis page, comparison, note, or table instead of leaving it only in chat.

### Lint The Wiki

Look for:

- unsupported claims
- contradictions across pages
- single-study claims written as consensus
- stale syntheses not updated after newer papers
- repeated concepts or storms that still lack their own page
- orphan pages with weak linking
- terminology drift, especially for similar but non-identical metrics

### Maintain `authors.md`

When the repository contains a top-level `authors.md` index:

1. Rebuild it from all current `papers/*.md` pages (not from memory or partial diffs).
2. Read each paper page's `# Citation` section and extract the listed authors as written.
3. Format every author as `Last, First` in the index.
4. Group entries alphabetically by letter with an A-Z jump list at the top.
   - Keep every A-Z section present; if a letter currently has no authors, leave the section blank (do not add placeholder text such as `No authors indexed.`).
5. For each author, list links to all wiki paper pages they co-authored.
6. Use abbreviated paper link labels:
   - one author: `Surname (Year)`
   - two authors: `Surname1 and Surname2 (Year)`
   - more than two authors: `Surname1 et al. (Year)`
7. Exclude placeholder/non-person tokens (for example, `and coauthors`) from `authors.md`; do not create entries such as `Coauthors, Unspecified`.
8. Run a duplicate pass before finalizing: detect likely duplicates where `Last name + first initial` match (for example, `Fischer, M. S.` vs `Fischer, Michael S.`), merge them into one canonical entry, and combine all paper links under that entry.
9. After updating `authors.md`, add or refresh its link from the top-level `index.md` page.

### Maintain `tc-cases.md`

When the repository contains a top-level `tc-cases.md` index:

1. Rebuild it from all current wiki pages (not from memory or partial diffs).
2. Include only specific named historical/real tropical cyclones that are explicitly and materially discussed on current wiki pages.
3. Exclude idealized vortices, unnamed seasonal samples/composites, nature runs, generic basin summaries, and storms that appear only inside cited-reference titles unless the wiki text itself also discusses them as cases.
4. Group entries by basin and include a basin jump list at the top.
5. Order basin sections alphabetically.
6. Within each basin, create year subsections using storm year (not publication year) in ascending order.
7. Within each year subsection, sort storm names alphabetically.
8. Format each case entry as a bold storm name followed by a short one-line synthesis of why the case matters in the wiki, then links to the current wiki pages that materially discuss it.
9. Use only links to current wiki pages; prefer the underlying paper page plus any topic/synthesis/method pages that explicitly discuss the named storm.
10. After updating `tc-cases.md`, add or refresh its link from the top-level `index.md` page.

## Writing Rules

- Separate what the paper observed from what the paper inferred.
- Attribute claims precisely: `Author et al. (Year) found ...`
- Preserve disagreement. If papers conflict, state the conflict and possible reasons.
- Distinguish mechanism, evidence, and operational implication.
- Record limitations, especially small samples, retrospective framing, model dependency, basin specificity, and sensitivity to definitions.
- Do not invent numerical claims or thresholds the source did not make.
- If a useful point comes from interpreting a figure, mark it as an inference from the figure rather than a direct textual claim.
- For review articles, keep cited-reference lists curated and functional. Do not paste the full bibliography into the main paper page unless the repository explicitly wants full bibliographies.
- Prefer updating a shared synthesis page over duplicating the same paragraph across many pages.
- Create a new page when a concept is central to multiple papers or is likely to become a repeated query target.

## Hurricane-Specific Heuristics

When deciding which pages to touch, check across these buckets:

- storms and case studies
- basins and environmental regimes
- physical processes such as shear interaction, eyewall replacement, vortex tilt, air-sea fluxes, ocean cooling, rainband dynamics, surge, and waves
- metrics and predictors such as SST, OHC, TCHP, MPI, VWS, humidity, instability, and RI predictors
- observing systems such as aircraft, dropsondes, satellites, floats, buoys, and reanalyses
- model and analysis methods such as coupled models, idealized models, data assimilation, statistical tools, and machine learning
- synthesis topics such as rapid intensification, air-sea coupling, forecast error sources, hazard pathways, and climate relationships

Touch the narrowest pages that changed and at least one broader synthesis page when the new paper materially shifts understanding.

## Evidence Standard

Prefer claims backed directly by the paper text, tables, figures, or supplement. Keep review articles separate from primary evidence. If a paper is outside scope, methodologically weak, or only partially relevant, say so plainly in the paper page instead of silently blending it into consensus language.

## Suggested Session Pattern

1. Read `index.md` and the latest entries in `log.md`.
2. Read the target paper or the target wiki pages.
3. Draft updates in the paper page first.
4. Propagate those updates into topic, storm, dataset, method, and synthesis pages.
5. Update `index.md` and `log.md`.
6. Tell the user what changed, what remains uncertain, and what sources would most improve the wiki next.

## Reference

Use [wiki-schema.md](./references/wiki-schema.md) only when the repository does not already have a clear wiki layout or when page conventions have drifted.
