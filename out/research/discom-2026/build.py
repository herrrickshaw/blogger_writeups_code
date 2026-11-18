"""Distribution losses and smart meters under RDSS (Ministry of Power replies, July-August 2026).
Build from the repo root:  python3 out/research/discom-2026/build.py   (writes out/post-india-discom-losses-smart-meters-rdss-2026.html)
Analysed 18 November 2026."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-discom-losses-smart-meters-rdss-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- AT&C loss, national (Lok Sabha USQ 2063 and 2032, 30 Jul 2026; Rajya Sabha USQ 1752, 3 Aug 2026) ----
ATC = [("FY14", 22.62), ("FY21", 21.91), ("FY23", 15.11), ("FY24", 16.12), ("FY25", 15.04)]
assert round(21.91 - 15.04, 2) == 6.87 and round(22.62 - 15.04, 2) == 7.58
PAT_FY25 = 2701
ACS_ARR_FY14, ACS_ARR_FY25 = 0.78, 0.06
assert round(ACS_ARR_FY14 - ACS_ARR_FY25, 2) == 0.72
TARGET_LOW, TARGET_HIGH = 12, 15
assert 15.04 > TARGET_HIGH and round(15.04 - TARGET_HIGH, 2) == 0.04

# ---- Smart meters under RDSS, as on 30 June 2026 (Rajya Sabha USQ 943 and 950, 27 Jul 2026) ----
SANCTIONED, INSTALLED, ALL_SCHEMES = 203388297, 57331930, 72400000
assert round(100 * INSTALLED / SANCTIONED, 1) == 28.2
assert round(INSTALLED / 1e7, 2) == 5.73 and round(SANCTIONED / 1e7, 2) == 20.34
CONSUMER_S, CONSUMER_I = 197930130, 55296526
assert round(100 * CONSUMER_I / CONSUMER_S, 1) == 27.9
STATES = {"Bihar": (2607153, 2302379), "Assam": (6445127, 5544334), "Maharashtra": (24004866, 12973051), "Uttar Pradesh": (28526730, 9753753), "Rajasthan": (14736692, 4758801),
          "Gujarat": (16787587, 5201496), "West Bengal": (21035262, 700182), "Kerala": (13383001, 192942), "Punjab": (8981414, 14662), "Tamil Nadu": (30490774, 9746)}
PCT = {k: 100 * i / s for k, (s, i) in STATES.items()}
assert round(PCT["Bihar"], 1) == 88.3 and round(PCT["Tamil Nadu"], 2) == 0.03 and round(PCT["Punjab"], 2) == 0.16 and round(PCT["Kerala"], 1) == 1.4
TN_S = STATES["Tamil Nadu"][0]
assert round(TN_S / SANCTIONED * 100, 1) == 15.0                  # Tamil Nadu is 15% of all sanctioned meters
GAP_BIG3 = sum(STATES[k][0] - STATES[k][1] for k in ("Tamil Nadu", "West Bengal", "Kerala", "Punjab"))
assert round(GAP_BIG3 / 1e7, 2) == 7.30

# ---- Money (Lok Sabha USQ 2063, 2032) ----
OUTLAY, GBS, LOSS_REDN, SMART = 303758, 97631, 153000, 131000
assert LOSS_REDN + SMART == 284000 and round(100 * (LOSS_REDN + SMART) / OUTLAY, 1) == 93.5 and round(100 * GBS / OUTLAY) == 32

# ---- Discoms: FY25 target vs actual (Lok Sabha USQ 2032 annexure; selected rows read) ----
DISCOMS = [("Arunachal Pradesh PD", 28.00, 46.20), ("PuVVNL, Uttar Pradesh", 22.75, 30.70), ("EDAN, Andaman and Nicobar", 17.00, 24.14), ("JBVNL, Jharkhand", 24.00, 28.19),
           ("KESCO, Kanpur", 10.65, 14.29), ("WBSEDCL, West Bengal", 15.50, 17.17), ("APEPDCL, Andhra Pradesh", 11.00, 7.70), ("APCPDCL, Andhra Pradesh", 11.54, 7.95),
           ("NBPDCL, Bihar", 19.00, 14.49), ("SBPDCL, Bihar", 25.00, 16.35)]
GAPS = [(n, round(a - t, 2)) for n, t, a in DISCOMS]
assert dict(GAPS)["Arunachal Pradesh PD"] == 18.20 and dict(GAPS)["SBPDCL, Bihar"] == -8.65
MISSED = sum(1 for _, g in GAPS if g > 0)
assert MISSED == 6 and len(GAPS) - MISSED == 4

TITLE = "Discom losses: AT&C down to 15.04% in FY25, smart meters 28% installed"
assert 55 <= len(TITLE) <= 82, len(TITLE)

top = top_line([
    ("15.04%", " is the national AT&C loss for FY25, down from 21.91% in FY21 but still above the 12 to 15% the scheme aims for; distribution utilities made a profit after tax of Rs 2,701 crore for the first time."),
    ("5.73 crore", " smart meters were installed under RDSS by 30 June 2026 of 20.34 crore sanctioned, 28%; the total across all schemes is 7.24 crore."),
    ("0.03%", " of Tamil Nadu's 3.05 crore sanctioned meters were installed, and Kerala 1.4%, Punjab 0.16%; Bihar was at 88%."),
])

s1 = insight(
    "Distribution losses fell from 21.91% in FY21 to 15.04% in FY25, and rose in FY24",
    bars("AT&C losses are 6.87 points below FY21 and 0.04 points above the top of the target range",
         ATC, accent="FY25", unit="%", ref=(15, "upper end of the 12 to 15% target"),
         sub="National aggregate technical and commercial loss of distribution utilities, % of energy input. FY26 will be published by PFC around January 2027.",
         source="Lok Sabha unstarred questions 2063 and 2032 (30 July 2026); Rajya Sabha unstarred question 1752 (3 August 2026).")
    + numbers(["Measure", "FY14", "FY25"],
              [["AT&C loss", "22.62%", "15.04%"], ["Gap between average cost of supply and average revenue, Rs a unit", "0.78", "0.06"],
               ["Distribution utilities, profit after tax", "&ndash;", "Rs 2,701 crore, first profit since the Electricity Act 2003"],
               ["Rural supply, hours a day", "12.5", "22.6 (FY26 per Lok Sabha reply 1896)"],
               ["Transmission loss", "&ndash;", "3 to 4% a year"]]),
    "A fall of 6.87 points in four years is real, but FY24 was higher than FY23 at 16.12%, and a profit of Rs 2,701 crore on an aggregate base is small against the scheme&rsquo;s outlay of Rs 3,03,758 crore.",
    "The Ministry of Power should publish FY26 loss and profit figures by utility as soon as PFC&rsquo;s report is ready, and state in the meantime whether FY26 is on the FY25 path.",
    "losses")

s2 = insight(
    "Smart meters installed: 88% of the Bihar sanction, 0.03% of Tamil Nadu's",
    bars("Installed smart meters as a share of sanction run from 88% in Bihar to 0.03% in Tamil Nadu",
         [(k, round(v, 2)) for k, v in sorted(PCT.items(), key=lambda kv: -kv[1])], accent="Tamil Nadu", unit="%",
         sub="Smart meters installed under RDSS divided by meters sanctioned, per state, as on 30 June 2026. Ten states shown; national 28.2%.",
         source="Rajya Sabha unstarred questions 943 and 950, 27 July 2026, state-wise annexure.")
    + numbers(["State", "Sanctioned", "Installed"], [[k, f"{s:,}", f"{i:,}"] for k, (s, i) in STATES.items()] + [["All states and UTs", f"{SANCTIONED:,}", f"{INSTALLED:,}"]]),
    "Four states with the lowest installation, Tamil Nadu, West Bengal, Kerala and Punjab, hold 7.30 crore sanctioned meters that are not yet installed, which is why the national rate sits near 28% while some states are almost done.",
    "The Ministry of Power should publish quarterly installation against sanction by state with the tender and delay status of each, so that the four states with almost no installation are visible as a group.",
    "meters")

s3 = insight(
    "RDSS has sanctioned Rs 2.84 lakh crore, 93.5% of its Rs 3.04 lakh crore outlay",
    bars("Loss-reduction and smart-metering sanctions use 93.5% of the scheme outlay",
         [("Scheme outlay", OUTLAY), ("Central grant (estimated)", GBS), ("Loss-reduction works sanctioned", LOSS_REDN), ("Smart metering sanctioned", SMART)],
         accent="Smart metering sanctioned", unit="₹ crore",
         sub="Rs crore. Sanctions are 1.53 lakh crore for loss reduction and 1.31 lakh crore for smart metering; the sunset date is 31 March 2028.",
         source="Lok Sabha unstarred questions 2063 and 2032; CEA, Report on Status of Metering, August 2026.")
    + numbers(["Item", "Value"],
              [["Scheme outlay", "Rs 3,03,758 crore"], ["Estimated central grant", "Rs 97,631 crore (32%)"], ["Loss-reduction works sanctioned", "Rs 1.53 lakh crore"], ["Smart metering sanctioned", "Rs 1.31 lakh crore"],
               ["Aim", "AT&C loss of 12 to 15% and average cost of supply minus revenue to zero"], ["Fund release", "linked to utilities&rsquo; operational and financial performance"]]),
    "Sanctions use almost the whole outlay while installed smart meters are 28% of sanction, so the scheme has committed money faster than it has delivered meters.",
    "The Ministry of Power should publish money released against meters installed by state, so the cost per installed meter can be compared with the sanctioned cost.",
    "money")

s4 = insight(
    "Of 10 utilities read, six missed their FY25 loss target and four beat it",
    bars("Arunachal Pradesh missed its FY25 target by 18.2 points; SBPDCL beat its by 8.65",
         [(n, g) for n, g in sorted(GAPS, key=lambda kv: -kv[1])], accent="PuVVNL, Uttar Pradesh", unit=" points", fmt=lambda v: f"{v:+.2f} points",
         sub="FY25 actual AT&C loss minus FY25 target under RDSS, percentage points; positive means the target was missed. Ten of 59 utilities, read from the annexure.",
         source="Lok Sabha unstarred question 2032, 30 July 2026, annexure of utility-wise targets and achievements.")
    + numbers(["Utility", "FY25 target, %", "FY25 actual, %"], [[n, f"{t:.2f}", f"{a:.2f}"] for n, t, a in DISCOMS]),
    "PuVVNL in Uttar Pradesh recorded 30.70% against a target of 22.75% and a baseline of 31.95%, so the largest state by consumers is essentially where it started.",
    "The Ministry of Power should publish for every utility the share of its loss reduction that came from billing efficiency and the share from collection, so that a utility far from target can be diagnosed.",
    "discoms")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Power:</b> publish quarterly smart-meter installation against sanction by state, with the tender status of each.</li>
<li><b>Ministry of Power:</b> publish funds released against meters installed and loss reduced, by state.</li>
<li><b>PFC:</b> publish FY26 utility-wise AT&amp;C loss with billing and collection efficiency, earlier than January 2027.</li>
<li><b>Standing Committee on Energy:</b> ask for the four lowest-installation states to explain their delays, since the committee heard the Power Ministry and REC on 30 October 2026.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''
method = '''<details class="xv-n"><summary>Method and definitions</summary><ul>
<li>AT&amp;C loss is the energy lost in distribution plus the revenue not collected, as a share of energy input. FY14 figures are from a different baseline series.</li>
<li>Installation share divides smart meters installed under RDSS by meters sanctioned under RDSS in each state; meters installed under state plans are excluded and total 1.51 crore nationally (7.24 crore less 5.73 crore).</li>
<li>The utility gap is FY25 actual minus FY25 target, in percentage points.</li></ul></details>
'''
gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary><ul>
<li>FY26 losses, which PFC&rsquo;s report is expected to publish by January 2027.</li>
<li>Why installation in Tamil Nadu, West Bengal, Kerala and Punjab is so low; the replies give counts, not reasons.</li>
<li>All 59 utilities: ten rows of the annexure were read; the other 49 were not.</li>
<li>Any finding of the Standing Committee on Energy, which met on 30 October 2026 for a briefing and has not published a report.</li>
<li>A conflict in the record: a Ministry of Power reply gives national FY25 loss as 15.04%, while another published figure is 16.16%; the blog covered the difference in an earlier post.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps
SOURCES = ('<a href="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU2063_7Fcnh4.pdf">Lok Sabha unstarred question 2063, 30 July 2026</a> (AT&amp;C losses; outlay); '
  '<a href="https://sansad.in/getFile/lsapps/loksabhaquestions/annex/188/AU2032_YRxzHa.pdf?source=lsapps">Lok Sabha unstarred question 2032, 30 July 2026</a> (utility-wise targets); '
  '<a href="https://sansad.in/getFile/annex/271/AU943_6mhBlx.pdf?source=pqars">Rajya Sabha unstarred question 943, 27 July 2026</a> and <a href="https://sansad.in/getFile/annex/271/AU950_Xld7cM.pdf?source=pqars">question 950</a> (smart meters by state); '
  '<a href="https://sansad.in/getFile/annex/271/AU1752_Pg7za4.pdf?source=pqars">Rajya Sabha unstarred question 1752, 3 August 2026</a>; '
  '<a href="https://cea.nic.in/api/dashboardReports/view-pdf/en/7c5a51f3-6637-4267-8f4d-b19ad1cc9d51">CEA, Report on Status of Metering, August 2026</a>; '
  '<a href="https://prsindia.org/parliament-committees">PRS, schedule of standing committees</a> (Energy committee, 30 October 2026). Shares and gaps computed by this blog. Analysed 18 November 2026.')
RELATED = [(f"{B}/2026/09/the-ministry-of-power-published-two.html", "India's power distribution losses for FY25: 2 ministry figures, 16.16% and 15.04%"),
           (f"{B}/2026/10/how-to-use-discom-debt-and-revenue.html", "How to use discom-debt-and-revenue-models: a scenario calculator for electricity distribution"),
           (f"{B}/2026/08/discom-debt-relief-token-charge.html", "Power distribution company debt: a token charge calculator for debt relief"),
           (f"{B}/2026/09/pngrb-wants-prepaid-smart-meters-on.html", "PNGRB smart meters: prepaid on new gas connections from 2027, all by 2030")]
build("Energy &middot; Power", TITLE, "National distribution losses fell to 15.04% in FY25 and discoms made a Rs 2,701 crore profit, while 28% of the sanctioned smart meters are installed and four states have almost none.", body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE))
