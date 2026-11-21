"""Telangana governance and service-delivery policy: whether a general guarantee-of-services law exists, the TS-iPASS Act of 2014 and its
dashboard, the Telangana Rising 2047 targets, and Bhu Bharati. Compared with Karnataka's Sakaala Act only where both sides have a source.
Build from the repo root:  python3 out/research/telangana-service-delivery-policy-2026/build.py   (writes out/post-telangana-service-delivery-policy.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 21 November 2026.
Not read from the build environment: TS-iPASS Act sections 12, 19 and 20 and the notified time limits (only the district portal summary and sections
7 and 13 were read), and any Telangana statute search beyond one Legal Data Hunter query and web searches; the post says so."""
import math
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-telangana-service-delivery-policy.html"
STEPS = 8


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


# ---- 1. TG-iPASS online single window dashboard, 1 Jan 2024 to 5 Nov 2026 (last update 05/11/2026 07:47:27): department, received, processed
step(1, "TG-iPASS dashboard rows and consistency checks")
ROWS = [("Pollution Control Board", 1699, 1534), ("Commercial Taxes", 48, 16), ("TGIIC", 5535, 5369), ("Panchayat Raj", 4, 3),
        ("Electrical Inspectorate", 610, 596), ("TGNPDCL", 559, 538), ("TGSPDCL", 1032, 1032), ("Factories", 1866, 1683),
        ("HMDA", 189, 121), ("Town and Country Planning", 471, 430), ("Fire", 20, 18), ("Ground Water", 197, 197),
        ("HMWSSB", 16, 15), ("Irrigation", 18, 14), ("Boilers Department", 489, 481), ("GHMC", 4, 4), ("KUDA", 23, 16),
        ("CESS-Sircilla", 27, 27), ("Collector-Medchal", 1, 0), ("Labour Department", 28, 23), ("Mission Bhagiratha", 28, 28),
        ("CP-RACHAKONDA", 1, 0), ("CP-CYBERABAD", 1, 1), ("Tourism", 4, 0), ("SUDA_KARIMNAGAR", 21, 17), ("NUDA", 20, 18),
        ("SUDA_KHAMMAM", 6, 4), ("SUDA_SIDDIPET", 9, 9)]
assert len(ROWS) == 28
assert all(p <= r for _, r, p in ROWS)
REC = sum(r for _, r, _ in ROWS)
PRO = sum(p for _, _, p in ROWS)
assert (REC, PRO) == (12926, 12194)
PCT = 100 * PRO / REC
assert f"{PCT:.2f}" == "94.34"
assert REC - PRO == 732
BIG = [(n, r, p) for n, r, p in ROWS if r >= 100]
assert len(BIG) == 10 and sum(r for _, r, _ in BIG) == 12647
BIG_SHARE = 100 * 12647 / REC
assert f"{BIG_SHARE:.1f}" == "97.8"
RATE = {n: round(100 * p / r, 2) for n, r, p in BIG}
assert RATE == {"Pollution Control Board": 90.29, "TGIIC": 97.0, "Electrical Inspectorate": 97.7, "TGNPDCL": 96.24, "TGSPDCL": 100.0,
                "Factories": 90.19, "HMDA": 64.02, "Town and Country Planning": 91.3, "Ground Water": 100.0, "Boilers Department": 98.36}, RATE
assert min(RATE, key=RATE.get) == "HMDA"
HMDA_OPEN = 189 - 121
assert HMDA_OPEN == 68
assert ROWS[2] == ("TGIIC", 5535, 5369) and round(100 * 5535 / REC, 1) == 42.8

# ---- 2. TS-iPASS Act, 2014 (Act 3 of 2014; assent 3 Dec 2014) and the Sangareddy district portal summary (updated 1 Oct 2026)
step(2, "statute and portal figures")
LIMIT_MIN, LIMIT_MAX = 1, 30            # district portal: time limits "varying from 1 day to a maximum of 30 days"
SHORTFALL_DAYS = 3                      # competent authorities may seek shortfall information once, within three days of receipt
PROVISIONAL_DAYS = 15                   # Act, T-SWIFT Board: provisional approval within 15 days of a self-certified application (mega projects)
assert LIMIT_MIN < SHORTFALL_DAYS < PROVISIONAL_DAYS < LIMIT_MAX

