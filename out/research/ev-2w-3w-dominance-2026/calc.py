"""Arithmetic and consistency checks for the 'two- and three-wheelers dominate India's EV sales' post.
Importing this module runs every check (assert) and prints progress with elapsed time and a time-to-completion estimate.
Every input below was read from a page opened during this work (raw copies in raw/) unless marked EXCERPT or ASSUMPTION.
Analysed 26 November 2026."""
import time

_T0 = time.time()
_STAGES = 7
_done = 0


def stage(msg):
    global _done
    _done += 1
    el = time.time() - _T0
    eta = el / _done * (_STAGES - _done)
    print(f"[{_done}/{_STAGES}] {msg}  (elapsed {el:.1f}s, est. {eta:.1f}s to completion)")


# ---------------------------------------------------------------- A. FY22-FY25: CEEW issue brief, Dec 2025, Figures 3 and 4
# Vahan registrations, Telangana excluded (CEEW section 2). Only the segment labels printed on the chart are used.
CEEW_TOTAL = {"FY22": 459_061, "FY23": 1_183_329, "FY24": 1_681_329, "FY25": 1_964_831}    # Figure 3
CEEW_E2W = {"FY22": 252_794, "FY23": 728_267, "FY24": 948_641, "FY25": 1_150_727}           # Figure 4 labels
CEEW_ERICK = {"FY22": 173_805, "FY23": 373_398, "FY24": 531_054, "FY25": 539_486}
CEEW_E3W = {"FY24": 101_747, "FY25": 159_540}                                              # FY22, FY23 not labelled on the chart
CEEW_E4WP = {"FY24": 80_472, "FY25": 101_057}

# ---------------------------------------------------------------- B. FY25 and FY26: Autocar Pro (Vahan, 1 to 6 April 2026)
AP = {"FY25": dict(total=1_967_547, e2w=1_150_780, e3w=698_914),
      "FY26": dict(total=2_451_719, e2w=1_401_663, e3w=830_818, epv=199_590, ecv=19_648, ebus=5_039)}
# retail denominators, FADA, FY2025-26
FADA = dict(w2=21_420_386, w3=1_363_412, pv=4_705_056, w2_prev=18_889_595, w3_prev=1_220_834)

# ---------------------------------------------------------------- C. FY26: EVreporter (Vahan plus Telangana RTO portal; low-speed e-2W excluded)
EVR26 = dict(total=2_550_865, e2w=1_472_029, erick=477_765, ecart=86_466, e4w=222_870, goods=14_803)
EVR26_L5M_SHARE = 0.094        # printed as 9.4% of EV sales; the unit count is not printed, so it is derived (+/- 0.05 points)
EVR26_PEN = dict(e2w=6.6, l5m=33.7, e4w=4.6, goods=1.6)   # EVreporter segment penetration; e-rickshaw and e-cart excluded from 3W

# ---------------------------------------------------------------- D. H1 FY27 monthly, EVreporter, as first reported on the 1st or 2nd of the next month
KEYS = ["e2w", "l5m", "l5n", "erick", "ecart", "e4w", "ebus", "goods", "others"]
MONTHS = {  # headline total, then components; None = not printed and derived as the residual
    "Apr": (239_014, dict(e2w=148_740, l5m=25_418, l5n=3_238, erick=28_151, ecart=7_742, e4w=23_314, ebus=347, goods=1_887, others=177)),
    "May": (271_019, dict(e2w=170_452, l5m=30_579, l5n=3_992, erick=29_803, ecart=7_486, e4w=26_226, ebus=320, goods=2_062, others=99)),
    "Jun": (305_678, dict(e2w=193_603, l5m=33_677, l5n=4_348, erick=32_123, ecart=7_297, e4w=31_388, ebus=710, goods=2_487, others=54)),
    "Jul": (327_557, dict(e2w=204_201, l5m=40_198, l5n=4_860, erick=34_716, ecart=7_277, e4w=32_609, ebus=548, goods=2_977, others=171)),
    "Aug": (298_048, dict(e2w=183_077, l5m=40_419, l5n=4_583, erick=28_811, ecart=6_029, e4w=30_424, ebus=908, goods=3_773, others=None)),
    "Sep": (333_571, dict(e2w=207_314, l5m=44_738, l5n=5_368, erick=29_509, ecart=6_409, e4w=36_010, ebus=832, goods=3_329, others=None)),
}
OCT = (354_284, dict(e2w=223_964, l5m=47_260, l5n=6_868, erick=27_529, ecart=6_912, e4w=36_745, ebus=768, goods=4_124, others=114))
SEP_REVISED = dict(total=337_859, e2w=208_724, l5m=45_202)       # same month as shown on the November page
SEP_NUVAMA_E2W = 203_411                                         # Autocar Pro, Nuvama, 1 October
SEP_INC42_E2W = 208_688                                          # Inc42, Vahan, 3 November

