"""Post-earnings-announcement drift (PEAD): the research record, the behavioural explanations, the Indian evidence, and October 2026 earnings reactions.
Build from the repo root:  python3 out/research/pead-behavioural-2026/build.py   (writes out/post-pead-behavioural-earnings-reactions.html)
Every figure is from the source named beside it, or computed below with an assert. Analysed 26 November 2026.

Opened in full text (primary for their own numbers): Martineau, Critical Finance Review (via a text-extraction fetch of cfr.ivo-welch.info/published/papers/martineau2021rest.pdf);
DellaVigna and Pollet, NBER WP 11683 (October 2005 version); Peress, March 2008 working paper; Fink, Univ. of Graz WP 2020-04 (a literature review, so secondary for the studies it summarises);
Krishnan and Rangan, NSE-IGIDR WP (January 2016) and its NSE-NYU sibling on FII trading; Gupta and Dhusia (2021, full PDF); EarningsWatcher daily pages (secondary, commercial).
Abstract only: Sehgal and Bijoy (2015, RePEc page); UCLA Anderson brief on Subrahmanyam (secondary). Not opened: see GAPS below and notes.md.
"""
import json
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, insight, numbers, top_line  # noqa: E402

T0 = time.time()
OUT = ROOT / "out/post-pead-behavioural-earnings-reactions.html"
B = "https://blog.vertistratsolution.com"
STEPS = 6


def progress(n, msg):
    el = time.time() - T0
    print(f"[{n}/{STEPS}] {msg}  (elapsed {el:.1f}s, est. remaining {el / n * (STEPS - n):.1f}s)", flush=True)


# ---- 1. Martineau, Critical Finance Review 11(3-4): announcement-day R-squared of analyst surprise, all-but-microcap stocks (Table 3 Panel A, IBES sample 1984-2019)
progress(1, "Martineau figures")
PER = ["1984-90", "1991-95", "1996-2000", "2001-05", "2006-10", "2011-15", "2016-19"]
R2 = [1.7, 2.8, 3.2, 6.0, 11.5, 11.7, 11.7]
assert len(PER) == len(R2) == 7
assert R2[0] == 1.7 and R2[-1] == 11.7                      # the text prints "from 1.7 to 11.7%" for all-but-microcap stocks
assert R2[-1] == max(R2) and R2 == sorted(R2)               # monotone non-decreasing, as the table shows
R2_MULT = round(R2[-1] / R2[0], 1)
assert R2_MULT == 6.9                                       # about seven times as much of the announcement-day return is explained
RESP_ABM = (20, 120)                                        # bps response of BHAR[0,1] to the surprise rank, all-but-microcap, early vs late
RESP_MIC = (30, 100)
assert RESP_ABM[1] / RESP_ABM[0] == 6 and round(RESP_MIC[1] / RESP_MIC[0], 1) == 3.3   # the paper says "six and three times"
N_IBES, N_COMPUSTAT = 312_462, 593_654
SLOPE = (1.4, 1.2)                                          # unbiasedness-regression slope, full sample, c.1990 vs recent years; >1 = under-reaction
assert SLOPE[0] > SLOPE[1] > 1
PAPERS_ALL, PAPERS_5Y = 183, 58
assert round(100 * PAPERS_5Y / PAPERS_ALL) == 32            # about a third of all PEAD papers in top journals came in the last five years

# ---- 2. The dispute (UCLA Anderson research brief, 21 Jan 2026, on Subrahmanyam SSRN 5930255; secondary)
progress(2, "dispute figures")
T_ALL, T_EXMICRO = 2.18, 1.43                               # t-statistics of the earnings-drift factor, Feb 2001-Dec 2024, all stocks vs excluding microcaps
assert T_ALL > 2 > T_EXMICRO                                # the brief's own threshold: 2 or higher is treated as real
MICRO_VALUE_SHARE = 3                                       # microcaps are about 3% of total market value (brief's words)
T_HPW = 14                                                  # Hirshleifer, Peng, Wang (RFS 2025) "around 14", as reported by the brief
assert abs((T_ALL - T_EXMICRO) - 0.75) < 1e-9

# ---- 3. Attention evidence
# Peress (March 2008 working paper): same-firm, same-year pairs with the same surprise; drift in the 70-day window by coverage (footnote 27)
PERESS = {"Bottom decile, low coverage": -4.4, "Bottom decile, high coverage": 1.4, "Top decile, low coverage": 6.7, "Top decile, high coverage": 3.1}
assert round(PERESS["Top decile, high coverage"] - PERESS["Top decile, low coverage"], 1) == -3.6   # paper prints -3.7 from unrounded values (one-decimal rounding)
assert round(PERESS["Bottom decile, high coverage"] - PERESS["Bottom decile, low coverage"], 1) == 5.8   # paper prints 5.8
HALVED = round(PERESS["Top decile, high coverage"] / PERESS["Top decile, low coverage"], 2)
assert HALVED == 0.46                                       # "halved for positive surprises"
LS_PA = 9.6                                                 # risk-adjusted long-short, per cent a year, low-attention long vs high-attention short
# DellaVigna and Pollet, NBER WP 11683 (Oct 2005): 1995 to June 2004, 121,381 announcements after filters
DV = {"immediate_lower_pct": 15, "delayed_larger_pct": 60, "delayed_share_fri": 60, "delayed_share_other": 40, "volume_lower_pct": 10,
      "neg_surprise_prob_higher_pct": 45, "ar_lower_bp": 50, "n": 121_381}
assert DV["delayed_share_fri"] + (100 - DV["delayed_share_fri"]) == 100 and DV["delayed_share_other"] == 40
assert DV["delayed_share_fri"] / DV["delayed_share_other"] == 1.5      # 60/40: a Friday announcement leaves half again as large a share for later
BRIEF_DELAYED = 70                                          # the search excerpt's "70% higher delayed response"; the opened working paper prints 60

