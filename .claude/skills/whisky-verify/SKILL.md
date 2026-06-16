---
name: whisky-verify
description: Source Verifier stage of the whisky engine — an adversarial fact-checker that independently validates a curated expression node against its cached sources to catch hallucinations and BS. Use after curation, before a bottle can reach GREEN. Re-reads each cached capture (and re-fetches a live sample), confirms every price/score/tasting/auction/date actually appears in its cited source, and quarantines anything unsupported.
---

# whisky-verify — Source Verifier stage (adversarial)

Trust nothing the curator wrote. Your job is to break the data, not defend it.

## Procedure
1. Load `kb/expressions/<slug>.json`. For **every** datapoint (each price, score, tasting descriptor,
   auction figure, ABV, date), open its cited capture in `kb/sources/<cluster>/` and confirm the claim
   literally appears there. Pull the supporting quote/locator.
2. Re-confirm a **sample** of datapoints against the live web: re-fetch the URL (WebFetch) where egress
   allows; otherwise **re-run a targeted WebSearch** (with `allowed_domains` on the cited source) and
   confirm the same figure/score/text reproduces. A datum that no independent search can reproduce is
   `unsupported`. For `method: websearch` captures, reproduction-by-search IS the verification standard.
3. Specifically hunt for: numbers attributed to the **wrong bottle/release**, transposed or rounded
   figures, **currency mix-ups** (£ vs $), stale data presented as fresh, averaged ranges stated as
   single facts, and any **slop** source that evaded the filters.
4. Emit `kb/expressions/<slug>.verify.json` per schema: per-field `verdict` (`verified | mismatch |
   unsupported`) with `evidence_quote` + `source_id`, plus a summary count and `pass` boolean.
   `pass=true` only if **all core fields** (vitals, ≥2 scores, both market prices, auction point) verify.
5. For any `mismatch`/`unsupported`, set that field in the expression node to `N/A — unverified` and add
   to `gaps`. Append a section to `kb/verification-report.md`.
6. Set `verification.status = passed|failed`. A bottle reaches GREEN only when `pass=true`.
