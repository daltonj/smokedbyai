# THE SNOB — Expert Audit of The Curator's Guide

_Read-only critique. Anchor 2026-06-16. Reviewer: "The Snob" (whisky expert + data auditor)._
_Scope: `whisky/index.html`, `whisky/data.json`, `whisky/kb/expressions/*.json`, `whisky/kb/verification-report.md`, `whisky/kb/schema.md`._

**Counts: P0 = 6 · P1 = 9 · P2 = 6.**

Verdict in one line: the underlying *data* is mostly honest and well-flagged in the node files, but the **product layer (index.html) quietly drops the most important caveats** (Rosebank release identity, RRP-vs-live, currency provenance) and the **rubric over-rewards the Rosebanks on appreciation/collectibility**, producing a ranking a knowledgeable buyer would not trust at a tasting.

---

## P0 — Factual / could mislead a purchase

### P0-1 — Rosebank Release One identity caveat is invisible in the product
- **Files:** `whisky/kb/expressions/rosebank-31-r1.json` (has `identity_note`), `whisky/index.html` (renderCards / renderFlight).
- **Datum:** node id/slug = `rosebank-31-r1`, `age_years: 30`, `display_name: "Rosebank 30 Year Old 1990 (Legacy Release One)"`, plus a paragraph-long `identity_note` explaining the 30yo-vs-31yo slug mismatch.
- **Problem:** The HTML only surfaces `vintage_conflict_note` (see line 340: `b.vintage_conflict_note ? ...`). **`identity_note` is never rendered.** The card/flight title is correct ("Release One = 30 Year Old"), but the slug `rosebank-31-r1` leaks into source-cache filenames, anchors and the flight TALK text ("Release One = the 30yo") with no warning that the *filing slug says 31*. A buyer cross-referencing the cached source files (`src_rosebank-31-r1_*`) against a 31-year-old listing can easily transpose R1 (30yo, £1,600 RRP, $3,528 top hammer) and R2 (31yo, £1,800 RRP, $2,891 top hammer). This is the single highest-risk confusion in the dossier and the prompt flags it explicitly.
- **Fix:** Render `identity_note` in the card exactly like `vintage_conflict_note` (one extra branch in `renderCards`). Better: rename the slug to `rosebank-30-r1` at the KG level so id == reality; at minimum add a ⚠︎ "Release One = 30yo; filed under legacy slug -r1" banner on the card and in the flight.

### P0-2 — Stale launch RRP / MSRP presented as "UK retail" / "US retail"
- **File:** `whisky/index.html` `priceCell()` (lines 317-320) + `_primaryGBP/_primaryUSD` in `data.json`.
- **Datum:** Rosebank R1 `_primaryGBP: 1600` is the **2020 launch RRP** (`prices.uk[0].retailer = "Original RRP (2020 launch)"`, `as_of: 2020-10`); R2 `_primaryUSD: 3300` is a **2023 MSRP** (`as_of: 2023`); Isle of Skye 25/30 `_primaryUSD` are 2023 Whisky Advocate stated prices.
- **Problem:** The card prints these under the fixed labels **"UK retail" / "US retail"** with no date. A 2020 RRP shown as today's "UK retail" on a bottle now trading at £2k+ secondary is materially misleading — it understates real acquisition cost by ~25%. The node files honestly flag "UK figure is launch RRP not a current listing"; the product hides it.
- **Fix:** Carry `as_of`/`retailer` into the primary price label, e.g. "£1,600 · RRP 2020" and "$3,300 · MSRP 2023", or visually mark non-current primaries. Do not label a launch RRP as live retail.

