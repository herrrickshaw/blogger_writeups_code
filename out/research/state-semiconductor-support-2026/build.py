"""State semiconductor capital support on one basis, 21 November 2026: Semicon 2.0 central rates plus the State rule in each of six states, rebuilt from
the state documents and checked against the comparison Andhra Pradesh published on 18 November 2026.
Build from the repo root:  python3 out/research/state-semiconductor-support-2026/build.py            (writes out/post-state-semiconductor-support-india-2026.html)
                           python3 out/research/state-semiconductor-support-2026/build.py --check    (arithmetic and asserts only)
Every figure is from the source named beside it, or computed below with an assert. Analysed 21 November 2026.
Document text seen as search excerpts or page text: Tamil Nadu Semiconductor Ecosystem Scheme 2026 (official PDF, fetched); Uttar Pradesh Semiconductor Policy 2024 (official PDF);
Gujarat Semiconductor Policy 2022-27 (official PDF and department page); Odisha Semiconductor Manufacturing and Fabless Policy 2023 (official PDF) and its resolution of 1 Aug 2025;
India Semiconductor Mission page for Semicon 2.0 fabs (official page).
Search excerpts only: EY Policy Alert 1 Sep 2026, KPMG Flash News 3 Sep 2026, Business Standard 31 Aug 2026, Industrial Economist 31 Aug 2026, New Indian Express (15 Jul, 13 Aug,
17 Oct, 19 Nov 2026), ETGovernment 18 Aug 2026, Business Standard 25 Oct 2026, Deloitte note on the UP site (May 2024), Ideas for India 27 Aug 2026, BusinessLine 18 Nov 2026.
Not found: G.O.Ms.No.87 of Andhra Pradesh, the text of Odisha's third amendment, and the Madhya Pradesh policy text itself (its rule is as the press reports it)."""
import datetime as dt
import html as _h
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
OUT = ROOT / "out/post-state-semiconductor-support-india-2026.html"
STEPS = 8


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


D = dt.date
# ---- 1. dates
step(1, "dates and weekday checks")
for d, wd in [(D(2026, 7, 15), "Wednesday"), (D(2026, 8, 12), "Wednesday"), (D(2026, 8, 31), "Monday"), (D(2026, 10, 15), "Thursday"),
              (D(2026, 11, 16), "Monday"), (D(2026, 11, 18), "Wednesday")]:
    assert d.strftime("%A") == wd, d
assert (D(2026, 8, 31) - D(2026, 7, 15)).days == 47      # Cabinet approval to notification of Semicon 2.0
assert (D(2026, 11, 16) - D(2026, 8, 31)).days == 77     # notification to Andhra Pradesh's order
assert (D(2026, 10, 15) - D(2026, 8, 31)).days == 45     # notification to Tamil Nadu's launch (the scheme was notified on 6 October)
assert (D(2026, 8, 12) - D(2026, 7, 15)).days == 28      # Cabinet approval to the Odisha cabinet amendment

# ---- 2. central rates and the State rules
step(2, "central rates and the State rule in each state")
CATS = ["Silicon fab", "Compound, photonics, sensor and discrete fab", "Advanced packaging", "Legacy packaging"]
C2 = dict(zip(CATS, [40, 35, 35, 25]))     # Semicon 2.0, % of eligible capex, pari passu (EY 1 Sep; KPMG 3 Sep; Business Standard 31 Aug; ISM fabs page)
C1 = 50                                    # first programme: 50% of eligible capex (Deloitte note on the UP site; Odisha official quoted by ETGovernment)
MIN_SILICON = 20_000                       # Rs crore, minimum capital investment for a silicon fab (ISM page; Business Standard)
STATES = ["Andhra Pradesh", "Tamil Nadu", "Odisha", "Uttar Pradesh", "Madhya Pradesh", "Gujarat"]
TN = dict(zip(CATS, [25, 25, 25, 20]))     # Track 1 table, official scheme: State % of eligible capex approved by the Centre


