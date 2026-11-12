"""Hub post: India trade-data tools (replaces eight separate how-to guides).
Build from the repo root:
  PYTHONPATH=tools/postbuild python3 out/research/phase2-hubs/trade-data/build.py
Every statement, command and figure below comes from the eight source guides listed in
out/research/phase2-hubs/hubs.json under "trade-data". Commands are copied verbatim from
the guides' <pre> blocks and HTML-escaped here.
"""
import html
from buildpost import build

OUT = 'out/post-hub-trade-data.html'
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
C_TRACKER = r'''
python3 collectors/eidb_trade.py --year 2024
'''
C_DEFICIT_BAL = r'''
python3 - <<'E'
import json
d=json.load(open('data/tradestat_hsn_export_import_2018-19_to_2025-26.json'))
t=d['totals']
for y in t['import']:
    print(y, round(t['import'][y]/1e3,1), round(t['export'][y]/1e3,1), round((t['export'][y]-t['import'][y])/1e3,1))
E
'''
C_DEFICIT_RANK = r'''
python3 - <<'E'
import json
d=json.load(open('data/tradestat_hsn_export_import_2018-19_to_2025-26.json'))
i,e=d['by_chapter']['import'],d['by_chapter']['export']
y='2025 - 2026'
r=sorted((e.get(c,{}).get(y,0)-v[y],c,v['name'][:40]) for c,v in i.items())
for b,c,n in r[:8]: print(c,n,round(b/1e3,1))
E
'''
C_CLONE_DEFICIT = r'''
git clone https://github.com/herrrickshaw/india-commodity-trade-deficit.git
cd india-commodity-trade-deficit
'''
C_ANALYSIS = r'''
python3 -c "import json;d=json.load(open('data/five_year_trade_currency_synthesis_2026-07-18.json'))['trade_totals_usd_million'];print(d['years']);print(d['export']);print(d['import']);print(d['export_growth_5yr_pct'],d['import_growth_5yr_pct'])"
'''
C_POLICY = r'''
python3 -c "import json;d=json.load(open('data/sector_and_policy_recommendations_2026-07-18.json'))
for t in d['import_substitution_tiers']:print(t['tier'],t['label'],[(c['hs'],c['name'],c['growth_pct']) for c in t['chapters']])"
'''
C_CHEM = r'''
python3 - <<'E'
import json
from collections import Counter
d=json.load(open('data/chem_hsn8_signals.json'))
for ch,v in sorted(d['by_chapter'].items()):
    print(ch, d['ch_names'][ch], len(v), round(sum(r['deficit_fy26'] for r in v)/1e3,1), dict(Counter(r['is_signal'][0] for r in v)))
E
'''
C_EXPORT = r'''
.venv/bin/python -c "import pandas as pd; print(pd.read_csv('HIGH_OPPORTUNITY_EXPORTS.csv').Opportunity.value_counts())"
'''
C_FOREX = r'''
grep -n "875.4" *.md
'''
C_MOSPI = r'''
python3 -c "import json;d=json.load(open('data/mospi_snapshot_2026-07-18.json'));print(d['cpi']['latest_month'],d['cpi']['general_index'])"
'''

# ---------------------------------------------------------------- outputs reported by the guide
O_BAL = r'''
FY          imports  exports  balance
2018-19      514.1    330.1   -184.0
2019-20      474.7    313.4   -161.3
2020-21      394.4    291.8   -102.6
2021-22      613.1    422.0   -191.0
2022-23      716.0    451.1   -264.9
2023-24      678.2    437.1   -241.1
2024-25      721.2    437.7   -283.5
2025-26      776.0    441.7   -334.3  (provisional)
'''
O_RANK = r'''
ch  name                                     imports exports balance
27  Mineral fuels, mineral oils              203.4    55.9   -147.5
71  Pearls, precious/semi-precious stones+metals 109.4  28.3    -81.1
85  Electrical machinery and equipment       104.9    54.0    -50.9
84  Nuclear reactors, boilers, machinery      74.0    36.6    -37.4
15  Animal or vegetable fats and oils         19.8     2.2    -17.5
39  Plastic and articles thereof              22.2     7.6    -14.6
31  Fertilisers                               14.6     0.2    -14.4
88  Aircraft, spacecraft and parts            13.8     1.7    -12.1
'''

stats = '''<div class="gb-stats">
<div class="gb-stat"><b>8 repos</b><span>each covering one slice of India&rsquo;s trade data, from HS chapters to chemical codes and reserves</span></div>
<div class="gb-stat"><b>FY2018-19 to FY2025-26</b><span>the longest annual span, in the chapter-level TRADESTAT files</span></div>
<div class="gb-stat"><b>827 codes</b><span>chemical HS-8 lines sorted into import-substitution signals</span></div>
<div class="gb-stat"><b>3 of 8</b><span>repos are archived or kept only as a legacy snapshot: read them, do not build on them</span></div>
</div>'''

