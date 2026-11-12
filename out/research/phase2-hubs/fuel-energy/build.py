"""Hub post: India fuel-retail and energy-data tools (replaces seven separate how-to guides).
Build from the repo root:
  PYTHONPATH=tools/postbuild python3 out/research/phase2-hubs/fuel-energy/build.py
Every statement, command and figure below comes from the seven source guides listed in
out/research/phase2-hubs/hubs.json under "fuel-energy". Commands are copied verbatim from
the guides' <pre> blocks and HTML-escaped here.
"""
import html
from buildpost import build

OUT = 'out/post-hub-fuel-energy.html'
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
C_PUMP_MAP = r'''
cd fuel-station-gap-analysis && python3 -m http.server 8001
'''
C_PUMP_CLONE = r'''
git clone https://github.com/herrrickshaw/fuel-retail-outlets.git
cd fuel-retail-outlets
'''
C_PUMP_DEDUP = r'''
python3 -I - <<'E'
import gzip,json,collections
p='api-data-integration/outlet_data_ssri_complete/ssri_pumps_raw_20261016.jsonl.gz'
rows=[json.loads(l) for l in gzip.open(p,'rt') if l.strip()]
k={}
for r in rows:
    key=(r['name'],r['address'],r['company'],r['latitude'],r['longitude'])
    if key not in k or r['id']>k[key]['id']: k[key]=r
u=list(k.values())
print(len(rows),len(u),len(rows)-len(u))
print(collections.Counter(r['company'] for r in u).most_common(5))
E
'''
C_CNG = r'''
python3 - <<'E'
import csv,gzip,collections
rows=list(csv.DictReader(gzip.open('data/outlets_cgd.csv.gz','rt')))
print(len(rows));print(collections.Counter(r['cgd_status'] for r in rows))
print(sum(r['has_cng']=='True' for r in rows))
E
'''
C_OMC = r'''
python3 omc_model.py
'''
C_PPAC = r'''
python3 -c "import pandas as pd;print(pd.read_csv('annual_fy2025-26_h1/csv/Table_4.7_grossrefiningmargins_grm_ofrefineries.csv',skiprows=2).head(8))"
'''
C_VEH = r'''
python scripts/build_model.py
python scripts/recalc.py outputs/EV_CNG_Diesel_Ethanol_Vehicle_Cost_Model.xlsx
'''
C_UCO = r'''
uvicorn app.main:app --port 8000
# interactive docs: http://127.0.0.1:8000/docs
'''
C_DISCOM = r'''
python3.13 discom_debt_calculator.py
'''

# ---------------------------------------------------------------- outputs reported by the guide
O_DELHI = r'''
raw rows with state == 'Delhi'  : 21,939
  of which district 'New Delhi' : 21,572, all IOCL-heavy
  sitting on only 57 distinct coordinates (3,986 identical rows on each of several points)
after dedup (name+address+company+lat+lon): 419
'''
O_STATES = r'''
state             pumps   per 100k people   per 1000 km2
Uttar Pradesh      8,915        4.5              37.0
Maharashtra        7,317        6.5              23.8
Tamil Nadu         5,812        8.1              44.7
Madhya Pradesh     5,320        7.3              17.3
Karnataka          5,268        8.6              27.5
-- lowest (states with 100+ pumps) --
Delhi                419        2.5             282.5
Bihar              2,779        2.7              29.5
West Bengal        2,522        2.8              28.4
Jharkhand          1,109        3.4              13.9
Assam              1,108        3.6              14.1
-- highest --
Arunachal Pradesh    201       14.6              2.4
Punjab             3,204       11.5              63.6
Haryana            2,855       11.3              64.6
Telangana          3,609       10.3              32.2
'''

stats = '''<div class="gb-stats">
<div class="gb-stat"><b>7 repos</b><span>covering petrol pumps, gas areas, ethanol blends, PPAC tables, running costs, used oil and discom debt</span></div>
<div class="gb-stat"><b>21%</b><span>of rows in the raw pump crawl (16 Oct 2026 file) are duplicates; remove them before counting anything</span></div>
<div class="gb-stat"><b>100 tables</b><span>from PPAC&rsquo;s Ready Reckoner (FY2025-26 H1 edition) as CSV, which still need cleaning</span></div>
<div class="gb-stat"><b>4% vs about 7%</b><span>the E20 mileage drop two models assume, against the extra litres implied by energy content alone</span></div>
</div>'''