def state_pct(state, c, cat=None, odisha=25):
    """State share as % of eligible capex, given the central rate c, using the rule each state's own text gives."""
    if state == "Andhra Pradesh":
        return c                           # matches 100% of the Centre's capital support (BusinessLine 18 Nov; TNIE 19 Nov)
    if state == "Tamil Nadu":
        return TN[cat]
    if state == "Odisha":
        return odisha                      # 25% of eligible capex (TNIE 13 Aug 2026); ETGovernment 18 Aug reports 35%
    if state == "Uttar Pradesh":
        return 0.5 * c                     # 50% of the capital subsidy approved by the Centre (policy clause 6.1.1)
    if state == "Madhya Pradesh":
        return min(25, 0.5 * c)            # 25% of eligible capex or 50% of the central incentive, whichever is lower (Business Standard 25 Oct 2026)
    if state == "Gujarat":
        return 0.4 * c                     # 40% of the capex assistance given by the Centre (policy clause 4.2.1)
    raise KeyError(state)


COMB = {s: {c: C2[c] + state_pct(s, C2[c], c) for c in CATS} for s in STATES}
COMB_OD35 = {c: C2[c] + state_pct("Odisha", C2[c], c, odisha=35) for c in CATS}
SIL, CMP, ADV, LEG = CATS

# the comparison Andhra Pradesh published must reproduce for silicon fabs
AP_LIST = {"Andhra Pradesh": 80, "Odisha": 65, "Tamil Nadu": 65, "Uttar Pradesh": 60, "Madhya Pradesh": 60, "Gujarat": 56}
for s, v in AP_LIST.items():
    assert COMB[s][SIL] == v, (s, COMB[s][SIL], v)
assert COMB["Andhra Pradesh"][CMP] == 70 and COMB["Andhra Pradesh"][ADV] == 70 and COMB["Andhra Pradesh"][LEG] == 50     # AP's own 70% and 50%
assert 30 + 18 == 48 and 18 / 30 == 0.6                                    # AP machines and materials: 18% on the Centre's 30%
assert [C2[SIL] + TN[SIL], C2[CMP] + TN[CMP], C2[ADV] + TN[ADV], C2[LEG] + TN[LEG]] == [65, 60, 60, 45]
assert 30 + 15 == 45                                                       # Tamil Nadu machines and materials: Centre 30% plus State 15%

# ---- 3. the combined table, every category
step(3, "combined support by category, with the Odisha 35% case")
assert COMB["Odisha"] == {SIL: 65, CMP: 60, ADV: 60, LEG: 50}
assert COMB["Uttar Pradesh"] == {SIL: 60, CMP: 52.5, ADV: 52.5, LEG: 37.5}
assert COMB["Madhya Pradesh"] == {SIL: 60, CMP: 52.5, ADV: 52.5, LEG: 37.5}     # at 35%, half of the central rate is 17.5, under the 25 ceiling; at 25%, 12.5
assert COMB["Gujarat"] == {SIL: 56, CMP: 49, ADV: 49, LEG: 35}
assert COMB["Tamil Nadu"] == {SIL: 65, CMP: 60, ADV: 60, LEG: 45}
assert COMB_OD35 == {SIL: 75, CMP: 70, ADV: 70, LEG: 60}
LEAD = {}
for c in CATS:
    best_other = max(COMB[s][c] for s in STATES if s != "Andhra Pradesh")
    LEAD[c] = COMB["Andhra Pradesh"][c] - best_other
assert LEAD == {SIL: 15, CMP: 10, ADV: 10, LEG: 0}
LEAD35 = {c: COMB["Andhra Pradesh"][c] - max(max(COMB[s][c] for s in STATES if s not in ("Andhra Pradesh", "Odisha")), COMB_OD35[c]) for c in CATS}
assert LEAD35 == {SIL: 5, CMP: 0, ADV: 0, LEG: -10}                         # if Odisha's State share is 35%, AP's lead shrinks and reverses for legacy packaging
assert COMB["Odisha"][LEG] == COMB["Andhra Pradesh"][LEG] == 50             # tie at 50% in legacy packaging on the 25% reading