# ---- 4. India
progress(3, "India figures")
KR = {"n_quarters": 18_269, "n_firms": 1_398, "sample": "Q1 2008 to Q1 2014", "high": 0.7, "low": -6.6, "hedge_mean": 7.3, "hedge_median": 6.2, "window": "days +2 to +64"}
assert round(KR["high"] - KR["low"], 1) == KR["hedge_mean"]            # top-quartile CAR minus bottom-quartile CAR equals the printed 7.3 hedge return
SEN = 10.05                                                 # Sen (2009), 582 BSE firms 2001-06, up to next announcement (~3 months); quoted inside Krishnan and Rangan, so secondary
FII = {"hedge_3m": 6.5, "obs": 46_514, "sample": "Q1 2003 to Q2 2014"}
GD = {"obs": 1130, "glamour": 620, "value": 510, "erc_fe": 0.03041, "erc_re": -0.17999, "firms": 100, "sample": "2014 to 2018"}
assert GD["glamour"] + GD["value"] == GD["obs"]
assert GD["erc_re"] < 0 < GD["erc_fe"]                      # fixed-effects sign positive, random-effects (selected by Hausman test) negative: a sign conflict inside the paper
SB = {"firms": 469, "quarters": 37, "post_sig": 35, "pre_sig": 32, "sample": "December 2002 to December 2011"}
assert round(100 * SB["post_sig"] / SB["quarters"]) == 95

# ---- 5. EarningsWatcher daily reaction pages, October 2026 (secondary; commercial options-data vendor)
progress(4, "EarningsWatcher count")
EW = json.loads((HERE / "ew_oct2026.json").read_text())
DAYS = sorted(EW)
assert DAYS == ["2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30"]
tot = beyond = up = 0
ties = []
per_day = []
beyond_up = beyond_down = 0
for d in DAYS:
    p, rows = EW[d]["printed"], EW[d]["rows"]
    assert len(rows) == p["measured"], (d, len(rows), p["measured"])                                   # parsed rows equal the page's own "Measured reactions"
    assert sum(r[3] == "moved more than priced" for r in rows) == p["beyond"], d                          # parsed verdicts equal the page's "Beyond the implied move"
    assert sum(r[2] > 0 for r in rows) == p["closed_up"], d                                               # parsed signs equal the page's "Closed up"
    for sym, imp, act, ver in rows:
        if (abs(act) > imp) != (ver == "moved more than priced"):
            ties.append((d, sym, imp, act, ver))                                                         # tolerated only if an exact tie at one decimal
        if ver == "moved more than priced":
            beyond_up += act > 0
            beyond_down += act < 0
    tot += p["measured"]
    beyond += p["beyond"]
    up += p["closed_up"]
    per_day.append((d, p["measured"], p["beyond"]))
assert ties == [("2026-10-22", "META", 7.0, -7.0, "moved more than priced")], ties           # META: -7.0 against a printed 7.0, verdict uses unrounded values (priced 7.1 on its own page)
assert (tot, beyond, up) == (137, 38, 67)
assert beyond_up + beyond_down == beyond and (beyond_up, beyond_down) == (20, 18)
BEY_PCT, UP_PCT = round(100 * beyond / tot, 1), round(100 * up / tot, 1)
assert (BEY_PCT, UP_PCT) == (27.7, 48.9)
assert EW["2026-10-23"]["printed"]["beyond"] == 1 and EW["2026-10-23"]["printed"]["measured"] == 8      # the "1 of 8 on 23 October" in the brief reproduces
SEASON_BEYOND, SEASON_N = 129, 480                          # EarningsWatcher's own halfway scorecard, close-based, 14 July to 20 November 2026 (seen in a search excerpt)
assert round(100 * SEASON_BEYOND / SEASON_N, 1) == 26.9
assert abs(BEY_PCT - 100 * SEASON_BEYOND / SEASON_N) < 1.0  # the October subset sits within a point of the season-wide close-based share
PENDING = EW["2026-10-30"]["printed"]["pending"]
assert PENDING == 4

# secondary anecdotes, kept in a table and not counted
DIS = {"move": -7.4, "eps": 1.63, "est": 1.58}              # TIKR, 3 Feb 2026; brief said about 7.2%: conflict of 0.2 point between two secondary reports
WMT_AUG = {"implied": 5.0, "close": -9.2}                   # EarningsWatcher, Walmart report of 20 Aug 2026; brief's 9.15 vs 4.98 reproduces as 9.2 and 5.0
WMT_NOV = {"implied": 6.4, "close": -1.0}                   # EarningsWatcher, Walmart report of 19 Nov 2026
assert abs(WMT_AUG["close"]) > WMT_AUG["implied"] and abs(WMT_NOV["close"]) < WMT_NOV["implied"]
assert round(DIS["eps"] - DIS["est"], 2) == 0.05