which = table(['Tool', 'What it does', 'Use it when'], [
    ('fuel-retail-outlets', 'A crawl of petrol-pump records from a public API, with extractors, a map and a state gap-analysis heatmap',
     'You need a pump-level list with company, fuel type and location, to count or map outlets'),
    ('cng-cgd-retail-outlet-mapping', 'Links each petrol pump to the city gas distribution area and company authorised in its district',
     'You want to know which gas company may supply CNG at a given pump'),
    ('india-omc-fuel-fleet-model', 'Small Python models of oil-company pump income at E20, E25 and E30, and of the active vehicle fleet',
     'You want to test the ethanol-blend argument with assumptions you can edit'),
    ('ppac-ready-reckoner-data', 'PPAC Ready Reckoner tables extracted from PDF into CSV, with the extraction script',
     'You need refining margins, ethanol blending or fuel sales as tables, not a PDF'),
    ('vehicle_fuel_mileage', 'A formula-driven Excel model of cost per km for petrol (E20), diesel, CNG and EVs in six cities',
     'You want to compare running costs by fuel and city, with your own prices'),
    ('uco-ulo-tracking', 'A FastAPI and SQLite backend that tracks used cooking oil and used lubricating oil from source to buyer',
     'You are designing a traceability or used-oil EPR compliance system'),
    ('discom-debt-and-revenue-models', 'An archived one-file calculator of distribution-company debt under five scenarios',
     'You want to show which levers move discom debt, and what each does to a household bill'),
])

