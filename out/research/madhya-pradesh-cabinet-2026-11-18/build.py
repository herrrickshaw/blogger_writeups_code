"""Madhya Pradesh cabinet of Wednesday 18 November 2026 at Gandhi Sagar: five industrial parks, the three different totals reported for them, per-park ratios,
and the Kurlasi chemical park set against the BHAVYA-Rasayan scheme rules.
Build from the repo root:  python3 out/research/madhya-pradesh-cabinet-2026-11-18/build.py            (writes out/post-madhya-pradesh-parks-18-november-2026.html)
                           python3 out/research/madhya-pradesh-cabinet-2026-11-18/build.py --check    (arithmetic and asserts only)
Every figure is from the source named beside it, or computed below with an assert. Analysed 21 November 2026.
Official documents (excerpts of their text): PIB release of 24 Jul 2026 and the PMINDIA copy; Gazette notification of 10 Aug 2026; Department of Chemicals and Petrochemicals scheme page
(5 Oct 2026) and the BHAVYA Rasayan flyer. Reports (search excerpts, several of them the full opening of the article): Business Standard (English and Hindi, 18 Nov), ANI (18 Nov),
IANS (18 Nov, as carried by Punjab Kesari and hi INDiA), Swarajya (19 Nov), Times of India (19 Nov; headline and first paragraph only), Patrika (18 Nov), Raj Express (18 Nov),
Peepals (19 Nov), DesiMachines (18 Nov; a trade blog), DailyConnects (18 Nov).
Not found: the cabinet note or the state release, the Kurlasi proposal, any central selection under BHAVYA-Rasayan, and any explanation of the gap between the totals."""
import datetime as dt
import html as _h
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
OUT = ROOT / "out/post-madhya-pradesh-parks-18-november-2026.html"
STEPS = 8


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. dates
step(1, "dates and weekday checks")
for d, wd in [(D(2026, 7, 24), "Friday"), (D(2026, 8, 10), "Monday"), (D(2026, 11, 18), "Wednesday"), (D(2026, 11, 30), "Monday")]:
    assert d.strftime("%A") == wd, d
assert (D(2026, 11, 30) - D(2026, 11, 18)).days == 12            # cabinet to the deadline for state proposals to BHAVYA-Rasayan
assert (D(2026, 11, 18) - D(2026, 7, 24)).days == 117            # scheme approval to the state cabinet
assert (D(2026, 8, 10) - D(2026, 7, 24)).days == 17              # Union Cabinet approval to the gazette notification

# ---- 2. the park figures as the Chief Minister gave them (Business Standard, ANI, IANS, Swarajya) and the three totals
step(2, "park figures, unit conversions and the three totals")
ACRE_HA = 0.40468564
assert round(3_500 * ACRE_HA) == 1_416                           # ANI/IANS/Swarajya 3,500 acres is Business Standard's 1,416 hectares: same area, two units
assert round(100 * ACRE_HA) == 40                                # ANI/IANS 100 acres is Business Standard/Swarajya 40 hectares
PARKS = [  # name, hectares, Rs crore, jobs
    ("Agro park, Basai (Mandsaur)", 178.0, 3_200, 14_000),
    ("Chemical park, Kurlasi (Mandsaur)", 1_416.0, 15_000, 100_000),
    ("Bio-pharma park, Ratlam", 453.0, 18_000, 25_000),
    ("Textile park, Bhainsola (Dhar)", 341.10, 6_150, 35_000),
    ("Research and innovation park, Ujjain", 40.0, 237, None),
]
INV_SUM = sum(p[2] for p in PARKS)
JOBS_SUM = sum(p[3] for p in PARKS if p[3])
HA_SUM = round(sum(p[1] for p in PARKS), 2)
assert INV_SUM == 42_587 and JOBS_SUM == 174_000 and HA_SUM == 2_428.1
assert sum(p[2] for p in PARKS[:4]) == 42_350                    # the four parks without Ujjain
CM_INV, CM_JOBS = 70_650, 314_000                                # Chief Minister (Business Standard, Swarajya): 'over' and 'more than'
TOI_INV, TOI_JOBS = 55_650, 270_000                              # Times of India, state industries department estimate: 'more than 2.7 lakh'
IANS_INV, IANS_JOBS = 42_450, 174_000                            # IANS: four projects
assert 3_200 + 15_000 + 18_100 + 6_150 == IANS_INV               # IANS uses Rs 18,100 crore for Ratlam; the other reports use Rs 18,000 crore
assert INV_SUM - 237 + 100 == IANS_INV                           # so IANS's total is the five park figures, less Ujjain, with Ratlam at 18,100
GAP_CM, GAP_TOI = CM_INV - INV_SUM, TOI_INV - INV_SUM
assert GAP_CM == 28_063 and GAP_TOI == 13_063
assert CM_INV - TOI_INV == 15_000                                # the two totals differ by exactly the chemical park's figure; no source says whether that is the reason
assert CM_JOBS - JOBS_SUM == 140_000 and TOI_JOBS - JOBS_SUM == 96_000 and CM_JOBS - TOI_JOBS == 44_000
PER_JOB_ALL = [round(i * 1e7 / j / 1e5, 1) for i, j in [(CM_INV, CM_JOBS), (TOI_INV, TOI_JOBS), (IANS_INV, IANS_JOBS)]]
assert PER_JOB_ALL == [22.5, 20.6, 24.4]                         # Rs lakh of investment per job implied by each total