# ---- 3. Telangana Rising 2047 (vision document, 9-10 Dec 2025) and the Socio-Economic Outlook 2026
step(3, "vision targets and implied growth")
NOW, T2034, T2047, BASE2047 = 0.201, 1.0, 3.0, 1.21       # USD trillion: Invest Telangana 'Now $201 Bn 2026'; vision targets; Outlook baseline
Y0, Y1, Y2 = 2026, 2034, 2047
g1 = (T2034 / NOW) ** (1 / (Y1 - Y0)) - 1
g2 = (T2047 / T2034) ** (1 / (Y2 - Y1)) - 1
gb = (BASE2047 / NOW) ** (1 / (Y2 - Y0)) - 1
assert Y1 - Y0 == 8 and Y2 - Y1 == 13 and Y2 - Y0 == 21
assert f"{100 * g1:.1f}" == "22.2" and f"{100 * g2:.1f}" == "8.8" and f"{100 * gb:.1f}" == "8.9"
MULT = T2047 / BASE2047
assert f"{MULT:.1f}" == "2.5"
assert math.isclose(T2047 / NOW, 14.925373134328357)
assert f"{T2047 / NOW:.1f}" == "14.9"
GSDP_SHARE_NOW, GSDP_SHARE_TARGET = 5, 10          # per cent of India's GDP, vision document
assert GSDP_SHARE_TARGET == 2 * GSDP_SHARE_NOW
GSDP_LAKH_CRORE, GSDP_GROWTH, NATIONAL_GROWTH = 17.82, 10.7, 8.0   # Outlook 2026, provisional advance estimates for 2025-26
assert round(GSDP_GROWTH - NATIONAL_GROWTH, 1) == 2.7

# ---- 4. Bhu Bharati, cumulative 14 Apr 2025 to 28 Feb 2026 (Outlook 2026)
step(4, "Bhu Bharati figures")
HITS_CRORE, PAYMENTS_LAKH, REVENUE_CRORE, SLOTS_LAKH = 4.68, 8.19, 1648.32, 6.72
AVG_PAYMENT = REVENUE_CRORE * 1e7 / (PAYMENTS_LAKH * 1e5)
assert round(AVG_PAYMENT) == 20126
assert round(HITS_CRORE * 100) == 468                  # 4.68 crore hits = 468 lakh
assert SLOTS_LAKH < PAYMENTS_LAKH                      # fewer slots booked than payments made: slots are one of several routes, not a ceiling

# ---- 5. MeeSeva portal home dashboard (ts.meeseva.telangana.gov.in, retrieved 21 Nov 2026; the counters are undated, October 2026 statistics are shown)
step(5, "MeeSeva and BharatNet figures")
MS_TOTAL, MS_CAT_A, MS_CAT_B = 188_360_341, 50_649_869, 137_123_756          # 18,83,60,341; 5,06,49,869; 13,71,23,756
MS_APPROVED, MS_REJECTED, MS_IN_SLA, MS_BEYOND_SLA = 114_011_173, 9_244_063, 210_345, 4_263_162   # beyond-SLA is stated 'from Jan-2025'
assert MS_CAT_A + MS_CAT_B == 187_773_625
assert MS_TOTAL - (MS_CAT_A + MS_CAT_B) == 586_716                              # the page's category counts do not add to its own total
MS_ACCOUNTED = MS_APPROVED + MS_REJECTED + MS_IN_SLA + MS_BEYOND_SLA
assert MS_ACCOUNTED == 127_728_743
MS_UNACC = MS_TOTAL - MS_ACCOUNTED
assert MS_UNACC == 60_631_598 and f"{100 * MS_UNACC / MS_TOTAL:.1f}" == "32.2"
MS_RATIO = MS_BEYOND_SLA / MS_IN_SLA
assert f"{MS_RATIO:.1f}" == "20.3"
MS_REJ = 100 * MS_REJECTED / (MS_APPROVED + MS_REJECTED)
assert f"{MS_REJ:.1f}" == "7.5"
OCT_TX, OCT_CR, OCT_SERV, OCT_CENTRES = 1_810_164, 456.26, 394, 5282
OCT_AVG = OCT_CR * 1e7 / OCT_TX
assert round(OCT_AVG) == 2521
M = 1e6
assert [round(v / M, 2) for v in (MS_TOTAL, MS_APPROVED, MS_REJECTED, MS_BEYOND_SLA, MS_IN_SLA, MS_UNACC)] == [188.36, 114.01, 9.24, 4.26, 0.21, 60.63]
# BharatNet in Telangana, PIB 6 Nov 2026: Rs 3,189 crore for 12,769 gram panchayats (1,946 upgraded + 10,787 phase II + 36 new)
BN_CR, BN_GP = 3189, 12769
assert 1946 + 10787 + 36 == BN_GP
BN_LAKH_PER_GP = BN_CR * 100 / BN_GP
assert f"{BN_LAKH_PER_GP:.2f}" == "24.97"

