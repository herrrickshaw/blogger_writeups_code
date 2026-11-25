"""Doing Business in India: The Way Forward (201st Report, Standing Committee on Commerce, Rajya Sabha, presented 7 Aug 2026): recommendations, evidence cited, and the link to the Karnataka and Telangana service-delivery posts.
Build from the repo root:  python3 out/research/commerce-doing-business-2026/build.py   (writes out/post-commerce-committee-doing-business-2026.html)
Sources read: the PIB press release of 7 Aug 2026 (all 58 numbered observations and recommendations with paragraph references, read in full) and the PRS report summary (read in full).
The full report (hosted by Rajya Sabha) was NOT read: its host is outside the research environment's network allowlist. Analysed 25 November 2026.
"""
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-commerce-committee-doing-business-2026.html"
STEPS = 8


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


# ---- 1. compliance reform counts (PRS summary of the report) against the PIB 'over 47,000'
step(1, "compliance counts and cross-source check")
RCB = {"Digitised": 22_287, "Simplified": 16_108, "Decriminalised": 4_458, "Redundancy removed": 4_270}      # PRS summary, 'Reducing compliance burden'
RCB_SUM = sum(RCB.values())
assert RCB_SUM == 47_123
assert RCB_SUM > 47_000            # PIB press release, item 1: 'over 47,000 compliances ... reduced, simplified, digitized, or decriminalized'; consistent only if the four counts do not overlap
STAKE_ACTS, STAKE_COMPL, STAKE_FILINGS = 1_500, 69_233, 6_618      # PRS: a stakeholder submission about what a typical firm faces
PER_ACT = STAKE_COMPL / STAKE_ACTS
assert f"{PER_ACT:.1f}" == "46.2"
# the two numbers measure different things (reforms to central and state compliances vs a typical firm's load): the ratio below is shown only to say it is not computed
assert RCB_SUM < STAKE_COMPL

# ---- 2. the 58 numbered items of the press release, grouped by the headings printed there (item ranges)
step(2, "grouping the 58 numbered items by heading")
RANGES = [("Initiatives of the Government (compliance burden)", 1, 5), ("Delays in approvals", 6, 9), ("Timeline adherence by authorities", 10, 13),
          ("Business Reform Action Plan (BRAP)", 14, 18), ("National Single Window System (NSWS)", 19, 22), ("Decriminalisation (Jan Vishwas)", 23, 26),
          ("Business Ready (B-READY)", 27, 30), ("Fragmented regulatory framework", 31, 31), ("Logistics and infrastructure", 32, 35),
          ("Credit for MSMEs", 36, 38), ("Starting a business", 39, 39), ("Trading across borders", 40, 43), ("Government e-Marketplace", 44, 44),
          ("E-commerce dark stores", 45, 49), ("Consumer protection and quick commerce", 50, 52), ("Visit to Jammu and Kashmir and Ladakh", 53, 56), ("Way forward", 57, 58)]
cover = [n for _, a, b in RANGES for n in range(a, b + 1)]
assert cover == list(range(1, 59))                          # every item 1 to 58 in exactly one heading
CNT = {h: b - a + 1 for h, a, b in RANGES}
GROUPS = [("Approvals, timelines and single window", ["Delays in approvals", "Timeline adherence by authorities", "National Single Window System (NSWS)", "Fragmented regulatory framework"]),
          ("Compliance burden and decriminalisation", ["Initiatives of the Government (compliance burden)", "Decriminalisation (Jan Vishwas)"]),
          ("BRAP and B-READY benchmarks", ["Business Reform Action Plan (BRAP)", "Business Ready (B-READY)"]),
          ("Logistics and trade", ["Logistics and infrastructure", "Trading across borders"]),
          ("E-commerce and quick commerce", ["E-commerce dark stores", "Consumer protection and quick commerce"]),
          ("Credit, procurement and starting a business", ["Credit for MSMEs", "Starting a business", "Government e-Marketplace"]),
          ("Jammu and Kashmir and Ladakh", ["Visit to Jammu and Kashmir and Ladakh"]),
          ("Way forward", ["Way forward"])]
GC = [(g, sum(CNT[h] for h in hs)) for g, hs in GROUPS]
assert sum(c for _, c in GC) == 58
assert dict(GC) == {"Approvals, timelines and single window": 13, "Compliance burden and decriminalisation": 9, "BRAP and B-READY benchmarks": 9,
                    "Logistics and trade": 8, "E-commerce and quick commerce": 8, "Credit, procurement and starting a business": 5,
                    "Jammu and Kashmir and Ladakh": 4, "Way forward": 2}
