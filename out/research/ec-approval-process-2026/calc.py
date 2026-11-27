"""Arithmetic for the environmental-clearance explainer. Importing this file runs every assert.
Inputs: nabet_aco_2026-11-27.csv (the NABET portal's list of accredited EIA consultant organisations, fetched 27 Nov 2026),
and figures transcribed from the EIA Notification 2006 consolidated text (PARIVESH, 'as on 13 July 2026') and the PARIVESH register post."""
import csv
import datetime
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
FETCHED = datetime.date(2026, 11, 27)

rows = list(csv.DictReader(open(HERE / "nabet_aco_2026-11-27.csv", encoding="utf-8")))
d = lambda s: datetime.datetime.strptime(s, "%d/%m/%Y").date()


def current(r):
    ext = r["extension_letter_validity"]
    return d(r["validity"]) >= FETCHED or (ext != "NA" and d(ext) >= FETCHED)


N = len(rows)
A = [r for r in rows if r["category"] == "A"]
B = [r for r in rows if r["category"] == "B"]
A_OK = sum(current(r) for r in A)
B_OK = sum(current(r) for r in B)
A_LAPSED, B_LAPSED = len(A) - A_OK, len(B) - B_OK
assert (N, len(A), len(B)) == (256, 225, 31)
assert (A_OK, A_LAPSED, B_OK, B_LAPSED) == (203, 22, 26, 5), (A_OK, A_LAPSED, B_OK, B_LAPSED)
LAPSED = A_LAPSED + B_LAPSED
assert LAPSED == 27 and N - LAPSED == 229
SHARE_A = round(100 * len(A) / N, 1)
assert SHARE_A == 87.9

# statutory clocks, days (EIA Notification 2006, as consolidated 13 July 2026)
TOR_STANDARD_WORKING_DAYS = 7      # para 7(i)(II)(iv): standard ToR online, listed cases
TOR_REFERRAL = 30                  # para 7(i)(II)(v): refer to EAC/SEAC within 30 days, else standard ToR issue on day 30
HEARING_NOTICE_MIN = 30            # Appendix IV 3.1
HEARING_PROCEEDINGS = 45           # para 7(i)(III)(iii): SPCB forwards proceedings within 45 days of request
APPRAISAL = 60                     # para 7(i)(IV)(iii)
TO_AUTHORITY = 15                  # recommendation placed before the authority within the next 15 days (inside the 60+45)
DECISION = 45                      # para 8(i)
TOTAL_AFTER_FINAL_EIA = 105        # para 8(i) "in other words within one hundred and five days"
assert APPRAISAL + DECISION == TOTAL_AFTER_FINAL_EIA
ToR_VALID_YEARS, ToR_VALID_YEARS_RIVER = 4, 5

# PARIVESH 2.0 register, from this blog's earlier post (india-ec-approval-funnel-parivesh-20), same open API
FILED, LIVE, DECIDED, GRANTED = 113_970, 88_909, 61_361, 54_406
AUTO_DELISTED = 25_061
PIPELINE = 27_548
assert PIPELINE + DECIDED == LIVE
assert LIVE + AUTO_DELISTED == FILED
GRANT_RATE_DECIDED = round(100 * GRANTED / DECIDED, 1)
assert GRANT_RATE_DECIDED == 88.7
assert round(100 * AUTO_DELISTED / FILED) == 22
NSWS_CENTRAL, NSWS_STATE = 325, 2364          # nsws.gov.in home page, 'Access over 325 Central Approvals and 2364 State Approvals'
RATIO_STATE_TO_CENTRAL = round(NSWS_STATE / NSWS_CENTRAL, 1)
assert RATIO_STATE_TO_CENTRAL == 7.3
print("calc ok", N, len(A), len(B), A_OK, B_OK, LAPSED, GRANT_RATE_DECIDED, RATIO_STATE_TO_CENTRAL)