# ---- 4. before and after the central rate cut
step(4, "before and after the central rate cut")
OLD = {"Andhra Pradesh": C1 + 0.6 * C1,          # State adds 60% of the central incentive (Ideas for India, DSCI; AP policy text not read)
       "Tamil Nadu": C1 + 0.5 * C1,              # up to 50% of the CAPEX assistance provided by the Centre (TN scheme, preamble)
       "Odisha": C1 + 25,                        # 'additional 50% of the Capex assistance' = 25% of project capex (policy clause 8.1)
       "Uttar Pradesh": C1 + 0.5 * C1,           # 50% of the capital subsidy approved by the Centre
       "Madhya Pradesh": C1 + min(25, 0.5 * C1), # lower of 25% of eligible capex or 50% of the central incentive: both 25 at a 50% central rate
       "Gujarat": C1 + 0.4 * C1}                 # 40% of the central capex assistance
assert OLD == {"Andhra Pradesh": 80, "Tamil Nadu": 75, "Odisha": 75, "Uttar Pradesh": 75, "Madhya Pradesh": 75, "Gujarat": 70}
assert 0.5 * C1 == 25                            # Odisha's two statements of the same rule agree: 50% of the central 50% is 25% of capex
LOST = {s: OLD[s] - COMB[s][SIL] for s in STATES}
assert LOST == {"Andhra Pradesh": 0, "Tamil Nadu": 10, "Odisha": 10, "Uttar Pradesh": 15, "Madhya Pradesh": 15, "Gujarat": 14}
assert OLD["Andhra Pradesh"] - C1 == 30 and COMB["Andhra Pradesh"][SIL] - C2[SIL] == 40      # AP's State share of cost: 30% then, 40% now
assert OLD["Gujarat"] - C1 == 20 and COMB["Gujarat"][SIL] - C2[SIL] == 16                    # Gujarat's: 20% then, 16% now
assert max(OLD.values()) - min(OLD.values()) == 10 and max(AP_LIST.values()) - min(AP_LIST.values()) == 24     # spread of combined rates, then and now
assert 70 <= min(OLD.values()) and max(OLD.values()) <= 80                  # DSCI report: 'combined 70-80% of cost' under the first programme

# ---- 5. state outlay on a minimum-size silicon fab (a ceiling: assumes all of the threshold is eligible capex)
step(5, "State outlay per minimum-size silicon fab")
OUTLAY = {s: MIN_SILICON * state_pct(s, C2[SIL], SIL) / 100 for s in STATES}
assert OUTLAY == {"Andhra Pradesh": 8_000, "Tamil Nadu": 5_000, "Odisha": 5_000, "Uttar Pradesh": 4_000, "Madhya Pradesh": 4_000, "Gujarat": 3_200}
assert MIN_SILICON * C2[SIL] / 100 == 8_000                               # the Centre's share of the same fab
assert OUTLAY["Andhra Pradesh"] / OUTLAY["Gujarat"] == 2.5
assert 40 <= 50                                                            # AP's State share is inside its own 50% ceiling on State incentives (from the AP cabinet post)
assert 80 <= 90                                                            # and inside the 90% all-source ceiling reported for AP

TITLE = "State chip subsidies: Andhra Pradesh leads by 15 points on silicon fabs, 0 to 10 elsewhere"
plain = _h.unescape(TITLE)
assert 55 <= len(plain) <= 90, len(plain)
assert not any(w in plain.lower().split() for w in ("you", "your", "we", "our"))
print(f"consistency checks passed (AP list reproduced, categories, before and after, outlay); title {len(plain)} characters", flush=True)
if "--check" in sys.argv:
    sys.exit(0)

from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402


def pc(v):
    return f"{v:g}%"