# ---------------------------------------------------------------- E. battery pack sizes, kWh (low, mid, high). Status in PACKS_NOTE.
PACKS = {"e2w": (2.2, 3.0, 3.7), "erick": (3.2, 5.4, 7.2), "ecart": (3.2, 5.4, 7.2), "l5m": (7.4, 9.0, 12.1),
         "l5n": (8.9, 10.24, 13.0), "e4w": (24.0, 35.0, 45.0), "goods": (14.0, 21.3, 32.0), "ebus": (150.0, 250.0, 366.66)}
LABEL = {"e2w": "e-2W", "erick": "E-rickshaw (L3)", "ecart": "E-cart (L3)", "l5m": "e-3W L5 passenger", "l5n": "e-3W L5 cargo",
         "e4w": "e-car (4W)", "goods": "e-goods carrier", "ebus": "e-bus"}


def _share(n, d):
    return 100 * n / d


# =============================================================== stage 1: sample, FY22-FY25 CEEW series and its internal checks
SAMPLE = {}
for fy in CEEW_TOTAL:
    assert CEEW_E2W[fy] + CEEW_ERICK[fy] < CEEW_TOTAL[fy]
for fy in ("FY24", "FY25"):                       # exact where every 2W/3W segment is labelled
    w23 = CEEW_E2W[fy] + CEEW_ERICK[fy] + CEEW_E3W[fy]
    SAMPLE[fy] = _share(w23, CEEW_TOTAL[fy])
    assert w23 + CEEW_E4WP[fy] <= CEEW_TOTAL[fy]            # labelled segments cannot exceed the total
for fy in ("FY22", "FY23"):                       # lower bound: e-3W (L5) is not labelled
    SAMPLE[fy] = _share(CEEW_E2W[fy] + CEEW_ERICK[fy], CEEW_TOTAL[fy])
W23 = {fy: round(v, 1) for fy, v in SAMPLE.items()}
assert W23 == {"FY24": 94.1, "FY25": 94.1, "FY22": 92.9, "FY23": 93.1}, W23
E2W_SH = {fy: round(_share(CEEW_E2W[fy], CEEW_TOTAL[fy]), 1) for fy in CEEW_TOTAL}
assert E2W_SH == {"FY22": 55.1, "FY23": 61.5, "FY24": 56.4, "FY25": 58.6}, E2W_SH
ERICK_SH = {fy: round(_share(CEEW_ERICK[fy], CEEW_TOTAL[fy]), 1) for fy in CEEW_TOTAL}
assert ERICK_SH == {"FY22": 37.9, "FY23": 31.6, "FY24": 31.6, "FY25": 27.5}, ERICK_SH
stage("CEEW FY22-FY25 series: sums and bounds pass (FY24, FY25 exact; FY22, FY23 lower bounds)")

# =============================================================== stage 2: cross-check CEEW against Autocar Pro on the overlap year FY25
d_total = AP["FY25"]["total"] - CEEW_TOTAL["FY25"]
d_e2w = AP["FY25"]["e2w"] - CEEW_E2W["FY25"]
d_e3w = AP["FY25"]["e3w"] - (CEEW_E3W["FY25"] + CEEW_ERICK["FY25"])
assert (d_total, d_e2w, d_e3w) == (2_716, 53, -112), (d_total, d_e2w, d_e3w)
assert abs(d_e2w) / CEEW_E2W["FY25"] < 0.0001 and abs(d_e3w) / AP["FY25"]["e3w"] < 0.0005   # agree to 0.01% and 0.02%
w23_ap25 = _share(AP["FY25"]["e2w"] + AP["FY25"]["e3w"], AP["FY25"]["total"])
assert round(w23_ap25, 1) == 94.0
a = AP["FY26"]
assert a["e2w"] + a["e3w"] + a["epv"] + a["ecv"] == a["total"]            # the four Autocar Pro segments add to its total
W23_FY26 = round(_share(a["e2w"] + a["e3w"], a["total"]), 1)
assert W23_FY26 == 91.1, W23_FY26
E2W_FY26 = round(_share(a["e2w"], a["total"]), 1)
E3W_FY26 = round(_share(a["e3w"], a["total"]), 1)
EPV_FY26 = round(_share(a["epv"], a["total"]), 1)
assert (E2W_FY26, E3W_FY26, EPV_FY26) == (57.2, 33.9, 8.1)
GROWTH_E2W = round(100 * (a["e2w"] / AP["FY25"]["e2w"] - 1))
assert GROWTH_E2W == 22                                                    # Autocar Pro prints +22%
stage("Autocar Pro FY25 matches CEEW to 0.01% (e-2W) and 0.02% (e-3W); FY26 segments add to total")