which = table(['Tool', 'What it does', 'Use it when'], [
    ('india-trade-tracker', 'Pulls annual exports and imports by 2-digit HS chapter from the Export-Import Data Bank into DuckDB; also World Bank, NIRYAT and UN Comtrade collectors',
     'You want to collect chapter totals yourself, straight from the government data bank'),
    ('india-commodity-trade-deficit', 'Two JSON files from TRADESTAT: all HS chapters for eight fiscal years, and 4-digit metal imports by partner country',
     'You need the trade balance by chapter over time, or gold, silver and copper imports split out'),
    ('india-trade-data-analysis', 'Dated JSON extracts and charts on trade, the rupee, reserves, inflation and GDP, with a five-year synthesis',
     'You want one sourced, descriptive picture of the external sector without installing anything'),
    ('india-trade-sector-policy-recommendations', 'Turns the same data into tiered calls on import substitution, export growth and country exposure',
     'You want explicit policy recommendations you can check or argue with'),
    ('chemical_import_substitution', 'Sorts 827 chemical, fertiliser and plastics HS-8 lines into substitution signals',
     'You are screening chemical imports at product level, not chapter level'),
    ('india-trade-export-analysis', 'Archived pandas scripts and CSVs on commodity exports, with a high-growth shortlist',
     'You want a starting export table to verify, or to see how a growth screen breaks'),
    ('india-forex-analysis', 'Archived markdown study of reserves, the trade deficit and borrowing; no code',
     'You want an audit exercise, not a source to cite'),
    ('mospi-dataset-analysis-public', 'Frozen snapshot of CPI, WPI, IIP and RBI forex series pulled through the MoSPI data connector, with 14 charts',
     'You want a worked example of the MoSPI connector, and dated figures are fine'),
])

