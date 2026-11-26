"""Post-earnings-announcement drift by geography: this blog's own market-by-market numbers and the cross-country literature.
Build from the repo root:  python3 out/research/pead-geography-2026/build.py   (writes out/post-pead-by-geography.html)

DATA STATUS (read this first). The public repo herrrickshaw/global-market-scanners holds NO saved per-market earnings-drift file (no CSV, JSON, notebook
or price parquet). The only per-market numbers are the prose table in EARNINGS_LIQUIDITY.md (12 markets with at least 40 events, `per_market_summary`
min_events=40). It has no per-market quintile gap or monotonicity score; those exist only pooled (PEAD.md: +2.50%, 0.90) and for the US (60 days).
The price download was not re-run: the cache is not in the repo and the earlier study used about one year of data per market.
Literature: figures are kept only where the page was read from an allowed host. Reads that went through a non-allowlisted fetch service are
shown as 'excerpt only' with no figures (see NOTES.md)."""
import math
import pathlib
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-pead-by-geography.html"
B = "https://blog.vertistratsolution.com"
T0 = time.time()
STEPS = 8


def step(i, msg):
    el = time.time() - T0
    eta = el / i * (STEPS - i) if i else 0
    print(f"[{i}/{STEPS}] {msg}  (elapsed {el:.1f}s, est. remaining {eta:.1f}s)", flush=True)


# ---- 1. Published pooled figures (live post earnings-drift-and-piotroski-work-only; PEAD.md; EARNINGS_LIQUIDITY.md)
step(1, "published pooled figures")
POOL_EVENTS, POOL_GAP, POOL_MONO, POOL_IC = 8803, 2.5, 0.90, 0.029
TOP_Q, BOT_Q = 1.4, -1.1
assert round(TOP_Q - BOT_Q, 1) == POOL_GAP                    # 1.4 - (-1.1) = 2.5, the published gap
US_GAP_60D, US_MONO_60D = -0.5, 0.00                          # PEAD.md, US only, 60 days (event count for this run not printed)
US_EDGAR = dict(events=313, ic=0.102, gap=1.04, surge=1.6)    # real SEC filing dates, illiquid-minus-liquid fifth
US_PROXY_IC = 0.010

# ---- 2. Per-market table, EARNINGS_LIQUIDITY.md ("Per-country test"): events, volume surge, illiquidity-drift rank correlation
step(2, "per-market table and consistency checks")
MK = {  # code: (name, region, events, vol surge x, illiq IC)
    "BR": ("Brazil", "Latin America", 109, 3.6, 0.242),
    "EU": ("EU (aggregate code)", "Europe", 404, 3.6, 0.151),
    "UK": ("United Kingdom", "UK", 482, 3.9, 0.132),
    "SG": ("Singapore", "Asia-Pacific", 440, 4.0, 0.100),
    "US": ("United States", "North America", 4075, 3.7, 0.010),
    "FI": ("Finland", "Europe", 108, 4.5, -0.26),
    "ZA": ("South Africa", "Africa and Middle East", 53, 3.5, -0.03),
}
NOCOUNT = {"AU": ("Australia", "Asia-Pacific"), "CA": ("Canada", "North America"), "DE": ("Germany", "Europe")}   # IC +0.02 to +0.06, events not printed, surge about 3.8
NOCOUNT_IC = (0.02, 0.06)
MIN_READ = 100
KNOWN_EVENTS = sum(v[2] for v in MK.values())
assert KNOWN_EVENTS == 5671
REMAIN = POOL_EVENTS - KNOWN_EVENTS
assert REMAIN == 3132
assert round(100 * MK["US"][2] / POOL_EVENTS) == 46         # 'nearly half of all events' in the live post
N_TABLE, N_ALL = 12, 19
UNNAMED_IN_TABLE = N_TABLE - len(MK) - len(NOCOUNT)
assert UNNAMED_IN_TABLE == 2 and N_ALL - N_TABLE == 7       # two markets in the 12 are not named; seven markets had under 40 events
POS = [k for k, v in MK.items() if v[4] > 0] + list(NOCOUNT)
assert len(POS) == 8                                        # the repo says '8 of 12 show the expected sign': that needs both unnamed markets at or below zero
SMALL = [k for k, v in MK.items() if v[2] < MIN_READ]
assert SMALL == ["ZA"]
W_KNOWN = sum(v[2] * v[4] for v in MK.values()) / KNOWN_EVENTS
assert round(W_KNOWN, 3) == 0.036
IMPLIED_REST = (POOL_IC * POOL_EVENTS - W_KNOWN * KNOWN_EVENTS) / REMAIN
assert round(IMPLIED_REST, 3) == 0.016                      # what the other 3,132 events would need to average for a weighted mean to equal +0.029
SE = {k: 1 / math.sqrt(v[2] - 1) for k, v in MK.items()}    # approximate standard error of a rank correlation under no relation
Z = {k: MK[k][4] / SE[k] for k in MK}
assert round(Z["BR"], 1) == 2.5 and round(Z["FI"], 1) == -2.7 and round(Z["US"], 1) == 0.6 and round(Z["EU"], 1) == 3.0 and round(Z["UK"], 1) == 2.9
assert max(abs(z) for z in Z.values()) < 3.1
# the published 'Finland and South Africa had too few events' (live post) against the 100-event threshold used here
assert MK["FI"][2] >= MIN_READ > MK["ZA"][2]

