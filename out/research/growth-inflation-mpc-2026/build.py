"""Growth against inflation going into the RBI's 2-4 December 2026 MPC: forecasts, the quarterly path, the real repo rate.
Build from the repo root:  python3 out/research/growth-inflation-mpc-2026/build.py   (writes out/post-india-growth-inflation-rbi-mpc-december-2026.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 19 November 2026.
rbi.org.in is not reachable from the build environment, so the RBI's October figures were read from search excerpts of its
press release and from secondary reports; the post says so."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-growth-inflation-rbi-mpc-december-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- RBI MPC, 5-7 October 2026 (decision 7 October): repo rate +25 bp to 5.50%, unanimous; stance to calibrated tightening, 4-2
REPO, SDF, MSF = 5.50, 5.25, 5.75
GDP_FY27_OCT, GDP_FY27_AUG = 7.1, 6.7                    # October raised the FY27 projection by 40 bp (reports); the earlier figure is 6.7
assert round(GDP_FY27_OCT - GDP_FY27_AUG, 1) == 0.4
CPI_FY27 = 5.2
# Quarterly projections as reported: Q2 (Jul-Sep) 4.9, Q3 (Oct-Dec) 6.0, Q4 (Jan-Mar) 5.7; growth Q2 7.2, Q3 6.9, Q4 6.8
CPI_PROJ = {"Q2": 4.9, "Q3": 6.0, "Q4": 5.7}
GDP_PROJ = {"Q2": 7.2, "Q3": 6.9, "Q4": 6.8}

# ---- MoSPI CPI 2024=100, monthly all-India combined (same series as the October CPI post)
CPI_M = {"Apr": 3.48, "May": 3.93, "Jun": 4.38, "Jul": 4.45, "Aug": 4.83, "Sep": 5.54, "Oct": 6.09}
CPI_Q1 = (CPI_M["Apr"] + CPI_M["May"] + CPI_M["Jun"]) / 3
CPI_Q2 = (CPI_M["Jul"] + CPI_M["Aug"] + CPI_M["Sep"]) / 3
assert round(CPI_Q1, 2) == 3.93 and round(CPI_Q2, 2) == 4.94
assert abs(CPI_Q2 - CPI_PROJ["Q2"]) < 0.1                 # the RBI's Q2 projection matches the three published months
# the RBI's FY27 5.2% against a simple average of its four quarters (approximate: the RBI weights months, not quarters)
FY_AVG = (CPI_Q1 + CPI_PROJ["Q2"] + CPI_PROJ["Q3"] + CPI_PROJ["Q4"]) / 4
assert abs(FY_AVG - CPI_FY27) < 0.1, FY_AVG
# what November and December must average for Q3 to land at 6.0
ND_AVG = (CPI_PROJ["Q3"] * 3 - CPI_M["Oct"]) / 2
assert round(ND_AVG, 2) == 5.96

# ---- GDP (MoSPI first estimate for April-June 2026, released 31 August 2026): real +7.8%, nominal +10.3%
GDP_Q1, GDP_Q1_RBI_AUG, GDP_Q1_POLL = 7.8, 7.0, 7.1
NOMINAL_Q1 = 10.3
DEFL_Q1 = ((1 + NOMINAL_Q1 / 100) / (1 + GDP_Q1 / 100) - 1) * 100
assert round(DEFL_Q1, 1) == 2.3
assert round(GDP_Q1 - GDP_Q1_RBI_AUG, 1) == 0.8
G = {"Q1": GDP_Q1, **GDP_PROJ}
GDP_AVG = sum(G.values()) / 4
assert abs(GDP_AVG - GDP_FY27_OCT) < 0.1, GDP_AVG        # the quarterly path averages to the 7.1% year figure within rounding
C = {"Q1": round(CPI_Q1, 1), **CPI_PROJ}
GAP = {q: round(G[q] - C[q], 1) for q in G}
assert GAP == {"Q1": 3.9, "Q2": 2.3, "Q3": 0.9, "Q4": 1.1}, GAP

# ---- real policy rate: repo less each inflation reading
REAL = [("Against October CPI, 6.09%", REPO - CPI_M["Oct"]), ("Against the RBI&rsquo;s Q3 path, 6.0%", REPO - CPI_PROJ["Q3"]),
        ("Against the RBI&rsquo;s Q4 path, 5.7%", REPO - CPI_PROJ["Q4"]), ("Against the 2026-27 projection, 5.2%", REPO - CPI_FY27)]
REAL = [(n, round(v, 2)) for n, v in REAL]
assert [v for _, v in REAL] == [-0.59, -0.5, -0.2, 0.3], REAL
HIKE = 0.25
REAL_HIKE = [round(REPO + HIKE - x, 2) for x in (CPI_M["Oct"], CPI_PROJ["Q3"], CPI_PROJ["Q4"], CPI_FY27)]
assert REAL_HIKE == [-0.34, -0.25, 0.05, 0.55], REAL_HIKE

# ---- external forecasts for FY27 (IMF WEO October 2026: 7.0% for FY27 and FY28, up from 6.4% in July; Moody's: 7%, reports differ on its prior figure)
FC = [("IMF, July", 6.4), ("RBI, August", GDP_FY27_AUG), ("IMF, October", 7.0), ("Moody&rsquo;s, 2026", 7.0), ("RBI, October", GDP_FY27_OCT)]
assert [v for _, v in FC] == sorted(v for _, v in FC)

TITLE = "Growth 7.1% against inflation 6.09%: the numbers before the RBI's 2-4 December meeting"
assert 55 <= len(TITLE) <= 90, len(TITLE)

top = top_line([
    ("7.1%", f" is the RBI&rsquo;s October projection for 2026-27 real growth, raised 0.4 points (the first quarter came in at 7.8%), while its inflation projection is {CPI_FY27}% and October&rsquo;s reading is 6.09%."),
    (f"{GAP['Q3']:.1f} points", f" is the gap between projected growth ({G['Q3']}%) and inflation ({C['Q3']}%) in October&ndash;December, down from {GAP['Q1']:.1f} points in April&ndash;June."),
    (f"&minus;{abs(REAL[0][1]):.2f} points", f" is the repo rate of {REPO:.2f}% less October&rsquo;s inflation, so the policy rate is below inflation; a 25 basis point rise on 2&ndash;4 December would still leave it at &minus;{abs(REAL_HIKE[0]):.2f}."),
])

s1 = insight(
    "Forecasters moved to about 7% for 2026-27 growth, and the RBI is at the top of the range",
    bars("The RBI and the IMF both raised their 2026-27 growth forecasts to about 7% since July",
         [(n, v) for n, v in FC], accent="RBI, October", unit="%", vmax=8,
         sub="Real GDP growth forecast for 2026-27, per cent, as each source reported it. The first-quarter outcome was 7.8%.",
         source="RBI (October 2026 statement, as reported); IMF World Economic Outlook, October 2026 (as reported); Moody&rsquo;s (as reported).")
    + numbers(["Source", "2026-27 growth forecast (%)", "Note"],
              [["IMF, July 2026", "6.4", "Replaced in October"],
               ["RBI, August 2026", f"{GDP_FY27_AUG}", f"Implied by the 0.4-point October raise to {GDP_FY27_OCT}"],
               ["IMF, October 2026", "7.0", "Also 7.0% for 2027-28"],
               ["Moody&rsquo;s", "7.0", "Reports differ on its earlier figure (6.0% in September reports, 6.5% in a November report)"],
               ["RBI, October 2026", f"{GDP_FY27_OCT}", "Quarterly path: 7.2, 6.9 and 6.8 for the second to fourth quarters"],
               ["First quarter, outcome", f"{GDP_Q1}", f"RBI&rsquo;s August expectation was {GDP_Q1_RBI_AUG}; a Reuters poll expected {GDP_Q1_POLL}"]]),
    f"The first quarter came in {GDP_Q1 - GDP_Q1_RBI_AUG:.1f} points above the RBI&rsquo;s own August expectation, and the October projection of {GDP_FY27_OCT}% already assumes growth slows to 6.8% by January&ndash;March, so the RBI&rsquo;s path already has a slowdown of one point built in.",
    "The 30 November release of July&ndash;September growth, which the RBI projected at 7.2%, is the first data point to compare with that path before the committee meets.",
    "growth")

s2 = insight(
    f"Growth&rsquo;s margin over inflation narrows from {GAP['Q1']:.1f} points to {GAP['Q3']:.1f} by October&ndash;December",
    bars("Projected growth minus inflation shrinks to 0.9 points in October to December",
         [("April&ndash;June (outcomes)", GAP["Q1"], f"growth {G['Q1']}%, inflation {C['Q1']}%"),
          ("July&ndash;September (growth projected)", GAP["Q2"], f"growth {G['Q2']}%, inflation {C['Q2']:.1f}%"),
          ("October&ndash;December (projected)", GAP["Q3"], f"growth {G['Q3']}%, inflation {C['Q3']}%"),
          ("January&ndash;March (projected)", GAP["Q4"], f"growth {G['Q4']}%, inflation {C['Q4']}%")],
         accent="October&ndash;December (projected)", unit=" points",
         sub="Real GDP growth less CPI inflation, percentage points, by quarter of 2026-27. Inflation for April&ndash;September is the average of the three published monthly readings; October to March are the RBI&rsquo;s projections.",
         source="MoSPI (GDP release of 31 August 2026; CPI releases); RBI October 2026 projections, as reported. Differences computed here.")
    + numbers(["Quarter", "Real growth (%)", "CPI inflation (%)", "Gap (points)", "Basis"],
              [["April&ndash;June", f"{G['Q1']}", f"{C['Q1']}", f"{GAP['Q1']}", "Both outcomes"],
               ["July&ndash;September", f"{G['Q2']}", f"{C['Q2']:.1f}", f"{GAP['Q2']}", "Growth projected (data due 30 November); inflation published"],
               ["October&ndash;December", f"{G['Q3']}", f"{C['Q3']}", f"{GAP['Q3']}", "Both RBI projections; October CPI is 6.09%"],
               ["January&ndash;March", f"{G['Q4']}", f"{C['Q4']}", f"{GAP['Q4']}", "Both RBI projections"]]),
    f"For the gap to hold at 0.9 points in October&ndash;December the average of November and December must come in near {ND_AVG:.2f}%, below October&rsquo;s 6.09%, so the RBI&rsquo;s own path already assumes inflation eases from here.",
    "The 14 December release of November inflation shows whether the October peak is being followed by the easing that the projection assumes.",
    "gap")

s3 = insight(
    "The repo rate is 0.59 points below inflation, and a quarter-point rise leaves it negative",
    bars("The repo rate sits below current inflation and above only the full-year projection",
         [(n, v) for n, v in REAL], accent="Against October CPI, 6.09%", unit=" points",
         sub="Repo rate of 5.50% less each inflation figure, percentage points; negative means the policy rate is below inflation. This is simple subtraction, not the RBI&rsquo;s own real-rate estimate.",
         source="RBI (repo rate, projections, as reported); MoSPI (October CPI). Computed here.")
    + numbers(["Inflation measure", "Value (%)", "Repo 5.50% less inflation", "Repo 5.75% less inflation"],
              [["October CPI", "6.09", f"{REAL[0][1]:.2f}", f"{REAL_HIKE[0]:.2f}"],
               ["RBI projection, October&ndash;December", "6.0", f"{REAL[1][1]:.2f}", f"{REAL_HIKE[1]:.2f}"],
               ["RBI projection, January&ndash;March", "5.7", f"{REAL[2][1]:.2f}", f"{REAL_HIKE[2]:.2f}"],
               ["RBI projection, 2026-27", "5.2", f"{REAL[3][1]:+.2f}", f"{REAL_HIKE[3]:+.2f}"]]),
    f"After the October rise the repo rate of {REPO:.2f}% is below October inflation of 6.09% and below the RBI&rsquo;s own October&ndash;March path, and only a year-average inflation of {CPI_FY27}% puts it above, which fits the committee&rsquo;s statement that rate cuts are off the table.",
    "The RBI&rsquo;s December policy statement should state the real policy rate it is targeting and the inflation measure it is using, so the size of any rise can be read against that target.",
    "realrate")

s4 = insight(
    "Growth data on 30 November, the MPC on 2-4 December and CPI on 14 December frame the call",
    flow([("30 Nov (reported date)", "Real GDP growth for July&ndash;September 2026; the RBI projected 7.2%, and April&ndash;June came in at 7.8%."),
          ("2&ndash;4 Dec", f"The MPC meets. The repo rate is {REPO}%, the standing deposit facility {SDF}% and the marginal standing facility {MSF}%; the October stance is calibrated tightening, adopted 4&ndash;2.", True),
          ("14 Dec", "November CPI. The RBI&rsquo;s path needs November and December near 5.96% for October&ndash;December to average 6.0%.")])
    + numbers(["Source", "Expectation for December (a forecast, not a decision)"],
              [["SBI Research", "A 50 basis point rise"],
               ["Nomura", "A 25 basis point rise to 5.75%"]],
              "Show the forecasts reported"),
    "Published expectations for December run from a 25 to a 50 basis point rise, and the October statement said the next move can only be a rise or a pause, so the open question is the size of any rise or whether the committee holds.",
    "The December statement is the document to read for the committee&rsquo;s vote split, its new quarterly projections and whether it changes the 7.1% and 5.2% figures set in October.",
    "dates")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Reserve Bank of India:</b> publish the monthly path behind the quarterly inflation projection, so the 5.96% needed for November and December can be checked against the committee&rsquo;s own numbers.</li>
<li><b>Reserve Bank of India:</b> state in each policy statement the real policy rate it is aiming at and the inflation measure used, since the same 5.50% repo is &minus;0.59 against October and +0.30 against the year projection.</li>
<li><b>MoSPI:</b> publish the implicit GDP deflator alongside real and nominal growth in each release, so the gap between a 2.3% deflator and 6.09% consumer inflation can be read without computing it.</li>
<li><b>Forecasters:</b> state the base year and series of any growth forecast, since the first-quarter outcome and revisions moved to the new 2022-23 base.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Real growth is the year-on-year change in real GDP at constant prices. CPI inflation is the year-on-year change in the all-India combined index (base 2024=100), the series used in this blog&rsquo;s October inflation post.</li>
<li>Quarterly inflation for April&ndash;September is the simple average of the three published monthly readings (3.93% and 4.94%). The RBI&rsquo;s Q2 projection of 4.9% matches the second figure. A simple average of the four quarters gives about 5.1%, within 0.1 points of the RBI&rsquo;s 5.2%, which is consistent with rounding and month weights, not an error in either.</li>
<li>The 5.96% for November&ndash;December is (6.0 &times; 3 &minus; 6.09) / 2. The implicit deflator is (1.103 / 1.078 &minus; 1) = 2.3%, from the reported nominal and real first-quarter growth.</li>
<li>The inflation target is 4% with a tolerance band of 2% either side. Under the RBI Act the target is treated as missed only if average inflation is above 6% (or below 2%) for three consecutive quarters; the RBI&rsquo;s projections put October&ndash;December at 6.0% and January&ndash;March at 5.7%.</li>
<li>The RBI statement itself (rbi.org.in) could not be opened from this blog&rsquo;s build environment. Its October figures were read from excerpts of the press release and from secondary reports, and the quarterly projections should be checked against the statement.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The RBI&rsquo;s quarterly tables from the primary document: the quarterly inflation figures (4.9%, 6.0%, 5.7%) and growth figures (7.2%, 6.9%, 6.8%) are as reported by secondary sources quoting the statement. The vote on the rate was reported as unanimous and the stance change as 4&ndash;2.</li>
<li>The IMF&rsquo;s inflation forecast for India: outlets map its 5.0% and 4.4% to calendar and fiscal years differently, so none is used here.</li>
<li>Moody&rsquo;s timing and base: reports date its move to 7% to September (from 6.0%) and to November (from 6.5%). Only the 7% level is used.</li>
<li>The 30 November date of the July&ndash;September GDP release comes from one report; MoSPI&rsquo;s release calendar was not opened. The GDP deflator is a computed approximation from reported rounded growth rates.</li>
<li>The December decision. SBI Research and Nomura are forecasts, reported by secondary outlets, and other forecasters differ.</li>
<li>Why October&ndash;December inflation is expected to ease: the statement lists drivers (monsoon, energy, food) but this piece did not test them.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=63742">RBI, Monetary Policy Statement, October 2026</a> (press release; read through excerpts, see method note); '
    '<a href="https://www.scconline.com/blog/post/2026/10/09/rbi-hikes-repo-rate-to-5-50-percent-october-2026/">SCC Online, 9 October 2026</a> and '
    '<a href="https://www.corplawupdates.in/updates/rbi-mpc-minutes-october-2026-repo-rate-5-50-rate-cuts-off-table">Corp Law Updates, MPC minutes, October 2026</a> (secondary: rate, stance vote, rate cuts off the table); '
    '<a href="https://www.moneylife.in/article/repo-rate-raised-to-550-percentage-by-rbi-amid-challenging-global-uncertainty-inflation/81869.html">Moneylife, October 2026</a> (secondary: projections); '
    '<a href="https://www.onmanorama.com/news/business/2026/08/31/india-gdp-grows-in-q1-beats-expectations-despite-iran-war.html">Onmanorama, 31 August 2026</a> (MoSPI first-quarter estimate: real 7.8%, nominal 10.3%, RBI expectation 7.0%); '
    '<a href="https://theprint.in/economy/imf-forecasts-7-growth-for-india-in-fy27-fy28-flags-fragile-global-uncertainties/3069987/">ThePrint, October 2026</a> and '
    '<a href="https://www.moneylife.in/article/imf-lifts-indias-fy27-outlook-to-7-percentage-as-domestic-demand-holds-firm/81940.html">Moneylife, October 2026</a> (IMF World Economic Outlook: 7.0% for 2026-27); '
    '<a href="https://theprint.in/economy/moodys-sharply-raises-indias-fy27-gdp-forecast-to-7-pc-flags-inflation-risks/3046256/">ThePrint</a> and '
    '<a href="https://newsonair.gov.in/moodys-ratings-raises-indias-gdp-growth-forecast-for-current-fiscal-year-to-7-from-6-5/">All India Radio, 11 November 2026</a> (Moody&rsquo;s 7%; prior figure differs between the two); '
    '<a href="https://www.newkerala.com/news/a/sbi-research-retains-call-50-bps-december-rate-hike-889.htm">NewKerala, 2 November 2026</a> and '
    '<a href="https://lapaasvoice.com/nomura-expects-25-bps-rbi-rate-hike-in-december-as-inflation-risks-rise/">Lapaas Voice</a> (SBI Research and Nomura December forecasts); '
    'MoSPI monthly CPI releases (as used in this blog&rsquo;s October inflation post). Differences, averages and the implicit deflator computed by this blog. Analysed 19 November 2026.')

RELATED = [
    (f"{B}/2026/11/indias-retail-inflation-609-in-october.html", "India's retail inflation: 6.09% in October 2026, above the RBI's 6% upper limit"),
    (f"{B}/2026/11/indias-wholesale-inflation-1229-in.html", "India's wholesale inflation: 12.29% in October 2026, fuel and power up 32.84%"),
    (f"{B}/2026/11/indias-crude-basket-120-in-october-89.html", "India's crude basket: $120 in October, $89 on 10 November; pump prices frozen"),
    (f"{B}/2026/11/indias-rupee-rs-9369-dollar-on-11.html", "India's rupee: Rs 93.69 a dollar on 11 November, 3% above its early-October low"),
    (f"{B}/2026/08/the-price-and-tap-two-levers-behind.html", "RBI's rate lever: a corridor around the repo rate, targeting the call rate"),
]

build("Economy &middot; RBI", TITLE,
      "The RBI raised its 2026-27 growth projection to 7.1% in October while retail inflation reached 6.09%; four charts set the quarterly path, the real repo rate and the three dates before the 2&ndash;4 December meeting.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
