# Whisky KG — Verification Report

_Regenerated 2026-06-16T22:26:08Z. Research anchor 2026-06-16._

All 9 bottles PASS adversarial verification (core fields reproduce from cited sources).

**Round 3 addendum:** Wide US retail prices and official Ian Macleod RRPs were added after the
verifier round. Each new US price was reproduced by a second independent search at capture time
(our reproduce-by-search standard), but was not re-run through a separate adversarial verifier pass.
Rubric scores were rebalanced per the expert audit (see kb/expert-audit.md); two GREENs were
demoted to AMBER after tightening `auction_point` to require a real hammer or whitelisted aggregate.


---

# Source Verification — Isle of Skye cluster (RE-VERIFICATION)

**Verifier:** adversarial Source Verifier stage
**Verified at:** 2026-06-16T21:55:00Z
**Bottles:** isle-of-skye-21, isle-of-skye-25, isle-of-skye-30
**Trigger:** re-verification after a gap-fill that added new scores/reviews/auction captures.
**Method:** Every present datapoint (abv, each score incl. the new ones, each uk/us price, each auction figure, headline tasting/award claims) checked (1) for literal appearance in its cited capture and (2) re-confirmed via targeted WebSearch with `allowed_domains` on the cited source. WebFetch is blocked (HTTP 403); reproduction-by-search is the standard. Special adversarial focus on the new datapoints and on wrong-expression numbers — especially the IoS-25 "97".

## What was NEW since last verify (all re-checked)
- **IoS-21:** Tastings.com/BTI **90** + Whisky Magazine **8.6/86** + a **dedicated 21YO whiskybase** capture (was previously borrowing the 25YO capture).
- **IoS-25:** Wine Enthusiast **97** (Kara Newman) + The Whiskey Reviewer review.
- **IoS-30:** The Whiskey Reviewer **A-** + Drinkhacker lineup review.

## Verdict summary

| Bottle | verified | mismatch | unsupported | pass |
|--------|----------|----------|-------------|------|
| isle-of-skye-21 | 9 | 0 | 1 | **PASS** |
| isle-of-skye-25 | 9 | 0 | 0 | **PASS** |
| isle-of-skye-30 | 10 | 0 | 0 | **PASS** |

All three nodes: `verification.status = passed`. No CORE field had to be quarantined.

## Most important catch — IoS-25 "97" is the 25YO, NOT a 21YO mix-up (CLEARED)
The headline adversarial risk this pass was the newly added **Wine Enthusiast 97** on the 25YO. Wine Enthusiast publishes a SEPARATE Isle of Skye **21**-year-old page rated **96** — a classic wrong-expression trap. Result: **clean.**
- The **97** sits on the dedicated 25YO page (`wineenthusiast.com/buying-guide/isle-of-skye-25-years-old/`) with 25YO-specific notes (caramel, cocoa, fresh-roasted coffee, orange marmalade, crushed hazelnut), reproduced live via two searches.
- The **96** is a distinct 21YO page and is **not** ingested anywhere in the KG. No transposition, no off-by-one between adjacent expressions.

## One unsupported sub-claim downgraded — IoS-21 Tastings "Gold"
The IoS-21 Tastings.com score was recorded as **"90/100 (BTI Gold)"**. The **90 numeric reproduces** cleanly on tastings.com; the accompanying **"Gold" medal tier does NOT** — the live re-search explicitly returned no gold-medal designation, and the capture itself flags an SFWSC-body-vs-BTI-tier ambiguity. Action taken:
- `scores[1].raw` softened to "90/100, dated 9/27/2023 ('Gold' tier N/A — unverified)".
- Logged in IoS-21 `gaps[]`; recorded as `unsupported` in the verify record.
- **Non-core**, so it does not fail the bottle: the 90 numeric score stands and the bottle still has ≥2 numeric scores (90 + 86).

## Resolved since last pass — IoS-21 auction provenance
Last verify flagged that the 21YO auction point €171.16 was cited to the 25YO's whiskybase capture (cross-reference only). The gap-fill added a **dedicated `src_isle-of-skye-21_whiskybase`** pointing at the correct page (`whisky/63435`). Value re-confirmed (€171.16, EUR, 21YO). **Provenance defect closed.**

