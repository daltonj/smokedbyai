#!/usr/bin/env python3
"""whisky-guide builder: compile the KG into data.json and inject it into index.html.

The product is a pure function of the knowledge graph. Re-run after any KG change:
    python3 whisky/build_guide.py
"""
import json, glob, os, datetime, re

ROOT = os.path.dirname(os.path.abspath(__file__))
KB = os.path.join(ROOT, "kb")

ANCHOR = "2026-06-16"
# Indicative FX for £-equiv comparisons ONLY (clearly labelled in the UI, not a sourced datum).
FX_USD_PER_GBP = 1.27
FX_GBP_PER_EUR = 0.85

TASTING_ORDER = [
    "isle-of-skye-21", "isle-of-skye-30", "isle-of-skye-25",
    "glengoyne-24", "glengoyne-25",
    "tamdhu-18", "tamdhu-21",
    "rosebank-31-r1", "rosebank-31-r2",
]

# platforms whose figures count as a real secondary/auction point
AUCTION_WHITELIST = ("whiskystats", "whiskyhunter", "whiskybase", "auctioneer",
                     "scotch whisky auction", "whisky.auction", "whisky-online",
                     "rare whisky", "whisky hammer")
# retailer-string markers that mean "not a transactable shelf price"
NONRETAIL = ("msrp", "srp", "rrp", "market avg", "average", "ex-tax", "stated",
             "wine-searcher", "winesearcher", "concierge")

def num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)

def load_json(p):
    with open(p) as f:
        return json.load(f)

def is_unverified(x):
    return isinstance(x, str) and "unverified" in x.lower()

def _clean(prices, key):
    out = []
    for p in prices:
        v = p.get(key)
        if num(v) and not is_unverified(v):
            retail = not any(m in (p.get("retailer", "") or "").lower() for m in NONRETAIL)
            out.append({"v": v, "retailer": p.get("retailer", ""), "retail": retail,
                        "as_of": p.get("as_of", ""), "url": p.get("url"), "source_id": p.get("source_id")})
    return out

def price_block(b, side, key):
    """Return {min,max,count,primary,primary_label,primary_kind} for a market side."""
    arr = _clean(b.get("prices", {}).get(side, []), key)
    if not arr:
        return None
    vals = [a["v"] for a in arr]
    transact = [a for a in arr if a["retail"]]
    # primary = cheapest transactable shelf price; else cheapest of all (flagged as MSRP/avg)
    pick = min(transact, key=lambda a: a["v"]) if transact else min(arr, key=lambda a: a["v"])
    kind = "retail" if pick["retail"] else "list"   # 'list' = MSRP/avg/stated
    return {"min": round(min(vals)), "max": round(max(vals)), "count": len(arr),
            "primary": round(pick["v"]), "primary_label": pick["retailer"],
            "primary_kind": kind, "primary_as_of": pick["as_of"]}

def secondary(b):
    """Pick the best secondary datum; keep it NATIVE and flag any FX conversion."""
    best = None  # (rank, dict)
    for pd in b.get("auction", {}).get("platform_data", []):
        plat = (pd.get("platform", "") or "").lower()
        wl = any(w in plat for w in AUCTION_WHITELIST)
        hammer = pd.get("latest_hammer")
        avg = pd.get("avg")
        if num(hammer):
            val, kind, rank = hammer, "hammer", 3
        elif num(avg) and wl:
            val, kind, rank = avg, "avg", 2
        elif num(pd.get("min")) and wl:
            val, kind, rank = pd.get("min"), "low offer", 1
        else:
            continue
        cur = pd.get("currency", "")
        gbp = (val if cur == "GBP" else val * FX_GBP_PER_EUR if cur == "EUR"
               else val / FX_USD_PER_GBP if cur == "USD" else None)
        cand = {"value": round(val), "currency": cur, "gbp_equiv": round(gbp) if gbp else None,
                "fx": cur != "GBP", "platform": pd.get("platform"), "kind": kind,
                "as_of": pd.get("as_of", ""), "source_id": pd.get("source_id"),
                "is_point": kind in ("hammer", "avg")}
        if best is None or rank > best[0]:
            best = (rank, cand)
    return best[1] if best else None

def recompute_coverage(b, manifest):
    srcs = [s for s in manifest if isinstance(s, dict) and s.get("bottle") == b["id"]]
    reviews = sum(1 for s in srcs if str(s.get("type", "")).startswith("review"))
    scores_num = sum(1 for s in (b.get("scores") or [])
                     if num(s.get("normalized_100")) and not is_unverified(s.get("raw")))
    uk = price_block(b, "uk", "price_gbp") is not None
    us = price_block(b, "us", "price_usd") is not None
    sec = b.get("_secondary")
    auction = bool(sec and sec.get("is_point"))   # tightened: hammer or whitelisted avg only
    fresh = any(s.get("freshness") == "fresh" for s in srcs)
    crit = {"reviews_ge_3": reviews >= 3, "scores_ge_2": scores_num >= 2,
            "uk_price": uk, "us_price": us, "auction_point": auction, "fresh_point": fresh}
    verify_pass = (b.get("verification", {}) or {}).get("status") == "passed"
    if all(crit.values()) and verify_pass:
        status = "green"
    elif (not uk and not us) or (scores_num == 0 and reviews < 2):
        status = "red"
    else:
        status = "amber"
    return crit, status

