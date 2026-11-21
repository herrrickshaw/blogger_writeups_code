"""Mandi harvest discount: how far below its 12-month price trend each crop sells in the months its arrivals peak.
Build from the repo root:
    python3 out/research/mandi-harvest-2026-11/harvest.py <india-mandi-arrivals>/data/agmarknet/state_monthly.csv.gz <h.json> --end 2026-10
    python3 out/research/mandi-harvest-2026-11/build_harvest_post.py <h.json> <state_monthly.csv.gz> [--facts facts.json]
writes out/post-india-mandi-harvest-discount.html. Data: Agmarknet dashboard API, state-wise price and arrival report,
January 2019 to 31 October 2026, as committed in herrrickshaw/india-mandi-arrivals (commit 8fe49e6; November 2026 rows are excluded).
"""
import html as _h
import json
import pathlib
import re
import sys
import time

import pandas as pd

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

HJ, SRC = sys.argv[1:3]
FACTS = sys.argv[sys.argv.index("--facts") + 1] if "--facts" in sys.argv else None
OUT = ROOT / "out/post-india-mandi-harvest-discount.html"
B = "https://blog.vertistratsolution.com"
STEPS = 6


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n) if n else 0:.1f}s left)", flush=True)


HEADS = []


def H(t):
    HEADS.append(t)
    return t


MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SHORT = {"Paddy(Common)": "Paddy", "Soyabean": "Soybean", "Bengal Gram(Gram)(Whole)": "Chana",
         "Red gram/Arhar/Tur(whole)": "Tur", "Green Gram(Moong)(Whole)": "Moong", "Black Gram(Urd Beans)(Whole)": "Urad",
         "Lentil(Masur)(Whole)": "Masur", "Cummin Seed(Jeera)": "Jeera", "Dry Chillies": "Dry chilli",
         "Jowar(Sorghum)": "Jowar", "Bajra(Pearl Millet/Cumbu)": "Bajra", "Ragi(Finger Millet)": "Ragi"}
sh = lambda c: SHORT.get(c, c)
STATE = {"Chattisgarh": "Chhattisgarh", "NCT of Delhi": "Delhi"}
sn = lambda s: STATE.get(s, s)
p1 = lambda x: round(x * 100, 1)                      # fraction -> percent, one decimal (charts print this exact value)
txt = lambda x: f"{abs(x) * 100:.1f}"                 # magnitude for prose
sgn = lambda x: f"{x * 100:+.1f}".replace("-", "&minus;")


def months_txt(ms):
    """Peak months in circular order: [1, 11, 12] -> 'Nov&ndash;Jan'; a non-contiguous set is listed."""
    ms = sorted(ms)
    for k in range(len(ms)):
        rot = ms[k:] + ms[:k]
        if all((rot[i + 1] - rot[i]) % 12 == 1 for i in range(len(rot) - 1)):
            return f"{MON[rot[0] - 1]}&ndash;{MON[rot[-1] - 1]}"
    return ", ".join(MON[m - 1] for m in ms)


# ---- 1. load and value ----
step(1, "loading harvest results and valuing the past year's arrivals")
r = json.load(open(HJ)); END, R = r["end"], r["res"]
assert END == "2026-10", END
d = pd.read_csv(SRC)
start12 = (pd.Period(END, "M") - 11).strftime("%Y-%m")
y = d[(d.month >= start12) & (d.month <= END) & (d.arrivals_t >= 50) & d.price_rs_qtl.notna()]
val = (y.price_rs_qtl * 10 * y.arrivals_t).groupby(y.commodity).sum()          # Rs/qtl x 10 = Rs/t; x t = Rs
A = {}
for k, v in R.items():
    c, s = k.split("|")
    if s == "All India":
        A[sh(c)] = dict(v, crop=c, value_cr=val[c] / 1e7, cost_cr=-v["discount"] * val[c] / 1e7)
assert len(A) == 23, len(A)
order = sorted(A, key=lambda n: A[n]["discount"])
losers = [n for n in order if A[n]["cost_cr"] > 0]
total_cost = sum(A[n]["cost_cr"] for n in losers)
total_value = sum(a["value_cr"] for a in A.values())
assert len(losers) == 18 and 7250 <= total_cost < 7350, (len(losers), total_cost)
TOT = f"{round(total_cost, -2):,.0f}"                 # "7,300"
So, Mu, Wh, Pa, On, Ga, Po = (A[n] for n in ("Soybean", "Mustard", "Wheat", "Paddy", "Onion", "Garlic", "Potato"))
Rk = lambda c, s: R[f"{c}|{s}"]
hp = Rk("Potato", "Haryana")
top4 = sorted(losers, key=lambda n: -A[n]["cost_cr"])[:4]
assert set(top4) == {"Wheat", "Soybean", "Onion", "Mustard"}, top4
share4 = sum(A[n]["cost_cr"] for n in top4) / total_cost
assert share4 > 0.5, share4

