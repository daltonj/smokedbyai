#!/usr/bin/env python3
"""whisky-guide builder: compile the KG into data.json and inject it into index.html.

The product is a pure function of the knowledge graph. Re-run after any KG change:
    python3 whisky/build_guide.py
"""
import json, glob, os, datetime, re

ROOT = os.path.dirname(os.path.abspath(__file__))
KB = os.path.join(ROOT, "kb")

ANCHOR = "2026-06-16"
# Indicative FX for the value scatter ONLY (clearly labelled in the UI, not a sourced datum).
FX_USD_PER_GBP = 1.27
FX_GBP_PER_EUR = 0.85

# Recommended flight order (delicate/lighter -> sherry crescendo -> ghost-distillery finale).
TASTING_ORDER = [
    "isle-of-skye-21", "isle-of-skye-30", "isle-of-skye-25",
    "glengoyne-24", "glengoyne-25",
    "tamdhu-18", "tamdhu-21",
    "rosebank-31-r1", "rosebank-31-r2",
]

def num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)

def load_json(p):
    with open(p) as f:
        return json.load(f)

def primary_gbp(b):
    uk = [p["price_gbp"] for p in b.get("prices", {}).get("uk", []) if num(p.get("price_gbp"))]
    return min(uk) if uk else None

def primary_usd(b):
    us = [p["price_usd"] for p in b.get("prices", {}).get("us", []) if num(p.get("price_usd"))]
    return min(us) if us else None

def secondary_gbp(b):
    """Best-effort secondary value in GBP for the value scatter (indicative conversions flagged)."""
    best = None
    for pd in b.get("auction", {}).get("platform_data", []):
        cur = pd.get("currency")
        val = pd.get("avg") or pd.get("latest_hammer") or pd.get("min") or pd.get("max")
        if not num(val):
            continue
        if cur == "GBP":
            g = val
        elif cur == "EUR":
            g = val * FX_GBP_PER_EUR
        elif cur == "USD":
            g = val / FX_USD_PER_GBP
        else:
            continue
        # prefer GBP-native and aggregate figures
        if best is None or cur == "GBP":
            best = round(g)
    return best

def retail_gbp_equiv(b):
    g = primary_gbp(b)
    if g is not None:
        return g
    u = primary_usd(b)
    return round(u / FX_USD_PER_GBP) if u is not None else None

def is_unverified(x):
    return isinstance(x, str) and "unverified" in x.lower()

def recompute_coverage(b, manifest):
    """Consistent, defensible red/amber/green from the actual cited data + verification."""
    srcs = [s for s in manifest if isinstance(s, dict) and s.get("bottle") == b["id"]]
    reviews = sum(1 for s in srcs if str(s.get("type", "")).startswith("review"))
    scores_num = sum(1 for s in (b.get("scores") or [])
                     if num(s.get("normalized_100")) and not is_unverified(s.get("raw")))
    uk = any(num(p.get("price_gbp")) and not is_unverified(p.get("price_gbp"))
             for p in b.get("prices", {}).get("uk", []))
    us = any(num(p.get("price_usd")) and not is_unverified(p.get("price_usd"))
             for p in b.get("prices", {}).get("us", []))
    auction = any(num(a.get("avg")) or num(a.get("latest_hammer")) or num(a.get("min")) or num(a.get("max"))
                  for a in b.get("auction", {}).get("platform_data", []))
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

    manifest = []
    mp = os.path.join(KB, "sources", "manifest.json")
    if os.path.exists(mp):
        manifest = load_json(mp)
    src_by_id = {s.get("id"): s for s in manifest if isinstance(s, dict)}

    # attach verification if present
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
        # consistent coverage recompute (preserve curator/verifier gaps), write back to KG
        crit, status = recompute_coverage(b, manifest)
        b.setdefault("coverage", {})
        b["coverage"]["criteria"] = crit
        b["coverage"]["status"] = status
        with open(p, "w") as f:
            json.dump(b, f, indent=2, ensure_ascii=False)
        b["_primaryGBP"] = primary_gbp(b)
        b["_primaryUSD"] = primary_usd(b)
        b["_secondaryGBP"] = secondary_gbp(b)
        b["_retailGBPequiv"] = retail_gbp_equiv(b)
        comp = b.get("rubric", {}).get("composite") or 0
        rge = b["_retailGBPequiv"]
        b["_valueIndex"] = round(comp / rge * 1000, 1) if rge else None
        bottles.append(b)

    # rank by composite desc
    ranked = sorted(bottles, key=lambda x: x.get("rubric", {}).get("composite", 0), reverse=True)
    for i, b in enumerate(ranked, 1):
        b["_rank"] = i

    data = {
        "meta": {
            "title": "The Curator's Guide — Tasting Night Dossier",
            "anchor": ANCHOR,
            "freshness_window": "Dec 2025 – Jun 2026",
            "generated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "fx_note": f"Value-for-money chart uses indicative FX (£1≈${FX_USD_PER_GBP}, €1≈£{FX_GBP_PER_EUR}); native-currency prices below are the sourced figures.",
            "source_count": len(manifest),
            "bottle_count": len(bottles),
            "fetch_note": "All data captured via WebSearch against expert/auction sources (WebFetch egress was blocked); every datum links to its source.",
        },
        "distilleries": distilleries,
        "bottles": bottles,
        "tasting_order": [bid for bid in TASTING_ORDER if any(b["id"] == bid for b in bottles)],
        "sources": manifest,
    }

    out = os.path.join(ROOT, "data.json")
    with open(out, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"wrote {out}: {len(bottles)} bottles, {len(distilleries)} distilleries, {len(manifest)} sources")

    # inject into index.html if a template marker exists
    tpl = os.path.join(ROOT, "index.html")
    if os.path.exists(tpl):
        html = open(tpl, encoding="utf-8").read()
        payload = json.dumps(data, ensure_ascii=False)
        new = re.sub(
            r'(<script id="whisky-data" type="application/json">).*?(</script>)',
            lambda m: m.group(1) + payload + m.group(2),
            html, flags=re.DOTALL)
        if new != html:
            open(tpl, "w", encoding="utf-8").write(new)
            print("injected data into index.html")
    return data

if __name__ == "__main__":
    build()
