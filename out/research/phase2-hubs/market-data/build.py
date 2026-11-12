"""Hub post: market-data tools (public repositories).
Build (from repo root): PYTHONPATH=tools/postbuild python3 out/research/phase2-hubs/market-data/build.py

Replaces seven separate "How to use <repo>" guides (four live, three drafts; see hubs.json key "market-data").
Every fact, command and figure below is taken from those guides; dates are the guides' own run dates.
The five-toolkits guide also covered four non-finance repos; they are not in this hub's repo list and are not linked."""
import html
import sys
sys.path.insert(0, 'tools/postbuild')
from buildpost import build

OUT = 'out/post-hub-market-data.html'
GH = 'https://github.com/herrrickshaw/'

PRE_STYLE = ('overflow-x:auto;background:#f8f9fa;border:1px solid #dee2e6;border-radius:8px;'
             'padding:.75rem 1rem;font-size:.8em;line-height:1.45;white-space:pre')
H3_STYLE = "font-family:-apple-system,'Segoe UI',sans-serif;font-weight:700;font-size:1.12em;margin:1.8rem 0 .5rem"
NOT_ADVICE = "Not investment advice: this is research and education material; nothing here is a recommendation to buy or sell anything."


def code(text):
    return f'<pre style="{PRE_STYLE}"><code>{html.escape(text.strip(chr(10)), quote=False)}</code></pre>'


def repo_link(repo):
    return f'<a href="{GH}{repo}">github.com/herrrickshaw/{repo}</a>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def tool(anchor, title, repo, paras, cmd_intro, cmd, cmd_out, limit):
    ps = "".join(f"<p>{p}</p>\n" for p in paras)
    return (f'<h3 id="{anchor}" style="{H3_STYLE}">{title}</h3>\n{ps}'
            f'<p><strong>Start here.</strong> {cmd_intro}</p>\n{code(cmd)}\n'
            f'<p>{cmd_out}</p>\n'
            f'<p><strong>Code:</strong> {repo_link(repo)}</p>\n'
            f'<p><strong>Main limitation.</strong> {limit}</p>\n')