TITLE = "Telangana service delivery: no general guarantee law found; industry has TG-iPASS"
assert 55 <= len(TITLE) <= 90, len(TITLE)
assert not any(w in TITLE.lower().split() for w in ("you", "your", "we", "our"))

step(6, "writing sections")
top = top_line([
    ("None found", " is the result of a search for a Telangana law guaranteeing citizen services within a time limit, as Karnataka has; a 2022 scoping study marks Telangana as having none, and the one statutory time-limit regime found is the TS-iPASS Act of 2014 for industrial clearances."),
    (f"{PCT:.2f}%", f" of the {REC:,} applications on the TG-iPASS dashboard between 1 January 2024 and 5 November 2026 are marked processed, leaving {REC - PRO} unprocessed; the dashboard does not say how many were within the time limit."),
    ("22.2% a year", f" is the dollar growth needed from USD 0.201 trillion in 2026 to the USD 1 trillion target for 2034, against 8.9% a year in the Outlook&rsquo;s own baseline path to USD 1.21 trillion by 2047."),
])

s1 = insight(
    "Telangana&rsquo;s time-limit statute covers industrial clearances; no general one was found",
    bars("TS-iPASS limits run 1 to 30 days; mega projects get provisional approval in 15",
         [("Shortest time limit for any clearance", LIMIT_MIN),
          ("Shortfall information sought once, within", SHORTFALL_DAYS),
          ("Provisional approval for mega projects, from self-certification", PROVISIONAL_DAYS),
          ("Longest time limit for any clearance", LIMIT_MAX)],
         accent="Longest time limit for any clearance", unit=" days", vmax=32,
         sub="Days, as stated for the Telangana State Industrial Project Approval and Self Certification System Act, 2014 (Act 3 of 2014). A clearance can be deemed approved if the authority misses its stipulated time (section 13).",
         source="Act 3 of 2014 (Telangana Law Department and India Code copies); Sangareddy district portal summary, updated 1 October 2026 (secondary).")
    + numbers(["Question", "Karnataka", "Telangana", "Basis"],
              [["General statute guaranteeing citizen services in a stipulated time", "Yes: Act 1 of 2012, Sakaala Services Act", "None found", "Karnataka: PRS compilation; Telangana: 2022 scoping study (secondary) and searches"],
               ["Compensation for delay", "Rs 20 a day up to Rs 500 an application, from the official&rsquo;s salary", "Act has a penalty section (19); amount not read", "Karnataka: Act text; Telangana: Act index only"],
               ["Appeals", "Two: 30 days, then 60 days", "Not read", "Karnataka: Act text"],
               ["Scope", "890 of 2,456 services under Sakala (Principal Secretary, 11 Sep 2026); the portal shows 1,446 services and 114 departments, undated; the two figures are not reconciled", "Industrial clearances; 28 departments on the dashboard", "Both from official portals and The Hindu"],
               ["Other citizen services", "Statutory time limits under the Act", "MeeSeva service levels (SLA); statutory basis not found", "Karnataka: Act; Telangana: MeeSeva portal"],
               ["Deemed approval on a missed deadline", "None in the Act text", "Yes for notified clearances (section 13)", "Telangana: Act text"]],
              "Show the Karnataka and Telangana comparison"),
    "Telangana&rsquo;s guarantee is for investors with notified clearances, with deemed approval as the remedy, while Karnataka&rsquo;s covers 1,446 notified services with compensation and two appeals.",
    "Telangana&rsquo;s General Administration Department should state publicly whether a general guarantee-of-services law exists or is planned and list which citizen services carry a statutory time limit.",
    "law")

