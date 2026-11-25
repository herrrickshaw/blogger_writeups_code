"""Forest Rights Act, 2006: claims funnel, state split, area per title. Official PIB state tables as on 31 May 2025 (PIB 24 and 31 Jul 2025), PIB 13 Dec 2023
(area at 31 Oct 2023), and secondary reports of figures as on 31 August 2026 (a PIB backgrounder of 16 Nov 2026 that was NOT found or read).
Build from the repo root:  python3 out/research/forest-rights-act-2026-11/build.py            (writes out/post-forest-rights-act-2026-11.html)
                           python3 out/research/forest-rights-act-2026-11/build.py --check    (arithmetic and asserts only)
Analysed 25 November 2026."""
import html as _h
import pathlib
import sys
import time

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
OUT = ROOT / "out/post-forest-rights-act-2026-11.html"
STEPS = 8


def step(n, what):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {el / n * (STEPS - n):.1f}s left)", flush=True)


# ---- 1. official state table, as on 31 May 2025 (PIB release 2150804, 31 Jul 2025): claims ind/comm/total, titles ind/comm/total, rejected, disposed, pending
step(1, "load official state table (PIB, 31 May 2025)")
NA = None
ST = {  # state: (claims_ind, claims_comm, claims_tot, tit_ind, tit_comm, tit_tot, rejected, disposed, pending)
    "Andhra Pradesh": (285098, 3294, 288392, 226651, 1822, 228473, 58410, 286883, 1509),
    "Assam": (148965, 6046, 155011, 57325, 1477, 58802, NA, 58802, 96209),
    "Bihar": (4696, 0, 4696, 191, 0, 191, 4496, 4687, 9),
    "Chhattisgarh": (890220, 57259, 947479, 481432, 52636, 534068, 406787, 940855, 6624),
    "Goa": (9757, 379, 10136, 856, 15, 871, 447, 1318, 8818),
    "Gujarat": (183055, 7187, 190242, 98732, 4792, 103524, 2331, 105855, 84387),
    "Himachal Pradesh": (4883, 683, 5566, 662, 146, 808, 54, 862, 4704),
    "Jharkhand": (107032, 3724, 110756, 59866, 2104, 61970, 28107, 90077, 20679),
    "Karnataka": (288549, 5940, 294489, 14981, 1345, 16326, 253269, 269595, 24894),
    "Kerala": (44455, 1014, 45469, 29422, 282, 29704, 12835, 42539, 2930),
    "Madhya Pradesh": (585326, 42187, 627513, 266901, 27976, 294877, 322407, 617284, 10229),
    "Maharashtra": (397897, 11259, 409156, 199667, 8668, 208335, 172631, 380966, 28190),
    "Odisha": (701148, 35024, 736172, 462067, 8832, 470899, 144636, 615535, 120637),
    "Rajasthan": (113162, 5213, 118375, 49215, 2551, 51766, 65921, 117687, 688),
    "Tamil Nadu": (33119, 1548, 34667, 15442, 1066, 16508, 12711, 29219, 5448),
    "Telangana": (651822, 3427, 655249, 230735, 721, 231456, 94426, 325882, 329367),
    "Tripura": (200557, 164, 200721, 127931, 101, 128032, 68848, 196880, 3841),
    "Uttar Pradesh": (92972, 1194, 94166, 22537, 893, 23430, 70736, 94166, 0),
    "Uttarakhand": (3587, 3091, 6678, 184, 1, 185, 6493, 6678, 0),
    "West Bengal": (131962, 10119, 142081, 44444, 686, 45130, 96587, 141717, 364),
    "Jammu and Kashmir": (33233, 12857, 46090, 429, 5591, 6020, 39924, 45944, 146),
}
TOT = (4911495, 211609, 5123104, 2389670, 121705, 2511375, 1862056, 4373431, 749673)       # the TOTAL row as printed
assert len(ST) == 21                                                                      # 20 States and 1 Union Territory
for i in range(9):
    s = sum((v[i] or 0) for v in ST.values())
    assert s == TOT[i], (i, s, TOT[i])                                                    # every column sums to the printed total (Assam rejected 'NA/NR' counted as 0)
for k, v in ST.items():
    assert v[0] + v[1] == v[2] and v[3] + v[4] == v[5], k                                 # individual + community = total
    assert v[5] + (v[6] or 0) == v[7], k                                                  # titles + rejected = disposed (Assam: rejected not reported)
    assert v[7] + v[8] == v[2], k                                                         # disposed + pending = received
