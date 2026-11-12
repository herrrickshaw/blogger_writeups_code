"""Hub post: India agri and food-data tools (replaces three separate how-to guides).
Build from the repo root:
  PYTHONPATH=tools/postbuild python3 out/research/phase2-hubs/agri-food/build.py
Every statement, command and figure below comes from the three source guides listed in
out/research/phase2-hubs/hubs.json under "agri-food" (two live posts and one draft).
Commands are copied verbatim from the guides' <pre> blocks and HTML-escaped here.
"""
import html
from buildpost import build

OUT = 'out/post-hub-agri-food.html'
GH = 'https://github.com/herrrickshaw/'

PRE_STYLE = ('background:#f6f3ea;color:#111;border:1px solid #dee2e6;border-radius:8px;'
             'padding:10px 12px;overflow-x:auto;font-size:.82rem;line-height:1.45;white-space:pre')
H3_STYLE = ("font-family:-apple-system,'Segoe UI',sans-serif;font-weight:700;font-size:1.12em;"
            "margin:1.8rem 0 .5rem;color:#212529")


def code(s):
    return f'<pre style="{PRE_STYLE}"><code>{html.escape(s.strip(chr(10)))}</code></pre>'


def repo(name):
    return f'<a href="{GH}{name}">github.com/herrrickshaw/{name}</a>'


def table(head, rows):
    h = ''.join(f'<th>{c}</th>' for c in head)
    r = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return (f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead>'
            f'<tbody>{r}</tbody></table></div>')


def tool(name, title, paras, cmd, cmd_note, limit):
    ps = ''.join(f'<p>{p}</p>\n' for p in paras)
    return (f'<h3 style="{H3_STYLE}">{title}</h3>\n{ps}'
            f'<p><strong>Quick start.</strong> {cmd_note}</p>\n{code(cmd)}\n'
            f'<p><strong>Code:</strong> {repo(name)}</p>\n'
            f'<p><strong>Main limitation.</strong> {limit}</p>\n')


# ---------------------------------------------------------------- commands (verbatim)
C_AGRI = r'''
python3 -c "import duckdb; print(duckdb.sql(\"select pulled_on, count(*) n, count(distinct commodity) commodities from read_csv_auto('data/mandi_prices_snapshot.csv') group by 1 order by 1 desc limit 3\"))"
'''
C_ARR_LOAD = r'''
python3 -c "import pandas as pd
for f in ['data/agmarknet/state_monthly.csv.gz','data/agmarknet/market_daily_sample.csv.gz','data/upag/apy_state.csv.gz','data/upag/msp.csv.gz']:
    d=pd.read_csv(f); print(f, len(d), list(d.columns)[:6])"
'''
C_ARR_CLONE = r'''
git clone https://github.com/herrrickshaw/india-mandi-arrivals.git
cd india-mandi-arrivals
'''
C_ARR_ENV = r'''
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
'''
C_ARR_BUILD = r'''
python analysis/build_insights.py
'''
C_ARR_GREP = r'''
grep '^## ' reports/INSIGHTS.md
'''
C_FCI = r'''
cd data && python3 holding_economics.py
'''

# ---------------------------------------------------------------- outputs reported by the guide
O_MP_WHEAT = r'''
v=pd.read_csv('reports/mandi_vs_msp.csv'); v[(v.commodity=='Wheat')&(v.state=='Madhya Pradesh')].tail(6)
  month          state  arrivals_t  price_rs_qtl msp_year  msp_rs_qtl  price_vs_msp  below_msp
2026-05 Madhya Pradesh  1925234.17       2418.76  2026-27      2585.0     -0.064309       True
2026-06 Madhya Pradesh  1227436.06       2395.11  2026-27      2585.0     -0.073458       True
2026-07 Madhya Pradesh   810673.96       2510.17  2026-27      2585.0     -0.028948       True
2026-08 Madhya Pradesh   544962.35       2581.90  2026-27      2585.0     -0.001199       True
2026-09 Madhya Pradesh   619729.43       2635.74  2026-27      2585.0      0.019629      False
2026-10 Madhya Pradesh   365163.71       2661.26  2026-27      2585.0      0.029501      False
'''
O_BELOW = r'''
| Commodity                   | State-months | Below MSP | Median price vs MSP |
| Ragi(Finger Millet)         | 78           | 98.7%     | -25.8% |
| Groundnut                   | 261          | 86.6%     | -15.9% |
| Bajra(Pearl Millet/Cumbu)   | 223          | 79.4%     | -11.5% |
| Green Gram(Moong)(Whole)    | 220          | 79.1%     | -16.5% |
| Soyabean                    | 199          | 76.4%     | -14.5% |
| Maize                       | 332          | 70.8%     | -6.5%  |
| Cotton                      | 126          | 54.0%     | -0.6%  |
| Paddy(Common)               | 429          | 40.1%     | 1.2%   |
| Mustard                     | 248          | 21.4%     | 9.1%   |
| Wheat                       | 314          | 20.1%     | 5.1%   |
'''

