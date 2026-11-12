"""Hub post: India governance, registry and regulation tools.
Build (from repo root): PYTHONPATH=tools/postbuild python3 out/research/phase2-hubs/governance/build.py

Replaces eight separate "How to use <repo>" guides (six live, two drafts; see hubs.json key "governance").
Every fact, command and figure below is taken from those guides; dates are the guides' own run dates."""
import html
import sys
sys.path.insert(0, 'tools/postbuild')
from buildpost import build

OUT = 'out/post-hub-governance.html'
GH = 'https://github.com/herrrickshaw/'

PRE_STYLE = ('overflow-x:auto;background:#f8f9fa;border:1px solid #dee2e6;border-radius:8px;'
             'padding:.75rem 1rem;font-size:.8em;line-height:1.45;white-space:pre')
H3_STYLE = "font-family:-apple-system,'Segoe UI',sans-serif;font-weight:700;font-size:1.12em;margin:1.8rem 0 .5rem"


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


# ---------------------------------------------------------------- tools
TOOLS = [
    dict(anchor="gazette", repo="gazette-translated-indexed",
         title="gazette-translated-indexed (Gazette Trail): the amendment chain of a notification",
         what="A SQLite citation index of gazette notifications and the links between them: amends, supersedes, corrigendum, rescinds, repeals, cites.",
         when="You need to know what a notification changed, and what later changed it.",
         paras=[
             "Gazette Trail is a citation index. Each notification is a row, and each link to another notification is a row in a <code>cross_reference</code> table. Read in both directions, the links give the lineage of a rule: what it changed and what changed it later. The links are drawn from quoted notification text using shared sentence templates. The pilot was CBIC customs notifications, since extended to 53 central ministries.",
             "In the guide&rsquo;s run of 19 October 2026, the committed seed files rebuilt a database of 2,637 notifications and 2,150 cross-references, and the repo&rsquo;s 197 tests passed. The README gave lower counts (2,591, 2,113 and 141 tests); the build is the newer figure. The database stores citations and summaries, not the PDFs. Network access is needed only to fetch PDFs from egazette.gov.in.",
         ],
         cmd_intro="Build the database from the seed files (after cloning and installing <code>requirements.txt</code> in a virtual environment).",
         cmd='''sqlite3 gazette.db < db/schema.sql
for f in db/seed_*.sql; do sqlite3 gazette.db < "$f"; done
sqlite3 gazette.db "PRAGMA foreign_key_check;"''',
         out="The foreign-key check prints nothing, which is the pass condition. The worked example below continues from here.",
         limit="Coverage is bounded: 53 ministries are modelled, 3 are documented as abandoned, and new notifications need the repo&rsquo;s freshness check. It is an index of public notifications, not legal advice; read the official notification on egazette.gov.in before acting."),
    dict(anchor="parliament", repo="lok-rajya-sabha-qa",
         title="lok-rajya-sabha-qa: who asks Parliament about what",
         what="A DuckDB ledger of Lok Sabha and Rajya Sabha questions since June 2024, summarised by party, ministry and state.",
         when="You want to see which ministries and subjects draw questions, by party or by state.",
         paras=[
             "The repo pulls every question since the 18th Lok Sabha convened in June 2024 from the public Parliament sources (sansad.in and rsdoc.nic.in), matches each to the asking member&rsquo;s party and state, and aggregates by party, ministry, state and topic. It also computes a &ldquo;lift&rdquo; score for each party-and-ministry pair: how much more a party asks about a ministry than its overall share would suggest. You can query <code>data/pq_ledger.duckdb</code>, open the Excel workbook, or open <code>site/index.html</code> for charts.",
             "When the guide queried it on 19 October 2026, the ledger held 59,381 questions (34,720 Lok Sabha and 24,661 Rajya Sabha) across 56 ministries. It needs Python 3.10 or newer and the <code>duckdb</code> package; no keys.",
         ],
         cmd_intro="Rank ministries by questions received (after <code>pip install duckdb</code>).",
         cmd='''python3 - <<'E'
import duckdb
c=duckdb.connect('data/pq_ledger.duckdb',read_only=True)
print(c.sql('select * from ministry_summary order by questions desc limit 6').fetchall())
E''',
         out="In the guide&rsquo;s run: Health and Family Welfare 3,550, Railways 2,900, Education 2,802, Agriculture and Farmers Welfare 2,754, Finance 2,253, Civil Aviation 2,129.",
         limit="The data has questions and metadata, not the answers; Lok Sabha rows carry only subject and ministry. Some build scripts need inputs that are not in the repo, so a full rebuild from a fresh clone is not possible. Question counts depend on seats, sessions attended and notice rules, and say nothing about the quality of a party or an MP."),
    dict(anchor="clearances", repo="india-ec-subsector-analysis",
         title="india-ec-subsector-analysis: which states lead each kind of Environmental Clearance",
         what="A state-by-sub-sector pivot of the PARIVESH 2.0 Environmental Clearance register, with grant rates.",
         when="You want to know which states dominate clearances for an activity, and where approvals stall.",
         paras=[
             "The repo turns the PARIVESH 2.0 Environmental Clearance register into a matrix of states against EIA-schedule activity codes, such as 5(f) Synthetic organic chemicals. Status is bucketed into granted, ToR-granted, in-process, dead and delisted, and the grant rate leaves out delisted proposals. The data is committed as a 2,055-row CSV and two JSON files, so analysis needs only Python&rsquo;s standard library.",
             "The committed snapshot was built on 22 July 2026 and holds 113,970 proposals in 22 sub-sectors. A refresh script downloads about 126 MB from the PARIVESH API. The repo also compares EC filings with IEM filings and covers forest, wildlife and CRZ clearances; the guide did not run those parts.",
         ],
         cmd_intro="Check the committed CSV and the snapshot date.",
         cmd='''python3 -I -c "import csv,json;r=list(csv.DictReader(open('data/ec_state_subsector.csv')));print(len(r),sum(int(x['count']) for x in r));print(json.load(open('data/ec_subsector_analysis.json'))['built'])"''',
         out="<code>2055 113970</code>, followed by the snapshot date 2026-07-22.",
         limit="It is a snapshot, not a time series, and it does not tell you the live status of any project. 8,037 proposals have no parseable activity code and are left out of the sub-sector view. Small states show extreme grant rates on few proposals. Not legal advice."),
    dict(anchor="iem", repo="iem-tracker",
         title="iem-tracker: did announced factories reach production?",
         what="A pipeline that links DPIIT&rsquo;s IEM Part A filings (intention) to Part B (production started) and checks registry status for the rest.",
         when="You want to test how many announced factories were built, and which filers no longer exist.",
         paras=[
             "An Industrial Entrepreneur Memorandum (IEM) is the filing an Indian manufacturer makes to DPIIT. Part A says the company intends to build; Part B says production has started. iem-tracker parses both sets of monthly PDF lists, links them by memorandum number and date and then by name, and looks up the companies with no Part B in registries: the data.gov.in company master, the GLEIF LEI register and public company sites. One command, <code>iem</code>, runs each stage: parse, build, web, report.",
             "No DPIIT data ships with the repo. You download the &lsquo;List of IEM Filed&rsquo; and &lsquo;List of IEM Implemented&rsquo; PDFs into <code>PartA/</code> and <code>PartB/</code> first. The repo&rsquo;s own documented status of 10 October 2026 records 19,913 Part B records; the guide&rsquo;s run on 2 November 2026 only installed the tool and checked it.",
         ],
         cmd_intro="See what exists locally.",
         cmd="./iem status",
         out="On a fresh clone it reports 0 / 0 PDFs, the parquet and DuckDB files missing, and <code>OGD_KEY</code> not set. After parsing it shows row counts per stage.",
         limit="A single identification is a lead, not a fact: the repo&rsquo;s GLEIF cross-check found that about 6% of tier 1 and 16% of tier 2 matches pointed at a different company with the same name. Status from free company sites is not an official certificate, and the data.gov.in master is labelled &lsquo;data up to 3 November 2023&rsquo;."),
    dict(anchor="incentives", repo="digital-twin-for-ipa",
         title="digital-twin-for-ipa: India&rsquo;s investment incentives as data",
         what="JSON layers of central and state incentive instruments and their stacking rules, plus a SQLite database of companies.",
         when="You need to know which incentives apply to a project and whether they can be combined.",
         paras=[
             "digital-twin-for-ipa is a machine-readable model of India&rsquo;s investment-promotion apparatus. Numbered JSON layers hold source networks, portal directories and incentive catalogues, normalised into one flat index of instruments; a separate layer records which schemes stack, exclude or feed each other. A SQLite database links companies to filings, clearance activity, credit ratings and news. Every claim carries a note on how it was verified, and blocked or JavaScript-only portals are recorded as data rather than skipped.",
             "In the guide&rsquo;s demo of 18 October 2026, the flat index held 312 instruments (195 central, 117 state) and the database 1,849 companies. The README said 1,785 companies; the database is the newer figure. Reading the data needs only Python 3 and, optionally, the <code>sqlite3</code> command line.",
         ],
         cmd_intro="Count companies in the database, read-only.",
         cmd='''sqlite3 -readonly -header -column data/companies.db "select count(*) companies, sum(is_india_entity) india_filers, count(distinct country) countries from companies;"''',
         out="1,849 companies, 1,483 Indian filers and 48 countries, as of the 18 October 2026 demo.",
         limit="There is no automated test suite. Whether a scheme is open is a snapshot, and many instruments are not verified on site. Most credit-rating rows (73 of 82) fall in a &lsquo;grade_check_in_python&rsquo; bucket, so stressed-asset flags need manual review. Public data, not legal, tax or investment advice."),
    dict(anchor="investors", repo="focus-sector-investor-map",
         title="focus-sector-investor-map: which foreign investors use which Indian scheme",
         what="A map of India&rsquo;s twelve focus sectors to listed companies worldwide, plus a hand-verified file pairing foreign investors with Indian initiatives.",
         when="You want to see which foreign companies sit behind which government initiative, or which countries to court for a sector.",
         paras=[
             "The repository joins India&rsquo;s twelve trade-policy focus sectors to the global listed-company universe. It has a coverage layer that classifies every company into a sector, a screened set of liquid names, a shortlist checked for profitability, and a file that pairs foreign investors with the Indian initiative that is their route in. Verified pairs cite a Press Information Bureau release or a Cabinet approval, and the file keeps its negative findings, such as a stalled steel joint venture.",
             "Read on 19 October 2026, the catalogue held 19,795 companies in 107 countries. The pairing file was retrieved on 20 July 2026 and has 12 verified and 7 prospective pairs. The sample commands use only Python&rsquo;s standard library.",
         ],
         cmd_intro="List the investor-to-scheme pairings.",
         cmd='''python3 -I - <<'E'
import json
d=json.load(open('data/foreign_investor_initiative_pairs.json'))
for k in ('verified_pairs','prospective_pairs'):
    for x in d[k]: print(k[:4],x['company'],'|',x['sector'],'|',x['status'])
E''',
         out="19 lines: 12 verified and 7 prospective pairings, each with its status.",
         limit="The build scripts read files from the author&rsquo;s own market-data stack that are not in the repo, so the screen cannot be rebuilt from a fresh clone. Profitability comes from trailing, unaudited free data, &lsquo;prospective&rsquo; pairings are not announced deals, and policy status changes quickly. Not investment advice."),
    dict(anchor="quality", repo="india-quality-regulation",
         title="india-quality-regulation: who certifies what",
         what="A sourced Markdown catalogue of BIS and other regulators, accreditation boards and marks, with link-checking scripts.",
         when="You need to know which body certifies a product, under which law, and whether the mark is mandatory.",
         paras=[
             "india-quality-regulation is a documentation repository, not an application. <code>docs/</code> has one page per body, grouped into ten categories, from BIS Hallmarking and FSSAI to CDSCO, the BEE Star Label, Legal Metrology and NABL. Each page names the authority, its legal basis, whether the mark is mandatory or voluntary, and the mirrored primary source. <code>COMPENDIUM.md</code> puts everything in one file for offline reading or for pasting into a chat assistant.",
             "Three standard-library scripts keep the catalogue consistent. In the guide&rsquo;s run of 19 October 2026, on the repo as committed on 24 September 2026, there were 36 entries (22 with statutory text mirrored, 14 with an official scheme page).",
         ],
         cmd_intro="Check that every source reference in the pages resolves to a mirrored file.",
         cmd="python3 scripts/check_source_refs.py",
         out="In the guide&rsquo;s run: 144 source references checked, all resolve.",
         limit="The repo is a snapshot, and Quality Control Orders and scheme rules change often. The checker proves that links point to mirrored files, not that the mirrored text is the latest amendment. Some entries rely on secondary mirrors because some .gov.in and .nic.in hosts were unreachable. Indian Standards texts are paid and are listed, not included. Not legal advice."),
    dict(anchor="rbi", repo="reg-intel",
         title="reg-intel: obligations from RBI Master Directions, with checkable quotes",
         what="An LLM pipeline that lists obligations in RBI Master Directions and keeps only those whose citation appears word for word in the source.",
         when="You want a list of what an RBI direction requires, with every item tied to a quote you can check.",
         paras=[
             "reg-intel fetches RBI Master Directions with a polite delay, stores the text, asks an LLM to pick out obligations (who must or must not do what, by when), and accepts an item only if its citation is found verbatim in the stored text. Every step is written to a hash-chained ledger, so a record edited afterwards shows up. The default mode has the model select numbered source lines; a generate mode, where the model writes the quote, is the stricter test of grounding.",
             "Extraction needs an OpenAI-compatible endpoint, such as a Groq key or a local LM Studio server. The tests do not. In the guide&rsquo;s run of 2 November 2026, all 8 tests passed offline in under a second, including one where an invented citation is rejected. <code>pip install -e .</code> failed in that run, so install the dependencies directly and run from the cloned folder.",
         ],
         cmd_intro="Run the offline tests (after <code>pip install requests beautifulsoup4 openai pytest</code> in a virtual environment).",
         cmd=".venv/bin/python -m pytest -v",
         out="8 passed: citation gate, hallucinated-citation flagging, ledger tamper detection, listing parser, bad-JSON handling, line-indexed citation, precision override and lead-in detection.",
         limit="Only two documents are labelled, and the labels are drafts made by Claude, not reviewed by a person, so the repo&rsquo;s recall and precision figures are indicative only. In the default line-indexed mode the citation is the source line itself, so the grounding check no longer measures precision on its own. RBI&rsquo;s PDF host blocks scripted downloads. Not legal advice."),
]