# ---- 3. per-park ratios
step(3, "per-park ratios")
LAKH_JOB = {p[0]: round(p[2] * 1e7 / p[3] / 1e5, 2) for p in PARKS if p[3]}
assert LAKH_JOB == {"Agro park, Basai (Mandsaur)": 22.86, "Chemical park, Kurlasi (Mandsaur)": 15.0, "Bio-pharma park, Ratlam": 72.0, "Textile park, Bhainsola (Dhar)": 17.57}
assert f"{72 / 15:.1f}" == "4.8"
CR_HA = {p[0]: round(p[2] / p[1], 1) for p in PARKS}
assert CR_HA["Agro park, Basai (Mandsaur)"] == 18.0 and CR_HA["Chemical park, Kurlasi (Mandsaur)"] == 10.6 and CR_HA["Bio-pharma park, Ratlam"] == 39.7
assert CR_HA["Textile park, Bhainsola (Dhar)"] == 18.0 and CR_HA["Research and innovation park, Ujjain"] == 5.9
JOBS_HA = {p[0]: round(p[3] / p[1], 1) for p in PARKS if p[3]}
assert JOBS_HA == {"Agro park, Basai (Mandsaur)": 78.7, "Chemical park, Kurlasi (Mandsaur)": 70.6, "Bio-pharma park, Ratlam": 55.2, "Textile park, Bhainsola (Dhar)": 102.6}
SHARE_LAND, SHARE_INV, SHARE_JOBS = 100 * 1_416 / HA_SUM, 100 * 15_000 / INV_SUM, 100 * 100_000 / JOBS_SUM
assert [f"{SHARE_LAND:.1f}", f"{SHARE_INV:.1f}", f"{SHARE_JOBS:.1f}"] == ["58.3", "35.2", "57.5"]
assert round(sum(p[1] for p in PARKS[:4]) + 182.289) == 2_570     # DesiMachines' 2,570 hectares is the four parks plus Gwalior phase II (182.289 ha)
assert f"{HA_SUM + 182.289:.1f}" == "2610.4"

