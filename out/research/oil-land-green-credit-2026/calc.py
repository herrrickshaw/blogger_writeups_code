"""Arithmetic for the oil-sector land and Green Credit article. Importing runs every assert.
ppac_blocks_status_2026-04-01.csv: PPAC India's Oil & Gas Ready Reckoner FY2025-26 (version 1), Tables 2.7(A) and 2.7(B), source DGH, status as on 1 April 2026.
In the NELP table the 'relinquished' column is headed 'relinquished / proposed for relinquishment / termination notice sent / operational issues / PEL awaited', so it is broader than relinquishment alone.
In the OALP and DSF table the heading is 'relinquished / proposed for relinquishment'. Other figures are transcribed from the sources named in build.py."""
import csv
import pathlib

H = pathlib.Path(__file__).resolve().parent
rows = list(csv.DictReader(open(H / "ppac_blocks_status_2026-04-01.csv")))
ri = lambda v: int(v) if v not in ("", None) else 0


def tot(regime, key):
    return sum(ri(r[key]) for r in rows if r["regime"] == regime)


NELP_AW, NELP_REL, NELP_OP = tot("NELP", "awarded"), tot("NELP", "relinquished_or_proposed"), tot("NELP", "operational")
OALP_AW, OALP_REL, OALP_OP, OALP_WAIT = tot("OALP", "awarded"), tot("OALP", "relinquished_or_proposed"), tot("OALP", "operational"), tot("OALP", "pel_pml_awaited")
DSF_AW, DSF_REL, DSF_OP = tot("DSF", "awarded"), tot("DSF", "relinquished_or_proposed"), tot("DSF", "operational")
assert (NELP_AW, NELP_REL, NELP_OP) == (254, 222, 32) and NELP_REL + NELP_OP == NELP_AW
assert (OALP_AW, OALP_REL, OALP_OP, OALP_WAIT) == (172, 43, 129, 10) and OALP_REL + OALP_OP == OALP_AW
assert (DSF_AW, DSF_REL, DSF_OP) == (86, 37, 49) and DSF_REL + DSF_OP == DSF_AW
pct = lambda a, b: round(100 * a / b, 1)
NELP_PCT, OALP_PCT, DSF_PCT = pct(NELP_REL, NELP_AW), pct(OALP_REL, OALP_AW), pct(DSF_REL, DSF_AW)
assert (NELP_PCT, OALP_PCT, DSF_PCT) == (87.4, 25.0, 43.0)
OALP_ROUND = {r["round"]: pct(ri(r["relinquished_or_proposed"]), ri(r["awarded"])) for r in rows if r["regime"] == "OALP"}
assert OALP_ROUND["OALP-I"] == 40.0 and OALP_ROUND["OALP-II"] == 42.9 and OALP_ROUND["OALP-V"] == 45.5 and OALP_ROUND["OALP-VI"] == 9.5 and OALP_ROUND["OALP-IX"] == 0.0
# earlier counts of NELP blocks (254 awarded in all)
MOPNG_2018_REL, CAG_2019_REL, CAG_2019_OP = 188, 54 + 139, 61
assert MOPNG_2018_REL + 66 == 254 and CAG_2019_REL + CAG_2019_OP == 254

# acreage measures, sq km
PEL_NOMINATION_PSU, PEL_ALL_OTHER = 1583, 12539            # Lok Sabha USQ 700, 4 Dec 2025, as on 31.3.2025
ONGC_NOM, OIL_NOM_MOPNG = 94358, 5158                        # MoPNG block-award page: ONGC 9 PEL + 334 PML; OIL 3 PEL + 22 PML
NOM_BOTH = ONGC_NOM + OIL_NOM_MOPNG
assert NOM_BOTH == 99516
OIL_OPERATING = 52298                                         # OIL annual report 2024-25: 56 blocks, 31 Mar 2025
ONGC_OALP9 = 82560.26                                         # MoPNG annual report 2024-25: 15 OALP-IX blocks to ONGC
OALP_AWARDED_AREA = 378652                                    # Lok Sabha USQ 4563, 19 Mar 2026: 172 blocks
BASIN = 3_360_000                                             # MoPNG annual report 2024-25: 3.36 million sq km
OALP_SHARE_OF_BASIN = round(100 * OALP_AWARDED_AREA / BASIN, 1)
assert OALP_SHARE_OF_BASIN == 11.3
KANGRA, WB_A, WB_B = 3800, 3131, 3170
WB_SURRENDERED = WB_A + WB_B
assert WB_SURRENDERED == 6301

# Oil India land on the ground
SITES_SQM, SITES_N, TREES = 440_291, 32, 41_323               # integrated annual report 2025-26
SITES_HA = round(SITES_SQM / 10_000, 1)
GCP_PLANTED_HA, GCP_RESERVED_FY25_HA = 431, 601                # AR 2025-26; BRSR 2024-25
assert SITES_HA == 44.0
GCP_VS_SITES = round(GCP_PLANTED_HA / SITES_HA, 1)
assert GCP_VS_SITES == 9.8
# oily waste, tonnes
OTBL_CLAIM_T, ONGC_FY23_T, OIL_FY25_T, OIL_LEGACY_T = 1_500_000, 93_151, 3_425, 130_000
# Green Credit Programme land bank
GCP_SELECTED_HA, GCP_STATES, GCP_TAKEN_HA, GCP_ENTITIES = 4391, 12, 4258, 17
assert round(100 * GCP_TAKEN_HA / GCP_SELECTED_HA) == 97

