---
name: whisky-orchestrate
description: Top-level repeatable agentic workflow for the whisky research engine. Use to research one or more whiskies end-to-end and append them to the knowledge graph and the interactive guide. Dispatches the Research -> Curate -> Verify -> gap-fill loop per whisky (>=3 agents each), then rebuilds the guide. This is the reusable entrypoint: "research these whiskies and add them to the guide."
---

# whisky-orchestrate — repeatable workflow

The reusable entrypoint. Given a list of whiskies (name + age[s] + optional release):

## Per whisky — dispatch a sub-agent team (minimum three roles)
1. **Researcher** (`whisky-research`) — freshness-biased multi-search, cache every source, draft node.
2. **Curator/Editor** (`whisky-curate`) — skeptical synthesis, rubric, coverage scorecard, gap list.
3. **Source Verifier** (`whisky-verify`) — adversarial per-field check vs cached sources; set pass/fail.
4. **Gap-fill loop** — if coverage RED/AMBER on core OR verification failed, re-dispatch Researcher on the
   named gaps, then re-Curate + re-Verify. Repeat until GREEN or gaps are provably unsourceable
   (then leave `N/A — not found`, status AMBER, documented).

Run independent whiskies' teams in parallel; keep each team's writes to distinct KG paths (per-cluster
source dirs + own manifest fragment) to avoid contention. Orchestrator merges manifests and spot-checks
a sample of verifications.

## After all whiskies
5. **Synthesis** — compute cross-bottle ranking from `rubric.composite`; derive tasting order
   (delicate → sherry-rich → showstopper finale), pour sizing, talking points.
6. **Build** (`whisky-guide`) — regenerate `whisky/data.json` + `whisky/index.html` from the KG.
7. **Verify product** — coverage statuses compute, sampled cached URLs match live, charts/sliders/
   localStorage/print all work. Commit to the working branch; push. No PR unless asked.

## Persona (shared)
"The Curator": expert, skeptical, precise on cask/ABV/provenance, allergic to fluff. Curators, not coders.