# ---- 4. BHAVYA-Rasayan (PIB 24 Jul; gazette 10 Aug; Department of Chemicals flyer): the arithmetic of the scheme against Kurlasi
step(4, "BHAVYA-Rasayan arithmetic against the Kurlasi park")
assert 3_000 + 30 == 3_030                                        # outlay: common infrastructure plus administration
assert 3 * 1_000 == 3_000                                         # three parks at a grant of up to Rs 1,000 crore
assert 3 * (1_000 + 500) == 4_500                                 # the flyer's 'at least Rs 4,500 crore' of investment across the three parks
CENTRE, STATE_MIN = 1_000, 500
assert [f"{100 * v / 15_000:.1f}" for v in (CENTRE, STATE_MIN, CENTRE + STATE_MIN)] == ["6.7", "3.3", "10.0"]
assert 3_500 > 2_000 and 3_500 / 2_000 == 1.75                    # Kurlasi against the scheme's minimum of 8 sq km, about 2,000 acres
assert round(8 * 247.105) == 1_977                                # 8 sq km is 1,977 acres, which the scheme rounds to 2,000
assert 3_500 > 1_000                                              # the general BHAVYA scheme caps a park at 1,000 acres (this blog's post of 27 Oct 2026, from the PIB release)
assert round(1_416 / 100, 2) == 14.16                             # Kurlasi in square kilometres

# ---- 5. other decisions the same day (IANS, Patrika)
step(5, "other decisions")
assert round(414.17 - 321.94, 2) == 92.23 and f"{100 * (414.17 - 321.94) / 321.94:.1f}" == "28.6"        # Rewa Medical College funding
assert f"{855 * 1e7 / 6_000 / 1e5:.2f}" == "14.25"                # Ujjain forest zoo: Rs 855 crore, 6,000 jobs, Rs lakh per job
assert f"{855 / 210:.2f}" == "4.07"                               # Rs crore per hectare
assert 800 + 200 == 1_000                                         # Omkareshwar phase II: 800 MW storage and 200 MW floating solar

TITLE = "Madhya Pradesh parks 18 Nov 2026: Rs 42,587 crore listed, Rs 70,650 crore announced"
plain = _h.unescape(TITLE)
assert 55 <= len(plain) <= 90, len(plain)
assert not any(w in plain.lower().split() for w in ("you", "your", "we", "our"))
print(f"consistency checks passed (units, totals, per-park ratios, scheme arithmetic); title {len(plain)} characters", flush=True)
if "--check" in sys.argv:
    sys.exit(0)

from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402


def _rs(v, unit="crore"):
    s = f"{v:,.2f}".rstrip("0").rstrip(".")
    return f"Rs {s} {unit}"


step(6, "writing sections")
top = top_line([
    ("Rs 28,063 crore", f" is the gap between the Chief Minister&rsquo;s total of Rs 70,650 crore and the five park figures he gave (Rs {INV_SUM:,} crore); the jobs gap is 140,000, and no report read explains either."),
    ("4.8 times", " is the investment per job at the bio-pharma park (Rs 72 lakh) against the chemical park (Rs 15 lakh), on the cabinet&rsquo;s own figures."),
    ("30 Nov 2026", " is the deadline for state proposals to BHAVYA-Rasayan, which will fund three chemical parks nationally; Kurlasi was cleared by the state 12 days earlier, and no central selection is reported."),
])

tvo = ('<table class="gb-table"><thead><tr><th>Kind</th><th>What this piece includes</th></tr></thead><tbody>'
       '<tr><td><b>Decided</b></td><td>On Wednesday 18 November 2026 the Madhya Pradesh cabinet, meeting at Gandhi Sagar in Mandsaur district, approved five industrial parks, the second phase of a telecom manufacturing zone at Gwalior, a new industrial area at Pandhurna and a battery storage and floating solar project at Omkareshwar.</td></tr>'
       '<tr><td><b>Targets</b></td><td>Investment and jobs for each park, as the Chief Minister gave them. They are projections of what private firms might bring, not construction budgets.</td></tr>'
       '<tr><td><b>Outcomes</b></td><td>None. No plot allotment, tender or investment commitment for any of the five parks was found.</td></tr>'
       '<tr><td><b>Conflict</b></td><td>Three totals are in print for the same meeting (Rs 70,650, 55,650 and 42,450 crore), and one report reads the chemical park as approved under a central scheme that has not yet chosen its parks.</td></tr>'
       '</tbody></table>\n')

TOT = [("Chief Minister, as reported by Business Standard and Swarajya", CM_INV), ("Times of India, state industries department estimate", TOI_INV),
       ("IANS, four parks", IANS_INV), ("Sum of the five park figures (computed)", INV_SUM)]