# DGH / MoPNG annual report 2024-25 tables 2.7 to 2.11 (as on 31 March 2025) and DGH NDR 'Research and Invest' page (as on 31 March 2019)
ONGC_PEL_N, ONGC_PEL, ONGC_PML_N, ONGC_PML = 3, 1583, 325, 46890
OIL_PML_N, OIL_PML, OIL_PEL_TEXT = 25, 4828.84, 24.61
PSC_PEL_N, PSC_PEL, PSC_PML_N, PSC_PML = 15, 12539.31, 67, 8997.53
DSF_PML_N, DSF_PML = 56, 13129.80
OALP_PEL_N, OALP_PEL, OALP_PEL_DUE = 158, 227367, 177
ONGC_NOM_2025 = ONGC_PEL + ONGC_PML
assert ONGC_NOM_2025 == 48473
ONGC_CHANGE = ONGC_NOM - ONGC_NOM_2025
ONGC_CHANGE_PCT = round(100 * ONGC_CHANGE / ONGC_NOM, 1)
assert (ONGC_CHANGE, ONGC_CHANGE_PCT) == (45885, 48.6)
PEL_TOTAL = ONGC_PEL + PSC_PEL + OALP_PEL
PEL_TOTAL_WITH_OIL = round(PEL_TOTAL + OIL_PEL_TEXT, 2)
PML_TOTAL = round(ONGC_PML + OIL_PML + PSC_PML + DSF_PML, 2)
assert round(PEL_TOTAL, 2) == 241489.31 and PEL_TOTAL_WITH_OIL == 241513.92 and PML_TOTAL == 73846.17
PEL_2019, PML_2019 = 99_000, 71_000                # 0.099 and 0.071 million sq km, as on 31.03.2019
PEL_GROWTH = round(PEL_TOTAL_WITH_OIL / PEL_2019, 1); PML_GROWTH_PCT = round(100 * (PML_TOTAL / PML_2019 - 1))
assert PEL_GROWTH == 2.4 and PML_GROWTH_PCT == 4
PEL_SHARE_BASIN, PML_SHARE_BASIN = round(100 * PEL_TOTAL_WITH_OIL / BASIN, 1), round(100 * PML_TOTAL / BASIN, 1)
assert (PEL_SHARE_BASIN, PML_SHARE_BASIN) == (7.2, 2.2)
OALP_GRANTED_SHARE = round(100 * OALP_PEL / OALP_AWARDED_AREA)
assert OALP_GRANTED_SHARE == 60

# MoPNG side: net-zero dates (MoPNG table in the Committee on Public Undertakings report, Dec 2025), ONGC emissions, ETAC (Feb 2023)
NZ = {"GAIL": (2035, 38025), "ONGC": (2038, 200000), "NRL": (2038, 17000), "Oil India": (2040, None), "BPCL": (2040, 99600), "HPCL": (2040, 135347), "IOCL": (2046, 247160)}
BASE_YEAR = 2026
YEARS_TO = {k: v[0] - BASE_YEAR for k, v in NZ.items()}
assert YEARS_TO == {"GAIL": 9, "ONGC": 12, "NRL": 12, "Oil India": 14, "BPCL": 14, "HPCL": 14, "IOCL": 20}
ONGC_BASE_FY22, ONGC_FY26 = 9.41, 8.81                 # MMtCO2e, scope 1+2 (ETAC profile via earlier article; ONGC annual report 2025-26)
ONGC_PACE = round((ONGC_BASE_FY22 - ONGC_FY26) / 4, 2)
ONGC_NEEDED = round(ONGC_FY26 / (2038 - 2026), 2)
ONGC_PACE_RATIO = round(ONGC_NEEDED / ONGC_PACE, 1)
assert (ONGC_PACE, ONGC_NEEDED, ONGC_PACE_RATIO) == (0.15, 0.73, 4.9)
ONGC_CUT_PCT = round(100 * (ONGC_BASE_FY22 - ONGC_FY26) / ONGC_BASE_FY22, 1)
assert ONGC_CUT_PCT == 6.4
KG_LOW, KG_HIGH = 5, 6                                   # Koyali-Gandhar, million tonnes CO2 cumulative by 2040 (ETAC)
KG_SHARE_LOW, KG_SHARE_HIGH = round(100 * KG_LOW / ONGC_FY26), round(100 * KG_HIGH / ONGC_FY26)
assert (KG_SHARE_LOW, KG_SHARE_HIGH) == (57, 68)
print("calc ok", NELP_PCT, OALP_PCT, DSF_PCT, NOM_BOTH, OALP_SHARE_OF_BASIN, SITES_HA, GCP_VS_SITES)
