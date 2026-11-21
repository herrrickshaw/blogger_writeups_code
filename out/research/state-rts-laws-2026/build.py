"""Right-to-services laws across Indian states and UTs: who is covered, penalty and cap, appeal tiers, how many states and UTs have such laws, and what is counted.
Build from the repo root:  python3 out/research/state-rts-laws-2026/build.py   (writes out/post-india-right-to-service-laws-states.html)
Read in full from PRS copies on 21 November 2026: Delhi Act 10 of 2026; Karnataka Act 1 of 2012 with 2014 and 2026 amendments; Bihar Right to Public Services Act, 2011;
the English 2013 amendment to the Rajasthan Act (the principal Rajasthan text and the MP Act are page scans in the PRS PDFs with no text layer: their
English sections 6 to 8 were read by viewing the page images on 21 November 2026, which is a visual reading and not a text extract); PRS Legislative Brief of 27 September 2012 (comparison table of the 2011 state laws); PRS Annual Review of State Laws 2025 (ARSL 2025).
The count of 22 is from a Parliament answer published by PIB (Department of Administrative Reforms and Public Grievances); ARSL 2025 prints no count and the PIB text prints no list.
Names beyond the PRS documents come from the PIB text, a Lok Sabha answer, Acts and gazettes read as search excerpts (Meghalaya, Sikkim, Arunachal Pradesh, Chhattisgarh, Mizoram, Ladakh, Lakshadweep), commission pages (Chandigarh, Maharashtra) and lists (Wikipedia, Kerala Calling, SAFAR), all read on 21 November 2026. A blank cell means the figure was not read in an Act or named report."""
import pathlib
import re
import sys
import time
import html as _h

T0 = time.time()
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-right-to-service-laws-states.html"
B = "https://blog.vertistratsolution.com"
STEPS = 7


def step(n, what):
    el = time.time() - T0
    eta = el / n * (STEPS - n) if n else 0
    print(f"[{n}/{STEPS}] {what}  (elapsed {el:.1f}s, about {eta:.1f}s left)", flush=True)


HEADS = []


def H(t):
    HEADS.append(t)
    return t


# ---- 1. Laws named in documents that were read
step(1, "count of laws named in documents read, with consistency checks")
# PRS brief of 27 Sep 2012, table 'Sources' line: nine state laws
BRIEF_2012 = {"Madhya Pradesh", "Uttar Pradesh", "Jammu and Kashmir", "Delhi", "Bihar", "Himachal Pradesh", "Rajasthan", "Uttarakhand", "Punjab"}
assert len(BRIEF_2012) == 9
# Tier A: Act text read including the penalty clause (Goa from reproductions of its Gazette; Delhi is the 2026 Act)
TIER_A = {"Madhya Pradesh", "Rajasthan", "Bihar", "Karnataka", "Delhi", "Jharkhand", "Haryana", "West Bengal", "Gujarat", "Odisha", "Goa",
          "Uttar Pradesh", "Himachal Pradesh", "Uttarakhand", "Punjab", "Kerala",
          "Jammu and Kashmir", "Assam", "Meghalaya", "Sikkim", "Arunachal Pradesh", "Lakshadweep", "Chhattisgarh", "Maharashtra", "Mizoram", "Chandigarh", "Ladakh"}
# Tier B: Act, gazette or official commission page read, penalty clause not read (some as search excerpts)
TIER_B = set()   # empty: Chandigarh and Ladakh (extended or adapted Acts) were moved to tier A once their penalty text was read
# Tier C: named in reports or lists only (PRS 2012 brief, PRS ARSL 2025, PIB, Kerala Calling, SAFAR), Act text not opened
TIER_C = set()      # none left: the five states first named only in reports were read as Acts on 21 November 2026
BRIEF_2012 = {"Madhya Pradesh", "Uttar Pradesh", "Jammu and Kashmir", "Delhi", "Bihar", "Himachal Pradesh", "Rajasthan", "Uttarakhand", "Punjab"}
PIB_COMMISSIONS = {"Assam", "Chandigarh", "Maharashtra", "Punjab", "Haryana", "Meghalaya", "Uttarakhand", "West Bengal"}   # PIB text: Commissions in 8
WIKI_TABLE = BRIEF_2012 | {"Kerala", "Karnataka", "Chhattisgarh", "Odisha", "Assam", "Gujarat", "West Bengal", "Goa", "Haryana", "Maharashtra", "Mizoram", "Jharkhand"}
assert len(BRIEF_2012) == 9 and len(PIB_COMMISSIONS) == 8 and len(WIKI_TABLE) == 21
assert not (TIER_A & TIER_B) and not (TIER_A & TIER_C) and not (TIER_B & TIER_C)
NAMED = TIER_A | TIER_B | TIER_C
POST_2025 = {"Nagaland"}   # Act 11 of 2026, assented 30 Sep 2026, gazette 13 Oct 2026: after the March 2025 answers, so not one of the 27 names the 22 could leave out
assert not (POST_2025 & NAMED)
assert (len(TIER_A), len(TIER_B), len(TIER_C), len(NAMED)) == (27, 0, 0, 27)
assert PIB_COMMISSIONS <= NAMED and WIKI_TABLE <= NAMED and BRIEF_2012 <= NAMED
REPORTED = 22                      # PIB Rajya Sabha reply (3 April 2025) and Lok Sabha unstarred question 4216 (26 March 2025): 'enacted by 22 States and Union Territories'
OVER = len(NAMED) - REPORTED
assert PIB_COMMISSIONS <= NAMED and len(NAMED - PIB_COMMISSIONS) == 19 and len(NAMED) - REPORTED == 5   # the 8 Commission names are inside the 22, so 5 of the other 19 are left out
assert OVER == 5                   # the names found exceed the reported count by five, so the 22 cannot be a complete list of the names found
# Left out of the 27 on purpose: Andaman and Nicobar Islands (a 2026 draft Regulation, after the PIB statement), Telangana and Tamil Nadu (listed in one law journal whose cited
# sources are a petition and a newspaper piece; no Act was found)
EXCLUDED = {"Andaman and Nicobar Islands", "Telangana", "Tamil Nadu"}
assert not (EXCLUDED & NAMED)
# Delhi: 2011 law replaced by Delhi Act 10 of 2026, so Delhi is one state or UT with a law, not two
assert "Delhi" in BRIEF_2012
FIRST_YEAR, SECOND_YEAR_COUNT = 2010, 8       # brief: MP 2010; eight more state laws dated 2011 in the table's source list
assert len(BRIEF_2012) - 1 == SECOND_YEAR_COUNT
assert FIRST_YEAR == 2010