s1 = insight(
    "Three totals in print for one meeting: Rs 70,650, 55,650 and 42,450 crore",
    bars("Three totals for five parks, against the sum of the park figures: Rs 42,587 crore",
         TOT, accent=TOT[3][0], unit=" crore", fmt=lambda v: _rs(v), vmax=75_000,
         sub=f"Rs crore of projected investment. The Chief Minister&rsquo;s total exceeds the sum of the five park figures by Rs {GAP_CM:,} crore and the Times of India&rsquo;s by Rs {GAP_TOI:,} crore (computed); the IANS total is the park figures with Ujjain left out and Ratlam at Rs 18,100 crore. The Chief Minister&rsquo;s and the Times of India&rsquo;s totals differ by exactly Rs 15,000 crore, the chemical park&rsquo;s figure; no report says whether that is the reason.",
         source="Business Standard and Swarajya, 18 and 19 November 2026; Times of India, 19 November 2026 (headline and first paragraph); IANS, 18 November 2026 (via Punjab Kesari and hi INDiA); park figures from Business Standard, ANI and IANS. Secondary.")
    + flow([("18 Nov 2026 (Wednesday)", "Special cabinet meeting at Gandhi Sagar, the ninth &lsquo;destination cabinet&rsquo; (Patrika); the Chief Minister briefs the press and gives the park figures (Business Standard, ANI, IANS).", True),
            ("18 Nov 2026", "IANS reports four projects, Rs 42,450 crore and over 1.74 lakh jobs; Business Standard reports five parks, over Rs 70,650 crore and more than 314,000 jobs."),
            ("19 Nov 2026 (Thursday)", "Times of India attributes Rs 55,650 crore and more than 2.7 lakh jobs to the state industries department&rsquo;s estimate; Swarajya repeats the Rs 70,650 crore total."),
            ("19 Nov 2026", "Peepals notes the different totals and that the numbers are projections, not commitments.")])
    + numbers(["Source", "Investment (Rs crore)", "Jobs", "Basis"],
              [["Chief Minister (Business Standard, Swarajya, DailyConnects)", "Over 70,650", "More than 314,000", "Five parks; the park figures listed in the same reports add to 42,587 and 174,000"],
               ["Times of India", "55,650", "More than 2.7 lakh", "Five projects; &lsquo;the state industries department estimates&rsquo;; headline and first paragraph only"],
               ["IANS", "42,450", "Over 1.74 lakh", "Four projects; Ratlam given as Rs 18,100 crore"],
               ["Raj Express (Hindi)", "&lsquo;45 thousand crore&rsquo; in the headline, &lsquo;more than 50 thousand crore&rsquo; in the subhead", "&lsquo;Lakhs&rsquo;", "Excerpt only; the two figures differ within the same article"],
               ["Sum of the five park figures (computed)", f"{INV_SUM:,}", f"{JOBS_SUM:,} (four parks; Ujjain gives none)", "3,200 + 15,000 + 18,000 + 6,150 + 237"],
               ["Ratlam", "18,000 (state text, per DesiMachines; Business Standard) or 18,100 (IANS)", "25,000", "A Rs 100 crore difference; not reconciled"],
               ["Chemical park area", "3,500 acres (ANI, IANS, Swarajya) or 1,416 hectares (Business Standard)", "", "The same area: 3,500 acres is 1,416 hectares, checked"],
               ["Ujjain park area", "100 acres (ANI, IANS) or 40 hectares (Business Standard, Swarajya)", "", "The same area to the nearest hectare, checked"]],
              "Show every total and the unit checks"),
    "Only the IANS total can be rebuilt from the park figures, and the Chief Minister's total exceeds them by Rs 28,063 crore and 140,000 jobs, which none of the reports read explains.",
    "The Madhya Pradesh industries department should publish the cabinet note listing every project and its investment and jobs behind the Rs 70,650 crore and 3.14 lakh jobs.",
    "totals")

