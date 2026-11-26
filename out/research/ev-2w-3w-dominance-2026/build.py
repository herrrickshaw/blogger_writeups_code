"""India's EV sales by vehicle type: two- and three-wheelers by units, by battery energy, by state and by cost per km.
Build from the repo root:  python3 out/research/ev-2w-3w-dominance-2026/build.py   (writes out/post-india-ev-sales-two-three-wheelers-dominate.html)
Arithmetic and consistency checks live in calc.py beside this file (importing it runs them); this file re-asserts every figure it prints.
Analysed 26 November 2026. Opened and read for this piece: the CEEW issue brief (PDF, December 2025), EVreporter (FY26 report page, monthly pages April to
October 2026, a CY2026 penetration page, a state e-2W page), Autocar Pro (FY26 e-2W and FY26 EV analysis, H1 FY27 e-2W, October 2025 analysis), Autocar India (October 2026
electric cars), Inc42, Angel One, Outlook Business (FADA FY26 release; a November 2025 article), the PIB PM E-DRIVE release of 1 October 2026, the blog's own
posts and the vehicle_fuel_mileage repository. Blocked and so NOT read: the CEEW dashboard pages (Cloudflare challenge, not bypassed), the Vahan dashboard (not reachable),
Mercom (network refusal), NewsBytes (403), JMK Research (outside the allowed network)."""
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402
import calc as c  # noqa: E402  (importing runs the asserts)

OUT = ROOT / "out/post-india-ev-sales-two-three-wheelers-dominate.html"
B = "https://blog.vertistratsolution.com"
TITLE = "India's EVs: two- and three-wheelers are 9 in 10 registrations, about half of battery kWh"
assert 55 <= len(TITLE) <= 90, len(TITLE)
T0 = time.time()


def n(x):
    return f"{x:,.0f}"


def lakh(x):
    return f"{x / 1e5:.2f}"


# ---- figures used in prose, each asserted again here so a change in calc.py cannot silently change the text
A26 = c.AP["FY26"]
assert (c.W23_FY26, c.E2W_FY26, c.E3W_FY26, c.EPV_FY26) == (91.1, 57.2, 33.9, 8.1)
assert (c.H1_W23_SH, c.H1_E2W_SH, c.H1_E4W_SH) == (88.7, 62.4, 10.1)
assert (c.OCT_W23_SH, c.OCT_E2W_SH) == (88.2, 63.2)
assert round(c.PEN["e3w"], 1) == 60.9 and round(c.PEN["e2w"], 1) == 6.5 and round(c.PEN["epv"], 1) == 4.2
assert round(c.PEN_RATIO, 1) == 9.3 and round(c.SIZE_RATIO, 1) == 15.7 and round(c.UNIT_RATIO, 2) == 1.69
assert (c.W23_KWH_SH, c.W23_UNIT_SH) == (51.5, 90.5) and round(c.G_TOTAL, 1) == 19.3
assert c.G_SH["e4w"] == 40.4 and c.U_SH["e4w"] == 8.7 and c.G_SH["e2w"] == 22.9 and c.U_SH["e2w"] == 57.7
assert round(min(r[2] for r in c.SCEN_ROWS), 1) == 36.5 and round(max(r[2] for r in c.SCEN_ROWS), 1) == 67.0
assert {k: round(v, 2) for k, v in c.COST.items()} == {"ev": 0.67, "cng": 2.93, "petrol": 5.08}
assert c.TOP5_SH == 51.1 and c.ST_SH["Uttar Pradesh"] == 19.2 and c.TEN_SH == 60.1
assert (c.GAP_E2W, c.GAP_E2W_PCT, c.GAP_TOTAL, c.GAP_TOTAL_PCT) == (70_366, 5.0, 99_146, 4.0)
L5M_GROWTH = round(100 * (c.OCT_C["l5m"] / c.MONTHS["May"][1]["l5m"] - 1))
assert L5M_GROWTH == 55                                             # L5 passenger, May to October 2026, after the L5 subsidy closed on 26 December 2025
OCT_YOY = round(100 * (c.OCT_TOTAL / 234_000 - 1))
assert OCT_YOY == 51
OCT25_PLUS = 234_000                                                 # Outlook Business, article dated 6 November 2025: October 2025
ICE2W_SEP, ICE2W_OCT = round(c.SEP_REVISED["e2w"] / 0.116), round(c.OCT_C["e2w"] / 0.097)
assert (ICE2W_SEP, ICE2W_OCT) == (1_799_345, 2_308_907)              # implied two-wheeler retail from rounded penetration: indicative only

# ------------------------------------------------------------------------------------------------ top line
top = top_line([
    (f"{c.W23_FY26:.0f}%", f" of FY2026 electric registrations were two- or three-wheelers ({n(A26['e2w'] + A26['e3w'])} of {n(A26['total'])}, Autocar Pro from Vahan); EVreporter&rsquo;s April&ndash;September 2026 count gives {c.H1_W23_SH}% as cars gain."),
    (f"{c.PEN_RATIO:.1f}&times;", f" is how much higher e-3W penetration ({c.PEN['e3w']:.1f}%) is than e-2W ({c.PEN['e2w']:.1f}%), yet e-2Ws outsell e-3Ws {c.UNIT_RATIO:.2f} to 1 because {c.SIZE_RATIO:.1f} two-wheelers are sold for each three-wheeler."),
    (f"{c.W23_KWH_SH:.0f}%", f" is the estimated share of FY2026 registered battery energy carried by two- and three-wheelers ({c.G_TOTAL:.1f} GWh in all), against {c.W23_UNIT_SH:.1f}% of units; an estimate, with a range of {min(r[2] for r in c.SCEN_ROWS):.0f}% to {max(r[2] for r in c.SCEN_ROWS):.0f}% across pack-size scenarios."),
])
intro = (f'<p class="gb-note">This piece is about the mix of electric vehicles and why, and does not repeat the volumes and subsidy history in '
         f'<a href="{B}/2026/08/indias-ev-market-single-digit.html">India&rsquo;s EV sales: 12% of vehicles in April&ndash;September, cars in single digits</a>. '
         f'The CEEW-GFC dashboard (National Volume Monitor) was read through four screenshots supplied by the blog&rsquo;s author on 27 November 2026, and the page itself and the Vahan dashboard could not be opened here (see the box at the end), so the monthly figures are from secondary reports of Vahan data and are labelled as such. '
         f'Every conflict between sources is shown, not blended.</p>\n')