GC.sort(key=lambda x: -x[1])

# ---- 3. the committee's evidence base (PIB press release)
step(3, "evidence base arithmetic")
MEET_H, MEET_M, MEETINGS = 8, 11, 4
MEET_MIN = MEET_H * 60 + MEET_M
assert MEET_MIN == 491 and round(MEET_MIN / MEETINGS) == 123      # an average of about 123 minutes a meeting (computed)
D_ADOPT, D_PRESENT = "5 August 2026", "7 August 2026"

# ---- 4. tie-in with the live Karnataka and Telangana posts (their own sourced figures), re-checked here
step(4, "state tie-in checks")
KA_RATE, KA_CAP = 20, 500                       # Karnataka Sakaala Act s.9: Rs 20 a day, at most Rs 500 (PRS compilation of the Act; Karnataka post)
KA_DAYS_TO_CAP = KA_CAP // KA_RATE
assert KA_DAYS_TO_CAP == 25 and KA_CAP % KA_RATE == 0
TS_MIN, TS_MID, TS_MAX = 1, 15, 30              # TS-iPASS Act 2014 clearance limits in days; 15 days provisional approval for mega projects (Telangana post)
IP_RECEIVED, IP_UNPROCESSED, IP_PCT = 12_926, 732, 94.34     # TG-iPASS dashboard, 1 Jan 2024 to 5 Nov 2026 (Telangana post)
assert round(100 * (IP_RECEIVED - IP_UNPROCESSED) / IP_RECEIVED, 2) == IP_PCT and IP_RECEIVED - IP_UNPROCESSED == 12_194

TITLE = "Doing Business in India: a committee seeks audited reform claims and one PAN-based ID"
assert 55 <= len(TITLE) <= 90, len(TITLE)
assert not any(w in TITLE.lower().replace(":", "").split() for w in ("you", "your", "we", "our"))

step(5, "writing sections")
top = top_line([
    ("58", f" numbered observations and recommendations are listed in the press release for the 201st Report of the Rajya Sabha Standing Committee on Commerce (chair Dola Sen, presented {D_PRESENT}), after {MEETINGS} meetings totalling {MEET_H} hours {MEET_M} minutes."),
    (f"{RCB_SUM:,}", f" compliances are reported as simplified, trimmed, digitised or decriminalised (computed sum of four counts; the press release says &lsquo;over 47,000&rsquo;), while one stakeholder told the committee a typical firm faces {STAKE_COMPL:,}; the two are different measures."),
    ("2 asks", " on state reforms: an audit by third-party sampling and industry interviews instead of state-submitted paperwork (para 4.4), and a single PAN-based Business ID across state-level clearances (para 4.5)."),
])

s1 = insight(
    f"{RCB_SUM:,} compliances reformed against {STAKE_COMPL:,} that a stakeholder says a typical firm faces",
    bars("22,287 compliances digitised and 16,108 simplified lead the reform count of 47,123",
         [(k, v) for k, v in RCB.items()], accent="Digitised", vmax=25_000, fmt=lambda v: f"{v:,}",
         sub=f"Compliances reformed by DPIIT with central ministries and states, as summarised by PRS. The total of {RCB_SUM:,} is computed here and assumes the four counts do not overlap; the press release says &lsquo;over 47,000&rsquo;. A stakeholder submission cited in the report says a typical firm faces about {STAKE_ACTS:,} Acts, {STAKE_COMPL:,} compliances and {STAKE_FILINGS:,} filings, which is a different measure, so no share is computed.",
         source="PRS Legislative Research summary of the 201st Report (secondary); PIB press release of 7 August 2026, item 1 (official); sum computed here.")
    + numbers(["Measure", "Figure", "Source"],
              [["Simplified", "16,108", "PRS summary"], ["Redundancy removed", "4,270", "PRS summary"], ["Digitised", "22,287", "PRS summary"], ["Decriminalised", "4,458", "PRS summary"],
               ["Sum of the four", f"{RCB_SUM:,}", "Computed here; the press release says &lsquo;over 47,000&rsquo;"],
               ["Acts a typical firm navigates", f"{STAKE_ACTS:,}", "Stakeholder submission, per PRS; not verified"],
               ["Compliances a typical firm faces", f"{STAKE_COMPL:,}", "Same"], ["Independent filings", f"{STAKE_FILINGS:,}", "Same"]]),
    "The reform count and the stakeholder&rsquo;s count are not on the same footing, so the report&rsquo;s numbers do not show what share of a firm&rsquo;s obligations has been reformed.",
    "DPIIT should publish the compliance count on one base, central and state, so that reformed compliances can be set against the total that a firm faces.",
    anchor="burden")

