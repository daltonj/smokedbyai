---
id: src_rosebank-31-r1_usretail_flask
bottle: rosebank-31-r1
source_name: FLASK Fine Wines / World Wine Whisky / Wine-Searcher (US retail, 30yo Release One)
url: https://flaskfinewines.com/products/rosebank-30-year-old-1990-release-1-70cl-48-6
type: retail
source_date: 2026-06-16
fetched_at: 2026-06-16T00:00:00Z
freshness: fresh
fetch_method: websearch_excerpt   # WebFetch BLOCKED environment-wide; price excerpts from WebSearch against named US retailers + Wine-Searcher US average. Each figure reproduced across >=2 independent queries.
---

IDENTITY (confirmed before writing): "Release One" = Rosebank 30 YEAR OLD (distilled 1990, bottled 2020, 48.6% ABV, 4,350 bottles). All excerpts below are explicitly tied to the 30yo Release 1 / Release #1 / 48.6% — NOT the 31yo Release Two. Filed under orchestrator slug `rosebank-31-r1`.

PURPOSE: Add named US retailers + the Wine-Searcher US price spread for R1 (30yo), supplementing the existing BuyMyLiquor $2,999.99 node entry.

VERBATIM EXCERPTS (via WebSearch):
"Buy Rosebank 30 Year Old 1990 Release 1 48.6% by Rosebank | FLASK" (flaskfinewines.com product page — US retailer, Los Angeles).
"the average price is $3,040 per 750ml, though one retailer offers it for $2,999.99." (Wine-Searcher USA average for the 30yo Release 1.)
"Corkdorks Nashville lists it at $3,209.99, while Riverhead Liquor Mart in New York has it priced at $3,299.99."
"Rosebank 30 Years Old 1990 2020 - Release 1 48.6% (1 of 4350 bottles) | WORLD WINE WHISKY" (worldwinewhisky.com/us/ — US retailer carries the 30yo Release 1).
"1990 Rosebank 30 Year Old Release 1 Unchillfiltered Lowland Single Malt Whisky" (thewinestop.com — US retailer carries the 30yo Release 1).

REPRODUCTION LOG (independent queries):
1. Query: "Rosebank 30 Year Old 1990 Release 1 48.6% FLASK Fine Wines price dollars" -> FLASK product page returned; "Corkdorks Nashville ... $3,209.99 ... Riverhead Liquor Mart ... $3,299.99 ... Wine-Searcher shows prices ranging ... at various retailers."
2. Query: "Rosebank 30 Year Old 1990 Release 1 World Wine Whisky price USD buy 48.6%" -> "The average price for Rosebank 30 Year Old is approximately $3,040 USD per 750ml ... available from retailers like World Wine Whisky and Flask Fine Wines."
3. Query: "Rosebank 30 Year Old 1990 Release 1 wine-searcher USA average price $3,040 stores" -> "The average price for Rosebank 30 Year Old ... on Wine-Searcher in the USA is $3,040."
4. Query: "Rosebank 30 Year Old 1990 Release 1 FLASK Fine Wines $3,499 ..." -> "the average price is $3,040 per 750ml, though one retailer offers it for $2,999.99."

EXCLUDED (did NOT reproduce — not written): a one-off mention of a Wine-Searcher US range "$3,610.99 to $3,968.99" appeared in a single query but failed reproduction (follow-up search instead said "retail price found appears to be slightly lower at around $3,300"); a Main Street Liquor "$99.99 sale price" is an obvious scrape glitch for a ~$3k bottle. Neither used.

KEY DATA: US retail for the 30yo Release One clusters ~ $2,999.99–$3,299.99 across named US retailers (BuyMyLiquor $2,999.99; Corkdorks $3,209.99; Riverhead $3,299.99), with FLASK Fine Wines, World Wine Whisky (US) and TheWineStop also carrying it. Wine-Searcher USA average $3,040 (reproduced x2). Recording the Wine-Searcher US average ($3,040, FLASK/World Wine Whisky listed retailers) as the new node datum alongside the existing BuyMyLiquor entry.