# ---- quantitative read: benchmarks computed here, each with an assert
import math  # noqa: E402
P_HAT = beyond / tot
CLUSTER_SE = math.sqrt(sum((b - P_HAT * n) ** 2 for d, n, b in per_day)) / tot            # ratio estimator clustered by reaction day
CI_LO, CI_HI = round(100 * (P_HAT - 1.96 * CLUSTER_SE), 1), round(100 * (P_HAT + 1.96 * CLUSTER_SE), 1)
NAIVE_SE = math.sqrt(P_HAT * (1 - P_HAT) / tot)
GAUSS_BEYOND = round(100 * (1 - math.erf(math.sqrt(2 / math.pi) / math.sqrt(2))), 1)         # P(|Z| > E|Z|) for a normal distribution
LAPLACE_BEYOND = round(100 * math.exp(-1), 1)                                                # P(|X| > E|X|) for a Laplace (fatter-tailed) distribution
assert (GAUSS_BEYOND, LAPLACE_BEYOND) == (42.5, 36.8)
assert (CI_LO, CI_HI) == (17.7, 37.8) and round(100 * NAIVE_SE, 1) == 3.8 and round(100 * CLUSTER_SE, 1) == 5.1
assert min(100 * b / n for d, n, b in per_day) < 7 and max(100 * b / n for d, n, b in per_day) == 50.0     # the daily shares run 6.2% to 50%
SLOPE_DRIFT_SHARE = (round(SLOPE[0] - 1, 1), round(SLOPE[1] - 1, 1))
assert SLOPE_DRIFT_SHARE == (0.4, 0.2)                                                       # slope above 1 = share of the day-0/1 move still to come
ANNUALISED_NSE = round(KR["hedge_mean"] * 252 / 63, 1)
assert ANNUALISED_NSE == 29.2                                                                # naive: one 63-day spread a quarter, mean gap every quarter, no costs
MTW = {"init": 7.5, "omit": -11.0, "years_pos": 22, "years": 25}                             # Michaely, Thaler, Womack (1995), as printed in the NBER abstract excerpt; paper not opened
YIELD_ASSUMED = 4.0                                                                          # illustrative yield, an assumption of this piece
OMIT_IN_YEARS = round(abs(MTW["omit"]) / YIELD_ASSUMED, 2)
assert OMIT_IN_YEARS == 2.75
ERC_PAYER_GAP = (11, 15)                                                                     # payers' earnings response coefficients 11% to 15% lower (Review of Accounting Studies excerpt; paper not opened)

progress(5, "all asserts passed; composing the post")

TITLE = "Post-earnings drift: absent in large US stocks since 2006 in one study, mixed in India"
assert 55 <= len(TITLE) <= 90, len(TITLE)

top = top_line([
    ("1.7% to 11.7%", " of US announcement-day returns explained by analyst surprises, 1984&ndash;90 against 2016&ndash;19 (Martineau); after 2005 the drift is not significant for large stocks, and after 2015 not for microcaps."),
    ("+7.3% against none", " is the gap between top and bottom earnings-surprise quartiles over 63 days on the NSE in 2008&ndash;14 (Krishnan and Rangan), against no drift found among 100 large NSE stocks in 2014&ndash;18 (Gupta and Dhusia)."),
    ("38 of 137", " earnings reactions closed beyond the options-implied move on eight October 2026 trading days (EarningsWatcher pages, secondary; a small, selected sample)."),
])

intro = f'''<h2 class="gb-h2" id="what">What post-earnings drift is and what the original studies found</h2>
<p>Post-earnings-announcement drift (PEAD) is the tendency of a share price to keep moving in the direction of an earnings surprise for weeks after the announcement. This blog&rsquo;s own 19-market test of it is in <a href="{B}/2026/10/earnings-drift-and-piotroski-work-only.html">Earnings drift and Piotroski F-score: both work in thinly traded stocks</a>; this piece does not repeat those figures and covers the published research record, the behavioural explanations, the Indian studies and recent reaction patterns.</p>
<p>The earliest studies are not open here, so their numbers come from Fink&rsquo;s 2020 literature review (University of Graz working paper, <b>secondary</b>). Fink reports that Ball and Brown (1968) split stocks into two groups and found a negligible drift, and that Bernard and Thomas (1989) found about 2% over 60 trading days for the best and worst surprise groups each, roughly 4% a quarter or 18% annualised. Fink also writes that, while several factors are supported, &lsquo;an all-encompassing explanation remains out of sight&rsquo;.</p>
'''

# ---------------------------------------------------------------- section 1
s1 = insight(
    "US fade: analyst surprises explain 11.7% of announcement-day returns, up from 1.7%",
    bars("Share of US announcement-day return explained by analyst surprise: 1.7% then, 11.7% now",
         list(zip(PER, R2)), accent="2016-19", unit="%", vmax=15,
         sub="R-squared of announcement-day abnormal return on analyst earnings-surprise rank, all-but-microcap stocks, per cent, by period; I/B/E/S sample 1984&ndash;2019.",
         source="Martineau, Critical Finance Review 11(3&ndash;4), Table 3 Panel A (primary; 312,462 announcements; 1.7% and 11.7% are printed in the text, the middle values are read from the table).")
    + numbers(["Measure", "Value", "Source and status"],
              [["Response of day-0/1 return to surprise, all-but-microcap", f"{RESP_ABM[0]} to {RESP_ABM[1]} basis points", "Martineau, 1984&ndash;90 to 2016&ndash;19 (primary)"],
               ["Same response, microcaps", f"{RESP_MIC[0]} to {RESP_MIC[1]} basis points", "Martineau (primary)"],
               ["Drift after announcement, analyst surprise, 2 to 60 days", "not significant for all-but-microcap stocks after 2005; for microcaps only from 2016", "Martineau (primary)"],
               ["Drift with a random-walk surprise measure", "absent for the top four size quintiles since 1996; microcap drift lasts five days or fewer", "Martineau (primary): the date depends on the surprise measure"],
               ["Under-reaction slope (1.0 = none)", f"{SLOPE[0]} around 1990 to {SLOPE[1]} in recent years", "Martineau, full sample (primary): under-reaction fell but did not reach zero"],
               ["Papers on PEAD in top journals", f"{PAPERS_ALL} in total, {PAPERS_5Y} in the latest five years", "Martineau, Web of Science count (primary)"],
               ["Conflict on timing", "a UCLA Anderson brief says drift began fading in 2001 and ended by 2006; Martineau&rsquo;s analyst-surprise result is &lsquo;since 2006&rsquo; and his random-walk result &lsquo;since 1996&rsquo;", "Conflict between a secondary summary and the paper; the paper&rsquo;s wording is used"]]),
    f"The announcement-day price now absorbs about {R2_MULT:.1f} times as much of the surprise as in 1984&ndash;90, which is the mechanism Martineau gives for drift disappearing in large US stocks.",
    "Studies of drift should report results by period and with microcaps shown separately, because pooling the full sample buries the decline.",
    "fade")

