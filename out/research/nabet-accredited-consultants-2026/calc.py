"""Arithmetic for the NABET-accredited-consultants article. Importing runs every assert.
Inputs, all in this folder:
  nabet_aco_2026-11-27.csv    one row per organisation on the NABET portal list (fetched 27 Nov 2026): state is parsed from the registered address
  nabet_scope_2026-11-27.csv  one row per organisation per sector in its scope (255 of the 256 organisations show sector lines)
  nabet_list_2022-02-14.csv, nabet_list_2022-05-09.csv   NABET's 'List of ACOs' PDFs, Rev. 19 and Rev. 23 (names, states, ORG codes)
Other figures are transcribed from sources named in build.py: India Together (2013), the NABET scheme text (2015), CAG Report 39 of 2016."""
import collections
import csv
import datetime
import pathlib
import re
import statistics

H = pathlib.Path(__file__).resolve().parent
TODAY = datetime.date(2026, 11, 27)
rd = lambda f: list(csv.DictReader(open(H / f, encoding="utf-8")))
orgs, scope = rd("nabet_aco_2026-11-27.csv"), rd("nabet_scope_2026-11-27.csv")
feb22, may22 = rd("nabet_list_2022-02-14.csv"), rd("nabet_list_2022-05-09.csv")
d = lambda s: datetime.datetime.strptime(s, "%d/%m/%Y").date()

N = len(orgs)
assert N == 256
CAT = collections.Counter(o["category"] for o in orgs)
assert CAT == {"A": 225, "B": 31}

# ---- time series of list sizes
SERIES = [("Sep 2013, QCI list (India Together)", 166), ("Jun 2015, scheme text, &lsquo;about&rsquo;", 170),
          ("14 Feb 2022, NABET list", len(feb22)), ("9 May 2022, NABET list", len(may22)), ("27 Nov 2026, NABET portal", N)]
assert (len(feb22), len(may22)) == (182, 181)
GROWTH = round(100 * (N / len(feb22) - 1))
assert GROWTH == 41
old_codes = {r["org_code"] for r in feb22}
cur_codes = {o["org_code"] for o in orgs if o["org_code"]}
STAYED, GONE, NEW = len(old_codes & cur_codes), len(old_codes - cur_codes), len(cur_codes - old_codes)
assert (len(old_codes), STAYED, GONE, NEW) == (182, 163, 19, 91) and len(cur_codes) == 254
NEW_SHARE = round(100 * NEW / len(cur_codes))
assert NEW_SHARE == 36
VINT = collections.Counter(d(o["accreditation_date"]).year for o in orgs)
SINCE_2021 = sum(v for y, v in VINT.items() if y >= 2021)
assert SINCE_2021 == 121 and sum(VINT.values()) == N

# ---- states (registered address)
ST = collections.Counter(o["state"] for o in orgs)
assert "UNKNOWN" not in ST and sum(ST.values()) == N
TOP3 = sum(v for _, v in ST.most_common(3)); TOP6 = sum(v for _, v in ST.most_common(6))
assert [k for k, _ in ST.most_common(6)] == ["Maharashtra", "Gujarat", "Uttar Pradesh", "Tamil Nadu", "Rajasthan", "Telangana"]
assert (TOP3, TOP6) == (106, 169) and round(100 * TOP3 / N) == 41 and round(100 * TOP6 / N) == 66
MINING3 = ST["Odisha"] + ST["Jharkhand"] + ST["Chhattisgarh"]
assert MINING3 == 15 and round(100 * MINING3 / N, 1) == 5.9
OTHER_STATES = N - sum(v for _, v in ST.most_common(8))
N_STATES = len(ST)
assert N_STATES == 23

# ---- validity
eff = []
for o in orgs:
    e = o["extension_letter_validity"]
    v = d(o["validity"])
    eff.append(max(v, d(e)) if e != "NA" else v)
LAPSED = sum(1 for x in eff if x < TODAY)
SOON = sum(1 for x in eff if TODAY <= x <= TODAY + datetime.timedelta(days=365))
assert (LAPSED, SOON) == (27, 82)
DUE = LAPSED + SOON
DUE_SHARE = round(100 * DUE / N)
assert DUE == 109 and DUE_SHARE == 43

# ---- sectors
names, tot, a_cap = {}, collections.Counter(), collections.Counter()
for s in scope:
    names[s["sector"]] = s["sector_name"]; tot[s["sector"]] += 1
    if s["sector_category"] == "A":
        a_cap[s["sector"]] += 1
ORG_WITH_SCOPE = len({s["sl"] for s in scope})
assert ORG_WITH_SCOPE == 255 and len(tot) == 41            # sector 26 was deleted from the scheme; 40 has four sub-items
per_org = collections.Counter(s["sl"] for s in scope)
MEDIAN_SECTORS, MAX_SECTORS = statistics.median(per_org.values()), max(per_org.values())
FEW = sum(1 for v in per_org.values() if v <= 3); MANY = sum(1 for v in per_org.values() if v >= 10)
assert (MEDIAN_SECTORS, MAX_SECTORS, FEW, MANY) == (7, 31, 59, 96)
short = {"38": "Building and construction (B projects only)", "1": "Mining of minerals", "4": "Thermal power plants",
         "23": "Integrated paint industry", "15": "Leather and hide processing", "14": "Soda ash", "30": "Ship breaking",
         "5": "Nuclear power and fuel processing", "35": "Aerial ropeways"}
assert (tot["38"], tot["1"], tot["4"], tot["23"], tot["15"], tot["14"], tot["30"], tot["5"], tot["35"]) == (207, 189, 111, 10, 6, 6, 6, 4, 2)
assert a_cap["5"] == 4 and a_cap["30"] == 6 and a_cap["14"] == 6 and a_cap["15"] == 4

# ---- CAG Report 39 of 2016, Table 2.8 (216 files of 249 sampled from 2,917 projects granted EC, 2011 to July 2015)
CAG = {"Infrastructure": (13, 38), "Thermal power": (10, 41), "River valley and hydro": (5, 7)}   # (consultant not registered for the activity, cases)
CAG_NOT = sum(a for a, _ in CAG.values()); CAG_CASES = sum(b for _, b in CAG.values())
assert (CAG_NOT, CAG_CASES) == (28, 86) and round(100 * CAG_NOT / CAG_CASES) == 33
assert sum(b for b in (39, 34, 37, 20, 38, 7, 41)) == 216
print("calc ok", N, GROWTH, STAYED, GONE, NEW, TOP3, TOP6, LAPSED, SOON, DUE, MEDIAN_SECTORS, CAG_NOT, CAG_CASES)

# ---- renewals by quarter ahead (effective validity = later of certificate and extension-letter dates)
def quarter_counts():
    edges = [TODAY + datetime.timedelta(days=91 * k) for k in range(5)]
    labels = ["27 Nov 2026 to Feb 2027", "Mar to May 2027", "Jun to Aug 2027", "Sep to 27 Nov 2027"]
    out = []
    for k in range(4):
        lo, hi = edges[k], (edges[k + 1] if k < 3 else TODAY + datetime.timedelta(days=365))
        out.append((labels[k], sum(1 for x in eff if lo <= x < hi or (k == 3 and x == hi))))
    return out
QUARTERS = quarter_counts()
assert sum(v for _, v in QUARTERS) == SOON, (QUARTERS, SOON)
BEYOND = sum(1 for x in eff if x > TODAY + datetime.timedelta(days=365))
assert BEYOND == 147 and LAPSED + SOON + BEYOND == N
