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
