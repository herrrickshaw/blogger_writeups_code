"""Hub post: developer and AI tooling.
Build (from repo root): PYTHONPATH=tools/postbuild python3 out/research/phase2-hubs/dev-ai/build.py

Replaces thirteen separate "How to use <repo>" guides (eleven live, two drafts; see hubs.json key "dev-ai").
Every fact, command and figure below is taken from those guides; dates are the guides' own run dates."""
import html
import sys
sys.path.insert(0, 'tools/postbuild')
from buildpost import build

OUT = 'out/post-hub-dev-ai.html'
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


def tool(t):
    return (f'<h3 id="{t["anchor"]}" style="{H3_STYLE}">{t["title"]}</h3>\n<p>{t["para"]}</p>\n'
            f'<p><strong>Start here.</strong> {t["cmd_intro"]}</p>\n{code(t["cmd"])}\n'
            f'<p>{t["out"]}</p>\n'
            f'<p><strong>Code:</strong> {repo_link(t["repo"])}. <strong>Main limitation:</strong> {t["limit"]}</p>\n')


GROUPS = [
    ("Working with LLMs and AI assistants", [
        dict(anchor="router", repo="claude-lmstudio-router",
             title="claude-lmstudio-router: fall back to a local model when Claude is unavailable",
             what="Sends a prompt to Claude first and falls back to a model in LM Studio on your machine; a proxy lets Claude Code itself run on a local model.",
             when="Rate limits stop a long job, or some text must stay on your own computer.",
             para="There are two tools. <code>router.py</code> tries the Claude API, retries twice on a 429 or 529 error, then sends the same prompt to a model served by LM Studio, and logs each call to <code>router_log.jsonl</code>. <code>claude_code_proxy.py</code> translates between the Anthropic API that Claude Code speaks and the OpenAI API that LM Studio speaks, so the whole agent can run offline on a local tool-calling model. You load the model and start LM Studio&rsquo;s server yourself. The guide&rsquo;s demo of 18 October 2026 used a canned stand-in server, not LM Studio.",
             cmd_intro="Run one prompt (needs <code>pip install anthropic</code>; set <code>ANTHROPIC_API_KEY</code> for the Claude path).",
             cmd='python -I router.py --prompt "Summarize: tariffs"',
             out="With no key and no LM Studio it fails honestly: it reports both failures, prints &lsquo;FAILED: Both Claude and local LM Studio failed&rsquo; and logs engine=none. When the local server answers, the output says &lsquo;Answered by: LOCAL&rsquo; and the log shows engine=local.",
             limit="local models are weaker and slower, so treat fallback output as a draft. The proxy needs a tool-calling model and drops image blocks. Text goes to Anthropic whenever Claude answers. No unit tests ship with the repo."),
        dict(anchor="citations", repo="llm-extract-citation-fix",
             title="llm-extract-citation-fix: LLM extraction that checks its own citations",
             what="One Python file that extracts JSON fields from a document with an LLM and checks that each field&rsquo;s quoted evidence is in the text.",
             when="You pull figures from filings or statements with an LLM and want a guard against invented values.",
             para="<code>llm_extract.py</code> exposes <code>extract_structured(text, schema)</code>: it asks a Groq model (Gemini as fallback) for fields plus citations, checks each citation against the source, and adds a <code>_grounding</code> map. The fix in this repo makes the check accept list fields, where each item carries its own quote; the old check marked such correct extractions as ungrounded. The verifier runs offline with no key. Live extraction needs your own Groq or Gemini key and was not run in the guide.",
             cmd_intro="Check a citation against source text, with no key.",
             cmd='''python3 -c "from llm_extract import _verify_citation as v; src='TCS  Qty 5   Avg 3200.50'; print(v(['TCS  Qty 5   Avg 3200.50'], src), v(['WIPRO Qty 7'], src))"''',
             out="<code>True False</code>: a list of per-item quotes passes only if every quote is in the text (run of 3 November 2026).",
             limit="a grounded field proves that the quote exists, not that a derived value such as a midpoint is right. The guide notes that the default model names in the file are retired, so set <code>GROQ_MODEL</code> and <code>GEMINI_MODEL</code> yourself. There are no tests, requirements file or packaging."),
        dict(anchor="tokens", repo="prompt-efficiency-tracker-public",
             title="prompt-efficiency-tracker-public: log Claude Code token cost, and notice when logging stops",
             what="A Claude Code Stop hook that logs tokens, estimated cost, project and a success or tool_error flag per turn to SQLite, plus a heartbeat check.",
             when="You use Claude Code heavily and want your own record of where tokens go.",
             para="The hook writes one row per turn into a local SQLite table, split by project and by main agent versus subagent, and marks a turn tool_error if a tool result errored since the last logged message. The heartbeat script reports when the hook has dropped out of <code>settings.json</code> or the database has gone stale; a macOS launchd plist runs it daily. In the guide&rsquo;s run of 3 November 2026, in a throwaway home directory with a synthetic transcript, running the hook twice left exactly two rows.",
             cmd_intro="Run the heartbeat (try it first with a throwaway <code>HOME</code>).",
             cmd='python3 scripts/heartbeat_check.py; tail -1 "$HOME/.ruflo/logs/heartbeat.log"',
             out="It always exits 0. On an empty home the log line lists two problems: settings.json missing, and token_usage.db does not exist. Once the hook was wired in the demo home, it reported ok.",
             limit="the hook does not create its <code>token_usage</code> table and the schema is not in the repo, so you must create it. Costs are estimates from a hard-coded price table, not billing data. Scheduling and notifications are macOS-only."),
        dict(anchor="maritime", repo="ship2shore_rag",
             title="ship2shore_rag: offline, cited answers from open maritime reports",
             what="Search over open maritime literature and accident reports that returns cited passages, on a shore server or offline on a ship.",
             when="You want to look up past maritime incidents or definitions, including on a vessel with no internet.",
             para="It collects arXiv papers, Wikipedia, UK MAIB and US NTSB accident reports, and your own PDF or Word files, splits them into passages, and combines meaning-based and keyword search with a reranking step. Ashore it uses Postgres with pgvector; on a vessel it uses one SQLite file. Writing an answer with Claude is optional; without a key it lists ranked passages with their sources. The repo ships a snapshot of 125 documents, and the install (sentence-transformers and two small models) needs about 1 GB of disk.",
             cmd_intro="With <code>STORAGE_BACKEND=sqlite</code> and <code>SQLITE_PATH=snapshots/ship2shore.sqlite3</code> set in <code>.env</code>, ask a question without an API key.",
             cmd='python3 cli.py ask "What is a bill of lading and what does it do?" --no-generate --top-k 3',
             out="Three passages. In the guide&rsquo;s run of 18 October 2026, two came from the Wikipedia article on the bill of lading and one from the article on charterparties. On the repo&rsquo;s 17 test questions, recall@5 was 0.76 without reranking and 0.82 with it.",
             limit="the corpus is small: questions about engine-room fires returned only loosely related reports, and 17 test queries make the scores indicative, not a benchmark. It does not replace statutory logs, and its web API accepts requests from any origin, so keep it on localhost."),
        dict(anchor="memory", repo="memory-map-optimizer",
             title="memory-map-optimizer: cluster a knowledge graph, search and dedupe notes",
             what="A single-file CLI that finds communities in a graph file, searches markdown notes with keywords plus embeddings, and flags near-duplicates.",
             when="You keep a large markdown notes or AI-assistant memory folder and want structure and duplicates found for you.",
             para="It has five commands. <code>cluster</code> runs Leiden community detection on a graph JSON; <code>embed</code> indexes markdown files with a sentence-embedding model; <code>search</code> combines BM25 keyword and embedding ranks, with an optional reranker; <code>dedup</code> groups near-duplicate files by cosine similarity; <code>report</code> writes an HTML overview. Defaults point at the author&rsquo;s own Claude Code memory paths, so pass your own.",
             cmd_intro="Cluster a graph file.",
             cmd="python memory_map_optimizer.py cluster --graph my_graph.json --write-back --out clusters.json",
             out="A line such as &lsquo;60 nodes, 213 edges -&gt; 3 communities (modularity 0.6082)&rsquo; and a size per cluster. The worked example below shows the full run.",
             limit="only <code>cluster</code> and the bundled checks were run in the guide. The other commands need a model download of about 1.5 GB, and the README says <code>embed</code> was never confirmed end to end. <code>--write-back</code> edits your graph JSON in place, so work on a copy."),
    ]),
    ("Data pipelines and testing", [
        dict(anchor="datamining", repo="data-source-mining",
             title="data-source-mining: World Bank indicators and mandi prices in one DuckDB file",
             what="A short script that pulls World Bank indicators and Agmarknet mandi prices into one local DuckDB file.",
             when="You want a quick cross-country macro panel, or a sample of daily mandi prices, queryable with SQL.",
             para="<code>mine_underused_sources.py</code> pulls 12 World Bank indicators (GDP, growth, inflation, agriculture share, trade, energy mix, FDI and others) for India and six comparison economies, and the data.gov.in Agmarknet resource using the public sample key that data.gov.in documents. It needs Python and the <code>duckdb</code> package, and no account. The committed database was pulled on 21 July 2026 and has 4,532 World Bank rows and 4 mandi rows.",
             cmd_intro="Pull the World Bank leg only.",
             cmd=".venv/bin/python mine_underused_sources.py --wb-only",
             out="One line per country, then &lsquo;worldbank_indicators: N rows&rsquo; and a table list. It makes about 84 API calls and takes a few minutes.",
             limit="run in the cloned folder, it overwrites the World Bank table in the committed database, so copy the folder first. The mandi sample key returns a small, rate-limited sample. It mines a fixed pair of sources and is not a general discovery tool."),
        dict(anchor="warehouse", repo="ltm-warehouse-tests",
             title="ltm-warehouse-tests: test a price-history backfill on a throwaway Postgres",
             what="A harness that builds a throwaway Postgres database, seeds awkward synthetic tickers, runs backfill scripts against it and drops it.",
             when="You maintain scripts that write into a price warehouse and want to re-check a change without touching real data.",
             para="<code>run_tests.sh</code> creates a test database, applies a schema that mirrors the real tables, and seeds synthetic symbols that encode past bugs: a ticker already carrying a suffix, a symbol under two countries, an NSE series switching mid-history. It runs three test files and drops the database even if a test fails. The tests check deduplication, that low-fidelity estimates go to a separate table, that a dry run never persists, and that the NSE tier fires only for India. No API keys are needed.",
             cmd_intro="Run the whole suite against a local Postgres (install <code>requirements.txt</code> with <code>&quot;sqlalchemy&lt;2.1&quot;</code> first).",
             cmd="./run_tests.sh",
             out="It ends with &lsquo;All tests passed.&rsquo; and drops the database. In the guide&rsquo;s run of 19 October 2026 on a throwaway Postgres 17, all three test files passed.",
             limit="with <code>requirements.txt</code> as written, a fresh install picked SQLAlchemy 2.1.5 and seeding failed, hence the pin. The script ignores the port in <code>PG_ADMIN_URL</code>, so set <code>PGPORT</code> and <code>PGHOST</code> for a non-default port. Live Yahoo, NSE and SerpApi calls are not exercised."),
        dict(anchor="lfs", repo="repo-data-dedup",
             title="repo-data-dedup: find duplicate Git LFS storage across your repos",
             what="An audit that lists every Git LFS pointer in every repo of a GitHub account, without downloading any LFS object, and totals the duplicates.",
             when="Your LFS quota is used up or growing and you need to know which repos hold the same bytes before deleting anything.",
             para="<code>scripts/audit_lfs.py</code> makes a filtered clone of each repo that reads only the small pointer files, writes <code>lfs_inventory.csv</code> (every pointer, its size and whether HEAD still uses it) and <code>repo_summary.csv</code>, and prints total stored, total unique and cross-repo duplicate waste. It needs Python 3, git and a logged-in GitHub CLI. On a synthetic three-repo account in the guide&rsquo;s run of 19 October 2026, it counted 1.83 GB stored against 0.71 GB unique.",
             cmd_intro="Audit your own account, read-only. Replace <code>&lt;owner&gt;</code> with your GitHub user or organisation.",
             cmd='''mkdir -p ~/lfs_audit && cd ~/lfs_audit
python3 /path/to/repo-data-dedup/scripts/audit_lfs.py <owner> ~/lfs_audit/clones''',
             out="One progress line per repo, then the three totals; the two CSVs appear in the current folder.",
             limit="it counts pointers; it does not prove that a copy is safe to delete. The repo&rsquo;s <code>delete_archive_twins.sh --run</code> deletes real repositories from a list hard-coded for the author&rsquo;s account, so read it and use only its default dry run. LFS storage is freed only by deleting repositories."),
    ]),
    ("Publishing, design and process", [
        dict(anchor="blogcheck", repo="blog-consistency-check",
             title="blog-consistency-check: is this blog post broken?",
             what="A script that fetches a published post from this blog and tests it against rules drawn from real defects, exiting non-zero on a blocker.",
             when="You hand-write or bulk-edit HTML posts with their own CSS and JavaScript and want a check after each edit, or a CI gate.",
             para="It lists posts through the public Blogger feed, downloads each with curl, and applies 10 static rules: 4 blockers (such as JavaScript that does not parse, or a dark palette with no light-mode lock), 2 major and 4 minor. <code>CHECKLIST.md</code> explains each rule. An optional Playwright pass adds contrast and overflow checks. It needs Python 3, curl and node.",
             cmd_intro="Audit one public post.",
             cmd="python3 audit.py --url <post URL>",
             out="It writes <code>out/report.md</code> and <code>out/report.json</code> and prints a count of BLOCKER failures. In the guide&rsquo;s run of 19 October 2026, one live post showed 1 BLOCKER and 1 MINOR, both about its CSS.",
             limit="it is hard-coded to masaladeutsch.blogspot.com, and several rules are specific to this blog. The static pass reads the HTML source, so a CSS finding is a signal to inspect, not proof of a visible fault. The fix scripts edit content and were not run in the guide."),
        dict(anchor="design", repo="research-design-system",
             title="research-design-system: one set of design tokens, four themes",
             what="A small CSS kit with one token contract, four themes and one component set for reports, bulletins and dashboards.",
             when="You publish HTML reports or dashboards and want them to look related without copying styles.",
             para="Components use only semantic tokens such as <code>--c-text</code> and <code>--c-accent</code>, and each theme rebinds about a dozen of them. The same page switches between the bulletin, report, reportage and slate themes by changing one stylesheet and one body class; the guide rendered all four on 19 October 2026. Templates for a report, a bulletin and a dashboard, a component gallery and A4 print rules for WeasyPrint are included. There is no JavaScript or build step.",
             cmd_intro="Start from a template and open it.",
             cmd='''cp templates/report.html my-report.html   # then fix the ../ paths or keep the file inside the repo
open my-report.html''',
             out="A report page with a masthead, stat tiles, a table and side and warning boxes. Load the stylesheets in this order: tokens, theme, components, print.",
             limit="it is a starter kit, not a brand system, and only CSS. Dark mode is opt-in through a data-theme attribute, not the operating-system setting. Numbers in the shipped templates are placeholders, not data. The WeasyPrint path was not tested in the guide."),
        dict(anchor="playbook", repo="delivery-playbook",
             title="delivery-playbook: a field guide for choosing and fixing a software process",
             what="A single-file HTML guide to SDLC models, Agile, DevOps, DDD and TOGAF, with a fit-finder and named failure modes.",
             when="Your team is choosing or fixing a delivery process and needs shared words for it.",
             para="The page compares Waterfall, V-Model, Spiral, Scrum, Kanban, XP and DevOps. It offers a two-question fit-finder (how often requirements really change, and how costly a mistake is once shipped) and six named failure modes, such as Zombie Scrum and Watermelon status, each with a fix. It also covers computer-science theory applied to product decisions, Domain-Driven Design, TOGAF and a testing playbook. There is nothing to install.",
             cmd_intro="Open the page.",
             cmd="open index.html   # macOS; on Linux use xdg-open, on Windows double-click the file",
             out="The fit-finder places a project in one of four quadrants. High stakes with unclear scope points to Spiral; low stakes with unclear scope to Scrum, XP or Lean Startup.",
             limit="it is a field guide with the author&rsquo;s opinions, not an official Scrum, SAFe or TOGAF text, so check the primary sources it links. The live copy is not auto-synced with the repo."),
    ]),
    ("Machine housekeeping", [
        dict(anchor="cleaner", repo="cache_memory_cleaner",
             title="cache_memory_cleaner: free Mac disk space without losing data",
             what="A macOS shell script that sorts any folder into five safety tiers before you delete it, and previews cache cleanup.",
             when="Your Mac disk is nearly full and you want a written reason before deleting anything.",
             para="Its key command, <code>classify</code>, reads git status, whether a running process has the path open, whether it sits in a cloud-sync folder, whether the name looks like a personal scan, and how long since anything changed, then prints a tier and the reason. It never deletes. Other commands act on the tiers: <code>clean-caches</code>, <code>compress-local</code> (needs afsctool) and <code>archive-evict</code>, which uploads to your cloud with rclone, checks the bytes, and only then deletes. Put <code>DRY_RUN=1</code> in front of any command to preview it.",
             cmd_intro="Ask which tier a folder belongs to (read-only).",
             cmd="./cache_memory_cleaner.sh classify path/to/venv",
             out="In the guide&rsquo;s demo of 18 October 2026, a virtual environment came back as Tier 1 (permanent local, compress in place) and a <code>__pycache__</code> folder as Tier 4 (delete immediately).",
             limit="<code>classify</code> is a heuristic, so read its reason before acting. Never point the archive remote at a path that another rclone sync job mirrors: in the author&rsquo;s case a sync wiped four verified archives. <code>archive-evict</code> deletes originals and was not run in the demo."),
        dict(anchor="transmission", repo="transmission-client",
             title="transmission-client: control a Transmission daemon from a CLI, a web page or Python",
             what="A Python client for the Transmission daemon&rsquo;s RPC API, with a command-line tool, a local web page and a library.",
             when="You run transmission-daemon headless on a server or NAS and want to script it.",
             para="You can list, inspect, add, start, stop and remove torrents from a terminal, from a web page on 127.0.0.1:5000, or from your own Python code. The client handles Transmission&rsquo;s session-id handshake for you: it catches the 409 reply, stores the id and retries. It needs Python 3.9 or newer and a running daemon. Use it only for content you have the right to download and share.",
             cmd_intro="List torrents (after <code>pip install -e .</code> and setting <code>TRANSMISSION_HOST</code> and <code>TRANSMISSION_PORT</code>).",
             cmd="transmission-cli list",
             out="A table with ID, STATUS, DONE, SIZE, DOWN, UP and NAME columns. The guide&rsquo;s run of 19 October 2026 used a mock daemon, not a real one.",
             limit="it was shown against a mock only, so behaviour with a real daemon is untested. The repo has no tests, and the session id is not cached between runs. The README&rsquo;s development setting <code>--allowed &quot;&quot;</code> opens the RPC port to every host; do not use it on an exposed machine."),
    ]),
]