# ---- 2. Penalty and cap, as printed in Acts read
step(2, "penalty and appeal figures with consistency checks")
K_RATE, K_CAP = 20, 500
D_RATE, D_CAP = 250, 5000
assert K_CAP / K_RATE == 25 and D_CAP / D_RATE == 20
assert D_CAP / K_CAP == 10 and D_RATE / K_RATE == 12.5
# MP Act 24 of 2010, section 7(1) and 7(2), and Rajasthan Act 23 of 2011, section 7(1) and 7(2) (English text, read from page images)
MPRJ_LUMP_LOW, MPRJ_LUMP_HIGH, MPRJ_RATE, MPRJ_CAP = 500, 5000, 250, 5000
assert MPRJ_CAP == MPRJ_LUMP_HIGH == D_CAP and MPRJ_RATE == D_RATE and MPRJ_CAP / MPRJ_RATE == 20
# The PRS 2012 brief's grouped Bihar/MP/UP/Rajasthan row (Rs 500 to Rs 5,000; Rs 250 a day up to Rs 5,000) matches the MP and Rajasthan Acts read
GROUP_LUMP_LOW, GROUP_LUMP_HIGH, GROUP_RATE, GROUP_CAP = 500, 5000, 250, 5000
assert (GROUP_LUMP_LOW, GROUP_LUMP_HIGH, GROUP_RATE, GROUP_CAP) == (MPRJ_LUMP_LOW, MPRJ_LUMP_HIGH, MPRJ_RATE, MPRJ_CAP)
MP_FIRST_DAYS, MP_SECOND_DAYS, MP_REVISION_DAYS = 30, 60, 60     # MP Act sections 6(1), 6(3), 8
RJ_FIRST_DAYS, RJ_SECOND_DAYS, RJ_REVISION_DAYS = 30, 60, 60     # Rajasthan Act sections 6(1), 6(3), 8 (section 8 replaced in 2013: revision to the Commission)
assert MP_FIRST_DAYS == RJ_FIRST_DAYS == 30 and MP_SECOND_DAYS == RJ_SECOND_DAYS == 60
DELHI2011_COST = 10
assert D_RATE / DELHI2011_COST == 25
# Six further Acts (English text read as search excerpts of the official Acts and gazettes, 21 November 2026)
WB_RATE, WB_CAP, WB_LUMP_LOW = 250, 1000, 250              # West Bengal Act XVII of 2013, section 7(1)
GOA_RATE, GOA_CAP, GOA_DEFICIENT = 50, 2500, 500           # Goa Act 19 of 2013, section 12: Rs 50 a day or Rs 2,500, whichever is less; Rs 500 for deficiency
HR_RATE, HR_CAP, HR_LUMP_LOW, HR_COMP = 250, 5000, 250, 1000   # Haryana Act 4 of 2014, section 9: lump sum Rs 250 to Rs 5,000; compensation up to Rs 1,000
JH_RATE, JH_CAP, JH_LUMP_LOW = 250, 5000, 500              # Jharkhand Act 20 of 2011, section 7
OD_RATE, OD_FAIL_CAP = 250, 5000                           # Odisha Act 8 of 2012, section 8(1): up to Rs 5,000 for failure; up to Rs 250 a day, no aggregate cap printed
GJ_LUMP_LOW, GJ_LUMP_HIGH = 1000, 10000                    # Gujarat Act 16 of 2013, section 23(1): lump sum Rs 1,000 to Rs 10,000 for mala fide action or failure
assert WB_CAP / WB_RATE == 4 and GOA_CAP / GOA_RATE == 50
assert HR_CAP == JH_CAP == OD_FAIL_CAP == D_CAP and HR_RATE == JH_RATE == OD_RATE == D_RATE
assert GJ_LUMP_HIGH / K_CAP == 20 and GJ_LUMP_HIGH / D_CAP == 2
# Five further Acts (English text read as search excerpts of the official Acts and gazettes, 21 November 2026)
UP_RATE, UP_CAP, UP_LUMP_LOW = 250, 5000, 500            # Uttar Pradesh Act 3 of 2011, section 7(1)
HP_CAP, HP_LUMP_LOW = 5000, 1000                         # Himachal Pradesh Act 34 of 2011, section 8(1): lump sum Rs 1,000 to Rs 5,000 for failure or delay, no per-day rate
UK_CAP, UK_LUMP_LOW = 5000, 500                          # Uttarakhand Act 20 of 2011, section 9(1)(a): lump sum Rs 500 to Rs 5,000 (delay rate cap not visible in the excerpt)
PB_RATE, PB_CAP, PB_LUMP_LOW, PB_COMMISSION = 250, 5000, 500, 10000   # Punjab Act 24 of 2011, section 9; Commission power of Rs 10,000 a case from Act 10 of 2014, section 17(1)(h)
KL_LOW, KL_HIGH, KL_APPEAL_LOW, KL_APPEAL_HIGH = 1000, 10000, 2000, 15000   # Kerala Right to Public Service Act, 2025 (Act 12 of 2025), section 20(1) and 20(2)
KL2012_RATE, KL2012_CAP, KL2012_LUMP_LOW = 250, 5000, 500            # Kerala State Right to Service Act, 2012 (Act 18 of 2012), section 8, repealed by section 27 of the 2025 Act
assert UP_CAP == UK_CAP == PB_CAP == HP_CAP == D_CAP and UP_RATE == PB_RATE == D_RATE
assert KL_HIGH == GJ_LUMP_HIGH and KL_APPEAL_HIGH / KL_HIGH == 1.5 and PB_COMMISSION / PB_CAP == 2
assert KL_HIGH / KL2012_CAP == 2 and KL2012_CAP == D_CAP
# Eleven further laws (English text read as search excerpts of the Acts, gazettes and official pages, 21 November 2026)
JK_RATE, JK_CAP, JK_DEFICIENT = 250, 5000, 2000                    # J&K Public Services Guarantee Act, 2011, section 11: Rs 250 a day or Rs 5,000, whichever is less; Rs 2,000 for deficiency
JK_NONCOMPLY_LOW, JK_NONCOMPLY_HIGH = 500, 5000                    # section 10(2); section 12 (first appellate authority) Rs 500 to Rs 5,000
AS_2019_RATE, AS_2019_CAP = 250, 25000                             # Assam Act IX of 2012, section 9(1) as substituted by Assam Act VII of 2019 (India Code text)
AS_2024_DAY_MIN, AS_2024_CAP = 100, 5000                           # Assam Ordinance 2 of 2024 (gazette read), new section 9: first appellate authority, not less than Rs 100 a day, total up to Rs 5,000
AS_SAA_CAP, AS_COMM_CAP, AS_COMM_FAA_LOW, AS_COMM_SAA_LOW = 7000, 10000, 500, 1000   # second appellate authority Rs 7,000 (Ordinance and Bill 2024); Commission Rs 10,000, Rs 500 to Rs 5,000 on a first and Rs 1,000 to Rs 5,000 on a second appellate authority that delays (Ordinance 2 of 2024, gazette read in full, and the Bill of 2024 agree on every amount; the enacted Act XXII of 2024 could not be read)
NG_LUMP_LOW, NG_RATE, NG_CAP, NG_APPEAL, NG_REVISION = 500, 250, 5000, 30, 60   # Nagaland Right to Public Services Act, 2026 (Act 11 of 2026), Gazette 13 Oct 2026, read from page images: s.11(1)(a) lump sum Rs 500 to Rs 5,000; s.11(1)(b) Rs 250 a day, at most Rs 5,000; s.11(2) Rs 500 to Rs 5,000 on a first appellate authority that delays; s.9(1) second appeal 30 days; s.12 revision 60 days
BR_LUMP_LOW, BR_RATE, BR_CAP = 500, 250, 5000                       # Bihar Right to Public Services Rules, 2011, rule 8 (notified 3 May 2011): section 7(1)(a) and 7(2) lump sum Rs 500 to Rs 5,000; section 7(1)(b) Rs 250 a day, total at most Rs 5,000
AS_APPEAL_2, AS_APPEAL_3 = 60, 90                                   # Bill 2024: second appeal within 60 days, third appeal to the Commission within 90 days
AS_RULES_RATE, AS_RULES_CAP, AS_RULES_LUMP_LOW, AS_RULES_LUMP_HIGH = 50, 2000, 200, 2000   # Assam Rules, 2012, rule 6
MG_FIRST, MG_REPEAT, MG_SLIDES = 5000, 20000, 25000                # Meghalaya Act 18 of 2020, section 8(1); the Commission's slides say Rs 25,000
SK_FURTHER_RATE, SK_CAP = 100, 10000                               # Sikkim Act 15 of 2022: further Rs 100 a working day, total at most Rs 10,000 a case
AR_RATE, AR_CAP = 100, 5000                                        # Arunachal Pradesh Act 3 of 2016, section 9(1): Rs 100 a day, up to Rs 5,000 on the first occasion
LK_LOW, LK_HIGH = 1000, 10000                                      # Lakshadweep Regulation 2 of 2022, section 21(2)
CG_RATE, CG_CAP = 100, 1000                                        # Chhattisgarh Act 23 of 2011, section 4(4): Rs 100 a day, at most Rs 1,000, payable to the applicant
MZ_LUMP_LOW, MZ_LUMP_HIGH = 500, 5000                              # Mizoram Act 6 of 2015, section 11(1)(a), read from a public copy of the Mizoram Gazette Ex-156/2015
MZ_RATE, MZ_CAP = 250, 5000                                        # delay rate and cap: official press note of 1 February 2019 and a 2015 news report (rest of section 11 not seen)
MZ_FIRST_DAYS, MZ_FIRST_MAX, MZ_SECOND_DAYS, MZ_SECOND_MAX = 30, 60, 30, 60   # sections 8(1) and 9(1): 30 days, up to 60 with sufficient cause
MH_LOW, MH_HIGH = 500, 5000                                        # Maharashtra Act 31 of 2015, section 10(1) and (2), revisable by notification
assert JK_CAP / JK_RATE == 20 and AS_2019_CAP / AS_2019_RATE == 100 and AS_2024_CAP / AS_2024_DAY_MIN == 50
assert NG_RATE == D_RATE and NG_CAP == D_CAP and NG_RATE == BR_RATE and BR_RATE == D_RATE and BR_CAP == D_CAP and AS_COMM_CAP == 2 * AS_2024_CAP and AS_SAA_CAP == 7 * 1000 and AS_RULES_CAP / AS_RULES_RATE == 40 and MG_REPEAT / MG_FIRST == 4 and MG_SLIDES != MG_REPEAT
assert SK_CAP / SK_FURTHER_RATE == 100 and AR_CAP / AR_RATE == 50 and CG_CAP / CG_RATE == 10
assert LK_LOW == HP_LUMP_LOW and LK_HIGH == GJ_LUMP_HIGH == KL_HIGH
assert MZ_RATE == D_RATE and MZ_CAP == MZ_LUMP_HIGH == D_CAP and MH_HIGH == D_CAP and MZ_SECOND_MAX == 2 * MZ_SECOND_DAYS
CAPS_READ = {"Karnataka": K_CAP, "West Bengal": WB_CAP, "Goa": GOA_CAP, "Madhya Pradesh": MPRJ_CAP, "Rajasthan": MPRJ_CAP, "Jharkhand": JH_CAP,
             "Haryana": HR_CAP, "Odisha": OD_FAIL_CAP, "Delhi": D_CAP, "Uttar Pradesh": UP_CAP, "Himachal Pradesh": HP_CAP, "Uttarakhand": UK_CAP,
             "Punjab": PB_CAP, "Gujarat": GJ_LUMP_HIGH, "Kerala": KL_HIGH,
             "Jammu and Kashmir": JK_CAP, "Meghalaya": MG_FIRST, "Arunachal Pradesh": AR_CAP, "Maharashtra": MH_HIGH, "Chhattisgarh": CG_CAP,
             "Sikkim": SK_CAP, "Lakshadweep": LK_HIGH, "Mizoram": MZ_LUMP_HIGH,
             "Chandigarh": PB_CAP, "Ladakh": JK_CAP, "Assam": AS_2024_CAP, "Bihar": BR_CAP, "Nagaland": NG_CAP}   # Chandigarh: Punjab Act as extended (s.9); Ladakh: J&K Act as adapted (s.11)