stats = '''<div class="gb-stats">
<div class="gb-stat"><b>3 repos</b><span>one for daily mandi prices, one for monthly prices and arrivals since 2019, one for MSP and grain stocks</span></div>
<div class="gb-stat"><b>Jan 2019 &ndash; Oct 2026</b><span>span of the monthly state-by-commodity mandi file in india-mandi-arrivals</span></div>
<div class="gb-stat"><b>10 records</b><span>per request with data.gov.in&rsquo;s public demo key, which makes a full daily pull slow</span></div>
<div class="gb-stat"><b>14 tables</b><span>of mandi insights rebuilt from the data in 16 seconds in one guide&rsquo;s run, identical to the committed ones</span></div>
</div>'''

which = table(['Tool', 'What it does', 'Use it when'], [
    ('agri-commodity-tracker', 'Collects daily APMC mandi prices from Agmarknet via data.gov.in, plus World Bank, FAOSTAT and NASA POWER data, into DuckDB',
     'You want market-level daily prices and are willing to run a collector every day'),
    ('india-mandi-arrivals', 'Monthly Agmarknet prices and arrivals since 2019, joined to UPAG output, MSP, procurement and trade, with 14 ready insight tables',
     'You want arrivals against production, prices against MSP, or seasonality, by state and crop'),
    ('FCI-warehouse-MSPvsMSV', 'A sourced data and research repo on procurement, MSP, FCI stocks and storage, with small economic models',
     'You are asking whether MSP holds in the market, or whether buying and storing grain pays'),
])

tools = ''.join([
    tool('agri-commodity-tracker', 'agri-commodity-tracker: daily mandi prices in one DuckDB file', [
        'This collects APMC mandi prices from Agmarknet through data.gov.in: state, district, market, commodity, variety, and minimum, maximum and modal price in rupees per quintal. It writes them to a local DuckDB file, and re-running a day replaces that day instead of duplicating it. The README suggests running the collector daily at 14:30 IST.',
        'Other collectors pull a World Bank agriculture indicator panel, FAOSTAT producer prices and crop production, NASA POWER monthly rainfall and temperature for 14 states, and the FCI depot directory. Committed CSV snapshots let you query without any network: the guide&rsquo;s snapshot held 463,023 price rows pulled between 21 July and 24 September 2026, and 10 tests passed.',
    ], C_AGRI, 'Query the committed snapshot with DuckDB, no network needed (the latest pull dates with row and commodity counts):',
        'The source serves only the current day, so history depends on running the collector. Days before 23 July 2026 are stubs of about 10 rows from an earlier bug and cannot be backfilled. The demo key returns 10 records per request, and the repo&rsquo;s collection log ends with an HTTP 429 (too many requests). Day sizes vary, so compare like with like.'),

    tool('india-mandi-arrivals', 'india-mandi-arrivals: arrivals and prices joined to production and MSP', [
        'This is a point-in-time extract plus the code to rebuild it. The Agmarknet side holds state-by-commodity monthly prices and arrivals from January 2019 to October 2026, a market-level daily sample (23 field crops, every sixth day since November 2025) and the master lists. The UPAG side holds area, production and yield by state and district, MSP, WPI, FCI procurement, DGCIS trade and the crop calendar.',
        'Crosswalks map Agmarknet commodity and state names to UPAG&rsquo;s, including the paddy &times; 0.67 conversion to milled rice. One script, build_insights.py, turns the data into 14 report tables: arrivals as a share of production, mandi prices against MSP, volatility and seasonality, yield trends, area by crop and the largest mandis. The collectors use only the standard library, throttle requests and cache, so an interrupted run resumes. The worked example below uses this tool.',
    ], C_ARR_LOAD, 'Check the main files load, and how big they are:',
        'Arrivals are what markets choose to report: grain bought directly by government agencies or traded outside APMCs is missing, and Agmarknet widened its market coverage from November 2025, so recent arrivals are not comparable with earlier years. The files are an unofficial extract, so check them against the source portals. A full refresh takes about an hour and was not run by the guide.'),

    tool('FCI-warehouse-MSPvsMSV', 'FCI-warehouse-MSPvsMSV: MSP, procurement and the cost of holding grain', [
        'This research and data repository asks whether a Minimum Support Volume guarantee could extend price support beyond rice and wheat. Its data folder holds 49 CSVs, and a MANIFEST.md records where each came from and what is missing. The files include the MSP series for 14 crops from 2010-11, procurement by year, stocks against norms and a one-day table of mandi modal prices against MSP for 16 crops (23 July 2026).',
        'It also has cited reports, a self-contained HTML dashboard, a Colab notebook and small Python models: holding economics, the unit economics of processing OMSS grain, rice-bran oil savings and a real farm income index. In the guide&rsquo;s run, the holding-economics model found storage and financing costs exceeded price appreciation for all 16 commodities tested, over 12, 24 and 36 months.',
    ], C_FCI, 'Run the holding-economics model (it prints summary, horizon-return and post-crash tables, and rewrites three CSVs next to the script, so run it in a copy if you want the repo untouched):',
        'Year labels differ between files: msp_series.csv uses the sowing year, while the mandi table uses the marketing year, so check before joining them. The mandi comparison covers one day and includes crops with very few reports. The holding verdict depends on the assumed storage and financing rates, and the models are stylised unit economics, not forecasts.'),
])

