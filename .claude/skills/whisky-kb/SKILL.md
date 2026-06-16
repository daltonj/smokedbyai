---
name: whisky-kb
description: Knowledge-graph contract for the whisky research engine. Use when reading or writing whisky distillery/expression/source/verification nodes, maintaining the source manifest, deduping, or appending a new whisky to the KG under whisky/kb/. Every other whisky-* skill reads and writes through this contract.
---

# whisky-kb — Knowledge Graph contract

The KG under `whisky/kb/` is the single source of truth; the HTML product is a pure function of it.
Full schema: `whisky/kb/schema.md` (read it before writing nodes).

## Layout
- `kb/distilleries/<slug>.json` — distillery/brand node
- `kb/expressions/<slug>.json` — one per bottle (slug `<distillery>-<age>[-<release>]`)
- `kb/expressions/<slug>.verify.json` — Verifier output
- `kb/sources/<cluster>/<src_id>.md` — raw cached capture (YAML front-matter + verbatim excerpts)
- `kb/sources/<cluster>.manifest.json` — per-cluster source index (avoids write contention)
- `kb/sources/manifest.json` — merged master index (orchestrator merges per-cluster files)
- `kb/verification-report.md` — human-readable cross-bottle verification summary

## Rules
- **Append, don't overwrite** unrelated nodes. A new whisky = new files; never reshape existing schema.
- Every fielded datum (price/score/tasting/auction) carries `source_id`(s) tracing to a cached capture.
- Unknown values are the literal string `N/A — not found` (never guessed).
- `id` slugs are stable and lowercase-hyphen. Source ids: `src_<bottle>_<sourceslug>`.
- Timestamps are ISO-8601 UTC. `freshness=fresh` iff within 6 months of the research anchor.

## Append-a-new-whisky entrypoint
Given a whisky name + age(s): research → curate → verify → (gap-fill loop) → guide.
Reuse existing distillery node if present; otherwise create it. Then run the other skills in order.