assert len(CAPS_READ) == 28
FIVE_K = sorted(k for k, v in CAPS_READ.items() if v == 5000)
TEN_K = sorted(k for k, v in CAPS_READ.items() if v == 10000)
ONE_K = sorted(k for k, v in CAPS_READ.items() if v == 1000)
assert len(FIVE_K) == 20 and TEN_K == ["Gujarat", "Kerala", "Lakshadweep", "Sikkim"] and ONE_K == ["Chhattisgarh", "West Bengal"]
assert min(CAPS_READ.values()) == 500 and max(CAPS_READ.values()) == 10000
# Bihar's Act leaves the amounts to its Rules, whose rule 8 gives Rs 5,000, so every name now has a cap; Assam is charted at the first-stage cap of the 2024 text (Rs 5,000)
assert set(CAPS_READ) == TIER_A | POST_2025   # every name has a cap; Nagaland (Act 11 of 2026) post-dates the 2025 answers and is outside the 27
APPEAL = {  # days allowed for the step after the first appeal
    "Madhya Pradesh (second appellate authority)": MP_SECOND_DAYS,   # Act section 6(3)
    "Rajasthan (second appellate authority)": RJ_SECOND_DAYS,        # Act section 6(3)
    "Bihar (reviewing authority)": 60,       # Act section 6(3)
    "Karnataka (appellate authority)": 60,   # Act section 13(3) as in the Karnataka post
    "Haryana (second grievance redressal authority)": 60,   # Act section 7(1)
    "West Bengal (reviewing officer)": 60,   # Act section 6(3)
    "Jharkhand (second appellate authority)": 60,   # Act section 6(3)
    "Delhi (Commission)": 30,                # Act 10 of 2026 section 9(2)
    "Odisha (revisional authority)": 30,     # Act section 6
    "Uttar Pradesh (second appellate authority)": 60,   # Act section 6(3)
    "Himachal Pradesh (second appellate authority)": 60,   # Act section 7(1)
    "Uttarakhand (second appellate authority)": 30,   # Act section 7(1), as substituted in 2023
    "Punjab (second appellate authority)": 30,   # Act section 7(1)
    "Jammu and Kashmir (second appellate authority)": 60,   # Act section 7(1)
    "Assam (second appellate authority)": AS_APPEAL_2,   # Bill 2024, section 8: second appeal within 60 days; third appeal to the Commission within 90 days
    "Meghalaya (Commission)": 30,            # Act section 7(1)
    "Maharashtra (second appellate authority)": 30,   # Act section 9(3); a third appeal to the Commission has 60 days (section 18)
    "Arunachal Pradesh (second appellate authority)": 30,   # Act section 8(4)
    "Mizoram (second appellate authority)": MZ_SECOND_DAYS,   # Act section 9(1)
    "Nagaland (second appellate authority)": NG_APPEAL,   # Act section 9(1)
}
assert sorted(APPEAL.values()) == [30] * 9 + [60] * 11
SIXTY = sorted(k.split(" (")[0] for k, v in APPEAL.items() if v == 60)
THIRTY = sorted(k.split(" (")[0] for k, v in APPEAL.items() if v == 30)
assert len(SIXTY) == 11 and len(THIRTY) == 9
# Disposal counters named in the two single-state posts
KA_DISPOSAL = round(100 * 431_632_443 / 432_426_014, 2)
assert f"{KA_DISPOSAL:.2f}" == "99.82"
DL_IN_TIME = 65.02
assert 100 - DL_IN_TIME == 34.98 or round(100 - DL_IN_TIME, 2) == 34.98

TITLE = H("India&rsquo;s right-to-service laws: 22 states and UTs reported, caps from Rs 500 to Rs 10,000")
assert 55 <= len(_h.unescape(TITLE)) <= 90, len(_h.unescape(TITLE))

step(3, "writing sections")
top = top_line([
    (f"{REPORTED}", f" states and union territories have enacted right-to-service laws, according to two 2025 answers to Parliament; sources read name {len(NAMED)}, so the 22 is not a complete list and none of the answers names them."),
    (f"Rs {K_CAP} to Rs {GJ_LUMP_HIGH:,}", f" is the range of per-case caps in the 28 laws whose penalty clause was read: Karnataka Rs {K_CAP}, West Bengal and Chhattisgarh Rs {WB_CAP:,}, Goa Rs {GOA_CAP:,}, twenty laws Rs {D_CAP:,}, and four laws Rs {GJ_LUMP_HIGH:,}; Bihar&rsquo;s Act leaves the amounts to its Rules, which give Rs {BR_CAP:,}, and Assam&rsquo;s first stage caps at Rs {AS_2024_CAP:,} with Rs {AS_SAA_CAP:,} and Rs {AS_COMM_CAP:,} at later stages."),
    ("2010", " is the year Madhya Pradesh enacted the first such law, followed by eight state laws dated 2011 in a 2012 PRS table, including Bihar, Rajasthan and the first Delhi Act."),
])