PJ = [(n, LAKH_JOB[n]) for n in ["Bio-pharma park, Ratlam", "Agro park, Basai (Mandsaur)", "Textile park, Bhainsola (Dhar)", "Chemical park, Kurlasi (Mandsaur)"]]
s2 = insight(
    "Investment per job: Rs 15 lakh at the chemical park, Rs 72 lakh at the bio-pharma park",
    bars("Projected investment per projected job: Rs 15 lakh to Rs 72 lakh across four parks",
         PJ, accent="Bio-pharma park, Ratlam", unit=" lakh", fmt=lambda v: f"Rs {v:g} lakh", vmax=80,
         sub="Rs lakh of projected investment per projected job, computed here from the Chief Minister&rsquo;s figures; 1 crore is 100 lakh. The Ujjain research park has no jobs figure. The reports word the jobs differently: &lsquo;direct and indirect&rsquo; for the chemical park (IANS), &lsquo;direct&rsquo; for the textile park (Swarajya), and no qualifier elsewhere.",
         source="Business Standard, ANI and IANS, 18 November 2026; Swarajya, 19 November 2026; Peepals, 19 November 2026 (agro park ratio). Secondary. Ratios computed here.")
    + numbers(["Park", "Area (ha)", "Investment (Rs crore)", "Jobs", "Rs crore per ha", "Jobs per ha"],
              [[p[0], f"{p[1]:g}", f"{p[2]:,}", f"{p[3]:,}" if p[3] else "not given", f"{CR_HA[p[0]]:g}", f"{JOBS_HA[p[0]]:g}" if p[3] else "n/a"] for p in PARKS]
              + [["Five parks (computed)", f"{HA_SUM:,.1f}", f"{INV_SUM:,}", f"{JOBS_SUM:,} (four parks)", f"{INV_SUM / HA_SUM:.1f}", f"{JOBS_SUM / sum(p[1] for p in PARKS[:4]):.1f}"]]
              + [["Implied by each total, Rs lakh per job", "", f"Chief Minister {PER_JOB_ALL[0]:g}; Times of India {PER_JOB_ALL[1]:g}; IANS {PER_JOB_ALL[2]:g}", "", "", ""]],
              "Show per-park areas, ratios and the checks"),
    "The bio-pharma park projects 4.8 times the capital per job of the chemical park, so its Rs 18,000 crore carries the highest capital per job among the four parks that give a jobs figure.",
    "The industries department should state, for each park, whether jobs are direct, indirect or both and the year they are expected, so that the ratios can be compared.",
    "perjob")