## Other cross-bottle checks run
- **Wrong-bottle transposition (WWA 2026):** Isle of Skye won BOTH a **Gold** (30YO) and a **Silver** (Cigar Reserve, a different expression) at WWA 2026. The 30YO node claims only the Gold. Clean.
- **IoS-25 WA 94** reproduces and is correctly tied to the 25YO; **IoS-30 / IoS-21 WA point scores** genuinely never surfaced and are honestly recorded null (no fabrication).
- **Currency discipline:** all £/$/€ figures correct and correctly labelled; Wine-Searcher figures labelled "US market avg (ex-tax)"; WA $210/$330 tagged `as_of: 2023-fall` (stale, not fresh).
- **Auction figures (€200.95 / €290.00):** reproduced against the correct 25YO/30YO whiskybase pages; detailed history member-gated (honestly flagged).

## Coverage caveats (insufficiency — NOT verification failures)
- **IoS-25:** now has THREE+ review captures and TWO numeric scores (WA 94, WE 97) plus the SFWSC double award → meets all six coverage criteria; with `verification.pass` holding it is **eligible for GREEN**.
- **IoS-30:** `scores_ge_2` STILL FALSE — no second NUMERIC normalized_100 exists. WWA/IWSC/SFWSC are medals; Whiskey Reviewer (A-) and Drinkhacker are letter grades. Truthful but not GREEN on the numeric-scores criterion. IWSC/SFWSC Gold year still undated; SRP ~$322 not verbatim (avg $302 captured).
- **All three:** natural-colour / chill-filtration unconfirmed; all captures are WebSearch excerpts (WebFetch blocked 403).

---

# Glengoyne Cluster — Source Verification (RE-VERIFY after gap-fill)

- **Verifier:** Source Verifier (adversarial), re-verification pass
- **Date:** 2026-06-16T22:15Z
- **Environment:** WebFetch BLOCKED (HTTP 403) on all URLs. Reproduction-by-WebSearch (allowed_domains on the cited source) is the verification standard.
- **Bottles:** glengoyne-24 (White Oak, bourbon/virgin oak), glengoyne-25 (Sherry Oak)

---

## glengoyne-24 (White Oak, 47.8%) — PASS (1 quarantine)

Counts: **11 verified, 1 mismatch, 0 unsupported.**

### Verified (live reproduction)
- ABV 47.8% and cask = American first-fill bourbon + virgin/new oak (sherry-distinct). Robb Report confirms "first-fill bourbon and new oak ... a small amount that spent time in virgin oak".
- Non-chill-filtered ("free from chill filtration", The Whisky Shop live page).
- Drinkhacker **A- (~90)** — white chocolate, grapefruit pith, "just now cresting into over-maturity" all reproduce.
- **Robb Report claim — SOFTENED wording CONFIRMED.** Live searches surface only inclusion in "The 10 Best Whiskeys of 2025 So Far" (published 2025-07-31); they do **not** surface any "#2" numbered ranking. The node's unranked-list wording is exactly what reproduces. The prior "#2 / Best of the Best 2025" claim does not reproduce.
- UK: HTFW £408.95; **The Whisky Shop £453.00 (live-confirmed)**.
- US: Total Wine $399.98 (700ml, live); Whisky Advocate stated $400.
- Auction: Whiskystats **€294 EUR** (whisky/253591) — correctly EUR, not mixed with GBP retail or the 25's £250.
- Tasting profile = citrus/vanilla/white-chocolate; no sherry crossover with the 25.

### MISMATCH → QUARANTINED
- **The Whisky Exchange £415 (primary UK quote).** Live re-verification of TWE p/81117 now returns **£375** (comparison-site low £365), not £415. The cached excerpt's £415 is stale/superseded and no longer reproduces; `as_of=2026-06-16` is contradicted. Set to `"N/A — unverified"` in the node with an explanatory note; added to `gaps`.
- **Impact on coverage:** none — the `uk_price` criterion is preserved by The Whisky Shop £453 (live-confirmed) and HTFW £408.95.

