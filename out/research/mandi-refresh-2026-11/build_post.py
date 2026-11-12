"""Regenerate the data blocks of the post "India's Biggest Mandi Crops Have the Steadiest Prices..."
(slug indias-biggest-mandi-crops-have) from crop_ranking.py's results JSON.

Usage: python3 build_post.py <results.json> <template.html> <out.html> [--facts facts.json]

The numbers come from india-mandi-arrivals/analysis/workbooks/crop_ranking.py (same method as the
original post). This script only re-renders: the four stat tiles, the scatter chart's points, the
all-India ranking table, the top-12-states table and the state heatmap. Prose is edited separately.
Run it on the October 2026 (to the 23rd) results first: the output blocks must equal the live post's.
"""
import json, math, re, sys, collections

RES, TPL, OUT = sys.argv[1:4]
FACTS = sys.argv[sys.argv.index("--facts") + 1] if "--facts" in sys.argv else None
d = json.load(open(RES)); res, pairs = d["res"], d["pairs"]

SHORT = {"Paddy(Common)": "Paddy", "Soyabean": "Soybean", "Bengal Gram(Gram)(Whole)": "Chana",
         "Red gram/Arhar/Tur(whole)": "Tur", "Green Gram(Moong)(Whole)": "Moong",
         "Black Gram(Urd Beans)(Whole)": "Urad", "Lentil(Masur)(Whole)": "Masur", "Cummin Seed(Jeera)": "Jeera",
         "Dry Chillies": "Dry chilli", "Jowar(Sorghum)": "Jowar", "Bajra(Pearl Millet/Cumbu)": "Bajra",
         "Ragi(Finger Millet)": "Ragi"}
short = lambda c: SHORT.get(c, c)
GROUP = {**{c: "#1c6e8c" for c in ("Paddy", "Wheat", "Maize", "Rice", "Bajra", "Jowar", "Ragi")},
         **{c: "#2b8a3e" for c in ("Chana", "Tur", "Moong", "Urad", "Masur")},
         **{c: "#8a5a12" for c in ("Soybean", "Mustard", "Groundnut", "Cotton")},
         **{c: "#c92a2a" for c in ("Onion", "Potato", "Tomato", "Garlic")},
         **{c: "#7048e8" for c in ("Dry chilli", "Jeera", "Turmeric")}}
STATE = {"Chattisgarh": "Chhattisgarh", "NCT of Delhi": "Delhi"}
ABBR = {"Uttar Pradesh": "UP", "Madhya Pradesh": "MP", "Chhattisgarh": "CG", "Maharashtra": "MH", "Karnataka": "KA",
        "Rajasthan": "RJ", "Gujarat": "GJ", "Haryana": "HR", "Telangana": "TG", "Andhra Pradesh": "AP",
        "West Bengal": "WB", "Delhi": "DL", "Punjab": "PB", "Keralam": "KL", "Kerala": "KL", "Tamil Nadu": "TN",
        "Bihar": "BR", "Odisha": "OD", "Assam": "AS", "Himachal Pradesh": "HP", "Jammu and Kashmir": "JK",
        "Uttarakhand": "UK", "Jharkhand": "JH", "Tripura": "TR", "Chandigarh": "CH"}
sname = lambda s: STATE.get(s, s)

ai = sorted([k for k in res if k.endswith("|All India")], key=lambda k: -res[k]["arr12"])
crops = [k.split("|")[0] for k in ai]
vrank = {c: i + 1 for i, c in enumerate(sorted(crops, key=lambda c: -res[c + "|All India"]["vol"]))}
R = lambda c: res[c + "|All India"]
pct = lambda v: f"{v * 100:.1f}"
total = sum(R(c)["arr12"] for c in crops)

# ---- state aggregates (filtered pairs, as in the original) ----
st_tot = collections.Counter(); st_crops = collections.defaultdict(list)
for k in pairs:
    c, s = k.split("|")
    if s == "All India": continue
    st_tot[s] += res[k]["arr12"]; st_crops[s].append(c)