s2 = insight(
    f"TG-iPASS shows {PCT:.2f}% of {REC:,} applications processed, with HMDA at {RATE['HMDA']:.0f}%",
    bars("Nine of ten large departments processed over 90% of applications; HMDA processed 64%",
         [(n, RATE[n], f"{r:,} received") for n, r, p in sorted(BIG, key=lambda x: x[2] / x[1])],
         accent="HMDA", unit="%", vmax=100,
         sub="Share of applications marked processed, per cent, for the ten departments with at least 100 applications received between 1 January 2024 and 5 November 2026. The dashboard does not define &lsquo;processed&rsquo; or show whether it was inside the time limit.",
         source="Telangana online single window dashboard, ipass.telangana.gov.in, last update 5 November 2026; shares computed here.")
    + numbers(["Department", "Received", "Processed", "Share processed (%)"],
              [[n, f"{r:,}", f"{p:,}", f"{100 * p / r:.2f}"] for n, r, p in ROWS] + [["All 28 rows", f"{REC:,}", f"{PRO:,}", f"{PCT:.2f}"]],
              "Show all 28 departments"),
    f"The ten large departments hold {BIG_SHARE:.1f}% of all applications, and HMDA&rsquo;s {HMDA_OPEN} unprocessed applications of 189 are the largest gap by share.",
    "The dashboard should report, for each department, applications decided inside the statutory time limit and deemed approvals, with a definition of &lsquo;processed&rsquo;.",
    "dashboard")

s2b = insight(
    "MeeSeva shows 4.26 million requests pending beyond the service level since January 2025",
    bars("MeeSeva: 4.26 million pending beyond SLA since January 2025, 20 times those within SLA",
         [("Approved", round(MS_APPROVED / M, 2)), ("Rejected", round(MS_REJECTED / M, 2)),
          ("Pending beyond SLA (from January 2025)", round(MS_BEYOND_SLA / M, 2)), ("Pending within SLA", round(MS_IN_SLA / M, 2)),
          ("Not in these four statuses (computed)", round(MS_UNACC / M, 2))],
         accent="Pending beyond SLA (from January 2025)", unit=" million", vmax=120,
         sub=f"Requests, millions, from the MeeSeva portal home dashboard retrieved on 21 November 2026; the counters carry no date. Total requests {MS_TOTAL / M:.2f} million. The beyond-SLA count is stated to run from January 2025, the other counts state no start date.",
         source="MeeSeva portal, ts.meeseva.telangana.gov.in (Electronic Service Delivery Department); shares and differences computed here.")
    + numbers(["Item", "Value", "Note"],
              [["Total requests", f"{MS_TOTAL:,}", "Portal"],
               ["Category A and B requests", f"{MS_CAT_A:,} and {MS_CAT_B:,}", f"Sum {MS_CAT_A + MS_CAT_B:,}, {MS_TOTAL - MS_CAT_A - MS_CAT_B:,} below the total"],
               ["Approved", f"{MS_APPROVED:,}", "Portal"],
               ["Rejected", f"{MS_REJECTED:,}", f"{MS_REJ:.1f}% of approved plus rejected (computed)"],
               ["Pending within SLA", f"{MS_IN_SLA:,}", "Portal"],
               ["Pending beyond SLA, from January 2025", f"{MS_BEYOND_SLA:,}", f"{MS_RATIO:.1f} times pending within SLA (computed)"],
               ["Not in the four statuses", f"{MS_UNACC:,}", f"{100 * MS_UNACC / MS_TOTAL:.1f}% of total requests (computed)"],
               ["October 2026", f"{OCT_TX:,} transactions, Rs {OCT_CR} crore", f"About Rs {OCT_AVG:,.0f} a transaction (computed); {OCT_SERV} active services and {OCT_CENTRES:,} active centres"]],
              "Show the MeeSeva figures"),
    f"The dashboard shows {MS_RATIO:.1f} times as many requests pending beyond the service level as within it, but the two counters do not share a stated start date, and {100 * MS_UNACC / MS_TOTAL:.1f}% of requests are in none of the four listed statuses.",
    "The Electronic Service Delivery Department should publish, for each MeeSeva service, the service level in days, the share decided inside it, and the date each counter starts from.",
    "meeseva")