# ---- 3. Regional figures recomputed from the per-market rows (event-weighted illiquidity IC over markets with a recorded count)
step(3, "regional figures")
REG_ORDER = ["North America", "UK", "Europe", "Asia-Pacific", "Latin America", "Africa and Middle East"]
REG = {}
for r in REG_ORDER:
    rows = [(k, v) for k, v in MK.items() if v[1] == r]
    n = sum(v[2] for _, v in rows)
    REG[r] = dict(n=n, ic=(sum(v[2] * v[4] for _, v in rows) / n), mk=[k for k, _ in rows])
assert sum(d["n"] for d in REG.values()) == KNOWN_EVENTS
assert round(REG["Europe"]["ic"], 3) == 0.064 and REG["Europe"]["n"] == 512
assert round(REG["North America"]["ic"], 3) == 0.010 and round(REG["Latin America"]["ic"], 3) == 0.242
MISSING = {"North America": "Canada", "Europe": "Germany", "Asia-Pacific": "Australia"}
INDIA_IN_TABLE = False                                      # India is not among the 12 named markets

# ---- 4. India, from papers read on allowed hosts (nsearchives.nseindia.com, ideas.repec.org, journals.lib.vutbr.cz)
step(4, "India study figures")
IN_INSIDER = dict(hi=0.7, lo=-6.6, hedge=7.3)
assert round(IN_INSIDER["hi"] - IN_INSIDER["lo"], 1) == IN_INSIDER["hedge"]       # 0.7 - (-6.6) = 7.3
IN_FII = 6.5
IN_SEN = 10.05                                              # second-hand, as described by Krishnan and Rangan
assert POOL_GAP < IN_FII < IN_INSIDER["hedge"] < IN_SEN

TITLE = "Post-earnings drift by market: this blog's 12-market data and what studies find by country"
assert 55 <= len(TITLE) <= 90, len(TITLE)

# ---- 5. build the page
step(5, "chart sections")
top = top_line([
    (f"+{POOL_GAP}%", f" was the 40-day drift gap between the best and worst earnings-day reactions, pooled over {POOL_EVENTS:,} events in 19 markets; the saved per-market notes give no gap or monotonicity score by market, so a country ranking of the gap cannot be built."),
    ("+0.242 to +0.010", f" is the range of the illiquidity-drift rank correlation across the markets with a recorded event count, Brazil ({MK['BR'][2]} events) to the US ({MK['US'][2]:,}); it is positive in 8 of the 12 markets the repo tabulates."),
    (f"{IN_FII}% to {IN_INSIDER['hedge']}%", " is the best-minus-worst drift reported in two Indian working papers over about three months; one peer-reviewed 2021 paper finds no drift, and the studies measure different things."),
])