# ---- 2. charts ----
step(2, "drawing charts")
deep = order[:4]
assert deep == ["Garlic", "Mustard", "Soybean", "Onion"], deep
c1 = bars(H("Garlic, mustard, soybean and onion sell 3.1 to 4.5% below trend at harvest"),
          [(n, p1(A[n]["discount"])) for n in order], unit="%", accent=deep,
          sub="Price fetched by the average tonne of mandi arrivals, against the 12-month price trend, all-India",
          source="Agmarknet, January 2019 to October 2026; this blog&rsquo;s calculations")
assert p1(On["discount"]) == -3.1 and p1(Ga["discount"]) == -4.5
n1 = numbers(["Crop", "Peak arrival months", "Share of year&rsquo;s arrivals in them (%)", "Price in peak months vs trend (%)",
              "Average tonne vs trend (%)", "Cheapest month", "Dearest month"],
             [[n, months_txt(A[n]["peak"]), f'{A[n]["peak_share"] * 100:.0f}', sgn(A[n]["peak_index"]), sgn(A[n]["discount"]),
               MON[A[n]["cheapest"] - 1], MON[A[n]["dearest"] - 1]] for n in order])

SEL = ["Paddy", "Wheat", "Maize", "Cotton", "Chana", "Tur", "Mustard", "Soybean", "Garlic", "Potato", "Onion"]
c2 = bars(H("In peak months paddy sells 5.3% above trend, wheat 2.9% below, soybean 6.3% below"),
          [(n, p1(A[n]["peak_index"]), months_txt(A[n]["peak"])) for n in sorted(SEL, key=lambda n: -A[n]["peak_index"])],
          unit="%", accent=["Paddy", "Wheat"],
          sub="Price in each crop&rsquo;s three largest-arrival months, against its 12-month trend, all-India",
          source="Agmarknet, January 2019 to October 2026; this blog&rsquo;s calculations")
assert (p1(Pa["peak_index"]), p1(Wh["peak_index"]), p1(So["peak_index"])) == (5.3, -2.9, -6.3)

PAIRS = sorted([(k, v) for k, v in R.items() if not k.endswith("|All India") and v["arr_last12"] >= 5e5], key=lambda kv: kv[1]["discount"])
sel = PAIRS[:10] + [kv for kv in PAIRS if kv[1]["discount"] > 0.02]
lab = lambda k: f"{sh(k.split('|')[0])}, {sn(k.split('|')[1])}"
assert lab(sel[0][0]) == "Potato, Haryana" and p1(hp["discount"]) == -16.5
c3 = bars(H("Potato in Haryana sells 16.5% below trend, the deepest of large state crops"),
          [(lab(k), p1(v["discount"]), f'{v["arr_last12"] / 1e6:.2f} Mt') for k, v in sel], unit="%", accent="Potato, Haryana",
          sub="Average tonne against trend; state-crop pairs with at least 0.5 million tonnes of arrivals, November 2025 to October 2026",
          source="Agmarknet; this blog&rsquo;s calculations")
n3 = numbers(["Crop, state", "Arrivals, past year (Mt)", "Peak arrival months", "Share in peak months (%)", "Price in peak months vs trend (%)",
              "Average tonne vs trend (%)"],
             [[lab(k), f'{v["arr_last12"] / 1e6:.2f}', months_txt(v["peak"]), f'{v["peak_share"] * 100:.0f}', sgn(v["peak_index"]),
               sgn(v["discount"])] for k, v in PAIRS])

c4 = bars(H(f"The harvest discount on 18 crops adds up to about Rs {TOT} crore a year"),
          [(n, round(A[n]["cost_cr"])) for n in sorted(losers, key=lambda n: -A[n]["cost_cr"])], unit="Rs crore", accent=top4,
          sub="Value of the past year&rsquo;s arrivals times each crop&rsquo;s harvest discount, November 2025 to October 2026",
          source="Agmarknet; this blog&rsquo;s calculations")
n4 = numbers(["Crop", "Value of past year&rsquo;s arrivals (Rs crore)", "Average tonne vs trend (%)", "Discount (Rs crore)"],
             [[n, f'{A[n]["value_cr"]:,.0f}', sgn(A[n]["discount"]), f'{A[n]["cost_cr"]:,.0f}'] for n in order])