worked = f'''<h2 class="gb-h2">Worked example: does the mandi price hold up to MSP? (india-mandi-arrivals)</h2>
<p>This follows the india-mandi-arrivals guide, which ran these steps in a fresh virtual environment on 29 October 2026. It used the committed extract (latest month October 2026) and did not run the collectors. The figures describe that extract, not current prices.</p>
<p><strong>Step 1.</strong> Get the repository and install the analysis dependencies (pandas, numpy and openpyxl).</p>
{code(C_ARR_CLONE)}
{code(C_ARR_ENV)}
<p><strong>Step 2.</strong> Rebuild the 14 insight tables from the data:</p>
{code(C_ARR_BUILD)}
<p>The guide reported that the script wrote reports/ in about 16 seconds, and that git status showed no changes: the committed tables were reproduced exactly.</p>
<p><strong>Step 3.</strong> List the headline sections:</p>
{code(C_ARR_GREP)}
<p>Six sections: arrivals as a share of production (2025-26), mandi prices against MSP (last 24 months), most and least volatile large markets, yield growth, area by crop, and the largest mandis.</p>
<p><strong>Step 4.</strong> Read Madhya Pradesh wheat against MSP for the last six months, from reports/mandi_vs_msp.csv. Arrivals are in tonnes and prices in rupees per quintal:</p>
{code(O_MP_WHEAT)}
<p>In the harvest month of May, the mandi price sat 6.4% under the Rs 2,585 MSP. By October it was 2.9% above. The script matches the MSP year to the marketing year.</p>
<p><strong>Step 5.</strong> Compare crops. The guide&rsquo;s table from INSIGHTS.md shows the share of state-months, over the last 24 months, in which a state&rsquo;s weighted mandi price was below that year&rsquo;s MSP:</p>
{code(O_BELOW)}
<p><strong>What the guide drew from it.</strong> Millets, groundnut and pulses traded below MSP most of the time; wheat and mustard rarely did. Commodity names are Agmarknet&rsquo;s own.</p>
'''

dont = '''<h2 class="gb-h2">What these tools do not do</h2>
<ul>
<li><strong>No trading signals.</strong> The prices are mandi spot prices, not futures, and they mix varieties and grades. None of the three is investment advice.</li>
<li><strong>No official statistics.</strong> All three republish or compile public data without auditing it. Check figures against agmarknet.gov.in and upag.gov.in before relying on them.</li>
<li><strong>No lot-level trades.</strong> District cumulative arrivals and anything behind a login or captcha are out of scope for india-mandi-arrivals.</li>
<li><strong>No complete record of what was grown or sold.</strong> Arrivals miss direct government purchases and trade outside APMCs. Shares above 100% of production, or near-zero volatility, are reporting patterns, not errors.</li>
<li><strong>No back history on demand.</strong> data.gov.in serves only the current day, so agri-commodity-tracker&rsquo;s daily history exists only for days someone ran the collector.</li>
<li><strong>No forecasts.</strong> The holding-economics and processing models in FCI-warehouse-MSPvsMSV are deterministic, with labelled assumptions. They are not for farm-level decisions.</li>
</ul>
'''

