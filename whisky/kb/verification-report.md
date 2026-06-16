# Whisky KG — Verification Report

_Adversarial source verification (reproduce-by-search). Generated 2026-06-16T21:00:00Z. Research anchor 2026-06-16._

Pass = every PRESENT core datapoint reproduces from its cited source. Fail = at least one field quarantined to `N/A — unverified` (a sourcing/provenance defect — note: no fabricated *values* were found).


---

# Source Verification — Isle of Skye cluster

**Verifier:** adversarial Source Verifier stage
**Verified at:** 2026-06-16T04:15:00Z
**Bottles:** isle-of-skye-21, isle-of-skye-25, isle-of-skye-30
**Method:** Every present datapoint (abv, each score, each uk/us price, each auction figure, headline tasting/award claims) checked (1) for literal appearance in its cited capture and (2) re-confirmed via targeted WebSearch with `allowed_domains` on the cited source. WebFetch is blocked (HTTP 403) in this environment, so reproduction-by-search is the verification standard. Pass = all PRESENT core fields (abv, scores present, both market prices, auction point) verify with zero mismatch/unsupported.

## Verdict summary

| Bottle | verified | mismatch | unsupported | pass |
|--------|----------|----------|-------------|------|
| isle-of-skye-21 | 6 | 0 | 0 | **PASS** |
| isle-of-skye-25 | 7 | 0 | 0 | **PASS** |
| isle-of-skye-30 | 8 | 0 | 0 | **PASS** |

All three nodes: `verification.status = passed`. No field had to be quarantined to `N/A — unverified`.

## Hallucinations / fabrications caught
**None.** No invented numbers, no wrong-expression numeric attributions, no currency mix-ups (£/$/€ all correct and correctly labelled), no averaged ranges passed off as single retail facts, and no stale figure presented as fresh. Wine-Searcher averages are honestly labelled "US market avg (ex-tax)"; the Whisky Advocate $210/$330 prices are tagged `as_of: 2023-fall` (stale, not fresh).

## Most important finding — the researcher-flagged 21YO auction figure (PROVENANCE, not a lie)
The IoS-21 auction point €171.16 is **cited to the 25YO's capture** (`src_isle-of-skye-25_whiskybase`), where it appears only as a cross-reference ("the 21-year-old has a lowest price of €171.16"), not in a dedicated 21YO capture. The adversarial check expected a hallucination here. It is not one:
- The figure **literally appears** in the cited file, AND
- An **independent WebSearch** against `whiskybase.com/whiskies/whisky/63435` — the 21YO page named in the node's own `url` — reproduces "the lowest price on the market is €171.16," correctly in EUR and correctly attributed to the 21YO.

**Verdict: value verified; provenance defect only.** The source_id should be re-captured into a dedicated `src_isle-of-skye-21_whiskybase` node. This is logged in the 21YO `gaps[]`. It does not fail verification because the datum is true, reproducible, and correctly attributed to its bottle.

## Other cross-bottle checks run
- **Wrong-bottle transposition (WWA 2026):** Isle of Skye won BOTH a Gold (30YO) and a Silver (Cigar Reserve, a different expression) at WWA 2026. The 30YO node correctly claims only the Gold and does not borrow the Silver. Clean.
- **Score attribution (25YO):** WA 94 points reproduces and is correctly tied to the 25YO (not the 21/30, whose WA point scores genuinely did not surface). Minor: the live WA excerpt did not surface the reviewer name "Jonny McCormick," though the 94 and $210 reproduce unambiguously.
- **30YO €290 auction:** literally present in the 30YO capture and corroborated by the 25YO cross-reference; exact live re-confirmation is gated behind a Whiskybase account (node honestly flags this). Met on the literal-support + internal-corroboration standard.

