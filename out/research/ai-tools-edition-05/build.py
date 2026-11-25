"""AI tools tracker, Edition 05 (25 Nov 2026): the launch board for items not in Edition 04, rebuilt from the
24 Nov tracker dashboard after a line-by-line fact-check on 25 Nov 2026.
Build from the repo root:  python3 out/research/ai-tools-edition-05/build.py   (writes out/post-ai-tools-edition-05.html)
Every figure is from the source named beside it, or computed here with an assert. Items the fact-check could not
support are left out and listed in the post. Sources are search-result excerpts, not opened pages."""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "tools/postbuild"))
from buildpost import build  # noqa: E402
from exec_viz import STYLE, bars, flow, insight, numbers, top_line  # noqa: E402

OUT = ROOT / "out/post-ai-tools-edition-05.html"
B = "https://blog.vertistratsolution.com"

# ---- funding rounds new to this edition (announcement dates, US$ million) ----
# Applied Compute: SiliconANGLE 3 Nov 2026 ($350M, $3.25B valuation, led by Elad Gil; "Series C" label not used by every source)
# LangChain: AI Weekly / unite.ai ($300M Series C, $3B valuation, CapitalG lead, 13 Nov)
# Model ML: tech.eu 17 Nov ($250M Series B, $1.5B valuation)
# Clark: The Next Web / dealroom (2 Nov, $11M seed, $16M total)  Phaze: The Next Web (4 Nov, $8.75M seed, a16z)
ROUNDS = [("Applied Compute", 350.0, "2&ndash;3 Nov, $3.25B valuation, led by Elad Gil"),
          ("LangChain", 300.0, "13 Nov, Series C at $3B, CapitalG lead"),
          ("Model ML", 250.0, "17 Nov, Series B at $1.5B"),
          ("Clark", 11.0, "2 Nov, seed, $16M raised in total"),
          ("Phaze", 8.75, "4 Nov, seed led by a16z")]
TOTAL = sum(v for _, v, _ in ROUNDS)
assert round(TOTAL, 2) == 919.75
TOP3 = sum(v for n, v, _ in ROUNDS[:3])
assert TOP3 == 900.0 and round(TOP3 / TOTAL * 100, 1) == 97.9
TRAVERSAL = 120.0            # $120M Series B at $1B, 3 Nov: already in Edition 04's funding strip, not counted above
NOOKS = 500.0                # $500M non-dilutive commitment from General Catalyst's Customer Value Fund (4 Nov): not equity, not counted
assert round(TOTAL + TRAVERSAL, 2) == 1039.75

# ---- model scores (Artificial Analysis Intelligence Index, effort as noted) and prices per 1M tokens ----
AA = [("Claude Fable 5.2 (max)", 65), ("GPT-6.2 Astra (max)", 62), ("GPT-6.2 Sol (max)", 57),
      ("Gemini 4 Hydrogen (xhigh)", 54), ("Gemini 4 Hydrogen (default)", 51), ("Qwen4-Max (xhigh)", 43)]
assert AA[0][1] - AA[-1][1] == 22 and AA[0][1] - AA[1][1] == 3
HYD_OUT, ASTRA_OUT, HYD_AA, ASTRA_AA = 7.50, 40.0, 51, 62
assert round(HYD_OUT / ASTRA_OUT * 100) == 19 and round(HYD_AA / ASTRA_AA * 100) == 82
PRICE_OUT = [("Claude Fable 5.2", 40.0, "one secondary source, score 65"), ("GPT-6.2 Astra", 40.0, "20% below GPT-6 Astra, score 62"),
             ("Kimi K3.1 Pro", 10.0, "one price comparison; Moonshot-reported benchmark"),
             ("Gemini 4 Hydrogen", 7.5, "score 51 by default"), ("Qwen4-Max", 4.5, "score 43; task cost $3.27 against $10.02 for its predecessor")]

# ---- copilot fusion (GitHub changelog 17 Nov 2026): 71.2% on Terminal-Bench 4.1, 5.4 points ahead, 88% cheaper than Fable 5.2 ----
FUSION, LEAD = 71.2, 5.4
RIVAL = round(FUSION - LEAD, 1)
assert RIVAL == 65.8