CL, TI, RJ, DI, PE = TOT[2], TOT[5], TOT[6], TOT[7], TOT[8]
assert f"{100 * TI / CL:.2f}" == "49.02" and f"{100 * RJ / CL:.2f}" == "36.35" and f"{100 * PE / CL:.2f}" == "14.63" and f"{100 * DI / CL:.2f}" == "85.37"      # printed shares reproduced
# the total of 5,123,104 is individual 4,911,495 plus community 211,609 as PIB states
assert f"{100 * TOT[4] / TI:.1f}" == "4.8"                                               # community titles are 4.8% of titles

# ---- 2. area (PIB 24 Jul 2025 annexure, as on 31 May 2025; PIB 13 Dec 2023, as on 31 Oct 2023)
step(2, "area tables and checks")
AC = {"Andhra Pradesh": (454706, 526454, 981160.00), "Bihar": (53.03, 0, 53), "Chhattisgarh": (949770.89, 9102957.49, 10052728.38),
      "Goa": (1506.45, 18.66, 1525.11), "Gujarat": (168448.83, 1240680.15, 1409128.99), "Himachal Pradesh": (126.65, 62677.24, 62803.89),
      "Jharkhand": (153395.86, 103758.97, 257154.83), "Karnataka": (20077.30, 36340.52, 56417.82), "Kerala": (38810.58, 788651.25, 827461.83),
      "Madhya Pradesh": (903533.06, 1463614.46, 2367147.52), "Maharashtra": (461491.25, 3371497.43, 3832988.68), "Odisha": (674775.33, 743193.39, 1417968.72),
      "Rajasthan": (70387.18, 239763.95, 310151.13), "Tamil Nadu": (22104.80, 60468.77, 82573.57), "Telangana": (669689.14, 457663.17, 1127352.32),
      "Tripura": (465192.88, 552.40, 465745.28), "Uttarakhand": (0, 0, 0), "West Bengal": (21014.27, 572.03, 21586.29)}
NA_AREA = ("Assam", "Uttar Pradesh", "Jammu and Kashmir")                                 # area printed as NA/NR
AC_TOT = (5075083.51, 18198863.89, 23273947.39)
for i in range(3):
    assert abs(sum(v[i] for v in AC.values()) - AC_TOT[i]) < 1.0, i                      # state areas sum to the printed total, to 1 acre
for k, v in AC.items():
    assert abs(v[0] + v[1] - v[2]) < 1.0, k
assert set(AC) | set(NA_AREA) == set(ST) and len(AC) == 18
T_ARE_IND = sum(ST[k][3] for k in AC)
T_ARE_COM = sum(ST[k][4] for k in AC)
assert T_ARE_IND == TOT[3] - sum(ST[k][3] for k in NA_AREA) == 2309379 and T_ARE_COM == TOT[4] - sum(ST[k][4] for k in NA_AREA) == 113744
IND_AC, COM_AC = AC_TOT[0] / T_ARE_IND, AC_TOT[1] / T_ARE_COM
assert f"{IND_AC:.1f}" == "2.2" and f"{COM_AC:.0f}" == "160"                             # acres per individual title and per community title (States that report area)
T_REP = T_ARE_IND + T_ARE_COM
assert f"{AC_TOT[2] / T_REP:.2f}" == "9.60" and f"{AC_TOT[2] / TI:.2f}" == "9.27"        # per title over reporting States vs over all titles
assert f"{100 * AC_TOT[1] / AC_TOT[2]:.1f}" == "78.2"                                    # community rights are 78.2% of the area on 4.8% of the titles
assert abs(AC_TOT[2] - 23273947.39) < 0.01
# 31 Oct 2023 (PIB 1985799): claims 45,70,932; titles 23,43,009 (22,29,013 individual + 1,13,996 community); acres 47,96,364.16 + 1,32,74,213.27 = 1,80,70,577.43
T23_TI, T23_IND, T23_COM = 2343009, 2229013, 113996
A23_IND, A23_COM, A23_TOT = 4796364.16, 13274213.27, 18070577.43
assert T23_IND + T23_COM == T23_TI and abs(A23_IND + A23_COM - A23_TOT) < 0.01
D_T = TI - T23_TI
D_A = AC_TOT[2] - A23_TOT
D_AC = AC_TOT[1] - A23_COM
D_TC = TOT[4] - T23_COM
assert D_T == 168366 and f"{D_A:.0f}" == "5203370" and f"{D_A / D_T:.1f}" == "30.9"
assert f"{D_AC:.0f}" == "4924651" and D_TC == 7709 and f"{D_AC / D_TC:.0f}" == "639"     # community area added per community title added
assert f"{A23_TOT / T23_TI:.2f}" == "7.71" and f"{AC_TOT[2] / TI:.2f}" == "9.27"
assert f"{100 * D_AC / D_A:.1f}" == "94.6"