s1 = insight(
    H(f"Per-case caps: Rs {K_CAP} to Rs {GJ_LUMP_HIGH:,} across 28 laws; twenty print Rs {D_CAP:,}"),
    bars(H(f"Twenty laws cap at Rs {D_CAP:,}; Karnataka caps at Rs {K_CAP}, four laws at Rs {GJ_LUMP_HIGH:,}"),
         [("Karnataka Act, section 9 (compensation to the citizen)", K_CAP),
          ("West Bengal (section 7) and Chhattisgarh (section 4(4), paid to the applicant)", WB_CAP),
          ("Goa Act, section 12 (Rs 50 a day)", GOA_CAP),
          ("Twenty laws, named in the note above the chart", D_CAP),
          ("Gujarat, Kerala (2025), Sikkim and Lakshadweep (Regulation)", GJ_LUMP_HIGH),
          ],
         accent=["Karnataka Act, section 9 (compensation to the citizen)", "Gujarat, Kerala (2025), Sikkim and Lakshadweep (Regulation)"],
         unit="", fmt=lambda v: f"Rs {v:,.0f}", vmax=11000,
         sub="Maximum per case, rupees, as printed. Rs 5,000: " + ", ".join(FIVE_K) + ". A dashed bar means no single figure is printed. Assam is shown at its first-stage cap of Rs 5,000; its later stages allow Rs 7,000 and Rs 10,000. Odisha&rsquo;s delay penalty has no aggregate cap in the excerpt read.",
         source="State Acts, gazettes and official pages (Madhya Pradesh and Rajasthan read from page scans; others as English text or search excerpts), 21 November 2026.")
    + numbers(["State and Act", "Delay", "Failure or rejection", "Who receives it", "Basis"],
              [["Madhya Pradesh, 2010", f"Rs {MPRJ_RATE} a day, to Rs {MPRJ_CAP:,} (section 7(1)(b))", f"Lump sum Rs {MPRJ_LUMP_LOW} to Rs {MPRJ_LUMP_HIGH:,} (section 7(1)(a))", "Penalty on the designated officer; the second appellate authority may order part of it paid to the appellant, not above the penalty (section 7(3))", "Act text read from the PRS page scan; a first appeal officer who fails to decide in time faces Rs 500 to Rs 5,000 (section 7(2))"],
               ["Bihar, 2011", f"Rs {BR_RATE} a day, total at most Rs {BR_CAP:,} (Act section 7(1)(b); Rules 2011, rule 8)", f"Lump sum Rs {BR_LUMP_LOW} to Rs {BR_CAP:,} (section 7(1)(a)); the same range on a reviewing authority that delays an appeal (section 7(2))", "Charged on the officer, appellate authority or staff (section 7(3)); recovered from salary or honorarium (rule 8)", "Act text read; the amounts are in rule 8 of the Bihar Right to Public Services Rules, 2011 (notified 3 May 2011), read in English and Hindi copies on a third-party site (secondary); later amendments to the Rules were not checked"],
               ["Rajasthan, 2011", f"Rs {MPRJ_RATE} a day, to Rs {MPRJ_CAP:,} (section 7(1)(b))", f"Lump sum Rs {MPRJ_LUMP_LOW} to Rs {MPRJ_LUMP_HIGH:,} (section 7(1)(a))", "Recovered from the designated officer&rsquo;s salary (section 7(1)(c)); compensation to the appellant out of the penalty, not above it (section 7(3))", "Act text read from the PRS page scan; first appeal officer who fails to decide in time faces Rs 500 to Rs 5,000 (section 7(2))"],
               ["Jharkhand, 2011 (Act 20 of 2011)", f"Rs {JH_RATE} a day, to Rs {JH_CAP:,} (section 7(1)(b))", f"Lump sum Rs {JH_LUMP_LOW} to Rs {JH_CAP:,} (section 7(1)(a))", "Deducted from the officer&rsquo;s salary", "Official English text of 30 September 2011 (search excerpt)"],
               ["Karnataka, 2011", f"Rs {K_RATE} a day, to Rs {K_CAP} an application", "&ndash;", "Citizen is paid; cost recovered from the official", "Act text read (section 9); the 2026 amendment lets the Schedule set other rates"],
               ["Delhi, 2026", f"Rs {D_RATE} a day, to Rs {D_CAP:,} a case", f"Lump sum Rs {D_RATE} to Rs {D_CAP:,}", "Government treasury", "Act text read (section 8)"],
               ["Delhi, 2011 (repealed on commencement of the 2026 Act)", f"Rs {DELHI2011_COST} an application", "&ndash;", "&ndash;", "PRS 2012 brief, comparison table (secondary)"],
               ["Haryana, 2014 (Act 4 of 2014)", f"Up to Rs {HR_RATE} a day, to Rs {HR_CAP:,} a case (section 9(2))", f"Lump sum Rs {HR_LUMP_LOW} to Rs {HR_CAP:,} (section 9(1))", f"Penalty on the officer; the second authority may award the appellant up to Rs {HR_COMP:,} as compensation (section 9(3))", "Act text read (Haryana gazette of 26 March 2014); the Commission&rsquo;s own power of Rs 20,000 is from a district page, not the Act text"],
               ["West Bengal, 2013 (Act XVII of 2013)", f"Rs {WB_RATE} a day, to Rs {WB_CAP:,} (section 7(1)(b))", f"Lump sum Rs {WB_LUMP_LOW} to Rs {WB_CAP:,} (section 7(1)(a))", "Deducted from salary (state FAQ)", "Act text read (Kolkata Gazette, 27 September 2013); the Commission is optional (section 12)"],
               ["Odisha, 2012 (Act 8 of 2012)", f"Up to Rs {OD_RATE} a day; no aggregate cap in the excerpt (section 8(1)(b))", f"Up to Rs {OD_FAIL_CAP:,} (section 8(1)(a))", "Charged on the officer, appellate authority and staff in the proportion the revisional authority decides (section 8(3))", "Act text read (Odisha Gazette, 1 November 2012; search excerpt)"],
               ["Goa, 2013 (Act 19 of 2013)", f"Rs {GOA_RATE} a day or Rs {GOA_CAP:,}, whichever is less (section 12)", f"Same figures for failure to provide; Rs {GOA_DEFICIENT} for a deficient service; fine of Rs 1,000 to Rs 5,000 on an authority that fails to decide an appeal (section 13)", "Compensation to the eligible person is separate (section 7(f))", "Act text read only from reproductions of the Goa Gazette (search excerpts); section 7 allows a fine or compensation of up to Rs 5,000, which does not match section 12 and was not reconciled"],
               ["Gujarat, 2013 (Act 16 of 2013)", "&ndash;", f"Lump sum Rs {GJ_LUMP_LOW:,} to Rs {GJ_LUMP_HIGH:,} for mala fide action or failure without reasonable cause (section 23(1))", "Recovered from salary; part may be awarded to the appellant, not above the penalty (section 23(2))", "Act text read (Gujarat Gazette, 15 April 2013); no per-day rate is printed"],
               ["Uttar Pradesh, 2011 (Act 3 of 2011)", f"Rs {UP_RATE} a day, to Rs {UP_CAP:,} (section 7(1)(b))", f"Lump sum Rs {UP_LUMP_LOW} to Rs {UP_CAP:,} (section 7(1)(a)); the same range on a first appeal officer who fails to decide in time (section 7(2))", "Compensation to the appellant from the penalty, not above it (section 7(3)); recovered from salary under the 2011 Rules", "Official English translation of 4 March 2011 (India Code and PRS copies); in force from 14 January 2011"],
               ["Himachal Pradesh, 2011 (Act 34 of 2011)", "One lump sum for failure or delay; no per-day rate (section 8(1))", f"Lump sum Rs {HP_LUMP_LOW:,} to Rs {HP_CAP:,} (section 8(1))", "Compensation to the appellant from the penalty, not above it; the officer bears the penalty personally (section 8(2))", "Act text read (India Code and PRS copies); amended by Act 18 of 2019"],
               ["Uttarakhand, 2011 (Act 20 of 2011)", "Rate and cap not visible in the excerpt read (section 9(1)(b))", f"Lump sum Rs {UK_LUMP_LOW} to Rs {UK_CAP:,} (section 9(1)(a))", "Compensation to the appellant from the penalty, not above it (section 9(2))", "Act text read (Uttarakhand portal copy, amended 2014 and 2023); the Commission may be constituted by the State (section 12)"],
               ["Punjab, 2011 (Act 24 of 2011)", f"Rs {PB_RATE} a day, to Rs {PB_CAP:,} (section 9(1)(b))", f"Lump sum Rs {PB_LUMP_LOW} to Rs {PB_CAP:,} (section 9(1)(a))", f"Recovered from salary; the Commission may also impose up to Rs {PB_COMMISSION:,} a case and award compensation from it (section 17(1)(h), added in 2014)", "Act text read (PRS copy and gazette reproductions); Chandigarh uses the same Act since 2017"],
               ["Kerala, 2025 (Act 12 of 2025)", f"Fine Rs {KL_LOW:,} to Rs {KL_HIGH:,} on the officer for failure, delay or a deficient service (section 20(1))", f"Same clause; Rs {KL_APPEAL_LOW:,} to Rs {KL_APPEAL_HIGH:,} on a first appellate authority that delays an appeal (section 20(2))", "&ndash;", "Act text read (PRS copy of the Kerala Gazette); it repealed the Kerala State Right to Service Act, 2012, which had Rs 250 a day up to Rs 5,000 and Rs 500 to Rs 5,000 (Act 18 of 2012, section 8)"],
               ["Assam, 2012 as amended in 2024", f"At least Rs {AS_2024_DAY_MIN} a day of delay, total up to Rs {AS_2024_CAP:,} on a first appellate authority and Rs {AS_SAA_CAP:,} on a second (section 9(1) and (2))", f"The Commission may impose up to Rs {AS_COMM_CAP:,}; Rs {AS_COMM_FAA_LOW} to Rs {AS_2024_CAP:,} on a first appellate authority and Rs {AS_COMM_SAA_LOW:,} to Rs {AS_2024_CAP:,} on a second that delays (section 9(3))", "Paid within 30 days, else recovered from salary (section 10)", f"Ordinance 2 of 2024 (gazette read in full: all three stages) and the Bill of 2024 (as introduced), which agree on every amount; the 2019 text (Rs {AS_2019_RATE} a day, total Rs {AS_2019_CAP:,}, Commission only) and the 2012 Rules (Rs {AS_RULES_RATE} a day, total Rs {AS_RULES_CAP:,}) are superseded or repealed"],
               ["Nagaland, 2026 (Act 11 of 2026), outside the 27", f"Rs {NG_RATE} a day, at most Rs {NG_CAP:,} (section 11(1)(b))", f"Lump sum Rs {NG_LUMP_LOW} to Rs {NG_CAP:,} (section 11(1)(a)); the same range imposed by the second appellate authority on a first appellate authority that delays an appeal (section 11(2))", "Charged on the officer, appellate authority or staff in proportion to responsibility (section 11(3)); disciplinary action may be recommended (section 13)", "Gazette of 13 October 2026 read from page images (PRS copy); assented 30 September 2026; in force on a date to be notified; the Act is a separate, later law and is not one of the 27 names"],
               ["Jammu and Kashmir, 2011 (Act IX of 2011)", f"Rs {JK_RATE} a day or Rs {JK_CAP:,}, whichever is less (section 11(i))", f"Same clause for non-provision; Rs {JK_DEFICIENT:,} for a deficient service; Rs {JK_NONCOMPLY_LOW} to Rs {JK_NONCOMPLY_HIGH:,} for ignoring an appellate order (section 10); Rs 500 to Rs 5,000 on a first appellate authority that delays (section 12)", "Part of the fine may be awarded to the appellant, not above the fine (section 13)", "Act text read (India Code and gazette excerpts); in force from 10 August 2011"],
               ["Ladakh", f"Rs {JK_RATE} a day or Rs {JK_CAP:,}, whichever is less (section 11(i)), as in Jammu and Kashmir", f"Rs {JK_DEFICIENT:,} for a deficient service; Rs {JK_NONCOMPLY_LOW} to Rs {JK_NONCOMPLY_HIGH:,} for ignoring an appellate order (section 10) and on a first appellate authority that delays (section 12)", "&ndash;", "Order S.O. 3775(E) of 23 October 2020 changes only the words Government, State and Gazette, definitions and sections 9 and 15, so the amounts are unchanged; section 11 was read in third-party reproductions of the Jammu and Kashmir Act (secondary), not in the Ladakh copy, whose excerpt stopped at section 4"],
               ["Chandigarh", f"Rs {PB_RATE} a day, to Rs {PB_CAP:,} (Punjab Act section 9(1)(b)), per the 2011 Bill text; a 2017 gazette scan is consistent but badly garbled", f"Lump sum Rs {PB_LUMP_LOW} to Rs {PB_CAP:,} (section 9(1)(a)); the Commission may impose up to Rs {PB_COMMISSION:,} a case (section 17(1)(h), added in 2014)", "Penalty is recovered from salary (Rule 12 of the 2019 Rules)", "Punjab Act extended by Ministry of Home Affairs G.S.R. 1015(E) of 14 August 2017; the modifications read (name of the State, the Administrator, the Commission and its senior officer) leave section 9 unchanged; the Commission imposed Rs 10,000 on a designated officer in an order of 2023"]]),    "A citizen in Karnataka or Chhattisgarh is paid for a delay and a citizen in Delhi is not, while 28 laws print a per-case cap between Rs 500 and Rs 10,000, and Assam allows Rs 5,000, Rs 7,000 and Rs 10,000 at three stages.",
    "Each state should print the delay rate, the cap and the payee in the Schedule entry for each service so that a rule change is visible to applicants.",
    "money")