s3 = insight(
    f"Telangana Rising 2047 needs {100 * g1:.0f}% a year in dollars to 2034; the baseline is {100 * gb:.1f}%",
    bars("The 2047 target of USD 3 trillion is about 2.5 times the USD 1.21 trillion baseline",
         [("Telangana economy, 2026 (Invest Telangana)", NOW), ("Target for 2034", T2034),
          ("Baseline projection for 2047 (Outlook 2026)", BASE2047), ("Target for 2047", T2047)],
         accent="Target for 2047", unit=" trillion USD", fmt=lambda v: f"USD {v:g} trillion", vmax=3.2,
         sub=f"USD trillion. The 2034 date for the USD 1 trillion milestone is stated in the vision document, the state press release and the Outlook. Implied growth, computed here in dollar terms: {100 * g1:.1f}% a year for 2026 to 2034, {100 * g2:.1f}% for 2034 to 2047, {100 * gb:.1f}% for the baseline.",
         source="Telangana Rising 2047 vision document (9&ndash;10 December 2025); Socio-Economic Outlook 2026, Planning Department; Invest Telangana. Growth rates computed here.")
    + numbers(["Item", "Value", "Source and status"],
              [["Economy, 2026", "USD 0.201 trillion (USD 201 billion)", "Invest Telangana; the vision document says about USD 200 billion"],
               ["Milestone", "USD 1 trillion by 2034", "Vision document; Outlook 2026; press release of 9 December 2025"],
               ["Target", "USD 3 trillion by 2047", "Vision document; Outlook 2026"],
               ["Baseline, current momentum", "About USD 1.21 trillion by 2047", "Outlook 2026"],
               ["Share of India&rsquo;s GDP", f"{GSDP_SHARE_NOW}% now, {GSDP_SHARE_TARGET}% targeted", "Vision document and Outlook 2026"],
               ["Required real growth", "Average 8% (2025&ndash;30), 7% (2031&ndash;39), 5.2% (2041&ndash;47)", "Outlook 2026; the excerpt read gives no figure for 2040"],
               ["2025-26 GSDP, provisional", f"Rs {GSDP_LAKH_CRORE} lakh crore, up {GSDP_GROWTH}% against {NATIONAL_GROWTH}% nationally", "Outlook 2026, provisional advance estimates"]]),
    f"Reaching USD 3 trillion means ending 2047 with an economy {MULT:.1f} times the baseline level, and the required dollar growth is concentrated in 2026 to 2034.",
    "The Planning Department should state whether the dollar figures are nominal and the exchange rate used, so the 22% a year can be set against the real growth rates in the Outlook.",
    "vision")