# section 1: pooled and US
s1 = insight(
    f"Pooled gap: +{POOL_GAP}% over 40 days in 19 markets, about {US_GAP_60D}% in the US",
    bars(f"Best-minus-worst drift gap: +{POOL_GAP}% pooled over 19 markets, {US_GAP_60D}% in the US alone",
         [("Top fifth by surprise, pooled, 40 days", TOP_Q, f"{POOL_EVENTS:,} events in all"),
          ("Bottom fifth by surprise, pooled, 40 days", BOT_Q, f"{POOL_EVENTS:,} events in all"),
          ("Gap, pooled, 40 days", POOL_GAP, "monotonicity 0.90"),
          ("Gap, US only, 60 days", US_GAP_60D, "monotonicity 0.00; event count for this run not printed")],
         accent="Gap, pooled, 40 days", unit="%",
         sub="Market-adjusted drift from two days after the event, per cent. Events are volume-spike days, not true earnings dates. The two gaps use different horizons and are not like for like.",
         source="This blog&rsquo;s 19-market study: global-market-scanners PEAD.md and EARNINGS_LIQUIDITY.md (primary, repo text; the underlying price files are not in the repo).")
    + numbers(["Measure", "Value", "Status"],
              [["Pooled events, 19 markets", f"{POOL_EVENTS:,}", "published; per-market counts known for 7 markets only"],
               ["Top fifth, bottom fifth, gap (40 days)", f"+{TOP_Q}%, {BOT_Q}%, +{POOL_GAP}%", "recomputed gap matches the published +2.5%"],
               ["Monotonicity of the five groups", f"{POOL_MONO}", "pooled only"],
               ["US only (60 days)", f"gap {US_GAP_60D}%, monotonicity {US_MONO_60D:.2f}", "different horizon from the pooled run"],
               ["US with real SEC filing dates", f"{US_EDGAR['events']} events, illiquidity link +{US_EDGAR['ic']}, drift gap +{US_EDGAR['gap']}%", "against +0.010 with the volume-spike stand-in; filing dates trail press releases"]]),
    f"The pooled top and bottom fifths recompute to the published {POOL_GAP}% gap, but the five groups line up at 0.90 only when all markets are mixed, so the per-market quintile gaps that would show where the drift sits were not saved.",
    "The study owner should re-run the earnings-event study with a per-market table of events, quintile gap and monotonicity written to a file, so that the pooled figures can be recomputed from the rows.",
    "pooled")

# section 2: by market
mk_rows = []
for k in ["BR", "EU", "UK", "SG", "US"]:
    v = MK[k]
    mk_rows.append((v[0], v[4], f"{v[2]:,} events", f"{v[4]:+.3f}".replace("+0.0", "+0.0")))