# ---- calendar of items in the 10 to 19 Nov slice ----
CAL = [("10 Nov", "Pixel Drop (Create My Widget, Gemini calls) and ElevenLabs Scribe v3 and v3 Live"),
       ("12 Nov", "Gemini 4 Hydrogen: $1.50/$7.50 per 1M tokens, 1M-token context"),
       ("13 Nov", "LangChain $300M Series C at $3B"),
       ("16 Nov", "Qwen4-Max: $1.50/$4.50, index score 43"),
       ("17 Nov", "GPT-6.2 Astra and Sol; GitHub changelog confirms Copilot Fusion Max at 71.2%; Model ML $250M Series B; Gemini Tasks free in six countries", True),
       ("19 Nov", "Gemini computer use reaches the Mac app")]
ON_17 = 4
assert ON_17 == 4

TITLE = "AI tools edition 05: five new rounds total $920 million; Copilot Fusion leads a benchmark"
assert 55 <= len(TITLE) <= 90, len(TITLE)

top = top_line([
    ("$920 million", f" is what five funding rounds announced between 2 and 17 November 2026 add up to (computed; $919.75M); three of them, Applied Compute, LangChain and Model ML, hold {TOP3 / TOTAL * 100:.0f}% of it."),
    ("71.2%", f" is the Terminal-Bench 4.1 resolution rate GitHub reports for Copilot Fusion Max, {LEAD} points above Opus 5.5 and Fable 5.2 (about {RIVAL}%), in GitHub&rsquo;s own changelog of 17 November."),
    ("65", " is Claude Fable 5.2&rsquo;s score on the Artificial Analysis index at max effort; GPT-6.2 Astra scores 62 and Gemini 4 Hydrogen 51 by default at about a fifth of Astra&rsquo;s output price."),
])

s1 = insight(
    "Three of five new rounds hold 98% of the $920 million",
    bars("Three rounds raised $900 million; Clark and Phaze together raised about $20 million",
         [(n, v, note, f"${v:g}M") for n, v, note in ROUNDS], accent=["Applied Compute", "LangChain", "Model ML"], unit="",
         sub="Funding rounds announced 2&ndash;17 November 2026, US$ million. Traversal&rsquo;s $120M Series B (3 Nov) was in Edition 04 and Nooks&rsquo; $500M is a non-dilutive commitment, so neither is counted.",
         source="SiliconANGLE; AI Weekly; tech.eu; The Next Web. Total computed here.")
    + numbers(["Company", "Amount ($M)", "Round and date", "Source type"],
              [["Applied Compute", "350", "Round at $3.25B valuation, 2&ndash;3 Nov; some reports call it Series C", "Press report"],
               ["LangChain", "300", "Series C at $3B, 13 Nov, CapitalG lead", "Press report"],
               ["Model ML", "250", "Series B at $1.5B, 17 Nov", "Press report"],
               ["Clark", "11", "Seed, 2 Nov; $16M raised in total", "Press report"],
               ["Phaze", "8.75", "Seed, 4 Nov, a16z lead", "Press report"],
               ["Total of the five", "919.75", "Computed", ""],
               ["Not counted: Traversal", "120", "Series B at $1B, 3 Nov, in Edition 04", "Press report"],
               ["Not counted: Nooks", "500", "Non-dilutive commitment from General Catalyst&rsquo;s Customer Value Fund, 4 Nov", "Press report"]]),
    f"The three large rounds, all for agent and enterprise-AI infrastructure, are {TOP3 / TOTAL * 100:.0f}% of the total, so the other two seeds move the sum by about $20 million.",
    "Each company&rsquo;s own announcement should state whether the amount is equity, debt or a commitment, since one of this month&rsquo;s headline numbers (Nooks) is not equity.",
    "funding")

