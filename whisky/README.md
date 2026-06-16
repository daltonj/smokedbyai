# 🥃 The Curator's Guide — Whisky Tasting Research Engine

A source-backed, interactive dossier for a high-end Scotch tasting, plus the **repeatable agentic
workflow** that built it. Everything is a pure function of a local **knowledge graph** — no number
appears in the product that doesn't trace to a cached expert/auction source.

## The product
Open **[`index.html`](index.html)** in any browser (self-contained; data is embedded, so it works
offline — charts need internet for the Chart.js CDN). It gives you:

- **Red/amber/green data-sufficiency matrix** — at a glance, where the research is solid vs thin.
- **Balanced rubric ranking** (50% drinking quality, 50% value/investment) with **live re-weight
  sliders** that re-rank everything in real time.
- **Value-for-money** and **retail-vs-secondary** charts.
- **Recommended tasting flight** with per-dram talking points + a printable cheat-sheet.
- **Per-bottle cards** — vitals, nose/palate/finish, curator verdict, UK & US retail, auction/secondary
  values — where **every datapoint links to its live source and its cached local copy**.
- **Editable, persistent notes** — your own live scores + tasting notes per dram (saved to
  `localStorage`); export to JSON.

## The lineup (8 bottles)
Isle of Skye **21 / 25 / 30** (blended) · Glengoyne **24** (White Oak) / **25** (Sherry) ·
Tamdhu **18 / 21** (oloroso) · Rosebank **31** (Release Two = the genuine 31yo) — with Rosebank
**30** (Release One) included as related context. (Rosebank's "Release One" is a 30yo; the **31** you
asked for is **Release Two**.)

## Data provenance & honesty
- **Research anchor: 2026-06-16.** Freshness window: **Dec 2025 – Jun 2026**.
- This environment's `WebFetch` egress was blocked (HTTP 403), so sources were captured via
  **WebSearch** against the named expert/retail/auction pages (`fetch_method: websearch_excerpt`).
  This is transparent in every capture and was **independently reproduced by an adversarial verifier**.
- **No vibing:** unsourced values are marked `N/A — not found`; values that failed verification are
  quarantined to `N/A — unverified` (see `kb/verification-report.md`).
- Verification caught real defects (e.g. Tamdhu 21's £299 was the RRP vs a live £295; a Rosebank 30
  auction hammer cited to the wrong capture) — **no fabricated values, no R1/R2 cross-contamination**.

## Knowledge graph (`kb/`)
- `kb/schema.md` — the entity/relationship contract (extensible for future whiskies).
- `kb/distilleries/*.json` — distillery/brand nodes.
- `kb/expressions/*.json` — one node per bottle (vitals, tasting, scores, prices, auction, rubric,
  coverage, verification, `source_ids`). `*.verify.json` = adversarial per-field verdicts.
- `kb/sources/<cluster>/*.md` — raw cached captures; `kb/sources/manifest.json` — evidence index.
- `kb/verification-report.md` — merged verification audit.

## Rebuild / extend
Regenerate the product from the KG after any change:
```bash
python3 whisky/build_guide.py      # compiles data.json + injects it into index.html, recomputes coverage
```

**Add another whisky** (repeatable workflow) — the skills under `.claude/skills/` encode it:
`whisky-orchestrate` chains **research → curate → verify → gap-fill → rebuild**, dispatching ≥3 agents
per whisky (Researcher · skeptical Curator · adversarial Verifier). New bottles append to the same KG
and appear in the guide on the next build. See `.claude/skills/whisky-*/SKILL.md`.

## Coverage rule (definition of done)
**GREEN** = ≥3 reviews · ≥2 numeric scores · UK price · US price · auction point · a fresh datapoint —
**and** verification passed. **AMBER** = solid but missing one of those. **RED** = thin (no market price,
or no score and <2 reviews). Coverage is recomputed at build time so the signal stays consistent.