step(6, "writing sections")
top = top_line([
    ("6 of 6", " silicon fab percentages in Andhra Pradesh&rsquo;s 18 November comparison (80, 65, 65, 60, 60 and 56) reproduce from each state&rsquo;s own rule and the Centre&rsquo;s 40%; the sources for Andhra Pradesh and Madhya Pradesh are press reports."),
    ("15 points", " is Andhra Pradesh&rsquo;s lead for silicon fabs; it is 10 points for compound fabs and advanced packaging and 0 for legacy packaging, where Odisha ties at 50% on the 25% reading of its rule."),
    ("24 points", " is the spread in combined silicon fab support now (56% to 80%), up from 10 points (70% to 80%) under the first programme, when the Centre paid 50%."),
])

tvo = ('<table class="gb-table"><thead><tr><th>Kind</th><th>What this piece includes</th></tr></thead><tbody>'
       '<tr><td><b>Rule</b></td><td>The Centre&rsquo;s Semicon 2.0 support is 40% of eligible capital cost for silicon fabs, 35% for compound fabs and advanced packaging, and 25% for legacy packaging. Each state adds either a share of that support or a flat share of capital cost.</td></tr>'
       '<tr><td><b>Checked</b></td><td>Andhra Pradesh&rsquo;s comparison for silicon fabs, from six state rules. The same rules are then applied to the other three categories, which the comparison did not cover.</td></tr>'
       '<tr><td><b>Method note</b></td><td>The percentages are shares of the capital cost the Centre approves, before ceilings, land, power and tax benefits; they are not rupees paid.</td></tr>'
       '<tr><td><b>Outcomes</b></td><td>None found: no project has been reported as sanctioned under any of the new state rules.</td></tr>'
       '</tbody></table>\n')

rows1 = [(s, AP_LIST[s]) for s in STATES]
s1 = insight(
    "Andhra Pradesh's silicon fab comparison reproduces: 80%, 65%, 65%, 60%, 60% and 56%",
    bars("Silicon fab combined support reproduces from each state's rule and the Centre's 40%",
         rows1, accent="Andhra Pradesh", unit="%", vmax=100,
         sub="Combined Centre and State capital support for a silicon fab, per cent of eligible capital cost, rebuilt here from each state&rsquo;s own rule; each value equals the figure in the Andhra Pradesh government&rsquo;s comparison. Eligible capital cost is the part the Centre approves.",
         source="Tamil Nadu Semiconductor Ecosystem Scheme 2026; Uttar Pradesh Semiconductor Policy 2024; Gujarat Semiconductor Policy 2022-27; New Indian Express, 13 August 2026 (Odisha); Business Standard, 25 October 2026 (Madhya Pradesh); BusinessLine, 18 November 2026 (Andhra Pradesh).")
    + flow([("15 Jul 2026 (Wednesday)", "Union Cabinet approves Semicon 2.0 with Rs 1,27,500 crore (New Indian Express)."),
            ("12 Aug 2026 (Wednesday)", "Odisha cabinet approves 25% of eligible capital cost for projects the Centre approves, per the New Indian Express; ETGovernment reports 35% six days later."),
            ("31 Aug 2026 (Monday)", "Semicon 2.0 notified: 40% for silicon fabs, 35% for compound semiconductor, display fabs and advanced packaging, 25% for legacy packaging, 30% for machines and materials (EY, KPMG, Business Standard)."),
            ("15 Oct 2026 (Thursday)", "Tamil Nadu launches its scheme, notified 6 October: 25% for silicon fabs and advanced packaging, 20% for legacy packaging, and 15% for materials and equipment (official scheme, DT Next)."),
            ("16 Nov 2026 (Monday)", "Andhra Pradesh order G.O.Ms.No.87 matches the Centre&rsquo;s support rupee for rupee for fabs and packaging (BusinessLine, TNIE).", True),
            ("18 Nov 2026 (Wednesday)", "Andhra Pradesh minister&rsquo;s release compares 80% for silicon fabs with five other states (BusinessLine).")])
    + numbers(["State", "Rule in the state&rsquo;s own text", "Silicon fab, combined", "Source and status"],
              [["Andhra Pradesh", "Matches 100% of the Centre&rsquo;s capital support: 40% plus 40%", "80%", "BusinessLine and TNIE (page text); G.O.Ms.No.87 not found"],
               ["Tamil Nadu", "Flat 25% of eligible capital cost for a 300 mm silicon fab, on the Centre&rsquo;s 40%", "65%", "Official scheme, Track 1 table (document text)"],
               ["Odisha", "Additional 25% of eligible capital cost for projects the Centre approves, paid pari passu", "65%", "New Indian Express, 13 August 2026 (excerpt); ETGovernment gives 35% (conflict, below)"],
               ["Uttar Pradesh", "50% of the capital subsidy the Centre approves, so 20% of cost at the Centre&rsquo;s 40%", "60%", "Policy 2024, clause 6.1.1 (document text); written for the first programme"],
               ["Madhya Pradesh", "The lower of 25% of eligible capital cost and 50% of the central incentive, so 20%", "60%", "Business Standard, 25 October 2026 (excerpt); policy text not read"],
               ["Gujarat", "40% of the Centre&rsquo;s capex assistance, so 16% of cost", "56%", "Policy 2022-27, clause 4.2.1 (document text); written for the first programme"]],
              "Show each state's rule and the source"),
    "The comparison holds for silicon fabs on the Centre's current 40% rate, but four of the six states set their share relative to central support, so the combined figure moves whenever the Centre changes its rate.",
    "The Ministry of Electronics and Information Technology should publish, on the Semicon 2.0 portal, a table of each state's top-up expressed as a percentage of eligible capital cost for every category.",
    "silicon")

