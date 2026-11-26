"""Backtest ideas 1 and 2 (price-only proxy version): India post-event drift by size tercile and period, and the continuation slope by year.

What this is: a volume-spike event study on NSE/BSE daily prices, 2016-2025. It is NOT the test in out/topics/pead-backtest-ideas-2026-11-26.md:
there are no exchange result timestamps and no analyst surprises in the data, so events are volume-spike days (the stand-in this blog already found weak),
and "surprise" is the market-adjusted return over [t-1, t+1]. An in-results-season flag is used as a crude filter for earnings days.

Run:  python3.13 out/research/pead-india-backtest-2026/run.py /path/to/global-market-data/warehouse
Needs pandas, numpy. Writes results.json and RESULTS.md next to this file.
"""
import json
import pathlib
import sys

import numpy as np
import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
WH = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "/home/user/herrrickshaw/global-market-data/warehouse")
YEARS = range(2016, 2026)
LOOK = 60            # trailing window for volume and sigma
VOL_X = 2.5          # volume spike multiple
SIG_X = 2.0          # abnormal return sigma multiple
GAP = 40             # de-cluster: no event in the previous 40 trading days for the same stock
H_SHORT, H_LONG = 20, 60
MIN_TV = 5e6         # eligibility: trailing 60-day median traded value at least Rs 50 lakh
MIN_PX = 20.0
BIN_MIN = 100        # a cell under 100 events is "too few to read"

# ---------------------------------------------------------------- load and clean
frames = []
for y in YEARS:
    df = pd.read_parquet(WH / f"ohlcv_adj/IN/year={y}.parquet", columns=["Date", "Symbol", "Close", "Volume"])
    frames.append(df)
px = pd.concat(frames, ignore_index=True)
px = px.drop_duplicates(["Date", "Symbol"])
close = px.pivot(index="Date", columns="Symbol", values="Close").sort_index()
vol = px.pivot(index="Date", columns="Symbol", values="Volume").reindex(close.index)
close = close.where(close > 0)
dates = close.index
print("panel", close.shape, dates[0].date(), dates[-1].date(), flush=True)

ret = close.pct_change(fill_method=None)
bad = (ret.abs() > 0.40)                      # splits and glitches: dropped, as in the repo's PEAD module
ret = ret.mask(bad).clip(-0.25, 0.25)
n_bad = int(bad.sum().sum())
tv = close * vol                              # traded value, rupees
tv60 = tv.rolling(LOOK, min_periods=40).median().shift(1)
elig = (tv60 >= MIN_TV) & (close.shift(1) >= MIN_PX) & ret.notna()
mkt = ret.where(elig).mean(axis=1)            # equal-weight market return over eligible stocks
abn = ret.sub(mkt, axis=0)

vavg = vol.rolling(LOOK, min_periods=40).mean().shift(1)
sig = abn.rolling(LOOK, min_periods=40).std().shift(1)
spike = (vol > VOL_X * vavg) & (abn.abs() > SIG_X * sig) & elig
size_pct = tv.rolling(252, min_periods=150).median().shift(1).where(elig).rank(axis=1, pct=True)   # trailing 252d traded value, percentile among eligible stocks that day

A = abn.fillna(0.0).to_numpy()
S = np.cumsum(np.vstack([np.zeros((1, A.shape[1])), A]), axis=0)      # S[k] = sum of A[:k]
def car(i0, i1):
    """sum of abnormal returns over positions i0..i1 inclusive, per column, for row-position arrays; used per event below."""
    return S[i1 + 1] - S[i0]

# ---------------------------------------------------------------- events
sp = spike.to_numpy()
rows = []
T, N = sp.shape
syms = np.array(close.columns)
for j in range(N):
    idx = np.flatnonzero(sp[:, j])
    last = -10**9
    for t in idx:
        if t - last < GAP:
            continue
        last = t
        if t < 1 or t + H_LONG + 1 >= T:
            continue
        rows.append((j, t))