assert len(TOOLS) == 8

# ---------------------------------------------------------------- page parts
stats = '''<div class="gb-stats">
<div class="gb-stat"><b>2,637</b><span>gazette notifications in the rebuilt citation index, with 2,150 cross-references (19 Oct 2026 build)</span></div>
<div class="gb-stat"><b>59,381</b><span>Parliament questions in the ledger since June 2024 (queried 19 Oct 2026)</span></div>
<div class="gb-stat"><b>113,970</b><span>Environmental Clearance proposals in the PARIVESH snapshot built 22 Jul 2026</span></div>
<div class="gb-stat"><b>36</b><span>quality regulators, boards and marks catalogued, 144 source links all resolving (19 Oct 2026)</span></div>
</div>'''

intro = '''<p>Much of what India&rsquo;s government decides is published, but in pieces: a gazette notification here, a Parliament answer there, a clearance on PARIVESH, a monthly PDF of factory filings from DPIIT, a Master Direction on the RBI&rsquo;s site. The eight open-source repositories below each take one of those record sets and turn it into something you can query on your own computer: a SQLite or DuckDB file, a CSV, a set of JSON layers or a Markdown catalogue.</p>

<p>They are for policy researchers, journalists, compliance teams, investment-promotion staff and students who need to trace a rule, count questions, or check whether announced projects were built. Most run on Python with the standard library or one extra package, and the steps shown need no API key. None of them gives legal or investment advice, and most are snapshots, so each section gives the date of the run its figures come from.</p>'''