TOOLS = [
    dict(anchor="tickers", repo="global-ticker-universe",
         title="global-ticker-universe: exchange-qualified symbols for 34 markets",
         what="A committed JSON list of Yahoo-style ticker symbols per market, with a small Python helper.",
         when="You need the list of symbols for a country before you download prices or fundamentals.",
         paras=[
             "The repository stores one file, <code>data/global_universe.json</code>, with Yahoo-Finance-style symbols per market, and a helper module, <code>global_tickers.py</code>. You ask for one market, several, or all; <code>tickers_for('JP')</code> returns the Japan list. Symbols carry their exchange: India comes as RELIANCE.NS or .BO, Japan as 7203.T, Germany as SAP.DE. A flat CSV with market, exchange and symbol columns is also included.",
             "In the guide&rsquo;s run of 19 October 2026, the helper loaded 74,239 symbols across 34 markets, all unique, and the 16 bundled tests passed. It needs no API key, network or extra package. It holds symbols and names only: no prices or fundamentals.",
         ],
         cmd_intro="Print the market summary table.",
         cmd="python3 global_tickers.py",
         out="A table of market code, exchange and ticker count, then the first five tickers for India, the US and Japan.",
         limit="It is a snapshot, and the README and the committed JSON disagree: the README says the universe was widened to 75,815 symbols, while the JSON loaded in the guide&rsquo;s run gives 74,239. Treat them as different snapshots. Some markets are small samples, China is flagged as a coverage gap, US symbols carry no exchange, and symbols are not checked for being tradable today."),
    dict(anchor="fundamentals", repo="colab-market-fundamentals",
         title="colab-market-fundamentals: annual company financials for 20 markets, in Colab",
         what="A Colab notebook that collects about five years of annual fundamentals per company through yfinance, with checkpoints and resume.",
         when="You want a free table of revenue, profit, assets, debt and cash flow for many companies.",
         paras=[
             "You open <code>collect.ipynb</code> in Google Colab, press Run all, and download <code>fundamentals.zip</code>. The notebook reads <code>tickers.csv</code> (32,590 tickers across 20 market codes), fetches the income statement, balance sheet and cash flow for each ticker, and writes one parquet file per market, saving every three minutes. It probes first for a Yahoo block, retries, and can resume from an uploaded zip. The US set is skipped by default.",
             "Each row is one company and one fiscal year, with 13 columns, including the fields needed for a Piotroski-style score. In the guide&rsquo;s local test on 19 October 2026, three German companies returned 12 rows (four fiscal years each).",
         ],
         cmd_intro="Test one market before a long run (cell 4 of the notebook).",
         cmd="collect_market('DE', ['SAP.DE','SIE.DE','ALV.DE'], workers=3)",
         out="&lsquo;DE: 3 names with data&rsquo;. A full Run all prints progress per market and writes <code>/content/fundamentals.zip</code> every three minutes.",
         limit="The data comes from Yahoo Finance: third-party, unaudited, and subject to Yahoo&rsquo;s terms. The &lsquo;filed&rsquo; column is fiscal year end plus 90 days, not the real filing date, so it is not safe for point-in-time backtests. Yahoo blocks many datacentre IPs, and a full run of about 30,000 tickers was not timed. Banks and insurers return only some columns."),
    dict(anchor="correlations", repo="market-correlation-matrices",
         title="market-correlation-matrices: how closely stocks move together in six markets",
         what="Ready-made correlation matrices of daily returns for India, the US, Japan, Korea, China and Europe, with top pairs and summaries.",
         when="You want to compare how tightly stocks co-move across markets, or find a stock&rsquo;s closest peers.",
         paras=[
             "For each market the repo stores three files: a dense correlation matrix (float16, with a symbol list), a table of pairs with an absolute correlation of at least 0.6, and a small summary. Correlation is the Pearson measure on daily log returns over the last 252 trading days, using the 3,000 most traded symbols. Reading the committed files needs numpy, pandas and pyarrow, no key.",
             "Rebuilding needs a DuckDB price warehouse that is not in the repo. The guide rebuilt the matrices on 23 October 2026 against a local copy of the author&rsquo;s warehouse, with a local patch for incomplete trading days; in that rebuild Korea and India were the most tightly co-moving markets and Europe the lowest. The committed snapshot&rsquo;s windows end in June and July 2026.",
         ],
         cmd_intro="Read the per-market summaries.",
         cmd='''import json
for m in ['IN','US','JP','KR','CN','EU']:
    s = json.load(open(f'data/{m}/summary.json'))
    print(m, s['window'], s['symbols'], s['mean_pairwise_corr'])''',
         out="One line per market with the window dates, symbol count and mean correlation.",
         limit="Windows are not aligned across markets (China&rsquo;s data stops on 1 July 2026), so comparisons mix dates. The unmodified script counts thin, partial trading days as full sessions, which changed the Europe result in the guide&rsquo;s run. The highest pairs are often one company listed twice, and the India and US sets include ETFs and trusts. It is descriptive, not a trading signal."),
    dict(anchor="finmodel", repo="financial-analysis-toolkit-public",
         title="financial-analysis-toolkit-public (finmodel): three-statement, DCF, LBO and comparables",
         what="A command-line engine for three-statement models, discounted cash flow, leveraged buyouts and comparable-company analysis.",
         when="You want an auditable valuation model whose balance sheet balances, from a JSON input file.",
         paras=[
             "The repo ships <code>finmodel</code>, which needs Python 3.10 or newer and only openpyxl at runtime. It runs four engines from JSON inputs: <code>three-statement</code>, <code>dcf</code>, <code>lbo</code> and <code>comps</code>. Add <code>--xlsx out/model.xlsx</code> for a workbook with live formulas. The bundled examples use case-study data from CFI, so their numbers are illustrative.",
             "The guide&rsquo;s demo of 18 October 2026 reported 670 tests passing, but on the author&rsquo;s main repo; the public mirror ships the same engines, and its DCF and LBO examples gave identical headline numbers.",
         ],
         cmd_intro="Install, then run the DCF example with a sensitivity grid.",
         cmd='''pip install -e '.[test]'
finmodel dcf examples/cfi_dcf.json --sensitivity''',
         out="EV=462,983, equity per share 33.63, upside 34.5%, IRR 26.3%, at a 12% discount rate and 3% perpetual growth, plus a WACC-by-growth grid. Case-study figures, illustrative only.",
         limit="A DCF that uses levered tax double counts the interest shield, so run <code>dcf-diagnostics</code> first. Bad input paths give a raw Python traceback. Running pytest rewrites timestamps in <code>catalog/*.json</code>, so run it on a copy."),
    dict(anchor="brief", repo="market-brief-base",
         title="market-brief-base: a one-file daily brief for 30 large caps",
         what="One Python file that fetches settled closes for 15 Indian and 15 US large caps and writes an HTML brief with trend and Darvas-box labels.",
         when="You follow a few large caps and want a dated daily summary, or a template for a report that fails loudly.",
         paras=[
             "For 30 hardcoded stocks, <code>brief.py</code> reports the last settled close with its bar date, the day change, a 50/200-day moving-average cross label and a Darvas box state (IN_BOX, BREAKOUT_BUY, BREAKDOWN_SELL or NO_DATA), then writes a self-contained HTML file and can optionally email it. Data comes from yfinance, with pandas and yfinance versions pinned.",
             "Its failure rules are written down: a missing price is never treated as zero, a failed market is named in the output, and if nothing fetches the script exits with an error rather than sending an empty brief. An offline self-test checks the signal logic.",
         ],
         cmd_intro="Produce today&rsquo;s brief (after <code>pip install -r requirements.txt</code>, or let <code>./run.sh</code> build the environment).",
         cmd="python brief.py --out brief.html",
         out="&lsquo;India: 15/15 priced&rsquo;, &lsquo;US: 15/15 priced&rsquo;, then &lsquo;wrote brief.html&rsquo;. The worked example below shows a full run.",
         limit="The labels are mechanical screen states, not recommendations. It covers only 30 stocks, with settled daily bars and no fundamentals or news. Email, the GitHub Actions schedule and the launchd job were not tested in the guide."),
    dict(anchor="kdb", repo="global-market-kdb",
         title="global-market-kdb: a cross-sectional signal study in kdb+/q, checked against Python",
         what="A kdb+/q port of a twelve-signal equity study with Newey-West, FDR, Fama-MacBeth, cost-adjusted spreads, Deflated Sharpe and walk-forward tests.",
         when="You want to learn q from a complete, tested study, or validate a q port against a Python reference.",
         paras=[
             "The study builds a date-partitioned database of daily bars, computes twelve signals (reversal, RSI, momentum, trend, 52-week high, low volatility, illiquidity and others) at 5, 10, 21 and 63-day horizons, and runs the statistics. The Python original is kept in <code>python/upstream/</code> as the reference, and <code>python/parity.py</code> runs both and compares every output table row by row.",
             "It needs q from KDB-X Community Edition (free but licensed) and Python 3.10 or newer. In the guide&rsquo;s run of 5 November 2026 on the bundled synthetic sample, all six output tables matched Python and pytest gave 10 passed. Every signal was rated NOISE, which is the right answer for random data.",
         ],
         cmd_intro="Run the parity check on the synthetic sample.",
         cmd=".venv/bin/python python/parity.py",
         out="It loads the CSV into a q database, runs both studies and prints a comparison table ending in PASS (about 10 seconds in the guide&rsquo;s run).",
         limit="You need a KDB-X licence to run it. The bundled data is synthetic, so no number it prints says anything about any market. The README&rsquo;s real-data parity rows were not re-run in the guide."),
    dict(anchor="events", repo="event-driven-stock-analysis",
         title="event-driven-stock-analysis: a portfolio-monitor design with a small event bus",
         what="An architecture for a multi-market portfolio monitor, a FastAPI skeleton, an in-process event bus and sample price files.",
         when="You are designing an event-driven finance back end and want a documented starting point.",
         paras=[
             "This is a design-first repository. The README and its architecture documents describe a portfolio monitor with risk metrics, rebalancing and alerts. The code that exists is a FastAPI backend with portfolio, risk, rebalance, alert and report routers, and an <code>EventBus</code> with a <code>PortfolioMonitor</code> class. The sample data is compressed OHLCV files for eight markets.",
             "In the guide&rsquo;s run of 4 November 2026, feeding the Korea sample through the bus at a 1.5% move threshold produced 20 price-move events for one ticker. The sample prices turned out to be synthetic: tickers are named like KOREA_STOCK_0000 and the dates are in 2023.",
         ],
         cmd_intro="Start the API with SQLite from <code>backend/</code>, then open <code>/docs</code>. Install FastAPI, uvicorn and the other packages first, plus pytz and psycopg, which <code>requirements.txt</code> leaves out.",
         cmd="DATABASE_URL=sqlite:///./test.db uvicorn main:app --reload",
         out="The app logs &lsquo;Database initialized&rsquo; and &lsquo;API routers registered&rsquo;; GET / returns the app name and version 0.1.0.",
         limit="Treat it as a design plus a skeleton. In the guide&rsquo;s run pytest gave 0 passed and 6 errors (missing fixtures, and two packages absent from <code>requirements.txt</code>), <code>/health</code> returned 404, and the pinned package versions are old. The README&rsquo;s target returns and Sharpe ratios are design goals, not results."),
]