mk_rows.append(("Finland", MK["FI"][4], f"{MK['FI'][2]} events: borderline, earlier post called it too few", f"{MK['FI'][4]:+.2f}"))
mk_rows.append(("South Africa", None, f"{MK['ZA'][2]} events", "too few to read"))
mk_rows.append(("Australia, Canada, Germany", None, "events not recorded", "+0.02 to +0.06, count unknown"))
s2 = insight(
    "By market: the illiquidity link is +0.242 in Brazil and +0.010 in the US",
    bars("Illiquidity-drift link by market: Brazil +0.242, EU +0.151, UK +0.132, US +0.010",
         mk_rows, accent=["Brazil", "United States"], vmax=0.3,
         sub="Rank correlation between a stock&rsquo;s illiquidity before the event and its drift in the direction of the surprise; positive means more drift in thinly traded stocks. Event counts beside each market; grey dashed bars are not read.",
         source="global-market-scanners EARNINGS_LIQUIDITY.md, per-country test, 40-day drift, about one year of daily data (primary, repo text). Markets with under 40 events are not in the table. Standard errors are this blog&rsquo;s approximation.")
    + numbers(["Market", "Region", "Events", "Volume surge (x)", "Illiquidity link", "About 1 SE", "Link / SE", "Quintile gap, monotonicity"],
              [[v[0], v[1], f"{v[2]:,}" + (" (too few to read)" if v[2] < MIN_READ else ""), v[3], f"{v[4]:+.3f}", f"{SE[k]:.3f}", f"{Z[k]:+.1f}", "not saved"]
               for k, v in MK.items()]
              + [[f"{n} ({k})", reg, "not recorded", "about 3.8", "+0.02 to +0.06", "&ndash;", "&ndash;", "not saved"] for k, (n, reg) in NOCOUNT.items()]
              + [["Two further markets in the 12", "unnamed", "&ndash;", "&ndash;", "at or below zero (derived)", "&ndash;", "&ndash;", "not saved"],
                 ["Seven other markets", "unnamed", "under 40 each", "&ndash;", "not computed", "&ndash;", "&ndash;", "not saved"]]),
    f"Eight of the 12 tabulated markets are positive, but with {MK['BR'][2]} events Brazil sits only {Z['BR']:.1f} standard errors from zero, Finland sits {abs(Z['FI']):.1f} on the other side from {MK['FI'][2]} events, and only the UK and EU ({MK['UK'][2]} and {MK['EU'][2]} events) pair a positive link with a count above 400.",
    "A reader should treat the order of the markets as unproven and wait for a re-run with true announcement dates and several years of prices before choosing a country on this evidence.",
    "markets")

# section 3: by region
reg_rows = []
for r in REG_ORDER:
    d = REG[r]
    lab = r
    note = f"{d['n']:,} events recorded" + (f"; {MISSING[r]} not recorded" if r in MISSING else "")
    if d["n"] < MIN_READ:
        reg_rows.append((lab, None, note, "too few to read"))
    else:
        reg_rows.append((lab, d["ic"], note, f"{d['ic']:+.3f}"))
reg_rows.append(("India", None, "not in the tabulated markets", "not in the data"))
s3 = insight(
    "By region: Latin America and the UK lead on the link, North America is near zero",
    bars("Illiquidity-drift link by region: Latin America +0.242, UK +0.132, N. America +0.010",
         reg_rows, accent=["Latin America", "North America"], vmax=0.3,
         sub="Event-weighted mean of the market figures above, over the markets with a recorded count; Canada, Germany and Australia are missing from their regions. Africa and the Middle East rests on 53 events; India is not in the table.",
         source="Recomputed here from the per-market table of EARNINGS_LIQUIDITY.md (primary, repo text); these are not figures the study published.")
    + numbers(["Region", "Markets with counts", "Events recorded", "Weighted link", "Not recorded"],
              [[r, ", ".join(MK[k][0] for k in REG[r]["mk"]), f"{REG[r]['n']:,}", f"{REG[r]['ic']:+.3f}" if REG[r]["n"] >= MIN_READ else "too few to read", MISSING.get(r, "&ndash;")]
               for r in REG_ORDER]
              + [["India", "none", "0", "&ndash;", "no India row in the tabulated markets"],
                 ["Check against the pooled figure", f"all 7 markets with counts: {KNOWN_EVENTS:,} of {POOL_EVENTS:,} events", f"{KNOWN_EVENTS:,}", f"{W_KNOWN:+.3f}", f"published pooled link +{POOL_IC}; the other {REMAIN:,} events would need to average {IMPLIED_REST:+.3f} (not a proof: a pooled rank correlation is not a weighted mean)"]]),
    f"The seven markets with recorded counts cover {KNOWN_EVENTS:,} of the {POOL_EVENTS:,} events and give a weighted link of {W_KNOWN:+.3f} against the published pooled +{POOL_IC}, a difference of {W_KNOWN - POOL_IC:+.3f} that the missing {REMAIN:,} events cannot be shown to explain.",
    "The study owner should publish the 19-market event table with each market&rsquo;s event count, so that the pooled +0.029 and the regional figures here can be rebuilt without inference.",
    "regions")

