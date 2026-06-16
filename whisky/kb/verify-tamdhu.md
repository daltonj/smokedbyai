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