disagree = '''<h2 class="gb-h2">Where the guides differ</h2>
<ul>
<li><strong>&ldquo;How often below MSP&rdquo; depends on the measure.</strong> FCI-warehouse-MSPvsMSV counts market reports on a single day (23 July 2026): 19% below MSP for wheat, 92% for bajra and 84% for moong. india-mandi-arrivals counts state-months over 24 months up to October 2026: 20.1%, 79.4% and 79.1%. The second is newer and covers far more time, so prefer it for patterns. Treat the one-day table as a snapshot, especially for crops with few reports.</li>
<li><strong>MSP year labels.</strong> The FCI repo&rsquo;s msp_series.csv files the Rs 2,425 rabi wheat MSP under 2024-25 and Rs 2,585 under 2025-26, by sowing year. Its mandi table, like india-mandi-arrivals, uses the marketing year: wheat Rs 2,425 for 2025-26, and Rs 2,585 in india-mandi-arrivals for 2026-27. Align the labels before you join files from different repos.</li>
<li><strong>Rate limits.</strong> Both collectors run into them. agri-commodity-tracker&rsquo;s collection log ends with an HTTP 429 from its source. india-mandi-arrivals throttles itself to one request per 1.5 seconds because Agmarknet returns HTTP 429 if hurried.</li>
</ul>
'''

opening = '''<p>India&rsquo;s farm-price data sits on several government portals. Agmarknet and data.gov.in carry daily mandi prices and arrivals. UPAG has area, production, yield, MSP and procurement, while CACP reports, DFPD bulletins and FCI data cover support prices, stocks and storage. Each portal has its own names and formats, and some serve only the current day. The three open-source repositories on this page pull that data into files you can query, and join it where the portals do not.</p>
<p>They are for agricultural economists, policy analysts, journalists and students who want to check a claim such as &ldquo;the mandi price is below MSP&rdquo; against the data. Each works at a different time grain: daily, monthly, or a single day&rsquo;s snapshot alongside long annual series. Start with the table, then read the section on the tool you pick.</p>
'''

body = f'''{stats}

{opening}
<h2 class="gb-h2">Which tool for which job</h2>
{which}
<p class="gb-note">Each section below gives the tool&rsquo;s data sources and outputs, one quick-start command copied from its guide, the repo link and its main limitation.</p>

<h2 class="gb-h2">The tools, one by one</h2>
{tools}
{worked}
{dont}
{disagree}'''

sources = ('This page replaces the separate how-to guides for these three repositories, which were run between 19 and 29 October 2026. '
           'Repositories: ' + '; '.join(repo(n) for n in [
               'agri-commodity-tracker', 'india-mandi-arrivals', 'FCI-warehouse-MSPvsMSV']) + '. '
           'Underlying data, as recorded by the repos: Agmarknet (directly and via data.gov.in), UPAG, CACP, DFPD bulletins, FCI, World Bank, FAOSTAT and NASA POWER. '
           'india-mandi-arrivals re-publishes Government of India open data under GODL-India. '
           'Figures quoted here are those the guides reported on the dates given, not current values. Not investment advice.')

related = [
    ("https://masaladeutsch.blogspot.com/2026/07/the-price-of-grain-msp-msv-and.html", "The Price of Grain: MSP, MSV, and the Arithmetic of the Indian Grain State"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-biggest-mandi-crops-have.html", "India’s Biggest Mandi Crops Have the Steadiest Prices. Its Vegetables Swing Two to Eight Times as Much."),
    ("https://masaladeutsch.blogspot.com/2026/10/maize-is-cheapest-in-different-state.html", "Maize Is Cheapest in a Different State Every Few Months. Rice Barely Moves."),
    ("https://masaladeutsch.blogspot.com/2026/10/wheats-support-price-rose-by-25.html", "Wheat&#x27;s Support Price Rose by ₹25, the Smallest Rise in Years. The Granaries Explain Why"),
    ("https://masaladeutsch.blogspot.com/2026/07/fci-grain-flow-procurement-storage.html", "FCI Grain Flow — Procurement · Storage · Disposal Dashboard"),
]

TITLE = ('Three Open-Source Tools for India&rsquo;s Mandi and Grain Data: Daily Prices, Monthly Arrivals Since 2019, '
         'and the MSP Question')
STANDFIRST = ('Three small repositories turn Agmarknet, UPAG and FCI data into files you can query, one for daily mandi prices, '
              'one for monthly arrivals joined to production and MSP, and one for procurement and the cost of holding grain. '
              'This guide shows which to pick, the command to start with, and where each one&rsquo;s numbers stop.')

build('Open-Source Tools &middot; 12 November 2026', TITLE, STANDFIRST, body, sources, related, OUT)
print('built', OUT)