assert len(TOOLS) == 7

stats = '''<div class="gb-stats">
<div class="gb-stat"><b>74,239</b><span>ticker symbols across 34 markets in the committed universe file (run 19 Oct 2026)</span></div>
<div class="gb-stat"><b>32,590</b><span>tickers in 20 market codes that the Colab fundamentals collector reads</span></div>
<div class="gb-stat"><b>6</b><span>markets with ready-made stock correlation matrices</span></div>
<div class="gb-stat"><b>6 of 6</b><span>kdb+/q output tables matching the Python original on synthetic data (5 Nov 2026)</span></div>
</div>'''

intro = f'''<p>Most stock-market research starts with the same chores: a list of symbols, a table of company financials, a sense of which stocks move together, and a model you can audit. The seven open-source repositories below each handle one of those chores, from a ticker list for 34 markets to a valuation engine, a one-file daily brief and a signal study written in kdb+/q.</p>

<p>They are for students, analysts and hobby quants who want to see the method, not just a result, and for developers who want tested templates. Most rely on free Yahoo Finance data or on synthetic samples, and the guides say so plainly. All of them are research and teaching tools. {NOT_ADVICE}</p>'''

choose = table(["Tool", "What it does", "Use it when"],
               [[f'<a href="#{t["anchor"]}">{t["repo"]}</a>', t["what"], t["when"]] for t in TOOLS])