s2 = insight(
    "Fable 5.2 leads the index at 65, three points ahead of GPT-6.2 Astra",
    bars("Six model settings span 22 index points, from Qwen4-Max at 43 to Fable 5.2 at 65",
         [(n, v) for n, v in AA], accent="Claude Fable 5.2 (max)", unit="", vmax=70,
         sub="Artificial Analysis Intelligence Index, effort setting in brackets. Scores at different effort levels are not strictly comparable.",
         source="Artificial Analysis model and release pages, as returned by search on 25 November 2026.")
    + numbers(["Model", "Index score", "Effort", "Note"],
              [["Claude Fable 5.2", "65 (62 at high)", "max", "Date of release not confirmed on a primary page"],
               ["GPT-6.2 Astra", "62", "max", "Released 17 Nov"],
               ["GPT-6.2 Sol", "57", "max", "Released 17 Nov"],
               ["Gemini 4 Hydrogen", "51 default, 54", "default, xhigh", "Released 12 Nov"],
               ["Qwen4-Max", "43", "xhigh", "Released 16 Nov; closed weights"]]),
    "The top two are three points apart and the range from first to last is 22 points, but the Hydrogen and Qwen4-Max rows use lower effort settings than the top two.",
    "Anyone comparing models should read the effort setting beside each score, because the same model can move several points between settings.",
    "index")

s3 = insight(
    "Hydrogen scores 82% of Astra's index at 19% of its output price",
    bars("Output prices run from $4.50 to $40 per 1M tokens across five recent models",
         [(n, v, note, f"${v:g}") for n, v, note in PRICE_OUT], accent="Gemini 4 Hydrogen", unit="",
         sub="US$ per 1M output tokens as reported. Fable 5.2 and Kimi figures each rest on one source; the index scores in the notes use different effort settings.",
         source="Artificial Analysis; Towards AI (Fable 5.2 price); a Kimi price comparison; Alibaba pricing as listed by Artificial Analysis.")
    + numbers(["Comparison", "Value", "Computed from"],
              [["Hydrogen output price against Astra", f"{HYD_OUT / ASTRA_OUT * 100:.0f}%", "$7.50 / $40"],
               ["Hydrogen default index against Astra max", f"{HYD_AA / ASTRA_AA * 100:.0f}%", "51 / 62"],
               ["Fable 5.2 and Astra output price", "Both $40", "Fable price single-source"]]),
    f"Hydrogen&rsquo;s default setting reaches {HYD_AA / ASTRA_AA * 100:.0f}% of Astra&rsquo;s score for {HYD_OUT / ASTRA_OUT * 100:.0f}% of its output price, though the two scores use different effort settings and per-task cost depends on how many tokens each model spends.",
    "Buyers should compare cost per finished task, which Artificial Analysis publishes, not the per-token price alone.",
    "price")

s4 = insight(
    "Four of the ten items in the 10 to 19 November slice landed on 17 November",
    flow(CAL),
    "The 17 November cluster, a model launch, a benchmark changelog, a funding round and a consumer rollout, falls inside a single working day.",
    "A weekly tracker should date each item to its primary announcement, since a cluster like this is easy to blur into one week&rsquo;s news.",
    "calendar")

# ---- carryovers and fixes ----
carry = '''<h2 class="gb-h2" id="carryover">What changed for items in earlier editions</h2>
<p>Edition 04 (9 November) and Edition 03 (31 July) already carry these. The new facts, with the source of each:</p>
<ul>
<li><b>Copilot Fusion Max.</b> Edition 04 listed its benchmark result as single-source. GitHub&rsquo;s own changelog of 17 November now gives 71.2% on Terminal-Bench 4.1, 5.4 points ahead of Opus 5.5 and Fable 5.2, at 88% less cost than Fable 5.2, and lists it on public leaderboards hosted by Stanford, Harbor and the Laude Institute. The result is still GitHub&rsquo;s own measurement.</li>
<li><b>Traversal.</b> The $120M Series B from Edition 04 is at a $1B valuation, co-led by Kleiner Perkins, Redpoint and Khosla.</li>
<li><b>Kimi K3.1 Pro.</b> Released 23 October 2026, with weights due by 4 November. Moonshot reports 65.7% on Terminal-Bench 4.0, against 66.4% for Claude Opus 5.5 (vendor-reported; this is the 4.0 version, not 4.1).</li>
<li><b>Graphify.</b> Edition 04 read 144,768 stars from GitHub&rsquo;s API on 9 November. Y Combinator S26 is confirmed by Augment Code coverage of June 2026. Star counts quoted elsewhere run from 58K to 135K, so none is repeated here, and two GitHub repositories appear in results, so check which one a count belongs to.</li>
<li><b>Ruflo.</b> Edition 04 read 81,324 stars on 9 November. The project was renamed from Claude Flow in February 2026 (npm package and CLI keep the claude-flow name). A project README reports 12.52M ecosystem npm downloads over the 12 months to 4 October 2026.</li>
<li><b>Kolibri</b> (Edition 03). Konecta launched it on 13&ndash;16 June 2026; the 80% pre-built figure is the company&rsquo;s.</li>
</ul>
'''