tools = ''.join([
    tool('india-trade-tracker', 'india-trade-tracker: chapter totals from the government data bank', [
        'This collects India&rsquo;s annual merchandise exports and imports by 2-digit HS chapter from the DGFT / Department of Commerce Export-Import Data Bank. Each row has the current-year and previous-year value in US$ million and the growth rate. The data bank site is built in JavaScript, so the collector drives headless Chrome and stores each pull in DuckDB with the pull date.',
        'Other collectors pull a World Bank trade indicator panel, bilateral monthly data and HS8 detail from the NIRYAT portal, and chapter totals from the UN Comtrade public preview API. A committed CSV snapshot holds two financial years (FY2024-25 and FY2025-26) for both flows, so the tests and queries run with no browser and no network. The guide&rsquo;s run had 17 tests passing.',
    ], C_TRACKER, 'Pull one financial year live (needs Chrome and a network connection; the guide did not run this step, only the snapshot and tests):',
        'The guide ran only the snapshot and the tests, not the live collector. The snapshot covers two years at chapter level, and monthly series and 4/6/8-digit drill-down are still on the roadmap. The NIRYAT collector turns off TLS certificate checks because of a certificate mismatch on that site; understand that before you use it.'),

    tool('india-commodity-trade-deficit', 'india-commodity-trade-deficit: eight years of chapters, plus bare metals', [
        'Two small JSON files from the Commerce Ministry&rsquo;s TRADESTAT (DGCI&amp;S) carry the commodity side of India&rsquo;s trade gap. The chapter file has exports and imports for all HS chapters from FY2018-19 to FY2025-26 in US$ million. The 4-digit file splits bullion out of chapter 71, with gold (7108), silver (7106), copper and other metal imports, and a by-country block for each code.',
        'You need only Python&rsquo;s standard library. The repo also holds a finished essay on metal recycling as a self-contained HTML page. The worked example below uses this tool.',
    ], C_DEFICIT_BAL, 'Print the trade balance by fiscal year (eight rows: year, imports, exports, balance in US$ billion):',
        'The data is annual, and FY2025-26 is provisional. The files were retrieved on 18 July and 3 August 2026, so later revisions are missing. The metals file covers 14 selected 4-digit codes, not all of HS.'),

    tool('india-trade-data-analysis', 'india-trade-data-analysis: the descriptive picture in one place', [
        'This is the data half of a two-repo study. It records CPI and WPI by state, GDP growth with revisions, forex reserves, the rupee, the goods and services balance, and imports and exports by HS chapter from FY2018-19 to FY2025-26. A five-year synthesis puts all of these on one window, and a sample FY2025-26 report states every figure in US$ million.',
        'The extracts come as JSON, each stating its purpose, source and retrieval date, with charts served on the project&rsquo;s GitHub Pages site. A validation file compares TRADESTAT totals with the Commerce Ministry&rsquo;s TIA portal and records a gap of about 2% on exports.',
    ], C_ANALYSIS, 'Print the five-year export and import totals and growth rates:',
        'Everything is a snapshot retrieved on 18 July 2026, and FY2025-26 is provisional in every source. The guide read the committed files only; it did not re-pull MoSPI, RBI or TRADESTAT data or run the Colab notebook. Services trade runs one year behind goods.'),

    tool('india-trade-sector-policy-recommendations', 'india-trade-sector-policy-recommendations: tiered calls you can argue with', [
        'This is the prescriptive half of the same study. It takes the chapter rankings and country concentration from india-trade-data-analysis, checks them against PLI scheme coverage and policy history, and sorts import chapters into three tiers: &ldquo;Act now&rdquo;, &ldquo;Scale existing scheme&rdquo; and &ldquo;Different lever&rdquo;. It does the same for export growth and for country relationships (de-risk, diversify, monitor).',
        'Each call names an HS chapter, its FY2025-26 value, a growth rate and any existing scheme. The repo has 67 data files, 29 HTML charts, a PLI scheme report card and a quarterly PDF. It flags two risks it says it cross-checked against NITI Aayog&rsquo;s Trade Watch: EU CBAM exposure on iron and steel exports, and a long decline in gems and jewellery exports.',
    ], C_POLICY, 'List the three import-substitution tiers with their chapters and growth rates:',
        'The tiers are the repo author&rsquo;s judgements on a July 2026 snapshot of provisional data, not official policy. A different weighting would move chapters between tiers. The guide did not rebuild the PDFs or re-check the NITI Aayog and PIB cross-checks.'),

    tool('chemical_import_substitution', 'chemical_import_substitution: product-level signals for chemical imports', [
        'One script and its results file sort India&rsquo;s chemical imports at 8-digit HS level. It covers chapters 28, 29, 31, 32, 33, 34, 38 and 39, and keeps every code with a FY2025-26 import-minus-export gap of at least $0.5 million: 827 codes in the committed results. For each it computes value, volume and unit-price growth and assigns a signal: A scissors (value and volume falling, price rising), B inelastic target, C insufficient data, D deepening, or E no clear signal.',
        'Each code also gets a short rationale tag. A styled HTML registry lets you browse all the lines. In the guide&rsquo;s read, 59.6% of codes showed no clear one-year signal, which says how little a single year can tell you.',
    ], C_CHEM, 'Summarise the committed results by chapter: code count, deficit in US$ billion, and a count of signal letters:',
        'It compares one year with the previous one (FY2024-25 to FY2025-26) only. The rationale tags are keyword rules on product names, not engineering assessment. The script needs raw TRADESTAT Excel files that are not in the repo, and the repo has no README; the usage notes come from the script&rsquo;s docstring.'),

    tool('india-trade-export-analysis', 'india-trade-export-analysis: an archived export table and growth screen', [
        'Pandas scripts read TradeStat Excel exports, compute growth between 2020 and 2023, project 2025 and 2026 by extending that growth, and classify commodities as mega-growth, high-value growing or emerging opportunity. The committed results include a 14,980-row commodity table and a 293-row shortlist (which includes the all-India total row).',
        'The repository is archived and read-only. The README calls it indicative analysis from public sources, not official statistics.',
    ], C_EXPORT, 'Count the three opportunity classes in the shortlist (run after installing pandas in a virtual environment):',
        'The scripts need raw TradeStat workbooks from a hard-coded personal Downloads path, so they cannot be re-run from a clone. The line items add up to about 5% more than the total row. The column labelled 5-year growth compares 2020 with 2023, and the 2025&ndash;2026 projections only repeat that growth rate.'),

    tool('india-forex-analysis', 'india-forex-analysis: a report to audit, not to cite', [
        'Nine numbered markdown documents and an index cover export growth from 2020 to 2023, imports and exports, RBI reserves against the trade deficit, a reconciliation of Budget 2026-27 tax revenue, debt and borrowing, a five-year comparison and an executive summary with scenario probabilities. There is no code. The &ldquo;amber alert&rdquo; rating and the scenario probabilities are the author&rsquo;s judgement, not outputs of a documented model.',
        'The guide treats it as an audit exercise. Some tables add up: the reserve components, the six-month change and the tax shares recompute correctly. The headline export figure does not (see below). The repository is archived and will not be corrected.',
    ], C_FOREX, 'Find every place the stated 2023 export figure appears (it recurs in several documents, so one error spreads):',
        'The 2023 export total of US$875.4 bn is exactly twice the 437.7 bn total row in india-trade-export-analysis, which points to double counting. The trade-deficit headline therefore needs re-deriving before anyone quotes it.'),

    tool('mospi-dataset-analysis-public', 'mospi-dataset-analysis-public: a frozen MoSPI snapshot', [
        'This is a public, frozen copy of an analysis built on India&rsquo;s MoSPI data connector (api.mospi.gov.in) and related sources: inflation by state, the rupee and reserves, the trade balance by HS chapter, import-dependency gaps and policy coverage. It has 14 interactive HTML charts and 20 JSON datasets, and the README catalogues 25 MoSPI datasets and the workflow used to pull them.',
        'It logs its own data problems. The snapshot&rsquo;s connector health log records that the NAS indicator call returned an upstream error and fell back to local definitions, and that the RBI forex series lagged to June 2025.',
    ], C_MOSPI, 'Read the dated snapshot (prints the latest month and the Rural, Urban and Combined CPI):',
        'It is a legacy snapshot dated 18 July 2026, kept for history. New work happens in india-trade-data-analysis and india-trade-sector-policy-recommendations, so use those for anything maintained.'),
])