top12 = [s for s, _ in st_tot.most_common(12)]

facts = {"window_last": d["months"][-1], "total_mt": total / 1e6,
         "ai": {short(c): dict(rank=i + 1, mt=R(c)["arr12"] / 1e6, vol=R(c)["vol"] * 100, vrank=vrank[c],
                               rng=R(c)["rng"] * 100, last=R(c)["last"]) for i, c in enumerate(crops)},
         "states": [dict(state=sname(s), mt=st_tot[s] / 1e6,
                         top=[(short(c), res[f"{c}|{s}"]["arr12"] / 1e6, res[f"{c}|{s}"]["vol"] * 100)
                              for c in sorted(st_crops[s], key=lambda c: -res[f"{c}|{s}"]["arr12"])[:3]]) for s in top12],
         "cell": {f"{short(c)}|{sname(s)}": res[f"{c}|{s}"]["vol"] * 100 for k in pairs
                  for c, s in [k.split("|")] if s != "All India"}}
pw = facts["ai"]["Paddy"]["mt"] + facts["ai"]["Wheat"]["mt"]
facts["paddy_wheat_share"] = pw / facts["total_mt"] * 100; facts["paddy_wheat_mt"] = pw

html = open(TPL, encoding="utf-8").read()
def sub1(pat, new, s, flags=re.S):
    out, n = re.subn(pat, lambda m: new, s, count=1, flags=flags)
    assert n == 1, f"block not found: {pat[:60]}"
    return out

# ---- stat tiles ----
A = facts["ai"]; ratio = A["Tomato"]["vol"] / A["Wheat"]["vol"]
words = {2: "twice", 3: "three times", 4: "four times", 5: "five times", 6: "six times", 7: "seven times",
         8: "eight times", 9: "nine times", 10: "ten times"}
onion_rank = A["Onion"]["rank"]; ordn = {1: "largest", 2: "second-largest", 3: "third-largest", 4: "fourth-largest", 5: "fifth-largest"}
tiles = f'''<div class="gb-stats">
<div class="gb-stat"><b>{facts["paddy_wheat_share"]:.0f}%</b><span>Share of the 23 crops&rsquo; mandi arrivals over the past year taken by paddy and wheat, {pw:.1f} million of {facts["total_mt"]:.0f} million tonnes</span></div>
<div class="gb-stat"><b>{A["Wheat"]["vol"]:.1f}%</b><span>Typical monthly price move for wheat, nationally, since January 2023</span></div>
<div class="gb-stat"><b>{A["Tomato"]["vol"]:.1f}%</b><span>Typical monthly price move for tomato, about {words.get(round(ratio), f"{ratio:.0f} times")} wheat&rsquo;s</span></div>
<div class="gb-stat"><b>{A["Onion"]["vol"]:.1f}%</b><span>Typical monthly move for onion, the {ordn[onion_rank]} crop by arrivals at {A["Onion"]["mt"]:.1f} million tonnes</span></div>
</div>'''
html = sub1(r'<div class="gb-stats">.*?</div>\n</div>', tiles, html)

# ---- scatter: keep each label's offset/anchor from the template, move the points ----
X = lambda v: 1010.43 + 515.61 * math.log10(v)          # fitted to the original chart (max error 0.23 px)
Y = lambda mt: 260.69 - 139.29 * math.log10(mt)
pt_re = re.compile(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="5" fill="(#\w+)"/>\n<text x="([\d.]+)" y="([\d.]+)" '
                   r'font-size="12" fill="#\w+" text-anchor="(\w+)">([^<]+)</text>\n')
old = {m[7]: (float(m[4]) - float(m[1]), float(m[5]) - float(m[2]), m[6]) for m in pt_re.finditer(html)}
assert len(old) == 23, len(old)
pts = ""
for c in crops:
    n = short(c); dx, dy, anc = old[n]; cx, cy = X(R(c)["vol"]), Y(R(c)["arr12"] / 1e6)
    pts += (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="5" fill="{GROUP[n]}"/>\n'
            f'<text x="{cx + dx:.1f}" y="{cy + dy:.1f}" font-size="12" fill="{GROUP[n]}" text-anchor="{anc}">{n}</text>\n')
