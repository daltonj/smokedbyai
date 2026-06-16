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