# ---- 3. reported figures as on 31 Aug 2026 (secondary: Legacy IAS and other summaries of a PIB backgrounder, 16 Nov 2026; not read)
step(3, "reported 31 August 2026 figures and consistency with 2025")
T26, T26_IND, T26_COM = 25.42e5, 24.18e5, 1.24e5                                          # lakh, as printed
assert abs(T26_IND + T26_COM - T26) < 1                                                   # the printed split sums to the printed total
DISP26, PCT26 = 43.56e5, 0.8064
CL26_LO, CL26_HI = (DISP26 - 500) / (PCT26 + 0.00005), (DISP26 + 500) / (PCT26 - 0.00005)
assert CL26_LO < 54.0e5 < CL26_HI or abs(54.0e5 - DISP26 / PCT26) < 2000                 # '54.0 lakh claims' agrees with 43.56 lakh / 80.64%
CL26 = DISP26 / PCT26
assert f"{CL26 / 1e5:.2f}" == "54.02"
RJ26 = DISP26 - T26                                                                        # disposed less titled, 18.14 lakh (computed)
assert f"{RJ26 / 1e5:.2f}" == "18.14"                                                      # agrees with the October 2026 report of 'over 18 lakh' rejected
PE26 = CL26 - DISP26
assert f"{PE26 / 1e5:.2f}" == "10.46"                                                      # about 10.5 lakh pending (October reports say about 11 lakh)
SH26 = (100 * T26 / CL26, 100 * RJ26 / CL26, 100 * PE26 / CL26)
assert [f"{x:.1f}" for x in SH26] == ["47.1", "33.6", "19.4"] and abs(sum(SH26) - 100) < 1e-6
SH25 = (100 * TI / CL, 100 * RJ / CL, 100 * PE / CL)
# change since 31 May 2025
assert DISP26 < DI and DI - DISP26 == 4373431 - 4356000                                    # disposed count is 17,431 lower in 2026 than in 2025 although claims rose
assert f"{(CL26 - CL) / 1e5:.2f}" == "2.79"
D_T26_LO, D_T26_HI = 2541500 - TI, 2542499 - TI                                            # 25.42 lakh is rounded, so the rise is a range
assert (D_T26_LO, D_T26_HI) == (30125, 31124)
assert f"{100 * 30625 / TI:.1f}" == "1.2"                                                  # about 30,600 more titles: 1.2% in 15 months
AC26 = 238e5
assert f"{(AC26 - AC_TOT[2]) / 1e5:.2f}" == "5.26"                                          # 'nearly 238 lakh acres' less 232.74 lakh
assert f"{AC26 / T26:.2f}" == "9.36"
assert (DISP26 + PE26) - CL26 < 1e-6

# ---- 4. pending concentration and state shares
step(4, "state shares")
TOP4 = ["Telangana", "Odisha", "Assam", "Gujarat"]
P4 = sum(ST[k][8] for k in TOP4)
assert P4 == 630600 and f"{100 * P4 / PE:.1f}" == "84.1"
assert f"{100 * ST['Telangana'][8] / ST['Telangana'][2]:.1f}" == "50.3" and f"{100 * ST['Telangana'][8] / PE:.1f}" == "43.9"
BIG = [k for k, v in ST.items() if v[2] >= 100000]
assert len(BIG) == 13
SHARE = {k: 100 * ST[k][5] / ST[k][2] for k in ST}
lo, hi = min(BIG, key=SHARE.get), max(BIG, key=SHARE.get)
assert (lo, hi) == ("Karnataka", "Andhra Pradesh") and f"{SHARE[lo]:.1f}" == "5.5" and f"{SHARE[hi]:.1f}" == "79.2"
assert f"{SHARE[hi] / SHARE[lo]:.0f}" == "14"
assert f"{100 * ST['Karnataka'][6] / ST['Karnataka'][2]:.1f}" == "86.0"
assert f"{100 * ST['Chhattisgarh'][5] / ST['Chhattisgarh'][2]:.1f}" == "56.4"
CH_AC = AC["Chhattisgarh"][2] / AC_TOT[2]
assert f"{100 * CH_AC:.1f}" == "43.2"                                                     # Chhattisgarh holds 43.2% of the recognised area
assert f"{100 * AC['Chhattisgarh'][1] / AC_TOT[1]:.1f}" == "50.0"
assert f"{100 * ST['Chhattisgarh'][5] / TI:.1f}" == "21.3"                                # and 21.3% of the titles