board = '''<h2 class="gb-h2" id="board">The rest of this edition&rsquo;s launch board</h2>
''' + numbers(["Item", "Date", "What it is", "Qualifier"],
    [["SWE-2 Flash (Cognition)", "4 Nov", "Fast coding model in Devin; 24.0 on FrontierCode 2.0 against 23.8 for SWE-2; about one-fifth the price of SWE-2", "Vendor-reported; free through 30 Nov"],
     ["OpenCode", "Active", "Open-source terminal coding agent, MIT", "Over 208,000 stars on its site, undated"],
     ["Nooks &ldquo;Node&rdquo;", "4 Nov", "AI assistant for sales reps; reps approve each message", "General availability early 2027; $500M is not equity"],
     ["Gemini computer use (Mac)", "19 Nov", "Operates native apps and browses in the background", "US English; AI Plus, Pro or Ultra; Apple silicon, macOS 15 or later"],
     ["Gemini Tasks", "17 Nov", "Calls businesses, books appointments, makes purchases via the Agent Payments Protocol", "Free in the US, Japan, Korea, Canada, Australia and India"],
     ["November Pixel Drop", "10 Nov", "Pixel Solver, Create My Widget, Gemini calls", "Features differ by Pixel model and region"],
     ["ElevenLabs Scribe v3 and v3 Live", "10 Nov", "Batch and real-time speech-to-text, 102 and 90+ languages", "27% and 43% fewer errors, company-reported"]],
    "Show the other launches")

left_out = '''<h2 class="gb-h2" id="leftout">Left out because the fact-check could not support it</h2>
<p>The 24 November tracker dashboard carried claims that did not survive a line-by-line check on 25 November, so they are not repeated here: a model called &ldquo;Kimi K3.1 Pro Prime&rdquo; with a 59.7% Terminal-Bench 4.1 score (no such product found); Ruflo&rsquo;s &ldquo;121M downloads&rdquo; and &ldquo;98 agents&rdquo;; SWE-2 Flash&rsquo;s $0.10/$0.50 price and 4 December end date; a $8.24B and 117-round November funding total; OpenCode&rsquo;s 209,405 stars and index score of 53.6; Graphify&rsquo;s Apache-2.0 licence and ROSS rank; and Copilot&rsquo;s reported addition of GPT-6.2 and MAI Code 2. The dashboard itself was corrected the same day.</p>
'''

gaps = '''<details class="xv-n"><summary>What this piece could not establish</summary>
<ul>
<li>Every figure was read from search-result excerpts, several of them from aggregator sites; no source page was opened. Benchmark scores from vendors (Copilot Fusion Max, SWE-2 Flash, Kimi, Scribe) were not reproduced.</li>
<li>Claude Fable 5.2&rsquo;s release date, and its $8/$40 price: the index score is on Artificial Analysis, the price comes from one secondary article.</li>
<li>Gemini 4 Carbon and Neon: both exist on Artificial Analysis, but their release dates were not confirmed, so they are not on the board.</li>
<li>Whether the Applied Compute round is a Series C: some reports use the label and others call it a growth round. Investor lists differ for Clark and Applied Compute.</li>
<li>GitHub star counts were not re-read this edition; the 9 November counts in Edition 04 are the latest verified ones.</li>
<li>Who among the five rounds&rsquo; investors is new to the company: this piece lists leads only.</li>
</ul></details>
'''