## Coverage gaps (insufficiency — NOT verification failures)
These remain open for a follow-up research pass and do not affect `pass`:
- All three: only 2 distinct REVIEW captures (need ≥3); numeric `scores_ge_2` unmet (21 & 30 have 0 numeric scores; 25 has 1).
- 21YO: WebSearch surfaced candidate sources to close gaps — a tastings.com 90/100 and a whiskeyreviewer.com (2023) review — not yet captured.
- 30YO: IWSC/SFWSC Gold year undated; SRP ~$322 not surfaced verbatim (avg $302 captured instead).
- All three: natural-colour / chill-filtration unconfirmed.

---

# Source Verification Report — Glengoyne cluster

Verifier: adversarial fact-check (Source Verifier stage). Date: 2026-06-16.
Environment: WebFetch BLOCKED (HTTP 403). All re-confirmation done by targeted **WebSearch**
(allowed_domains on the cited source where possible). Reproduction-by-search is the standard.

Bottles: **glengoyne-24** (White Oak, ~47.8%, bourbon/virgin oak) · **glengoyne-25** (Sherry Oak, 48%).

---

## glengoyne-24 — White Oak (Oak Masters' Series) — PASS

Verdicts: 12 verified / 0 mismatch / 0 unsupported. `verification.status = passed`. `pass = true`.

| Field | Claim | Verdict | Source |
|---|---|---|---|
| abv | 47.8% | verified | robbreport |
| cask | American 1st-fill bourbon + virgin/white oak | verified | robbreport |
| availability ("will not return") | Ltd; UK 10 Jul 2024 RRP £430; US Mar 2025 $400 | verified | whiskymag |
| score Drinkhacker A- → 90 | 90 | verified (A-→~90 normalization defensible) | drinkhacker |
| score Robb Report "#2 / Best of Best 2025" | #2 of 2025 (null 100-pt) | verified w/ caveat | robbreport |
| UK price TWE | £415.00 | verified | thewhiskyexchange |
| UK price HTFW | £408.95 | verified | thewhiskyexchange |
| UK price Whisky Shop | £453.00 | verified | thewhiskyexchange |
| US price Total Wine (700ml) | $399.98 | verified (verbatim reproduce) | totalwine |
| US price Whisky Advocate stated | $400 | verified | whiskyadvocate |
| auction Whiskystats | **€294 (EUR)** | verified — currency correctly EUR | whiskystats |
| tasting headline | citrus/vanilla/chocolate, NOT sherry | verified — no 24/25 conflation | robbreport |