TITLE = "Forest Rights Act: 25.42 lakh titles on about 238 lakh acres, 47% of claims received"
plain = _h.unescape(TITLE)
assert 55 <= len(plain) <= 90, len(plain)
assert not any(w in plain.lower().split() for w in ("you", "your", "we", "our"))
print(f"consistency checks passed (table sums, funnel identities, area sums, 2026 vs 2025); title {len(plain)} characters", flush=True)
if "--check" in sys.argv:
    sys.exit(0)

from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

step(5, "writing sections")
lk = lambda v: f"{v:.2f} lakh"
top = top_line([
    (f"{SH26[0]:.1f}%", f" of about 54.0 lakh claims had become titles by 31 August 2026 (25.42 lakh titles); on the official 31 May 2025 table the share was {SH25[0]:.2f}%. The 2026 figures are from secondary summaries of a PIB backgrounder that this piece could not locate."),
    (f"{PE / 1e5:.2f} lakh", f" claims were pending on 31 May 2025, and four states hold {100 * P4 / PE:.1f}% of them: Telangana ({ST['Telangana'][8] / 1e5:.2f} lakh), Odisha, Assam and Gujarat."),
    (f"{COM_AC:.0f} acres", f" is the average area of a community title and {IND_AC:.1f} acres of an individual title in the 18 states that report area; community titles are {100 * TOT[4] / TI:.1f}% of titles and {100 * AC_TOT[1] / AC_TOT[2]:.1f}% of the area."),
])

tvo = ('<table class="gb-table"><thead><tr><th>Kind</th><th>What this piece includes</th></tr></thead><tbody>'
       '<tr><td><b>Official counts</b></td><td>The Ministry of Tribal Affairs table of 31 May 2025 (state-wise claims, titles, rejections, pending, and area), and the area at 31 October 2023, all from PIB releases that were read in full.</td></tr>'
       '<tr><td><b>Reported counts</b></td><td>Figures as on 31 August 2026 (25.42 lakh titles, about 238 lakh acres, about 54.0 lakh claims, 43.56 lakh disposed) from summaries of a PIB backgrounder of 16 November 2026; the backgrounder itself was not found.</td></tr>'
       '<tr><td><b>Computed here</b></td><td>Shares, averages and the 2026 rejected and pending counts, each derived from the figures above and checked in the build script.</td></tr>'
       '<tr><td><b>Not found</b></td><td>The August 2026 state table, the monthly progress report for 2026, and an area figure per title for 2026.</td></tr>'
       '</tbody></table>\n')