choose = table(["Tool", "What it does", "Use it when"],
               [[f'<a href="#{t["anchor"]}">{t["repo"]}</a>', t["what"], t["when"]] for t in TOOLS])

sections = "\n".join(tool(t["anchor"], t["title"], t["repo"], t["paras"], t["cmd_intro"], t["cmd"], t["out"], t["limit"]) for t in TOOLS)

worked = f'''<h2 class="gb-h2">Worked example: tracing one customs notification (gazette-translated-indexed)</h2>
<p>This is the run recorded in the Gazette Trail guide on 19 October 2026. It used only the committed SQL seed files: nothing was downloaded from egazette.gov.in, and no PDFs or OCR were used.</p>
<p><strong>1. Get the code and build the database.</strong></p>
{code("""git clone https://github.com/herrrickshaw/gazette-translated-indexed.git
cd gazette-translated-indexed
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
sqlite3 gazette.db < db/schema.sql
for f in db/seed_*.sql; do sqlite3 gazette.db < "$f"; done
sqlite3 gazette.db "PRAGMA foreign_key_check;"
""")}
<p>The foreign-key check printed nothing. Running <code>pytest tests/</code> then gave 197 passed in 0.30 seconds.</p>
<p><strong>2. See what kinds of links the index holds.</strong></p>
{code("""sqlite3 -header -column gazette.db "select relation_type, count(*) n from cross_reference group by 1 order by n desc;"
relation_type   n
-------------  ----
amends         1655
cites           213
supersedes      155
corrigendum      90
rescinds         32
repeals           5
""")}
<p>Amendments dominate; supersessions and corrigenda are the minority.</p>
<p><strong>3. List everything that points at Customs notification 45/2025.</strong></p>
{code("""sqlite3 -header -column gazette.db "select g.gazette_id, g.publish_date, g.gsr_or_so, x.relation_type from cross_reference x join gazette_notification g on g.gazette_id=x.source_gazette_id where x.target_gazette_id='cus-45-2025';"
    gazette_id      publish_date    gsr_or_so    relation_type
------------------  ------------  -------------  -------------
cus-2-2026          2026-02-01    G.S.R. 83(E)            amends
cus-corr-45-2025-a  2025-10-31    G.S.R. 807(E)           corrigendum
cus-48-2025         2025-11-14    G.S.R. 847(E)           amends
cus-6-2026          2026-03-12    G.S.R. 181(E)           amends
cus-14-2026         2026-04-30    G.S.R. 330(E)           amends
cus-15-2026         2026-05-12    G.S.R. 358(E)           amends
cus-corr-45-2025-b  2026-06-12    G.S.R. 476(E)           corrigendum
cus-25-2026         2026-07-08    G.S.R. 600(E)           amends
cus-44-2025         2025-10-24    G.S.R. 782(E)           cites
""")}
<p>Nine later or related notifications link to one 2025 customs notification: six amendments, two corrigenda and one citation. That is the amendment chain a single PDF does not show. For one notification&rsquo;s links in both directions from Python, the repo&rsquo;s <code>db/crud.py</code> has a <code>get_lineage</code> function, which returns a dictionary with &lsquo;points_at&rsquo; and &lsquo;pointed_at_by&rsquo;. The index is current only to the seed files; check the freshness of anything you rely on against the official notification.</p>'''