TOOLS = [t for _, ts in GROUPS for t in ts]
assert len(TOOLS) == 13

stats = '''<div class="gb-stats">
<div class="gb-stat"><b>13</b><span>small tools, most of them one script or one short package</span></div>
<div class="gb-stat"><b>0.76 &rarr; 0.82</b><span>recall@5 without and with reranking on 17 test questions (ship2shore_rag, 18 Oct 2026)</span></div>
<div class="gb-stat"><b>1.83 GB vs 0.71 GB</b><span>LFS storage counted against unique content in a synthetic three-repo audit (19 Oct 2026)</span></div>
<div class="gb-stat"><b>5 tiers</b><span>from &ldquo;never touch&rdquo; to &ldquo;delete now&rdquo; in the Mac disk cleaner</span></div>
</div>'''

intro = '''<p>These thirteen repositories are small and single-purpose. Most were written to fix a problem their author actually hit: a Claude rate limit in the middle of a long job, an LLM check that marked a correct extraction as ungrounded, a GitHub LFS quota used up by backup copies, a Mac disk at 99%, and defects that reached this blog&rsquo;s own published posts.</p>

<p>They are for developers, data engineers and heavy users of AI assistants who want a working example to read or reuse. Several are also usable by non-programmers who hand the repository to an AI assistant and ask in plain language. Many were demonstrated on synthetic data, mock servers or dry runs, so each section says what was actually run, and when.</p>'''