# ---------------------------------------------------------------- section 2
s2 = insight(
    "Dispute: the earnings-drift factor has a t-statistic of 2.18 with microcaps, 1.43 without",
    bars("Earnings-drift factor, 2001&ndash;2024: t-statistic 2.18 with microcaps, 1.43 without",
         [("All stocks", T_ALL), ("Excluding microcaps", T_EXMICRO)], accent="Excluding microcaps", unit="", vmax=3,
         sub="t-statistic of an earnings-drift factor replicated for February 2001 to December 2024; 2 is the conventional threshold for a pattern that is unlikely to be chance.",
         source="UCLA Anderson research brief, 21 January 2026, on Subrahmanyam (SSRN 5930255) (secondary: the working paper itself was not opened).")
    + numbers(["Position", "Claim", "Source and status"],
              [["PEAD has ended", "No drift in large stocks from 2006; microcaps lost it by 2016", "Martineau, Critical Finance Review (primary)"],
               ["PEAD persists, 2025", "Dickerson, Julliard and Mueller (Journal of Financial Economics, in press) find the earnings factor remains priced; Hirshleifer, Peng and Wang (Review of Financial Studies 2025) find drift with a t-statistic of about 14", "As reported by the UCLA brief (secondary); neither paper opened"],
               ["Reconciliation", "Subrahmanyam attributes the disagreement to research design and to whether microcaps are included; microcaps are about 3% of market value", "UCLA brief (secondary)"],
               ["Lower persistence of earnings news", "A 2022 paper by Wuyang Zhao is said to attribute the decline to it", "Seen only in the commissioning brief; <b>not found or opened</b>, so no figure is used"],
               ["Caveat on the factor", "The factor in the first 2025 paper uses price reactions around announcements, not accounting surprises", "UCLA brief (secondary)"]]),
    f"Both camps can be right on their own samples, since removing microcaps, which are about {MICRO_VALUE_SHARE}% of market value but most of the sample, moves the same factor from just above to well below the threshold of 2.",
    "Read any claim that drift is alive or dead against whether microcaps are in the sample and how the surprise is measured.",
    "dispute")

# ---------------------------------------------------------------- section 3
s3 = insight(
    "Attention: drift after a good surprise was 6.7% with little media coverage, 3.1% with more",
    bars("Drift over 70 days after good news: 6.7% with low media coverage, 3.1% with more",
         list(PERESS.items()), accent=["Top decile, low coverage", "Top decile, high coverage"], unit="%", vmax=8,
         sub="Average abnormal return in the post-announcement window, per cent, for the top and bottom earnings-surprise deciles, by whether the announcement was covered in the Wall Street Journal.",
         source="Peress, &lsquo;Media Coverage and Investors&rsquo; Attention to Earnings Announcements&rsquo;, March 2008 working paper, footnote 27 (primary; mostly NYSE firms with an analyst; I/B/E/S forecasts 1993&ndash;2002).")
    + numbers(["Mechanism", "What it predicts", "What the opened papers found", "Status"],
              [["Friday announcements", "Weaker immediate reaction, larger delayed reaction", f"Immediate response {DV['immediate_lower_pct']}% lower; delayed response {DV['delayed_larger_pct']}% larger; delayed share of the total response {DV['delayed_share_fri']}% on Friday against {DV['delayed_share_other']}% on other days; volume {DV['volume_lower_pct']}% lower; {DV['n']:,} announcements, 1995 to June 2004", "DellaVigna and Pollet, NBER WP 11683, October 2005 (primary, working paper)"],
               ["Friday: conflict with the brief", f"The brief&rsquo;s excerpt says {BRIEF_DELAYED}% for the delayed response", f"The version opened prints {DV['delayed_larger_pct']}%; the {BRIEF_DELAYED}% was not found in it and may come from the later published version, which was not opened", "Conflict, unresolved"],
               ["Management timing", "Worse news released on Friday", f"{DV['neg_surprise_prob_higher_pct']}% higher probability of a negative surprise and {DV['ar_lower_bp']} basis points lower abnormal return on Fridays", "DellaVigna and Pollet (primary)"],
               ["Low media coverage", "More drift", "Drift halved for good news and eliminated for bad news when covered; long-low-attention, short-high-attention portfolio earned 9.6% a year risk-adjusted", "Peress (primary, working paper)"],
               ["Crowded announcement days", "More drift when many firms report", "Hirshleifer, Lim and Teoh (2009) found it, as summarised by Fink; the CFR Working Paper 20-10 named in the brief was <b>not found</b>", "Secondary, via Fink; no figure used"],
               ["Anchoring on the 52-week high", "More drift for good news near the high", "George, Hwang and Li (2015) and others, as summarised by Fink", "Secondary, via Fink; original not opened"],
               ["Small investors as the cause", "More drift where individuals dominate", "Fink calls evidence from brokerage data &lsquo;mixed&rsquo; and institutional ownership negatively related to drift", "Secondary, via Fink"],
               ["Illiquidity and trading costs", "More drift where costs are high", "Drift is larger in less liquid, smaller stocks; Fink reports studies that find near-zero profit after costs and others that find significant profit", "Secondary, via Fink; consistent with Martineau&rsquo;s microcap result"]]),
    f"Attention explanations make checkable predictions, and the two primary papers opened here support them in US data: drift on a covered good-news announcement was {HALVED:.2f} of the uncovered level, and Friday releases left {DV['delayed_share_fri']}% of the total response for later.",
    "A claim that investors under-react should name the date, coverage or liquidity condition under which it predicts more drift, since each is testable.",
    "attention")