s2 = insight(
    H("Second-stage appeal windows: 60 days in eleven states and UTs, 30 days in nine"),
    bars(H("Eleven laws allow 60 days for the second step; nine allow 30"),
         [("60 days: " + ", ".join(SIXTY), 60), ("30 days: " + ", ".join(THIRTY), 30)],
         accent="30 days: " + ", ".join(THIRTY), unit=" days", vmax=70,
         sub="Days allowed to take the step after the first one, as printed in each Act. In Meghalaya the second step is the Commission, in Delhi the first appeal is automatic, and in Maharashtra a third appeal to the Commission has 60 days. Goa, Chhattisgarh, Gujarat, Sikkim and Lakshadweep are not shown because the second window was not read or does not exist.",
         source="Sections 6 to 9 of each Act (Madhya Pradesh, Rajasthan, Bihar, Karnataka, Haryana, West Bengal, Jharkhand, Odisha, Uttar Pradesh, Himachal Pradesh, Uttarakhand, Punjab, Jammu and Kashmir, Assam, Meghalaya, Maharashtra, Arunachal Pradesh, Delhi), PRS copies, gazettes and search excerpts.")
    + numbers(["State", "First stage", "Second stage", "Basis"],
              [["Madhya Pradesh", f"First appeal officer, {MP_FIRST_DAYS} days", f"Second appellate authority, {MP_SECOND_DAYS} days; revision to an officer the State nominates, {MP_REVISION_DAYS} days", "Act sections 6 and 8 (page scan)"],
               ["Bihar", "Appellate authority, 30 days", "Reviewing authority, 60 days", "Act sections 6(1) and 6(3)"],
               ["Rajasthan", f"First appeal officer, {RJ_FIRST_DAYS} days", f"Second appellate authority, {RJ_SECOND_DAYS} days; revision, {RJ_REVISION_DAYS} days, to a nominated officer in 2011 and to the Commission after the 2013 amendment", "Act sections 6 and 8 (page scan); 2013 amendment"],
               ["Karnataka", "Competent officer, 30 days", "Appellate authority, 60 days", "Act sections 13(1) and 13(3)"],
               ["Haryana", "First grievance redressal authority, 30 days; decided within 30 days", "Second grievance redressal authority, 60 days; decided within 60 days as far as possible", "Act sections 6 and 7"],
               ["West Bengal", "Appellate officer, 30 days", "Reviewing officer, 60 days; revision of a penalty to a nominated officer, 60 days", "Act sections 6 and 8"],
               ["Jharkhand", "First appeal officer, 30 days", "Second appellate authority, 60 days", "Act section 6"],
               ["Odisha", "Appellate authority, 30 days, decided within 30 days", "Revisional authority, 30 days", "Act sections 5 and 6"],
               ["Goa", "Appellate authority, 30 days, decided within 45 days", "None seen in the sections read", "Act section 6"],
               ["Gujarat", "Complaint to a grievance redressal officer, then appeal to the designated authority within 30 days", "State Appellate Authority; the window was not read", "Act and Rules 2014 (search excerpts)"],
               ["Uttar Pradesh", "First appeal officer, 30 days", "Second appellate authority, 60 days; revision of a penalty to a nominated officer, 60 days", "Act sections 6 and 8"],
               ["Himachal Pradesh", "First appellate authority, 30 days; decided within 30 days, extendable to 45", "Second appellate authority, 60 days", "Act sections 6 and 7"],
               ["Uttarakhand", "First appellate authority, 30 days", "Second appellate authority, 30 days; revision to the Commission or a nominated officer, 60 days", "Act sections 6, 7 and 10 (section 7 as substituted in 2023)"],
               ["Punjab", "First appellate authority, 30 days", "Second appellate authority, 30 days; revision to the Commission or a nominated officer, 60 days", "Act sections 6, 7 and 10"],
               ["Kerala (2025)", "Appellate authorities as in the 2025 Act; windows not read", "Revision to the Commission within 60 days, per a news report (secondary); a single-member Commission is to be set up", "Act section 20 read; windows from Onmanorama, 5 November 2025"],
               ["Jammu and Kashmir", "First appellate authority, 30 days; decided within 45 days", "Second appellate authority, 60 days; decided within 45 days", "Act section 7 and a 2011 circular"],
               ["Assam", "First appellate authority, window not seen in the excerpt; decided within 45 days or an extended period", f"Second appellate authority (head of the department), {AS_APPEAL_2} days; then a third appeal to the Commission, {AS_APPEAL_3} days; decision binding", "Ordinance 2 of 2024 (gazette) and the Bill passed in August 2024; the enacted Act XXII of 2024 could not be read"],
               ["Nagaland", f"First appellate authority, 30 days (up to 60 with cause); decided within 30 days (section 8)", f"Second appellate authority, {NG_APPEAL} days (up to 60 with cause); decided within 30 days; revision to an officer the State Government nominates within {NG_REVISION} days (sections 9 and 12)", "Act sections 8, 9 and 12 (gazette page images)"],
               ["Meghalaya", "Appellate authority, 30 days", "Commission, 30 days (up to 60 with cause); decided within 30 days", "Act sections 6 and 7"],
               ["Maharashtra", "First appellate authority, 30 days (up to 90 with cause); decided within 30 days", "Second appellate authority, 30 days; decided within 45 days; third appeal to the Commission, 60 days", "Act sections 9 and 18"],
               ["Arunachal Pradesh", "First appellate authority; window not visible in the excerpt", "Second appellate authority, 30 days (up to 60 with cause)", "Act section 8"],
               ["Sikkim", "Appellate authority, 20 working days, with admission after later dates in exceptional cases; a Commission of up to three members", "Not read", "Act section 8 (partial excerpt)"],
               ["Chhattisgarh", "Appeal to the appellate authority against the competent officer&rsquo;s order, 30 days; decided within 45 days; the order is final", "None", "Act section 7"],
               ["Mizoram", "First appellate authority, 30 days, up to 60 with sufficient cause; decided within 30 days (section 8)", "Second appellate authority, 30 days, up to 60 with sufficient cause, by the officer or the applicant; decided within 30 days (section 9)", "Act sections 8 and 9 (public copy of the Gazette)"],
               ["Lakshadweep", "Complaint to a grievance redressal officer, appeal to the designated authority, then a Union Territory Appellate Authority; windows not read", "&ndash;", "Regulation 2 of 2022, sections 9 and 12"],
               ["Delhi (2026)", "Citizen Grievance Redressal Authority, appeal lodged automatically on a missed deadline", "Commission, 30 days", "Act sections 7 and 9"]]),
    "Eleven laws give 60 days for the second step and nine give 30 days, while Goa and Chhattisgarh have a single appeal and Gujarat and Lakshadweep begin with a complaint to a grievance officer.",
    "A citizen who is refused should note the date of the rejection or of the missed deadline, because the first window runs from that date in most of the Acts read.",
    "appeals")

s3 = insight(
    H(f"Sources name {len(NAMED)} states and UTs against {REPORTED} reported; {len(TIER_A)} have a penalty clause read"),
    bars(H(f"{len(NAMED)} names found against the {REPORTED} reported by the Government of India"),
         [("Act text with penalty clause read (tier A)", len(TIER_A)),
          ("All names found (computed)", len(NAMED)),
          ("Reported to Parliament, 2025", REPORTED)],
         accent="Reported to Parliament, 2025", unit="", vmax=30,
         sub=f"States and union territories. The names exceed the reported count by {OVER}. No source read lists the 22, so which names the Government of India counts is not known.",
         source="PIB and Lok Sabha answers, 2025; the Acts, gazettes and commission pages named in the sources. Totals computed here.")
    + numbers(["Tier", "States and UTs", "Basis"],
              [["A: Madhya Pradesh, Rajasthan, Bihar, Karnataka, Delhi, Jharkhand, Haryana, West Bengal, Gujarat, Odisha, Goa, Uttar Pradesh, Himachal Pradesh, Uttarakhand, Punjab, Kerala, Jammu and Kashmir, Assam, Meghalaya, Sikkim, Arunachal Pradesh, Lakshadweep, Chhattisgarh, Maharashtra, Mizoram, Chandigarh, Ladakh", f"{len(TIER_A)}", "Act or Regulation text read, including a penalty clause; Madhya Pradesh and Rajasthan from page scans, Goa from reproductions of its Gazette, Sikkim and Mizoram in part, Chandigarh and Ladakh through extended or adapted Acts, the others as English text or search excerpts; Delhi is the 2026 Act, Kerala the 2025 Act that repealed the 2012 Act, Lakshadweep a President&rsquo;s Regulation, and Assam has conflicting versions"],
               ["All names", f"{len(NAMED)}", "Computed; Delhi counted once although its 2011 law is replaced by Act 10 of 2026"],
               ["Reported", f"{REPORTED}", "PIB Rajya Sabha reply and Lok Sabha question 4216 (answered 26 March 2025): enacted by 22 States and Union Territories, Commissions in 8; no list printed"],
               ["Names above the reported count", f"{OVER}", "Computed"]]),
    f"Every one of the {len(NAMED)} names has an Act, gazette or commission page behind it, so the Government of India&rsquo;s 22 is an older or narrower count and the five or more names it leaves out cannot be identified.",
    "The Department of Administrative Reforms and Public Grievances should publish the list of 22 with each Act, its year and whether it is in force, and say how Union Territory Regulations are counted.",
    "count")

s4 = insight(
    H(f"Disposal counters: Karnataka {KA_DISPOSAL}%, Delhi {DL_IN_TIME}% in time, none found elsewhere"),
    bars(H("Karnataka and Delhi publish a counter; none found for Madhya Pradesh, Bihar, Rajasthan"),
         [("Karnataka: share of receipts with a recorded disposal", KA_DISPOSAL),
          ("Delhi: share of applications disposed in time", DL_IN_TIME),
          ("Madhya Pradesh", None), ("Bihar", None), ("Rajasthan", None)],
         accent="Delhi: share of applications disposed in time", unit="%", vmax=100,
         sub="Per cent. The two counters measure different things: Karnataka counts any recorded disposal and Delhi counts disposal in time. Both are undated portal figures read from search excerpts. A dashed bar means no figure was found.",
         source="Sakala portal and Delhi e-SLA dashboard (search excerpts, 21 November 2026), as used in the Karnataka and Delhi posts.")
    + numbers(["State", "Counter found", "What it counts"],
              [["Karnataka", "99.82% of 432,426,014 receipts have a recorded disposal", "Disposal of any kind; no timeliness split"],
               ["Delhi", "65.02% of over 36 lakh applications disposed in time", "The e-SLA system of the 2011 law; definition of in time not read"],
               ["Madhya Pradesh, Bihar, Rajasthan", "None found", "No pending or disposal figure was found in any source read"]]),
    "A disposal rate and an in-time rate cannot be compared across states, and states with no published counter cannot be assessed at all.",
    "Each state should publish applications received, delivered in time, delivered late, rejected and pending, by service, on a stated date.",
    "counters")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>State right-to-service commissions:</b> publish an annual report with applications received, delivered in time, late, rejected and pending, by department.</li>