**Caveat (logged, non-gating):** The Robb Report "ranked #2 / Best of the Best 2025" claim reproduces
in WebSearch only via **retailer (The Whisky Exchange) marketing copy**. Robb Report's own site exposes
inclusion in "The 10 Best Whiskeys of 2025 So Far" but does NOT surface a confirmed #2 numbered rank
in-page. The datum is non-core (awards-only, `normalized_100 = null`) so it does not gate pass, but the
rank provenance is retailer copy, not a verified Robb Report numbered list. Recommend softening node
language from "Robb Report ranked it the #2 whisky released in 2025" to "Robb Report named it one of the
best new whiskies of 2025 (#2 per retailer listing copy)."

**Conflation / currency checks:** CLEAN. The 24 is unambiguously White Oak (bourbon/virgin oak, 47.8%),
corroborated by the official page title "White Oak." Whiskystats value is **EUR €294** and is correctly
labeled EUR — NOT mislabeled as £/$ — and correctly noted as below retail (no secondary premium).

---

## glengoyne-25 — Sherry Oak — PASS

Verdicts: 8 verified / 0 mismatch / 0 unsupported. `verification.status = passed`. `pass = true`.
(`pass` certifies truthfulness of PRESENT data, not coverage sufficiency — node remains coverage RED.)

| Field | Claim | Verdict | Source |
|---|---|---|---|
| abv | 48% | verified | glengoyneofficial |
| cask | exclusively sherry oak | verified — official page titled "Sherry Oak" | glengoyneofficial |
| natural colour / non-chill-filtered | true / false | verified | glengoyneofficial |
| score | Best Scotch, Whiskey Wash Awards 2025 (null 100-pt) | verified (verbatim) | thewhiskeywash |
| US price Whiskey Wash MSRP | $600 | verified | thewhiskeywash |
| US price Total Wine | null (listing exists, price not exposed) | verified — no fabricated figure | totalwine |
| auction Whisky Returns | **£250.00 GBP (as of 2026-01-28)** | verified (verbatim) | whiskyreturns |
| tasting headline | sherry/dried-fruit/chocolate, NOT citrus | verified — no 24/25 conflation | thewhiskeywash |

**"Whisky Returns" aggregator figure (curator-flagged):** RECONFIRMED. The £250.00 average (as of
2026-01-28) reproduces **verbatim** from whiskyreturns.com via WebSearch, is correctly **GBP**, and is
correctly attributed to Whisky Returns — NOT mislabeled as Whiskystats. The flagged Whiskystats cross-refs
(whisky/135597, /151799) exist but did not expose a clean comparable single figure in snippet; the node
makes no Whiskystats claim, so nothing to correct.

**Conflation / currency checks:** CLEAN. The 25 is unambiguously Sherry Oak (48%; official page title
"Sherry Oak"). Oloroso designation correctly left UNCONFIRMED. £250 is GBP; $600 is USD — both correct.

---

## Cluster summary

- **glengoyne-24: PASS** — 12 verified, 0 mismatch, 0 unsupported.
- **glengoyne-25: PASS** — 8 verified, 0 mismatch, 0 unsupported.
- No node field required quarantine ("N/A — unverified"); no new gaps added.
- **Most important catch:** the suspected 24-vs-25 white-oak/sherry conflation and the EUR-vs-£/$ currency
  swap that the brief warned about did **NOT** occur — the curator kept them correctly walled off
  (Whiskystats €294 EUR for the 24, Whisky Returns £250 GBP for the 25, both correctly labeled). The one
  genuine soft spot is the Robb Report "#2 of 2025" rank, which reproduces only from **retailer marketing
  copy**, not a confirmed Robb Report numbered list — a non-core, non-gating overstatement worth softening.

---

# Verification Report — Tamdhu cluster

Verifier: adversarial Source Verifier. Verified 2026-06-16.
Method: WebFetch was blocked (HTTP 403) on every URL this run, so every datapoint was re-confirmed by (a) quoting it from its cited cached capture and (b) re-running a targeted WebSearch (allowed_domains on the cited source where possible). Reproduction-by-search is the standard per whisky-verify SKILL.md step 2.

Standard applied: **truthfulness, not sufficiency.** `pass=true` iff all PRESENT core fields verify with no mismatch/unsupported. The nodes' RED/AMBER coverage status (driven by the researcher's websearch_excerpt evidence policy) is a sufficiency judgment and does not by itself fail verification.

---

## tamdhu-18 (46.8%, oloroso) — PASS

| Field | Claim | Verdict | Basis |
|---|---|---|---|
| abv | 46.8% | verified | Whiskey Wash capture + WebSearch reproduction |
| cask / colour / chill-filter | oloroso, Euro+American oak, Jerez, natural colour, un-chill-filtered | verified | Whiskey Wash capture + reproduction |
| prices.us TWE→Total Wine | $199.99 | verified | Total Wine capture + WebSearch ("$199.99 at Total Wine & More") |
| scores[0] Whiskybase | 87.20/100 | verified | capture + WebSearch (entry 209109 confirmed) |
| scores[1] SFWSC | Double Gold | verified | Whiskey Wash capture; reproduced via tamdhu.com news + thedailypour roundup |
| auction | GBP ~£90–£100, hammer £100, stale 2024, trend N/A | verified | whisky.auction lot 137270 (correct 46.8% bottle) + WebSearch |
| tasting nose/palate | as written | verified | Whiskey Wash capture |

**Summary: 8 verified, 0 mismatch, 0 unsupported. pass = true.**