# section 1: funnel and shares
s1 = insight(
    "Claims disposed: 80.64% in August 2026 against 85.37% in May 2025",
    bars("Pending share of claims rose from 14.6% to 19.4%; titled share fell from 49.0% to 47.1%",
         [("Titled, 31 May 2025 (official)", SH25[0]), ("Titled, 31 Aug 2026 (reported)", SH26[0]),
          ("Rejected, 31 May 2025 (official)", SH25[1]), ("Rejected, 31 Aug 2026 (computed)", SH26[1]),
          ("Pending, 31 May 2025 (official)", SH25[2]), ("Pending, 31 Aug 2026 (computed)", SH26[2])],
         accent="Pending, 31 Aug 2026 (computed)", unit="%", vmax=60,
         sub=(f"Share of claims received, per cent. 2025: {CL:,} claims, {TI:,} titles, {RJ:,} rejected, {PE:,} pending. 2026: about {CL26 / 1e5:.2f} lakh claims (43.56 lakh disposed &divide; 80.64%), 25.42 lakh titles; rejected (18.14 lakh) and pending (10.46 lakh) are computed here as disposed less titles and claims less disposed, from rounded figures."),
         source="PIB release 2150804, 31 July 2025 (official, read in full); Legacy IAS, 17 November 2026, and other summaries of a PIB backgrounder of 16 November 2026 (secondary; the backgrounder was not read).")
    + numbers(["Item", "31 May 2025 (official)", "31 Aug 2026 (reported or computed)"],
              [["Claims received", f"{CL:,} ({TOT[0]:,} individual, {TOT[1]:,} community)", f"about {CL26 / 1e5:.2f} lakh (reported as about 54.0 lakh; {CL26 / 1e5:.2f} computed from 43.56 lakh at 80.64%)"],
               ["Disposed", f"{DI:,} ({100 * DI / CL:.2f}%)", f"43.56 lakh (80.64%), {(DI - DISP26):,.0f} fewer than in 2025 although claims rose by about {(CL26 - CL) / 1e5:.2f} lakh"],
               ["Titles distributed", f"{TI:,} ({TOT[3]:,} individual, {TOT[4]:,} community)", "25.42 lakh (24.18 lakh individual, 1.24 lakh community, sum checked)"],
               ["Rejected", f"{RJ:,} ({100 * RJ / CL:.2f}%)", "18.14 lakh computed (disposed less titles); reports of October 2026 say over 18 lakh"],
               ["Pending", f"{PE:,} ({100 * PE / CL:.2f}%)", "10.46 lakh computed; reports of October 2026 say about 11 lakh"],
               ["Change in titles", "&ndash;", f"{D_T26_LO:,} to {D_T26_HI:,} more than in May 2025 (rounded figure), about 1.2% in 15 months"]],
              "Show the funnel figures and checks"),
    "The official count of disposed claims is higher in May 2025 than the reported count for August 2026 although claims received rose, so the two series cannot both be measured the same way.",
    "The Ministry of Tribal Affairs should publish the August 2026 monthly progress report with its definition of disposed and a reconciliation to the 31 May 2025 table.",
    "funnel")

# section 2: state split of titled share
rows2 = sorted(BIG, key=SHARE.get)
s2 = insight(
    "Titled share of claims: 5.5% in Karnataka, 79.2% in Andhra Pradesh, among large states",
    bars("In 13 states with over 1 lakh claims the titled share ranges from 5.5% to 79.2%",
         [(k, round(SHARE[k], 1)) for k in rows2],
         accent="Karnataka", unit="%", vmax=85,
         sub=(f"Titles distributed as a share of claims received, per cent, as on 31 May 2025, for states with at least 1,00,000 claims. Karnataka rejected {ST['Karnataka'][6]:,} of {ST['Karnataka'][2]:,} claims, {100 * ST['Karnataka'][6] / ST['Karnataka'][2]:.1f}%. The all-India share is {SH25[0]:.2f}%."),
         source="PIB release 2150804, 31 July 2025 (official, read in full); shares computed here.")
    + numbers(["State", "Claims", "Titles", "Rejected", "Pending", "Titled %"],
              [[k, f"{v[2]:,}", f"{v[5]:,}", ("not reported" if v[6] is None else f"{v[6]:,}"), f"{v[8]:,}", f"{SHARE[k]:.1f}%"] for k, v in sorted(ST.items(), key=lambda kv: -kv[1][2])],
              "Show all 21 states and union territories"),
    f"Titled shares differ by a factor of 14 between large states, so the all-India share of {SH25[0]:.0f}% describes no state.",
    "The Ministry of Tribal Affairs should publish rejection reasons by state and the outcome of the Supreme Court's 2019 direction to review rejected claims.",
    "states")