s2 = insight(
    "Andhra Pradesh's lead: 15 points for silicon fabs, 0 for legacy packaging",
    bars("Lead over the next-best state: 15 points for silicon fabs, 0 for legacy packaging",
         [(CATS[0], LEAD[SIL]), (CATS[1], LEAD[CMP]), (CATS[2], LEAD[ADV]), (CATS[3], LEAD[LEG])], accent=SIL, unit=" points", vmax=18,
         sub="Percentage points of combined Centre and State support, Andhra Pradesh minus the highest other state in that category, using the same rules as the silicon fab figures. In legacy packaging Andhra Pradesh and Odisha are both at 50% on the 25% reading of Odisha&rsquo;s rule.",
         source="Computed here from the state rules in the first section; Semicon 2.0 rates from EY, 1 September 2026 and KPMG, 3 September 2026. The comparison covered silicon fabs only.")
    + numbers(["Category (Centre&rsquo;s rate)", "Andhra Pradesh", "Tamil Nadu", "Odisha", "Uttar Pradesh", "Madhya Pradesh", "Gujarat", "Odisha if 35%"],
              [[f"{c} ({C2[c]}%)"] + [pc(COMB[s][c]) for s in STATES] + [pc(COMB_OD35[c])] for c in CATS]
              + [["Machines and materials (30%)", "48%", "45%", "55%", "not found", "not found", "not found", "65%"]],
              "Show combined support in every category and the Odisha 35% case"),
    "Andhra Pradesh is ahead in three categories and level with Odisha in the fourth, and the 15-point lead applies to a category that needs a Rs 20,000 crore investment and 40,000 wafer starts a month.",
    "The Government of Andhra Pradesh should publish G.O.Ms.No.87 and state which categories its comparison covers, so that a 15-point lead for silicon is not read as a lead everywhere.",
    "lead")