Adversarial checks cleared:
- **No 18-vs-21 conflation.** The cited auction is whisky.auction lot 137270 — the standard 46.8% Tamdhu 18, NOT the separate "Tamdhu 18 Limited Release **Cask Strength**" lots that dominate Whisky Hammer.
- **No stale-as-fresh.** The 2024-era auction figures are explicitly labeled stale, as_of 2024-xx-xx, trend N/A.
- **No phantom UK price.** The £299/£275 TWE figures the search surfaced were correctly DROPPED by the researcher (they could not be tied to the 18); the node asserts no UK price.
- **No currency mix-up.** Auction GBP, US retail USD — kept distinct.
- **No award without a source.** SFWSC Double Gold is backed by the distillery's own news page and a third-party roundup.

verification.status set to **passed**. (Coverage stays RED on sufficiency grounds — see node gaps — but every present datum is truthful.)

---

## tamdhu-21 (47.5%, oloroso, 2025 release, 12,000 bottles) — FAIL

| Field | Claim | Verdict | Basis |
|---|---|---|---|
| abv | 47.5% | verified | official_vitals capture + reproduction |
| cask / colour / chill-filter | first-fill+refill Euro+American oak oloroso, Jerez, natural, un-chill-filtered | verified | capture + reproduction |
| outturn | 12,000 bottles, Aug 2025 | verified | whiskeywash_news + WebSearch ("Limited to 12,000 bottles") |
| **prices.uk[0] TWE £299** | **£299** | **MISMATCH** | capture calls it "official RRP"; live TWE listing reproduces at **£295** (two searches) |
| **prices.uk[1] Master of Malt £252.70** | **£252.70** | **UNSUPPORTED** | snippet-only; no independent search reproduces it |
| prices.us Total Wine | $399.99 | verified | capture + WebSearch reproduction |
| scores[0] Robb Report | "Very Good" 85–89 band implied, no /100; Macallan framing | verified | WebSearch reproduced "$400 vs Macallan 25 ~three grand," "sherry bomb banger," Jonah Flicker, pub. 19 Oct 2025 |
| scores[1] Spirit of Speyside 2026 | Gold (18&over) + Overall Winner | verified | sltn.co.uk capture + WebSearch (sltn.co.uk, whiskyexperts.net) |
| scores[2] Scottish Field 2025 | Whisky of the Year / Gold Over £100 / Distillery Bottling of the Year | verified | capture + WebSearch (scottishfield.co.uk Grand Final + JPHA) |
| auction | empty [] | verified | correctly quarantined — see below |
| tasting nose/palate/finish | as written | verified | official_vitals + critic captures |

**Summary: 9 verified, 1 mismatch, 1 unsupported. pass = false.**

Catches and quarantine:
- **MISMATCH — TWE £299.** The node carried £299 as a retail price; that figure is the **official RRP**, and the live The Whisky Exchange listing now reproduces at **£295** on two independent searches. The price_gbp field was set to "N/A — unverified", uk_price criterion flipped to false, gap logged.
- **UNSUPPORTED — Master of Malt £252.70.** Snippet-only; the MoM product page surfaces but exposes no price, and no independent search reproduces £252.70. Set to "N/A — unverified".

Adversarial checks cleared:
- **No false 21yo auction point.** The node's auction array is empty. The researcher correctly determined the only "Tamdhu 21" auction lots are an OLDER ~250-bottle "Cask Strength Limited Edition" — a different bottle — and asserted NO secondary point for the 2025 core 21. Confirmed: no real 21yo core auction figure is claimed.
- **No currency mix-up.** US $399.99 (USD) and the UK GBP figures are kept distinct; the GBP/$ confusion the brief warned about did not occur.
- **Awards real and sourced.** Spirit of Speyside 2026 (sltn.co.uk + whiskyexperts.net) and Scottish Field 2025 (scottishfield.co.uk + JPHA) both reproduce. A stray "Summer Challenge" Silver for *Tamdhu Cigar Malt IV* is an unrelated sub-list and was NOT conflated into the node.
- **No fabricated numeric score.** Robb Report's exact /100 is not exposed; the node correctly sets normalized_100=null and only carries the qualitative band as implied.

verification.status set to **failed** (UK pricing quarantined). The rest of the node is truthful; once a live UK price is captured the bottle can re-verify.

---

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
