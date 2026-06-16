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