# ------------------------------------------------------------------------------------------------ section 1: share of units
rows1 = [("FY2022 (CEEW, lower bound)", c.W23["FY22"], "e-3W L5 not labelled in the chart"),
         ("FY2023 (CEEW, lower bound)", c.W23["FY23"], "e-3W L5 not labelled in the chart"),
         ("FY2024 (CEEW)", c.W23["FY24"], ""),
         ("FY2025 (CEEW)", c.W23["FY25"], "Autocar Pro: 94.0"),
         ("FY2026 (Autocar Pro)", c.W23_FY26, f"EVreporter: {c.W23_EVR_LO} to {c.W23_EVR_HI}"),
         ("April&ndash;September 2026 (EVreporter)", c.H1_W23_SH, "monthly first reports"),
         ("October 2026 (EVreporter, first report)", c.OCT_W23_SH, "")]
assert [r[1] for r in rows1] == [92.9, 93.1, 94.1, 94.1, 91.1, 88.7, 88.2]
chart1 = bars("Two- and three-wheelers: 94.1% of EVs in FY2025, 91.1% in FY2026, 88.7% in H1 FY2027", rows1,
              accent=["FY2026 (Autocar Pro)", "April&ndash;September 2026 (EVreporter)"], unit="%", vmax=100,
              sub="Share of electric registrations that are two- or three-wheelers (e-2W, e-3W, e-rickshaw, e-cart). Rows come from different sources and definitions, shown as published; they are not one continuous series.",
              source="CEEW issue brief, Dec 2025 (Vahan, Telangana excluded); Autocar Pro, 2 and 6 Apr 2026 (Vahan, secondary); EVreporter monthly reports, May to Nov 2026 (Vahan, low-speed e-2W excluded, secondary). Shares computed by this blog.")
# table A: CEEW and Autocar Pro segment counts
tA = [["FY2022", "CEEW", n(c.CEEW_TOTAL["FY22"]), n(c.CEEW_E2W["FY22"]), n(c.CEEW_ERICK["FY22"]), "not labelled", "not labelled", f"{c.W23['FY22']}% or more"],
      ["FY2023", "CEEW", n(c.CEEW_TOTAL["FY23"]), n(c.CEEW_E2W["FY23"]), n(c.CEEW_ERICK["FY23"]), "not labelled", "not labelled", f"{c.W23['FY23']}% or more"],
      ["FY2024", "CEEW", n(c.CEEW_TOTAL["FY24"]), n(c.CEEW_E2W["FY24"]), n(c.CEEW_ERICK["FY24"]), n(c.CEEW_E3W["FY24"]), n(c.CEEW_E4WP["FY24"]), f"{c.W23['FY24']}%"],
      ["FY2025", "CEEW", n(c.CEEW_TOTAL["FY25"]), n(c.CEEW_E2W["FY25"]), n(c.CEEW_ERICK["FY25"]), n(c.CEEW_E3W["FY25"]), n(c.CEEW_E4WP["FY25"]), f"{c.W23['FY25']}%"],
      ["FY2025", "Autocar Pro", n(c.AP["FY25"]["total"]), n(c.AP["FY25"]["e2w"]), f"e-3W incl. e-rickshaw: {n(c.AP['FY25']['e3w'])}", "", "", "94.0%"],
      ["FY2026", "Autocar Pro", n(A26["total"]), n(A26["e2w"]), f"e-3W incl. e-rickshaw: {n(A26['e3w'])}", "", f"e-PV {n(A26['epv'])}; e-CV {n(A26['ecv'])}", f"{c.W23_FY26}%"]]
tblA = numbers(["Year", "Source", "All EVs", "e-2W", "E-rickshaw (or e-3W incl. e-rickshaw)", "e-3W L5", "e-4W (personal) or other", "2W + 3W share"], tA,
               "Show the segment counts, FY2022 to FY2026 (CEEW and Autocar Pro)")
# table B: EVreporter H1 FY27 and October by category
def _row(lab, src, tot, comp):
    return [lab, src, n(tot)] + [f"{n(comp[k])} ({100 * comp[k] / tot:.1f}%)" for k in ("e2w", "l5m", "l5n", "erick", "ecart", "e4w", "ebus", "goods")]


h1c = dict(c.H1)
tB = [_row("April&ndash;September 2026", "EVreporter, six monthly first reports", c.H1_TOTAL, h1c),
      _row("October 2026", "EVreporter, Vahan as of 2 Nov", c.OCT_TOTAL, c.OCT_C)]
tblB = numbers(["Period", "Source", "All EVs", "e-2W", "e-3W L5 passenger (L5M)", "e-3W L5 cargo (L5N)", "E-rickshaw", "E-cart", "e-4W", "E-bus", "E-goods carrier"], tB,
               "Show the category counts, April to October 2026 (EVreporter)")
# table C: conflicts
tC = [["FY2026 EV total", f"{n(c.E['total'])} (EVreporter, 13 May 2026: Vahan plus the Telangana transport portal, low-speed e-2W excluded)", f"{n(A26['total'])} (Autocar Pro, Vahan of 1 to 6 Apr 2026, sum of its segments)", f"{n(c.GAP_TOTAL)} units, {c.GAP_TOTAL_PCT}%"],
      ["FY2026 e-2W", f"{n(c.E['e2w'])} (EVreporter)", f"{n(A26['e2w'])} (Autocar Pro)", f"{n(c.GAP_E2W)} units, {c.GAP_E2W_PCT}%"],
      ["FY2026 e-cars", f"{n(c.E['e4w'])} (EVreporter &lsquo;e-4W&rsquo;)", f"{n(A26['epv'])} (Autocar Pro &lsquo;e-PV&rsquo;)", f"{n(c.GAP_4W)} units, 11.7%"],
      ["FY2026 e-2W share of EVs", f"57.9% printed by EVreporter; {c.EVR_E2W_SH}% from its own printed counts", f"{c.E2W_FY26}% (Autocar Pro counts)", "EVreporter&rsquo;s printed share differs from its printed counts by 0.2 points"],
      ["FY2026 e-3W penetration", "33.7% (EVreporter, L5 passenger only; e-rickshaws and e-carts excluded)", "60.9% (Autocar Pro e-3W over FADA retail 3W, e-rickshaws included)", "Different numerators and denominators, both called e-3W; this blog&rsquo;s August piece shows 30.5% for L5 passenger from a CEEW/JMK deck"],
      ["September 2026 e-2W", f"{n(c.MONTHS['Sep'][1]['e2w'])} (EVreporter, 2 Oct), {n(c.SEP_REVISED['e2w'])} (EVreporter, 2 Nov)", f"{n(c.SEP_NUVAMA_E2W)} (Nuvama via Autocar Pro, 1 Oct), {n(c.SEP_INC42_E2W)} (Inc42, 3 Nov)", f"{n(max(c.SEP_E2W_SPREAD) - min(c.SEP_E2W_SPREAD))} units, 2.6%"],
      ["September 2026 EV total", f"{n(c.MONTHS['Sep'][0])} (EVreporter, 2 Oct)", f"{n(c.SEP_REVISED['total'])} (EVreporter, 2 Nov)", f"+{c.SEP_REV_PCT}% in one month as late registrations arrived"],
      ["June 2026 EV total", f"{n(305_678)} (EVreporter headline)", f"{n(305_687)} (sum of its own categories and its 12-month chart text)", "9 units"],
      ["October 2026 EV total", f"{n(c.OCT_TOTAL)} (EVreporter, Vahan of 2 Nov 2026)", "about 2.34 lakh (Outlook Business, citing the Times of India)", "Not a conflict: the Outlook article is dated 6 November 2025 and reports October 2025"]]