# section 4: India
s4 = insight(
    f"India: working papers report {IN_FII}% to {IN_INSIDER["hedge"]}% drift in about three months",
    bars("India: best-minus-worst drift of 6.5% and 7.3% in working papers, 10.05% second-hand",
         [("This blog, 19 markets pooled, 40 days", POOL_GAP, "volume-spike events"),
          ("FII working paper, 3 months, top and bottom quartile", IN_FII, "NSE-NYU series, 2003-14 data"),
          ("Insider-trading working paper, days 2 to 64", IN_INSIDER["hedge"], "18,269 announcements, 1,398 firms, 2008-14"),
          ("Sen (2009), about 3 months, as cited", IN_SEN, "582 BSE firms; secondary description")],
         accent="Insider-trading working paper, days 2 to 64", unit="%", vmax=11,
         sub="Top minus bottom portfolio, market-adjusted, per cent. The studies use different portfolios (quintile or quartile), windows and surprise measures, so the bars are not like for like.",
         source="Krishnan and Rangan, NSE-IGIDR working paper (read in full) and NSE-NYU working paper (6-page file, footnote 7); Sen (2009) as described in the first; this blog (secondary context).")
    + numbers(["Study", "Status", "Sample", "Method and window", "Finding"],
              [["Krishnan and Rangan, insider trading and earnings announcements", "NSE-IGIDR working paper, 2015-16", "18,269 quarterly announcements, 1,398 NSE firms, 2008 to Q1 2014", "seasonal random walk surprise; market-adjusted return, days +2 to +64; four portfolios", "highest portfolio +0.7%, lowest -6.6%, hedge 7.3% (t 15.80)"],
               ["Krishnan and Rangan, FII trading and returns", "NSE-NYU working paper; file read is 6 pages without tables", "FII trades 2003-14; firm count not read", "surprise measure not in the file; next 3 months", "6.5% market-adjusted, top minus bottom quartile (footnote 7)"],
               ["Brochet, Lee and Srinivasan, insider trading and news", "NSE-NYU draft, Dec 2016, marked very preliminary", "24,135 firm-years, 2006-14", "scaled seasonal-random-walk surprise; 30-day CAR from day 2", "SUE coefficient positive and significant; no value read for the full sample; no drift after insider purchases"],
               ["Gupta and Dhusia (2021), Trends Economics and Management", "peer reviewed", "100 large-cap NSE firms 2014-18 in the abstract; 98 firms and 2013-18 in the text; 1,130 observations", "analyst forecast error; 30- and 60-day windows", "counts of positive and negative drifts only; concludes the market is efficient to earnings"],
               ["Sehgal and Bijoy (2015), Vision", "peer reviewed; abstract only", "469 companies, Dec 2002 to Dec 2011, 37 quarters", "not read", "significant post-event abnormal returns in 35 of 37 quarters"],
               ["Sen (2009)", "described in Krishnan and Rangan; not opened", "582 BSE firms, 2001-06", "highest minus lowest quintile, about 3 months", "10.05% hedge return (second-hand)"]]),
    f"Two working papers from one author team report {IN_FII}% and {IN_INSIDER['hedge']}% over about three months against this blog&rsquo;s pooled {POOL_GAP}% over 40 days, while the one peer-reviewed paper that tests efficiency directly (Gupta and Dhusia, 2021) finds none, so India looks larger than the blog&rsquo;s pooled figure but the evidence is not yet like for like.",
    "A reader should read the Indian numbers as 2008-14 working-paper results on a different surprise measure and not as a current figure.",
    "india")