s2 = insight(
    "The committee asks for third-party checks of state reform claims and one PAN-based ID",
    flow([("Para 4.3", "A new edition of the Business Reform Action Plan (BRAP) with more weight on outcome-based indicators, on-ground implementation and the reduction in time and cost of compliance; best practices of leading states to be documented and shared."),
          ("Para 4.4", "A mandatory Ground Reality Verification audit in the BRAP evaluation, using third-party random sampling and direct industry interviews instead of relying strictly on state-submitted paperwork.", True),
          ("Para 4.5", "A single, PAN-based Business ID adopted as standard across all state-level clearances, ending re-verification of identity across local departments (as the press release words it).", True),
          ("Paras 4.6 and 4.7", "Future BRAP metrics to reward states that close the gap between industrial hubs and rural areas, with capacity-building for lagging regions.")])
    + numbers(["Item", "Press release (official)", "PRS summary (secondary)"],
              [["Audit", "&lsquo;Ground Reality Verification audit&rsquo; in the BRAP evaluation protocol, third-party random sampling and direct industry interviews (para 4.4)", "&lsquo;mandatory third-party ground reality verification audit rather than reliance on state-submitted paperwork&rsquo;"],
               ["Business ID", "&lsquo;single, PAN-based Business ID across all State-level clearances&rsquo;, expanding the BRAP 2024 framework (para 4.5)", "&lsquo;a single PAN-based id across state clearances&rsquo; (the sentence breaks across a page)"],
               ["Scope of the ID", "State-level clearances", "State clearances; neither source says &lsquo;across regulators&rsquo;"]]),
    "Both asks concern how states are scored and how a business is identified to them, and neither is yet a rule, since the committee recommends and the Department decides.",
    "DPIIT should state whether the next BRAP edition will include the audit and the PAN-based ID, with the sampling method and the date from which they apply.",
    anchor="brap")

s3 = insight(
    "Committee seeks deemed approval and public dashboards; Karnataka and Telangana differ",
    bars(f"Karnataka&rsquo;s cap is reached after {KA_DAYS_TO_CAP} days; Telangana&rsquo;s clearance limits run 1 to 30 days",
         [(f"Karnataka: days of delay to reach Rs {KA_CAP} at Rs {KA_RATE} a day (computed)", KA_DAYS_TO_CAP),
          ("Telangana TS-iPASS: longest limit for a clearance", TS_MAX), ("Telangana: provisional approval for mega projects", TS_MID),
          ("Telangana: shortest limit for a clearance", TS_MIN)],
         accent="Telangana TS-iPASS: longest limit for a clearance", unit=" days", vmax=35,
         sub=f"Days. Karnataka&rsquo;s Sakaala Act pays the citizen Rs {KA_RATE} a day from the official, with no deemed approval in the Act text; Telangana&rsquo;s TS-iPASS Act deems notified clearances approved when time runs out. The committee asks for deemed approval through the National Single Window System after the time limit lapses (para 3.30) and a public dashboard with average resolution times down to district level (para 3.32).",
         source="Committee side: PIB press release, items 11 and 13 (official). State side: this blog&rsquo;s Karnataka and Telangana service-delivery posts, from the Karnataka Sakaala Services Act (PRS compilation) and the TS-iPASS Act 2014 (not re-read for this piece).")
    + numbers(["Committee ask", "Karnataka (Sakaala Act)", "Telangana (TS-iPASS)"],
              [["Deemed approval after the time limit (para 3.30)", "None in the Act text; the remedy is compensation of Rs 20 a day up to Rs 500", "Yes for notified industrial clearances (section 13)"],
               ["Public dashboard with average resolution times (para 3.32)", "The Sakala portal home counter shows applications and disposals, undated, per this blog&rsquo;s post; whether it shows resolution times was not checked", f"The TG-iPASS dashboard marks {IP_PCT}% of {IP_RECEIVED:,} applications processed ({IP_RECEIVED - IP_UNPROCESSED:,}); it does not say how many were inside the time limit"],
               ["Single window for all approvals (paras 5.6 and 5.7)", "Not examined", "TG-iPASS covers industrial clearances; no link to the National Single Window System was found"]]),
    f"The dashboard the committee describes would report time taken, whereas the Telangana dashboard reports whether an application is marked processed ({IP_PCT}% of {IP_RECEIVED:,}), so it cannot show whether time limits such as the 1 to 30 days were met.",
    "The Telangana Industries Department should add the processing time for each application to the TG-iPASS dashboard, which is the measure the committee asks the National Single Window System to publish.",
    anchor="states")