# ---------------------------------------------------------------- section 4
s4 = insight(
    "India: earlier studies find a 6.5% to 10% drift gap; one finds none in the top 100 stocks",
    bars("Indian top-minus-bottom surprise gap: 10.05% (BSE 2001&ndash;06), 7.3% (NSE 2008&ndash;14), 6.5% (NSE)",
         [("Sen 2009: BSE, 582 firms, 2001-06", SEN, "to the next announcement, about three months; quoted in another paper"),
          ("Krishnan and Rangan: NSE, 2008-14", KR["hedge_mean"], f"mean over {KR['window']}; median {KR['hedge_median']}%"),
          ("Krishnan and Rangan, FII paper: NSE", FII["hedge_3m"], "market-adjusted, next three months, 2003-14"),
          ("Gupta and Dhusia: top 100 NSE, 2014-18", 0, "no drift reported; random-effects ERC negative")],
         accent="Krishnan and Rangan: NSE, 2008-14", unit="%", vmax=12,
         sub="Return gap between the highest and lowest earnings-surprise groups in each study, per cent; windows and portfolio definitions differ, so the bars are not strictly comparable.",
         source="Krishnan and Rangan, NSE-IGIDR working paper (January 2016) and NSE-NYU working paper (February 2016); Gupta and Dhusia (2021); Sen (2009) as quoted by Krishnan and Rangan (secondary).")
    + numbers(["Study", "Sample and method", "Headline result", "Status"],
              [["Krishnan and Rangan, insider trading and earnings", f"{KR['n_quarters']:,} quarterly announcements, {KR['n_firms']:,} NSE firms, {KR['sample']}; quartiles of earnings surprise, cumulative abnormal return {KR['window']}", f"Top quartile {KR['high']:+.1f}%, bottom {KR['low']:+.1f}%, hedge {KR['hedge_mean']}% mean ({KR['hedge_median']}% median); insiders&rsquo; post-announcement trades line up with the surprise", "Working paper (NSE-IGIDR); not peer reviewed as far as can be told"],
               ["Krishnan and Rangan, FII trading", f"{FII['obs']:,} firm-quarters for return tests, {FII['sample']}; NSDL daily FII trades", f"Top-minus-bottom surprise portfolio {FII['hedge_3m']}% market-adjusted over three months; FII net buying at the announcement is unrelated to the surprise and negatively related to later returns, so FIIs do not exploit the drift", "Working paper (NSE-NYU initiative); the FII angle; retail investors are not measured"],
               ["Gupta and Dhusia, Trends Economics and Management 15(37)", f"{GD['firms']} NSE firms, {GD['sample']}, {GD['obs']:,} observations ({GD['glamour']} glamour, {GD['value']} value); earnings response coefficients and 30- and 60-day drifts", f"Fixed-effects ERC {GD['erc_fe']:+.3f}, random-effects ERC {GD['erc_re']:+.3f} (the one selected); authors conclude prices are efficient to earnings news in liquid stocks", "Journal article; peer-review process not checked; the authors&rsquo; own method is a simple expectations model"],
               ["Sehgal and Bijoy, Vision 19(1), 2015", f"{SB['firms']} companies, {SB['sample']}, {SB['quarters']} quarters", f"Significant post-event abnormal returns in {SB['post_sig']} of {SB['quarters']} quarters and pre-event in {SB['pre_sig']}; no coefficient in the abstract", "Journal article; abstract only was read"],
               ["Conflict between Indian studies", "Krishnan and Rangan (all NSE firms) and Gupta and Dhusia (top 100 only) differ in size and liquidity of sample", "Consistent with Martineau&rsquo;s size result and Gupta and Dhusia&rsquo;s own explanation; not tested here", "Interpretation, not a finding"]]),
    f"The Indian record is mixed for a reason that matches the US dispute, since the studies that find a gap of 6.5% to 10% use broad samples of listed firms and the one that finds none uses only 100 large, liquid stocks, and every sample ended in 2018 or earlier.",
    "NSE or SEBI-backed researchers should rerun the drift test on 2019&ndash;2026 results with exchange time-stamps, reported separately for large, mid and small stocks.",
    "india")

# ---------------------------------------------------------------- section 5
s5 = insight(
    f"October 2026: {beyond} of {tot} US earnings reactions closed beyond the options-implied move",
    bars(f"Closed beyond the options-implied move: {beyond} of {tot} names on eight October days ({BEY_PCT}%)",
         [(f"{d[5:].replace('-', '/')}", round(100 * b / n, 1), f"{b} of {n}") for d, n, b in per_day],
         accent="10/30", unit="%", vmax=60,
         sub="Share of measured names whose first-session close was farther from the prior close than the options-implied move, per cent, by reaction date (month/day). Oct 26 and Oct 1&ndash;19 had no page.",
         source="EarningsWatcher daily &lsquo;Earnings reactions&rsquo; pages, updated 1&ndash;4 November 2026 (secondary: a commercial options-data vendor; its list of names is selected by its own tracking and not random).")
    + numbers(["Item", "Figure", "Source and status"],
              [["Names measured, eight days", f"{tot}", "Computed here from the pages; each day&rsquo;s parsed count matches the page&rsquo;s own total"],
               ["Closed beyond implied move", f"{beyond} ({BEY_PCT}%); {beyond_down} down and {beyond_up} up", "Computed here; the Oct 23 page&rsquo;s 1 of 8 reproduces"],
               ["Closed up on the day", f"{up} ({UP_PCT}%)", "Computed here"],
               ["Season-wide, close-based", f"{SEASON_BEYOND} of {SEASON_N} (26.9%), 14 July to 20 November", "EarningsWatcher scorecard, seen in a search excerpt only"],
               ["Excluded", f"{PENDING} names on Oct 30 with reaction pending; META on Oct 22 is counted as beyond because its page does so, though the rounded figures tie at 7.0%", "Rule: use each page&rsquo;s own verdict"],
               ["Disney, 2 Feb 2026", f"Fell {abs(DIS['move'])}% after earnings per share of ${DIS['eps']} against ${DIS['est']} expected; the brief had about 7.2%", "TIKR (secondary); a 0.2-point conflict between two secondary reports"],
               ["Walmart, 20 Aug 2026", f"Closed {WMT_AUG['close']}% against a priced move of &plusmn;{WMT_AUG['implied']}%", "EarningsWatcher (secondary); the brief&rsquo;s 9.15% and 4.98% reproduce as 9.2% and 5.0%"],
               ["Walmart, 19 Nov 2026", f"Closed {WMT_NOV['close']}% against a priced move of &plusmn;{WMT_NOV['implied']}%", "EarningsWatcher (secondary); the next print went the other way"]]),
    f"Roughly {BEY_PCT}% of these names moved farther than options priced, in line with the vendor&rsquo;s season-wide 26.9%, with the large moves split almost evenly ({beyond_up} up, {beyond_down} down), and the pages carry no beat or miss labels, so they cannot show whether beats are sold.",
    "Treat the Disney and Walmart episodes as anecdotes and compare any claim about selling on beats with a full list of reports that includes the surprise.",
    "reactions")

