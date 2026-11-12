#!/usr/bin/env python3
"""CPI heatmap post, rebuilt for October 2026 (12 Nov 2026).

Reads cpi_2026_jun_sep_oct.json (MoSPI CPI base 2024, fetched via the MoSPI MCP connector) and
out/update-2026-11-10-cpi-inflation-heatmap-india-june-2026.html (live post + Phase 1 link fix), and writes
out/update-2026-11-12-cpi-inflation-heatmap-india-june-2026.html.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SRC = ROOT / "out/research/cpi-heatmap/base_2026-11-10.html"  # live post + Phase 1 link fix
OUT = ROOT / "out/update-2026-11-12-cpi-inflation-heatmap-india-june-2026.html"
D = json.load(open(HERE / "cpi_2026_jun_sep_oct.json"))
S = D["states_general_yoy"]
DIV = D["all_india_division_yoy_oct2026"]
AI = S["All India"]

# MoSPI state name -> map id and display name
MAPID = {"Andaman And Nicobar Islands": ("IN-AN", "Andaman and Nicobar Islands"), "Andhra Pradesh": ("IN-AP", None),
         "Arunachal Pradesh": ("IN-AR", None), "Assam": ("IN-AS", None), "Bihar": ("IN-BR", None),
         "Chandigarh": ("IN-CH", None), "Chhattisgarh": ("IN-CG", None), "Goa": ("IN-GA", None), "Gujarat": ("IN-GJ", None),
         "Haryana": ("IN-HR", None), "Himachal Pradesh": ("IN-HP", None), "Jammu And Kashmir": ("IN-JK", "Jammu and Kashmir"),
         "Jharkhand": ("IN-JH", None), "Karnataka": ("IN-KA", None), "Kerala": ("IN-KL", None), "Ladakh": ("IN-LK", None),
         "Lakshadweep": ("IN-LD", None), "Madhya Pradesh": ("IN-MP", None), "Maharashtra": ("IN-MH", None),
         "Manipur": ("IN-MN", None), "Meghalaya": ("IN-ML", None), "Mizoram": ("IN-MZ", None), "Nagaland": ("IN-NL", None),
         "NCT of Delhi": ("IN-DL", "Delhi"), "Odisha": ("IN-OD", None), "Puducherry": ("IN-PY", None), "Punjab": ("IN-PB", None),
         "Rajasthan": ("IN-RJ", None), "Sikkim": ("IN-SK", None), "Tamil Nadu": ("IN-TN", None), "Telangana": ("IN-TS", None),
         "The Dadra And Nagar Haveli And Daman And Diu": ("IN-DH", "Dadra and Nagar Haveli and Daman and Diu"),
         "Tripura": ("IN-TR", None), "Uttar Pradesh": ("IN-UP", None), "Uttarakhand": ("IN-UK", None), "West Bengal": ("IN-WB", None)}
NAME = {k: (v[1] or k) for k, v in MAPID.items()}
# States with population above 50 lakh (Census 2011), the cut MoSPI's own release uses for its state rankings
MAJOR = ["Andhra Pradesh", "Assam", "Bihar", "Chhattisgarh", "NCT of Delhi", "Gujarat", "Haryana", "Himachal Pradesh",
         "Jammu And Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Odisha", "Punjab",
         "Rajasthan", "Tamil Nadu", "Telangana", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
assert set(MAPID) == set(S) - {"All India"} and len(MAPID) == 36

NOTE = ('<div class="warn" style="border-left:4px solid #a5402c;background:rgba(165,64,44,.07);padding:.8em 1em;'
        'margin:1.2em 0;border-radius:4px"><b>Updated 12 November 2026.</b> {}</div>')


def pct(v):
    return f"{v:.2f}%"


def x_of(v, x0=230, per=43.425):
    return x0 + v * per


def bar_svg(rows, title, sub, ref_label, ref_val, caption_aria, label_w=220, row_h=22, band=None):
    """Horizontal bars, 0-11% (or wider), with a dashed reference line and an optional shaded band."""
    vmax = max(11.0 if max(v for _, v in rows) > 8 else 8.0, 0)
    per = (640 - 230) / vmax
    top = 78
    h = top + len(rows) * row_h + 70
    o = [f'<svg role="img" aria-label="{caption_aria}" style="width:100%;height:auto;max-width:700px;display:block;margin:0 auto" '
         f'viewBox="0 0 700 {h}" xmlns="http://www.w3.org/2000/svg" font-family="Georgia, \'Times New Roman\', serif">',
         f'  <rect x="0" y="0" width="700" height="{h}" fill="#f8f9fa" />',
         f'  <text x="30" y="34" font-size="19" font-weight="700" fill="#1a1a1a">{title}</text>',
         f'  <text x="30" y="54" font-size="12.5" fill="#555">{sub}</text>']
    if band is not None:
        bx = 230 + band * per
        o.append(f'  <rect x="{bx:.1f}" y="{top - 6}" width="{640 - bx:.1f}" height="{len(rows) * row_h + 6}" fill="#c0392b" fill-opacity=".07" />')
        o.append(f'  <text x="636" y="{top + len(rows) * row_h + 14}" font-size="10.5" fill="#a5402c" text-anchor="end">shaded: above the RBI&#8217;s 6% upper limit</text>')
    o.append('  <g stroke="#ddd" stroke-width="1">')
    step = 2
    ticks = [t for t in range(0, int(vmax) + 1, step)]
    for t in ticks:
        o.append(f'    <line x1="{230 + t * per:.1f}" y1="{top - 6}" x2="{230 + t * per:.1f}" y2="{top + len(rows) * row_h}" />')
    o.append('  </g>')
    o.append('  <g font-size="10.5" fill="#777" text-anchor="middle">')
    for t in ticks:
        o.append(f'    <text x="{230 + t * per:.1f}" y="{top + len(rows) * row_h + 30}">{t}%</text>')
    o.append('  </g>')
    rx = 230 + ref_val * per
    o.append(f'  <line x1="{rx:.1f}" y1="{top - 10}" x2="{rx:.1f}" y2="{top + len(rows) * row_h + 2}" stroke="#0b5794" stroke-width="1.6" stroke-dasharray="4,3" />')
    o.append(f'  <text x="{rx:.1f}" y="{top - 14}" font-size="11" fill="#0b5794" text-anchor="middle" font-weight="700">{ref_label}</text>')
    o.append('  <g font-size="12.5">')
    for i, (lab, v) in enumerate(rows):
        y = top + i * row_h
        col = "#c0392b" if v > ref_val else "#2b6cb0"
        o.append(f'    <text x="{label_w}" y="{y + 13}" text-anchor="end" fill="#1a1a1a">{lab}</text>')
        o.append(f'    <rect x="230" y="{y + 2}" width="{max(v, 0) * per:.1f}" height="{row_h - 6}" fill="{col}" />')
        o.append(f'    <text x="{230 + max(v, 0) * per + 5:.1f}" y="{y + 14}" fill="#1a1a1a">{pct(v)}</text>')
    o.append('  </g>')
    ly = top + len(rows) * row_h + 44
    o.append(f'  <g font-size="11" fill="#555">\n    <rect x="230" y="{ly}" width="12" height="12" fill="#c0392b" />'
             f'\n    <text x="247" y="{ly + 10}">Above {ref_label.split(" ")[0]}</text>'
             f'\n    <rect x="420" y="{ly}" width="12" height="12" fill="#2b6cb0" />'
             f'\n    <text x="437" y="{ly + 10}">Below {ref_label.split(" ")[0]}</text>\n  </g>')
    o.append('</svg>')
    return "\n".join(o)


t = SRC.read_text()
n0 = len(t)

# ---- numbers used in the text
maj = sorted(MAJOR, key=lambda s: -S[s]["oct"])
allst = sorted(MAPID, key=lambda s: -S[s]["oct"])
above6 = [s for s in allst if S[s]["oct"] > 6]
above6_maj = [s for s in maj if S[s]["oct"] > 6]
below4 = [s for s in allst if S[s]["oct"] < 4]
rise = sorted(MAPID, key=lambda s: -(S[s]["oct"] - S[s]["jun"]))
fell = [s for s in MAPID if S[s]["oct"] < S[s]["sep"]]
fmt = lambda s: f"{NAME[s]} ({pct(S[s]['oct'])})"
spread_maj = S[maj[0]]["oct"] - S[maj[-1]]["oct"]
print("above 6:", len(above6), [NAME[s] for s in above6]); print("major above 6:", len(above6_maj))
print("below 4:", [fmt(s) for s in below4]); print("top risers since June:", [(NAME[s], round(S[s]['oct'] - S[s]['jun'], 2)) for s in rise[:6]])
print("fell Sep->Oct:", [(NAME[s], S[s]['sep'], S[s]['oct']) for s in fell])

# ---- dek
t = t.replace('<p style="order:4" class="dek">Combined-sector CPI, year-on-year inflation by state, June 2026, shaded low to high against the scale below. The All-India rate is 4.38%.</p>',
              f'<p style="order:4" class="dek">Combined-sector CPI, year-on-year inflation for all 28 states and 8 union territories, October 2026, shaded low to high against the scale below. '
              f'The All-India rate is {pct(AI["oct"])}, above the RBI&#8217;s 6% upper limit for the first time since October 2024.</p>', 1)

# ---- state bar chart (major states)
rows = [(NAME[s], S[s]["oct"]) for s in maj]
svg = bar_svg(rows, "CPI: year-on-year inflation by state, October 2026",
              "The 22 states with more than 50 lakh people (Census 2011), ranked hottest to coolest",
              f"All-India {pct(AI['oct'])}", AI["oct"],
              f"Bar chart of year-on-year CPI inflation in October 2026 for India's 22 largest states, from {fmt(maj[0])} to {fmt(maj[-1])}; the All-India rate is {pct(AI['oct'])}.",
              band=6.0)
t, n = re.subn(r'<svg role="img" style="width:100%;height:auto;max-width:700px[^>]*viewBox="0 0 700 460".*?</svg>', lambda m: svg, t, count=1, flags=re.S)
assert n == 1
t = t.replace("CPI year-on-year inflation by state, June 2026 (13 of 28 states tracked). Source: MoSPI, via the post.",
              "CPI year-on-year inflation, October 2026 (provisional), for the 22 states with more than 50 lakh people. The map below shows all 36 states and union territories. Source: MoSPI CPI, base 2024.", 1)

# ---- map
mapdata = {MAPID[s][0]: {"name": NAME[s], "yoy": S[s]["oct"]} for s in MAPID}
t, n = re.subn(r'"data":\s*\{.*?\}\}', lambda m: '"data": ' + json.dumps(mapdata) , t, count=1, flags=re.S)
assert n == 1, n
lo, hi = min(v["yoy"] for v in mapdata.values()), max(v["yoy"] for v in mapdata.values())
mz = min(mapdata.values(), key=lambda v: v["yoy"])["name"]; mx = max(mapdata.values(), key=lambda v: v["yoy"])["name"]
t = t.replace('aria-label="Choropleth map of India shading 13 states by year-on-year CPI inflation for June 2026, from 2.96 per cent in Delhi to 6.36 per cent in Telangana."',
              f'aria-label="Choropleth map of India shading all 36 states and union territories by year-on-year CPI inflation for October 2026, from {lo:.2f} per cent in {mz} to {hi:.2f} per cent in {mx}."', 1)
t = t.replace('<div class="card-title">YoY inflation, Jun 2026</div>', '<div class="card-title">YoY inflation, Oct 2026</div>', 1)
t = t.replace('<div class="legend-scale"><span>2.96%</span><span>4.65%</span><span>6.36%</span></div>',
              f'<div class="legend-scale"><span>{lo:.2f}%</span><span>{(lo + hi) / 2:.2f}%</span><span>{hi:.2f}%</span></div>', 1)
t, n = re.subn(r'\s*<div class="legend-nodata">.*?</div>\n', "\n", t, count=1, flags=re.S)
assert n == 1
t = t.replace("<p><b>13 of 28 states</b> are tracked in this dataset (see the earlier CPI/WPI trend chart); the rest have no reading here, not necessarily low inflation.</p>",
              "<p><b>All 28 states and 8 union territories</b> have a reading. The smallest of them rest on fewer price quotations, so read their figures with more caution than the large states&#8217;.</p>", 1)

# ---- update note (replaces the 26 Oct note and its September table)
note = NOTE.format(
    f"Rebuilt for October 2026, MoSPI&rsquo;s latest release (provisional, published 12 November). All-India CPI inflation rose to {pct(AI['oct'])} from {pct(AI['sep'])} in September and {pct(AI['jun'])} in June, "
    f"above the RBI&rsquo;s 6% upper tolerance limit for the first time since October 2024; food inflation was 8.94%. "
    f"<b>Corrections.</b> This post said only 13 of 28 states were tracked in MoSPI&rsquo;s state release. That was wrong: the release covers all 28 states and 8 union territories every month, and the original build had fetched 13 of them. "
    f"The map and chart now show every state and union territory. The post also said a single month above 6% would oblige the RBI to explain the miss; that obligation applies only when average inflation stays outside the 2&ndash;6% band for three consecutive quarters.")
t, n = re.subn(r'<div class="warn"[^>]*><b>Updated 26 October 2026\.</b>.*?</table></div></div>', lambda m: note, t, count=1, flags=re.S)
assert n == 1, n

# ---- section 1: spread
sec1_old = re.search(r'<h2 style="font-size:1.25em">A 3\.4-point spread, and what it hides</h2>.*?(?=\s*<h2 style="font-size:1.25em">The map\'s biggest limitation)', t, re.S)
assert sec1_old
south = ["Tamil Nadu", "Telangana", "Andhra Pradesh", "Karnataka", "Kerala"]
sec1 = f'''<h2 style="font-size:1.25em">A {spread_maj:.1f}-point spread among the big states</h2>
      <p>Among the 22 states with more than 50 lakh people, October&rsquo;s readings run from {fmt(maj[0])} down to {fmt(maj[-1])}, a {spread_maj:.1f}-point spread on the same combined-CPI series, in the same month, under the same method. The hottest six are close together: {", ".join(fmt(s) for s in maj[:6])}. Each is about a point or more above the All-India rate. The coolest large states are {", ".join(fmt(s) for s in maj[-6:][::-1][:-1])} and {fmt(maj[-6])}.</p>
      <p>The southern pattern this map showed in June still holds: {", ".join(NAME[s] for s in south[:-1])} and {NAME[south[-1]]} are all above the national rate. What changed is that it is no longer only southern. Madhya Pradesh and Odisha, which the first version of this map left grey, sit in the same 7%-plus group, and Uttar Pradesh ({pct(S["Uttar Pradesh"]["oct"])}) is above the national rate too. The North-East and Delhi are the cool end: {", ".join(fmt(s) for s in ["Mizoram", "Meghalaya", "Nagaland"])} and Delhi at {pct(S["NCT of Delhi"]["oct"])}.</p>
      <p>Counting every state and union territory, the range is wider, from {fmt(allst[-1])} to {fmt(allst[0])}, with Dadra and Nagar Haveli and Daman and Diu next at {pct(S["The Dadra And Nagar Haveli And Daman And Diu"]["oct"])}. Those extremes are small territories, where fewer price quotations stand behind each index, so the large-state spread is the safer comparison.</p>
      <p>Since June the biggest rises have come in {", ".join(f"{NAME[s]} (up {S[s]['oct'] - S[s]['jun']:.2f} points)" for s in rise[:3])} and {NAME[rise[3]]} (up {S[rise[3]]['oct'] - S[rise[3]]['jun']:.2f} points). Between September and October, {len(fell)} of the 36 fell, among them Andaman and Nicobar Islands ({pct(S["Andaman And Nicobar Islands"]["sep"])} to {pct(S["Andaman And Nicobar Islands"]["oct"])}); the rest rose or held.</p>
      <h2 style="font-size:1.25em">What October&rsquo;s {pct(AI["oct"])} is made of</h2>
      <p>MoSPI&rsquo;s all-India figures by division show where the pressure sits. Three divisions run near or above 10%: personal care and miscellaneous goods ({pct(DIV["Personal care, social protection and miscellaneous goods and services"])}), where jewellery and watches are up 28.00% on the year; restaurants and accommodation ({pct(DIV["Restaurants and accommodation services"])}); and food and beverages ({pct(DIV["Food and beverages"])}, with the food group alone at 8.94%). Inside food, fresh vegetables other than leafy and fruit-bearing kinds are up 48.08%, cane and beet sugar 25.44% and vegetable oils 11.15%, while tubers and cooking bananas are down 14.24%. Transport is at {pct(DIV["Transport"])}, with domestic air fares up 43.23%, diesel 8.41% and petrol 7.51%. Housing and fuel ({pct(DIV["Housing, water, electricity, gas and other fuels"])}) and health ({pct(DIV["Health"])}) are the coolest.</p>
{{DIVSVG}}
      <p>MoSPI&rsquo;s data service has the same division split for every state, but only inside the full item-level series, which runs to about 23,000 rows a month. This edition does not map it. The national split above is what can be said with confidence today.</p>
'''
divrows = sorted(((k.replace("Personal care, social protection and miscellaneous goods and services", "Personal care and misc.")
                   .replace("Housing, water, electricity, gas and other fuels", "Housing, water and fuel")
                   .replace("Furnishings, household equipment and routine household maintenance", "Furnishings and household")
                   .replace("Restaurants and accommodation services", "Restaurants and accommodation")
                   .replace("Paan, tobacco and intoxicants", "Paan, tobacco, intoxicants")
                   .replace("Recreation, sport and culture", "Recreation and culture")
                   .replace("Information and communication", "Information and comms"), v) for k, v in DIV.items()), key=lambda r: -r[1])
divsvg = bar_svg(divrows, "What is driving it: inflation by division, October 2026",
                 "All-India, combined, year on year; MoSPI CPI base 2024 (provisional)",
                 f"General {pct(AI['oct'])}", AI["oct"],
                 f"Bar chart of all-India CPI inflation by the 12 divisions in October 2026, from {pct(max(DIV.values()))} for personal care and miscellaneous goods to {pct(min(DIV.values()))} for health; the general index is {pct(AI['oct'])}.")
fig = ('<figure class="gb-figure" style="margin:1.5rem 0 1.75rem;text-align:center">\n' + divsvg +
       '\n<figcaption style="font-size:.8em;color:#868e96;font-family:-apple-system,\'Segoe UI\',sans-serif;margin-top:.5rem">All-India CPI inflation by division, October 2026 (provisional). Source: MoSPI CPI, base 2024.</figcaption>\n</figure>')
t = t[:sec1_old.start()] + sec1.replace("{DIVSVG}", fig) + t[sec1_old.end():]

# ---- section 2: coverage
sec2_old = re.search(r'<h2 style="font-size:1.25em">The map\'s biggest limitation is what it doesn\'t show</h2>\s*<p>Only 13 of India.*?</p>', t, re.S)
assert sec2_old
sec2 = ('<h2 style="font-size:1.25em">What the map can and cannot tell you</h2>\n'
        '      <p>Every state and union territory now has a reading; there are no grey &ldquo;unknown&rdquo; states. The limit is now sample size. MoSPI collects prices from 1,407 urban markets and 1,465 villages across the country, so a small territory&rsquo;s index rests on far fewer quotations than Uttar Pradesh&rsquo;s or Maharashtra&rsquo;s. MoSPI itself warns that state-level item indices &ldquo;should be interpreted and used with caution&rdquo; because some are compiled from thin samples. Read Puducherry&rsquo;s or Mizoram&rsquo;s figure as a signal, not a precise rate.</p>')
t = t[:sec2_old.start()] + sec2 + t[sec2_old.end():]
t = t.replace("useful for seeing whether June's 4.38% All-India rate is accelerating or cooling, a question this single-month state map can't answer on its own.",
              f"useful for seeing how the national rate climbed from {pct(AI['jun'])} in June to {pct(AI['oct'])} in October, a trend this single-month state map can't show on its own.", 1)

# ---- section 3: RBI band
sec3_old = re.search(r'(<h2 style="font-size:1.25em">Reading these numbers against the RBI\'s own target band</h2>)\s*<p>.*?</p>\s*<p>.*?</p>', t, re.S)
assert sec3_old
sec3 = (sec3_old.group(1) + "\n"
        f'      <p>The Reserve Bank of India&rsquo;s inflation-targeting mandate sets a CPI target of 4%, with a tolerance band of 2&ndash;6%. In October the national rate itself left the band: {pct(AI["oct"])} is the first reading above 6% since October 2024. '
        f'One month outside the band is not, on its own, a failure under the Monetary Policy Framework; that is defined as average inflation above the upper limit (or below the lower one) for three consecutive quarters, at which point the RBI must report to the government on why. '
        f'No month of the July&ndash;September quarter was above 6% (September was {pct(AI["sep"])}), so the earliest a failure could be recorded is after June 2027, and only if the October&ndash;December, January&ndash;March and April&ndash;June quarters all average above 6%.</p>\n'
        f'      <p>State by state, {len(above6)} of the 36 states and union territories are above 6%, including {len(above6_maj)} of the 22 large states: {", ".join(NAME[s] for s in above6_maj[:-1])} and {NAME[above6_maj[-1]]}. None is below the 2% floor. '
        f'Only {len(below4)} are below the 4% target: {", ".join(fmt(s) for s in below4[:-1])} and {fmt(below4[-1])}. '
        f'The RBI sets one policy rate for the whole country on the national print, so a household in Tamil Nadu living with {pct(S["Tamil Nadu"]["oct"])} and one in Delhi living with {pct(S["NCT of Delhi"]["oct"])} get the same rate decision, calibrated to {pct(AI["oct"])}. '
        f'That gap was there in June too; October&rsquo;s difference is that the national number has caught up with the hot states rather than the other way round.</p>')
t = t[:sec3_old.start()] + sec3 + t[sec3_old.end():]

# ---- What would fix this
fx_old = re.search(r'<li><b>MoSPI should publish a combined CPI reading for every state.*?</li>\s*<li><b>MoSPI should publish state-level CPI by commodity group.*?</li>', t, re.S)
assert fx_old
fx = ('<li><b>MoSPI should add a division-level option to the CPI API</b>, returning one row per state and division, so a state-by-division heatmap does not require paging through about 23,000 item rows a month. The state-wise division table could also go into the monthly release as an annexure.</li>\n'
      '<li><b>MoSPI should publish the number of price quotations behind each state&rsquo;s general index</b>, so readers can tell how much weight a small territory&rsquo;s reading, such as Puducherry&rsquo;s 7.96% in October 2026, can bear.</li>')
t = t[:fx_old.start()] + fx + t[fx_old.end():]
t = t.replace("such as Telangana above the band in June 2026, is officially on record.",
              f"such as Tamil Nadu at {pct(S['Tamil Nadu']['oct'])} in October 2026, is officially on record.", 1)

# ---- restore the map's styles (stripped from the live post in August; without them the map renders black)
MAPCSS = """<style>
:root{--ramp-lo:#86b6ef;--ramp-hi:#0d366b}
.bulletin .layout{display:grid;grid-template-columns:minmax(0,1.55fr) minmax(220px,.9fr);gap:28px;align-items:start;margin:1.2rem 0}
@media (max-width:720px){.bulletin .layout{grid-template-columns:1fr}}
.bulletin .map-card{background:#fcfcfa;border:1px solid #c3c7b8;padding:16px;position:relative}
.bulletin .map-card svg{width:100%;height:auto;display:block}
.bulletin .state-path{stroke:#fcfcfa;stroke-width:.75}
.bulletin .state-path.is-hover{filter:brightness(1.12);stroke-width:1.4}
.bulletin .state-path.no-data{fill:#d7d9cd}
.bulletin .tooltip{position:absolute;pointer-events:none;background:#14180f;color:#fcfcfa;font:11.5px/1.5 Menlo,Consolas,monospace;padding:7px 10px;border-radius:2px;opacity:0;transition:opacity .08s ease;white-space:nowrap;z-index:5}
.bulletin .side{display:flex;flex-direction:column;gap:20px}
.bulletin .legend-card,.bulletin .rank-card,.bulletin .note-card{background:#fcfcfa;border:1px solid #c3c7b8;padding:16px 18px}
.bulletin .card-title{font:10.5px Menlo,Consolas,monospace;text-transform:uppercase;letter-spacing:.08em;color:#5f6357;margin-bottom:12px}
.bulletin .legend-bar{height:12px;border-radius:1px;background:linear-gradient(to right,var(--ramp-lo),var(--ramp-hi))}
.bulletin .legend-scale{display:flex;justify-content:space-between;font:11px Menlo,Consolas,monospace;color:#4f5348;margin-top:6px}
.bulletin .rank-row{display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-bottom:1px solid #d7dace;font-size:12.5px;gap:8px}
.bulletin .rank-row:last-child{border-bottom:none}
.bulletin .rank-name{display:flex;align-items:center;gap:8px}
.bulletin .rank-dot{width:9px;height:9px;border-radius:2px;flex-shrink:0}
.bulletin .rank-val{font-family:Menlo,Consolas,monospace;font-variant-numeric:tabular-nums;font-weight:600;white-space:nowrap}
.bulletin .note-card{border-left:3px solid #a5402c}
.bulletin .note-card p{margin:0 0 8px;font-size:12.5px;line-height:1.55;color:#4f5348}
.bulletin .note-card p b{color:#14180f}
</style>
"""
assert t.count('<div class="bulletin">') == 1
t = t.replace('<div class="bulletin">', MAPCSS + '<div class="bulletin">', 1)
t = t.replace(' &middot; states without a tracked reading shown in gray', '', 1).replace(' · states without a tracked reading shown in gray', '', 1)

SRCP = ('<p class="sources" style="font-size:.85em;color:#555"><b>Sources.</b> State and division figures: MoSPI CPI data service (api.mospi.gov.in, base 2024, combined), '
        'fetched 12 November 2026; the data and build script are in this blog&rsquo;s repository under out/research/cpi-heatmap/. '
        '<a href="https://www.pib.gov.in/PressReleaseDetail.aspx?PRID=2335416">MoSPI press release, CPI for October 2026</a> (PIB, 12 November 2026); '
        '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2322244&amp;reg=3&amp;lang=1">MoSPI press release, CPI for September 2026</a> (PIB, 12 October 2026), for the 1,407 markets and 1,465 villages and the caution on thin state samples; '
        '&ldquo;first time since October 2024&rdquo;: <a href="https://english.mathrubhumi.com/news/money/retail-inflation-rises-october-breaches-rbi-limit-ptiaoebaftt">PTI, 12 November 2026</a>.</p>\n')
k = '<p>These are proposals from this blog, not recommendations any agency has adopted.</p>'
assert t.count(k) == 1
t = t.replace(k, k + '\n' + SRCP, 1)

OUT.write_text(t)
left = [w for w in ("June 2026", "13 of 28", "Jun 2026", "4.65%") if w in t]
print(f"wrote {OUT.relative_to(ROOT)} ({n0} -> {len(t)} bytes); June mentions left: {left}")