s3 = insight(
    "Five of six states lost 10 to 15 points of silicon fab support after the central rate cut",
    bars("Silicon fab support lost since the first programme: 10 to 15 points in five states",
         [(s, LOST[s]) for s in ["Uttar Pradesh", "Madhya Pradesh", "Gujarat", "Tamil Nadu", "Odisha", "Andhra Pradesh"]], accent="Andhra Pradesh", unit=" points", vmax=18,
         sub="Percentage points of combined support for a silicon fab, first programme (Centre at 50%) minus Semicon 2.0 (Centre at 40%), computed here. Tamil Nadu and Odisha rewrote their rules in 2026 and still stand 10 points below the first programme; Andhra Pradesh is level at 80%.",
         source="Computed here. First-programme rates: Deloitte note on the Uttar Pradesh site, May 2024; ETGovernment, 18 August 2026 (Odisha: 50 plus 25); Ideas for India, 27 August 2026 (state top-ups as shares of central support); DSCI report, 8 October 2026.")
    + numbers(["State", "First programme (Centre 50%)", "Semicon 2.0 (Centre 40%)", "Points lost", "Source and status"],
              [[s, pc(OLD[s]), pc(COMB[s][SIL]), f"{LOST[s]:g}", note] for s, note in [
                  ("Andhra Pradesh", "State share 60% of central support from Ideas for India and DSCI; the policy text was not read"),
                  ("Tamil Nadu", "Up to 50% of central support, per the official scheme&rsquo;s preamble; the new flat 25% replaced it"),
                  ("Odisha", "Additional 50% of central support, equal to 25% of capital cost (policy clause 8.1)"),
                  ("Uttar Pradesh", "50% of central support (policy 6.1.1)"),
                  ("Madhya Pradesh", "The 25% ceiling and 50% of central support coincide at a 50% central rate"),
                  ("Gujarat", "40% of central support (policy 4.2.1)")]],
              "Show combined support before and after the central rate cut"),
    "The spread between the highest and lowest state widened from 10 points to 24 points, because Andhra Pradesh raised its State share from 30% to 40% of cost while Gujarat's fell from 20% to 16%.",
    "Each state with a top-up written as a share of central support should state, in a notified table, what that share now yields at the Semicon 2.0 rates in every category.",
    "ratecut")

s4 = insight(
    "Minimum-size silicon fab: State outlay of Rs 3,200 to Rs 8,000 crore",
    bars("State outlay on a minimum silicon fab: Rs 3,200 crore to Rs 8,000 crore",
         [(s, OUTLAY[s]) for s in STATES], accent="Andhra Pradesh", unit=" crore", fmt=lambda v: f"Rs {v:,.0f} crore", vmax=9_000,
         sub="Rs crore, computed as the State share of capital cost times Rs 20,000 crore, the minimum capital investment for a silicon fab. It is a ceiling because only the part of the investment the Centre treats as eligible is supported; the Centre&rsquo;s own share of the same fab is Rs 8,000 crore.",
         source="Computed here. Threshold from the India Semiconductor Mission Semicon 2.0 fabs page and Business Standard, 31 August 2026; State shares as in the first section.")
    + numbers(["Item", "Value", "Source and status"],
              [["Silicon fab entry test", "300 mm wafers, 40,000 wafer starts a month or more, Rs 20,000 crore minimum capital investment and Rs 7,500 crore minimum revenue in one of three prior years", "ISM Semicon 2.0 fabs page; Business Standard"],
               ["Ratio, highest to lowest", f"{OUTLAY['Andhra Pradesh'] / OUTLAY['Gujarat']:.1f} times (Rs 8,000 crore against Rs 3,200 crore), computed", "Computed here"],
               ["Ceilings in the state texts", "Uttar Pradesh: all sources together at most 100% of eligible project cost. Andhra Pradesh: all sources reported at 90%", "UP policy 2024 (document text); AP release (see the Andhra Pradesh cabinet post)"],
               ["Fabs approved so far", "One silicon fab, Tata Electronics at Dholera, Gujarat, approved under the first programme; none under Semicon 2.0 found", "This blog&rsquo;s post of 27 October 2026 (secondary)"],
               ["Tamil Nadu second route", "Track 2 pays 25% of eligible fixed assets plus a turnover subsidy of 2% for five years to compound fabs and similar projects outside Semicon 2.0; silicon and display fabs there are customised case by case", "Official scheme, Track 2 table (document text)"]],
              "Show the entry test, the ceilings and the second route"),
    "A state matching the Centre rupee for rupee commits up to 2.5 times the money of a state at 16% of cost for the same fab, so the percentage has to be read together with the size of the project.",
    "Each state should publish, per sanctioned project, the State subsidy committed and the amount released, so that percentages in the policy can be checked against rupees.",
    "outlay")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Electronics and Information Technology:</b> publish on the Semicon 2.0 portal one table of each state&rsquo;s top-up as a percentage of eligible capital cost, by category, with the notification number.</li>