tools = ''.join([
    tool('fuel-retail-outlets', 'fuel-retail-outlets: where the petrol pumps are', [
        'This repo collects Indian petrol, diesel and CNG outlet listings from public sources: the SSRI petrol-pump API, the BPCL dealership locator and CashAtPOS. The committed crawl is a gzipped JSON-lines file dated 16 October 2026. Two small web apps show the outlets on a map and draw a state-level coverage heatmap.',
        'The raw crawl must be deduplicated before use; the worked example below shows how and what changes. The data is indicative, for planning and visualisation, and the outlet records are public business listings.',
    ], C_PUMP_MAP, 'Serve the gap-analysis heatmap, then visit http://localhost:8001 (the page loads its map tiles from the internet; the guide did not open it):',
        'It is not an official registry. Even after cleaning, the guide counted 82,602 outlets against a PPAC baseline of 103,450 (May 2026) quoted in the repo&rsquo;s notes, about 80% coverage. State names come in 53 spellings, and all 9,007 Nayara outlets have the state &ldquo;unknown&rdquo;.'),

    tool('cng-cgd-retail-outlet-mapping', 'cng-cgd-retail-outlet-mapping: which gas company may supply each pump', [
        'The repo parses the regulator PNGRB&rsquo;s list of authorised City Gas Distribution geographical areas (309 areas, 58 companies). It assigns each petrol pump to a district by point-in-polygon and publishes the result as a table of outlets plus a self-contained map page that works offline.',
        'The table flags pumps already equipped for CNG, so you can see the CNG share by state or by authorised company. The guide&rsquo;s run had 17 of 17 tests passing, and the headline counts reproduced.',
    ], C_CNG, 'Summarise the linkage table: outlet count, link status and CNG-equipped outlets:',
        'Authorisation is not pipeline reach: the list does not say how far a company&rsquo;s network has actually been built. The data is a 22 July 2026 snapshot running through bidding round 12A. The full pipeline cannot be rerun from a fresh clone, because a 47 MB district map and the regulator PDF are not committed.'),

    tool('india-omc-fuel-fleet-model', 'india-omc-fuel-fleet-model: ethanol blends and pump income', [
        'The repo models the retail margin of India&rsquo;s oil marketing companies on petrol and diesel from PPAC reference data, and what changes at E20, E25 and E30. The mechanism: blended fuel has less energy per litre, so drivers buy more litres, which raises pump throughput and so oil-company income.',
        'Other scripts estimate how many vehicles are actually driven from fuel sales, compare the energy content of blends and split the extra spend between excise, VAT, dealers and oil companies. The main scripts use only the Python standard library; in the guide&rsquo;s run the main model took 0.05 seconds. Results land in outputs/ as CSV and Markdown.',
    ], C_OMC, 'Run the profitability and blend-scenario model (five lines of output, plus files under outputs/):',
        'The README calls the headline results illustrative and the oil-company margin the key lever. The model assumes a 4% mileage drop at E20, while the energy-content script implies about 6.8% less energy per litre and 7.3% more litres; that choice drives the extra-income result.'),

    tool('ppac-ready-reckoner-data', 'ppac-ready-reckoner-data: PPAC&rsquo;s statistics as CSV', [
        'The repo holds the tables of the PPAC Ready Reckoner, FY2025-26 H1 edition, as 100 CSV files, from Table 1.1 (economy indicators) to Table 6.10 (ethanol blending). They include gross refining margins by refinery and state-wise fuel sales. An index.csv maps each file to its table number, caption and page.',
        'The script extract_rr.py rebuilds the CSVs from a Ready Reckoner PDF using pdfplumber, so it can be pointed at the next edition. In the guide&rsquo;s run all 100 CSVs loaded in pandas.',
    ], C_PPAC, 'Read one table, gross refining margins by refiner and financial year:',
        'The tables are machine-extracted and need cleaning: some state names lost their spaces, a Grand Total row is shifted one column, &ldquo;**&rdquo; and &ldquo;#&rdquo; source markers sit in the data, and numbers use Indian digit grouping. Only one edition is covered, the PDF is not in the repo, and the guide found no PPAC licence terms in it.'),

    tool('vehicle_fuel_mileage', 'vehicle_fuel_mileage: running cost per km by fuel', [
        'The repo builds an 11-sheet Excel cost model: cities, cost per km, ethanol impact, total cost of ownership, tax structure, fleet sales, an oil-company price board and exchequer revenue, on a July 2026 price basis. You choose a city, change inputs such as the E20 mileage drop or usage, and the workbook reprices.',
        'A second script extracts and analyses 303 certified car fuel-efficiency declarations from the SIAM PDF, which the model uses to calibrate its mileage assumptions. The guide&rsquo;s run had 19 tests passing and all 21 built-in checks reading PASS after recalculation.',
    ], C_VEH, 'Build the workbook, then recalculate it so the values can be read (recalc.py uses LibreOffice; you can also open the file in Excel):',
        'Prices are a July 2026 snapshot, so update them before drawing conclusions. The workbook has no values until it is recalculated. The declaration data is for passenger vehicles as on 1 April 2020, with only 11 CNG, 8 hybrid and 1 electric entry, so those averages are thin.'),

    tool('uco-ulo-tracking', 'uco-ulo-tracking: chain of custody for used cooking and lubricating oil', [
        'A FastAPI service over SQLite, with a React front end, tracks used cooking oil and used lubricating oil from generator to buyer: collection manifests, lots, processing batches, dispatches and shipments, with the quality fields regulators care about. Named integrity checks flag things like suspiciously fresh cooking oil, a generator collecting over capacity, duplicate manifests, a lapsed registration or a broken mass balance. A SHA-256 hash-chained ledger makes edits to logged records detectable.',
        'A used-oil EPR module codes the arithmetic of the HOWM 2023 amendment: the producer target ladder, the Y-2 basis, certificate weightage and the purchase cap. Every threshold is an editable default served at /api/compliance/parameters. On first start the API seeds six months of mock data with planted anomalies, so each check has something to show.',
    ], C_UCO, 'From the backend/ folder, start the API (it seeds the mock data on first run):',
        'Everything the guide showed is mock data. Several regulatory defaults are marked VERIFY or PLACEHOLDER, a flag is a prompt to investigate rather than a finding, and the ledger is tamper-evident on one node only, not tamper-proof. It is not legal or regulatory advice.'),

    tool('discom-debt-and-revenue-models', 'discom-debt-and-revenue-models: a debt scenario calculator', [
        'One standard-library Python script models a distribution company&rsquo;s year: energy billed after losses, revenue collected, cost of supply, subsidy actually received, interest, and closing debt. It compares five scenarios (status quo, tariff hikes, loss and collection reform, a combined UDAY-style path and an aggressive turnaround) and prints the household bill for each.',
        'Every input can be changed with a command-line flag, and --json gives machine-readable output. On the default, illustrative inputs only the aggressive scenario cut debt in the guide&rsquo;s run, at a 50.4% rise in the household bill. The repository is archived.',
    ], C_DISCOM, 'Run the default illustrative company (the guide used Python 3.13):',
        'It is a conceptual calculator, not a forecast: flat cost growth, one blended tariff, no demand response and a fixed subsidy. It crashes at start-up on Python 3.14 because of a bare percent sign in a help string. Its own interpretation text says operational reform cuts debt, but on the default inputs reform alone ends with more debt than a tariff-only path.'),
])