<li><b>State governments:</b> print the delay rate, the cap and the payee beside each service in the Schedule.</li>
<li><b>Department of Administrative Reforms and Public Grievances, Government of India:</b> keep one dated list of the states and union territories with a right-to-service law, with the Act, its year and whether it is in force.</li>
<li><b>PRS Legislative Research and state legislative departments:</b> post searchable text of the Acts, since the Madhya Pradesh and Rajasthan files are page scans.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Who is covered, and what is counted</summary>
<ul>
<li><b>Delhi 2026:</b> substantive government servants and employees of local bodies and authorities the Government owns, controls or substantially finances; casual, daily-wage and (unless the contract says otherwise) contract staff are excluded; only services in the Schedule are covered (section 1(4) and (5)).</li>
<li><b>Karnataka:</b> services in the Schedule, with the penalty falling on the designated officer or the subordinate who defaults; nothing applies where the Government has banned or restricted the service (section 9).</li>
<li><b>Madhya Pradesh and Rajasthan:</b> services, designated officers, first appeal officers, second appellate authorities and time limits notified by the State Government under section 3 of each Act; Rajasthan&rsquo;s Act defines a public authority to include bodies owned, controlled or substantially financed by the State.</li>
<li><b>Haryana, West Bengal, Jharkhand, Odisha, Goa and Gujarat:</b> each Act applies to services notified by its State Government. Gujarat&rsquo;s begins with a complaint to a grievance redressal officer and a penalty for mala fide action; Goa&rsquo;s defines an authority to include non-governmental bodies that received a government grant of Rs 5 lakh or more; West Bengal&rsquo;s Commission is created only if the State considers it necessary.</li>
<li><b>Bihar:</b> services, designated public servants and appellate authorities notified by the Government under section 3; the penalty may be charged to the designated public servant, the appellate authority or staff (section 7(3)).</li>
<li><b>What is counted as a law:</b> the 2012 PRS table counts Acts and, for Madhya Pradesh, a Vidheyak (Bill) of 2010; the 2025 PRS review counts Bills passed and an Ordinance; the Wikipedia table mixes Acts, Bills and a 2015 Maharashtra Ordinance. This piece counts a state or union territory once whatever the number of its laws, counts a Regulation made by the President for Lakshadweep as a law, and does not know how the PIB count treats Bills, Ordinances or Regulations.</li>
<li><b>Stipulated time limits:</b> each Act fixes limits in a Schedule or notification, which this piece did not read for any state.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>Which 22. Two 2025 answers to Parliament (Rajya Sabha reply, PIB release dated 3 April 2025, and Lok Sabha unstarred question 4216 answered 26 March 2025) say the Right to Service Act has been enacted by 22 States and Union Territories, with Commissions in eight, and print no list. The names found reach 27, so at least five are left out, and which five was not established. The eight Commission names the answer prints (Assam, Chandigarh, Maharashtra, Punjab, Haryana, Meghalaya, Uttarakhand, West Bengal) must all be inside the 22, so the five left out come from the other 19 names, which narrows the question but does not answer it. The only list found that totals exactly 22 is a 2019 table by the Centre for Budget and Governance Accountability (22 states marked as having a law), which marks Meghalaya as having none and does not list Chandigarh, Ladakh or Lakshadweep, so it cannot be the list behind the 2025 answer. A 2022 scoping study by SAFAR marks 24 states with a law (it counts Andhra Pradesh and Meghalaya, and not Sikkim). A February 2024 DARPG annual report carries a chart titled Status of RTS Act across States/UTs whose extracted text shows only the numbers 7, 23 and 6; if those are counts of 36 States and UTs they would imply 30 with an Act, but the chart image could not be viewed and the numbers are unconfirmed. DARPG&rsquo;s own monthly NeSDA reports (2024 to 2026) discuss Right to Service Commissions in Haryana, Bihar, Assam, Meghalaya and Chandigarh but print no list of the 22, and the DARPG pages that should hold one returned no text. A journal article from the National Law University Assam lists Telangana (2016) and Tamil Nadu (2019) among states with an Act; the next bullet explains why neither is counted. The reason may be an older count, a different treatment of Union Territory Regulations, or both; no source says. Every one of the 27 has an Act, a gazette, an official commission page or an official press note behind it, so the shortfall is in the count, not in the evidence for a law.</li>
<li>Names not counted among the 27. The Andaman and Nicobar Islands (Right to Public Services) Regulation, 2026 appears only as a draft with a blank number, dated July 2026. One law journal lists a Telangana Right to Services Act, 2016 and a Tamil Nadu Public Services Guarantee Act, 2019, but its footnotes point to a petition and a newspaper piece asking for such a law, and no Act was found for either. For Telangana, a Deccan Chronicle report of 1 August 2022 says the Act is still on paper, a South First list of August 2025 names the Right to Public Services Act among the Congress government&rsquo;s unkept promises, and a V6 Velugu piece of 31 October 2026 still urges one. For Tamil Nadu, a Times of India piece of November 2022 and a Hindustan Times report of September 2021 describe a promised law, and a DT Next column of 2 November 2026 says the State Budget 2026 commits to introducing one and that the state is preparing to draft it. Neither state is counted, and both stay open to a primary-source check of their legislature lists. Nagaland is a different case: the Nagaland Right to Public Services Act, 2026 (Act 11 of 2026) was passed on 3 September 2026 and published in the Nagaland Gazette of 13 October 2026 (PRS copy, text not extractable); the Act text was read from page images of the PRS copy (sections 1 to 18, including the penalty clause in section 11), and it comes into force on a date to be notified. It post-dates the 2025 answers to Parliament, so it is not one of the 27 names and cannot be among the five the count of 22 leaves out; it is counted in the cap totals. The Act text has not been checked against the Nagaland government&rsquo;s own copy. No rules, no commencement notification and no list of notified services were found on 21 November 2026 in news reports, the Department of Information and Public Relations pages or the state portal&rsquo;s Act and Rules page, so the time limits, designated officers and appellate authorities are not yet set and the Act may not yet be in force. A customer-care website describes a Nagaland Right to Service Act, 2012; no Act of that name was found anywhere else, so it is not used.</li>
<li>The six Acts of Haryana, West Bengal, Gujarat, Goa, Jharkhand and Odisha were read as English text in search excerpts of the official gazettes and department pages, not as full documents. The Goa Act was read only from reproductions of its Gazette on commercial and open-data sites, and a Bill on the Goa Government site, so its clauses should be checked against the Goa Gazette; its section 7 (fine or compensation up to Rs 5,000) and section 12 (Rs 50 a day up to Rs 2,500) were not reconciled. Odisha&rsquo;s section 8 prints no aggregate cap for the delay penalty in the excerpt. Haryana&rsquo;s Commission penalty of Rs 20,000 and compensation of Rs 5,000 come from a district page. The Gujarat Act has no per-day rate, and a slide of its Administrative Reforms and Training Division says it was implemented from 1 April 2016 after staged commencement.</li>
<li>The five Acts of Uttar Pradesh, Himachal Pradesh, Uttarakhand, Punjab and Kerala were read as English text in search excerpts of official copies, not as full documents. Uttarakhand&rsquo;s delay-penalty rate and cap were cut off in the excerpt, so only its lump sum of Rs 500 to Rs 5,000 is stated; its Act was amended in 2014 and 2023, and the second-appeal window is the 2023 text. Himachal Pradesh prints one lump sum for failure or delay and no per-day rate. The Punjab Commission&rsquo;s power of Rs 10,000 a case comes from the 2014 amendment as reproduced on a Chandigarh Housing Board site. Kerala&rsquo;s Rs 15,000 fine falls on a first appellate authority, not on the officer.</li>
<li>The eleven laws read last (Jammu and Kashmir, Assam, Meghalaya, Sikkim, Arunachal Pradesh, Lakshadweep, Chhattisgarh, Maharashtra and Mizoram, with Chandigarh and Ladakh read through the Punjab and Jammu and Kashmir Acts they use) were read as English text in search excerpts of official copies. Assam&rsquo;s section 9 has been rewritten three times: the 2019 text (Commission only, Rs 250 a day, total Rs 25,000, which no Commission could apply until one was set up), Ordinance 2 of 2024 (first appellate authority at least Rs 100 a day up to Rs 5,000, second up to Rs 7,000) and the Bill passed on 30 August 2024, which became Assam Act XXII of 2024 on assent on 25 September 2024 and was said to repeal the Ordinance. The gazette copy of Act XXII has no readable text layer (its fonts do not extract), so the in-force wording is taken from the gazette text of Ordinance 2 of 2024, read in full, and the Bill as introduced; the two agree on every rupee amount (Rs 5,000, Rs 7,000 and Rs 10,000 as totals, Rs 500 to Rs 5,000 and Rs 1,000 to Rs 5,000 for appellate authorities that delay), but the Bill words some limits without the phrase per day, and the enacted Act may differ from both. The enacted Act was not read. Later 2025 amendments (Ordinance II and Act II of 2025) change only section 8B on Commissioners&rsquo; tenure. The Assam Right to Public Services Rules, 2026 (5 August 2026) repeal the 2012 Rules, whose Rs 50 a day and Rs 2,000 figures therefore no longer apply, and refer to penalties imposed by appellate authorities under section 9, which fits the 2024 structure. A state portal page also cites the 2024 Amendment Act as the current law. Meghalaya&rsquo;s Act says up to Rs 20,000 for repeated instances while the Commission&rsquo;s slides say Rs 25,000; the Act text is used. Sikkim&rsquo;s base penalty clause was cut off in the excerpt. Arunachal Pradesh&rsquo;s first-appeal window was not visible. Chandigarh&rsquo;s section 9 amounts come from the Punjab Bill of 2011 as introduced, because the enacted text was not read there; the 2017 Chandigarh Gazette scan is consistent with it but too garbled to quote, and later Punjab amendments were not checked. Ladakh&rsquo;s section 11 was read in third-party reproductions of the Jammu and Kashmir Act, not in the Ladakh copy. Lakshadweep&rsquo;s Regulation was amended by Regulation 15 of 2026, which was only partly read. Chhattisgarh&rsquo;s section 4(4) is a cost payable to the applicant, not a penalty to the treasury. Chandigarh&rsquo;s Punjab Act was extended with &lsquo;some minor modifications&rsquo; that were not read, and Ladakh&rsquo;s adapted Jammu and Kashmir text did not show its penalty clause. Mizoram&rsquo;s Act was read only from sections 1 to 11(1)(a) in a public Scribd copy of the Mizoram Gazette, because the Mizoram government site refused automated requests (HTTP 403) and was not retried; the delay rate and the rest of section 11 come from an official press note in the Mizo language and a 2015 news report. The Gazette of 20 April 2015 publishes the Act, section 1(3) leaves commencement to a notification, and the press note and the news report give 1 December 2015; a state department slide that says the Act came into force on 20 April 2015 appears to give the publication date.</li>
<li>Date conflicts. The fetched PIB page carries a date of 3 April 2025, while Wikipedia cites a PIB release of 22 June 2025 for the same count. Wikipedia gives Bihar&rsquo;s enactment as 25 July 2011 and a Kerala Calling article as 25 July 2012; the Act itself is titled 2011. Kerala&rsquo;s Act 18 of 2012 was repealed by the Kerala Right to Public Service Act, 2025 (Act 12 of 2025, PRS copy of the digitally signed Gazette, with a news report of 5 November 2025 saying it was notified); PRS ARSL 2025 lists the measure as a Bill, and the 2025 Act&rsquo;s appeal windows and Commission were not read.</li>
<li>Machine-readable text of the Madhya Pradesh and Rajasthan Acts. The PRS PDFs are page scans with no text layer, so sections 6 to 8 of each were read by viewing the page images. The Madhya Pradesh amendments (Acts 22 of 2011 and 5 of 2012, and later amendments listed in PRS reviews) and the rest of the Rajasthan Act were not read for changes to the penalty.</li>
<li>Bihar&rsquo;s rupee amounts come from rule 8 of the Bihar Right to Public Services Rules, 2011 (Rs 250 a day, total at most Rs 5,000; lump sums of Rs 500 to Rs 5,000), read in English and Hindi copies that agree on a third-party site and in a legal-database copy; the gazette itself and any amendment to the Rules after 2011 were not seen, because the Act leaves the rates to rules that can be changed by notification. A 2015 student article puts the penalty at Rs 500 a day, which conflicts with the Rules and is not used.</li>
<li>The Rajasthan Right to Hearing Act, 2012 is a different Act from the Rajasthan Guaranteed Delivery of Public Services Act, 2011; a search excerpt about a Rs 500 to Rs 5,000 fine on a Public Hearing Officer relates to the former and is not used here.</li>
<li>Pending applications: no pending or disposal figure was found for any of the states beyond Karnataka and Delhi, and none is given.</li>
<li>Whether each law is in force today, which Schedules exist, and how many services each state has notified (other than the Karnataka and Delhi counters in the single-state posts).</li>
<li>The 2012 PRS brief is used only for the Delhi 2011 cost of Rs 10 an application; amendments after the dates of the texts read may have changed any figure, and amendments to the Madhya Pradesh Act (Acts 22 of 2011 and 5 of 2012 and later) were not read.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + s4 + fixes + method + gaps