limits = '''<h2 class="gb-h2">What these tools do not do</h2>
<ul>
<li><strong>They are not legal, tax or investment advice.</strong> Every guide says so. Read the official notification, direction or regulator&rsquo;s page before acting on anything they show.</li>
<li><strong>They are snapshots, not live feeds.</strong> The clearance data was built on 22 July 2026, the quality catalogue reflects the repo as of 24 September 2026, the investor pairings were retrieved on 20 July 2026, and the company master used by iem-tracker is labelled &lsquo;data up to 3 November 2023&rsquo;.</li>
<li><strong>Some cannot be rebuilt from a fresh clone.</strong> focus-sector-investor-map reads local files from the author&rsquo;s market-data stack; lok-rajya-sabha-qa needs a PIB index and a minister directory that are not in the repo; iem-tracker ships no data at all.</li>
<li><strong>Matches and flags are leads.</strong> Same-name companies defeat registry matching in a measurable share of cases, and stressed-asset flags in digital-twin-for-ipa need manual review.</li>
<li><strong>Counts are not judgements.</strong> A party that asks more Parliament questions has more members; a high grant rate in a small state may rest on a handful of proposals.</li>
<li><strong>LLM output still needs a reader.</strong> reg-intel proves that a quote exists in the source, not that the obligation was read correctly, and its accuracy figures rest on two unreviewed documents.</li>
<li><strong>READMEs lag the data.</strong> In two repos the README counts were lower than the data the guides actually built; this page uses the built figures.</li>
</ul>'''