sections = "\n".join(tool(t["anchor"], t["title"], t["repo"], t["paras"], t["cmd_intro"], t["cmd"], t["out"], t["limit"]) for t in TOOLS)

worked = f'''<h2 class="gb-h2">Worked example: one daily brief, end to end (market-brief-base)</h2>
<p>This is the run recorded in the market-brief-base guide on 6 November 2026, on Python 3.11 with the pinned versions (yfinance 0.2.66, pandas 2.3.3), in a fresh clone and a throwaway virtual environment.</p>
<p><strong>1. Get the code and build the environment.</strong></p>
{code("""git clone https://github.com/herrrickshaw/market-brief-base.git
cd market-brief-base
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
""")}
<p><strong>2. Check the signal logic offline.</strong> No network is needed.</p>
{code("""python brief.py --self-test
  PASS  decisive break above the box is BREAKOUT_BUY
  PASS  decisive break below the box is BREAKDOWN_SELL
  PASS  a NaN final close is NO_DATA, not a fabricated zero
  PASS  sma returns None rather than inventing a short average
  PASS  sma ignores NaN instead of treating it as zero
  email: not configured (SMTP_USER, SMTP_PASS, SMTP_TO) — skipping send
  PASS  unconfigured send skips cleanly instead of raising
  self-test: OK
""")}
<p>Trimmed; there were 12 PASS lines in all.</p>
<p><strong>3. Fetch live bars and write the brief.</strong></p>
{code("""python brief.py --out brief.html
  India: 15/15 priced
  US: 15/15 priced
  wrote brief.html (7,086 bytes)
""")}
<p>The run took about 7.6 seconds. Five of the 30 rows in the HTML table, for bars dated 4 and 5 November 2026:</p>
{code("""Symbol       Close      As of       Day     Trend         Darvas
TCS.NS       2,436.00   2026-11-04  -2.52%  Death Cross   IN_BOX
TITAN.NS     4,754.40   2026-11-04  +4.22%  Golden Cross  BREAKOUT_BUY
AAPL         344.17     2026-11-05  -1.53%  Golden Cross  IN_BOX
MSFT         535.93     2026-11-05  -3.58%  Golden Cross  IN_BOX
NVDA         181.60     2026-11-05  -9.26%  Golden Cross  BREAKDOWN_SELL
""")}
<p>India and US rows carry different bar dates because the markets close at different times, and the date is printed on every row. A stock can show BREAKOUT_BUY and Death Cross together, because the Darvas box and the 50/200-day cross measure different things. These are one day&rsquo;s mechanical screen states from public Yahoo Finance data, not current prices and not advice; your run will differ.</p>'''