choose = table(["Tool", "What it does", "Use it when"],
               [[f'<a href="#{t["anchor"]}">{t["repo"]}</a>', t["what"], t["when"]] for t in TOOLS])

sections = "\n".join(f'<h2 class="gb-h2">{g}</h2>\n' + "\n".join(tool(t) for t in ts) for g, ts in GROUPS)

worked = f'''<h2 class="gb-h2">Worked example: clustering a graph (memory-map-optimizer)</h2>
<p>This is the run recorded in the memory-map-optimizer guide on 19 October 2026, from a fresh clone in a throwaway virtual environment. The guide installed only python-igraph, leidenalg, rank-bm25 and numpy, which is enough for the checks and the <code>cluster</code> command; the full <code>requirements.txt</code> also pulls in sentence-transformers.</p>
<p><strong>1. Get the code and an environment.</strong></p>
{code("""git clone https://github.com/herrrickshaw/memory-map-optimizer.git
cd memory-map-optimizer
python3 -m venv .venv
source .venv/bin/activate
""")}
<p><strong>2. Run the bundled checks.</strong></p>
{code("""python test_memory_map_optimizer.py
test_leiden_finds_real_communities OK (4 communities found, planted 4, modularity 0.721)
test_hybrid_search_ranks_relevant_doc_first OK
test_find_duplicate_groups_merges_transitively OK
test_report_runs_without_index_or_clusters OK
ALL TESTS PASSED
""")}
<p>Trimmed to four of 14 lines. The search and dedup checks use hand-built vectors, not a real model.</p>
<p><strong>3. Cluster a test graph.</strong> The guide built a random graph of 60 nodes in three planted groups of 20: dense inside each group (35% of node pairs linked) and sparse between them (1%).</p>
{code("""python memory_map_optimizer.py cluster --graph g.json --write-back --out clusters.json
60 nodes, 213 edges -> 3 communities (modularity 0.6082)
  cluster 2: 20 nodes
  cluster 0: 20 nodes
  cluster 1: 20 nodes
wrote clusters.json
wrote community assignments back into g.json
""")}
<p>The tool recovered the three planted groups exactly, in 0.14 seconds. <code>clusters.json</code> records the node and edge counts, the modularity, the cluster sizes and each node&rsquo;s cluster, and <code>--write-back</code> added a &lsquo;community&rsquo; field to every node in <code>g.json</code>. Leiden results depend on the seed and resolution, so other settings can give a different number of communities.</p>'''