step(6, "literature table")
DRV = [
    ["Retail share and limited attention", "Four China A-share papers (Chen, Gao and Liu 2021; Shu and Tan 2022; Du et al. 2023; Feng et al. 2022) tie drift to inattention, opinion divergence and policy uncertainty", "abstracts only; no figures read", "no retail-versus-institution split found; Du et al. say institutional ownership does not reduce the effect"],
    ["Culture (individualism)", "Dou, Truong and Veeraraghavan (2016): 30,383 firms, 41 countries, 1995-2008; individualism is positively and uncertainty avoidance negatively linked to earnings momentum profits. Guo and Holmes (2022) report the same direction", "Dou et al.: abstract; Guo and Holmes: excerpt only", "earnings momentum here is a profit measure, not this blog&rsquo;s drift gap; no country figures read"],
    ["Market openness", "Guo and Holmes (2022): the individualism effect is smaller in more open, capital-market-integrated countries", "excerpt only", "no figures used"],
    ["Reporting standards (IFRS)", "Hung, Li and Wang: PEAD declines after the 2005 mandatory IFRS adoption outside the US. Forbes and Giannopoulos (2015) find Greek drift alive and growing after IFRS", "Hung et al.: working paper, excerpt only; Forbes and Giannopoulos: abstract", "conflict: the two point in opposite directions for the same shift in standards, with different periods and methods"],
    ["Algorithmic trading, disclosure, investor protection", "Chen (2023): 41 markets; algorithmic activity around announcements is negatively associated with PEAD, more so where investor protection, information dissemination and disclosure are stronger", "abstract only", "no figures read; this means arbitrage capital alone does not explain the map"],
    ["Time, within the US", "Martineau (2022): drift for large US stocks non-existent since 2006; two 2025 papers dispute this (per a UCLA Anderson summary)", "abstract excerpt; the 2025 papers were not read", "contested"],
    ["Breadth of drift", "Fink (2020, read in full) lists country studies finding drift in Australia, Canada, China, Finland, Greece, India, New Zealand, Saudi Arabia, South Africa, South Korea, Spain, Tunisia, Turkey and the UK, and none in Belgium and Singapore; he calls the size &lsquo;surprisingly stable&rsquo; across developed and emerging markets", "secondary review, full text", "conflicts with this blog&rsquo;s Singapore link of +0.100, a different measure; also says there is none in markets with very weak institutions"],
]
s5 = (f'<section class="xv-sec"><h2 class="gb-h2" id="drivers">What studies say drives the differences</h2>\n'
      + numbers(["Possible driver", "What the studies report", "How it was read", "Limit"], DRV, "Show the driver-by-driver table")
      + '<div class="xv-so"><p><b>What it means:</b> Culture, retail attention, reporting standards, algorithmic trading and openness each have a paper behind them, but none was read with country-level drift numbers, so the drivers are candidates and not a ranking.</p>'
        '<p><b>What to do:</b> Treat any single-cause story for why one country drifts more as untested.</p></div></section>\n')

