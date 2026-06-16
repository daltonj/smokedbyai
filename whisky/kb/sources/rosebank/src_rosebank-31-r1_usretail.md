---
id: src_rosebank-31-r1_usretail
bottle: rosebank-31-r1
source_name: BuyMyLiquor / Riverhead Liquor Mart / Corkdorks (US retail)
url: https://www.buymyliquor.com/products/rosebank-30-year-old-release-1-2020-edition
type: retail
source_date: 2026-06-16
fetched_at: 2026-06-16T00:00:00Z
freshness: fresh
fetch_method: websearch_excerpt   # WebFetch HTTP 403 environment-wide; price excerpts from WebSearch against named US retailers. Reproduced across 2 independent queries with multiple retailers.
---

NOTE ON IDENTITY: "Release One" = Rosebank 30 Year Old (1990, bottled 2020, 48.6% ABV). Filed under slug `rosebank-31-r1` per orchestrator assignment.

PURPOSE: Provide a US retail/secondary price for R1 (prior US prices empty).

VERBATIM EXCERPTS (via WebSearch):
"BuyMyLiquor offers the Rosebank 30 Year Old Vintage Release #1 Bottled In 2020 for $2,999.99."
"Riverhead Liquor Mart - Priced at $3,299.99"
"Corkdorks Nashville - Priced at $3,209.99"

REPRODUCTION LOG:
1. Query: "Rosebank 30 Year Old 1990 Release One price US dollars buy retail secondary wine-searcher" -> "BuyMyLiquor offers ... for $2,999.99."
2. Query: "Rosebank 30 Year Old 1990 Release 1 48.6% price $2,999 BuyMyLiquor OR Flask US retailer" -> "Riverhead Liquor Mart - Priced at $3,299.99 ... Corkdorks Nashville - Priced at $3,209.99 ... aligns with the $2,999 price point."

KEY DATA: US retail listings for the 30yo Release One cluster around USD $3,000-$3,300: BuyMyLiquor $2,999.99; Corkdorks $3,209.99; Riverhead Liquor Mart $3,299.99. Multiple named US retailers, reproduced across 2 searches. Recording BuyMyLiquor $2,999.99 as the primary node datum (lowest named listing).
