---
name: whisky-research
description: Researcher stage of the whisky engine. Use to gather freshness-biased, expert-sourced data on a whisky (tasting reviews, numeric scores, UK + US retail prices, auction/secondary values, recent news), WebFetch and cache every source verbatim into the KG, and draft the expression node. Breadth over a single search; expert sources only, no slop, no vibing.
---

# whisky-research — Researcher stage

Goal: assemble a fully-sourced draft for one expression. **Cite-or-drop. No memory, no vibing.**

## Source policy
APPROVED — *critics:* Whiskyfun (Serge Valentin), Malt Review, Dramface, WhiskyNotes (Ruben Luyten),
The Dramble, Words of Whisky, Whisky Advocate, Whisky Magazine, Master of Malt & The Whisky Exchange
tasting notes, Distiller, Connosr, Diving for Pearls, GreatDrams, The Whiskey Wash, Robb Report/Forbes
spirits, award bodies (IWSC/ISC/SFWSC). *retail:* The Whisky Exchange, Master of Malt, Royal Mile
Whiskies, Hard To Find (UK); Total Wine, Caskers, Wine-Searcher, ReserveBar (US). *auction/indices:*
Whisky Auctioneer, Scotch Whisky Auctions, Whisky.Auction, Whisky-Online Auctions, Just Whisky,
Whiskystats, Whiskybase, Whiskyhunter, Rare Whisky 101.
BANNED — AI listicles, generic "best whisky" SEO pages, dropship/Amazon-reseller blogs, Pinterest,
content farms, any page lacking named provenance or a verifiable record.

## Fetch channel (environment-aware)
Prefer `WebFetch` for full-page verbatim captures. **If WebFetch egress is blocked (HTTP 403),
fall back to `WebSearch`** — it is the only live channel in some sandboxes. WebSearch returns real,
attributed data from expert-source pages (prices, scores, tasting text) with their URLs and a
current-month recency bias; use `allowed_domains` to target the whitelist. This is NOT vibing: the
data comes from a search of the named source, not from memory. Captures created this way MUST set
`method: websearch`, record the exact query, the returned excerpt verbatim, and the attributed source
URL — full transparency that the page body was not directly fetched. The Verifier re-runs searches to
confirm each datum reproduces. Never invent a number that no search returns.

## Procedure (per expression — multiple searches, not one)
1. Run separate searches for: (a) expert tasting reviews, (b) numeric scores, (c) UK retail price,
   (d) US retail price, (e) auction/secondary value + trend, (f) news in the **last 6 months**.
   Bias queries toward 2026 / recent. Capture the source date on every result.
2. For each kept result, capture it to `kb/sources/<cluster>/<src_id>.md` with the schema's YAML
   front-matter + verbatim excerpts (actual price/score/tasting text + dates). Add `method: webfetch`
   or `method: websearch` to the front-matter per the channel used (see above).
3. Append a manifest entry to `kb/sources/<cluster>.manifest.json` (include `method`).
4. Draft `kb/expressions/<slug>.json` per schema — every field's `source_ids` point to captures.
   Leave rubric/coverage/verification for later stages; mark unknowns `N/A — not found`.

Hand off the draft + a list of any gaps you couldn't source.