s3 = insight(
    "Chemical park: public support is about 10% of the projected Rs 15,000 crore",
    bars("Scheme money as a share of the Kurlasi park's projected Rs 15,000 crore investment",
         [("Centre grant, up to", 100 * CENTRE / 15_000), ("State contribution, at least", 100 * STATE_MIN / 15_000), ("Both together, at the stated levels", 100 * (CENTRE + STATE_MIN) / 15_000)],
         accent="Both together, at the stated levels", unit="%", fmt=lambda v: f"{v:.1f}%", vmax=12,
         sub="Per cent of the projected Rs 15,000 crore, computed. The grant is up to Rs 1,000 crore and the State&rsquo;s share at least Rs 500 crore, per park, under BHAVYA-Rasayan; the scheme pays for common infrastructure only, and the rest of the projected investment is expected from private firms. Reports call the scheme &lsquo;BHAVYA&rsquo;; Rasayan is inferred from the size rule below.",
         source="PIB release, 24 July 2026; Gazette notification, 10 August 2026; Department of Chemicals and Petrochemicals scheme page and flyer, October 2026 (official). Park figure from Business Standard and ANI, 18 November 2026. Ratios computed here.")
    + flow([("24 Jul 2026 (Friday)", "Union Cabinet approves BHAVYA-Rasayan: Rs 3,030 crore over 2026-27 to 2030-31 for three dedicated chemical parks chosen by challenge (PIB)."),
            ("10 Aug 2026 (Monday)", "Scheme notified in the Gazette of India; each park at least 8 sq km of encumbrance-free land (gazette)."),
            ("18 Nov 2026 (Wednesday)", "Madhya Pradesh cabinet approves a 3,500-acre chemical park at Kurlasi, reported &lsquo;under BHAVYA&rsquo; (ANI, Business Standard).", True),
            ("30 Nov 2026 (Monday)", "Last date for states to submit proposals to the Department of Chemicals and Petrochemicals, 12 days after the state cabinet (scheme page).")])
    + numbers(["Item", "Value", "Source and status"],
              [["Scheme", "BHAVYA-Rasayan: three greenfield chemical parks nationally, chosen by challenge; outlay Rs 3,030 crore (Rs 3,000 crore for common infrastructure, Rs 30 crore administration)", "PIB; gazette (official)"],
               ["Support per park", "Grant of up to Rs 1,000 crore from the Centre; at least Rs 500 crore from the State; the Department says each park gets public investment of more than Rs 1,500 crore, and at least Rs 4,500 crore goes to the three together", "PIB; flyer (official)"],
               ["State obligations", "Encumbrance-free land at the State&rsquo;s own cost, external infrastructure up to the park, all clearances, any cost above the central grant, and at least 51% of the equity of a state implementing agency", "Flyer (official)"],
               ["Size rule", f"At least 8 sq km, about 2,000 acres. Kurlasi is 3,500 acres, or 14.16 sq km, which is 1.75 times the minimum (computed)", "PIB; ANI; Business Standard"],
               ["Which BHAVYA", "The general BHAVYA scheme caps a park at 1,000 acres; a 3,500-acre park fits only the chemical-park scheme. This is an inference from the sizes, not a statement in the reports", "This blog&rsquo;s post of 27 October 2026 (from the PIB release); computed"],
               ["Selection", "The three highest-ranked states on 100 marks; one criterion is proximity to the sea, within 20 km of the coastline, and Mandsaur is inland; the weights were not read. No selection has been reported", "Flyer (official; excerpt)"],
               ["Where the Kurlasi proposal stands", "Cleared by the State cabinet. Whether it has been submitted, and the State&rsquo;s own contribution, were not found", "Not stated in any report read"]],
              "Show the scheme terms and how Kurlasi compares"),
    "The cabinet approved a state proposal and not a central selection, because only three parks nationally will be chosen by challenge and state proposals close on 30 November, 12 days after the meeting.",
    "The Madhya Pradesh industries department should state whether the Kurlasi proposal has been submitted under BHAVYA-Rasayan and what contribution the State has committed.",
    "chemical")

