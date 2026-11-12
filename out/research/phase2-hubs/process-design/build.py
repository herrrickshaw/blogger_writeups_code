"""Hub: open-source process-design kits (replaces nine separate how-to guides).
Build from the repo root: PYTHONPATH=tools/postbuild python3 out/research/phase2-hubs/process-design/build.py
Every figure, command and caveat is taken from the source guides listed in hubs.json under "process-design":
posts/how-to-use-{ethanol-design-opensource, lignocellulosic-ethanol, cbg-design-opensource-size,
coal-to-urea-design, biomass-to-syngas-opensource, refinery-design-opensource, lng-design-opensource-size,
saf-monitoring-system-track}.html and out/research/phase2-hubs/sources/drafts/lng-cost.html."""
import html
import sys
sys.path.insert(0, 'tools/postbuild')
from buildpost import build

OUT = 'out/post-hub-process-design.html'
GH = 'https://github.com/herrrickshaw/'


def tw(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f'<div class="gb-tblwrap"><table class="gb-table"><thead><tr>{h}</tr></thead><tbody>{r}</tbody></table></div>'


def code(text):
    return '<pre><code>' + html.escape(text.strip('\n'), quote=False) + '</code></pre>'


def repo(name):
    return f'<a href="{GH}{name}">github.com/herrrickshaw/{name}</a>'


def tool(name, heading, paras, cmd, cmd_note, limit):
    out = [f'<h3>{heading}</h3>']
    out += [f'<p>{p}</p>' for p in paras]
    out.append(f'<p>{cmd_note}</p>')
    out.append(code(cmd))
    out.append(f'<p><strong>Main limitation.</strong> {limit}</p>')
    out.append(f'<p>Code: {repo(name)}</p>')
    return "\n".join(out)


stats = '''<div class="gb-stats">
<div class="gb-stat"><b>9</b><span>open-source tools: seven plant-sizing kits, one LNG cost model and one SAF tracking app</span></div>
<div class="gb-stat"><b>1.12x</b><span>2G ethanol model yield against IOCL Panipat&rsquo;s published design figure</span></div>
<div class="gb-stat"><b>&minus;13.6%</b><span>coal-to-urea model output against Talcher Fertilizers&rsquo; published 1.27 mtpa</span></div>
<div class="gb-stat"><b>2.93x</b><span>CBG from an all-straw feed against the published Barsana figure; an all-dung feed lands at 10.14 vs 10 t/day</span></div>
</div>'''

choose = tw(["Tool", "What it does", "Use it when"], [
    [f'<a href="{GH}ethanol-design-opensource">ethanol-design-opensource</a>',
     "Sizes a first-generation fuel-ethanol distillery, from cane molasses or grain to anhydrous ethanol and spent wash or DDGS",
     "You need a first sketch of a molasses or grain distillery for E20-style blending"],
    [f'<a href="{GH}lignocellulosic-ethanol-opensource">lignocellulosic-ethanol-opensource</a>',
     "Sizes a second-generation (cellulosic) ethanol plant on rice straw, including lignin residue for process heat",
     "You want a straw-to-ethanol yield and size to set against IOCL Panipat"],
    [f'<a href="{GH}cbg-design-opensource">cbg-design-opensource</a>',
     "Estimates compressed biogas output from a feedstock mix, through digestion, upgrading and 250 bar compression",
     "You are screening a SATAT-scheme CBG plant and its dung/straw split"],
    [f'<a href="{GH}coal-to-urea-design-opensource">coal-to-urea-design-opensource</a>',
     "Sizes a coal gasification to urea complex: six units on one mass basis",
     "You want a ballpark for a complex like Talcher and its surplus CO2"],
    [f'<a href="{GH}biomass-to-syngas-opensource">biomass-to-syngas-opensource</a>',
     "Estimates syngas, tar and gas quality from a biomass gasifier and rates the gas for power or chemicals",
     "You want to know whether straw syngas suits an engine or a synthesis plant"],
    [f'<a href="{GH}refinery-design-opensource">refinery-design-opensource</a>',
     "Runs crudes through a conceptual refinery: yields, sulfur, FCC regenerator temperature, margin, Nelson complexity",
     "You are testing which crudes or blends a refinery can take"],
    [f'<a href="{GH}lng-design-opensource">lng-design-opensource</a>',
     "Sizes an LNG liquefaction train stage by stage on one feed basis, plus LPG import and regas terminal examples",
     "You need a first-pass size and compressor power before a licensed simulator run"],
    [f'<a href="{GH}lng-cost">lng-cost</a>',
     "Builds a delivered LNG cost in USD/MMBtu from liquefaction, shipping and regas, with an optional bottom-up capex",
     "You want a screening cost stack for a supply route, with your own inputs"],
    [f'<a href="{GH}saf-monitoring-system">saf-monitoring-system</a>',
     "Tracks SAF feedstock, batches, GHG intensity, ASTM pathway checks, ReFuelEU blending and CORSIA credits",
     "You want a worked data model for SAF compliance tracking, on mock data"],
])

install = code('''
git clone https://github.com/herrrickshaw/cbg-design-opensource.git
cd cbg-design-opensource
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
''')

t_ethanol = tool(
    "ethanol-design-opensource", "1. ethanol-design-opensource: a first-generation distillery",
    ["This kit sizes a first-generation fuel-ethanol distillery for E20-style blending. You give it the feedstock "
     "(cane molasses or milled grain) and the plant size. It works through starch hydrolysis, batch fermentation, a "
     "shortcut Fenske-Underwood-Gilliland distillation column and 3A molecular-sieve dehydration, and reports the "
     "co-product stream: spent wash for molasses, DDGS for grain. It checks its results against published figures and "
     "the BIS anhydrous ethanol specification.",
     "In the demo, 1,000 t/day of cane gave 72.5 t/day of B-heavy molasses and 21,751 L/day of ethanol: 21.75 L per "
     "tonne of cane, the same as the published figure. It went on to size a 512 m3 fermenter and a 15-stage column, "
     "and 44 tests passed. A grain example covers milled and broken rice and maize at 500 t/day."],
    "python examples/full_chain_worked_example.py",
    "The molasses worked example, after the install above:",
    "Grain yields overshoot published plants by 13 to 21 percent. The guide traces this to a lab-optimised 95% "
    "hydrolysis efficiency combined with a molasses-calibrated fermentation efficiency. The molasses route matches "
    "its published figure because it was calibrated on it, so that match is not independent proof. One sieve bed came "
    "out with a height-to-diameter ratio of 35.9, and the tool itself advises splitting it across parallel vessels.")

t_2g = tool(
    "lignocellulosic-ethanol-opensource", "2. lignocellulosic-ethanol-opensource: a 2G ethanol plant on rice straw",
    ["This kit sizes a cellulosic ethanol biorefinery: pretreatment, enzymatic hydrolysis, C5 and C6 co-fermentation, "
     "distillation and dehydration. It also reports how much lignin residue is left for process heat. The demo runs "
     "rice straw at 425.7 t/day, the scale of IOCL Panipat, India&rsquo;s first commercial 2G plant.",
     "The worked example prints 72.6 t/day of xylose and 124.2 t/day of glucose, then 112,411 L/day of ethanol "
     "(264.1 L per tonne; 64% from glucose and 36% from xylose), a 15-stage column at 94.0% w/w, and 177.7 t/day of "
     "lignin residue at 14.1 MJ/kg. 40 tests passed."],
    "python examples/full_chain_worked_example.py",
    "The Panipat-scale run, after the install above:",
    "The model gives 264.1 L/t, 1.12x Panipat&rsquo;s published design figure of 234.9 L/t. It is 1.04x Clariant&rsquo;s "
    "achieved figure at Podari, but that plant uses wheat straw and a different pretreatment, so the guide treats it "
    "as context, not a resolved discrepancy. The model does not predict commissioning performance: Panipat ran at "
    "only 62% of design throughput in November and December 2025.")

t_cbg = tool(
    "cbg-design-opensource", "3. cbg-design-opensource: a compressed biogas plant",
    ["This kit gives a first, traceable estimate of how much compressed biogas (CBG) a plant makes from a given "
     "feedstock. It covers anaerobic digestion (Buswell equation), upgrading to the IS 16087 gas standard, "
     "multistage compression to 250 bar and the digestate left over. The demo checks it against Barsana Phase I, a "
     "published plant that takes in 225 tonnes a day and makes about 10 tonnes a day of CBG.",
     "The worked example prints CBG output for dung/straw splits from 0% to 100% dung. At a 50/50 split it gives "
     "49,102 Nm3/day of raw biogas at 50.4% methane, upgrading to 98.0% methane that meets IS 16087 (about 583 kW), 4-stage compression "
     "to 250 bar at about 277 kW, and 609 m3/day of digestate. 32 tests passed."],
    "python examples/full_chain_worked_example.py",
    "The Barsana-scale run, after the install above:",
    "Only a 100% dung feed lands near the published plant (10.14 vs 10 t/day). Every mix with straw overshoots, up "
    "to 29.31 t/day for pure straw, because straw&rsquo;s calibrated gas yield is about 3x dung&rsquo;s. Barsana&rsquo;s "
    "real feedstock mix is not public, so the gap is unresolved. The guide says to treat it as a sanity check, not a "
    "guarantee of what a real plant will produce.")

t_urea = tool(
    "coal-to-urea-design-opensource", "4. coal-to-urea-design-opensource: a coal gasification to urea complex",
    ["Urea needs ammonia and CO2, and a coal-to-urea complex gets both from one gasification block. This kit sizes "
     "the chain on one consistent mass basis: gasifier, water-gas shift, acid gas removal, air separation, ammonia "
     "synthesis and urea synthesis.",
     "The demo feeds 145 kg/s of Indian high-ash coal. It reports 8,584 mol/s of syngas at 64.1% cold gas efficiency, "
     "shift conversion of 79.7% (high temperature) and 85.9% cumulative, 190.2 kg/s of CO2 captured, 59.1 kg/s of "
     "ammonia and 34.8 kg/s of urea, or 1.10 mtpa. 37 tests passed in about 3.5 seconds."],
    "python examples/full_chain_worked_example.py",
    "The whole chain and the Talcher comparison, after the install above:",
    "The result is 13.6% below Talcher Fertilizers&rsquo; published 1.27 mtpa, and the guide claims no accuracy beyond "
    "ballpark. 3,330 mol/s of captured CO2 (77%) is surplus after urea, which the model flags but does not solve. "
    "Methanation polishing and the recycle and stripping duty for unconverted CO2 and ammonia are not modelled, and "
    "conversions are single-pass. The repo as checked had no LICENSE file, so check the repo page before reusing the code.")

t_syngas = tool(
    "biomass-to-syngas-opensource", "5. biomass-to-syngas-opensource: a biomass gasifier",
    ["This kit characterises the feedstock, runs a gasifier at a chosen temperature and type (downdraft, fluidized "
     "bed or updraft), sizes tar and particulate cleanup, and screens the syngas for its likely use.",
     "For 100 t/day of rice straw in a fluidized bed at 850 C it reports 87.43 mol/s of syngas, 75.8% cold gas "
     "efficiency, tar cut from 29.40 g/s to 0.882 g/s after cleanup, an H2:CO ratio of 1.73:1, an LHV of "
     "5.71 MJ/Nm3 and 50.2% inert gas. Because the inert share is that high, it recommends direct combustion or "
     "gas-engine power only, not chemical synthesis. 18 tests passed in about 1.3 seconds."],
    "python examples/full_chain_worked_example.py",
    "The 100 t/day rice-straw run, after the install above:",
    "In the demo, tar stayed at 29.39 g/s and cold gas efficiency at 75.8% from 750 to 950 C. Tar is a lookup by "
    "gasifier type, not a temperature model, so do not use it to find an optimum temperature. The README notes fixed "
    "conversions and no rate-based cleanup sizing, and straw collection and logistics, the real barrier, are outside "
    "it. The repo as checked had no LICENSE file.")

t_refinery = tool(
    "refinery-design-opensource", "6. refinery-design-opensource: what a crude does to a refinery",
    ["This kit asks which crudes a refinery can run, where the fluid catalytic cracker (FCC) overheats and how "
     "complex the plant is. It covers assays, distillation, FCC heat balance and riser behaviour, blending, gross "
     "refining margin, petrochemicals and a Nelson complexity check against Paradip. It has 11 worked example "
     "scripts and an MIT licence.",
     "The main example runs eight crudes through one refinery. Bakken (API 44.0) gives 95.1% light products and a "
     "regenerator at 682 C; Cold Lake Blend (API 19.5) gives 72.3% light products, 16.7% petcoke and 867 C. Six of "
     "the eight crudes carry a warning for FCC regenerator temperature. Blending Cold Lake into Azeri BTC raises the "
     "regenerator from 677 C at 0% to 800 C at 50%, past the roughly 760 C limit."],
    "python examples/full_refinery_worked_example.py",
    "Eight crudes through one refinery (install with <code>pip install -e \".[dev]\"</code> in a virtual environment):",
    "Conceptual sizing, not a substitute for a licensed simulator or licensor design. FCC kinetics are calibrated to "
    "typical published ranges, not fitted to plant data, and feed-quality effects are directional heuristics. The "
    "Paradip Nelson index comes out between 7.55 and 11.92 against a published 10.6, and brackets it only when "
    "ambiguous units are counted. Reforming, hydrocracking, alkylation, sulfur recovery and the hydrogen plant are not "
    "covered. The README quotes 263 tests; the demo ran 267, all passing.")

t_lng = tool(
    "lng-design-opensource", "7. lng-design-opensource: an LNG liquefaction train",
    ["This kit sizes the stages of a liquefaction train from public correlations, all on one feed basis: inlet "
     "separator, amine absorber, molecular sieve, air cooler, propane pre-cool, main heat exchanger, end flash, "
     "storage and refrigerant make-up. It also has LPG import and regasification terminal examples, and a Streamlit app.",
     "For a 2 mtpa train the example reports a feed of 63.4 kg/s, propane pre-cool duty of 12,168 kW at minus 43.0 C, "
     "main exchanger duty of 11,027 kW, LNG out at 60.4 kg/s and minus 164.7 C, 63,827 m3 of storage and total "
     "compressor power of 36,549 kW. Install it with <code>pip install -r requirements.txt</code>."],
    "python examples/full_train_worked_example.py",
    "The 2 mtpa full-train example:",
    "The README calls it a screening tool, not a rate-based simulator, and says to validate in HYSYS, PRO/II or IDAES. "
    "A sweep stopped at 4 mtpa with a ValueError because one molecular sieve vessel exceeded the largest standard "
    "size, so parallel units are needed. Sub-cooling duty (10,844 kW at 2 mtpa) needs a dedicated loop this module "
    "does not size. The full test suite is slow: 279 tests passed in 5 min 28 s. Note one unexplained difference in "
    "the guide: the sweep function reported 36,871 kW of compressor power at 2 mtpa, while the full-train example "
    "reported 36,549 kW.")

t_lngcost = tool(
    "lng-cost", "8. lng-cost: a screening delivered LNG cost",
    ["This is a small Python package and command-line tool with no runtime dependencies beyond the standard library "
     "(Python 3.9 or newer). It adds three blocks into a delivered cost in USD/MMBtu: liquefaction (annuitised "
     "capex, fixed O&amp;M, and feed gas grossed up for fuel and loss), shipping (a round-trip voyage with boil-off "
     "and port days) and regas (a levelised charge). An optional bottom-up mode builds capex from steel, cement, "
     "labour and equipment for five regions, and runs a +/-20% sensitivity on each driver.",
     "With its defaults (5 Mtpa, 5,000 nm one way) it prints a delivered cost of 8.49 USD/MMBtu. In the bottom-up "
     "mode, a 20% move in the equipment index shifts delivered cost by 0.45 USD/MMBtu, labour by 0.30, steel by 0.05 "
     "and cement by 0.001. 13 tests passed in 0.08 s."],
    "lng-cost --distance-nm 9000 --capex-per-tpa 1000",
    "The README example, after <code>pip install -e '.[dev]'</code>:",
    "Every default, quantity, price and regional multiplier is an illustrative placeholder, not a sourced benchmark, "
    "and no figure should be quoted as an industry number. Accuracy is screening level, roughly AACE Class 5. There is "
    "no tax, royalty, inflation or financing during construction; no fleet sizing, terminal tank, jetty, pipeline or "
    "upstream cost; and no uncertainty analysis. Not investment advice.")

t_saf = tool(
    "saf-monitoring-system", "9. saf-monitoring-system: tracking SAF batches against blending and credit rules",
    ["This is an app, not a sizing kit. A FastAPI backend with SQLite models feedstock deliveries, production "
     "batches, ASTM D7566 pathways, SAF certificates, airline offtakes and deliveries, a CORSIA-style credit ledger "
     "and ReFuelEU blending records, and a React frontend shows dashboards for each. On first start it seeds about "
     "twelve months of mock data.",
     "In the demo 39 tests passed in 3.95 seconds. The blending endpoint flagged one of three seeded airports below "
     "the repo&rsquo;s 2.0% mandate, which the seeder does on purpose to show the flag. A worked CORSIA calculation with "
     "the repo&rsquo;s own default for used-cooking-oil HEFA-SPK (13.9 gCO2e/MJ) gave an 84.38% reduction against an "
     "89 gCO2e/MJ baseline."],
    "uvicorn app.main:app --port 8000",
    "Start the API from the <code>backend</code> folder after <code>pip install -r requirements.txt</code>; it seeds mock data on first run and serves interactive docs at localhost:8000/docs:",
    "Not legal advice. The repository is archived, so its regulatory defaults (mandate shares, baselines, pathway "
    "limits, lifecycle values) are frozen at whatever the author entered, and the guide did not verify any of them. "
    "Everything it shows on first start is mock data, not real plant, airline or credit data. The React frontend and "
    "the PDF and Excel report paths were not run in the demo.")

worked = '''<p>This example is from the lng-cost guide, run from a fresh clone in a throwaway virtual environment on 29 October 2026. It shows how a screening cost stack is built and how one input moves it.</p>
<p><strong>Step 1: install and test.</strong></p>
''' + code('''
git clone https://github.com/herrrickshaw/lng-cost.git
cd lng-cost
pip install -e '.[dev]'
''') + '''
<p>pytest passed 13 tests in 0.08 s.</p>
<p><strong>Step 2: run the defaults.</strong> The defaults are a 5 Mtpa plant at 900 USD/tpa liquefaction capex, feed gas at 3.50 USD/MMBtu with 9% fuel and loss, a 10% discount rate over 20 years, 5,000 nm one way in a 174,000 m3 vessel at 17 knots chartered at 90,000 USD/day, and regas capex of 150 USD/tpa.</p>
''' + code('''
lng-cost
Feed gas (incl. fuel & loss)        3.85  USD/MMBtu
Liquefaction capital charge         2.21  USD/MMBtu
Liquefaction fixed O&M              0.56  USD/MMBtu
Liquefaction other variable         0.25  USD/MMBtu
FOB cost                            6.87  USD/MMBtu
Shipping                            0.98  USD/MMBtu
Regasification                      0.64  USD/MMBtu
DELIVERED cost                      8.49  USD/MMBtu
Round trip: 27.5 days, boil-off 1.23%
Defaults are illustrative placeholders; see README.
''') + '''
<p><strong>Step 3: change distance and capex.</strong> The README example lengthens the voyage to 9,000 nm and raises liquefaction capex to 1,000 USD/tpa.</p>
''' + code('lng-cost --distance-nm 9000 --capex-per-tpa 1000') + '''
<p>Shipping rises to 1.73 and the delivered cost to 9.55 USD/MMBtu; the round trip is 47.1 days. Through the Python API, a distance sweep at 3,000, 6,000, 9,000 and 12,000 nm gave delivered costs of 7.88, 8.44, 9.00 and 9.57 USD/MMBtu, about 0.19 USD/MMBtu per 1,000 nm with those inputs.</p>
<p><strong>A difference to know about.</strong> The README&rsquo;s Python example prints 9.0 at 9,000 nm, while the command-line example with the same distance and capex prints 9.55. The guide traced the gap: the Python example sets feed gas at 3.0, while the command line keeps the 3.50 default, and 0.50 of feed gas grossed up by 1/(1&minus;0.09) is 0.55.</p>
<p><strong>Step 4, optional: bottom-up capex.</strong> <code>lng-cost --bottom-up --region australia --steel-price 2400 --labour-rate 90 --sensitivity</code> built liquefaction capex of 1,311 USD per tonne a year and a delivered cost of 10.06 USD/MMBtu. Equipment and labour dominated; cement was a rounding error. All of these are placeholder inputs, so the point is the method, not the numbers.</p>'''

donot = '''<ul>
<li><strong>They are not engineering design.</strong> Every sizing guide says so: no detailed design, equipment purchase or bank-grade feasibility. The LNG and refinery guides say to validate in a licensed simulator; the LNG README names HYSYS, PRO/II and IDAES.</li>
<li><strong>They use literature correlations, not vendor data.</strong> The ethanol, 2G ethanol and CBG guides state this outright.</li>
<li><strong>A match with a real plant is not always proof.</strong> The molasses route matches its published figure because it was calibrated on it. The CBG model matches Barsana only with an all-dung feed, and Barsana&rsquo;s real mix is not public.</li>
<li><strong>They do not predict operation.</strong> The 2G model gives a design yield; it does not explain why Panipat ran at 62% of design throughput in late 2025.</li>
<li><strong>Cost numbers are placeholders.</strong> lng-cost&rsquo;s defaults are illustrative, its own reference list is unverified, and it is not investment advice.</li>
<li><strong>The SAF app is not a compliance system.</strong> It is not legal advice, runs on mock data and is archived, so its regulatory values will not follow rule changes.</li>
<li><strong>Licences differ.</strong> The refinery kit is MIT-licensed. The coal-to-urea and biomass repos had no LICENSE file when checked. Check each repo page before reusing code.</li>
</ul>'''

body = f"""{stats}

<p>These nine repositories give a first, traceable estimate for a plant before anyone pays for a licensed simulator or vendor quotes. Seven size a plant from public correlations: a first-generation ethanol distillery, a second-generation (cellulosic) ethanol plant, a compressed biogas plant, a coal-to-urea complex, a biomass gasifier, a refinery and an LNG train. One builds a delivered LNG cost. The ninth is different: an app that tracks sustainable aviation fuel (SAF) batches against blending and carbon-credit rules.</p>

<p>The guides name the same readers each time: students and analysts learning how a plant is sized, project teams sketching early feasibility, and engineers who want a transparent baseline before a licensed simulator run. Several check themselves against a named Indian plant, such as IOCL Panipat, Barsana, Talcher or Paradip, and report where they miss. Each has a Python core that runs locally. None of the guides lists an API key or paid software as a requirement.</p>

<h2 class="gb-h2">Which tool for which job</h2>
{choose}

<h2 class="gb-h2">Which one to start with</h2>
<p>If you have a specific plant in mind, pick the matching row above. If you want to see how these models behave first, two are the quickest to try. lng-cost needs nothing beyond the Python standard library, and its 13 tests passed in 0.08 s. biomass-to-syngas-opensource&rsquo;s 18 tests passed in about 1.3 seconds. The LNG train kit is the slowest to verify: its full suite took 5 min 28 s, and the guide suggests running single test files while exploring.</p>
<p>The ethanol, 2G ethanol, CBG, coal-to-urea and biomass kits install the same way. They need Python 3.10 or newer; pip pulls in CoolProp, pandas and the rest from pyproject.toml, and no internet is needed to run the sizing code after the first install. Swap the repo name for the kit you want:</p>
{install}

<h2 class="gb-h2">The nine tools</h2>
{t_ethanol}

{t_2g}

{t_cbg}

{t_urea}

{t_syngas}

{t_refinery}

{t_lng}

{t_lngcost}

{t_saf}

<h2 class="gb-h2">Worked example: a delivered LNG cost with lng-cost</h2>
{worked}

<h2 class="gb-h2">What these tools do not do</h2>
{donot}
"""

links = "; ".join(repo(r) for r in [
    "ethanol-design-opensource", "lignocellulosic-ethanol-opensource", "cbg-design-opensource",
    "coal-to-urea-design-opensource", "biomass-to-syngas-opensource", "refinery-design-opensource",
    "lng-design-opensource", "lng-cost", "saf-monitoring-system"])

sources = ("This page replaces the nine separate how-to guides this blog published for these tools, one per repository. "
           "Everything here is taken from those guides, which drew on each repository&rsquo;s README, docs and examples and on "
           "demo runs: 18 October 2026 for the seven sizing kits, 23 October 2026 for saf-monitoring-system and "
           "29 October 2026 for lng-cost. Where a guide reported a gap between a README and the run (refinery test count, "
           "lng-cost&rsquo;s two 9,000 nm results), both are given above. Repositories: " + links + ".")

related = [
    ("https://masaladeutsch.blogspot.com/2026/11/how-to-use-process-safety-design.html", "How to Use the Process-Safety Design Toolkit: A Complete Walkthrough, Command by Command"),
    ("https://masaladeutsch.blogspot.com/2026/08/interest-subvention-built-499-ethanol.html", "Interest Subvention Built 499 Ethanol Distilleries. Viability Gap Funding Built One Working 2G Plant."),
    ("https://masaladeutsch.blogspot.com/2026/09/india-has-132-compressed-biogas-plants.html", "India Has 132 Compressed Biogas Plants Running. The Pipeline to Actually Use That Gas Reaches 17 of Them."),
    ("https://masaladeutsch.blogspot.com/2026/09/the-reactor-nobody-names-how-coal.html", "The Reactor Nobody Names: How Coal Becomes Syngas, and Why India&#x27;s Flagship Plant Runs on Someone Else&#x27;s Technology"),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-cheapest-lng-capacity-is-extra.html", "India&#x27;s Cheapest LNG Capacity Is an Extra Tank at Dahej. Its Newer Terminals Run a Quarter Full"),
]

TITLE = "Nine Open-Source Tools for Sizing and Costing India&rsquo;s Biofuel, Gas and Refining Plants, and Which One to Start With"
build("Open-Source Tools &middot; 12 November 2026", TITLE,
      "Seven free Python kits size an ethanol, biogas, urea, gasifier, refinery or LNG plant from public correlations, one prices "
      "delivered LNG, and one tracks SAF batches against blending and credit rules. "
      "Here is what each does, the command to run first, and where each one says it stops being reliable.",
      body, sources, related, OUT)
print("built", OUT)