tblC = numbers(["Figure", "Source A", "Source B", "Gap or status"], tC, "Show the conflicts between sources")
means1 = (f"Two- and three-wheelers are about nine in ten electric registrations on every source read, but the share fell from {c.W23['FY25']}% in FY2025 to {c.W23_FY26}% in FY2026 and {c.H1_W23_SH}% in April&ndash;September 2026 as e-cars rose to {c.H1_E4W_SH}% of units on EVreporter&rsquo;s count.")
todo1 = f"Quote the source and its definition with every share, because the same FY2026 year differs by {c.GAP_E2W_PCT}% on e-2W units between Autocar Pro and EVreporter."
s1 = insight("Share of units: two- and three-wheelers were 91.1% of FY2026 electric registrations", chart1 + tblA + tblB + tblC, means1, todo1, "units")

# ------------------------------------------------------------------------------------------------ section 2: penetration against share
rows2 = [("e-3W, all three-wheelers including e-rickshaws", round(c.PEN["e3w"], 1), f"{lakh(A26['e3w'])} lakh of {lakh(c.FADA['w3'])} lakh sold"),
         ("e-3W, L5 passenger only (EVreporter)", c.EVR26_PEN["l5m"], "e-rickshaws and e-carts excluded"),
         ("e-2W", round(c.PEN["e2w"], 1), f"{lakh(A26['e2w'])} lakh of {lakh(c.FADA['w2'])} lakh sold"),
         ("e-car (Autocar Pro e-PV over FADA passenger vehicles)", round(c.PEN["epv"], 1), f"{lakh(A26['epv'])} lakh of {lakh(c.FADA['pv'])} lakh sold")]
assert [r[1] for r in rows2] == [60.9, 33.7, 6.5, 4.2]
chart2 = bars("FY2026 penetration: 60.9% of three-wheelers are electric, 6.5% of two-wheelers", rows2,
              accent=["e-3W, all three-wheelers including e-rickshaws", "e-2W"], unit="%", vmax=70,
              sub=f"Electric share of segment retail sales, FY2026, %. Each row also shows the segment&rsquo;s size: {c.SIZE_RATIO:.1f} two-wheelers are sold for each three-wheeler.",
              source="Autocar Pro (Vahan, Apr 2026) for electric units; FADA FY2026 retail release as printed by Outlook Business for segment sales; EVreporter FY2026 report for the L5 row. Ratios computed by this blog.")
tbl2 = numbers(["Item", "Figure", "Source and status"],
               [["Two-wheeler retail, FY2026", f"{n(c.FADA['w2'])}", "FADA, secondary (Outlook Business), up 13.4% on 18,889,595"],
                ["Three-wheeler retail, FY2026", f"{n(c.FADA['w3'])}", "FADA, secondary; includes e-rickshaws, which FADA counts as three-wheelers (its EV share is 60.95%)"],
                ["Market-size ratio", f"{c.SIZE_RATIO:.1f} to 1", "computed"],
                ["Penetration ratio", f"{c.PEN_RATIO:.1f} to 1 (60.94% over 6.54%)", "computed; FADA prints 6.54% and 60.95%"],
                ["Electric units ratio", f"{c.UNIT_RATIO:.2f} to 1 (1,401,663 over 830,818)", "computed; equals the size ratio divided by the penetration ratio"],
                ["SIAM wholesale, FY2026", "21,705,974 two-wheelers; 836,231 three-wheelers", "SIAM via search excerpt, not opened; wholesale dispatches, not registrations, and its three-wheeler count excludes non-members"],
                ["Low-speed e-2W", "excluded by EVreporter; Autocar Pro and CEEW do not say", "the exclusion is why EVreporter&rsquo;s 6.6% and FADA&rsquo;s 6.54% can agree while unit counts differ"]],
               "Show the denominators and ratios")
means2 = (f"The two facts are consistent because e-2W units equal e-3W units times the market-size ratio ({c.SIZE_RATIO:.1f} to 1) divided by the penetration ratio ({c.PEN_RATIO:.1f} to 1), which gives {c.UNIT_RATIO:.2f} to 1 exactly.")
todo2 = "State the denominator whenever an electric three-wheeler figure is quoted, since 60.9% counts every three-wheeler and 33.7% counts only L5 passenger vehicles."
s2 = insight("Penetration against share: e-3W penetration is 9.3 times e-2W, yet e-2W units are higher", chart2 + tbl2, means2, todo2, "penetration")

# ------------------------------------------------------------------------------------------------ section 3: units against energy
order = sorted(c.G, key=lambda k: -c.G[k])
rows3 = [(c.LABEL[k], c.G_SH[k], f"{c.U_SH[k]}% of units; {c.G[k]:.2f} GWh") for k in order]
assert [r[1] for r in rows3] == [40.4, 22.9, 13.4, 11.2, 6.5, 2.4, 1.7, 1.6]
chart3 = bars("Estimated FY2026 battery energy: e-cars 40.4% of kWh on 8.7% of units, e-2W 22.9% on 57.7%", rows3,
              accent=["e-car (4W)", "e-2W"], unit="%", vmax=45,
              sub=f"Estimated share of the {c.G_TOTAL:.1f} GWh registered in FY2026, %, each segment&rsquo;s share of units in the note. An estimate from units times assumed typical pack sizes, not a registration figure.",
              source="Units: EVreporter FY2026 report (e-bus count from Autocar Pro; L5 passenger derived from its 9.4% share). Pack sizes: manufacturer pages and market guides, see the table. Computed by this blog.")
