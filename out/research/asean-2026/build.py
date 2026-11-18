"""India-ASEAN goods trade FY2025-26 and the AITIGA review (to 18 Nov 2026).
Build from the repo root:  python3 out/research/asean-2026/build.py   (writes out/post-india-asean-trade-deficit-aitiga-review-nov-2026.html). Analysed 18 November 2026."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-india-asean-trade-deficit-aitiga-review-nov-2026.html"
B = "https://blog.vertistratsolution.com"

# ---- Official, FY2025-26 (PIB 24 Sep 2026; BusinessLine 12 and 16 Nov citing official figures) ----
EXP, IMP, TRADE = 38.41, 89.96, 128.38
DEF = round(IMP - EXP, 2)
assert DEF == 51.55 and abs(EXP + IMP - TRADE) < 0.02   # reported total 128.38 is rounded from components
SHARE_PIB = 10.55
TOTAL_TRADE_IMPLIED = TRADE / (SHARE_PIB / 100)
assert round(TOTAL_TRADE_IMPLIED) == 1217
# ---- Rubix Data Sciences (ANI, 16 Nov 2026), secondary: FY2021-22 vs FY2025-26 ----
EXP22, EXP26, IMP22, IMP26 = 42.4, 38.5, 68.1, 90.0
DEF22, DEF26 = round(IMP22 - EXP22, 1), round(IMP26 - EXP26, 1)
assert DEF22 == 25.7 and DEF26 == 51.5
assert round(100 * (EXP26 / EXP22 - 1)) == -9 and round(100 * (IMP26 / IMP22 - 1)) == 32
DEF2010 = 7.0
assert round(DEF / DEF2010, 1) == 7.4
# Exports to Indonesia 8.5 -> 4.5, CAGR -15% over four years
IDN22, IDN26 = 8.5, 4.5
assert round(100 * ((IDN26 / IDN22) ** (1 / 4) - 1)) == -15 and round(100 * (IDN26 / IDN22 - 1)) == -47
# Import shares
IMP_SH = [("Singapore", 27), ("Indonesia", 23), ("Thailand", 18)]
assert sum(v for _, v in IMP_SH) == 68
OTHER_IMP = 100 - 68
EXP_TOP3 = 66     # Singapore, Malaysia, Vietnam share of exports
assert round(0.66 * EXP26, 1) == 25.4

TITLE = "India-ASEAN trade: $51.55 billion deficit in FY2026, goods pact review runs into 2027"
assert 55 <= len(TITLE) <= 90, len(TITLE)

top = top_line([
    ("$51.55 billion", " was India's goods deficit with ASEAN in FY2025-26: exports $38.41 billion, imports $89.96 billion, against a deficit of about $7 billion when the agreement began in 2010."),
    ("$8.5 to $4.5 billion", " is how exports to Indonesia fell between FY2021-22 and FY2025-26, a drop of 47%, while total exports to ASEAN fell 9% and imports rose 32%."),
    ("January 2027", " is the date of the next Joint Committee meeting on the review of the trade-in-goods agreement, after the 15th round in Jakarta on 6 to 9 October ended with a call to speed up pending chapters."),
])

s1 = insight(
    "The ASEAN goods deficit doubled from $25.7 billion in FY2022 to $51.5 billion in FY2026",
    bars("India's deficit with ASEAN rose from about $7 billion in 2010 to $51.55 billion in FY2026",
         [("2010 (when the agreement began)", DEF2010), ("FY2021-22", DEF22), ("FY2025-26", DEF)], accent="FY2025-26", unit="$ billion",
         sub="Merchandise trade deficit with ASEAN, US$ billion. The FY2022 figure is from a private data report; the 2010 figure is as given by the Commerce Ministry sources.",
         source="PIB, 24 September 2026; The Hindu BusinessLine, 12 and 16 November 2026; Rubix Data Sciences via ANI, 16 November 2026.")
    + numbers(["Measure", "FY2021-22", "FY2025-26"],
              [["Exports to ASEAN, $ billion", f"{EXP22}", f"{EXP} (official); {EXP26} (Rubix)"], ["Imports from ASEAN, $ billion", f"{IMP22}", f"{IMP} (official); {IMP26} (Rubix)"],
               ["Deficit, $ billion", f"{DEF22}", f"{DEF} (official); {DEF26} (Rubix)"], ["Total trade", "&ndash;", f"{TRADE} billion, 10.55% of India&rsquo;s trade (PIB); about 11% (Rubix)"]]),
    "The deficit is 7.4 times its 2010 level while exports fell 9% from FY2022, so the gap grew because imports rose 32% and exports did not follow, in a period when the agreement was in force throughout.",
    "The Commerce Ministry should publish the goods deficit with ASEAN by tariff line and country for each year since 2010, so that the review can be tested against what moved.",
    "deficit")

s2 = insight(
    "Three countries supply 68% of India's imports from ASEAN; exports to Indonesia halved",
    bars("Singapore, Indonesia and Thailand supply 68% of India's imports from ASEAN",
         IMP_SH + [("All other ASEAN members", OTHER_IMP)], accent="Singapore", unit="%",
         sub="Share of India's FY2025-26 merchandise imports from ASEAN. Exports to Singapore, Malaysia and Vietnam are 66% of exports; exports to Indonesia fell from $8.5 billion to $4.5 billion.",
         source="Rubix Data Sciences via ANI, 16 November 2026 (secondary).")
    + numbers(["Measure", "Value"],
              [["Imports: Singapore, Indonesia, Thailand", "27%, 23%, 18%"], ["Exports: Singapore, Malaysia, Vietnam", "66% of exports, about $25.4 billion on the Rubix total"], ["Exports to Indonesia", "$8.5 billion to $4.5 billion, -15% a year over four years"],
               ["Singapore and Indonesia", "47% of India's total merchandise trade with the bloc"]]),
    "The trade is concentrated on both sides in a few countries, which means the deficit depends on three suppliers and a drop in one market, Indonesia, that accounts for $4 billion of lost exports.",
    "The Commerce Ministry should publish a table of India's top 20 exports and imports with each ASEAN country with the tariff paid, so that the review can target the lines that matter.",
    "countries")

s3 = insight(
    "The goods pact review was due in October 2025 and next meets in January 2027",
    flow([("2010", "The ASEAN-India Trade in Goods Agreement (AITIGA) comes into force with a deficit of about $7 billion."),
          ("October 2025", "The review was expected to conclude at the ASEAN-India summit but differences stopped it."),
          ("September 2026", "ASEAN formally notes India's position that the review must produce a &ldquo;balanced framework&rdquo;."),
          ("6 to 9 Oct 2026", "The 15th Joint Committee in Jakarta directs sub-committees to speed up pending chapters; three of eight sub-committees met: legal, national treatment on market access, and rules of origin.", True),
          ("16 to 17 Nov 2026", "The 23rd ASEAN-India Summit in Manila; The Hindu BusinessLine reported before it that a breakthrough was unlikely."),
          ("January 2027", "The next Joint Committee meeting, in India.")]),
    "The review is stuck on market access, rules of origin and the extent of concessions, and ASEAN is also seeking more market access, so a deal in which India gains balance and gives nothing is unlikely.",
    "The Commerce Ministry should publish the list of tariff lines it wants changed and the lines ASEAN has asked of India, so the trade-offs can be debated before the January meeting.",
    "review")

fixes = '''<h2 class="gb-h2" id="fixes">What would fix this</h2>
<ol>
<li><b>Ministry of Commerce and Industry:</b> publish India-ASEAN trade by tariff line and country each year since 2010.</li>
<li><b>Ministry of Commerce and Industry:</b> publish the lines India seeks to change in the review and the lines ASEAN seeks, before the January 2027 meeting.</li>
<li><b>DGFT and Customs:</b> publish the share of ASEAN imports that claim AITIGA preference, to test the transhipment concern.</li>
</ol>
<p>These are proposals from this blog, not recommendations any agency has adopted.</p>
'''
method = '''<details class="xv-n"><summary>Method and definitions</summary><ul>
<li>Official trade figures are from the Commerce Ministry as reported by PIB and The Hindu BusinessLine; deficits are imports minus exports in US dollars.</li>
<li>FY2021-22 values, country shares and the Indonesia series are from a Rubix Data Sciences report summarised by ANI, a secondary source; its FY2026 values differ slightly from the official ones.</li>
<li>The Indonesia annual rate is the compound rate over four years.</li></ul></details>
'''
gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary><ul>
<li>The outcome of the 17 November summit on trade: pre-summit reports said a breakthrough was unlikely; no outcome on the review was read.</li>
<li>A conflict on the deficit: Mint says imports exceed exports by more than $45 billion, while the official figures give $51.55 billion.</li>
<li>The 2010 deficit: sources say about $7 billion or $6 to 7 billion.</li>
<li>Exports in January to May 2026: Gateway House says they rose 56% to $23 billion; this was not checked.</li>
<li>Why exports to Indonesia fell.</li>
</ul></details>
'''
body = STYLE + top + s1 + s2 + s3 + fixes + method + gaps
SOURCES = ('<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2314556&amp;reg=48&amp;lang=2">PIB, 24 September 2026</a> (trade of $128.38 billion; 10.55%); '
  '<a href="https://www.thehindubusinessline.com/economy/modi-to-focus-on-strategic-ties-at-asean-india-summit-as-trade-talks-drag-on/article71694249.ece">The Hindu BusinessLine, 12 November 2026</a> (exports, imports, deficit); '
  '<a href="https://www.thehindubusinessline.com/economy/trade-imbalance-defence-maritime-ties-to-top-modis-agenda-at-asean-meetings/article71707145.ece">The Hindu BusinessLine, 16 November 2026</a>; '
  '<a href="https://www.thehindubusinessline.com/economy/india-asean-summit-unlikely-to-break-deadlock-on-trade-pact-review/article71670146.ece">The Hindu BusinessLine, 5 November 2026</a> (review timeline); '
  '<a href="https://www.pib.gov.in/PressReleasePage.aspx?PRID=2321209">PIB, 9 October 2026</a> (15th Joint Committee); '
  '<a href="https://www.aninews.in/news/business/indias-asean-trade-reaches-usd-1284-billion-in-fy26-but-share-in-overall-trade-remains-stagnant-report20261116175640">ANI, 16 November 2026</a> (Rubix Data Sciences; secondary); '
  '<a href="https://www.livemint.com/news/world/can-india-bridge-trade-gap-with-southeast-asia-as-pm-modi-heads-to-manila-for-asean-amid-china-s-growing-clout-11794578664909.html">Mint, 13 November 2026</a>; '
  '<a href="https://www.drishtiias.com/current-affairs-news-analysis-editorials/news-analysis/18-11-2026">Drishti IAS, 18 November 2026</a>. Computed by this blog. Analysed 18 November 2026.')
RELATED = [(f"{B}/2026/08/what-tepa-actually-opens-efta-goods.html", "India-EFTA TEPA: in force since 1 October 2025, with a $100 billion commitment"),
           (f"{B}/2026/09/the-50-tariff-and-234-one-untangling.html", "US tariffs on Indian goods: from 50% in August 2025 to 10% since 24 July 2026"),
           (f"{B}/2026/08/priority-export-destinations-by-growth.html", "India's 12 growth export chapters: top destinations and PLI coverage, FY2025-26")]
build("Trade &middot; Asia", TITLE, "India's goods deficit with ASEAN reached $51.55 billion in FY2025-26, and the review of the trade-in-goods pact, due in October 2025, next meets in January 2027.", body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE))