body = STYLE + top + s1 + s2 + s3 + s4 + carry + board + left_out + gaps

SOURCES = (
    '<a href="https://siliconangle.com/2026/11/03/ai-cloud-startup-applied-compute-raises-350m-after-reaching-key-revenue-milestone/">SiliconANGLE, 3 November 2026</a> (Applied Compute); '
    '<a href="https://aiweekly.co/alerts/langchain-hits-3b-valuation-on-300m-series-c-led-by-capitalg">AI Weekly</a> (LangChain); '
    '<a href="https://tech.eu/2026/11/17/model-ml-hits-15b-valuation-with-250m-raise-just-18-months-after-emerging-from-stealth/">tech.eu, 17 November 2026</a> (Model ML); '
    '<a href="https://thenextweb.com/news/clark-11m-seed-clerks-ai-audit-employees">The Next Web</a> (Clark), '
    '<a href="https://thenextweb.com/news/phaze-8-75m-seed-a16z-remote-computers-ai-agents">The Next Web</a> (Phaze) and '
    '<a href="https://thenextweb.com/news/traversal-120m-series-b-1b-valuation-ai-sre">The Next Web</a> (Traversal); '
    '<a href="https://www.citybiz.co/?p=929354">citybiz</a> (Nooks); '
    '<a href="https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models">GitHub changelog, 17 November 2026</a> (Copilot Fusion); '
    '<a href="https://artificialanalysis.ai/articles/openai-has-the-2-model-in-the-intelligence-index-with-the-release-of-gpt-6-2-astra-and-gpt-6-2-sol">Artificial Analysis, 17 November 2026</a> (GPT-6.2), '
    '<a href="https://artificialanalysis.ai/models/releases/claude-fable-5-2">Fable 5.2</a>, '
    '<a href="https://artificialanalysis.ai/ko/models/qwen4-max">Qwen4-Max</a>; '
    '<a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/">Google, Gemini 4 Hydrogen</a>; '
    '<a href="https://cognition.com/blog/swe-2-flash">Cognition, SWE-2 Flash</a>; '
    '<a href="https://kimi.com/blog/kimi-k3-1-pro">Moonshot, Kimi K3.1 Pro</a>; '
    '<a href="https://9to5google.com/2026/11/19/gemini-mac-computer-use/">9to5Google, 19 November 2026</a>, '
    '<a href="https://blog.google/innovation-and-ai/products/gemini-app/tasks-in-gemini-free-new-features/">Google, Gemini Tasks</a>, '
    '<a href="https://9to5google.com/2026/11/10/november-2026-pixel-feature-drop/">9to5Google, Pixel Drop</a>; '
    '<a href="https://elevenlabs.io/blog/scribe-v3">ElevenLabs, Scribe v3</a>; '
    '<a href="https://github.com/ruvnet/ruflo">Ruflo</a>, <a href="https://github.com/Graphify-Labs/graphify">Graphify</a>, <a href="https://opencode.ai/en">OpenCode</a>, '
    '<a href="https://konecta.com/solutions/kolibri-ai-platform?hsLang=en">Konecta, Kolibri</a>. '
    'Sums, ratios and shares computed by this blog. Checked 25 November 2026.')

RELATED = [
    (f"{B}/2026/11/ai-tools-edition-04-deepseek-put-its.html", "AI tools edition 04: DeepSeek's agent and inference engine drew 47,000 GitHub stars"),
    (f"{B}/2026/07/ai-high-demand-launch-tracker.html", "AI tools tracker edition 03: wider sources and a 98,000-star repository it missed"),
    (f"{B}/2026/11/growth-71-against-inflation-609-numbers_0897023343.html", "Growth 7.1% against inflation 6.09%: the numbers before the RBI's 2-4 December meeting"),
]

build("AI Tracker &middot; Edition 05", TITLE,
      "Edition 05 logs what is new since 9 November: five funding rounds, GitHub&rsquo;s confirmed Copilot Fusion result, the 17 November model cluster and the earlier items whose facts changed.",
      body, SOURCES, RELATED, str(OUT))
print("wrote", OUT.relative_to(ROOT), len(TITLE), "chars in title")