src_pack = {"e2w": "Ather Rizta 2.9 and 3.7, TVS iQube 2.2 to 5.3, Bajaj Chetak 3.5, Vida 2.2 to 4.4 (Autocar India); mid 3.0 is an ASSUMPTION; 5.3 left out of the high case",
            "erick": "Saera Mayuri L3 5.4 (belectriq compilation), Joy e-rik 7.2 lead-acid, Mahindra Zor Grand 5.5, Mayuri cargo 3.2; mid is the Mayuri L3 figure; lead-acid versus lithium mix unknown",
            "ecart": "ASSUMPTION: same packs as e-rickshaws (e-cart packs were not found separately)",
            "l5m": "Treo 7.37, Piaggio Ape E-City 8.0 to 10.2, Bajaj RE E-TEC 8.9, Treo Plus 10.24, GoGo 12.1; mid 9.0 equals WRI India&rsquo;s assumed pack",
            "l5n": "Bajaj 8.9, Mahindra Zor Grand 10.24, Euler HiLoad 13.0 (OEM sites; a market assessment table)",
            "e4w": "Tiago 19.2 and 24, Punch 30 and 40 (25 and 35 in older listings), Nexon 30 and 45, Windsor 38 and 52.9 (Autocar India, Cartoq, CarWale); mid 35 is an ASSUMPTION",
            "goods": "Tata Ace EV 21.3, Mahindra 21.3, Euler 30 to 32, Jupiter 14 (market assessment table); heavier trucks would carry more, so this is probably low",
            "ebus": "12-metre buses 150 to 389 kWh (ICCT, WRI India, PMI 366.66 kWh); mid 250 is an ASSUMPTION"}
tbl3a = numbers(["Segment", "FY2026 units", "How the count was obtained", "Pack kWh low / mid / high", "GWh at mid", "Pack-size source and status"],
                [[c.LABEL[k], n(c.COUNTS[k]),
                  {"l5m": "derived: 9.4% (printed, rounded) of 2,550,865", "l5n": "derived: the residual after every other count; includes about 1,000 forklift-type vehicles",
                   "ebus": "Autocar Pro (EVreporter prints none)"}.get(k, "EVreporter, printed"),
                  " / ".join(f"{v:g}" for v in c.PACKS[k]), f"{c.G[k]:.2f}", src_pack[k]] for k in order],
                "Show the units, pack sizes and their status")
tbl3b = numbers(["Scenario", "Total GWh", "2W + 3W share of kWh", "e-car share of kWh"],
                [[name, f"{t:.1f}", f"{s:.1f}%", f"{cs:.1f}%"] for name, t, s, cs in c.SCEN_ROWS]
                + [[f"E-bus count {nb:,} instead of 5,039 (balance moves to L5 cargo)", f"{t:.1f}", f"{s:.1f}%", ""] for nb, t, s in c.BUS_SENS if nb != 5039]
                + [[f"E-car pack {kwh:g} kWh, others at mid", f"{t:.1f}", f"{s:.1f}%", f"{cs:.1f}%"] for kwh, t, s, cs in c.CAR_SENS if kwh != 35.0]
                + [["April&ndash;September 2026, every count reported, mid packs", f"{c.H1_G:.1f}", f"{c.H1_W23_KWH}%", ""]],
                "Show the pack-size sensitivity")
note3 = (f'<p class="gb-note">For scale: the {c.G_TOTAL:.1f} GWh is energy registered in one year, a flow, while the blog&rsquo;s '
         f'<a href="{B}/2026/09/indias-battery-storage-boom-is.html">grid battery storage piece</a> counts about 9.3 GWh installed in total by mid-2026, a stock; the two are different measures and the comparison is only an order of magnitude. '
         f'About {c.G_SH["e4w"] + c.G_SH["ebus"]:.0f}% of the estimated energy sits in cars and buses, which is where large cells are used.</p>\n')
means3 = (f"Two- and three-wheelers are {c.W23_UNIT_SH}% of FY2026 units but an estimated {c.W23_KWH_SH}% of battery energy, and the estimate stays between {min(r[2] for r in c.SCEN_ROWS):.1f}% and {max(r[2] for r in c.SCEN_ROWS):.1f}% across five pack-size scenarios, always at least 23 points below the unit share.")
todo3 = "Cell and storage planners should size demand from kWh by segment and not from unit counts, and the Ministry of Road Transport should publish registered battery kWh by class so that the estimate becomes a count."
s3 = insight("Units against energy: 90.5% of FY2026 EV units, an estimated 51.5% of battery kWh", chart3 + tbl3a + tbl3b + note3, means3, todo3, "energy")

# ------------------------------------------------------------------------------------------------ section 4: where
rows4 = sorted(c.ST_SH.items(), key=lambda kv: -kv[1])
rows4 = [(k, v, f"{c.ST[k]:,} EVs") for k, v in rows4]
chart4 = bars("Five states held at least 51.1% of FY2025 EV registrations; Uttar Pradesh alone 19.2%", rows4,
              accent=["Uttar Pradesh", "Maharashtra"], unit="%", vmax=22,
              sub="Share of the 1,964,831 EVs registered in FY2025, %, for the ten states CEEW chose for high EV penetration (Telangana excluded from the national total). Other states are not in the table, so these are lower bounds for any top five: the CEEW dashboard&rsquo;s cumulative ranking above puts Tamil Nadu fourth and Rajasthan fifth, and neither is among these ten.",
              source="CEEW issue brief, Dec 2025, Table 1 and Figure 3 (Vahan). Shares computed by this blog. The CEEW dashboard that holds the full state and RTO tables could not be read.")
tbl4 = numbers(["State (FY2025)", "EV volume", "EV penetration %", "e-2W penetration %", "e-3W penetration %", "e-car (personal) penetration %"],
               [["Uttar Pradesh", "377,212", "10.0", "3.7", "52.9", "1.7"], ["Maharashtra", "256,991", "8.2", "10.0", "10.3", "3.4"],
                ["Karnataka", "173,588", "9.3", "11.2", "12.7", "4.4"], ["Bihar", "113,609", "8.1", "2.1", "30.5", "1.2"],
                ["Delhi", "83,423", "11.6", "6.0", "52.7", "3.3"], ["Kerala", "82,279", "10.6", "12.9", "15.1", "5.8"],
                ["Assam", "67,967", "10.9", "0.8", "61.6", "0.5"], ["Goa", "10,088", "11.9", "15.6", "13.8", "5.8"],
                ["Tripura", "9,837", "15.9", "1.1", "65.5", "0.7"], ["Chandigarh", "5,714", "12.1", "7.5", "56.2", "6.3"]],
               "Show CEEW Table 1 (FY2025, ten states)") + numbers(
    ["e-2W by state, January to May 2026", "Units", "Share of 774,924", "Note"],
    [["Maharashtra", n(c.MH), f"{100 * c.MH / c.E2W_JM:.1f}%", "highest volume; 13.28% penetration"],
     ["Karnataka", n(c.KA), f"{100 * c.KA / c.E2W_JM:.1f}%", "18.87% penetration"],
     ["Tamil Nadu (as read)", n(c.TN_AMB), f"{100 * c.TN_AMB / c.E2W_JM:.1f}%", "the page&rsquo;s sentence reads &lsquo;Karnataka and Tamil Nadu with 92,522&rsquo;; read here as Tamil Nadu, not confirmed"],
     ["Kerala", n(c.KL), f"{100 * c.KL / c.E2W_JM:.1f}%", "19.36% penetration, the highest"],
     ["Top three together", n(c.MH + c.KA + c.TN_AMB), f"{c.TOP3_JM}%", "southern states 39.4% of e-2W, west 20.1%, central 18.2%, east 11.3%, north 10.9%"]],
    "Show the e-2W state counts (EVreporter, January to May 2026)")