limits = '''<h2 class="gb-h2">What these tools do not do</h2>
<ul>
<li><strong>Most were not tested at full scale.</strong> The guides ran them against a mock Transmission daemon, a canned stand-in for LM Studio, a synthetic GitHub account, a synthetic transcript and a random graph. Behaviour on real systems is less tested than the outputs suggest.</li>
<li><strong>Some can delete things.</strong> <code>archive-evict</code> deletes originals, <code>delete_archive_twins.sh --run</code> deletes repositories, and the blog checker&rsquo;s fix scripts edit posts. Use the dry runs and read the scripts first.</li>
<li><strong>The LLM tools check where an answer came from, not whether it is right.</strong> A grounded citation proves that a quote exists; a local fallback answer is a draft; a 17-question retrieval test is indicative.</li>
<li><strong>Costs and scores are estimates.</strong> The token tracker&rsquo;s cost comes from a hard-coded price table, not billing data.</li>
<li><strong>Several are tied to the author&rsquo;s setup.</strong> The blog checker is hard-coded to this blog, the memory tool and the heartbeat default to the author&rsquo;s paths, and the archive-twin list names the author&rsquo;s repositories.</li>
<li><strong>Some ship without tests.</strong> The guides found no tests in claude-lmstudio-router, transmission-client or llm-extract-citation-fix.</li>
<li><strong>They are not professional advice.</strong> The data miner returns raw open statistics, not investment advice; ship2shore_rag is not for legal, safety-critical or class decisions; delivery-playbook is not a certification text.</li>
</ul>'''