# ---------------------------------------------------------------- dividend investors
s6 = insight(
    "For a dividend investor, drift is a payout warning more than a return source",
    bars("Drift after dividend changes, 12 months: +7.5% after initiations, -11.0% after omissions",
         [("Initiations", MTW["init"], "+7.5%"), ("Omissions", abs(MTW["omit"]), "-11.0%")],
         accent="Omissions", unit="%", vmax=14,
         sub="Market-adjusted return in the 12 months after the announcement, per cent; the omission bar is drawn as a size, its sign is negative. Michaely, Thaler and Womack (1995), figures as printed in the NBER abstract excerpt.",
         source="Michaely, Thaler and Womack, Price Reactions to Dividend Initiations and Omissions: Overreaction or Drift?, Journal of Finance 50(2), 1995 (secondary: abstract excerpt only; the paper was not opened here).")
    + numbers(["Case", "What the evidence says", "Source and status"],
              [["Return case: weak", "Drift is not significant for large US stocks after 2005 (Martineau, above), and an accounting study of dividend payers reports payers&rsquo; earnings responses 11% to 15% lower, with no drift difference between payers and non-payers in untabulated tests", "Martineau (primary, opened); payer study is a Review of Accounting Studies excerpt (secondary; not opened; the drift result is untabulated)"],
               ["Risk case: stronger", f"Over 12 months, firms omitting a dividend lost {abs(MTW['omit'])}% market-adjusted and initiators gained {MTW['init']}%; the authors call this drift distinct from and more pronounced than earnings drift, and a trading rule on both samples was positive in {MTW['years_pos']} of {MTW['years']} years", "Michaely, Thaler and Womack 1995 (secondary: abstract excerpt; sample period not seen)"],
               ["What dividends signal", "Increasers had earnings rises before the change and no unexpected growth after; cutters saw earnings fall before and recover in year 1 (Benartzi, Michaely and Thaler 1997); after allowing for nonlinear earnings, dividend changes carry no information about future earnings (Grullon et al. 2005); Stacescu (2006) finds the opposite", "Excerpts only (secondary); a conflict between papers that was not resolved here"],
               ["Timing case", "Adding to a payer after a positive surprise, or waiting out the drift after a negative one, costs nothing against an income plan; no study of this rule was found", "Reasoning from the evidence above, not a tested strategy"],
               ["Illustration", f"At an assumed {YIELD_ASSUMED}% yield, an {abs(MTW['omit'])}% price fall after an omission equals {OMIT_IN_YEARS} years of the dividend", "Computed here; the yield is an assumption of this piece"],
               ["Not the same effect", "Dividend payers outperform non-payers globally by 0.58% a month after risk adjustment in one 2024 paper; that is a payout premium, not drift", "Working paper excerpt (secondary; not opened)"]]),
    f"An income investor gains little from the return side of drift in large stocks but faces the downside side, since omissions went with an {abs(MTW['omit'])}% twelve-month fall, about {OMIT_IN_YEARS} years of income at a {YIELD_ASSUMED}% yield.",
    "Treat a run of negative earnings surprises in a payer as a reason to re-check its payout cover, and use positive surprises only to time additions, not to choose what to own.",
    "income")

