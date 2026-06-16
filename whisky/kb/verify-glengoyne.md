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