assert abs(sum(round(A[n]["cost_cr"]) for n in losers) - total_cost) < 10

# ---- 3. text ----
step(3, "writing text")
TITLE = H(f"Mandi harvest discount in India: 18 of 23 crops sell below trend, about Rs {TOT} crore")
STAND = (f"Agmarknet data for 23 crops, January 2019 to October 2026, shows most crops reaching mandis in the months their price is weakest. "
         f"Soybean, mustard and garlic lose 3.3&ndash;4.5% against trend on the average tonne; paddy gains, because its support price resets at harvest.")
top = top_line([
    (f"Rs {TOT} crore", f" is the gap, over the past year, between what 18 crops&rsquo; mandi arrivals fetched and their trend price, at each crop&rsquo;s usual seasonal pattern."),
    (f"{So['peak_share'] * 100:.0f}%", f" of soybean&rsquo;s arrivals land in {months_txt(So['peak'])}, when its price runs {txt(So['peak_index'])}% below trend."),
    (f"+{Pa['peak_index'] * 100:.1f}%", f" is paddy&rsquo;s price in {months_txt(Pa['peak'])} against trend: the new support price takes effect as the harvest arrives."),
])
assert So["peak_share"] * 100 >= 52.5 and So["peak_share"] * 100 < 53.5

intro = (f'<p>The <a href="{B}/2026/10/indias-biggest-mandi-crops-have.html">previous piece in this series</a> ranked 23 crops by how much reaches '
         f'India&rsquo;s regulated mandis and how much their prices move. This one asks when each crop arrives, and what the price is then. '
         f'A seller who must sell at harvest sells when everyone else does.</p>\n')

s1 = insight(H("Most crops sell below their price trend when arrivals peak"), c1 + n1,
             f"For {len(losers)} of 23 crops the average tonne sold below its trend price, so the timing of sale, not the crop alone, sets part of what a seller gets.",
             "Lenders and warehouse operators should look first at garlic, mustard and soybean, which store well and show the deepest discounts.")
s2 = insight(H("Paddy sells above trend at harvest, where the support price resets"), c2,
             f"Where the government buys at the support price in the harvest weeks, the dip shrinks to {txt(Wh['peak_index'])}% for wheat or reverses for paddy, while soybean in its peak months falls {txt(So["peak_index"])}%.",
             "Support-price purchases of oilseeds would do most in October to December for soybean and March to May for mustard, the months their prices bottom.")
s3 = insight(H("The discount is deepest for vegetables and garlic in single states"), c3 + n3,
             f"A state that harvests one crop in a short window sells it into its own glut, as Haryana does with {hp['peak_share'] * 100:.0f}% of its potato arriving in {months_txt(hp['peak'])}.",
             "Cold-storage capacity is most valuable in such states, and its siting should follow the state-crop pairs at the top of this chart.")
s4 = insight(H(f"The 18 discounts add up to about Rs {TOT} crore over the past year"), c4 + n4,
             f"Wheat, soybean, onion and mustard carry {share4 * 100:.0f}% of the total, wheat through volume, against about Rs {total_value / 1e5:.1f} lakh crore of arrivals across all 23 crops.",
             "Treat the figure as scale, not as money any seller could have banked, because if everyone stored, the seasonal pattern itself would change.")
assert 0.55 <= share4 < 0.65

fixes = (f'<h2 class="gb-h2">{H("What would fix this")}</h2>\n<ol>\n'
         '<li><b>Directorate of Marketing and Inspection:</b> publish a seasonal price index for each crop and state beside the monthly Agmarknet prices.</li>\n'
         '<li><b>Warehousing Development and Regulatory Authority:</b> publish monthly electronic warehouse-receipt issuance by commodity and state, to show whether receipt loans reach the deepest-discount crops.</li>\n'
         '<li><b>Department of Agriculture and Farmers Welfare:</b> report storage projects financed under the Agriculture Infrastructure Fund by district and crop, for comparison with these discounts.</li>\n'
         '<li><b>Commission for Agricultural Costs and Prices:</b> report each support-price crop&rsquo;s harvest-month price against trend in its kharif and rabi price-policy reports.</li>\n'
         '</ol>\n<p><i>These are proposals from this blog, not recommendations any agency has adopted.</i></p>\n')