limits = f'''<h2 class="gb-h2">What these tools do not do</h2>
<ul>
<li><strong>They do not give investment advice.</strong> Every guide in this group says so. The labels, shortlists and model outputs are research and teaching material, not recommendations to buy or sell.</li>
<li><strong>They do not supply audited data.</strong> The ticker list, the fundamentals collector and the daily brief rely on Yahoo Finance through yfinance: third-party, unaudited, rate-limited, and covered by Yahoo&rsquo;s terms.</li>
<li><strong>They are not live.</strong> The ticker list&rsquo;s validated flat file is dated July 2026 in its README, the correlation windows end on different dates per market, and nothing refreshes them automatically.</li>
<li><strong>Some samples are synthetic.</strong> The kdb+/q study&rsquo;s bundled data and the event-bus sample prices are generated; no figure from them describes a real market.</li>
<li><strong>Some cannot be rebuilt from the repo alone.</strong> The correlation rebuild needs a price warehouse that is not included, and the kdb+/q study needs a KDB-X licence.</li>
<li><strong>Dates in the data are not always real dates.</strong> The fundamentals &lsquo;filed&rsquo; column is an assumption, so the output is not suitable for strict point-in-time backtests.</li>
<li><strong>Not every repo is finished.</strong> event-driven-stock-analysis is a design and a skeleton whose tests did not run in the guide&rsquo;s demo.</li>
</ul>'''

body = f"""{stats}

{intro}

<h2 class="gb-h2">Which tool for which job</h2>
{choose}

<h2 class="gb-h2">The seven tools</h2>
<p>Each section says what the tool does, where its data comes from, the one command to start with, and the main limitation its guide records. All need git and Python 3; extra software is noted where it matters.</p>
{sections}
{worked}

{limits}
"""

src_links = "; ".join(repo_link(t["repo"]) for t in TOOLS)
sources = ("Code: " + src_links + ". "
           "This page replaces the separate how-to guides for these seven repositories, written between 18 October and 6 November 2026. "
           "Every command, output and figure here is taken from those guides&rsquo; own demo runs, on the dates given in the text. "
           "Where a README and a fresh run disagreed (the ticker count; the correlation rebuild), both are noted and the run is used. "
           "The earlier five-toolkits guide also covered four non-finance toolkits; they are outside this page. "
           "Market data comes from Yahoo Finance via yfinance or from synthetic samples, as stated per tool. "
           + NOT_ADVICE)

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/what-seven-model-stock-portfolios-look.html", "What Seven Model Stock Portfolios Look Like Once You Check Them Against the Index"),
    ("https://masaladeutsch.blogspot.com/2026/10/how-to-use-five-open-toolkits-finance.html", "How to use five open toolkits: finance models, documents, care audits"),
    ("https://masaladeutsch.blogspot.com/2026/08/do-cheap-stocks-stay-cheap-price-band.html", "Do Cheap Stocks Stay Cheap? Price-Band Migration and What K-Means Clustering Actually Finds"),
    ("https://masaladeutsch.blogspot.com/2026/08/below-250-is-where-real-junk-lives.html", "Below ₹250 Is Where the Real Risk Lives: Splitting India&#x27;s Cheapest Stocks Four Ways"),
]

TITLE = "Seven Open-Source Tools for Stock-Market Research, From Ticker Lists to Valuation Models, and Where Each One Stops"
STANDFIRST = ("Seven free repositories cover the routine work of market research: symbol lists for 34 markets, annual fundamentals, "
              "correlation matrices, a valuation engine, a daily brief, a kdb+/q signal study and an event-driven monitor design. "
              "This guide sets out what each one does, the command to start with and its main limit; all are research tools, not investment advice.")

build("Open-Source Tools &middot; 12 November 2026", TITLE, STANDFIRST, body, sources, related, OUT)
print("built", OUT, "tools", len(TOOLS))