ev = pd.DataFrame(rows, columns=["j", "t"])
ev["date"] = dates[ev["t"].to_numpy()]
ev["sym"] = syms[ev["j"].to_numpy()]
ev["surp"] = [S[t + 2, j] - S[t - 1, j] for j, t in zip(ev.j, ev.t)]                 # [t-1, t+1]
ev["d20"] = [S[t + 2 + H_SHORT, j] - S[t + 2, j] for j, t in zip(ev.j, ev.t)]       # [t+2, t+21]
ev["d60"] = [S[t + 2 + H_LONG, j] - S[t + 2, j] for j, t in zip(ev.j, ev.t)]        # [t+2, t+61]
ev["size_pct"] = [size_pct.to_numpy()[t, j] for j, t in zip(ev.j, ev.t)]
ev = ev[ev.surp.abs() > 0].dropna(subset=["size_pct"]).copy()
ev["size"] = pd.cut(ev.size_pct, [0, 1 / 3, 2 / 3, 1.0001], labels=["small", "mid", "large"], include_lowest=True)
md = ev.date.dt.month * 100 + ev.date.dt.day
ev["season"] = ((md >= 715) & (md <= 820)) | ((md >= 1015) & (md <= 1120)) | ((md >= 115) & (md <= 220)) | ((md >= 425) & (md <= 605))
ev["year"] = ev.date.dt.year
ev["period"] = pd.cut(ev.year, [2015, 2018, 2021, 2025], labels=["2016-18", "2019-21", "2022-25"])
ev["sgn"] = np.sign(ev.surp)
ev["sd60"] = ev.sgn * ev.d60          # signed drift: positive = continuation in the direction of the first move
ev["sd20"] = ev.sgn * ev.d20
print("events", len(ev), "in season share", round(ev.season.mean(), 3), flush=True)

# ---------------------------------------------------------------- statistics
def clustered_mean(x, g):
    """mean and date-clustered standard error."""
    x = np.asarray(x, float); g = np.asarray(g)
    m = x.mean(); n = len(x)
    gs = pd.Series(x - m).groupby(g).sum()
    se = np.sqrt((gs ** 2).sum()) / n
    return m, se

def cell_stats(d):
    m, se = clustered_mean(d.sd60, d.date)
    m20, se20 = clustered_mean(d.sd20, d.date)
    out = dict(n=len(d), mean60=100 * m, t60=m / se if se > 0 else np.nan, med60=100 * d.sd60.median(), pos60=100 * (d.sd60 > 0).mean(),
               mean20=100 * m20, t20=m20 / se20 if se20 > 0 else np.nan)
    if len(d) >= BIN_MIN:
        q = pd.qcut(d.surp.rank(method="first"), 5, labels=False)
        g = d.groupby(q).d60.mean()
        out["gap60"] = 100 * (g.iloc[4] - g.iloc[0])
        out["mono"] = float(pd.Series(g.values).corr(pd.Series(range(5)), method="spearman"))
        # slope of d60 on the first move, date-clustered
        x = d.surp.to_numpy(); y = d.d60.to_numpy(); xm, ym = x.mean(), y.mean()
        b = ((x - xm) * (y - ym)).sum() / ((x - xm) ** 2).sum()
        e = (y - ym) - b * (x - xm)
        sc = pd.Series((x - xm) * e).groupby(d.date.to_numpy()).sum()
        seb = np.sqrt((sc ** 2).sum()) / ((x - xm) ** 2).sum()
        out["slope"] = b; out["slope_t"] = b / seb
    return out

# ---------------------------------------------------------------- placebo: big price move on ordinary volume (no volume spike), same de-clustering and windows
def build_events(mask):
    sp2 = mask.to_numpy(); rows2 = []
    for j in range(sp2.shape[1]):
        last2 = -10**9
        for t in np.flatnonzero(sp2[:, j]):
            if t - last2 < GAP: continue
            last2 = t
            if t < 1 or t + H_LONG + 1 >= sp2.shape[0]: continue
            rows2.append((j, t))
    e = pd.DataFrame(rows2, columns=["j", "t"])
    e["date"] = dates[e.t.to_numpy()]
    e["surp"] = [S[t + 2, j] - S[t - 1, j] for j, t in zip(e.j, e.t)]
    e["d60"] = [S[t + 2 + H_LONG, j] - S[t + 2, j] for j, t in zip(e.j, e.t)]
    e["size_pct"] = [size_pct.to_numpy()[t, j] for j, t in zip(e.j, e.t)]
    e = e[e.surp.abs() > 0].dropna(subset=["size_pct"]).copy()
    e["sd60"] = np.sign(e.surp) * e.d60
    e["size"] = pd.cut(e.size_pct, [0, 1 / 3, 2 / 3, 1.0001], labels=["small", "mid", "large"], include_lowest=True)
    e["year"] = e.date.dt.year
    return e