body = f"""{stats}

{intro}

<h2 class="gb-h2">Which tool for which job</h2>
{choose}

<h2 class="gb-h2">The eight tools</h2>
<p>Each section says what the tool does, where its data comes from, the one command to start with, and the main limitation its guide records. All need git to clone; the extra software is noted where it matters.</p>
{sections}
{worked}

{limits}
"""

src_links = "; ".join(repo_link(t["repo"]) for t in TOOLS)
sources = ("Code: " + src_links + ". "
           "This page replaces the separate how-to guides for these eight repositories, written between 18 October and 2 November 2026. "
           "Every command, output and figure here is taken from those guides&rsquo; own demo runs, on the dates given in the text; "
           "where a README and a fresh build disagreed, the build (the newer figure) is used. The underlying data comes from egazette.gov.in, "
           "sansad.in and rsdoc.nic.in, PARIVESH 2.0, DPIIT&rsquo;s SIA statistics pages, data.gov.in, GLEIF, PIB releases, regulators&rsquo; own sites and the RBI. "
           "None of this is legal, tax or investment advice.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/09/right-of-user-what-indias-pipeline.html", "Right of User: What India&#x27;s Pipeline Gazette Notifications Actually Show, State by State"),
    ("https://masaladeutsch.blogspot.com/2026/09/the-two-biggest-parties-in-parliament.html", "The Two Biggest Parties in Parliament Ask About Everything. Everyone Else Doesn&#x27;t."),
    ("https://masaladeutsch.blogspot.com/2026/10/indias-factory-intentions-20012024-how_0101046393.html", "India&#x27;s Factory Intentions, 2001–2024: How Many IEM Filings Became Plants"),
    ("https://masaladeutsch.blogspot.com/2026/09/india-doesnt-have-one-quality-regulator.html", "India Doesn&#x27;t Have One Quality Regulator. It Has 37 — and One Just Repealed Itself Before It Started."),
]

TITLE = ("Eight Open-Source Tools for Tracking India&rsquo;s Gazette, Parliament, Clearances, Incentives and Regulators, "
         "and What Each One Answers")
STANDFIRST = ("Eight free repositories turn scattered Indian government records into files you can query: gazette notifications, Parliament questions, "
              "environmental clearances, factory filings, incentive schemes, quality regulators and RBI directions. "
              "This guide sets out what each one answers, the command to start with, and where each one stops.")

build("Open-Source Tools &middot; 12 November 2026", TITLE, STANDFIRST, body, sources, related, OUT)
print("built", OUT, "tools", len(TOOLS))