**Verdict:** `pass=true`. All core fields verify; the single stale retail quote is quarantined and does not gate pass.

---

## glengoyne-25 (Sherry Oak, 48%) — PASS

Counts: **14 verified, 0 mismatch, 0 unsupported.** All NEW gap-fill datapoints reproduce LIVE.

### Verified (live reproduction)
- ABV 48%, cask = exclusively hand-selected sherry oak (Whiskybase: "European Oak Sherry casks, mainly 1st Fill"). Natural colour, non-chill-filtered.
- **NEW UK prices — all three reproduce on their cited domains:**
  - Master of Malt **£419.90** (48% ABV, 33 reviews) — live.
  - Glengoyne official shop **£499.00** (70cl) — live.
  - Royal Mile Whiskies **£525.00** (in stock, 70cl 48%) — live.
- **NEW Whiskybase community score 89.74/100 (324 ratings)** (whisky/167031) — reproduces verbatim.
- **NEW Drinkhacker A- (~90)** — sherry-cask review (2024-03-10), profile reproduces on drinkhacker.com.
- **NEW WhiskyNotes (Ruben Luyten)** review reproduces (first-fill European oak, figs/cherries/plums/blackberries); its /100 not exposed, correctly recorded N/A. Gives the 3rd named review.
- Whiskey Wash "Best Scotch, Awards 2025" — reproduces; corroborated by Master of Malt blog.
- US: Whiskey Wash stated MSRP **$600** (USD, correctly labeled); Total Wine listing exists, price null (no fabrication).
- Auction: Whisky Returns avg **£250 GBP** (as of 2026-01-28) — reproduces verbatim; GBP, correctly attributed to Whisky Returns.

### Adversarial checks
- **No 24-vs-25 conflation:** the 25 is unambiguously Sherry Oak (dried fruit/chocolate), kept distinct from the 24's citrus/vanilla White Oak.
- **No currency mix-ups:** GBP retail £419.90 / £499 / £525, USD MSRP $600, GBP secondary £250 — each correctly labeled. The €294 EUR auction figure belongs to the **24** and did NOT bleed into the 25.
- Oloroso designation correctly left UNCONFIRMED for the standard 25.

**Verdict:** `pass=true`. All 14 fields verify against live reproduction.

---

## Most important catch
**glengoyne-24 The Whisky Exchange £415 is now stale** — the live TWE page (p/81117) returns £375 (comparison low £365). Quarantined to "N/A — unverified"; the UK-price criterion survives via the live-confirmed The Whisky Shop £453. Separately, the **softened Robb Report wording is confirmed correct**: only the unranked "10 Best Whiskeys of 2025 So Far" inclusion reproduces — no "#2" rank.

---

# Tamdhu cluster — Source Verification report (RE-VERIFICATION)

- Verifier: adversarial source verifier (re-run after gap-fill)
- Date: 2026-06-16 (anchor 2026-06-16 02:49 UTC)
- Environment: **WebFetch BLOCKED (HTTP 403) entire run.** Reproduction-by-**WebSearch** is the verification standard (per whisky-verify SKILL.md step 2; all captures are `capture_method: websearch_excerpt`).
- Bottles: `tamdhu-18`, `tamdhu-21`

## Result summary

| Bottle | Prior | Now | Verified | Mismatch | Unsupported |
|---|---|---|---|---|---|
| tamdhu-18 | pass | **PASS** | 10 (+1 stale) | 0 | 0 |
| tamdhu-21 | **FAIL** | **PASS** | 12 | 0 | 0 |

Both bottles PASS on truthfulness. Both remain **AMBER** on coverage-sufficiency only (not a verification failure) — see gaps.

---

## tamdhu-18 — PASS (re-confirmed)

Re-verification of the two gap-fill additions plus all prior fields. Every present core field reproduces via independent WebSearch.