s4 = insight(
    "The chemical park holds 58% of the land and 35% of the investment",
    bars("Chemical park's share of the five parks: 58% of land, 35% of investment, 57% of jobs",
         [("Share of land (2,428 ha)", SHARE_LAND), ("Share of listed jobs (174,000)", SHARE_JOBS), ("Share of investment (Rs 42,587 crore)", SHARE_INV)],
         accent="Share of investment (Rs 42,587 crore)", unit="%", fmt=lambda v: f"{v:.1f}%", vmax=70,
         sub="The Kurlasi chemical park as a per cent of the five parks together, computed from the Chief Minister&rsquo;s figures. Jobs are shares of the four parks that give a figure; Ujjain gives none. The cabinet did not publish a site-development cost for any park except the Ujjain research park.",
         source="Business Standard, ANI and IANS, 18 November 2026; DesiMachines, 18 November 2026 (on development costs). Shares computed here.")
    + numbers(["Decision on 18 November 2026", "Figure", "Source and status"],
              [["Telecom manufacturing zone, phase II, Gwalior", "182.289 hectares at Talpura and Kulaith; adding it to the four parks gives 2,570 hectares, the figure DesiMachines prints (checked); with Ujjain, 2,610.4 hectares", "ANI (via The News Mill); IANS; DesiMachines"],
               ["Pandhurna", "A multi-product industrial area at Sausar, in place of a long-proposed special economic zone", "Business Standard; IANS"],
               ["Omkareshwar floating solar, phase II", "An 800 MW battery storage system and a 200 MW floating solar unit; no cost was found", "Business Standard; IANS; Patrika"],
               ["Ujjain forest zoo and rescue centre", "Rs 855 crore on 210 hectares with about 6,000 direct and indirect jobs: Rs 4.07 crore a hectare and Rs 14.25 lakh a job (computed)", "IANS; Patrika"],
               ["MSME", "&lsquo;MP MSME Limited&rsquo; with Rs 10 crore initially; the MSME Infrastructure Development Scheme continued five years at Rs 1,507 crore", "IANS; Patrika"],
               ["Rewa Medical College", "Funding raised from Rs 321.94 crore to Rs 414.17 crore, up Rs 92.23 crore or 28.6% (computed)", "IANS"],
               ["Investment promotion", "CII named national partner of the state industrial development corporation for three years; industrial proposals above 500 jobs to go through a committee and not the cabinet", "Business Standard; Raj Express (Hindi, excerpt)"],
               ["Other", "Special NDPS courts in six cities; Shri Radhe University at Morena from 2027-28; aviation viability gap funding extended to four years (domestic) and two years (international); the two-child norm for state employees removed", "IANS; Patrika; Peepals"],
               ["Allocations", "Projects and allocations of more than Rs 2,700 crore, as a lump sum; the items behind it were not listed in the reports read", "ANI"]],
              "Show the other decisions and the checks"),
    "The chemical park uses 58.3% of the land for 35.2% of the investment, so it has the lowest investment per hectare, Rs 10.6 crore, among the four parks that give a jobs figure.",
    "The industries department should publish a site-development cost for each park, so that the public cost of the land and infrastructure can be set against the projected private investment.",
    "land")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Madhya Pradesh industries department:</b> publish the cabinet note of 18 November 2026 with every project behind the Rs 70,650 crore and 3.14 lakh jobs, and say which items are not parks.</li>