worked = f'''<h2 class="gb-h2">Worked example: counting petrol pumps by state (fuel-retail-outlets)</h2>
<p>This follows the fuel-retail-outlets guide. It read the committed crawl dated 16 October 2026 with the Python standard library on 19 October 2026. Nothing needs installing and no network call is made. The counts describe that crawl, not today&rsquo;s network.</p>
<p><strong>Step 1.</strong> Get the repository.</p>
{code(C_PUMP_CLONE)}
<p><strong>Step 2.</strong> Load the crawl and deduplicate it on name, address, company and coordinates, the way the repo&rsquo;s notes describe:</p>
{code(C_PUMP_DEDUP)}
<p>The guide reported <code>104945 82602 22343</code>: 104,945 rows, 82,602 outlets after deduplication and 22,343 duplicate rows removed (21.3%). The company counts that follow were BPCL 25,795, HPCL 23,543, IOCL 19,446, Nayara 9,007 and Unknown 2,504.</p>
<p><strong>Step 3.</strong> See why the step matters. Delhi, raw against cleaned:</p>
{code(O_DELHI)}
<p>The repo&rsquo;s own notes document this, but the 16 October file is still raw, so you have to apply the step yourself. The guide&rsquo;s count of 82,602 differs slightly from the 82,609 in the notes&rsquo; earlier snapshot.</p>
<p><strong>Step 4.</strong> Group the cleaned outlets by state and divide by the populations in the gap-analysis app&rsquo;s data.js. The guide&rsquo;s result:</p>
{code(O_STATES)}
<p><strong>How to read it.</strong> Delhi&rsquo;s low per-person figure is a dense city counted against its whole population, not a real gap. Only outlets whose state name could be matched (72,070 in the guide&rsquo;s check) feed this table, so states with spelling variants are understated and Nayara&rsquo;s outlets are missing. The populations are older census-based numbers. Treat the table as a first screen, not a verdict.</p>
'''

dont = '''<h2 class="gb-h2">What these tools do not do</h2>
<ul>
<li><strong>No official registers.</strong> The pump list and the gas-area table are indicative planning data. PPAC publishes the official outlet totals, and the guide says to check with the regulator before acting on any authorisation.</li>
<li><strong>No pipeline or supply data.</strong> An outlet inside an authorised gas area can be supplied by the authorised company, but the data does not say whether the pipe has reached it.</li>
<li><strong>No live prices.</strong> Pump prices in the crawl, the cost model&rsquo;s fuel prices and the PPAC tables are snapshots (July 2026 prices; the FY2025-26 H1 Ready Reckoner).</li>
<li><strong>No forecasts.</strong> The oil-company projection, the discom scenarios and the cost model run on stated assumptions. The guides call them illustrative or conceptual, not forecasts or investment advice.</li>
<li><strong>No real compliance data.</strong> uco-ulo-tracking runs on seeded mock data with fictional names, and its regulatory thresholds must be checked against the official notifications before anyone relies on them.</li>
<li><strong>No audited tables.</strong> The PPAC CSVs are extracted from PDF as printed and are not corrected or validated.</li>
<li><strong>Not every pipeline reruns from a clone.</strong> The gas-area pipeline needs files that are not committed, and the PPAC extractor needs the source PDF.</li>
</ul>
'''

