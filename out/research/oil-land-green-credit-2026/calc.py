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
print("calc ok", NELP_PCT, OALP_PCT, DSF_PCT, NOM_BOTH, OALP_SHARE_OF_BASIN, SITES_HA, GCP_VS_SITES)