CTRY = [
    ["UK", "Hew, Skerratt, Strong and Walker (1996): drift for small firms but not large (206 firms, seven half-years); Liu, Strong and Xu (2003): significant drift on three surprise measures", "search excerpts of abstracts", "no magnitude read"],
    ["Korea", "Goh and Jeon (2017): drift stronger near 52-week highs; a 2019 study of individual investors exists", "Goh and Jeon: abstract; the 2019 study was read only through a route outside the allowed hosts, so its figures are not used", "no Korean magnitude used"],
    ["Japan", "Kasahara and Zhong (2022): drift persists in Tokyo-listed stocks (2007-18) and is not explained by size or illiquidity; Jinushi (2023) reports drift weakening over 2002-20, excerpt only", "Kasahara and Zhong: abstract; Jinushi: excerpt only", "no magnitude used"],
    ["Continental Europe", "G&eacute;rard (2012): market-based surprise, 1997 to June 2010, drift not limited to small illiquid stocks (abstract only). Hong, Lee and Swaminathan (2003, forecast-revision earnings momentum, excerpt only): significant in France and Germany and the UK, not in Japan, Korea, Malaysia, Singapore or Taiwan", "abstracts and excerpts", "revision-based momentum is not drift after announcements"],
    ["Latin America", "Santana, Black and de Lima (2022): six markets; drift found in Brazil, Chile and Mexico, the markets with the most events (excerpt only; figures not used)", "excerpt only", "Argentina, Colombia and Peru: no significant result stated"],
]
s6 = (f'<section class="xv-sec"><h2 class="gb-h2" id="countries">Country studies found outside this blog&rsquo;s data</h2>\n'
      + numbers(["Market", "What was found", "How it was read", "Limit"], CTRY, "Show the country studies")
      + '<div class="xv-so"><p><b>What it means:</b> The earlier search found no UK, Korea, Japan or European study, and a wider search found several, nearly all read at abstract level, so the literature supports drift in most places studied but gives no cross-country magnitude comparison.</p>'
        '<p><b>What to do:</b> Compare countries only within a single study that uses one method across all of them.</p></div></section>\n')

step(7, "conclusions and caveats")
conclude = '''<h2 class="gb-h2" id="conclude">What a reader choosing where to look should and should not conclude</h2>
<ul>
<li><b>Reasonable:</b> drift is not a US constant. Studies find it in the UK, India, Japan, China, Korea and Latin America, while the US shows little in large stocks, and this blog&rsquo;s own US numbers are near zero.</li>
<li><b>Reasonable:</b> if drift lives anywhere it is where trading is costly, and the blog&rsquo;s link is positive in 8 of 12 markets. The US with true filing dates (313 events) shows +0.102, so even the US result depends on the event date.</li>
<li><b>Not supported:</b> a ranking of countries. Per-market counts run from 53 to 4,075 over about one year, event days are volume spikes outside the US, and no per-market drift gap was saved.</li>
<li><b>Not supported:</b> that any market can be traded on this. Drift sizes of a few per cent over weeks come before trading costs, and this is not investment advice.</li>
</ul>
'''

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>This blog&rsquo;s study owner:</b> write one file with each market&rsquo;s event count, quintile gap, monotonicity, volume surge and illiquidity link, and have the post&rsquo;s pooled figures recomputed from it.</li>
<li><b>This blog&rsquo;s study owner:</b> replace the volume-spike stand-in with announcement dates from each exchange or regulator, as the US filing-date run did.</li>
<li><b>This blog&rsquo;s study owner:</b> extend the price history from about one year to at least five before ranking any country.</li>
<li><b>NSE and BSE:</b> publish a machine-readable file of board-meeting results dates with the time stamp, so that Indian event dates need not be proxied.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''