- **abv 46.8 / cask (oloroso, EU+US oak, Jerez) / natural colour / un-chill-filtered** — verified (Whiskey Wash).
- **Whiskybase 87.20/100** — verified vs capture. Live reproduction now reads 87.53/100 (550 votes); community ratings drift, node value matches the cited capture and is within rounding of normalized 87. No mismatch.
- **WhiskyNotes / Ruben Luyten 88/100 (NEW)** — verified; reproduced live. Source page is a 2023 (stale) review — valid score datapoint, not a fresh review.
- **SFWSC Double Gold** — verified (non-numeric).
- **The Whisky Exchange £176 (NEW UK price)** — verified; reproduced on p/65584 (70cl / 46.8%). A stray £175 search mention was seen but £176 dominates and matches the capture.
- **Total Wine $199.99 (US)** — verified; currency USD correct.
- **Auction ~£90–£100 (2024)** — verified-but-**stale**; correctly labeled, not presented as fresh. Correct 46.8% standard 18 (whisky.auction lot 137270), not a Cask Strength edition.
- **Nose/palate** — verified; **finish** honestly carried as N/A (no critic finish text in captures).

**scores_ge_2 and uk_price now satisfied.** Gaps (coverage only): reviews_ge_3 still fails (1 fresh review; WhiskyNotes stale); fresh auction missing; finish note missing.

---

## tamdhu-21 — PASS (prior FAIL cleared)

The prior run FAILED on the UK price (TWE £299 mismatch + Master of Malt £252.70 unsupported). Both are now RE-SOURCED and reproduce live.

- **TWE £295 (re-sourced)** — verified on p/84852 (70cl / 47.5%, £421.43/litre). **Critical £295-vs-£299 distinction held:** £295 is the LIVE TWE retail price; £299 is the official RRP (The Spirits Business; Royal Mile Whiskies separately lists £299). The node carries the live £295 and does NOT assert £299 as the live price — the price note disambiguates correctly. PRIOR MISMATCH CLEARED.
- **Master of Malt £252.70 (re-sourced)** — verified; reproduces across two independent searches against masterofmalt.com. PRIOR UNSUPPORTED CLEARED.
- **Total Wine $399.99 (US)** — verified; currency USD correct, not conflated with GBP figures.
- **abv 47.5 / cask (first-fill+refill EU+US oak oloroso, European dominant, Jerez) / 12,000 bottles / Aug 2025** — verified.
- **Robb Report (Jonah Flicker) Macallan value framing** — verified; node correctly sets normalized_100=null (no fabricated /100).
- **Spirit of Speyside 2026 Overall Winner + Gold (18&over)** — verified (sltn.co.uk, whiskyexperts.net).
- **Scottish Field Whisky Challenge 2025 Whisky of the Year** — verified (non-numeric).
- **Auction = empty** — verified. The only Tamdhu 21 auction lots (Whisky Hammer 208616, Grand Whisky Auction, Whisky Shop Auctions) are an OLDER **55.3% Cask Strength Limited Edition, 250 bottles** — a different bottle. Node correctly asserts NO core-bottle auction point.
- **Nose/palate/finish** — verified (official + WhiskyNotes/Whiskey Wash/Whisky For Everyone).

**Gaps (coverage only):** scores_ge_2 still fails (no numeric /100 sourced; Robb Report band only implied); auction_point absent by design (core 21 too new).

---

## Adversarial findings (most important catches)

1. **tamdhu-21 UK price now reproduces — the prior FAIL clears.** The £295-vs-£299-RRP trap was specifically hunted: the node carries the **live £295** with a note that **£299 is the RRP**, not the selling price. Both halves reproduce. This is the headline result.
2. **No 18-vs-21 conflation and no false auction.** tamdhu-21's only auction lots are the older 55.3% Cask Strength edition (250 bottles); the node correctly keeps `platform_data: []`. tamdhu-18's auction is the correct 46.8% standard bottle.
3. **No currency mix-ups.** $399.99 (US) vs £295 / £252.70 (UK) all correct.
4. Minor, non-blocking: tamdhu-18 Whiskybase live rating has drifted to 87.53 (from 87.20 in capture); WhiskyNotes 88/100 comes from a 2023 (stale) page — valid as a score, flagged as not a fresh review.

