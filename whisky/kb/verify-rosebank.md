# Source Verification Report — Rosebank cluster (adversarial)

Verifier: Source Verifier (adversarial fact-checker), Rosebank cluster.
Date: 2026-06-16. Anchor: 2026-06-16 02:49 UTC.
Method: WebFetch blocked (403) environment-wide. Every cited capture re-read; every datapoint re-confirmed against the cited capture AND independently reproduced via targeted WebSearch (allowed_domains on the cited source where possible). Reproduction-by-search is the verification standard for `method: websearch` captures.

Bottles:
- `rosebank-31-r1` = Legacy Release One = a **30 Year Old** 1990 (bottled 2020), **48.6%** ABV. (Slug quirk — see below.)
- `rosebank-31-r2` = Legacy Release Two = the genuine **31 Year Old** (bottled 2022), **48.1%** ABV.

---

## rosebank-31-r1 — VERDICT: FAIL (verification.status = failed)

Summary: 15 verified / 0 mismatch / **1 unsupported**. `pass = false`.

Core vitals, score, RRP, and the Whiskyhunter aggregate all VERIFY and reproduce live:
- ABV 48.6%, 30yo, cask 62% refill sherry / 38% refill bourbon, outturn 4,350 (some sources 4,300 — conflict preserved): all verified vs `src_rosebank-31-r1_retail`.
- Whisky Advocate **92** (Jonny McCormick, Winter 2021): verified, reproduced live on whiskyadvocate.com.
- RRP **£1,600** (2020 launch, Spirits Business): verified, reproduced live (GBP correct).
- Whiskyhunter aggregate **GBP** min £1,999 / avg £2,999.60 (node rounds to 3,000 — faithful) / max £3,500: verified, reproduced live on whiskyhunter.net.

**THE CATCH — unsupported USD hammer / citation defect.**
The second auction entry — "Whisky Auctioneer (historical hammer)", **USD $3,528**, 2022-01-10 — is attributed in the node to `source_id: src_rosebank-31-r1_whiskyhunter`. That capture **explicitly states** "Latest individual hammer / explicit trend direction: **N/A — not surfaced via search**." The figure is real (it reproduces via independent WebSearch: "$3,528 ... sold on January 10, 2022 at Whisky Auctioneer"), **but it is not present in its cited source and no Whisky Auctioneer capture exists in the KG for R1.** Per procedure (datum must literally appear in its cited capture), this is **unsupported**.
- Action: `latest_hammer` set to `"N/A — unverified"`, added to `gaps[]`, `verification.status = failed`. Fix = add a real Whisky Auctioneer capture for R1, then re-verify.
- Note: it is NOT cross-contamination from R2 — R2's hammer is the distinct $2,891 (Whisky-Online, 2022-09-14). The two USD hammers stay correctly separated.

**Identity quirk — correctly flagged, NOT a data error.** Node is filed under slug `rosebank-31-r1` but documents the **30 Year Old** Release One. The node's `identity_note` states this plainly and every R1 capture carries a "NOTE ON IDENTITY" header. Verified as a flagged quirk, not a mislabel.

---

## rosebank-31-r2 — VERDICT: PASS (verification.status = passed)

Summary: 17 verified / 0 mismatch / 0 unsupported. `pass = true`.

Every core field verifies vs its cited capture AND reproduces live:
- 31yo, ABV **48.1%**, outturn **4,000**, bottled 2022: verified.
- Whisky Auctioneer **91**: verified ("The 31 year old Release #2 earned 91 points").
- Whiskybase **90.42** (ID 215536): verified, reproduced live (~114 ratings).
- US MSRP **$3,300** (Paste): verified, reproduced live (USD correct).
- Whiskystats whisky value **€1,548** (EUR): verified, reproduced live (whiskystats.com/whisky/215536 is a real page; EUR correctly carried).
- Whiskyhunter aggregate **GBP** min £1,750 / avg £2,049 / max £2,500: verified, reproduced live (GBP correct).
- Whisky-Online hammer **$2,891** (USD, 2022-09-14): verified, reproduced live; labeled historical, not presented as current.
- Trend **rising**: verified at distillery level (Whiskystats Feb 2026, Rosebank index 191.66 / +5.71%).
- Tasting (champagne gold; banana cake/cherry blossom/lavender; dried-grass chamomile/wild strawberry/toasted marshmallow; champagne+oak+medicinal finish) and the Words-of-Whisky verdict "an ideal of what traditional Lowland whisky is": all verified verbatim.

**1990-vs-1991 vintage conflict — correctly preserved.** Whiskyhunter / Whisky Auctioneer hub say distilled **1990**; Whisky Auctioneer product 1280618 is titled "Rosebank **1991** 31 Year Old Release #2" and Whiskybase carries alt slug `rosebank-1991`. Both reproduce live. The node leaves it **unresolved** in `vintage_conflict_note` + `gaps[]` — exactly as required. Age (31yo) and 2022 bottling are consistent across sources.

---

## Cross-contamination audit (R1 vs R2) — CLEAN

The single biggest risk was a figure crossing between the two releases. None found. Each datapoint stays correctly scoped:

| Datapoint | R1 (30yo) | R2 (31yo) |
|---|---|---|
| Age / ABV | 30yo / 48.6% | 31yo / 48.1% |
| Critic score | WA **92** (McCormick) | WA **91** / Whiskybase 90.42 |
| RRP / MSRP | **£1,600** RRP (GBP) | **$3,300** MSRP (USD) |
| Whiskyhunter aggregate (GBP) | £1,999 / 2,999.60 / 3,500 | £1,750 / 2,049 / 2,500 |
| Market value | (none surfaced) | Whiskystats **€1,548** (EUR) |
| USD hammer | $3,528 (2022-01-10) [unsupported by cite] | $2,891 (2022-09-14) |

Currencies (£ vs $ vs €) each carry correctly on both nodes. Stale 2022 hammers are flagged as historical on both (not presented as current). Only defect is the R1 USD-hammer citation (above).

---

## Final tally
- rosebank-31-r1: **FAIL** — 15 verified / 0 mismatch / 1 unsupported.
- rosebank-31-r2: **PASS** — 17 verified / 0 mismatch / 0 unsupported.
- Most important catch: R1's $3,528 USD auction hammer is **unsupported by its cited capture** (cite says hammer N/A; figure has no Whisky Auctioneer capture in the KG) — quarantined to "N/A — unverified". No actual R1/R2 cross-contamination; vintage conflict and slug quirk both correctly preserved/flagged.