means4 = (f"Uttar Pradesh&rsquo;s volume is three-wheeler led (52.9% e-3W penetration against 3.7% for e-2W) while Maharashtra and Karnataka are e-2W markets (10.0% and 11.2%), so one state ranking hides two different markets.")
todo4 = "Anyone publishing state rankings should split them by segment, because the top five states for e-2W units and for e-3W units could not be established from the dashboards this piece was allowed to read."
s4 = insight("Where: five states hold at least 51.1% of EVs, and the leaders differ by segment", chart4 + tbl4, means4, todo4, "where")

# ------------------------------------------------------------------------------------------------ section 5: why
rows5 = [("Electric three-wheeler (charging cost)", round(c.COST["ev"], 2), f"{c.KWH_KM:g} kWh/km and a {int(c.LOSS * 100)}% charging loss at &#8377;{c.ELEC:g}/kWh"),
         ("CNG three-wheeler", round(c.COST["cng"], 2), f"{c.KM_KG:g} km/kg at &#8377;{c.CNG_P:g}/kg"),
         ("Petrol three-wheeler", round(c.COST["petrol"], 2), f"{c.KM_L:g} km/L at &#8377;{c.PETROL_P:g}/L")]
assert [r[1] for r in rows5] == [0.67, 2.93, 5.08]
chart5 = bars("Running cost of a three-wheeler: electric &#8377;0.67 a km, CNG &#8377;2.93, petrol &#8377;5.08", rows5,
              accent="Electric three-wheeler (charging cost)", unit="&#8377;/km", vmax=5.5,
              sub="Fuel or charging cost per km, &#8377;, July 2026 prices from the blog&rsquo;s vehicle_fuel_mileage model; vehicle efficiency from WRI India (2020 evaluator). Excludes purchase cost, maintenance, insurance and battery replacement.",
              source="Prices: this blog&rsquo;s vehicle_fuel_mileage post (Delhi, July 2026; the model has no three-wheeler sheet). Efficiency: WRI India, Enabling the shift to electric auto-rickshaws (2023). Computed by this blog.")
tbl5a = numbers(["Input", "Value", "Status and source"],
                [["Electricity", "&#8377;10.6/kWh blended", "vehicle_fuel_mileage model, July 2026; commercial and public charging can cost more"],
                 ["CNG", "&#8377;83.09/kg", "vehicle_fuel_mileage model, Delhi, July 2026"],
                 ["Petrol (E20)", "&#8377;102.12/L", "vehicle_fuel_mileage model, Delhi, July 2026; the 4% E20 mileage drop is not applied to the WRI figure"],
                 ["e-3W consumption", "0.057 kWh/km (7.4 kWh over 130 km, Mahindra Treo)", "WRI India guidebook, certified-range basis; real-world use differs"],
                 ["Charging loss", "10%", "ASSUMPTION of this blog"],
                 ["CNG and petrol autos", "28.4 km/kg and 20.1 km/L", "WRI India TCO table, 2020 evaluator, secondary"],
                 ["Blog two-wheeler comparison", "petrol &#8377;1.93/km, electric &#8377;0.35/km (5.5 times)", "vehicle_fuel_mileage post, same price basis"]],
                "Show the inputs and their status") + numbers(
    ["Case", "Electric &#8377;/km", "CNG &#8377;/km"],
    [[f"Electricity &#8377;{el:g}/kWh, loss {int(lo * 100)}%", f"{v:.2f}", "2.93"] for el, lo, v in c.COST_SENS]
    + [[f"CNG at {kmkg:g} km/kg", "0.67", f"{v:.2f}"] for kmkg, v in c.CNG_SENS if kmkg != 28.4],
    "Show the sensitivity: electricity price, charging loss and CNG efficiency") + numbers(
    ["Source", "Finding", "Status"],
    [["CEEW, cost of ownership study (2025)", "three-wheeler total cost per km in 2024: electric &#8377;1.28, CNG &#8377;2.35, diesel &#8377;2.69, petrol &#8377;3.21; e-2W &#8377;1.48 against petrol &#8377;2.46", "search excerpt of a CEEW PDF; the CEEW site was not opened for this piece"],
     ["CEEW blog, Lucknow (2025)", "L5 passenger e-autos cost 38 to 46% less to run than CNG at 160 km a day; lead-acid e-rickshaws cost more than L5 e-autos because the batteries need replacing in about nine months", "search excerpt, not opened"],
     ["WRI India (2023)", "ten-year total cost per km: e-auto &#8377;2.53, CNG &#8377;2.90, petrol &#8377;3.31, diesel &#8377;3.17 at 100 km a day", "opened, 2020 evaluator inputs"],
     ["JMK Research (March 2026)", "L5 cargo, five years at 100 km a day: total cost CNG &#8377;904,859, electric without subsidy &#8377;806,556 (&#8377;756,556 with); fuel cost per km diesel &#8377;3.6, CNG &#8377;2.7, electric &#8377;0.8", "search excerpt, JMK outside the allowed network"]],
    "Show total-cost studies (secondary)")
subs = flow([("1 October 2026", "PIB: PM E-DRIVE runs to 31 March 2028 with an outlay of &#8377;11,900 crore; registered e-2Ws get &#8377;2,500 a kWh capped at &#8377;5,000 on vehicles up to &#8377;1.5 lakh ex-factory, with &#8377;2,767 crore set aside."),
             ("10 August 2026", "S.O. 4424(E) of the Ministry of Heavy Industries, as reported by this blog&rsquo;s August piece from the Gazette, set the e-2W end date at 31 March 2028 and the last date for claims at 31 December 2027; not re-read for this piece."),
             ("26 December 2025", "PIB: the L5 e-3W sub-component met its target and closed. L5 passenger registrations nevertheless rose " + f"{L5M_GROWTH}% from May to October 2026 ({n(c.MONTHS['May'][1]['l5m'])} to {n(c.OCT_C['l5m'])}, EVreporter first reports).", True)])
note5 = ('<p class="gb-note">Subsidy status, all in the box above: the e-2W incentive is live to 31 March 2028; the L5 three-wheeler incentive is closed; e-rickshaws and e-carts carry their own scheme date, which this blog&rsquo;s August piece records as 31 March 2028. '
         'CEEW&rsquo;s brief adds that lower-income states are electrifying through three-wheelers (average e-3W penetration 52.6% in four lower-income states against 26.8% in six higher-income ones) while e-2W penetration in the higher-income group is 10.5% against 1.9%. '
         f'Running-cost arithmetic for cars is in <a href="{B}/2026/10/how-to-use-vehiclefuelmileage-running.html">How to use vehicle_fuel_mileage</a>.</p>\n')