# ---------------------------------------------------------------- quantitative read
s7 = insight(
    f"Quant read: {BEY_PCT}% beyond the implied move, under the 42.5% a normal curve gives",
    bars(f"Beyond the implied move: observed {BEY_PCT}%, normal-curve benchmark {GAUSS_BEYOND}%",
         [("Observed, 8 days", BEY_PCT, f"{beyond} of {tot}"), ("Season-wide (vendor)", 26.9, f"{SEASON_BEYOND} of {SEASON_N}"),
          ("Laplace benchmark", LAPLACE_BEYOND, "fat tails"), ("Normal benchmark", GAUSS_BEYOND, "thin tails")],
         accent="Observed, 8 days", unit="%", vmax=50,
         sub=f"If the options-implied move equals the expected absolute move, a normal distribution puts {GAUSS_BEYOND}% of names beyond it and a Laplace distribution {LAPLACE_BEYOND}%. The 95% interval for the observed share is {CI_LO}% to {CI_HI}% when days are treated as clusters (naive interval: {round(100 * (P_HAT - 1.96 * NAIVE_SE), 1)}% to {round(100 * (P_HAT + 1.96 * NAIVE_SE), 1)}%).",
         source="Computed here from the EarningsWatcher counts above (secondary data; benchmarks are textbook results, not from a paper).")
    + numbers(["Quantity", "Value", "How it is built"],
              [["Observed share beyond the implied move", f"{BEY_PCT}% ({beyond} of {tot})", "Count from the vendor pages, eight days"],
               ["Standard error, naive and day-clustered", f"{round(100 * NAIVE_SE, 1)} and {round(100 * CLUSTER_SE, 1)} points", "Daily shares run from 6.2% to 50%, so names on one day are not independent; the clustered figure treats each day as one draw"],
               ["Benchmarks", f"Normal {GAUSS_BEYOND}%, Laplace {LAPLACE_BEYOND}%", "Chance that an absolute move exceeds its own mean; true if the implied move is the mean absolute move"],
               ["Reading", "Below both benchmarks; the clustered interval just reaches the Laplace value and excludes the normal one", "Consistent with fat tails or with options pricing a premium over the realised move; this sample cannot separate the two"],
               ["Under-reaction slope", f"{SLOPE[0]} to {SLOPE[1]}, so the share of the day-0/1 move still to come fell from {SLOPE_DRIFT_SHARE[0]} to {SLOPE_DRIFT_SHARE[1]}", "Slope minus 1, reading the slope as total move per unit of the first-days move (Martineau&rsquo;s unbiasedness regression, full sample); this reading is the piece&rsquo;s own"],
               ["Naive annualised NSE gap", f"{ANNUALISED_NSE}% a year gross", f"{KR['hedge_mean']}% over 63 days times 4, assuming the mean gap repeats every quarter at zero cost; an upper bound, not a forecast"],
               ["Risk-adjusted benchmark", f"{LS_PA}% a year", "Peress low-attention long, high-attention short, risk adjusted (primary); a different strategy and sample, shown for scale against the naive NSE figure"]]),
    f"Measured against a normal curve the October names were less often outliers than expected ({BEY_PCT}% against {GAUSS_BEYOND}%), but eight days and day-level clustering leave a wide interval of {CI_LO}% to {CI_HI}%.",
    "Judge a drift or reaction claim by its interval and its benchmark, and compare a paper gap with a risk-adjusted, after-cost number before reading it as a return.",
    "quant")