<li><b>Government of Andhra Pradesh:</b> publish G.O.Ms.No.87 and state in every comparison which categories it covers and on which central rate it rests.</li>
<li><b>Government of Odisha:</b> publish the third amendment to its semiconductor policy and state whether the State&rsquo;s share is 25% or 35% of eligible capital cost.</li>
<li><b>Governments of Uttar Pradesh, Gujarat and Madhya Pradesh:</b> amend or confirm in a notified order how their shares of central support apply to the Semicon 2.0 categories, including machines and materials.</li>
<li><b>All six state governments:</b> report, for each sanctioned project, the State subsidy committed and the amount released, in rupees.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Combined support is the Centre&rsquo;s share plus the State&rsquo;s share, each as a percentage of the eligible capital cost the Centre approves. It leaves out land, power, interest, stamp duty and payroll benefits, ceilings and the time over which money is paid.</li>
<li>The Centre&rsquo;s Semicon 2.0 rates were read in the EY alert, the KPMG note, Business Standard and the Industrial Economist, and on the India Semiconductor Mission page for fabs; the four agree (40, 35, 35 and 25).</li>
<li>State shares written as a share of central support were converted to a share of capital cost by multiplying by the central rate; this is arithmetic on the state&rsquo;s own text and is checked by an assertion for each of the six states. The Uttar Pradesh and Gujarat policies pre-date Semicon 2.0, so applying them to its categories is an assumption, flagged as such.</li>
<li>The first-programme comparison uses a central rate of 50% for fabs and for compound and packaging units, as reported by Deloitte and by an Odisha official. The Andhra Pradesh 60% is from secondary sources.</li>
<li>Document text was read for the Tamil Nadu scheme, the Uttar Pradesh policy, the Gujarat policy, the Odisha 2023 policy and the India Semiconductor Mission page. Everything else is press, read as excerpts, and is secondary.</li>
<li>Weekdays were checked against the calendar.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>Whether Odisha&rsquo;s State share is 25% or 35% of eligible capital cost. The New Indian Express, from the cabinet briefing of 12 August 2026, says 25%; ETGovernment on 18 August 2026, quoting an official through Moneycontrol, says 35%. The 25% reading reproduces Andhra Pradesh&rsquo;s figure of 65% and is used here; the 35% case is shown separately.</li>
<li>The text of Andhra Pradesh&rsquo;s G.O.Ms.No.87, Odisha&rsquo;s third amendment and Madhya Pradesh&rsquo;s policy. The Madhya Pradesh rule is as Business Standard and PTI report it.</li>
<li>Whether the Uttar Pradesh, Gujarat and Madhya Pradesh rules apply to the Semicon 2.0 categories, including machines and materials; none of the three has issued a Semicon 2.0 amendment that was found.</li>
<li>Any state subsidy sanctioned or paid under a rule above, and the eligible capital cost of any project; the percentages are not rupees paid.</li>
<li>Whether other states, such as Assam, Karnataka and Rajasthan, offer more than the six compared; they were outside the Andhra Pradesh comparison and were not rebuilt.</li>
</ul></details>
'''

step(7, "assembling body")
body = STYLE + top + tvo + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://storage.investingintamilnadu.com/Guidance/Uploads/Documents/tn-semiconductor-ecosystem-scheme-2026.pdf">Tamil Nadu Semiconductor Ecosystem Scheme 2026</a> (official scheme, document text); '
    '<a href="https://invest.up.gov.in/wp-content/uploads/go/UP-SEMICONDUCTOR-POLICY.pdf">Uttar Pradesh Semiconductor Policy 2024</a> (official policy, document text); '
    '<a href="https://gsem.gujarat.gov.in/Home/GujaratSemiconductorPolicy202227">Gujarat Semiconductor Policy 2022-27</a> (official policy page and PDF); '
    '<a href="https://investodisha.gov.in/download/Odisha-Semi-Conductor-Manufacturing-and-Fabless-Policy-2023.pdf">Odisha Semiconductor Manufacturing and Fabless Policy 2023</a> (official policy, document text); '
    '<a href="https://www.ism.gov.in/schemes/semicon2.0">India Semiconductor Mission, Semicon 2.0</a> (official page); '
    '<a href="https://www.ey.com/content/dam/ey-unified-site/ey-com/en-in/technical/alerts-hub/documents/2026/09/semicon-notified-government-unveils-support-framework.pdf">EY Policy Alert, 1 September 2026</a>, '
    '<a href="https://assets.kpmg.com/content/dam/kpmgsites/in/pdf/2026/09/KPMG-Flash-News-Semicon-2.0.pdf">KPMG Flash News, 3 September 2026</a> and '
    '<a href="https://www.business-standard.com/industry/news/govt-notifies-1-27-trillion-semicon-2-0-offers-40-fab-capex-support-126083101167_1.html">Business Standard, 31 August 2026</a> (secondary: Semicon 2.0 rates and thresholds); '
    '<a href="https://www.newindianexpress.com/story/states/odisha/2026/aug/13/odisha-widens-semicon-policy-offers-25-more-capex-support">The New Indian Express, 13 August 2026</a> and '
    '<a href="https://government.economictimes.indiatimes.com/news/policy/odisha-raises-semicon-subsidy-to-35-after-centre-trims-aid-to-40-under-ism-2-0/133314888">ETGovernment, 18 August 2026</a> (secondary, excerpts: Odisha); '
    '<a href="https://www.business-standard.com/economy/news/mp-semicon-summit-draws-15-425-cr-investment-proposals-14k-jobs-in-sight-126102500216_1.html">Business Standard, 25 October 2026</a> (secondary, excerpt: Madhya Pradesh); '
    '<a href="http://www.thehindubusinessline.com/news/national/andhra-pradesh-launches-semiconductor-policy-offers-up-to-80-capital/article71715026.ece">The Hindu BusinessLine, 18 November 2026</a> and '
    '<a href="https://www.newindianexpress.com/states/andhra-pradesh/2026/Nov/19/80-support-for-fab-units-in-andhra-pradesh">The New Indian Express, 19 November 2026</a> (secondary: Andhra Pradesh); '
    '<a href="https://www.ideasforindia.in/topics/macroeconomics/from-subsidies-to-semiconductor-clusters-why-some-states-are-pulling-ahead">Ideas for India, 27 August 2026</a> and '
    '<a href="https://invest.up.gov.in/wp-content/uploads/2024/05/Semiconductor-Sector_220524.pdf">Deloitte note on the Invest UP site, May 2024</a> (secondary: first-programme rates). '
    'Percentages, differences and rupee outlays computed by this blog. Analysed 21 November 2026.')
B = "https://blog.vertistratsolution.com"
RELATED = [(f"{B}/2026/10/india-has-approved-12-chip-plants-and.html", "India has approved 12 chip plants and paid out about 7% of the money"),
           (f"{B}/2026/09/indias-display-fab-scheme-got-two.html", "India's display fab scheme got two")]

step(8, "writing page")
build("Policy &middot; Semiconductors", TITLE,
      "A check of Andhra Pradesh's 18 November 2026 comparison of state semiconductor fab support, rebuilt from each state's own rule and the Centre's Semicon 2.0 rates, extended to compound fabs and packaging, and set against the first programme.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(plain), "chars in title")