<li><b>Madhya Pradesh industries department:</b> state for each park whether the jobs are direct, indirect or both, and the year they are expected; give areas in hectares with the acre conversion.</li>
<li><b>Madhya Pradesh industries department:</b> state in each release which BHAVYA scheme a park falls under, and whether a state approval is a proposal or a central selection.</li>
<li><b>Department of Chemicals and Petrochemicals:</b> publish the list of state proposals received by 30 November 2026 and the marks given on each criterion when the three parks are chosen.</li>
<li><b>Madhya Pradesh industries department:</b> publish a site-development cost and a funding source for each of the five parks.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Park figures are as the Chief Minister gave them at the press conference after the cabinet, as carried by Business Standard, ANI, IANS and Swarajya. They are projections of private investment and jobs, not construction budgets or commitments.</li>
<li>Sums, differences, per-job and per-hectare ratios and shares are computed here and each is checked by an assertion in the builder. Acres and hectares were converted at 0.40468564 hectares to the acre.</li>
<li>BHAVYA-Rasayan terms are from the official release, the gazette notification and the Department of Chemicals and Petrochemicals; the match between that scheme and the Kurlasi park is an inference from the 3,500-acre size and is marked as one.</li>
<li>Business Standard, ANI, IANS, Swarajya, Patrika and Raj Express were read as excerpts, several of them the full opening of the article; the Times of India was read as its headline and first paragraph. News sites are secondary, and DesiMachines is a trade blog.</li>
<li>Weekdays were checked against the calendar.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>What makes up the Chief Minister&rsquo;s Rs 70,650 crore and 3.14 lakh jobs, or the Times of India&rsquo;s Rs 55,650 crore and 2.7 lakh jobs, beyond the five parks; the cabinet note and the state release were not found.</li>
<li>Whether the Ratlam figure is Rs 18,000 crore or Rs 18,100 crore; the state text is reported as 18,000 by a trade blog, which is secondary.</li>
<li>Whether the Kurlasi proposal has been submitted under BHAVYA-Rasayan, the State&rsquo;s own contribution, and the weights of the selection criteria.</li>
<li>Any site-development cost or funding source for any park except the Ujjain research park, and any plot allotment, tender or investor commitment.</li>
<li>The text of the Raj Express figures of Rs 45,000 and over Rs 50,000 crore beyond their headlines, and the Times of India article beyond its first paragraph.</li>
<li>The cost of the Omkareshwar phase II project, and the items behind the Rs 2,700 crore of allocations.</li>
</ul></details>
'''

step(7, "assembling body")
body = STYLE + top + tvo + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://www.business-standard.com/economy/news/madhya-pradesh-approves-five-new-industrial-parks-targets-314-000-jobs-126111801156_1.html">Business Standard, 18 November 2026</a>, '
    '<a href="https://www.aninews.in/news/national/general-news/mp-cabinet-approves-agro-chemical-textile-parks-to-boost-investment-employment-grants-over-rs-2700-cr-for-various-development-works20261118153747">ANI, 18 November 2026</a>, '
    '<a href="https://english.punjabkesari.com/india/mp-unveils-mega-industrial-push-across-four-western-districts-eyes-over-174-lakh-jobs">IANS, 18 November 2026 (via Punjab Kesari)</a>, '
    '<a href="https://swarajyamag.com/news-brief/mp-unveils-massive-industrial-expansion-five-new-parks-to-generate-over-314000-jobs-and-attract-70650-crore-investment">Swarajya, 19 November 2026</a> and '
    '<a href="https://www.patrika.com/mandsaur-news/mp-mohan-yadav-cabinet-decisions-gandhi-sagar-meeting-18-november-2026-21061729">Patrika, 18 November 2026</a> (secondary: the cabinet decisions and park figures); '
    '<a href="https://timesofindia.indiatimes.com/city/bhopal/mp-cabinet-backs-five-industrial-projects-with-rs-55650-crore-investment-potential/articleshow/135990595.cms">Times of India, 19 November 2026</a> (secondary, headline and first paragraph: the Rs 55,650 crore total); '
    '<a href="https://rajexpress.com/madhya-pradesh-news/mandsaur-gandhi-sagar-mp-cabinet-decisions-mandsaur-industrial-parks-investment-employment-projects-mp-news-hindi">Raj Express, 18 November 2026</a> (secondary, excerpt, in Hindi); '
    '<a href="https://peepalsglobal.com/bharat/article/mandsaur-agro-park-kurlasi-chemical-park-mp-cabinet-gandhi-sagar-2026-11-19">Peepals, 19 November 2026</a> and '
    '<a href="https://desimachines.com/news/mandsaur-chemical-park-mp-cabinet/">DesiMachines, 18 November 2026</a> (a trade blog: the Ratlam figure and the BHAVYA-Rasayan link); '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2288863&amp;reg=48&amp;lang=2">PIB release on BHAVYA-Rasayan, 24 July 2026</a>, '
    '<a href="http://chemicals.gov.in/sites/default/files/inline-files/Gazette-Notification-BHAVYA-RASAYAN_0.pdf">Gazette notification, 10 August 2026</a>, '
    '<a href="https://chemicals.gov.in/bharat-audyogik-vikas-yojana-rasayan-bhavya-rasayan-scheme">Department of Chemicals and Petrochemicals scheme page</a> and '
    '<a href="https://chemicals.gov.in/sites/default/files/ticker/Bhavya_Rasayan_Flyer.pdf">BHAVYA Rasayan flyer</a> (official). '
    'Sums, ratios and shares computed by this blog. Analysed 21 November 2026.')
B = "https://blog.vertistratsolution.com"
RELATED = [(f"{B}/2026/10/india-will-spend-rs-33660-crore-on.html", "India will spend Rs 33,660 crore on ready-made factory parks")]

step(8, "writing page")
build("Policy &middot; Madhya Pradesh", TITLE,
      "Madhya Pradesh's cabinet approved five industrial parks on 18 November 2026; this piece sets out the three different investment totals reported for them, the investment per job and per hectare, and how the Kurlasi chemical park stands against the BHAVYA-Rasayan scheme.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(plain), "chars in title")