SOURCES = (
    '<a href="https://prsindia.org/files/legislature/ARSL_2025.pdf">PRS Legislative Research, Annual Review of State Laws 2025</a> (primary report; no count of right-to-service laws); '
    '<a href="https://prsindia.org/files/bills_acts/bills_parliament/2011/Legislative_Brief_Citizens_Charter_27_Sep.pdf">PRS Legislative Brief, Citizens Charter Bill, 2011, 27 September 2012</a> (named report; comparison table of the 2011 state laws); '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/delhi/2026/Act10of2026DL.pdf">Delhi Act 10 of 2026, PRS copy</a>; '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/karnataka/2012/2012KA1.pdf">Karnataka Sakaala Services Act, PRS compilation</a>; '
    '<a href="https://csharyana.gov.in/WriteReadData/Act/Administrative%20Reforms/4297.pdf">Haryana Right to Service Act, 2014 (Haryana Act 4 of 2014), Haryana gazette</a>; '
    '<a href="https://udma.wb.gov.in/public/uploads/act_rules_pdf/pdfs_wbrtps_act_2013.pdf">West Bengal Right to Public Services Act, 2013, Kolkata Gazette</a>; '
    '<a href="https://gidc.gujarat.gov.in/pdf/act-and-rules/RCPS-Act-2013.pdf">Gujarat (Right of Citizens to Public Services) Act, 2013, Gujarat Gazette</a> and '
    '<a href="https://indiankanoon.org/doc/4339031/">Indian Kanoon reproduction, section 23</a> (secondary); '
    '<a href="https://openacts.in/pdf/Goa/Goa%20%28Right%20of%20Citizens%20to%20Time-Bound%20Delivery%20of%20Public%20Services%29%20Act%2C%202013.pdf?v=253989">Goa Act 19 of 2013, reproduction of the Goa Gazette</a> (secondary) and '
    '<a href="https://www.goa.gov.in/wp-content/uploads/2016/05/The-Goa-Right-of-Citizen-Amendment-2013.pdf">Goa Government copy of the 2013 Bill</a>; '
    '<a href="https://dop.jharkhand.gov.in/download.aspx?id=840&amp;sub=Jharkhand%20Rajya%20Sewa%20Dene%20Ki%20Garantee%20Act-%202011">Jharkhand Rajya Sewa Dene ki Guarantee Act, 2011, Jharkhand government</a>; '
    '<a href="https://serviceonline.gov.in/resources/pdf/Odisha_Act.pdf">Odisha Right to Public Services Act, 2012</a> (Odisha Gazette, 1 November 2012); '
    '<a href="https://panchkula.nic.in/right-to-service-act/">Panchkula district page on the Haryana Act</a> (official summary: Commission powers); '
    '<a href="https://upload.indiacode.nic.in/showfile?actid=AC_UP_88_1433_00001_00001_1595583848599&amp;filename=janhit_final_act.pdf&amp;type=actfile">Uttar Pradesh Janhit Guarantee Adhiniyam, 2011, India Code</a>; '
    '<a href="https://www.indiacode.nic.in/bitstream/123456789/21978/1/the_himachal_pradesh_public_services_guarantee_act%2C_2011.pdf">Himachal Pradesh Public Services Guarantee Act, 2011, India Code</a>; '
    '<a href="https://cdnbbsr.s3waas.gov.in/s3bc7f621451b4f5df308a8e098112185d/uploads/2025/03/20250325159522727.pdf">Uttarakhand Right to Service Act, 2011 as amended (Uttarakhand portal)</a>; '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/punjab/2011/2011PB24.pdf">Punjab Right to Service Act, 2011, PRS copy</a> and '
    '<a href="https://chbonline.in/wp-content/uploads/2021/01/Right-to-service-act.pdf">2014 amendment as reproduced by the Chandigarh Housing Board</a> (secondary); '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/kerala/2025/Act12of2025KL.pdf">Kerala Right to Public Service Act, 2025 (Act 12 of 2025), PRS copy</a>, '
    '<a href="https://employment.kerala.gov.in/wp-content/uploads/2022/08/RIGHT-TO-SERVICE-ACT-GAZETTE.pdf">Kerala State Right to Service Act, 2012 (Act 18 of 2012)</a> and '
    '<a href="https://www.onmanorama.com/news/kerala/2025/11/05/public-service-delivery-via-electronic-mode.html">Onmanorama, 5 November 2025</a> (secondary); '
    '<a href="https://www.indiacode.nic.in/bitstream/123456789/16498/1/public_services_guarantee_act%2C_2011.pdf">Jammu and Kashmir Public Services Guarantee Act, 2011, India Code</a> and <a href="https://jkgad.nic.in/PDF/Circulars.pdf">2011 General Administration Department circular</a>; '
    '<a href="https://www.indiacode.nic.in/bitstream/123456789/15699/1/the_assam_right_to_public_services_act,_2012__1_.pdf">Assam Right to Public Services Act, 2012 (India Code text)</a>, '
    '<a href="https://art.assam.gov.in/sites/default/files/swf_utility_folder/departments/anrt_webcomindia_org_oid_3/menu/document/ARTPS%20RULES.pdf">Assam Rules, 2012</a> and '
    '<a href="https://prsindia.org/files/bills_acts/bills_states/assam/2024/Ord2of2024AS.pdf">Assam Ordinance 2 of 2024</a>, <a href="https://www.assambidhansabha.org/assets/uploads/bills/en/En_FVNVC1724770127.pdf">Assam Right to Public Services (Amendment) Bill, 2024 (Assam Legislative Assembly)</a>, <a href="https://legislative.assam.gov.in/sites/default/files/swf_utility_folder/departments/legislative_medhassu_in_oid_3/menu/document/the_assam_right_to_public_servicesamendment_act_2024_assam_act_no.xxii_of_2024.pdf">Assam Act XXII of 2024 (gazette copy, text not extractable)</a>, <a href="https://legislative.assam.gov.in/sites/default/files/swf_utility_folder/departments/legislative_medhassu_in_oid_3/menu/document/the_assam_right_to_public_services_amendment_act_2025_assam_act_no.ii_of_2025.pdf">Assam Act II of 2025</a> and <a href="https://art.assam.gov.in/sites/default/files/swf_utility_folder/departments/anrt_webcomindia_org_oid_3/menu/document/doc-20260810-wa0000.pdf">Assam Right to Public Services Rules, 2026</a> (primary; search excerpts); '
    '<a href="https://www.meghalaya.gov.in/sites/default/files/acts/LL_B_55_2013_50.pdf">Meghalaya Act 18 of 2020 (Meghalaya government copy)</a> and '
    '<a href="https://mspsdc.meghalaya.gov.in/viewpresentation.htm?presentationid=7">Meghalaya Commission presentation</a> (state document; Rs 25,000 figure); '
    '<a href="https://www.indiacode.nic.in/bitstream/123456789/12585/1/1575018164562_chhattisgarh_lok_seva_guarantee_act_2011_no._23_of_2011_date_30.09.2011.pdf">Chhattisgarh Lok Sewa Guarantee Act, 2011, India Code</a>; '
    '<a href="https://dpar.mizoram.gov.in/uploads/attachments/eb9e73bf448c090afed60a49d0c130d9/posts-129-press-note-on-mrtps-act-2015-for-the-meet-the-press-programme-on-01022019.pdf">Mizoram DPAR press note, 1 February 2019</a> (official, Mizo language), '
    '<a href="https://www.scribd.com/document/832503994/pages-48-the-mizoram-right-to-public-services-act-2015-1">Mizoram Gazette Ex-156/2015 (Act 6 of 2015), public Scribd copy</a> (reproduction of the official Gazette; preview to section 11(1)(a)) and '
    '<a href="https://assamtribune.com/right-to-public-services-act-comes-into-force">Assam Tribune report</a> (secondary); '
    '<a href="https://www.indiacode.nic.in/bitstream/123456789/19708/1/201531.pdf">Maharashtra Right to Public Services Act, 2015, India Code</a> and '
    '<a href="https://home.maharashtra.gov.in/en/maharashtra-right-to-public-services-act-2015">Maharashtra Home Department page</a>; '
    '<a href="https://egazette.gov.in/WriteReadData/2026/276610.pdf">Lakshadweep Amendment Regulation, 2026 (Gazette of India)</a>; '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/bihar/2011/2011Bihar4.pdf">The Bihar Right to Public Services Act, 2011, PRS copy</a> and <a href="https://www.indianemployees.com/acts-rules/details/bihar-right-to-public-services-rules-2011">Bihar Right to Public Services Rules, 2011 (English copy)</a>, <a href="https://www.indianemployees.com/acts-rules/details/bihar-public-services-rights-rules-2011">Hindi copy</a> and <a href="https://www.legitquest.com/act/bihar-right-to-public-services-rules-2011/76BD">legal-database copy</a> (secondary); '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/rajasthan/2011/2011Rajasthan23.pdf">The Rajasthan Guaranteed Delivery of Public Services Act, 2011 with the 2013 amendment, PRS copy</a> (page scan; amendment has a text layer); '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/madhya-pradesh/2010/2010MP24.pdf">Madhya Pradesh Lok Sewaon ke Pradan ki Guarantee Adhiniyam, 2010, PRS copy</a> (page scan); '
    '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2118276">PIB, Parliament question on Sevottam and redressal of public grievances</a> (primary; 22 states and UTs, eight Commissions); '
    '<a href="https://sansad.in/getFile/loksabhaquestions/annex/184/AU4216_YkZmPz.pdf?source=pqals">Lok Sabha unstarred question 4216, answered 26 March 2025</a> (primary; same 22 and eight Commissions); '
    '<a href="https://meghalaya.gov.in/sites/default/files/acts/LL_B_55_2013_50.pdf">Meghalaya Right to Public Services Act, 2020</a> (primary Gazette; read as a search excerpt); '
    '<a href="https://www.sikkim.gov.in/uploads/Gazette/363_20240720.pdf">Sikkim Gazette, Act 15 of 2022</a> and '
    '<a href="https://eodb.arunachal.gov.in/uploads/policyguideline_documents/f6f6fd30f1ebb16e359805e98781cfd9.pdf">Arunachal Pradesh Gazette, Act 3 of 2016</a> (primary; search excerpts); '
    '<a href="http://rtsc.chd.gov.in/">Chandigarh Right to Service Commission</a> (primary; Punjab Act extended in 2017); '
    '<a href="https://www.cbgaindia.org/wp-content/uploads/2019/06/Have-the-Public-Service-Delivery-Laws-Actually-Delivered.pdf">CBGA, Have Public Service Delivery Laws Actually Delivered? (2019)</a>, <a href="https://safar-india.org/documents/RTPSD_Final.pdf">SAFAR scoping study (2022)</a> and <a href="https://it.delhi.gov.in/sites/default/files/IT/generic_multiple_files/nwf_annual_report.pdf">DARPG NeSDA Way Forward annual report (2024)</a> (secondary; state-by-state tables used only to test the count of 22); '
    '<a href="https://prsindia.org/files/bills_acts/acts_states/nagaland/2026/Act11of2026NG.pdf">Nagaland Right to Public Services Act, 2026 (PRS copy of the gazette, read from page images)</a>, <a href="https://www.easternmirrornagaland.com/government-service-delays-could-cost-officials-inr-250-a-day-in-nagaland">Eastern Mirror</a> and <a href="https://morungexpress.com/time-bound-services-vs-rs-5000-penalty-cap-will-nagalands-bill-deliver">Morung Express</a> (secondary, agree with the Act); <a href="https://www.deccanchronicle.com/nation/current-affairs/010822/right-to-services-act-still-on-paper-in-ts.html">Deccan Chronicle on Telangana</a>, <a href="https://www.dtnext.in/news/tamilnadu/from-promise-to-performance-how-to-make-right-to-services-act-work">DT Next on Tamil Nadu</a> (secondary); '
    '<a href="https://chdctu.gov.in/files/documents/CRSC_Rules.pdf">Chandigarh Right to Service Rules, 2019</a>, <a href="https://rtsc.chd.gov.in/uploads/20250603212622_petition_76-2023-14112023.pdf">Commission order, 2023</a> and <a href="https://mha.php-staging.com/files/notice_document/Punjab_right_24082017.PDF">G.S.R. 1015(E) copy</a> (primary; search excerpts), with <a href="http://amritsarcorp.com/RTS_Service_Act.pdf">Punjab Right to Service Bill, 2011</a> (secondary; as introduced); '
    '<a href="https://lawgist.in/states/jammu-and-kashmir/jammu-and-kashmir-public-services-guarantee-act-2011/11">Jammu and Kashmir Act section 11</a> and <a href="https://igr.jk.gov.in/files/J%26K%20Reorganisation%20Act%2C%202019.pdf">S.O. 3775(E) as printed with the Reorganisation Act</a> (secondary for section 11; the order is primary); '
    '<a href="https://eodb.ladakh.gov.in/storage/uploads/incentives/20260514225404_6a060534d66f9.pdf">Ladakh text of the Public Services Guarantee Act, 2011</a> and '
    '<a href="https://thc.nic.in/Central%20Governmental%20Regulations/Lakshadweep%20(Right%20To%20Public%20Services)%20Regulation,%202022.pdf">Lakshadweep (Right to Public Services) Regulation, 2022</a> (primary; search excerpts); '
    '<a href="https://egazette.servantsofknowledge.in/details/in.gazette.chhattisgarh.eo.2026-06-19.334">Chhattisgarh Gazette, 19 June 2026</a>, '
    '<a href="https://dpar.mizoram.gov.in/page/mizoram-right-to-public-services-act-2015">Mizoram Department of Personnel and Administrative Reforms page</a> and '
    '<a href="https://aaplesarkar.mahaonline.gov.in/pdf/Annual_Report_2019-20_English.pdf">Maharashtra State Commission annual report, 2019-20</a> (official; search excerpts); '
    '<a href="https://safar-india.org/documents/RTPSD_Final.pdf">SAFAR scoping study of right-to-public-service Acts, 2021</a> and '
    '<a href="https://ijcrt.org/papers/IJCRT2509471.pdf">IJCRT paper on the Jharkhand Right to Service Act, 2025</a> (secondary; search excerpts); '
    '<a href="https://mspsdc.meghalaya.gov.in/viewpresentation.htm?presentationid=8">Meghalaya State Public Services Delivery Commission presentation, 2023</a> (state document, excerpt: Karnataka, Jammu and Kashmir, Haryana, Gujarat and Delhi Acts); '
    '<a href="https://keralacalling.kerala.gov.in/right-to-service-act-a-leap-in-governance">Kerala Calling, 23 September 2023</a> (secondary; list of states); '
    '<a href="https://en.wikipedia.org/wiki/Right_to_Public_Services_legislation">Wikipedia, Right to Public Services legislation</a> (secondary; table of implementing states); '
    '<a href="https://accountabilityindia.in/wp-content/uploads/2020/03/policy_brief_right_to_service_laws_0.pdf">Accountability Initiative policy brief, January 2012</a> (secondary; the eight 2011 laws). '
    'Ratios and differences computed by this blog. Analysed 21 November 2026.')