s4 = (f'<section class="xv-sec"><h2 class="gb-h2" id="other">Other Telangana measures with a dated source</h2>\n'
      + flow([("3 Dec 2014", "Governor&rsquo;s assent to the TS-iPASS Act (Act 3 of 2014): single-point clearances, self-certification, deemed approval, and a right to clearances within time limits."),
              ("1 Jan 2024 to 5 Nov 2026", f"TG-iPASS dashboard: {REC:,} applications received, {PRO:,} processed."),
              ("14 Apr 2025 to 28 Feb 2026", f"Bhu Bharati land portal: {HITS_CRORE} crore hits, {PAYMENTS_LAKH} lakh payments worth Rs {REVENUE_CRORE:,} crore (about Rs {AVG_PAYMENT:,.0f} a payment, computed) and {SLOTS_LAKH} lakh slots booked."),
              ("8 and 9 Dec 2025", "Telangana Rising Global Summit at Bharat Future City; the Telangana Rising 2047 vision document was unveiled on 9 December.", True),
              ("6 Nov 2026 (PIB)", f"Agreement for the Amended BharatNet Program in Telangana: Rs {BN_CR:,} crore of central support for {BN_GP:,} gram panchayats, about Rs {BN_LAKH_PER_GP:.2f} lakh each (computed), and around three lakh rural home fibre connections expected."),
              ("12 Nov 2026 (as reported)", "MeeSeva doorstep delivery of government services began in Cyberabad, run by the Electronic Service Delivery Department with Cyberabad Police, the Cyberabad municipal corporation and the Society for Cyberabad Security Council."),
              ("2026 Outlook (undated)", "Prajavani, a programme to receive grievances in person at Mahatma Jyothiba Phule Praja Bhavan, is described without counts.")])
      + numbers(["Measure", "Dated fact", "Source"],
                [["BharatNet, Telangana", f"Rs {BN_CR:,} crore; {BN_GP:,} gram panchayats (1,946 upgraded, 10,787 phase II, 36 new)", "PIB, 6 November 2026"],
                 ["Bhu Bharati hits", f"{HITS_CRORE} crore", "Outlook 2026 (cumulative to 28 Feb 2026)"],
                 ["Bhu Bharati payments", f"{PAYMENTS_LAKH} lakh, Rs {REVENUE_CRORE:,} crore", "Outlook 2026"],
                 ["Bhu Bharati slots booked", f"{SLOTS_LAKH} lakh", "Outlook 2026"],
                 ["MeeSeva doorstep delivery", "Cyberabad, reported 12 November 2026", "The Hindu (secondary)"],
                 ["Prajavani", "Launched for in-person grievances; no counts found", "Outlook 2026"]],
                "Show the dated facts")
      + '</section>\n')

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Telangana Industries and Commerce Department:</b> add to the TG-iPASS dashboard the count decided inside the statutory time limit, the count deemed approved, and a definition of &lsquo;processed&rsquo;.</li>
<li><b>Telangana General Administration Department:</b> state whether a general guarantee-of-services law exists or is planned, and list the citizen services that carry a statutory time limit.</li>
<li><b>Telangana Planning Department:</b> state in the vision document and the Outlook whether the USD figures are nominal and which exchange rate is used.</li>
<li><b>Telangana Revenue Department:</b> publish time-to-decision for each Bhu Bharati service alongside the payment and slot counts.</li>
<li><b>Telangana Electronic Service Delivery Department:</b> publish the service level for each MeeSeva service, the share decided inside it, and the start date of each dashboard counter.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The dashboard rows were added by this blog: 28 departments, 12,926 received and 12,194 processed, and no department has more processed than received.</li>
<li>Implied growth is (end / start) raised to 1 over the years, in dollars, using USD 0.201 trillion for 2026. It is not the real GDP growth the Outlook lists, and the two should not be compared without a deflator and exchange rate.</li>
<li>The Act is titled TS-iPASS; the dashboard and district pages use TG-iPASS after the state&rsquo;s abbreviation change. They are the same system.</li>
<li>Karnataka figures in the comparison are from this blog&rsquo;s companion article on the Sakaala Services Act and carry the same caveats, including that the Sakala counters are undated.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>That no general guarantee-of-services law exists in Telangana. A Legal Data Hunter query returned only central Gazette notices, and a 2022 scoping study of right-to-public-service laws lists Telangana as &lsquo;N&rsquo; in its annexure while also naming Telangana among the states it analyses. Neither is proof; a search of Telangana Gazette and Law Department listings was not done.</li>
<li>The text of TS-iPASS sections 12, 19 and 20 (time limits, penalty, right to clearances) and the notified time limits: only the Act index, sections 7 and 13, and a district portal summary were read. The penalty amount is unknown.</li>
<li>Whether TG-iPASS applications were processed within time: the dashboard shows received and processed only, with no definition of &lsquo;processed&rsquo; and no approvals, rejections or delays.</li>
<li>The date of the USD 1 trillion milestone in one report that gives 2037: every Telangana source read (the vision document, the state press release of 9 December 2025, the Socio-Economic Outlook 2026 and Invest Telangana) says 2034, and the report giving 2037 was not found, so 2034 is used.</li>
<li>Whether the vision&rsquo;s dollar figures are nominal or real, and the exchange rate behind USD 201 billion; the Outlook&rsquo;s file date is 17 March 2026 in search metadata while its address shows August 2026.</li>
<li>The MeeSeva dashboard&rsquo;s dates and definitions: the counters are undated, its category counts do not add to its own total (a gap of 586,716), 32.2% of requests fall in none of the four listed statuses, and the same page shows 27 active services, 38 departments and 9 centres in one block but 394 active services and 5,282 active centres in its October 2026 statistics. Only the October 2026 statistics and the status counts are used, with these caveats. Whether MeeSeva service levels have a statutory basis was not found.</li>
<li>Prajavani and Praja Palana outcomes: the Outlook describes them without counts. No other Telangana policy is included because no dated figure was found for it.</li>
<li>Any Telangana evaluation: the sources read are the state&rsquo;s own documents, which state targets and counts, not independent outcomes.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s2b + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://ipass.telangana.gov.in/UI/TSiPASS/frmSingleWindowDashboard.aspx">Telangana online single window dashboard</a> (official; 1 January 2024 to 5 November 2026); '
    '<a href="https://law.telangana.gov.in/fileShow?fileName=%2FUploads%2FLawDepartment%2Fpdf%2FAct%203%20of%202014_16012023_151050.pdf">TS-iPASS Act, 2014 (Act 3 of 2014), Telangana Law Department</a> and '
    '<a href="https://www.indiacode.nic.in/bitstream/123456789/8562/1/act_3_of_2014.pdf">India Code copy</a> (primary; only part of the text was read); '
    '<a href="https://sangareddy.telangana.gov.in/industrial-approvals-and-clearances-tg-ipass">Sangareddy district portal, TG-iPASS summary</a> (official, secondary summary; updated 1 October 2026); '
    '<a href="https://tgswc.telangana.gov.in/wp-content/uploads/2025/12/TelanganaRising-2047.pdf">Telangana Rising 2047 vision document</a> (official; December 2025); '
    '<a href="https://www.telangana.gov.in/news/press-releases/2025/12/honble-cm-sri-a-revanth-reddy-launches-the-vision-document-telangana-rising-2047-at-the-telangana-rising-global-summit-2025-bharat-future-city">Telangana press release, 9 December 2025</a>; '
    '<a href="https://www.telangana.gov.in/wp-content/uploads/2026/08/Socio-Economic-Outlook-2026.pdf">Socio-Economic Outlook 2026, Planning Department</a> (official); '
    '<a href="https://invest.telangana.gov.in/">Invest Telangana</a> (official); '
    '<a href="https://www.thehindu.com/news/national/telangana/telangana-rising-vision-2047-document-unveiled-charts-roadmap-to-achieve-3-trillion-economy/article70377583.ece">The Hindu, 10 December 2025</a> (secondary); '
    '<a href="https://ts.meeseva.telangana.gov.in/meeseva/home.htm">MeeSeva portal home dashboard</a> (official; counters undated); '
    '<a href="https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2333683&amp;reg=48&amp;lang=2">PIB, 6 November 2026, Amended BharatNet Program in Telangana</a> (government release); '
    '<a href="https://www.thehindu.com/news/national/telangana/now-meeseva-doorstep-delivery-of-govt-services-in-cyberabad/article71693914.ece">The Hindu, 12 November 2026</a> (secondary: MeeSeva doorstep delivery); '
    '<a href="https://www.thehindu.com/news/national/karnataka/karnataka-govts-praja-seve-to-be-expanded-with-launch-of-namma-seve-app/article71456733.ece">The Hindu, 11 September 2026</a> (secondary: Karnataka 890 of 2,456 services under Sakala); '
    '<a href="https://safar-india.org/documents/RTPSD_Final.pdf">SAFAR, scoping study of right to public service delivery Acts</a> (secondary, 2022; annexure on state status); '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/karnataka/2012/2012KA1.pdf">PRS Legislative Research, Karnataka Sakaala Services Act</a> and '
    '<a href="https://sakala.kar.nic.in/index.aspx">Sakala portal</a> (for the Karnataka comparison). '
    'Shares, growth rates and averages computed by this blog. Analysed 21 November 2026.')

RELATED = []

step(7, "assembling page")
build("Governance &middot; Telangana", TITLE,
      "Telangana has a statutory time-limit regime for industrial clearances, a single-window dashboard, the MeeSeva service portal, a land portal and a 2047 vision document; no general guarantee-of-services law was found.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
step(8, "complete")