Both verify.json records overwritten; both node `verification` blocks set to **passed**.

---

# Rosebank Cluster — Source Verification Report (RE-VERIFICATION after gap-fill)

**Verifier:** adversarial Source Verifier
**Date:** 2026-06-16
**Environment:** WebFetch BLOCKED (HTTP 403 environment-wide). Reproduction-by-WebSearch is the verification standard (per SKILL §2, `method: websearch` captures).
**Bottles:** `rosebank-31-r1` (Legacy Release One = 30 Year Old 1990, 48.6%), `rosebank-31-r2` (Legacy Release Two = 31 Year Old, 48.1%)

---

## Headline result

| Bottle | Prior | Now | Verified | Mismatch | Unsupported |
|---|---|---|---|---|---|
| rosebank-31-r1 (30yo Release One) | FAIL (1 unsupported) | **PASS** | 17 | 0 | 0 |
| rosebank-31-r2 (31yo Release Two) | PASS | **PASS** | 18 | 0 | 0 |

**Most important catch — the R1 $3,528 hammer CLEARED.** In the prior pass it was `unsupported`: the figure was attributed to `src_rosebank-31-r1_whiskyhunter`, whose capture explicitly says "Latest individual hammer … N/A — not surfaced." A dedicated capture `src_rosebank-31-r1_whiskyauctioneer` now exists, the node's `auction.platform_data[1].source_id` points to it, and the figure appears verbatim there. It reproduces live across multiple independent WebSearch queries, attributed **specifically to the 30 Year Old Release No. 1, sold January 10, 2022 at Whisky Auctioneer** — and an adversarial probe confirmed it is **NOT** the 31yo Release Two (whose top documented hammer is $2,891). Citation defect repaired; datum verified.

---

## rosebank-31-r1 — Legacy Release One (30 Year Old 1990, 48.6%) — PASS

Identity quirk **preserved, not a data error**: the node is filed under the orchestrator slug `rosebank-31-r1` but documents a **30 Year Old** (1990 vintage, bottled 2020, 48.6% ABV). `identity_note` and every R1 capture's "NOTE ON IDENTITY" header flag this; live search corroborates (Whisky Advocate, Spirits Business, BuyMyLiquor all label it 30yo Release One).

All 17 core/supporting fields verified against cited captures **and** reproduced live:

- **Vitals** — 30yo, 48.6% ABV, 62% refill sherry / 38% refill bourbon, 4,350 bottles (4,300 conflict preserved), distilled 1990 / bottled 2020. ✔
- **Scores (now ≥2)** — Whisky Advocate / Jonny McCormick **92** (Winter 2021); Connosr / markjedi1 **91**. Both reproduce live. ✔
- **UK price** — RRP **£1,600** (2020 launch). Reproduced live ("priced at £1,600 … directly from Rosebank's website"). ✔
- **US price (new)** — BuyMyLiquor **$2,999.99**. Reproduced live. ✔
- **Auction** — Whiskyhunter GBP min £1,999 / avg £2,999.60 (node rounds 3000) / max £3,500. ✔
- **Auction (RESTORED & VERIFIED)** — Whisky Auctioneer USD **$3,528** hammer, 2022-01-10, now correctly cited and reproduced. Carried as a historical 2022 hammer, not current value. ✔
- **Tasting** — buttery/golden vanilla, lemon meringue, honeycomb, marzipan; creamy fruity palate; pear+vanilla finish; Connosr "the nose is just out of this world." ✔

**Coverage:** AMBER (reviews_ge_3 still not met — 2 numeric scores; tasting from 3 expert sources, all 2020-2021 stale). All PRESENT core fields verify → `verification.pass = true`, `status = passed`.

**Remaining gaps (non-blocking for verification):** third numeric score (Words of Whisky) not surfaced; UK figure is launch RRP not a current listing; no Release-One-specific Whiskystats EUR value; freshest individual hammer is 2022.

---