body = f"""{stats}

{intro}

<h2 class="gb-h2">Which tool for which job</h2>
{choose}

<p>Each section below says what the tool does, the one command to start with, and the main limitation its guide records. All need git to clone; extra software is noted where it matters.</p>
{sections}
{worked}

{limits}
"""

src_links = "; ".join(repo_link(t["repo"]) for t in TOOLS)
sources = ("Code: " + src_links + ". "
           "This page replaces the separate how-to guides for these thirteen repositories, written between 18 October and 9 November 2026. "
           "Every command, output and figure here is taken from those guides&rsquo; own demo runs, on the dates given in the text. "
           "Data used by the tools comes from the World Bank API, data.gov.in (Agmarknet), arXiv, Wikipedia, UK MAIB and US NTSB reports, as stated per tool.")

related = [
    ("https://masaladeutsch.blogspot.com/2026/07/ai-high-demand-launch-tracker.html", "AI Tools Edition 03: A Repo With 98,000 Stars This Tracker Had Never Heard Of"),
    ("https://masaladeutsch.blogspot.com/2026/08/indian-it-in-ai-era.html", "Indian IT in an AI Era"),
    ("https://masaladeutsch.blogspot.com/2026/10/ai-is-not-taking-indias-offshore-work.html", "AI Is Not Taking India&#x27;s Offshore Work Evenly: A Sector-by-Sector Check, and the Government Backlogs the Same Skills Could Clear"),
    ("https://masaladeutsch.blogspot.com/2026/10/half-of-php-websites-run-version-nobody.html", "Half of PHP Websites Run a Version Nobody Patches. What a Hacked Site Gives Away About Its Company"),
]

TITLE = ("Thirteen Small Open-Source Tools for Developers and AI Users, From a Local Claude Fallback "
         "to an LFS Duplicate Audit, and What Each One Is For")
STANDFIRST = ("Thirteen small repositories each solve one narrow problem: falling back to a local model when Claude is unavailable, checking an LLM&rsquo;s citations, "
              "logging token cost, searching maritime reports offline, testing a warehouse backfill, finding duplicate Git LFS storage, checking blog posts for broken code, "
              "or freeing Mac disk space safely. This guide says what each one does, the command to start with, and what its own guide found it cannot do.")

build("Open-Source Tools &middot; 12 November 2026", TITLE, STANDFIRST, body, sources, related, OUT)
print("built", OUT, "tools", len(TOOLS))