### P0-3 — Secondary "£-equiv" is silently FX-converted from EUR, and the number doesn't match its source
- **Files:** `data.json` `_secondaryGBP`; `index.html` price card ("secondary £-eq") + Retail-vs-secondary chart.
- **Datum:** `glengoyne-24._secondaryGBP = 250` — but the **only** auction datum for the 24 is Whiskystats **€294 EUR** (`auction.platform_data[0].avg = 294, currency EUR`). €294 × 0.85 ≈ £250. Same silent EUR→£ conversion drives Isle of Skye 21 (`€171.16 → _secondaryGBP 145`... actually shown 145/171 mismatch), IoS-25 (`€200.95 → 171`), IoS-30 (`€290 → 246`).
- **Problem:** The card column header says "secondary £-eq" but the `fx_note` only mentions the *value-for-money chart*, not the per-card secondary figure. A user reading "£250 secondary" for the Glengoyne 24 has no on-card signal it's a converted EUR lowest-offer, not a £ hammer. The meta `fx_note` ("£1≈$1.27, €1≈£0.85") is an *indicative* rate presented honestly for the chart, but it is being applied to a headline per-bottle number that reads as sourced.
- **Fix:** Either show the native currency on the card ("€294 secondary, Whiskystats") or append "(FX est.)" to every `_secondaryGBP` that was converted. Tie the per-card figure to the `fx_note` caveat, not just the chart.

### P0-4 — Robb Report "#2 / Best of the Best" claim still lives in a cached source's key_data
- **File:** `data.json` source `src_glengoyne-24_robbreport.key_data` (and the underlying cache md).
- **Datum:** `"...Best of the Best 2025 (#2 whisky of 2025)..."` — yet the verification report and the node both **retracted** this ("the prior '#2' placement could not be confirmed"; softened to unranked "10 Best Whiskeys of 2025 So Far").
- **Problem:** The retracted, unverifiable award claim is still sitting verbatim in the source manifest's `key_data` that the product links to as evidence. Anyone clicking the Robb Report source chip lands on a cache asserting a "#2" rank the team itself could not reproduce. An award/rank claim that failed verification must not survive anywhere it can be read as fact.
- **Fix:** Edit `src_glengoyne-24_robbreport.key_data` (and its cache md) to the softened wording, matching `src_glengoyne-24_robbreport_list`. (Audit only — not edited here.)