method = ('<details class="xv-n"><summary>How the harvest discount is measured</summary>'
          '<p>Prices and arrivals are Agmarknet&rsquo;s monthly state figures, January 2019 to October 2026; state-months under 50 tonnes are dropped, '
          'and all-India prices are arrival-weighted. The trend is a centred 12-month moving average. A month&rsquo;s seasonal index is its price over the trend, averaged across years.</p>'
          '<p>A month&rsquo;s arrival share is its average share of a calendar year&rsquo;s arrivals over 2019&ndash;2024, before Agmarknet widened its market coverage in November 2025. '
          'The harvest discount is the arrival-weighted seasonal index, less one. A crop-state needs four years of index for every month.</p>'
          '<p>Rebuilding the index from 2019&ndash;2024 alone moves no crop&rsquo;s discount by more than 2.4 points and changes no sign. '
          'The rupee figures multiply the past year&rsquo;s arrivals, valued at state prices, by the discount.</p></details>\n')
caveats = (f'<h2 class="gb-h2">{H("What this piece could not establish")}</h2>\n'
           '<details class="xv-n"><summary>Limits of the data</summary>'
           '<p>These are wholesale prices at regulated mandis, mixing varieties and grades, not what farmers were paid after commission and transport. '
           'The data does not show who sold, or whether they could have stored.</p>'
           f'<p>Storage costs rent, interest and some loss of weight; the <a href="{B}/2026/10/maize-is-cheapest-in-different-state.html">earlier maize and rice analysis</a> '
           'found the seasonal spread usually did not cover it for those grains. Crops sold outside mandis, or bought directly by government agencies, are undercounted.</p>'
           '<p>November 2026 data, to the 20th, is in the source repository but left out here, because a part-month would distort the 12-month window.</p></details>\n')

body = STYLE + top + intro + s1 + s2 + s3 + s4 + fixes + method + caveats
SOURCES = ('Agmarknet dashboard API (<a href="https://agmarknet.gov.in/">agmarknet.gov.in</a>; endpoint api.agmarknet.gov.in/v1/dashboard-data, '
           'state-wise price and arrival report), 23 commodities, January 2019 to 31 October 2026: wheat, paddy (common), rice, maize, jowar, bajra, ragi, '
           'chana, tur, moong, urad, masur, soybean, mustard, groundnut, cotton, onion, potato, tomato, garlic, dry chillies, turmeric and jeera. '
           'Weighted-average prices in Rs per quintal and arrivals in tonnes, as published. Seasonal indices, arrival shares, harvest discounts and rupee values '
           'are this blog&rsquo;s calculations; data and code are in the <a href="https://github.com/herrrickshaw/india-mandi-arrivals">india-mandi-arrivals</a> repository. '
           'No spreadsheet accompanies this piece. Analysed 21 November 2026. This post is AI-assisted analysis of public data, not investment advice.')
RELATED = [(B + "/2026/10/indias-biggest-mandi-crops-have.html", "Mandi prices in India: vegetables swing 2 to 8 times as much as paddy and wheat"),
           (B + "/2026/10/maize-is-cheapest-in-different-state.html", "Maize and rice prices in India: maize is cheapest in a different state every few months"),
           (B + "/2026/07/the-price-of-grain-msp-msv-and.html", "India's grain prices: 6 administered prices for 1 kg of rice, from MSP to MSV")]

# ---- 4. assemble ----
step(4, "assembling page")
build("Agriculture &middot; Mandi prices &middot; 21 November 2026", TITLE, STAND, body, SOURCES, RELATED, str(OUT))

# ---- 5. checks ----
step(5, "checking output")
html = OUT.read_text()
mine = TITLE + STAND + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
for h in re.findall(r'<h2 class="gb-h2"[^>]*>(.*?)</h2>', body) + re.findall(r'class="xv-t"[^>]*>(.*?)</span>', body):
    HEADS.append(h)
BAD = ("you", "your", "we", "our", "only", "just", "still", "actually", "really", "finally", "nobody")
for h in HEADS:
    p = _h.unescape(h)
    assert len(p) <= 90, (len(p), p)
    assert "?" not in p, p
    assert not any(w in p.lower().replace(",", " ").replace(":", " ").split() for w in BAD), p
for para in re.findall(r"<p>(.*?)</p>", body):
    n = len(re.sub(r"<[^>]+>", "", _h.unescape(para)).split())
    assert n <= 60, (n, para[:80])
if FACTS:
    json.dump({"total_cost_cr": total_cost, "losers": losers, "share_top4": share4, "total_value_cr": total_value,
               "crops": {n: {k: A[n][k] for k in ("discount", "peak_index", "peak_share", "value_cr", "cost_cr")} for n in A}},
              open(FACTS, "w"), indent=1)
step(6, "complete")
print("wrote", OUT.relative_to(ROOT), "| title", len(_h.unescape(TITLE)), "chars | headings checked:", len(HEADS))