worked = f'''<h2 class="gb-h2">Worked example: which chapters drive the deficit (india-commodity-trade-deficit)</h2>
<p>This walk-through follows the india-commodity-trade-deficit guide, which ran these queries with Python 3&rsquo;s standard library on 19 October 2026. The files hold TRADESTAT data retrieved in July and August 2026; FY2025-26 is provisional. Treat the figures as that snapshot, not as current numbers.</p>
<p><strong>Step 1.</strong> Get the repository. Nothing else needs installing.</p>
{code(C_CLONE_DEFICIT)}
<p><strong>Step 2.</strong> Run the trade-balance command shown in the tool section above. The guide reported eight rows, in US$ billion:</p>
{code(O_BAL)}
<p><strong>Step 3.</strong> Rank chapters by their FY2025-26 balance:</p>
{code(C_DEFICIT_RANK)}
<p>The guide&rsquo;s table of the eight largest deficits, in US$ billion (it added the import and export columns for readability):</p>
{code(O_RANK)}
<p><strong>What the guide drew from it.</strong> Mineral fuels come first, then precious stones and metals, then electrical machinery. In the guide&rsquo;s calculation chapters 27 and 71 together were 40.3% of FY2025-26 imports, and chapter 71 alone supplied $20.5 bn of the $54.8 bn rise in total imports (37%). The README puts the commodity share at 48%, but it counts oil plus chapter 71 plus the metal chapters. The two figures use different definitions, so say which one you use.</p>
'''

dont = '''<h2 class="gb-h2">What these tools do not do</h2>
<ul>
<li><strong>No shipment or company data.</strong> The chapter collectors give totals, not bills of lading. HS8 detail exists only in the NIRYAT collector (for a few partner countries) and in the chemical tool (for eight chemical chapters).</li>
<li><strong>No live figures.</strong> The data is annual, FY2025-26 is provisional everywhere, and the committed snapshots date from July to September 2026. The MoSPI snapshot&rsquo;s reserves series stops at June 2025.</li>
<li><strong>No official statistics or advice.</strong> Every guide says its tool is not investment advice, and the tracker guide adds that it is not an official customs reference. The policy tiers and the &ldquo;amber alert&rdquo; are the repos&rsquo; author&rsquo;s judgements; the export &ldquo;opportunity&rdquo; classes are a mechanical growth screen.</li>
<li><strong>Not every script re-runs.</strong> india-trade-export-analysis and chemical_import_substitution need raw TRADESTAT workbooks that are not in their repos. The guides read the committed results instead.</li>
<li><strong>No trends from one year.</strong> The chemical signals compare two years only. Its docstring lists what is missing: a 3&ndash;5 year trend, an import penetration ratio, country-of-origin checks and a tariff/PLI cross-reference.</li>
<li><strong>No forecasts.</strong> The export projections to 2025 and 2026 extend one historical growth rate, and the forex scenario probabilities are stated without a method.</li>
</ul>
'''