# =============================================================== stage 3: EVreporter FY26 and the conflict with Autocar Pro
E = EVR26
L5M = round(EVR26_L5M_SHARE * E["total"])
assert L5M == 239_781
EBUS_XSRC = AP["FY26"]["ebus"]                    # cross-source: EVreporter prints no e-bus count in the excerpt
named = E["e2w"] + E["erick"] + E["ecart"] + E["e4w"] + E["goods"] + L5M + EBUS_XSRC
L5N = E["total"] - named                          # residual = L5 cargo plus 'others'; 'others' are forklifts and the like
assert L5N == 32_112
assert E["e2w"] + E["erick"] + E["ecart"] + E["e4w"] + E["goods"] == 2_273_933
GAP_E2W = E["e2w"] - AP["FY26"]["e2w"]
GAP_TOTAL = E["total"] - AP["FY26"]["total"]
assert (GAP_E2W, GAP_TOTAL) == (70_366, 99_146)
GAP_E2W_PCT = round(100 * GAP_E2W / AP["FY26"]["e2w"], 1)
GAP_TOTAL_PCT = round(100 * GAP_TOTAL / AP["FY26"]["total"], 1)
assert (GAP_E2W_PCT, GAP_TOTAL_PCT) == (5.0, 4.0)
GAP_4W = E["e4w"] - AP["FY26"]["epv"]
assert GAP_4W == 23_280 and round(100 * GAP_4W / AP["FY26"]["epv"], 1) == 11.7
EVR_E2W_SH = round(_share(E["e2w"], E["total"]), 1)
assert EVR_E2W_SH == 57.7              # EVreporter prints 57.9%; the printed total and unit count give 57.7%: a published inconsistency
EVR_ERICK_SH = round(_share(E["erick"], E["total"]), 1)
assert EVR_ERICK_SH == 18.7            # printed as 18.8%
# 2W+3W share on EVreporter's FY26 counts: lower bound drops L5 cargo; upper bound removes only the cars and goods carriers
lo = E["e2w"] + E["erick"] + E["ecart"] + L5M
hi = E["total"] - E["e4w"] - E["goods"]
W23_EVR_LO, W23_EVR_HI = round(_share(lo, E["total"]), 1), round(_share(hi, E["total"]), 1)
assert (W23_EVR_LO, W23_EVR_HI) == (89.2, 90.7), (W23_EVR_LO, W23_EVR_HI)
# the same share with the L5 cargo residual counted as 3W (it is mostly L5 cargo) and e-buses removed
W23_EVR_MID = round(_share(lo + L5N, E["total"]), 1)
assert W23_EVR_MID == 90.5, W23_EVR_MID
stage("EVreporter FY26: derived L5M and L5N counts, conflict sizes with Autocar Pro, share bounds")

# =============================================================== stage 4: H1 FY27 monthly series (sample April, then scale to the six months)
H1 = {k: 0 for k in KEYS}
H1_TOTAL = 0
DERIVED = {}
t4 = time.time()
for i, (mon, (tot, comp)) in enumerate(MONTHS.items(), 1):
    comp = dict(comp)
    missing = [k for k, v in comp.items() if v is None]
    s = sum(v for v in comp.values() if v is not None)
    if missing:
        assert len(missing) == 1
        comp[missing[0]] = tot - s                                   # 'others' derived as the residual
        DERIVED[mon] = (missing[0], comp[missing[0]])
        assert 0 <= comp[missing[0]] < 100
    got = sum(comp.values())
    if mon == "Jun":
        assert got - tot == 9                                        # the page's headline is 9 below its own components
        tot = got
    assert got == tot, (mon, got, tot)
    for k in KEYS:
        H1[k] += comp[k]
    H1_TOTAL += tot
    print(f"    month {i}/6 {mon}: {tot:,} registrations, sums checked ({time.time() - t4:.2f}s)")