disagree = '''<h2 class="gb-h2">Where the guides disagree</h2>
<ul>
<li><strong>Outlet counts.</strong> The fuel-retail-outlets guide gets 82,602 outlets after deduplicating the 16 October 2026 crawl. The cng-cgd guide&rsquo;s linkage table, built from a 22 July 2026 snapshot, has 82,593. The repo notes&rsquo; earlier figure is 82,609. The crawl dated 16 October 2026 is the newest.</li>
<li><strong>Raw source size.</strong> The cng-cgd guide says the SSRI source has grown to 107,380 raw records. The fuel-retail-outlets guide counts 104,945 rows in the 16 October 2026 file. The guides do not reconcile the two.</li>
<li><strong>CNG-equipped outlets.</strong> 11,198 in the file the cng-cgd guide read, against 11,194 in that repo&rsquo;s README; the guide puts the gap down to a later edit of the table.</li>
<li><strong>The E20 mileage drop.</strong> Both the oil-company model and the running-cost workbook default to 4%. The energy-content comparison implies about 6.8% less energy per litre. Both models let you change it, and the result moves with it.</li>
</ul>
'''

opening = '''<p>Questions about India&rsquo;s fuel and power systems often start with a simple count or sum. Where are the petrol pumps? Which gas company may sell CNG at this one? What does E20 do to oil-company income, or to the cost of driving a kilometre? How fast does a distribution company&rsquo;s debt grow if nothing changes? The seven open-source repositories on this page each answer one of these questions from public data, or from assumptions you can see and edit.</p>
<p>They are for energy analysts, planners of CNG and EV-charging sites, students, journalists and compliance teams. Some are datasets you load and clean, some are models you run, and one is a working backend for tracking used oil. Start with the table, then read the section on the tool you pick, including its main limitation.</p>
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

sources = ('This page replaces the seven separate how-to guides for these repositories, which were run between 19 and 29 October 2026 and published between 19 and 30 October 2026. '
           'Repositories: ' + '; '.join(repo(n) for n in [
               'fuel-retail-outlets', 'cng-cgd-retail-outlet-mapping', 'india-omc-fuel-fleet-model',
               'ppac-ready-reckoner-data', 'vehicle_fuel_mileage', 'uco-ulo-tracking',
               'discom-debt-and-revenue-models']) + '. '
           'Underlying data, as recorded by the repos: the SSRI petrol-pump API, the BPCL dealership locator and CashAtPOS; PNGRB&rsquo;s list of authorised City Gas Distribution areas; PPAC&rsquo;s Ready Reckoner and reference data; SIAM fuel-efficiency declarations. '
           'Figures quoted here are those the guides reported on the dates given, not current values. Not investment, legal or regulatory advice.')

related = [
    ("https://masaladeutsch.blogspot.com/2026/07/ethanol-blending-omc-books-e20-today-vs.html", "Ethanol Blending &amp; the OMC Books — E20 today vs E30 + SGST"),
    ("https://masaladeutsch.blogspot.com/2026/08/blending-on-budget-energy-density-and.html", "Blending on a Budget: Energy Density and Cost Per Kilometre, Across Four Fuel Pairs"),
    ("https://masaladeutsch.blogspot.com/2026/08/indias-used-oil-epr-wants-half-of-all.html", "India&#x27;s Used-Oil EPR Wants Half of All Lubricant Recycled by 2030. So Far, 119 Producers Have Actually Registered."),
    ("https://masaladeutsch.blogspot.com/2026/08/discom-debt-relief-token-charge.html", "DISCOM Debt Relief — Token Charge Calculator"),
]

TITLE = ('Seven Open-Source Tools for India&rsquo;s Fuel and Power Data: Petrol Pumps, CNG Areas, Ethanol Blends, '
         'Used Oil and Discom Debt, and Which One to Use')
STANDFIRST = ('Seven small repositories turn pump crawls, regulator lists, PPAC tables and stated assumptions into data and models you can run, '
              'each built for a different question about India&rsquo;s fuel and power. '
              'This guide shows what each one does, the command to start with, and the limit its own guide found.')

build('Open-Source Tools &middot; 12 November 2026', TITLE, STANDFIRST, body, sources, related, OUT)
print('built', OUT)