disagree = '''<h2 class="gb-h2">Where the guides disagree</h2>
<ul>
<li><strong>FY2025-26 totals differ slightly by data vintage.</strong> The india-trade-tracker snapshot, pulled on 15 September 2026, sums to US$441.4 bn of exports and US$775.7 bn of imports. india-trade-data-analysis and india-commodity-trade-deficit, built on July and August 2026 retrievals, give 441.7 and 776.0. The tracker&rsquo;s pull is the latest of the three. All of them call the year provisional.</li>
<li><strong>Chapter counts.</strong> The tracker guide reports 97 chapters per flow and year. The commodity-trade guide describes 98 HS chapters. Neither guide explains the difference, so check before you join the two.</li>
<li><strong>Year labels in the export table.</strong> The total row that india-trade-export-analysis labels 2023 (US$437.7 bn) is the same figure the commodity-trade and trade-data-analysis guides give for FY2024-25. Its 2020 value (US$291.8 bn) matches their FY2020-21. Check the year basis before you compare it with the other tools.</li>
<li><strong>Commodity share of imports.</strong> 48% in the commodity-trade README against 40.3% in its guide. The gap comes from which chapters are counted.</li>
</ul>
'''

opening = '''<p>India&rsquo;s trade data is spread across several official sites: the Commerce Ministry&rsquo;s TRADESTAT and Export-Import Data Bank, the RBI and MoSPI. Each has its own download format, and the Export-Import Data Bank can only be queried through a browser. The eight open-source repositories on this page each take one slice of that data and turn it into files you can query: chapter totals, eight-digit chemical lines, metal imports by country, reserves and inflation. Some also add an analysis or a set of policy calls on top.</p>
<p>They are for students, journalists, policy analysts and exporters who want a dated, sourced number without paying for a data feed. Most need only Python, and several need nothing but a browser to read the committed files. Three of them are archived or kept only as a legacy snapshot, and this page says which. Start with the table, then read the section on the tool you pick.</p>
'''

body = f'''{stats}

{opening}
<h2 class="gb-h2">Which tool for which job</h2>
{which}
<p class="gb-note">Each section below gives the tool&rsquo;s data sources, one quick-start command copied from its guide, the repo link and its main limitation.</p>

<h2 class="gb-h2">The tools, one by one</h2>
{tools}
{worked}
{dont}
{disagree}'''

sources = ('This page replaces the eight separate how-to guides for these repositories, which were run or read between 19 and 23 October 2026 and published between 19 October and 3 November 2026. '
           'Repositories: ' + '; '.join(repo(n) for n in [
               'india-trade-tracker', 'india-commodity-trade-deficit', 'india-trade-data-analysis',
               'india-trade-sector-policy-recommendations', 'chemical_import_substitution',
               'india-trade-export-analysis', 'india-forex-analysis', 'mospi-dataset-analysis-public']) + '. '
           'Underlying data, as recorded by the repos: DGFT / Department of Commerce Export-Import Data Bank, DGCI&amp;S TRADESTAT, the Commerce Ministry TIA portal, RBI, MoSPI, World Bank, NIRYAT and UN Comtrade. '
           'Figures quoted here are those the guides reported on the dates given, not current values; FY2025-26 is provisional in every source. Not legal, customs or investment advice.')

related = [
    ("https://masaladeutsch.blogspot.com/2026/08/half-of-indias-import-bill-is.html", "Half of India&#x27;s Import Bill Is Commodities. Recycling and Import Substitution Are the Only Two Exits."),
    ("https://masaladeutsch.blogspot.com/2026/08/you-cannot-substitute-crude-oil-or-gold.html", "You Cannot Substitute Crude Oil or Gold. That Is 40% of India&#x27;s Import Bill."),
    ("https://masaladeutsch.blogspot.com/2026/08/chemical-import-substitution-hsn-8-registry.html", "Which of 827 Chemical HSN-8 Codes Are Real Substitution Targets"),
    ("https://masaladeutsch.blogspot.com/2026/08/five-year-synthesis-trade-currency.html", "Five-Year Synthesis: Trade, Currency &amp; Policy, FY2021-22 to FY2025-26"),
    ("https://masaladeutsch.blogspot.com/2026/08/indias-8-digit-trade-book-searchable.html", "India&#x27;s 8-Digit Trade Book, Searchable"),
]

TITLE = ('Eight Open-Source Tools for India&rsquo;s Trade Data, From HS Chapters to Chemical Codes and Forex, '
         'and Which One Answers Which Question')
STANDFIRST = ('Eight small repositories turn TRADESTAT, the Export-Import Data Bank, RBI and MoSPI data into files you can query, '
              'each answering a different question about India&rsquo;s trade. '
              'This guide shows what each one does, the command to start with, and where its numbers stop being reliable.')

build('Open-Source Tools &middot; 12 November 2026', TITLE, STANDFIRST, body, sources, related, OUT)
print('built', OUT)