assert DERIVED == {"Aug": ("others", 24), "Sep": ("others", 62)}
assert H1_TOTAL == sum(H1.values()) == 1_774_896, H1_TOTAL
OCT_TOTAL, OCT_C = OCT
assert sum(OCT_C.values()) == OCT_TOTAL
H1_W23 = H1["e2w"] + H1["l5m"] + H1["l5n"] + H1["erick"] + H1["ecart"]
H1_W23_SH = round(_share(H1_W23, H1_TOTAL), 1)
H1_E2W_SH = round(_share(H1["e2w"], H1_TOTAL), 1)
H1_E4W_SH = round(_share(H1["e4w"], H1_TOTAL), 1)
assert (H1_W23_SH, H1_E2W_SH, H1_E4W_SH) == (88.7, 62.4, 10.1), (H1_W23_SH, H1_E2W_SH, H1_E4W_SH)
OCT_W23_SH = round(_share(OCT_C["e2w"] + OCT_C["l5m"] + OCT_C["l5n"] + OCT_C["erick"] + OCT_C["ecart"], OCT_TOTAL), 1)
OCT_E2W_SH = round(_share(OCT_C["e2w"], OCT_TOTAL), 1)
assert (OCT_W23_SH, OCT_E2W_SH) == (88.2, 63.2)                      # 63.2% matches the Ticker/Finology figure quoted in the brief
# cross-checks against other sources
assert abs(H1["e2w"] - 1_108_606) / 1_108_606 < 0.002                # Nuvama, via Autocar Pro: 1,108,606 e-2W in April-September
H1_JMK_GAP = round(100 * (1_789_000 - H1_TOTAL) / 1_789_000, 1)      # JMK 17.89 lakh as quoted in the live post (EXCERPT, JMK not opened)
assert H1_JMK_GAP == 0.8
SEP_REV_PCT = round(100 * (SEP_REVISED["total"] / MONTHS["Sep"][0] - 1), 1)
assert SEP_REV_PCT == 1.3
assert (SEP_REVISED["e2w"] - MONTHS["Sep"][1]["e2w"]) == 1_410
SEP_E2W_SPREAD = (SEP_NUVAMA_E2W, MONTHS["Sep"][1]["e2w"], SEP_REVISED["e2w"], SEP_INC42_E2W)
assert max(SEP_E2W_SPREAD) - min(SEP_E2W_SPREAD) == 5_313
stage("H1 FY27 (April-September 2026, EVreporter): six months added and cross-checked against Nuvama and JMK")

# =============================================================== stage 5: penetration against share
PEN = {"e2w": 100 * AP["FY26"]["e2w"] / FADA["w2"], "e3w": 100 * AP["FY26"]["e3w"] / FADA["w3"], "epv": 100 * AP["FY26"]["epv"] / FADA["pv"]}
assert (round(PEN["e2w"], 2), round(PEN["e3w"], 2), round(PEN["epv"], 2)) == (6.54, 60.94, 4.24)     # FADA prints 6.54% and 60.95%
SIZE_RATIO = FADA["w2"] / FADA["w3"]
PEN_RATIO = PEN["e3w"] / PEN["e2w"]
UNIT_RATIO = AP["FY26"]["e2w"] / AP["FY26"]["e3w"]
assert round(SIZE_RATIO, 1) == 15.7 and round(PEN_RATIO, 1) == 9.3 and round(UNIT_RATIO, 2) == 1.69
assert abs(UNIT_RATIO - SIZE_RATIO / PEN_RATIO) < 1e-9                # units ratio = market-size ratio / penetration ratio, exactly
assert round(100 * FADA["w2"] / (FADA["w2"] + FADA["w3"]), 1) == 94.0  # two-wheelers are 94.0% of two- plus three-wheeler retail
assert round(100 * (FADA["w2"] / FADA["w2_prev"] - 1), 1) == 13.4
stage("Penetration against share: units ratio equals market-size ratio divided by penetration ratio (exact)")

# =============================================================== stage 6: battery energy, FY26 (an estimate, not a registration figure)
COUNTS = dict(e2w=E["e2w"], erick=E["erick"], ecart=E["ecart"], l5m=L5M, l5n=L5N, e4w=E["e4w"], goods=E["goods"], ebus=EBUS_XSRC)
assert sum(COUNTS.values()) == E["total"]                              # by construction; 'others' (forklifts) carry zero energy here