# ---------------------------------------------------------------- reader conclusions, fixes, method, gaps
conclude = '''<h2 class="gb-h2" id="conclude">What an investor can and cannot conclude</h2>
<ul>
<li>The best-documented drift sits in small, thinly covered, illiquid stocks, which are the stocks where trading costs and limited liquidity are largest, so a paper gap is not a tradable return.</li>
<li>For large US stocks the primary evidence opened here finds no significant drift after 2005, though two 2025 papers dispute that for samples that include microcaps.</li>
<li>India has no study opened here that covers 2019&ndash;2026, so how far the 2008&ndash;14 NSE gap carries to today&rsquo;s market is not known.</li>
<li>For an income investor, the documented damage from drift is on the downside: negative surprises and dividend omissions were followed by falls, while the return side is thin in large stocks.</li>
<li>A single day of reactions, or a handful of well-known names, is not a trend; this piece is research, not investment advice.</li>
</ul>
'''

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>NSE and SEBI:</b> publish a time-stamped dataset of results filings (date, hour, consolidated or standalone) so that Indian drift studies stop relying on commercial databases and guessed announcement dates.</li>
<li><b>NSE research initiative:</b> commission a rerun of the 2008&ndash;14 drift tests on 2019&ndash;2026 results, with large, mid and small stocks reported separately.</li>
<li><b>Academic authors:</b> report every drift result with and without microcaps, and name the surprise measure, since both choices move the conclusion.</li>
<li><b>Earnings-reaction trackers:</b> publish the full list of names with the reported surprise, so that claims about selling on beats can be tested on a stated, complete sample.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Martineau&rsquo;s I/B/E/S sample runs 1984&ndash;2019 (312,462 announcements) and his Compustat sample 1973&ndash;2019 (593,654); microcaps are stocks below the NYSE 20th percentile of market value. Drift is the buy-and-hold abnormal return from day 2 to day 60.</li>
<li>The middle values of the R-squared series (2.8, 3.2, 6.0, 11.5, 11.7) were read from Table 3 Panel A of the paper&rsquo;s text extraction; the first and last values are printed in the paper&rsquo;s prose and were checked against it.</li>
<li>The October 2026 count is built by <code>ew_fetch.py</code> (downloads one page per weekday, one request a second) and the parser in <code>build.py</code> and <code>ew_oct2026.json</code>. Each parsed day is asserted equal to the page&rsquo;s own measured, beyond-implied and closed-up totals. A page&rsquo;s &lsquo;beyond&rsquo; uses the first-session close, not the intraday peak, and the implied move is the options straddle price frozen before the report.</li>
<li>Indian windows differ across studies: 63 days (Krishnan and Rangan), three months (the FII paper and Sen), 30 and 60 days (Gupta and Dhusia), so the bars in the India chart are indicative.</li>
<li>Benchmarks in the quantitative section: if the implied move equals the expected absolute move, the chance that a normal variable exceeds its own mean absolute value is 42.5% and a Laplace variable 36.8%. The day-clustered standard error is the ratio-estimator form, the square root of the sum over days of (beyond minus share times measured) squared, divided by the total names; it assumes days are independent.</li>
<li>Percentages are as printed in the sources; differences between printed values are computed here with the assert noted in <code>build.py</code>.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The Ball and Brown (1968) and Bernard and Thomas (1989) papers were not opened, so their figures are Fink&rsquo;s summary, and Fink says Ball and Brown found a negligible drift.</li>
<li>The Choi and Kim conservatism model (cis.upenn.edu): the host was not reachable from this environment, so the conservatism explanation is not described.</li>
<li>The Fink, Palan and Theissen experiment: the Graz file opened is Fink&rsquo;s review, not the experiment, so no experimental figure is given.</li>
<li>Wuyang Zhao&rsquo;s 2022 paper and the competing-announcements working paper (CFR 20-10): neither was found; no number from them is used. The Hirshleifer, Lim and Teoh crowded-day result is Fink&rsquo;s summary only.</li>
<li>Anchoring: only a review&rsquo;s summary of George, Hwang and Li (2015) was found, with no Indian evidence. Retail investors: the evidence in Fink is described as mixed and no Indian retail study was found.</li>
<li>The Rangan paper in the IIMB repository (ICFMCG 2016) was not located. The NSE file 1516_BS3.pdf is a different paper (Brochet, Lee and Srinivasan) marked as a very preliminary draft not to be cited without the authors&rsquo; consent, so none of its figures are used. The NSE file 4.pdf is a summary of the Krishnan and Rangan insider-trading paper, not a paper on FIIs; the FII paper is NSE file 1415_BS5.</li>
<li>Sehgal and Bijoy: the full text was not opened, so no coefficient or return is given. Gupta and Dhusia&rsquo;s drift tables (counts only) were not turned into a return.</li>
<li>The investinglive.com count of 18 names (6 beyond implied downward, 2 beats to the upside) and the reports on Apple and Palantir were not located and are not used. The Disney move differs between two secondary sources (7.2% in the brief, 7.4% on TIKR).</li>
<li>Whether beats are sold: the EarningsWatcher pages carry no surprise label, so the share of beats with falling prices could not be computed. October pages from 1 to 19 and 26 October returned no page (404), so the count covers 8 of 22 weekdays.</li>
<li>An India-specific 2026 earnings-reaction count: none was found.</li>
<li>The dividend section rests on abstract or search excerpts only: Michaely, Thaler and Womack (1995), Benartzi, Michaely and Thaler (1997), Grullon et al. (2005), Stacescu (2006), a Review of Accounting Studies paper on dividend payers and a 2024 dividend-premium paper. None was opened here, so sample periods, windows and the untabulated drift result are unchecked.</li>
<li>No study was found that tests drift separately for dividend growers against flat payers, that uses accruals or earnings quality to predict dividend cuts, or that covers Indian dividend payers.</li>
<li>The 4% yield is an illustration, not a data point, and the 29.2% annualised NSE gap is a naive upper bound.</li>
</ul></details>
'''

body = STYLE + top + intro + s1 + s2 + s3 + s4 + s5 + s6 + s7 + conclude + fixes + method + gaps

SOURCES = (
    'Primary, opened for this piece: <a href="https://cfr.ivo-welch.info/published/papers/martineau2021rest.pdf">Martineau, Rest in Peace Post-Earnings Announcement Drift, Critical Finance Review 11(3&ndash;4)</a>; '
    '<a href="https://www.nber.org/papers/w11683">DellaVigna and Pollet, Investor Inattention, Firm Reaction, and Friday Earnings Announcements, NBER WP 11683</a>; '
    '<a href="https://www.fmg.ac.uk/sites/default/files/2020-08/J-Peress.pdf">Peress, Media Coverage and Investors&rsquo; Attention to Earnings Announcements (2008 working paper)</a>; '
    '<a href="https://nsearchives.nseindia.com/research/content/NSE-IGIDR-WP4-14-15.pdf">Krishnan and Rangan, insider trading and earnings announcements in India, NSE-IGIDR working paper</a>; '
    '<a href="https://nsearchives.nseindia.com/research/content/1415_BS5.pdf">Krishnan and Rangan, FII trading and future returns, NSE-NYU working paper</a>; '
    '<a href="https://journals.lib.vutbr.cz/index.php/trends/article/view/541">Gupta and Dhusia (2021), Trends Economics and Management 15(37)</a>. '
    'Abstract only: <a href="https://ideas.repec.org/a/sae/vision/v19y2015i1p25-36.html">Sehgal and Bijoy (2015), Vision 19(1)</a>. '
    'Secondary: <a href="https://static.uni-graz.at/fileadmin/sowi/Working_Paper/2020-04_Fink.pdf">Fink, A Review of the Post-Earnings-Announcement Drift (2020)</a> (original studies, anchoring, retail, crowded days); '
    '<a href="https://anderson-review.ucla.edu/is-post-earnings-announcement-drift-a-thing-again">UCLA Anderson Review, 21 January 2026</a> (Subrahmanyam and the 2025 papers); '
    '<a href="https://earnings-watcher.com/wiki/earnings-reactions-2026-10-23">EarningsWatcher daily reaction pages, 20&ndash;30 October 2026</a> and its Walmart page; '
    '<a href="https://www.tikr.com/blog/disney-shares-nyse-dis-stock-fall-despite-theme-park-revenue-hitting-record-10-billion">TIKR, 3 February 2026</a> (Disney). '
    'Dividend section, secondary (abstract or search excerpts, not opened): <a href="https://www.nber.org/papers/w4778">Michaely, Thaler and Womack, NBER WP 4778 (Journal of Finance 1995)</a>; <a href="https://econpapers.repec.org/RePEc:bla:jfinan:v:52:y:1997:i:3:p:1007-34">Benartzi, Michaely and Thaler (1997)</a>; <a href="https://econpapers.repec.org/RePEc:ucp:jnlbus:v:78:y:2005:i:5:p:1659-1682">Grullon, Michaely, Benartzi and Thaler (2005)</a>; <a href="https://efmaefm.org/0EFMSYMPOSIUM/2007/papers/stacescu.pdf">Stacescu (2006)</a>; <a href="https://link.springer.com/doi/10.1007/s11142-021-09642-4">dividend payers and earnings response, Review of Accounting Studies</a>. '
    'Shares, ratios and counts computed by this blog. Analysed 26 November 2026. Not investment advice.')

RELATED = [
    (f"{B}/2026/10/earnings-drift-and-piotroski-work-only.html", "Earnings drift and Piotroski F-score: both work in thinly traded stocks"),
]

progress(6, "writing file")
build("Markets &middot; Earnings reactions", TITLE,
      "Post-earnings drift has faded in large US stocks in one major study, remains disputed for microcaps, and is mixed in Indian studies; attention and coverage explanations have direct evidence, and October 2026 reactions are a small sample.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
