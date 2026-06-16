---
name: whisky-guide
description: Builder stage of the whisky engine. Use to (re)generate the interactive HTML Curator's Guide (whisky/index.html) and its whisky/data.json from the knowledge graph. The product is a pure function of the KG — never hand-edit data into the HTML; regenerate it whenever the KG changes.
---

# whisky-guide — Builder stage

Output: `whisky/data.json` (compiled from the KG) + `whisky/index.html` (self-contained, no build step).

## Procedure
1. Read all `kb/expressions/*.json` + `kb/distilleries/*.json` + `kb/sources/manifest.json`. Compile a
   single `whisky/data.json` (array of expressions with their distillery, scores, prices, auction,
   rubric, coverage, verification, and source links — both live URL and `local_path`).
2. Generate `whisky/index.html`: vanilla JS + Chart.js via CDN, data loaded from `data.json` (with an
   inline fallback so it works opened from `file://`). Required sections:
   - **Coverage dashboard:** red/amber/green matrix + per-criterion checklist; "data as of <anchor>" stamp; stale flags.
   - **Ranking + value viz:** composite-ranking bar chart; quality-vs-price scatter; UK-vs-US price bars; Rosebank auction-trend line.
   - **Per-whisky cards (curator voice):** vitals, nose/palate/finish, score chips, UK/US retail, auction value, verdict — every datum links to live URL **and** cached copy.
   - **Live rubric sliders:** re-weight → recompute composite + re-rank in real time.
   - **Tasting plan:** ordered flight + talking points; printable cheat-sheet view (@media print).
   - **Editable + persistent:** personal live scores + notes per dram saved to `localStorage`; export/print.
   - **Sources appendix:** master cited list grouped by bottle, type, freshness.
3. Keep it accessible and fast; no framework, no bundler. Re-run this whenever the KG changes.