def energy(packs_idx=1, counts=None, packs=None):
    c = counts or COUNTS
    p = packs or {k: v[packs_idx] for k, v in PACKS.items()}
    return {k: c[k] * p[k] / 1e6 for k in c}              # GWh


def shares(g):
    t = sum(g.values())
    return {k: 100 * v / t for k, v in g.items()}


G = energy()
G_TOTAL = sum(G.values())
assert round(G_TOTAL, 2) == 19.33, G_TOTAL
G_SH = {k: round(v, 1) for k, v in shares(G).items()}
U_SH = {k: round(_share(COUNTS[k], E["total"]), 1) for k in COUNTS}
W23_KEYS = ("e2w", "erick", "ecart", "l5m", "l5n")
W23_KWH_SH = round(sum(G[k] for k in W23_KEYS) / G_TOTAL * 100, 1)
W23_UNIT_SH = round(sum(COUNTS[k] for k in W23_KEYS) / E["total"] * 100, 1)
assert (W23_KWH_SH, W23_UNIT_SH) == (51.5, 90.5), (W23_KWH_SH, W23_UNIT_SH)
assert G_SH["e4w"] == 40.4 and U_SH["e4w"] == 8.7 and G_SH["ebus"] == 6.5 and U_SH["ebus"] == 0.2, (G_SH, U_SH)
assert G_SH["e2w"] == 22.9 and U_SH["e2w"] == 57.7
# sensitivity: pack size scenarios, and e-bus count
SCEN = {}
lowp, midp, highp = ({k: v[i] for k, v in PACKS.items()} for i in range(3))
SCEN["Every pack at its low value"] = energy(packs=lowp)
SCEN["Every pack at its mid value (base case)"] = energy(packs=midp)
SCEN["Every pack at its high value"] = energy(packs=highp)
mixA = {k: (highp[k] if k in W23_KEYS else lowp[k]) for k in PACKS}      # most favourable to 2W and 3W
mixB = {k: (lowp[k] if k in W23_KEYS else highp[k]) for k in PACKS}      # least favourable to 2W and 3W
SCEN["2W and 3W packs high, cars, goods and buses low"] = energy(packs=mixA)
SCEN["2W and 3W packs low, cars, goods and buses high"] = energy(packs=mixB)
SCEN_ROWS = []
for name, g in SCEN.items():
    t = sum(g.values())
    SCEN_ROWS.append((name, t, 100 * sum(g[k] for k in W23_KEYS) / t, 100 * g["e4w"] / t))
share_range = [r[2] for r in SCEN_ROWS]
assert round(min(share_range), 1) == 36.5 and round(max(share_range), 1) == 67.0, (min(share_range), max(share_range))
assert all(r[2] < W23_UNIT_SH - 23 for r in SCEN_ROWS)      # in every scenario the kWh share is at least 23 points below the unit share
BUS_SENS = []
for nb in (3_000, EBUS_XSRC, 11_000):
    cts = dict(COUNTS)
    cts["ebus"] = nb
    cts["l5n"] = COUNTS["l5n"] + EBUS_XSRC - nb                      # keep the total fixed; the difference moves to L5 cargo
    g = energy(counts=cts)
    BUS_SENS.append((nb, sum(g.values()), 100 * sum(g[k] for k in W23_KEYS) / sum(g.values())))
assert [round(r[2], 1) for r in BUS_SENS] == [52.9, 51.5, 47.6], BUS_SENS
# one-at-a-time: the e-car pack (24 to 45 kWh)
CAR_SENS = []
for kwh in (24.0, 35.0, 45.0):
    p = dict(midp); p["e4w"] = kwh
    g = energy(packs=p)
    CAR_SENS.append((kwh, sum(g.values()), 100 * sum(g[k] for k in W23_KEYS) / sum(g.values()), 100 * g["e4w"] / sum(g.values())))
assert [round(r[2], 1) for r in CAR_SENS] == [59.0, 51.5, 46.2], CAR_SENS
# H1 FY27 repeat with every count reported
H1C = dict(e2w=H1["e2w"], erick=H1["erick"], ecart=H1["ecart"], l5m=H1["l5m"], l5n=H1["l5n"], e4w=H1["e4w"], goods=H1["goods"], ebus=H1["ebus"])
g1 = energy(counts=H1C)
H1_G = sum(g1.values())
H1_W23_KWH = round(100 * sum(g1[k] for k in W23_KEYS) / H1_G, 1)
assert (round(H1_G, 2), H1_W23_KWH) == (14.31, 47.1), (H1_G, H1_W23_KWH)     # 'others' (H1 total less these eight) carry zero energy
assert H1_TOTAL - sum(H1C.values()) == H1["others"] == 24 + 62 + 177 + 99 + 54 + 171
stage("Battery energy FY26: base case, five pack scenarios, e-bus count and e-car pack sensitivity, H1 FY27 repeat")