means5 = (f"An electric three-wheeler saves about &#8377;{c.COST['cng'] - c.COST['ev']:.2f} a km against CNG on fuel alone, a gap that stays above &#8377;1.30 in every sensitivity case, and the blog&rsquo;s model puts the two-wheeler gap at &#8377;1.58 a km (&#8377;1.93 against &#8377;0.35), so high daily distance is what makes the three-wheeler case stronger.")
todo5 = "Fleet buyers should compare total cost at their own daily distance with the inputs in the box, and agencies should publish a three-wheeler cost sheet, because the blog&rsquo;s own cost model has none."
s5 = insight("Why: an electric three-wheeler costs about &#8377;0.67 a km to charge, CNG &#8377;2.93", chart5 + tbl5a + subs + note5, means5, todo5, "why")
# the sensitivity claim in means5, asserted
assert min(v_cng - v_ev for (_, v_cng), (_, _, v_ev) in [(a, b) for a in c.CNG_SENS for b in c.COST_SENS]) > 1.30
assert round(c.COST["cng"] - c.COST["ev"], 2) == 2.25 and round(1.93 - 0.35, 2) == 1.58

# ------------------------------------------------------------------------------------------------ fixes, caveats, gaps
fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Road Transport and Highways (Vahan):</b> publish one monthly table of registrations by vehicle class, fuel, state and RTO, with the class definitions (L3, L5M, L5N, low-speed, goods, passenger) and a revision log, so that a month&rsquo;s figure can be cited with its vintage.</li>
<li><b>Ministry of Heavy Industries:</b> report PM E-DRIVE claims by segment, state and battery kWh, so that registered battery energy by class can be counted instead of estimated.</li>
<li><b>Vahan and the state transport departments:</b> add Telangana to the national dashboard, or publish its monthly class counts in the same format, because the two largest secondary series differ by about 5% in e-2W units with one including Telangana and the other apparently not.</li>
<li><b>FADA, SIAM and the trackers:</b> state in each release whether e-rickshaws and low-speed e-2Ws are inside the three-wheeler and two-wheeler counts and penetration, so that 33.7% and 60.9% are never both called e-3W penetration.</li>
<li><b>CEEW-GFC:</b> offer the dashboard&rsquo;s state and RTO tables as a downloadable file with a citation date, so that state concentration by segment can be checked without a browser.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''
method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li><b>One source per series.</b> FY2022 to FY2025 shares use the CEEW brief (Vahan, Telangana excluded, 1,378 RTOs); FY2026 shares use Autocar Pro&rsquo;s Vahan pull of 1 to 6 April 2026; April to October 2026 uses EVreporter&rsquo;s monthly first reports (Vahan, low-speed e-2W excluded, Telangana excluded in the April report only). Autocar Pro&rsquo;s FY2025 figures match CEEW&rsquo;s to 0.01% for e-2W and 0.02% for e-3W, which is why those two can be read as one definition; EVreporter&rsquo;s FY2026 figures are 4.0% higher in total and 5.0% higher for e-2W and say they include the Telangana transport portal.</li>
<li><b>Segments.</b> E-rickshaw is EVreporter&rsquo;s term for a low-speed (up to 25 km/h) electric three-wheeler carrying passengers, and e-cart for one carrying goods; L5M is the passenger and L5N the cargo three-wheeler; CEEW calls the low-speed passenger class &lsquo;E-rickshaw&rsquo; and the rest &lsquo;E3W&rsquo;. Autocar Pro&rsquo;s e-3W includes all of them. How Vahan codes these classes was not opened; the labels are the trackers&rsquo;.</li>
<li><b>Registrations are not sales.</b> Every figure is a Vahan registration, used as a proxy for retail sales; late registrations raised September 2026 by 1.3% in a month, so the latest month is always understated.</li>
<li><b>Derived counts.</b> L5 passenger FY2026 (239,781) is 9.4% of 2,550,865 and carries the rounding of that percentage; the L5 cargo count (32,112) is the residual after every other count and includes a few hundred forklift-type vehicles; the e-bus count (5,039) comes from Autocar Pro.</li>
<li><b>Energy.</b> Units times assumed typical pack kWh. Pack sizes come from manufacturer pages and guides for models on sale, not sales-weighted, so the mid values are assumptions. The estimate counts energy registered, not energy delivered, and counts lead-acid e-rickshaws at lithium-equivalent kWh.</li>
<li><b>Cost per km.</b> Charging or fuel cost only; the blog&rsquo;s model prices are July 2026 and Delhi-based; the vehicle efficiencies are WRI India&rsquo;s 2020 inputs.</li>
</ul></details>
'''
gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The CEEW-GFC dashboard itself: only four screenshots were seen (supplied 27 November 2026), so state volumes, penetration lines and the unlabelled registration points are read by eye, and the top five states for e-2W and for e-3W by units remain unestablished. The dashboard pages (www.ceew.in, three addresses tried) returned a Cloudflare challenge and were not bypassed; only the CEEW issue brief PDF could be read. The Vahan dashboard did not load. State figures here come from the brief&rsquo;s Table 1 (ten states, all EVs, FY2025) and an EVreporter page on e-2W (January to May 2026).</li>
<li>Any RTO-level ranking. EVreporter&rsquo;s city and RTO tables are for data-portal subscribers; its FY2026 page names only Bengaluru (98,892 e-2Ws), Delhi (41,238), Lucknow (14,099 L5 passenger) and Kanpur (7,513).</li>
<li>FY2026 L5 passenger, L5 cargo and e-bus counts from one source. EVreporter&rsquo;s public excerpt gives a 9.4% share for L5 passenger and no cargo or bus count.</li>
<li>Whether the 70,366-unit FY2026 e-2W gap between EVreporter and Autocar Pro is Telangana, late registrations or the low-speed classes. The EVreporter note names the Telangana transport portal; Autocar Pro&rsquo;s inclusion of Telangana was not stated.</li>
<li>The FY2022 and FY2023 e-3W L5 counts (not labelled on CEEW&rsquo;s chart), so those two shares are lower bounds.</li>
<li>Mercom&rsquo;s January to March 2026 figures (696,769 EVs, 9% of vehicles; 427,773 e-2Ws, about 61%): the page was refused by the network and the figures are from a search excerpt only. They are not used in any computed figure here. January to March is also a different quarter from EVreporter&rsquo;s April to June fiscal quarter of 834,222 EVs.</li>
<li>JMK Research&rsquo;s reports (H1 FY2027 at 17.89 lakh, the FY2026 report card, the cargo three-wheeler white paper), NewsBytes (403) and CEEW&rsquo;s cost-of-ownership PDF were outside the allowed network or blocked; they appear only as labelled excerpts, and the JMK total is used once, as a 0.8% cross-check.</li>
<li>S.O. 4424(E) of 10 August 2026 itself. PIB&rsquo;s release of 1 October 2026 confirms its terms; the Gazette text was read for the blog&rsquo;s August piece and not re-read. A July 2026 parliamentary answer found in search gives 31 July 2026 for the e-2W end date; it predates the 10 August notification.</li>
<li>Real-world electricity use and charging price for three-wheelers, and the lead-acid share of e-rickshaws.</li>
<li>Whether the 11.6% September 2026 e-2W penetration the August piece attributes to FADA appears on a FADA page; the only copy opened is EVreporter&rsquo;s, with Nuvama and Angel One giving 11.4% and 11.5%.</li>
</ul></details>
'''
covers = '''<h2 class="gb-h2" id="covers">What this piece does and doesn&rsquo;t cover</h2>
<div class="gb-warn"><p style="margin:0">It covers the mix of electric registrations, not the number of vehicles on the road, and not electric cars or buses beyond their effect on the mix. It treats Vahan registrations as a proxy for sales: a registration lags a sale, some states report late, Telangana is handled differently by different trackers, and low-speed e-2Ws are in or out depending on the source. Source definitions drift: &lsquo;e-3W penetration&rsquo; is 33.7% or 60.9% depending on whether e-rickshaws count. The October 2026 total of 354,284 is a first report and will rise; the 2.34 lakh figure that circulated with it describes October 2025. Battery energy is an estimate built on assumed pack sizes.</p></div>
'''