### P0-5 — US retail coverage is thin and several "US" prices are not real current US retail
- **Files:** all nodes' `prices.us`; surfaced as headline "US retail" in the card.
- **Datum:** Glengoyne 25 US = `$600` (a 2025 Whiskey Wash *stated MSRP*, `as_of 2025-08`; Total Wine price `null`). IoS-25/30 US headline = Wine-Searcher *ex-tax market average* ($186 / $302) — explicitly not a shelf price. Rosebank R1 US = a single obscure retailer (BuyMyLiquor $2,999.99). Rosebank R2 US = 2023 MSRP. Glengoyne 25 `_primaryUSD` = **600**, the MSRP, not a transactable US price.
- **Problem:** For a tool aimed (per the userEmail/US context) partly at a US buyer, the "US retail" headline is frequently an MSRP, an ex-tax average, or a lone thin listing — and the card label says "US retail" flatly. The Glengoyne 25 in particular shows **$600** as US retail while the UK price is ~£420 (~$530 incl. the guide's own FX), i.e. the US headline is the *highest, least-real* number.
- **Fix:** Distinguish "US retail" from "US MSRP" / "US market avg (ex-tax)" in the label (the data already carries the distinction in `retailer`/`as_of`). Prefer a transactable Total Wine price as `_primaryUSD` where one exists; flag MSRP/avg as such.

### P0-6 — Wide US price spreads hidden behind a single headline number
- **Files:** `data.json` `_primaryUSD`/`_primaryGBP` selection; card.
- **Datum:** Glengoyne 24 UK spread is £365 (comparison low) → £453 (Whisky Shop), a ~24% range, all collapsed to `_primaryGBP 408.95`. IoS-21 US spans $89.99 (Total Wine) → $114.99 (SRP) but headlines $89.99. Glengoyne 25 UK spans £419.90 → £525 (a 25% spread) collapsed to £419.90.
- **Problem:** Single-number display hides real, double-digit-percent spreads that matter when deciding where to buy. The card's expandable "price sources" does list them, but the headline (and the chart) pick one end with no range shown.
- **Fix:** Show a range on the card headline (e.g. "£420–£525") or a "low/typical/high" triplet, at least where the spread exceeds ~10%.

---

## P1 — Important quality / clarity

### P1-1 — Rosebank 30 (R1) ranked #1, ABOVE 31 (R2) at #2 — defensible only as a scoring artifact
- **Files:** `rosebank-31-r1.json` / `rosebank-31-r2.json` rubric; chart ordering.
- **Datum:** R1 composite **82** (`appreciation 14, collectibility 10`), R2 composite **80** (`appreciation 13, collectibility 9`). Critic scores are essentially equal (R1: WA 92 / Connosr 91; R2: WA 91 / Auctioneer 91 / Whiskybase 90.42 — R2 actually has the *deeper* score set). Both `complexity 10`, both `impact 9`.
- **Problem:** R1 wins purely on a +1 appreciation and +1 collectibility nudge — i.e. on *secondary-market* sub-scores, not on what's in the glass, where R2 has more (and arguably better-credentialed) numeric support. Presenting the 30yo as the #1 bottle of the flight is an artifact of the value half of the rubric, and it compounds the P0-1 identity confusion (the lower-ranked R2 is the one the narrative itself calls "the headline bottle"). An expert would rank these as a near-tie or put R2 nose-ahead.
- **Fix:** Either tie them or justify the split with glass-based evidence. Re-examine whether `appreciation 14` for R1 is supportable (see P1-2). Consider showing "near-tie" rather than a hard #1/#2.

### P1-2 — Appreciation sub-scores (14/15, 13/15) rest on stale 2022 hammers + aggregates, not a demonstrated trend
- **Files:** Rosebank R1/R2 `auction`, `rubric.value.appreciation`.
- **Datum:** R1 `appreciation 14` but the only individual hammer is **2022** ($3,528); "trend: rising" is asserted on a Whiskyhunter aggregate with no hammer history. R2 `appreciation 13`, freshest hammer also 2022 ($2,891), Whisky-Online row even labeled `trend: flat`.
- **Problem:** A near-max appreciation score (14/15) implies a demonstrated upward secondary trajectory. The evidence is a 4-year-old hammer plus an undated "rising" label on an aggregator. That's a thin basis for the highest value sub-scores in the entire set — and these are exactly the sub-scores that put R1 at #1.
- **Fix:** Cap appreciation where the freshest hammer is >12 months old and trend is aggregate-only; annotate the sub-score with "trend = aggregate, last hammer 2022".

### P1-3 — Glengoyne 24 critic_consensus 16 vs Glengoyne 25 critic_consensus 12 is inverted relative to evidence
- **Files:** `glengoyne-24.json` (`critic_consensus 16`), `glengoyne-25.json` (`critic_consensus 12`).
- **Datum:** The 24 has **one** normalizable score (Drinkhacker A-≈90) + an unranked list mention. The 25 has **two** numeric scores (Whiskybase 89.74 across 324 ratings, Drinkhacker A-≈90) **plus** "Best Scotch, Whiskey Wash Awards 2025." Yet the 24 scores *higher* on critic consensus (16 vs 12).
- **Problem:** The better-evidenced bottle (the 25, which is also `green` vs the 24's `amber` on `scores_ge_2`) gets the lower consensus score. The cited evidence does not support the 24 > 25 consensus gap.
- **Fix:** Re-balance: the 25's consensus should be ≥ the 24's given more and stronger scores plus a competition Best-in-class.

### P1-4 — `presentation` scoring is internally inconsistent, not just "4/8 for 40% blends"
- **Files:** all nodes `rubric.drinking.presentation`.
- **Datum:** 40% blends (IoS 25/30) = **4**; IoS-21 (also 40%) = **3**; Glengoyne 24/25 (47.8–48%, NCF, natural colour) = **7**; Rosebank (48.x%, NCF, natural colour) = **8**; Tamdhu 18 = **7**, Tamdhu 21 = **7**.
- **Problem:** "Presentation 4/8" for the 40% blends is *defensible* (chill-filtered-implied, 40%, colour unconfirmed) — but IoS-21 at **3** vs IoS-25/30 at **4** has no stated basis (all three are 40%, all three "natural_colour: N/A", all blends), and the single-malts' 7–8 partly rewards NCF/natural-colour that is **confirmed** for Glengoyne/Rosebank but only *assumed* for the blends' penalty. The axis conflates ABV, filtration, and prestige without a documented rule.
- **Fix:** Document the presentation rubric (ABV band + NCF + natural colour + packaging) and apply it uniformly; justify the IoS-21=3 vs IoS-25=4 split or equalize.

### P1-5 — Coverage GREEN/AMBER is defensible but two GREENs lean on weak "auction" points
- **Files:** `glengoyne-25.json` (green), `isle-of-skye-25.json` (green), `rosebank-31-r2.json` (green).
- **Datum:** IoS-25 `auction_point` is a **single Whiskybase lowest-offer** (€200.95), explicitly "no trend/avg/hammer." Glengoyne-25 auction is a **Whisky Returns aggregator** £250 (node itself says "not a strict-whitelist platform (reconfirm vs Whiskystats)"). Both count as a satisfied `auction_point` → GREEN.
- **Problem:** A "lowest current offer" is a retail-ask, not a secondary/auction hammer; counting it as the auction criterion inflates GREEN status. The nodes flag the weakness honestly in `gaps`, but the green dot in the matrix doesn't.
- **Fix:** Tighten `auction_point` to require an actual hammer or a whitelisted aggregate; otherwise mark the criterion amber with a footnote.

### P1-6 — Tamdhu 21 ranked #3 overall on zero numeric scores
- **Files:** `tamdhu-21.json` (`_rank 3`, composite 69, all `scores[].normalized_100 = null`).
- **Datum:** No numeric /100 anywhere (Robb Report band only *implied* 85–89; awards are non-numeric). `critic_consensus 14`. Coverage is `amber` (`scores_ge_2: false`).
- **Problem:** A bottle with **no** confirmed numeric critic score outranks the green, multiply-scored Isle of Skye 25 (#4) and both Glengoynes. `critic_consensus 14` is generous for "no numeric score, one implied band + two trade-show medals." Defensible as a value play, but as a *consensus/quality* rank it overshoots its evidence.
- **Fix:** Lower `critic_consensus` to reflect the absence of numeric scores, or annotate that the rank is value-driven; don't let an unscored bottle sit at #3 on quality-weighted composite.

### P1-7 — Auction chart and Retail-vs-secondary chart mix currencies on a log axis
- **File:** `index.html` `drawCharts()` (lines 245-251) + `auctionCell` table.
- **Datum:** "Retail £-equiv" vs "Secondary £-equiv" bars on a **logarithmic** y-axis; the secondary series is FX-converted from EUR/USD/GBP (per P0-3). The auction *table* per card correctly shows native `currency`, but the chart flattens everything to £-equiv.
- **Problem:** (a) Log axis on a paired retail-vs-secondary bar chart makes the gap between RRP and secondary visually compressed and easy to misread (Rosebank's £1,600 RRP vs ~£3,000 secondary looks modest on a log scale). (b) The £-equiv secondary mixes a EUR lowest-offer, a GBP aggregate, and a USD hammer as if comparable. Honest FX note exists but the visual still invites apples-to-oranges reads.
- **Fix:** Either use a linear axis for the retail-vs-secondary comparison, or label the axis "£-equiv (FX-est., mixed-source)" and add the per-bar source currency to the tooltip.

### P1-8 — Glengoyne 24 quarantined TWE price still appears as a captured source with the stale £415 in key_data
- **Files:** `data.json` source `src_glengoyne-24_thewhiskyexchange.key_data` ("TWE £415.00 ... Whisky Shop £453.00").
- **Datum:** Node quarantined TWE to "N/A — unverified" (live £375), but the source `key_data` still leads with "TWE £415.00." Three UK price rows (HTFW, Whisky Shop) all cite this **same** `source_id` `src_glengoyne-24_thewhiskyexchange`, while a dedicated `src_glengoyne-24_royalmilewhiskies` source exists but is **unused** by any price row.
- **Problem:** (a) Stale £415 persists in evidence text. (b) Multiple distinct retailers share one source_id — clicking "Whisky Shop £453" link sends you to the TWE capture, a provenance smell. (c) A captured source is dead (unreferenced).
- **Fix:** Update the key_data to the current £375; give HTFW/Whisky Shop their own source captures (or relabel the shared capture as a multi-retailer roundup); either wire in or drop the unused Royal Mile source.

### P1-9 — Blend cask/colour/filtration unknowns penalize the blends without being shown to the user
- **Files:** IoS-21/25/30 `natural_colour: "N/A — not found"`, `chill_filtered: "N/A — not found"`.
- **Datum:** All three blends carry unknown colour/filtration; the rubric `presentation` penalizes them (3–4), but the card vitals show ABV/age/category, not the "colour/filtration unconfirmed" status that drove the penalty.
- **Problem:** The user sees a low presentation score with no visible reason; the honest "we don't know if it's coloured/chill-filtered" caveat is buried in `coverage.gaps`.
- **Fix:** Surface natural-colour/NCF status (incl. "unconfirmed") in the card vitals so the presentation score is legible.

---

## P2 — Nice-to-have

### P2-1 — `meta.source_count: 89` vs `data.json` sources array
- **File:** `data.json` `meta.source_count`. The footnote advertises 89 sources but the actual `sources[]` length should be displayed from the array (`#srccount` already does `${DATA.sources.length} captured`). Confirm 89 matches the array length; if not, reconcile so the pill and the "(N captured)" never disagree.

### P2-2 — `fetch_note` overclaims "every datum links to its source" while WebFetch was blocked
- **File:** `data.json` `meta.fetch_note`. All captures are `websearch_excerpt` (WebFetch 403). "Every datum links to its source" is true for *links*, but the methodological caveat (reproduction-by-search, not verbatim page fetch) deserves a one-line mention in the product footnote, not only in the verification report.

### P2-3 — Glengoyne 25 "oloroso" left unconfirmed but house_style/distillery prose leans oloroso
- **Files:** `glengoyne-25.json` cask ("oloroso designation UNCONFIRMED"), distillery `tamdhu` prose (oloroso) — fine. Just ensure the card cask line shows the "oloroso unconfirmed" hedge rather than implying oloroso.

### P2-4 — Tamdhu founded-year (1897) flagged as not WebFetch-verified
- **File:** `distilleries.tamdhu.notes`. Honest, but the distillery card (if it shows "founded 1897") should carry the same "general knowledge, unverified" hedge the node does.

### P2-5 — Isle of Skye 30 IWSC/SFWSC Gold years undated
- **File:** `isle-of-skye-30.json` `scores[1].raw` ("IWSC Spirit Gold; SFWSC Gold ... undated"). Medal claims without a year are weak evidence at a tasting; either date them or down-weight their visual prominence.

### P2-6 — `tasting_order` vs composite `_rank` are different orderings, lightly explained
- **Files:** `data.json` `tasting_order` (lightest→heaviest, Rosebanks last) vs `_rank` (Rosebank R1 #1). The flight rationale notes the tension, but a first-time user may read the #1-ranked bottle being poured *last* as an error. A one-line "flight order ≠ ranking" note on the flight header would help.

---

## Cross-cutting note for the builder
The KG nodes are, on the whole, *more honest than the rendered product*: quarantines, RRP-vs-live distinctions, EUR provenance, and the Rosebank identity caveat all exist in the JSON but are **dropped, relabeled, or FX-flattened** on the way into `index.html`. The cheapest high-value fixes are all in the render layer: render `identity_note`, date the primary prices, mark FX-converted secondaries, and stop labeling MSRP/RRP/ex-tax-average as flat "retail."