# section 3: pending concentration
rows3 = [(k, round(ST[k][8] / 1e5, 2)) for k in sorted(ST, key=lambda x: -ST[x][8])[:6]]
rest = (PE - sum(ST[k][8] for k in sorted(ST, key=lambda x: -ST[x][8])[:6])) / 1e5
rows3.append(("All other 15 states and territories", round(rest, 2)))
s3 = insight(
    "Four states hold 84.1% of the 7.50 lakh claims pending on 31 May 2025",
    bars("Telangana alone holds 3.29 lakh of 7.50 lakh pending claims, 43.9%",
         rows3, accent="Telangana", unit=" lakh", fmt=lk, vmax=3.6,
         sub=f"Claims pending disposal by state, lakh, as on 31 May 2025. Telangana had disposed {ST['Telangana'][7] / ST['Telangana'][2] * 100:.2f}% of its claims, the lowest share among states with over 1 lakh claims after Assam ({100 * ST['Assam'][7] / ST['Assam'][2]:.2f}%). Totals sum to {PE:,} (checked).",
         source="PIB release 2150804, 31 July 2025 (official, read in full); shares computed here.")
    + numbers(["State", "Pending", "Claims", "Pending % of claims"],
              [[k, f"{ST[k][8]:,}", f"{ST[k][2]:,}", f"{100 * ST[k][8] / ST[k][2]:.1f}%"] for k in sorted(ST, key=lambda x: -ST[x][8])[:8]],
              "Show the eight largest pending counts"),
    f"A national pending count of 7.50 lakh is mostly four states, so clearing it depends on Telangana, Odisha, Assam and Gujarat.",
    "The Ministry of Tribal Affairs should publish the pending count by stage (Gram Sabha, sub-division committee, district committee) for those four states.",
    "pending")

# section 4: area per title
s4 = insight(
    "A community title covers 160 acres on average and an individual title 2.2 acres",
    bars("Community titles are 4.8% of titles and 78.2% of the recognised forest area",
         [("Community title, acres (18 states that report area)", round(COM_AC, 1)), ("Individual title, acres (same states)", round(IND_AC, 1)),
          ("Area added per title added, Oct 2023 to May 2025", round(D_A / D_T, 1)), ("Area per title, 31 Oct 2023", round(A23_TOT / T23_TI, 2))],
         accent="Community title, acres (18 states that report area)", unit=" acres", vmax=170,
         sub=(f"Acres per title on 31 May 2025 for the {T_REP:,} titles in the 18 states that report area; Assam, Uttar Pradesh and Jammu and Kashmir report area as not available. All-title average over {TI:,} titles is {AC_TOT[2] / TI:.2f} acres (232.74 lakh acres). Between 31 Oct 2023 and 31 May 2025 titles rose by {D_T:,} and area by {D_A / 1e5:.2f} lakh acres, {100 * D_AC / D_A:.1f}% of it community area."),
         source="PIB release 2147815, 24 July 2025, and PIB release 1985799, 13 December 2023 (official, read in full); averages computed here.")
    + numbers(["Item", "Value", "Source and status"],
              [["Area, 31 May 2025", f"{AC_TOT[2] / 1e5:.2f} lakh acres ({AC_TOT[0] / 1e5:.2f} individual, {AC_TOT[1] / 1e5:.2f} community)", "PIB 2147815 (official)"],
               ["Area, 31 Oct 2023", f"{A23_TOT / 1e5:.2f} lakh acres ({A23_IND / 1e5:.2f} individual, {A23_COM / 1e5:.2f} community) on {T23_TI:,} titles", "PIB 1985799 (official)"],
               ["Chhattisgarh", f"{100 * CH_AC:.1f}% of the recognised area and {100 * ST['Chhattisgarh'][5] / TI:.1f}% of titles", "Computed from PIB 2147815 and 2150804"],
               ["Area, 31 Aug 2026", f"nearly 238 lakh acres, {(AC26 - AC_TOT[2]) / 1e5:.2f} lakh more than May 2025 (computed from a rounded figure); {AC26 / T26:.2f} acres a title", "Secondary summaries; the backgrounder was not read"],
               ["Uttarakhand", "185 titles with 0 acres printed", "PIB 2147815: area may be unreported rather than zero"]],
              "Show the area figures and caveats"),
    "Most recognised area is community forest area in a few states, so a count of titles says little about how much forest land is recognised.",
    "The Ministry of Tribal Affairs should add area per title, by individual and community title and by state, to each monthly progress report.",
    "area")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Tribal Affairs:</b> publish the monthly progress report for August 2026 by state, with a stated definition of claims disposed and a reconciliation to the 31 May 2025 table.</li>
