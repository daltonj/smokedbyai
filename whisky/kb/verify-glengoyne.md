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