RELATED = [(B + "/2026/11/karnataka-sakaala-services-act-rs-20.html", "Karnataka Sakaala Services Act: Rs 20 a day for delay, capped at Rs 500")]
step(4, "assembling page")
build("Governance &middot; India", TITLE,
      "A comparison of right-to-service laws across Indian states: who is covered, the penalty per day and its cap, the appeal tiers, and how the reported 22 states and union territories compare with the 27 names found in sources.",
      body, SOURCES, RELATED, str(OUT))
step(5, "checking output")
html = OUT.read_text()
mine = TITLE + body + SOURCES
for banned in ("masaladeutsch", "masala deutsch", "blogspot"):
    assert banned not in mine.lower(), banned
assert html.count("<h1") == 1
for h2 in re.findall(r'<h2 class="gb-h2"[^>]*>(.*?)</h2>', body):
    HEADS.append(h2)
for t in re.findall(r'class="xv-t"[^>]*>(.*?)</span>', body):
    HEADS.append(t)
for h in HEADS:
    p = _h.unescape(h)
    assert len(p) <= 90, (len(p), p)
    assert "?" not in p, p
    assert not any(w in p.lower().replace(",", " ").split() for w in ("you", "your", "we", "our")), p
step(6, "headline checks done")
step(7, "complete")
print("wrote", OUT.relative_to(ROOT), "| title", len(_h.unescape(TITLE)), "chars | headings checked:", len(HEADS))