def build():
    distilleries = {}
    for p in sorted(glob.glob(os.path.join(KB, "distilleries", "*.json"))):
        d = load_json(p)
        distilleries[d["id"]] = d

    manifest = load_json(os.path.join(KB, "sources", "manifest.json")) if os.path.exists(os.path.join(KB, "sources", "manifest.json")) else []

    bottles = []
    for p in sorted(glob.glob(os.path.join(KB, "expressions", "*.json"))):
        if p.endswith(".verify.json"):
            continue
        b = load_json(p)
        vp = p.replace(".json", ".verify.json")
        if os.path.exists(vp):
            try:
                v = load_json(vp)
                b.setdefault("verification", {})
                b["verification"]["pass"] = v.get("pass")
                b["verification"]["summary"] = v.get("summary")
                b["verification"]["status"] = "passed" if v.get("pass") else ("failed" if v.get("pass") is False else b.get("verification", {}).get("status", "pending"))
            except Exception:
                pass
        # pricing blocks + secondary (native)
        b["_uk"] = price_block(b, "uk", "price_gbp")
        b["_us"] = price_block(b, "us", "price_usd")
        b["_secondary"] = secondary(b)
        # retail £-equiv for the value scatter
        rge = b["_uk"]["primary"] if b["_uk"] else (round(b["_us"]["primary"] / FX_USD_PER_GBP) if b["_us"] else None)
        b["_retailGBPequiv"] = rge
        # official RRP from the producer layer
        im = (distilleries.get(b.get("distillery_id"), {}) or {}).get("ian_macleod", {}) or {}
        b["_officialRRP"] = (im.get("official_rrp", {}) or {}).get(b["id"])
        # coverage recompute (uses _secondary) + write back
        crit, status = recompute_coverage(b, manifest)
        b.setdefault("coverage", {})
        b["coverage"]["criteria"] = crit
        b["coverage"]["status"] = status
        write = {k: v for k, v in b.items() if not k.startswith("_")}
        with open(p, "w") as f:
            json.dump(write, f, indent=2, ensure_ascii=False)
        comp = b.get("rubric", {}).get("composite") or 0
        b["_valueIndex"] = round(comp / rge * 1000, 1) if rge else None
        bottles.append(b)

    ranked = sorted(bottles, key=lambda x: x.get("rubric", {}).get("composite", 0), reverse=True)
    for i, b in enumerate(ranked, 1):
        b["_rank"] = i

    # producer profile (Ian Macleod) — pull the richest ian_macleod block
    producer = {"name": "Ian Macleod Distillers", "brands": {}, "source_ids": []}
    for did, d in distilleries.items():
        im = d.get("ian_macleod")
        if im:
            if im.get("company_facts") and "profile" not in producer:
                producer["profile"] = im["company_facts"]
            if im.get("portfolio") and "portfolio" not in producer:
                producer["portfolio"] = im["portfolio"]
            producer["brands"][did] = {"name": d.get("name"), "url": im.get("official_brand_url"),
                                       "status": d.get("status"), "region": d.get("region")}
            for s in im.get("source_ids", []):
                if s not in producer["source_ids"]:
                    producer["source_ids"].append(s)

    data = {
        "meta": {
            "title": "The Curator's Guide — Tasting Night Dossier",
            "anchor": ANCHOR,
            "freshness_window": "Dec 2025 – Jun 2026",
            "generated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "fx_note": f"Some £-equiv figures use indicative FX (£1≈${FX_USD_PER_GBP}, €1≈£{FX_GBP_PER_EUR}) and are marked “FX est.”; native-currency prices are the sourced figures.",
            "method_note": "All data captured via WebSearch against named expert/retail/auction pages (WebFetch egress was blocked) and reproduced by a second search; not verbatim full-page fetches.",
            "source_count": len(manifest),
            "bottle_count": len(bottles),
        },
        "producer": producer,
        "distilleries": distilleries,
        "bottles": bottles,
        "tasting_order": [bid for bid in TASTING_ORDER if any(b["id"] == bid for b in bottles)],
        "sources": manifest,
    }

    out = os.path.join(ROOT, "data.json")
    with open(out, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"wrote {out}: {len(bottles)} bottles, {len(distilleries)} distilleries, {len(manifest)} sources")

    tpl = os.path.join(ROOT, "index.html")
    if os.path.exists(tpl):
        html = open(tpl, encoding="utf-8").read()
        payload = json.dumps(data, ensure_ascii=False)
        new = re.sub(r'(<script id="whisky-data" type="application/json">).*?(</script>)',
                     lambda m: m.group(1) + payload + m.group(2), html, flags=re.DOTALL)
        if new != html:
            open(tpl, "w", encoding="utf-8").write(new)
            print("injected data into index.html")
    return data

if __name__ == "__main__":
    build()