# =============================================================== stage 7: running cost per km and subsidy facts
ELEC, CNG_P, PETROL_P = 10.6, 83.09, 102.12            # blog model, July 2026 basis (Rs/kWh, Rs/kg, Rs/L); the L is E20 petrol
KWH_KM, LOSS = 0.057, 0.10                            # WRI India Treo: 7.4 kWh over 130 km; charging loss is an ASSUMPTION
KM_KG, KM_L = 28.4, 20.1                              # WRI India TCO table (2020 evaluator): CNG and petrol autos
COST = dict(ev=ELEC * KWH_KM / (1 - LOSS), cng=CNG_P / KM_KG, petrol=PETROL_P / KM_L)
assert {k: round(v, 2) for k, v in COST.items()} == {"ev": 0.67, "cng": 2.93, "petrol": 5.08}, COST
assert round(COST["cng"] / COST["ev"], 1) == 4.4 and round(COST["petrol"] / COST["ev"], 1) == 7.6
COST_SENS = []
for el in (6.0, 10.6, 15.0):
    for loss in (0.0, 0.10, 0.20):
        COST_SENS.append((el, loss, el * KWH_KM / (1 - loss)))
assert round(min(c[2] for c in COST_SENS), 2) == 0.34 and round(max(c[2] for c in COST_SENS), 2) == 1.07
assert max(c[2] for c in COST_SENS) < COST["cng"]                       # the dearest electric case is still below CNG
CNG_SENS = [(kmkg, CNG_P / kmkg) for kmkg in (20.0, 28.4, 35.0)]
assert [round(c[1], 2) for c in CNG_SENS] == [4.15, 2.93, 2.37]
assert min(c[1] for c in CNG_SENS) > max(c[2] for c in COST_SENS)       # even the cheapest CNG case exceeds the dearest electric case
# blog model, two-wheelers (how-to-use-vehiclefuelmileage-running): petrol 1.93, EV 0.35 Rs/km
assert round(1.93 / 0.35, 1) == 5.5
# JMK (March 2026) L5 cargo 5-year TCO, Rs: CNG 904,859; electric without subsidy 806,556; with 756,556
assert 904_859 - 806_556 == 98_303 and 806_556 - 756_556 == 50_000
# state concentration, CEEW Table 1 (FY25 EV volume): ten states selected by CEEW for high penetration
ST = {"Uttar Pradesh": 377_212, "Maharashtra": 256_991, "Karnataka": 173_588, "Bihar": 113_609, "Delhi": 83_423, "Kerala": 82_279,
      "Assam": 67_967, "Goa": 10_088, "Tripura": 9_837, "Chandigarh": 5_714}
assert sum(ST.values()) == 1_180_708
TEN_SH = round(100 * sum(ST.values()) / CEEW_TOTAL["FY25"], 1)
assert TEN_SH == 60.1
TOP5 = sorted(ST.items(), key=lambda kv: -kv[1])[:5]
assert [n for n, _ in TOP5] == ["Uttar Pradesh", "Maharashtra", "Karnataka", "Bihar", "Delhi"]
TOP5_SH = round(100 * sum(v for _, v in TOP5) / CEEW_TOTAL["FY25"], 1)
assert TOP5_SH == 51.1
ST_SH = {n: round(100 * v / CEEW_TOTAL["FY25"], 1) for n, v in ST.items()}
assert ST_SH["Uttar Pradesh"] == 19.2 and ST_SH["Maharashtra"] == 13.1 and ST_SH["Karnataka"] == 8.8
# EVreporter e-2W by state, January to May 2026
E2W_JM = 774_924
MH, KA, TN_AMB, KL = 177_736, 99_305, 92_522, 43_226
assert round(100 * MH / E2W_JM, 1) == 22.9 and round(100 * KA / E2W_JM, 1) == 12.8 and round(100 * TN_AMB / E2W_JM, 1) == 11.9
TOP3_JM = round(100 * (MH + KA + TN_AMB) / E2W_JM, 1)
assert TOP3_JM == 47.7
stage("Running cost per km, state concentration and subsidy arithmetic")
print(f"all checks passed in {time.time() - _T0:.1f}s")