s4 = insight(
    "58 committee items: 13 on approvals and timelines, 9 each on compliance and benchmarks",
    bars("13 of 58 items cover approvals and timelines; logistics and e-commerce have 8 each",
         [(g, c) for g, c in GC], accent="Approvals, timelines and single window", vmax=15, fmt=lambda v: f"{v} items",
         sub="Items in the press release&rsquo;s at-a-glance list, grouped by the headings printed there; the grouping into eight themes is this blog&rsquo;s (computed). Every item from 1 to 58 falls in exactly one heading (checked).",
         source="PIB press release, 7 August 2026 (official); grouping computed here.")
    + numbers(["Heading in the press release", "Items", "Item numbers"],
              [[h, str(b - a + 1), (f"{a}" if a == b else f"{a} to {b}")] for h, a, b in RANGES]),
    "Most of the report&rsquo;s weight is on how long approvals take and who verifies reform claims, with sector items such as dark stores and logistics a smaller share.",
    "Readers should check the full report for the evidence behind each item, because the press release lists recommendations and not the data the committee relied on.",
    anchor="themes")

evidence = '''<details class="xv-n"><summary>What the committee examined</summary>
<ul>
<li><b>Meetings:</b> four meetings totalling 8 hours 11 minutes (491 minutes, an average of about 123 minutes each, computed); the draft report was adopted on 5 August 2026 and presented on 7 August 2026 (PIB press release).</li>
<li><b>Witnesses named in the press release:</b> the Department for Promotion of Industry and Internal Trade and the Department of Commerce, Government e-Marketplace, and the ministries of Ports, Shipping and Waterways; Electronics and Information Technology; Micro, Small and Medium Enterprises; Environment, Forest and Climate Change; Road Transport and Highways; Railways (Railway Board); and Civil Aviation, with CII, FICCI, FIEO, banks and financial institutions and other stakeholders.</li>
<li><b>Visit:</b> the press release has a section on a committee visit to Jammu and Kashmir and Ladakh (items 53 to 56); its dates and findings were not read.</li>
<li><b>Data cited:</b> the 47,123 reformed compliances (DPIIT) and a stakeholder&rsquo;s count of 69,233 compliances; PRS says the India assessment under the World Bank&rsquo;s third-cycle B-READY is due around September 2026. No state-level scores, survey or time-and-cost data appear in the press release or the PRS summary.</li>
</ul></details>
'''

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Department for Promotion of Industry and Internal Trade:</b> publish the sampling method, sample size and findings of any Ground Reality Verification audit, state by state, alongside the BRAP score it adjusts.</li>
<li><b>Department for Promotion of Industry and Internal Trade:</b> state which regulators and which state clearances a PAN-based Business ID would cover, since the sources describe state-level clearances only.</li>
<li><b>Rajya Sabha Secretariat:</b> publish the report&rsquo;s evidence chapters and annexures with the press release, so that the 47,123 and 69,233 counts can be traced to their sources.</li>
<li><b>The Karnataka and Telangana governments:</b> publish processing time, not only counts of applications processed, on the Sakala and TG-iPASS portals.</li>
<li><b>National Single Window System team:</b> publish the list of states and central ministries onboarded, with dates, so that the committee&rsquo;s call for mandatory onboarding can be measured.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The PIB press release of 7 August 2026 (Rajya Sabha Secretariat) lists all 58 observations and recommendations with paragraph numbers; it was read in full and is the source for every item quoted here. The PRS summary was read in full. The report itself was not read.</li>
<li>The committee is a Department Related Parliamentary Standing Committee of the Rajya Sabha, so the full report is hosted by the Rajya Sabha rather than on the Lok Sabha committee pages; the press release says it is under sansad.in/rs, Committees, DRPSC-RS, Commerce, Report.</li>
<li>Counts are summed or grouped here as stated beside each chart; the grouping into themes is this blog&rsquo;s.</li>
<li>The Karnataka and Telangana figures are those of this blog&rsquo;s service-delivery posts, which read the Sakaala Services Act (PRS compilation), the TS-iPASS Act 2014 and the two state portals; they were not re-read for this piece.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The full report: its host was blocked for the research environment, so the committee&rsquo;s evidence chapters, state-wise data, annexures and the reasoning behind each item were not read; everything here rests on the press release and the PRS summary.</li>
<li>The scope of the PAN-based ID: the press release and PRS say state-level (state) clearances; the brief for this piece said &lsquo;across regulators&rsquo;, which neither source supports. Whether it would also cover central regulators is not stated.</li>
<li>Whether the audit is a new exercise or a change to the existing BRAP process: the sources do not say how BRAP evidence is collected today beyond &lsquo;State-submitted paperwork&rsquo;.</li>
<li>Whether the four reform counts overlap: the sum of 47,123 is consistent with the press release&rsquo;s &lsquo;over 47,000&rsquo; only if they do not, and the sources do not say.</li>
<li>The stakeholder&rsquo;s figures (1,500 Acts, 69,233 compliances, 6,618 filings): who gave them and how they were counted are not in the summary.</li>
<li>The result of the World Bank&rsquo;s third-cycle B-READY assessment: PRS expected it around September 2026, and a search on 25 November 2026 found no published result for India.</li>
<li>Whether the Government has accepted any recommendation: no action-taken report was found.</li>
<li>Whether Karnataka or Telangana is onboarded to the National Single Window System, or uses a PAN-based business ID: no source was found for either; the comparison is limited to the time limits, remedies and dashboards the two posts document.</li>
<li>Conflicts between sources: PRS lists &lsquo;compensation for delayed government refunds and subsidies&rsquo; (para 3.31) as a time-limit remedy; the Karnataka compensation of Rs 20 a day applies to citizen services, a different thing, so the two are compared only as remedies and not as like for like.</li>
</ul></details>
'''

step(6, "assembling body")
body = STYLE + top + s1 + s2 + s3 + s4 + evidence + fixes + method + gaps

SOURCES = (
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2296240&amp;reg=3&amp;lang=1">PIB (Rajya Sabha Secretariat), press release on the 201st Report of the Standing Committee on Commerce, 7 August 2026</a> (official; 58 items with paragraph references); '
    '<a href="https://prsindia.org/policy/report-summaries/doing-business-in-india-the-way-forward">PRS Legislative Research summary</a> and its '
    '<a href="https://prsindia.org/files/policy/policy_committee_reports/SCR_Summary_Doing_Business_in_India.pdf">PDF</a> (secondary; compliance counts and the stakeholder submission). '
    'State side: <a href="https://prsindia.org/files/bills_acts/acts_states/karnataka/2012/2012KA1.pdf">Karnataka Sakaala Services Act, 2011, PRS compilation</a>; '
    '<a href="https://www.indiacode.nic.in/bitstream/123456789/8562/1/act_3_of_2014.pdf">TS-iPASS Act, 2014, India Code copy</a>; '
    '<a href="https://ipass.telangana.gov.in/UI/TSiPASS/frmSingleWindowDashboard.aspx">Telangana single window dashboard</a> and '
    '<a href="https://sakala.kar.nic.in/index.aspx">Sakala portal</a> (figures as recorded in this blog&rsquo;s two posts). '
    'Sums, groupings and day counts computed by this blog. Analysed 25 November 2026.')
RELATED = [("https://blog.vertistratsolution.com/2026/11/karnataka-sakaala-services-act-rs-20.html", "Karnataka Sakaala Services Act: Rs 20 a day for delay, capped at Rs 500, amended 2026")]

step(7, "writing page")
build("Policy &middot; Governance", TITLE,
      "The Rajya Sabha Standing Committee on Commerce presented its 201st Report on 7 August 2026; this piece sets out its recommendations on approvals, reform audits and a single business ID, and how they bear on the Karnataka and Telangana service-delivery rules.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in html.lower().replace("accordion.js", ""), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
step(8, "complete")
