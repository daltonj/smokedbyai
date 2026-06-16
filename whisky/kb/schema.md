# Whisky Knowledge Graph — Schema & Contract

> The KG is the single source of truth. Every agent reads/writes through this contract.
> It is **extensible**: new whiskies append new nodes without changing the shape.
> Research anchor for the initial load: **2026-06-16 02:49 UTC**. Freshness window: **last 6 months**.

## Node types

### 1. Distillery node — `kb/distilleries/<slug>.json`
```json
{
  "id": "rosebank",
  "name": "Rosebank",
  "type": "distillery | brand",
  "region": "Lowland | Highland | Speyside | Islay | ...",
  "country": "Scotland",
  "status": "active | closed | reborn",
  "house_style": "short prose, curator voice",
  "owner": "Ian Macleod Distillers",
  "founded": 1840, "closed": 1993, "revived": 2023,
  "notes": "string",
  "source_ids": ["src_..."]
}
```

### 2. Expression node — `kb/expressions/<slug>.json`
One per bottle. Slug pattern: `<distillery>-<age>` (e.g. `glengoyne-25`, `rosebank-31-r2`).
```json
{
  "id": "glengoyne-25",
  "distillery_id": "glengoyne",
  "display_name": "Glengoyne 25 Year Old (Sherry Oak)",
  "category": "single malt | blended",
  "age_years": 25,
  "abv": 48.0,
  "cask": "1st-fill & refill sherry (European/American oak)",
  "natural_colour": true, "chill_filtered": false,
  "outturn_or_availability": "string or N/A — not found",
  "vitals_source_ids": ["src_..."],

  "tasting": {
    "nose": "curator-synthesized, from cited critics",
    "palate": "...",
    "finish": "...",
    "narrative": "curator-voice paragraph + verdict",
    "source_ids": ["src_...", "src_..."]
  },

  "scores": [
    {"critic": "Whiskyfun / Serge", "raw": "88/100", "normalized_100": 88, "source_id": "src_..."}
  ],

  "prices": {
    "uk": [{"retailer": "The Whisky Exchange", "price_gbp": 399.0, "url": "...", "source_id": "src_...", "as_of": "2026-06-15"}],
    "us": [{"retailer": "Total Wine", "price_usd": 525.0, "url": "...", "source_id": "src_...", "as_of": "2026-06-15"}]
  },

  "auction": {
    "platform_data": [
      {"platform": "Whiskystats", "currency": "GBP", "min": null, "avg": 2049, "max": 2500,
       "latest_hammer": 2100, "trend": "rising | flat | falling", "url": "...", "source_id": "src_...", "as_of": "2026-06-10"}
    ]
  },

  "rubric": {
    "drinking": {"critic_consensus": 0, "complexity": 0, "impact": 0, "presentation": 0},
    "value": {"price_to_quality": 0, "rarity": 0, "appreciation": 0, "collectibility": 0},
    "composite": 0
  },

  "coverage": {
    "status": "red | amber | green",
    "criteria": {
      "reviews_ge_3": false, "scores_ge_2": false, "uk_price": false,
      "us_price": false, "auction_point": false, "fresh_point": false
    },
    "gaps": ["string"]
  },

  "verification": {"status": "pending | passed | failed", "report_id": "glengoyne-25.verify.json"},
  "last_updated": "2026-06-16T02:49:00Z"
}
```

### 3. Source node — `kb/sources/<cluster>/<src_id>.md` + index in `kb/sources/manifest.json`
Each cached capture is a Markdown file:
```
---
id: src_rosebank31_whiskystats
bottle: rosebank-31-r2
source_name: Whiskystats
url: https://www.whiskystats.com/whisky/215536
type: review | score | retail | auction | news | vitals
source_date: 2026-05-xx      # date the data/page reflects, if known
fetched_at: 2026-06-16T02:55:00Z
freshness: fresh | stale     # fresh = within 6 months of anchor
---

<verbatim key excerpts of the fetched page — prices, scores, tasting text, dates>
```
`manifest.json` is an array of `{id, bottle, source_name, url, type, source_date, fetched_at, freshness, local_path, key_data}`.
To avoid write contention, each Researcher writes its own `kb/sources/<cluster>.manifest.json`; the orchestrator merges into `manifest.json`.

### 4. Verification record — `kb/expressions/<slug>.verify.json`
Written by the Verifier; per-field verdict.
```json
{
  "expression_id": "glengoyne-25",
  "verified_at": "2026-06-16T03:30:00Z",
  "fields": [
    {"field": "prices.uk[0].price_gbp", "claimed": 399.0, "verdict": "verified | mismatch | unsupported",
     "evidence_quote": "…£399.00…", "source_id": "src_..."}
  ],
  "summary": {"verified": 0, "mismatch": 0, "unsupported": 0},
  "pass": true
}
```

## Coverage rule (definition of done)
- **GREEN**: reviews≥3 AND scores≥2 AND uk_price AND us_price AND auction_point AND fresh_point, AND verification.pass==true.
- **AMBER**: core present, missing freshness / one market / scores, OR verification pending.
- **RED**: below minimums → trigger another research pass on `gaps`.

## Append-a-new-whisky procedure (repeatable)
1. `whisky-research` → create/extend distillery node + draft expression node + cache sources.
2. `whisky-curate` → synthesize, score rubric, compute coverage, list gaps.
3. `whisky-verify` → per-field check vs cached sources; set verification.pass.
4. If RED/AMBER on core → loop step 1 on gaps.
5. `whisky-guide` → regenerate `whisky/data.json` + `whisky/index.html`.
All steps mutate only this KG; the product is always a pure function of the KG.