# ------------------------------------------------------------------------------------------------ section: CEEW dashboard (screenshots)
rows_d = [(k, v, f"{v}%") for k, v in c.DASH_SHARE.items()]
chart_d = bars("CEEW dashboard, FY2014 to FY2027: 92.6% of registered EVs are 2W, 3W or e-rickshaws", rows_d,
               accent=["E-2W", "E-Rickshaw"], unit="%", vmax=60,
               sub="Share of all electric vehicles registered from FY2014 to FY2027 to date, per cent, as printed in the dashboard&rsquo;s EV Shares legend. E-3W and E-Rickshaw are separate categories on the dashboard; whether its E-3W is L5 only is not stated.",
               source="CEEW-GFC Electric Mobility Dashboard, National Volume Monitor (primary; read from a screenshot supplied on 27 November 2026; the page was not opened here). Sum of E-2W, E-3W and E-Rickshaw computed by this blog.")
def _d(v):
    return f"{v:+,}"
tbl_d1 = numbers(["Year", "CEEW dashboard (screenshot labels)", "CEEW issue brief, Dec 2025", "Dashboard minus brief", "Other source"],
    [["FY2022", n(c.DASH_REG["FY22"]), n(c.CEEW_TOTAL["FY22"]), f"{_d(c.DASH_VS_BRIEF['FY22'])} ({c.DASH_VS_BRIEF_PCT['FY22']}%)", ""],
     ["FY2023", n(c.DASH_REG["FY23"]), n(c.CEEW_TOTAL["FY23"]), f"{_d(c.DASH_VS_BRIEF['FY23'])}", ""],
     ["FY2024", n(c.DASH_REG["FY24"]), n(c.CEEW_TOTAL["FY24"]), f"{_d(c.DASH_VS_BRIEF['FY24'])}", ""],
     ["FY2025", n(c.DASH_REG["FY25"]), n(c.CEEW_TOTAL["FY25"]), f"{_d(c.DASH_VS_BRIEF['FY25'])} ({c.DASH_VS_BRIEF_PCT['FY25']}%)", "Autocar Pro 1,967,547"],
     ["FY2026", n(c.DASH_REG["FY26"]), "not in the brief", "", f"EVreporter {n(c.EVR26['total'])} ({_d(c.D26_EVR)}); Autocar Pro {n(c.AP['FY26']['total'])} ({_d(c.D26_AP)})"]],
    "Show the dashboard registration series against the other sources")
tbl_d2 = numbers(["State, cumulative FY2014 to FY2027 (read by eye)", "EVs, thousand (about)", "Largest segment", "e-2W share (about)", "E-rickshaw share (about)"],
    [[k, f"{v['total']:,}", ("E-rickshaw" if k in c.DASH_RICK_LED else ("E-2W" if k in c.DASH_E2W_LED else "E-2W and E-rickshaw close")),
      f"{100 * v['e2w'] / v['total']:.0f}%", (f"{100 * v['erick'] / v['total']:.0f}%" if "erick" in v else "small")] for k, v in c.DASH_ST.items()],
    "Show the state bars read from the dashboard chart (about plus or minus 50 thousand)")
tbl_d3 = numbers(["Penetration, read by eye", "FY2025-26", "FY2026-27 to date"],
    [[k, f"about {c.DASH_PEN['FY2025-26'][k]:g}%" if k in c.DASH_PEN["FY2025-26"] else "not read", f"about {c.DASH_PEN['FY2026-27 to date'][k]:g}%" if k in c.DASH_PEN["FY2026-27 to date"] else "not read"]
     for k in ["E-3W", "E-2W", "E-4W", "E-4W (C)", "E-Bus", "National average"]],
    "Show the penetration lines read from the dashboard chart") + (
    '<p class="gb-note">Reading notes: the chart&rsquo;s title still says FY2014 to FY2022 while its axis runs to FY2026-27. The FY2014-15 and FY2015-16 labels overlap and read as 2,399 and 16,165; the FY2016-17, FY2018-19, FY2020-21 and FY2026-27 points carry no label '
    f'(FY2026-27 is a part year, about 2.4 million by eye).</p>'
    f'<p class="gb-note">The dashboard&rsquo;s FY2025-26 E-3W penetration (about 32%) sits beside EVreporter&rsquo;s 33.7% for L5 passenger and the August piece&rsquo;s 30.5%, which suggests its E-3W line is L5 and leaves e-rickshaws out; that is an inference, not something the dashboard states.</p>'
    f'<p class="gb-note">The state and penetration values are read from the bars and lines by eye, so only the printed shares and the labelled registration figures are exact.</p>'
    f'<p class="gb-note">On the same reading the ten leading states hold about {c.DASH_TOP10_SH}% of cumulative registrations and the top five (Uttar Pradesh, Maharashtra, Karnataka, Tamil Nadu, Rajasthan) about {c.DASH_TOP5_SH}%, '
    f'using a rough cumulative total of {c.DASH_CUM / 1e6:.1f} million; treat both as estimates within a few points.</p>')