placebo_mask = ((abn.abs() > SIG_X * sig) & (vol < 1.5 * vavg) & elig)
pe = build_events(placebo_mask)
placebo = {}
for sz in ["small", "mid", "large", "all"]:
    d = pe if sz == "all" else pe[pe["size"] == sz]
    m, se = clustered_mean(d.sd60, d.date)
    placebo[sz] = dict(n=len(d), mean60=100 * m, t60=m / se, pos60=100 * (d.sd60 > 0).mean())
print("placebo", {k: (v["n"], round(v["mean60"], 2), round(v["t60"], 2)) for k, v in placebo.items()}, flush=True)

res = {"panel": dict(start=str(dates[0].date()), end=str(dates[-1].date()), symbols=int(N), days=int(T), glitch_moves_dropped=n_bad),
       "events": dict(total=int(len(ev)), in_season_share=float(ev.season.mean()), null_season_share=145 / 365)}
cells = {}
for sub_name, sub in [("all events", ev), ("results-season events", ev[ev.season])]:
    for per in ["2016-18", "2019-21", "2022-25", "all"]:
        for sz in ["small", "mid", "large", "all"]:
            d = sub
            if per != "all": d = d[d.period == per]
            if sz != "all": d = d[d["size"] == sz]
            if len(d) >= 20:
                cells[f"{sub_name} | {per} | {sz}"] = cell_stats(d)
res["cells"] = cells
res["placebo_large_move_ordinary_volume"] = placebo
yr = {}
for sub_name, sub in [("all events", ev), ("results-season events", ev[ev.season])]:
    for y in sorted(sub.year.unique()):
        for sz in ["small", "large", "all"]:
            d = sub[sub.year == y]
            if sz != "all": d = d[d["size"] == sz]
            if len(d) >= BIN_MIN:
                s = cell_stats(d); yr[f"{sub_name} | {y} | {sz}"] = dict(n=s["n"], slope=s["slope"], slope_t=s["slope_t"], mean60=s["mean60"], t60=s["t60"])
res["by_year"] = yr
(HERE / "results.json").write_text(json.dumps(res, indent=1, default=float))

def fmt(v, p=1):
    return "-" if v is None or (isinstance(v, float) and np.isnan(v)) else f"{v:.{p}f}"
L = ["# India price-only drift backtest, results", "", f"Panel: {res['panel']}", f"Events: {res['events']}", "",
     "## Signed 60-day drift (percent, continuation = positive), by period and size", "",
     "| subset | period | size | n | mean60 | t (date-clustered) | median60 | share positive | mean20 | t20 | gap60 Q5-Q1 | monotonicity | slope | slope t |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for k, v in cells.items():
    a, b, c = [s.strip() for s in k.split("|")]
    L.append(f"| {a} | {b} | {c} | {v['n']} | {fmt(v['mean60'],2)} | {fmt(v['t60'],2)} | {fmt(v['med60'],2)} | {fmt(v['pos60'],1)} | {fmt(v['mean20'],2)} | {fmt(v['t20'],2)} | {fmt(v.get('gap60'),2)} | {fmt(v.get('mono'),2)} | {fmt(v.get('slope'),3)} | {fmt(v.get('slope_t'),2)} |")
L += ["", "## Continuation slope (d60 on first move) by year", "", "| subset | year | size | n | slope | slope t | mean60 | t60 |", "|---|---|---|---|---|---|---|---|"]
for k, v in yr.items():
    a, b, c = [s.strip() for s in k.split("|")]
    L.append(f"| {a} | {b} | {c} | {v['n']} | {fmt(v['slope'],3)} | {fmt(v['slope_t'],2)} | {fmt(v['mean60'],2)} | {fmt(v['t60'],2)} |")
(HERE / "RESULTS.md").write_text("\n".join(L) + "\n")
print("done")