## rosebank-31-r2 — Legacy Release Two (31 Year Old, 48.1%) — PASS

All 18 fields verified against cited captures and reproduced live.

- **Vitals** — 31yo, 48.1% ABV, 4,000 bottles, bottled 2022. ✔
- **Vintage conflict (1990 vs 1991) — PRESERVED & STILL UNRESOLVED.** Live search confirms the conflict is alive: Whiskyhunter / Whisky Auctioneer hub say "distilled 1990"; Master of Malt live result, product listing 1280618 ("Rosebank 1991 31 Year Old Release #2") and Whiskybase alt-slug "rosebank-1991" say 1991. The node carries `vintage_conflict_note` and does **not** silently resolve it. ✔ Correct.
- **Scores (≥3)** — Whisky Auctioneer **91**, Whiskybase **90.42** (→90), Whisky Advocate / McCormick **91** (new). All reproduce live. The two 91s are independently sourced (auction house vs professional critic). ✔
- **UK price (new)** — Master of Malt / House of Bruar **£1,800** (70cl). Reproduced live. Distinct from R1's £1,600. ✔
- **US price** — MSRP **$3,300** (Paste; corroborated Whiskey Wash $3,299-3,300, Whisky Advocate $3,300). ✔
- **Auction** — Whiskystats **€1,548** (EUR); Whiskyhunter GBP £1,750 / £2,049 / £2,500; Whisky-Online USD **$2,891** hammer (2022-09-14, historical). All reproduce; currencies each carry correctly. ✔
- **Tasting** — champagne gold; banana cake, cherry blossom, lavender, virgin oak; dried-grass chamomile, wild strawberry, lemon, toasted marshmallow, cocoa; bubbly champagne/oak/medicinal finish; Words of Whisky "an ideal of what traditional Lowland whisky is." ✔

**Coverage:** AMBER (UK price now present; RRP-vs-listing nuance noted). `verification.pass = true`, `status = passed`.

**Remaining gaps (non-blocking):** exact cask split for R2 not found; vintage unresolved (intentional); freshest individual hammer is 2022.

---

## Adversarial contamination sweep — CLEAN

Cross-checked the exact contamination vectors flagged in the task. No R1↔R2 bleed:

| Attribute | R1 (30yo Release One) | R2 (31yo Release Two) | Verdict |
|---|---|---|---|
| Age | 30yo | 31yo | distinct ✔ |
| UK RRP/price | £1,600 | £1,800 | distinct ✔ |
| US price | $2,999.99 retail | $3,300 MSRP | distinct ✔ |
| Whisky Advocate score | 92 | 91 | distinct ✔ |
| Other score | Connosr 91 | Auctioneer 91 / Whiskybase 90.42 | distinct ✔ |
| Top auction hammer | $3,528 (Whisky Auctioneer, 2022-01-10) | $2,891 (Whisky-Online, 2022-09-14) | distinct ✔ |
| Currencies | GBP/USD | EUR/GBP/USD | each carries correctly ✔ |

- The **$3,528** hammer is firmly the **30yo R1** (probe "Release Two highest hammer $3,528" returned only the R1 attribution). No mis-binding to the 31yo.
- The two coincident **91** scores on R2 are independently sourced (Whisky Auctioneer vs Whisky Advocate/McCormick), not a duplicated figure.
- **1990-vs-1991** vintage conflict on R2 remains preserved/unresolved, as required.
- No currency mix-ups: € (Whiskystats), £ (retail/Whiskyhunter), $ (US retail / auction hammers) all carried correctly.

---

## Outcome

- `rosebank-31-r1`: **PASS** (17 verified / 0 mismatch / 0 unsupported). `verification.status = passed`. The restored $3,528 hammer cleared.
- `rosebank-31-r2`: **PASS** (18 verified / 0 mismatch / 0 unsupported). `verification.status = passed`.

Both nodes are verification-clean. Neither reaches GREEN purely on coverage (R1 reviews_ge_3 unmet; UK-price-as-RRP / freshness nuances) — but no field is unsupported or mismatched, so verification no longer blocks them.