means_d = (f"CEEW&rsquo;s own dashboard puts {c.DASH_W23}% of EVs registered since FY2014 in two-wheelers, three-wheelers and e-rickshaws, shows e-rickshaws as a {c.DASH_SHARE['E-Rickshaw']}% category that the three-wheeler label hides, "
           f"and gives an FY2026 total of {n(c.DASH_REG['FY26'])} that sits between EVreporter and Autocar Pro.")
todo_d = "Quote the dashboard&rsquo;s category definitions and the date of the pull with every share, because its three-wheeler and e-rickshaw lines are separate while most other sources combine them."
sd = insight("CEEW dashboard: 92.6% of EVs registered since FY2014 are 2W, 3W or e-rickshaws", chart_d + tbl_d1 + tbl_d2 + tbl_d3, means_d, todo_d, "dashboard")

body = (STYLE + top + intro + s1 + sd + s2 + s3 + s4 + s5 + fixes + covers + method + gaps)

SOURCES = (
    'Primary, from screenshots supplied on 27 November 2026 (page not opened here): <a href="https://www.ceew.in/gfc/tools_and_dashboards/electric-mobility/national-volume-monitor">CEEW-GFC Electric Mobility Dashboard, National Volume Monitor</a>. '
    'Read for this piece, primary or near-primary: <a href="https://www.ceew.in/gfc/solutions-factory/publications/CEEW-Navigating_India\'s_Electric_Mobility_Transition_WEB.pdf">CEEW, Navigating India&rsquo;s Electric Mobility Transition (issue brief, December 2025)</a> (Vahan data via the CEEW-GFC dashboard); '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2317890&amp;lang=1&amp;reg=48">PIB, PM E-DRIVE Scheme, 1 October 2026</a>; <a href="https://github.com/herrrickshaw/vehicle_fuel_mileage">vehicle_fuel_mileage repository</a>. '
    '</p><p class="gb-note" style="margin:.6rem 0 0">Secondary, opened (all report Vahan data): <a href="https://evreporter.com/india-sold-2550865-electric-vehicles-across-categories-in-fy-2025-26/">EVreporter, FY2025-26 report</a>; '
    '<a href="https://evreporter.com/indias-electric-vehicle-sales-trend-april-2026/">April</a>, <a href="https://evreporter.com/indias-electric-vehicle-sales-trend-may-2026/">May</a>, <a href="https://evreporter.com/indias-electric-vehicle-sales-trend-june-2026/">June</a>, '
    '<a href="https://evreporter.com/indias-electric-vehicle-sales-trend-july-2026/">July</a>, <a href="https://evreporter.com/indias-electric-vehicle-sales-trend-august-2026/">August</a>, '
    '<a href="https://evreporter.com/indias-electric-vehicle-sales-trend-september-2026/">September</a> and <a href="https://evreporter.com/indias-electric-vehicle-sales-trend-october-2026/">October 2026</a> trend pages; '
    '<a href="https://evreporter.com/in-2026-india-records-increasing-ev-penetration-across-vehicle-segments/">EVreporter, penetration January to July 2026</a>; '
    '<a href="https://evreporter.com/electric-2ws-capture-over-8-of-indias-2w-market-marketkerala-records-19-ev-penetration-in-2w-sales-jan-2026-may-2026/">EVreporter, e-2W by state, January to May 2026</a>; '
    '<a href="https://www.autocarpro.in/news/record-14-million-electric-2ws-sold-in-fy2026-command-57-share-of-india-ev-market-131938">Autocar Pro, e-2W FY2026</a>; '
    '<a href="https://www.autocarpro.in/analysis-sales/ev-sales-in-india-surpass-245-million-units-in-fy2026-all-4-segments-register-double-digit-growth-131974">Autocar Pro, EV sales FY2026</a>; '
    '<a href="https://www.autocarpro.in/news/electric-two-wheeler-registrations-cross-1-million-in-h1-fy27-as-september-volumes-surge-85-percent-135022">Autocar Pro, H1 FY2027 e-2W (Nuvama)</a>; '
    '<a href="https://www.autocarindia.com/car-news-amp/october-2026-ev-sales-over-30000-units-hit-for-fifth-straight-month-441232">Autocar India, October 2026 electric cars</a>; '
    '<a href="https://inc42.com/buzz/e2w-registrations-rise-2-9-mom-to-2-15-lakh-in-october-tvs-hero-gain-market-share/">Inc42, e-2W October 2026</a>; '
    '<a href="https://www.angelone.in/news/economy/electric-two-wheeler-sales-cross-15-lakh-in-nine-months-of-2026">Angel One, e-2W January to September 2026</a>; '
    '<a href="https://www.outlookbusiness.com/industry/auto-retail-sales-up-133-pc-at-29671064-units-in-fy26-fada">Outlook Business, FADA FY2026 retail release</a>; '
    '<a href="https://www.outlookbusiness.com/industry/india-ev-registrations-record-october-two-wheelers-lead">Outlook Business, 6 November 2025 (October 2025 registrations)</a>. '
    '</p><p class="gb-note" style="margin:.6rem 0 0">Pack sizes and costs, secondary: manufacturer pages (Mahindra Last Mile Mobility, Piaggio, Euler, MG, Tata), Autocar India, Cartoq and CarWale car guides, a belectriq compilation, an ICCT e-bus paper, WRI India&rsquo;s <a href="https://wri-india.org/sites/default/files/E-auto-guidebook_WRI-India.pdf">auto-rickshaw guidebook</a>; read as search excerpts, not full pages. '
    '</p><p class="gb-note" style="margin:.6rem 0 0">Not opened (see the &lsquo;could not establish&rsquo; box): the CEEW dashboard page itself (seen only as screenshots), the Vahan dashboard, Mercom, JMK Research, NewsBytes, Ticker (Finology). Every figure marked estimate, derived or assumption was computed by this blog. Analysed 26 November 2026.')

RELATED = [
    (f"{B}/2026/08/indias-ev-market-single-digit.html", "India's EV sales: 12% of vehicles in April&ndash;September, cars in single digits"),
    (f"{B}/2026/09/indias-battery-storage-boom-is.html", "Grid battery storage in India: about 9.3 GWh by mid-2026, up from 1.08 GWh"),
    (f"{B}/2026/10/how-to-use-vehiclefuelmileage-running.html", "How to use vehicle_fuel_mileage: running cost per km for petrol, diesel, CNG and EV in India"),
]

build("Energy &middot; Transport", TITLE,
      f"Two- and three-wheelers were {c.W23_FY26}% of India&rsquo;s FY2026 electric registrations but an estimated {c.W23_KWH_SH:.0f}% of the battery energy; five sections set out the share, the penetration paradox, the energy, the states and the cost per km.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
assert "masaladeutsch" not in html.lower() and "masala deutsch" not in html.lower()
assert "<details" in html and "accordion.js" in html
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title,", f"{len(html):,} bytes, built in {time.time() - T0:.1f}s")
