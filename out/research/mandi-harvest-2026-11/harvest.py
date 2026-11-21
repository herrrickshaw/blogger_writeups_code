"""Harvest discount: how far below trend each crop's mandi price sits in the months its arrivals peak.

Usage: python3 harvest.py <state_monthly.csv.gz> <out.json> [--crops a,b,c] [--end YYYY-MM]
Method (all-India and state, Agmarknet state-monthly, state-months under 50 t dropped):
  trend    = centred 12-month moving average of the monthly price (2x12 MA, needs 13 months)
  index_m  = mean over years of price / trend for calendar month m (seasonal price index), Jan 2019 - END
  share_m  = mean share of the calendar year's arrivals in month m, calendar years 2019-2024
             (before Agmarknet widened coverage in Nov 2025, which would bias later shares)
  discount = sum_m share_m * index_m - 1  (what the average arriving tonne fetched against trend)
  peak     = the 3 calendar months with the largest share_m; peak_index = their mean index - 1
  spread   = max index_m / min index_m - 1
"""
import sys, json, time, numpy as np, pandas as pd
SRC, OUT = sys.argv[1:3]
arg = lambda k: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else None
END = arg("--end") or "2026-10"; ONLY = arg("--crops")
CORE = ["Wheat", "Paddy(Common)", "Rice", "Maize", "Jowar(Sorghum)", "Bajra(Pearl Millet/Cumbu)", "Ragi(Finger Millet)",
        "Bengal Gram(Gram)(Whole)", "Red gram/Arhar/Tur(whole)", "Green Gram(Moong)(Whole)", "Black Gram(Urd Beans)(Whole)",
        "Lentil(Masur)(Whole)", "Soyabean", "Mustard", "Groundnut", "Cotton", "Onion", "Potato", "Tomato", "Garlic",
        "Dry Chillies", "Turmeric", "Cummin Seed(Jeera)"]
crops = ONLY.split(",") if ONLY else CORE
d = pd.read_csv(SRC); d = d[(d.month <= END) & d.commodity.isin(crops) & (d.arrivals_t >= 50) & d.price_rs_qtl.notna()]
d["pa"] = d.price_rs_qtl * d.arrivals_t
ai = d.groupby(["commodity", "month"], as_index=False)[["pa", "arrivals_t"]].sum().assign(state="All India")
d = pd.concat([d[["commodity", "state", "month", "pa", "arrivals_t"]], ai])
d["price"] = d.pa / d.arrivals_t
months = pd.period_range("2019-01", END, freq="M").strftime("%Y-%m")

def calc(g):
    s = g.set_index("month").reindex(months)
    p, a = s.price, s.arrivals_t.fillna(0)
    w = np.r_[0.5, np.ones(11), 0.5] / 12
    tr = p.rolling(13, center=True).apply(lambda x: (x * w).sum() if x.notna().all() else np.nan, raw=False)
    ratio = (p / tr).dropna()
    cal = pd.Series(ratio.values, index=[int(m[5:]) for m in ratio.index])
    yrs = pd.Series(a.values, index=a.index)
    sh = []
    for y in range(2019, 2025):
        ya = yrs[[f"{y}-{m:02d}" for m in range(1, 13)]]
        if ya.sum() > 0 and (ya > 0).sum() >= 6: sh.append(ya.values / ya.sum())
    cnt = cal.groupby(level=0).size().reindex(range(1, 13)).fillna(0)
    if len(sh) < 4 or cnt.min() < 4: return None   # every calendar month needs >= 4 years of index
    share = np.mean(sh, axis=0); idx = cal.groupby(level=0).mean().reindex(range(1, 13)).values
    peak = np.argsort(-share)[:3]
    return dict(share=share.round(4).tolist(), index=idx.round(4).tolist(), years=len(sh),
                discount=float((share * idx).sum() / share.sum() - 1), peak=[int(i) + 1 for i in sorted(peak)],
                peak_share=float(share[peak].sum()), peak_index=float(idx[peak].mean() - 1),
                spread=float(np.nanmax(idx) / np.nanmin(idx) - 1), cheapest=int(np.nanargmin(idx)) + 1,
                dearest=int(np.nanargmax(idx)) + 1, arr_last12=float(a[-12:].sum()))
res, t0, groups = {}, time.time(), list(d.groupby(["commodity", "state"]))
for i, ((c, s), g) in enumerate(groups, 1):
    r = calc(g)
    if r: res[f"{c}|{s}"] = r
    if i % 50 == 0 or i == len(groups):
        el = time.time() - t0; print(f"  {i}/{len(groups)} pairs, {el:.0f}s elapsed, ~{el / i * (len(groups) - i):.0f}s left", flush=True)
json.dump({"end": END, "res": res}, open(OUT, "w"))
print("kept", len(res), "pairs")
