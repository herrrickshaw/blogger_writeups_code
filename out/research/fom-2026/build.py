"""Biogas biofertiliser: tonnage sold, subsidy paid, plants registered and gazette clearances (to 18 Nov 2026).
Build from the repo root:  python3 out/research/fom-2026/build.py   (writes out/post-india-biogas-biofertiliser-sales-subsidy-clearances-2026.html)
Tonnage and subsidy: Rajya Sabha starred question 186, 10 March 2026. Clearances: Gazette of India orders under clause 22(c) of the Fertiliser Control Order, listed in the vertistrat-site register. Analysed 18 November 2026."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-biogas-biofertiliser-sales-subsidy-clearances-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- Annexure I: sale in tonnes ----
SALE = {"2023-24": (27899.62, 28159.00, 0.00, 56058.62), "2024-25": (106620.15, 228181.00, 1490.16, 336291.30), "2025-26 to 28 Feb 2026": (578865.03, 1089019.04, 4799.13, 1672683.20)}
TOT = (713384.80, 1345359.04, 6289.28, 2065033.12)
for k, (f, l, p, t) in SALE.items():
    assert abs(f + l + p - t) < 0.02, k
for i in range(4):
    assert abs(sum(v[i] for v in SALE.values()) - TOT[i]) < 0.05, i
MDA = {"2023-24": 0.0, "2024-25": 28.00, "2025-26 to 28 Feb 2026": 83.72}
assert round(sum(MDA.values()), 2) == 111.72
RATE = 1500                                                    # Rs per tonne
# subsidy at Rs 1,500 a tonne on the sales reported: 20.65 lakh t x 1,500 = Rs 309.8 crore, against Rs 111.72 crore released
POTENTIAL_CR = TOT[3] * RATE / 1e7
assert round(POTENTIAL_CR, 1) == 309.8
RELEASED_SHARE = 100 * 111.72 / POTENTIAL_CR
assert round(RELEASED_SHARE) == 36
g = lambda a, b: round(a / b, 1)
assert g(SALE["2025-26 to 28 Feb 2026"][3], SALE["2024-25"][3]) == 5.0 and g(SALE["2024-25"][3], SALE["2023-24"][3]) == 6.0
LFOM_SHARE = 100 * TOT[1] / TOT[3]
assert round(LFOM_SHARE) == 65

# ---- Annexure II: production by state, 2023 to 4 March 2026, total MT (sums of FOM+LFOM+PROM) ----
STATE = {"Uttar Pradesh": (10586.00, 142795.26, 596481.88, 214494.39), "Punjab": (12228.40, 129766.88, 330720.04, 123351.88), "Haryana": (10160.00, 45591.74, 243924.41, 129429.41),
         "Gujarat": (2330.02, 92530.58, 134080.53, 44533.00), "Karnataka": (9171.02, 90111.61, 132852.52, 29693.50), "Maharashtra": (21985.21, 36869.42, 62609.16, 33480.00),
         "Madhya Pradesh": (27.00, 1369.00, 55749.39, 28981.50), "Rajasthan": (0.0, 3163.00, 21296.50, 32511.00), "Andhra Pradesh": (30.60, 14944.00, 13555.00, 20453.60),
         "Tamil Nadu": (2289.00, 11431.22, 18435.00, 5048.81), "Uttarakhand": (2332.04, 11530.03, 22780.20, 5982.00), "Telangana": (0.0, 393.00, 3851.00, 1524.00)}
STATE_TOT = {k: sum(v) for k, v in STATE.items()}
ALL = (71139.28, 580495.73, 1636340.63, 669483.09)
assert abs(sum(ALL) - 2957458.73) < 0.5
# production in the states listed vs the national total: others (Bihar, 5 t) negligible
shown = sum(STATE_TOT.values())
assert abs(shown + 5.0 - sum(ALL)) < 5, (shown, sum(ALL))
UP_SHARE = 100 * STATE_TOT["Uttar Pradesh"] / sum(ALL)
assert round(UP_SHARE) == 33
# sales (20.65 lakh t) and reported production (29.57 lakh t): different measures and dates
assert round(sum(ALL) / TOT[3], 2) == 1.43

# ---- Gazette register (vertistrat-site src/data/biogasFomAuthorisations.ts) ----
ENTRIES, CURRENT, EXPIRED, ORDERS = 149, 122, 27, 10
assert CURRENT + EXPIRED == ENTRIES
IFMS, MOUS, CAMPS = 120, 44, 15690
RELIANCE = 30
assert round(100 * RELIANCE / ENTRIES) == 20

TITLE = "Biogas manure: 20.65 lakh tonnes sold, Rs 111.72 crore subsidy, 149 clearances"
assert 55 <= len(TITLE) <= 82, len(TITLE)
TOP3 = sum(STATE_TOT[k] for k in ("Uttar Pradesh", "Punjab", "Haryana")); TOP3_SHARE = 100 * TOP3 / sum(ALL)
assert round(TOP3_SHARE) == 67 and round(STATE_TOT["Uttar Pradesh"]) == 964358 and round(100 * 1672683.20 / 2065033.12) == 81

top = top_line([
    ("20.65 lakh tonnes", " of fermented organic manure, liquid and phosphate-rich organic manure were sold from 2023-24 to 28 February 2026, 81% of it in 2025-26 alone."),
    ("Rs 111.72 crore", f" of the Rs 1,500 a tonne subsidy had been released by 28 February 2026, about {RELEASED_SHARE:.0f}% of the Rs {POTENTIAL_CR:.0f} crore that the rate implies on the tonnage reported; the scheme ends this year and is being evaluated."),
    ("149 entries", " in ten gazette orders from 14 November 2023 to 27 July 2026 authorise biogas plants to sell the manure in bulk to farmers; 122 are current and 27 lapsed on 14 November 2026."),
])

s1 = insight(
    "Sales of biogas manure rose from 56,059 tonnes in 2023-24 to 16.73 lakh tonnes in 2025-26",
    bars("Sales grew six times in 2024-25 and five times again in 2025-26, to 16.73 lakh tonnes",
         [(k, round(v[3])) for k, v in SALE.items()], accent="2025-26 to 28 Feb 2026", unit=" tonnes",
         sub="Sale of FOM, liquid FOM and PROM under the Market Development Assistance scheme, tonnes. 2025-26 is ten months.",
         source="Rajya Sabha starred question 186, Ministry of Chemicals and Fertilizers, 10 March 2026, Annexure I.")
    + numbers(["Year", "FOM, t", "Liquid FOM, t", "PROM, t", "Total, t"],
              [[k, f"{v[0]:,.0f}", f"{v[1]:,.0f}", f"{v[2]:,.0f}", f"{v[3]:,.0f}"] for k, v in SALE.items()] + [["Total", f"{TOT[0]:,.0f}", f"{TOT[1]:,.0f}", f"{TOT[2]:,.0f}", f"{TOT[3]:,.0f}"]]),
    f"Liquid manure is {LFOM_SHARE:.0f}% of the 20.65 lakh tonnes, and the jump from 3.36 lakh tonnes to 16.73 lakh tonnes in one year comes with 15,690 farmer camps and 44 marketing agreements between fertiliser companies and biogas operators.",
    "The Department of Fertilizers should publish sales by plant and by quarter with the realised price per tonne, so that the volume can be tied to named plants and to what farmers paid.",
    "sales")

s2 = insight(
    "The Rs 1,500 a tonne subsidy has released Rs 111.72 crore, 36% of what the tonnage implies",
    bars("Rs 111.72 crore released by February 2026 against Rs 310 crore implied by the tonnage",
         [("Released, 2024-25", MDA["2024-25"]), ("Released, 2025-26 to 28 February", MDA["2025-26 to 28 Feb 2026"]), ("Released in total", 111.72), ("Implied at Rs 1,500 on 20.65 lakh tonnes", round(POTENTIAL_CR, 1))],
         accent="Released in total", unit="₹ crore",
         sub="Market Development Assistance released by year, Rs crore, against this blog's calculation of the rate times the tonnage reported sold.",
         source="Rajya Sabha starred question 186, 10 March 2026; calculation by this blog.")
    + numbers(["Item", "Value"],
              [["Rate", "Rs 1,500 a tonne for FOM, liquid FOM and PROM from plants under GOBARdhan"], ["Released, 2023-24", "Rs 0"], ["Released, 2024-25", "Rs 28.00 crore"],
               ["Released, 2025-26 to 28 February", "Rs 83.72 crore"], ["Implied if every reported tonne qualified", f"Rs {POTENTIAL_CR:.1f} crore"],
               ["Status", "scheme &ldquo;culminating this year&rdquo;; under evaluation by NITI Aayog"], ["ICAR awareness project", "Rs 11.79 crore for two years from 29 November 2024"]]),
    "The gap between Rs 111.72 crore released and about Rs 310 crore implied may reflect lags in claims, plants not registered or tonnage that did not qualify, and the reply does not say which, so the subsidy bill for a scheme ending this year is not yet known.",
    "The Department of Fertilizers should state the claims received, paid and pending as of the scheme end date, so that a decision to extend or replace the subsidy rests on the full liability.",
    "subsidy")

s3 = insight(
    "Uttar Pradesh produced a third of the manure reported, 9.64 lakh tonnes of 29.57 lakh",
    bars("Uttar Pradesh, Punjab and Haryana produced 67% of the biogas manure reported to March 2026",
         [(k, round(v)) for k, v in sorted(STATE_TOT.items(), key=lambda kv: -kv[1])], accent="Uttar Pradesh", unit=" tonnes",
         sub="Production of FOM, liquid FOM and PROM by state, tonnes, 2023 to 4 March 2026. The 12 states shown are all but Bihar (5 tonnes).",
         source="Rajya Sabha starred question 186, 10 March 2026, Annexure II; sums computed by this blog.")
    + numbers(["State", "2023, t", "2024, t", "2025, t", "2026 to 4 Mar, t"], [[k, f"{v[0]:,.0f}", f"{v[1]:,.0f}", f"{v[2]:,.0f}", f"{v[3]:,.0f}"] for k, v in STATE.items()]),
    "Three northern states produced 67% of the reported tonnage, so the national figure is close to a regional one and a policy tested there says little about the south and the east.",
    "State agriculture departments should publish the tonnage and the hectares reached by the manure in their own states, so that its effect on chemical fertiliser use can be measured.",
    "states")

s4 = insight(
    "122 of 149 gazette clearances are current; 27 lapsed on 14 November 2026",
    bars("Of 149 gazette entries, 122 are current and 27 lapsed with the November 2023 order",
         [("Entries in the ten orders", ENTRIES), ("Current on 18 November 2026", CURRENT), ("Expired, order of 14 November 2023", EXPIRED), ("Reliance-named plants", RELIANCE),
          ("Plants registered on iFMS for the subsidy, 4 March 2026", IFMS)],
         accent="Current on 18 November 2026", unit="",
         sub="Counts. Gazette entries authorise bulk sale directly to farmers for three years from publication; the iFMS list is a separate subsidy registration.",
         source="Gazette of India orders under clause 22(c), 14 Nov 2023 to 27 Jul 2026 (register on the VertiStrat trade-ideas page); Rajya Sabha starred question 186.")
    + numbers(["Order", "Date", "Entries"],
              [["S.O. 4918(E)", "14 Nov 2023", "27"], ["S.O. 1366(E)", "15 Mar 2024", "14"], ["S.O. 3723(E)", "2 Sep 2024", "21"], ["S.O. 1102(E)", "6 Mar 2025", "7"],
               ["S.O. 3042(E)", "8 Jul 2025", "17"], ["S.O. 5836(E)", "17 Dec 2025", "20"], ["S.O. 1018(E)", "25 Feb 2026", "13"], ["S.O. 3345(E)", "23 Jun 2026", "13"],
               ["S.O. 3356(E)", "23 Jun 2026", "9"], ["S.O. 4123(E)", "27 Jul 2026", "8"]]),
    "Reliance-named plants account for 30 of the 149 entries and some plants appear twice because a renewal re-lists them, so the number of distinct plants is lower than 149.",
    "The Department of Agriculture and Farmers Welfare should publish one live list of authorised plants with the expiry date of each, so that a lapsed entry such as those of November 2023 can be told from a plant that has stopped selling.",
    "register")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Department of Fertilizers:</b> publish sales and subsidy claims by plant and quarter, with the realised price per tonne.</li>
<li><b>Department of Fertilizers and NITI Aayog:</b> state claims received, paid and pending at the scheme end date before deciding on extension.</li>
<li><b>Department of Agriculture and Farmers Welfare:</b> publish one live list of authorised plants with expiry dates, and say whether the Seventh Amendment Order of 29 June 2026 makes the per-plant orders unnecessary.</li>
<li><b>State agriculture departments:</b> publish the hectares and crops reached by biogas manure, so effects on chemical fertiliser use can be measured.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''
method = '''<details class="xv-n"><summary>Method and definitions</summary><ul>
<li>FOM is fermented organic manure, a solid by-product of biogas plants; liquid FOM is the liquid form; PROM is phosphate-rich organic manure.</li>
<li>Sale (Annexure I) and production (Annexure II) are separate series in the reply and cover different dates; production to 4 March 2026 is 1.43 times the sales to 28 February 2026, and the reply does not reconcile them.</li>
<li>The implied subsidy multiplies the Rs 1,500 rate by the total tonnes sold and assumes every tonne qualifies, which the reply does not say.</li>
<li>The gazette register counts each entry in each order; plants that appear in more than one order are counted more than once.</li></ul></details>
'''
gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary><ul>
<li>Sales after 28 February 2026 and subsidy released after the same date.</li>
<li>Why sales (20.65 lakh tonnes) and production (29.57 lakh tonnes) differ, and how many tonnes were sold at what price.</li>
<li>The number of distinct authorised plants, and whether each is selling.</li>
<li>Orders before 14 November 2023, and any order after 27 July 2026.</li>
<li>The reasoning for the 27 entries lapsing: whether the plants have applied again is not shown.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps
SOURCES = ('<a href="https://sansad.in/getFile/annex/270/AS186_ZuBH8s.pdf?source=pqars">Rajya Sabha starred question 186, 10 March 2026</a> (Annexures I and II; 120 plants; 44 MoUs; 15,690 camps); '
  '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2237444">PIB, 10 March 2026</a>; '
  '<a href="https://egazette.gov.in/WriteReadData/2025/268601.pdf">Gazette of India, S.O. 5836(E), 17 December 2025</a> and the other nine orders listed in the table; '
  '<a href="https://www.teamleaseregtech.com/updates/article/57526/fertiliser-inorganic-organic-or-mixed-control-seventh-amendment-order-/">TeamLease RegTech on the Seventh Amendment Order, 6 July 2026</a>; '
  '<a href="https://github.com/herrrickshaw/vertistrat-site/pull/2">VertiStrat site register of plants (pull request 2)</a>. Sums, shares and implied subsidy computed by this blog. Analysed 18 November 2026.')
RELATED = [(f"{B}/2026/07/the-cbg-incentive-stack-every-leg-of.html", "Compressed biogas incentives: offtake, subsidy, feedstock, fertiliser, finance and tax"),
           (f"{B}/2026/09/india-has-132-compressed-biogas-plants.html", "Compressed biogas plants in India: most lack a pipeline link to city gas"),
           (f"{B}/2026/10/how-to-use-cbg-design-opensource-size.html", "How to use cbg-design-opensource: size a compressed biogas plant"),
           (f"{B}/2026/08/nature-versus-nurture-indias-fertiliser.html", "India's fertiliser-fed food security: demand forecast, import bill and gas grid")]
build("Agriculture &middot; Energy", TITLE, "Biogas plants sold 20.65 lakh tonnes of organic manure to February 2026 and drew Rs 111.72 crore of subsidy, while ten gazette orders list 149 plant clearances.", body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE))