first = pt_re.search(html).start(); last = list(pt_re.finditer(html))[-1].end()
html = html[:first] + pts + html[last:]

# ---- all-India table ----
rows = "".join(f'<tr><td>{a["rank"]}</td><td>{n}</td><td>{a["mt"]:.2f}</td><td>{a["vol"]:.1f}</td><td>{a["vrank"]}</td>'
               f'<td>{a["rng"]:.0f}</td><td>{a["last"]:,.0f}</td></tr>\n' for n, a in A.items())
html = re.sub(r'(<th>Latest price \(Rs/qtl\)</th></tr></thead><tbody>\n).*?(</tbody>)', lambda m: m[1] + rows + m[2], html, count=1, flags=re.S)

# ---- states table ----
cell = lambda t: f"{t[0]} ({t[1]:.1f}, {t[2]:.1f})"
rows = "".join(f'<tr><td>{x["state"]}</td><td>{x["mt"]:.1f}</td>' + "".join(f"<td>{cell(t)}</td>" for t in x["top"])
               + "<td></td>" * (3 - len(x["top"])) + "</tr>\n" for x in facts["states"])
html = re.sub(r'(<th>Third \(Mt, monthly move %\)</th></tr></thead><tbody>\n).*?(</tbody>)', lambda m: m[1] + rows + m[2], html, count=1, flags=re.S)

# ---- heatmap ----
def colour(v):
    if v < 2.5: return "#2b8a3e", "#ffffff"
    if v < 4: return "#8ce99a", "#212529"
    if v < 8: return "#ffec99", "#212529"
    if v < 15: return "#ffa94d", "#212529"
    return "#e03131", "#ffffff"
cols = ["All India"] + top12
hm = ""
for j, s in enumerate(cols):
    lab = "India" if s == "All India" else ABBR[sname(s)]
    hm += (f'<text x="{118 + 46 * j:.1f}" y="32" font-size="12" font-weight="{700 if j == 0 else 400}" fill="#212529" '
           f'text-anchor="middle">{lab}</text>\n')
for i, c in enumerate(sorted(crops, key=lambda c: (R(c)["vol"]))):
    y = 42 + 22 * i; hm += f'<text x="88" y="{y + 15}" font-size="12" fill="#212529" text-anchor="end">{short(c)}</text>\n'
    for j, s in enumerate(cols):
        x = 96 + 46 * j; k = f"{c}|{s}"
        if k in pairs or s == "All India":
            v = res[k]["vol"] * 100; bg, fg = colour(v)
            hm += (f'<rect x="{x}" y="{y}" width="44" height="20" fill="{bg}"/>\n'
                   f'<text x="{x + 22:.1f}" y="{y + 14}" font-size="10.5" fill="{fg}" text-anchor="middle">{v:.1f}</text>\n')
        else:
            hm += f'<rect x="{x}" y="{y}" width="44" height="20" fill="#f1f3f5"/>\n'
html = re.sub(r'(<rect x="0" y="0" width="704" height="588" fill="#ffffff"/>\n).*?(<rect x="96" y="564")',
              lambda m: m[1] + hm + m[2], html, count=1, flags=re.S)
names = ", ".join(f"{ABBR[sname(s)]} {sname(s)}" for s in top12)
html = re.sub(r"(Grey = the crop is not traded in that state&rsquo;s mandis at scale, or its data is too thin\. ).*?(\. Source)",
              lambda m: m[1] + names + m[2], html, count=1)

open(OUT, "w", encoding="utf-8").write(html)
if FACTS: json.dump(facts, open(FACTS, "w"), indent=1)
print("wrote", OUT, "| total", f"{facts['total_mt']:.1f} Mt", "| paddy+wheat", f"{facts['paddy_wheat_share']:.1f}%")