<li><b>Ministry of Tribal Affairs:</b> report rejected claims by state with reasons and the count restored after review, in line with the Supreme Court direction of 2019.</li>
<li><b>State governments of Telangana, Odisha, Assam and Gujarat:</b> publish pending claims by stage and the date by which each stage will be cleared.</li>
<li><b>Ministry of Tribal Affairs:</b> publish area per title for every state, with Assam, Uttar Pradesh and Jammu and Kashmir reporting the area they currently mark as not available.</li>
<li><b>Ministry of Tribal Affairs:</b> publish the field list and counts of the National FRA Digital Platform, so that its claims data can be compared with the state monthly reports.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>The state table of 31 May 2025 is the Annexure to PIB release 2150804 (31 July 2025); every column was summed and matched to the printed total, and each state row was checked: individual plus community equals total, titles plus rejected equals disposed, and disposed plus pending equals received.</li>
<li>Assam&rsquo;s rejected claims are printed as not available or not reported; disposed equals titles for Assam, so rejected is treated as zero in sums and Assam&rsquo;s pending of 96,209 is claims less titles.</li>
<li>Area figures are from PIB release 2147815 (24 July 2025) and PIB release 1985799 (13 December 2023). Average area per title divides area by titles in the 18 states that report area.</li>
<li>For 31 August 2026 only secondary summaries of a PIB backgrounder were found, through search excerpts. Claims received of about 54.0 lakh are checked against 43.56 lakh disposed at 80.64%. Rejected and pending counts are computed from rounded figures.</li>
<li>Percentages and sums are computed here and checked by assertions in the builder.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The PIB backgrounder of 16 November 2026 itself, and the Ministry of Tribal Affairs monthly progress report for 2026: the ministry site was refused by the research network and the backgrounder did not appear in searches, so every 2026 figure is from secondary summaries.</li>
<li>Why the disposed count is 43.56 lakh in August 2026 against 43.73 lakh in May 2025 while claims rose. A different definition of disposed, a correction of data or a different base are all possible, and none is documented in the sources read.</li>
<li>What disposed includes. The 2025 table counts titles plus rejected claims as disposed; the 2026 summaries do not say whether the same rule applies.</li>
<li>The area per title in 2026 and the state split of the 2026 figures. The 238 lakh acres is reported as nearly, and no state table for August 2026 was found.</li>
<li>State coverage in 2026: summaries say the Act applies in 20 states and Jammu and Kashmir, which matches the 21 rows of the 2025 table, but no 2026 table was seen.</li>
<li>Whether Uttarakhand&rsquo;s 185 titles carry zero area or unreported area, and the area of Assam, Uttar Pradesh and Jammu and Kashmir.</li>
<li>Anything about the National FRA Digital Platform beyond PIB&rsquo;s description that it will bring claims from Gram Sabha submission to digitally signed titles onto one system; the PIB release of 11 November 2026 says it will be launched, and the launch itself is reported only by summaries.</li>
<li>The October 2026 reports of about 11 lakh pending and over 18 lakh rejected were read as search excerpts only.</li>
</ul></details>
'''

step(6, "assembling body and page")
body = STYLE + top + tvo + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2150804&amp;reg=48&amp;lang=2">PIB, Ministry of Tribal Affairs, 31 July 2025: state-wise claims, titles, rejected and pending as on 31 May 2025</a> and '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2147815">PIB, 24 July 2025: state-wise area as on 31 May 2025</a> and '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=1985799">PIB, 13 December 2023: titles and area as on 31 October 2023</a> (official; page text read); '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2335189&amp;reg=48&amp;lang=2">PIB, 11 November 2026: Janjatiya Gaurav Pakhwada 2026</a> (official; page text read; the National FRA Digital Platform line); '
    '<a href="https://www.legacyias.com/pib-summaries-17-november-2026/">Legacy IAS, PIB summaries, 17 November 2026</a>, '
    '<a href="https://www.insightsonindia.com/2026/11/17/forest-rights-act-fra-2006-key-provisions-and-analysis/">Insights IAS, 17 November 2026</a> and '
    '<a href="https://theshillongtimes.com/2026/10/10/tribal-affairs-ministry-says-25-lakh-titles-distributed-under-forest-rights-act/">The Shillong Times, 10 October 2026</a> (secondary; search excerpts only; figures as on 31 August 2026). '
    'Percentages, averages and the 2026 rejected and pending counts computed by this blog. Analysed 25 November 2026.')
RELATED = []

build("Policy &middot; Tribal affairs", TITLE,
      "The Forest Rights Act, 2006 has recognised 25.42 lakh titles on about 238 lakh acres by the latest reported count; this piece sets the claims funnel and state split from the Ministry of Tribal Affairs table of May 2025 beside the 2026 headline figures, and lists what the sources do not show.",
      body, SOURCES, RELATED, str(OUT))
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
step(7, "banned-name and h1 checks passed")
print("wrote", OUT.relative_to(ROOT), len(plain), "chars in title")
step(8, "complete")
