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