method = '''<details class="xv-n"><summary>Method and definitions</summary>
<ul>
<li>Events are days when volume exceeded 2.5 times its recent average on a move of more than two standard deviations, on a liquidity-filtered universe (top 40% by dollar volume). Drift is market-adjusted return from day 2; the pooled run used 40 days, the US-only run 60.</li>
<li>The illiquidity link is a rank correlation between pre-event illiquidity and drift multiplied by the sign of the surprise. The markets table only lists markets with at least 40 events.</li>
<li>The standard error shown is 1 divided by the square root of events minus one, an approximation that treats events as independent.</li>
<li>Regional figures are event-weighted means of the market figures and are computed here; the study did not publish them.</li>
<li>The page marks a market under 100 events &lsquo;too few to read&rsquo;. Finland has 108, so it is plotted, but the blog&rsquo;s earlier post called it too few: that is a conflict in how the cut-off was applied, and its +0.26 rests on 108 events.</li>
<li>Papers are labelled by how they were read. &lsquo;Excerpt only&rsquo; means the page text came through a search excerpt or a fetch route outside the allowed hosts; no figure from such a read is printed.</li>
</ul></details>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>The per-market quintile drift gap and monotonicity score for any market: the saved notes give them only pooled and for the US.</li>
<li>Event counts for Australia, Canada and Germany, the identity of two further markets in the 12, and anything for the seven markets with under 40 events.</li>
<li>That the pooled +2.5%, +0.029 and 8,803 events can be rebuilt from per-market rows. The seven markets with counts cover 5,671 events; the pooled +0.029 differs from their weighted +0.036, and the gap cannot be traced.</li>
<li>Whether India is among the 19 markets or what its row would show.</li>
<li>Country-by-country drift sizes from the cross-country papers (Dou et al., Guo and Holmes, Chen, Hung et al.): only abstracts or excerpts were read, so no cross-country magnitude is given.</li>
<li>Any Korean, Japanese, UK or European drift magnitude from a paper read in full on an allowed host.</li>
<li>Any direct retail-versus-institutional drift split for China.</li>
<li>The 2025 US papers disputing Martineau; they were not read.</li>
<li>Whether Kim and Kim (2003) is a Korean study: it is not, so it is not used.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + s5 + s6 + conclude + fixes + method + gaps

SOURCES = (
    'This blog&rsquo;s own data: <a href="https://github.com/herrrickshaw/global-market-scanners">global-market-scanners</a>, files EARNINGS_LIQUIDITY.md, PEAD.md and earnings_liquidity.py (primary; the price data are not in the repository); the live piece '
    '<a href="' + B + '/2026/10/earnings-drift-and-piotroski-work-only.html">Earnings drift and Piotroski F-score: both work in thinly traded stocks</a>. '
    'India (primary where read in full): Krishnan and Rangan, NSE-IGIDR working paper on <a href="https://nsearchives.nseindia.com/research/content/NSE-IGIDR-WP4-14-15.pdf">insider trading and earnings announcements</a>; NSE-NYU working papers; '
    '<a href="https://journals.lib.vutbr.cz/index.php/trends/article/view/541">Gupta and Dhusia (2021)</a>; Sehgal and Bijoy (2015) via <a href="https://ideas.repec.org">IDEAS</a> (abstract only). '
    'Literature read as abstracts on IDEAS (secondary): Dou, Truong and Veeraraghavan (2016); Chen (2023); Forbes and Giannopoulos (2015); Forner and Sanabria (2010); Chen, Gao and Liu (2021); Shu and Tan (2022); Du et al. (2023); Feng et al. (2022); Kasahara and Zhong (2022); G&eacute;rard (2012). '
    'Secondary review read in full: <a href="https://static.uni-graz.at/fileadmin/sowi/Working_Paper/2020-04_Fink.pdf">Fink (2020)</a>. '
    'Excerpt only, no figures used (secondary): Guo and Holmes (2022); Hung, Li and Wang (HKUST working paper 2015-17); Martineau (2022); Santana, Black and de Lima (2022); Hew et al. (1996); Liu, Strong and Xu (2003); Jinushi (2023); Hong, Lee and Swaminathan (2003); '
    '<a href="https://anderson-review.ucla.edu/is-post-earnings-announcement-drift-a-thing-again">UCLA Anderson Review summary</a>. '
    'Shares, weighted means, standard errors and gaps computed by this blog. Analysed 26 November 2026. Not investment advice.')

RELATED = [(B + "/2026/10/earnings-drift-and-piotroski-work-only.html", "Earnings drift and Piotroski F-score: both work in thinly traded stocks")]

step(8, "writing the page")
build("Markets &middot; Stock signals", TITLE,
      "Post-earnings drift is not the same in every market. This blog&rsquo;s own data cover 12 markets with enough events; they show where the link to thin trading looks strongest, and where the sample is too small to say.",
      body, SOURCES, RELATED, str(OUT))
print(f"done in {time.time() - T0:.1f}s -> {OUT}")
