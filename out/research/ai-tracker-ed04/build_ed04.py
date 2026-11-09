#!/usr/bin/env python3
"""Build AI Tracker Edition 04 (9 Nov 2026) from the Edition 03 post template.

Inputs (all in this folder): cards_A.json, cards_B.json (launch board research),
ed03_cards.json (Edition 03 board), radar.json (tools/ai_radar.py --days 45),
stars_2026-11-09.json (GitHub search API star counts).
Output: out/post-ai-tracker-edition-04.html
"""
import json, re, html, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
T = (ROOT / "posts/ai-high-demand-launch-tracker.html").read_text()
A = json.load(open(HERE / "cards_A.json"))
B = json.load(open(HERE / "cards_B.json"))
ED03 = json.load(open(HERE / "ed03_cards.json"))
RADAR = json.load(open(HERE / "radar.json"))
STARS = json.load(open(HERE / "stars_2026-11-09.json"))


def rep(t, old, new, count=1):
    n = t.count(old)
    assert n == count, (n, old[:80])
    return t.replace(old, new)


# ---------------- board ----------------
board, seen = [], set()
for c in B["new"] + A["new"]:          # B first: its dsh-superagent card wins the dedupe
    key = re.sub(r"\W+", "", c["name"].lower())[:12]
    if key in seen:
        continue
    seen.add(key)
    board.append(c)
n_new = len(board)
for c in A["carryover_updates"] + B["carryover_updates"]:
    board.append(c)
n_upd = len(A["carryover_updates"]) + len(B["carryover_updates"])
UNCHANGED = {"Gemini agent", "Agents API (public beta)", "Copilot Autopilot"}
for c in ED03:
    if c["name"] in UNCHANGED:
        c = dict(c, isNew=False)
        c["why"] = re.sub(r"^NEW(?: raise)?:\s*", "CARRIED OVER (no change this window): ", c["why"])
        board.append(c)
assert len([c for c in board if c["name"] in UNCHANGED]) == 3
cat_order = {"foundation": 0, "agentic": 1, "coding": 2, "consumer": 3, "automation": 4}
board.sort(key=lambda c: (not c["isNew"], cat_order[c["cat"]]))
n_found = sum(1 for c in board if c["cat"] == "foundation")
retired = [r["name"] for r in A["retire"] + B["retire"]]

FUND = [("Serval", 150, "Series C"), ("Traversal", 120, "Series B"), ("Pliant", 80, "Series C"),
        ("Daytona", 60, "Series B"), ("Greptile", 50, "Series B")]
fund_total = sum(v for _, v, _ in FUND)
assert fund_total == 460

top = RADAR[0]
assert top["repo"] == "deepseek-ai/dsh-superagent-prototype"
dsh = STARS["deepseek-ai/dsh-superagent-prototype"]["stars"]
dinf = STARS["deepseek-ai/deepinfer"]["stars"]
assert dsh + dinf > 47000

# ---------------- header ----------------
t = T
t = rep(t, "AI Tracker &middot; Edition 03 &middot; Refresh &middot; 9 October 2026",
        "AI Tracker &middot; Edition 04 &middot; 9 November 2026")
t = rep(t, "OpenAI Shipped GPT-6 and Agents That Keep Working After You Log Off. Google Kept Its Best Model for Cyber Defenders.",
        "DeepSeek Put Its Agent and Its Inference Engine on GitHub. They Drew 47,000 Stars in Under Four Weeks.")
s = t.find('class="standfirst">'); e = t.find("</p>", s)
t = t[:s] + ('class="standfirst">Edition 04 covers 10 October to 9 November 2026 with both of the tracker&rsquo;s instruments refreshed. '
             'The <b>GitHub radar</b> ranks new repositories by stars per day, read directly from GitHub&rsquo;s API on 9 November; DeepSeek&rsquo;s '
             'agent prototype and inference engine top it. The <b>launch board</b> logs models, agent tools and funding rounds, each tagged '
             '<b>Verified</b> (first-party page, repository or reputable press) or <b>Reported</b> (one secondary source); Google, OpenAI and '
             'GitHub&rsquo;s Universe conference filled most of it.') + t[e:]

# ---------------- funding figure ----------------
fs = t.find('<figure class="gb-figure"'); fe = t.find("</figure>", fs) + len("</figure>")
bars, x0, w, gap, base, hmax = [], 70, 92, 32, 300, 190
for i, (name, v, rnd) in enumerate(FUND):
    x = x0 + i * (w + gap); h = round(hmax * v / 150); cx = x + w // 2
    bars.append(f'<rect x="{x}" y="{base - h}" width="{w}" height="{h}" fill="#0b5794" />\n'
                f'<text x="{cx}" y="{base - h - 12}" font-size="20" fill="#0b5794" font-weight="bold" text-anchor="middle">${v}M</text>\n'
                f'<text x="{cx}" y="322" font-size="14" fill="#1a1a1a" text-anchor="middle" font-weight="bold">{name}</text>\n'
                f'<text x="{cx}" y="340" font-size="12" fill="#595959" text-anchor="middle">{rnd}</text>')
fig = ('<figure class="gb-figure" style="margin:1.5rem 0 1.75rem;text-align:center">\n'
       '<svg role="img" aria-label="Five AI-tooling funding rounds, 19 October to 4 November 2026, $460M combined" style="width:100%;height:auto;max-width:700px;display:block;margin:0 auto" viewBox="0 0 700 380" xmlns="http://www.w3.org/2000/svg" font-family="Georgia,\'Times New Roman\',serif">\n'
       '<rect x="0" y="0" width="700" height="380" fill="#f8f9fa" />\n'
       '<text x="40" y="42" font-size="20" fill="#1a1a1a" font-weight="bold">Fresh AI-Tooling Funding</text>\n'
       '<text x="40" y="64" font-size="13.5" fill="#4a4a4a">Five rounds announced 19 Oct &#8211; 4 Nov 2026 &middot; $460M combined &middot; all confirmed by the companies</text>\n'
       '<line x1="50" y1="300" x2="660" y2="300" stroke="#c9c9c9" stroke-width="1" />\n'
       + "\n".join(bars) +
       '\n<text x="40" y="365" font-size="11.5" fill="#8a8a8a">Sources: company announcements and Business Wire releases; TechCrunch and Fortune for Daytona &middot; masaladeutsch AI Tracker Edition 04</text>\n'
       '</svg>\n'
       '<figcaption style="font-size:.8em;color:#868e96;font-family:-apple-system,\'Segoe UI\',sans-serif;margin-top:.5rem">Five AI-tooling rounds between 19 October and 4 November 2026 came to $460M: agents that build enterprise service workflows (Serval), agents that investigate production incidents (Traversal), payment accounts for AI agents (Pliant), sandboxed machines for long-running agents (Daytona) and AI code review (Greptile). Daytona&rsquo;s round is dated 20 October by Fortune and 23 October by TechCrunch. Nous Research&rsquo;s $90M (7 October), now confirmed by the company, was logged in Edition 03.</figcaption>\n'
       '</figure>')
t = t[:fs] + fig + t[fe:]

# revision line; drop the Cloudflare photo (Cloudflare items are retired this edition)
t = rep(t, 'Revised <time datetime="2026-10-09" itemprop="dateModified">9 October 2026</time> &middot; v5.0.0 &middot; Edition 03 refresh &middot; 17 new movers this window',
        f'Published <time datetime="2026-11-09" itemprop="dateModified">9 November 2026</time> &middot; v1.0.0 &middot; Edition 04 &middot; {n_new} new movers this window')
cs = t.find('<figure style="margin:1.6rem 0">\n<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Cloudflare')
ce = t.find("</figure>", cs) + len("</figure>")
assert cs > 0
t = t[:cs] + t[ce:]

# ---------------- notes ----------------
ns = t.find('<section class="notes">'); ne = t.find('<div class="legend">', ns)
notesA = A["notes"]; notesB = B["notes"]
li = lambda x: f"      <li>{x}</li>\n"
notes = ('<section class="notes">\n    <h2>Consistency &amp; methodology notes</h2>\n'
         '    <p>Every board item links one source. It is labelled <strong>Verified</strong> where that source is a first-party page, repository or changelog, '
         'or reputable press found by its own URL, and <strong>Reported</strong> where it rests on a single secondary source. Benchmark, usage and customer figures are '
         'the companies&rsquo; own unless a card says otherwise.</p>\n'
         f'    <p><strong>What changed this edition (window 10 October to 9 November):</strong> {n_new} new movers, {n_upd} earlier items with a new development, '
         f'and three carried over unchanged (Gemini agent, OpenAI&rsquo;s Agents API and Copilot Autopilot). {len(retired)} items were retired because they predate '
         f'the window, were superseded or had no new development: {html.unescape(", ".join(retired))}.</p>\n'
         '    <ul>\n'
         + li('<strong>GitHub star counts were re-read on 9 November</strong> from GitHub&rsquo;s search API (Edition 03 could not read the API). '
              'Ruflo (ruvnet/ruflo) now has 81,324 stars, up from 67.6k on 11 August.')
         + li('<strong>Correction to Edition 03 &mdash; Graphify.</strong> Edition 03 gave Graphify as 16 stars and called claims of 85,000+ stars unverified. '
              'The 16 stars belong to a different, small repository (rhanka/graphify). The project the tracker follows, Graphify-Labs/graphify, is real and '
              'had 144,768 stars on 9 November.')
         + li('<strong>Moved or gone:</strong> OmniRoute now lives at cheaper-inference/OmniRoute (85,834 stars); madslorentzen/ai-job-search no longer appears '
              'on GitHub and is dropped from the watch list.')
         + li("<strong>Dates that differ between sources</strong> are shown as given, not resolved: " + notesA[1].split(":",1)[1].strip() + " " + notesB[1].split(":",1)[1].strip())
         + li(notesA[2])
         + li("<strong>Single-source or company-reported figures:</strong> " + notesA[4].split(":",1)[1].strip() + " " + notesB[2].split(":",1)[1].strip())
         + li(notesA[3])
         + li("<strong>Name-collision watch:</strong> " + notesA[6].split(":",1)[1].strip() + " " + notesB[5].split(":",1)[1].strip())
         + li("<strong>Just outside the window, so not carded:</strong> " + notesB[4].split(":",1)[1].strip())
         + li("<strong>Missed by Edition 03:</strong> " + notesA[0].split(":",1)[1].strip())
         + li('<strong>Freshness bias:</strong> the board prioritises roughly the last four to eight weeks. Carried-over items say what, if anything, changed.')
         + '    </ul>\n    ')
t = t[:ns] + notes + t[ne:]

# ---------------- board data and KPIs ----------------
ds = t.find("var DATA = ["); de = t.find("];", ds)
t = t[:ds] + "var DATA = " + json.dumps(board, ensure_ascii=False, indent=0).replace("\n", "\n    ") + t[de + 1:]
t = rep(t, '{n:"17", l:"New this refresh", d:"added since 11 Aug", c:"up"}', f'{{n:"{n_new}", l:"New this edition", d:"added since 9 Oct", c:"up"}}')
t = rep(t, '{n:"$690M", l:"Fresh funding logged", d:"Temporal &middot; Nous &middot; AIR", c:"up"}',
        '{n:"$460M", l:"Fresh funding logged", d:"5 rounds, 19 Oct&ndash;4 Nov", c:"up"}')
t = rep(t, '{n:"67.6k", l:"Top repo stars (Ruflo)", d:"snapshot 11 Aug (not re-read)", c:"flat"}',
        f'{{n:"{dsh/1000:.1f}k", l:"Fastest new repo", d:"DeepSeek dsh-superagent, {top["stars_per_day"]:,.0f} stars/day", c:"up"}}')
t = rep(t, '{n:"6", l:"Foundation-model moves", d:"Aug&ndash;Oct 2026 window", c:"up"}',
        f'{{n:"{n_found}", l:"Foundation-model moves", d:"10 Oct&ndash;9 Nov window", c:"up"}}')

# ---------------- GitHub radar section ----------------
flags = {"ccch1mneyyy/dsh-Go": "Unofficial: a phone port of DeepSeek&rsquo;s harness by an individual developer, not by DeepSeek.",
         "tangency-labs/solidcraft": "Check before relying on it: 6,710 open issues against 15,163 stars is unusual and may be automated filing.",
         "wheresryan22/anatomy": "No commits since 18 October; growth came in its first ten days."}
TRANSLATED = {"ccch1mneyyy/dsh-Go": "dsh-go: DeepSeek Harness in your pocket. Runs on the phone itself and can also control your computer remotely.",
              "KKKKhazix/agent-autoloop": "Lets a command-line agent take on and follow through tasks in the background, and sends a card only when it needs a decision."}
brk = lambda n: html.escape(n).replace("/", "/<wbr>").replace("-", "-<wbr>")
rows = []
for r in RADAR[:10]:
    st = STARS.get(r["repo"].lower(), {})
    stars = st.get("stars", r["stars"])
    d0 = TRANSLATED.get(r["repo"], r["description"])
    desc = html.escape(d0[:110]) + ("&hellip;" if len(d0) > 110 else "") + (" (translated from Chinese)" if r["repo"] in TRANSLATED else "")
    flag = flags.get(r["repo"], "")
    rows.append(f'<tr><td><a href="{r["url"]}" rel="noopener">{brk(r["repo"])}</a><br><span style="font-size:.82em;color:#595959">{desc}'
                + (f'<br><em>{flag}</em>' if flag else "") + f'</span></td><td style="text-align:right">{stars:,}</td>'
                f'<td style="text-align:right">{r["stars_per_day"]:,.0f}<br><span style="font-size:.8em;color:#595959">{r["age_days"]} days</span></td></tr>')
watch = [("thedotmack/claude-mem", "Claude-Mem"), ("Graphify-Labs/graphify", "Graphify"), ("cheaper-inference/OmniRoute", "OmniRoute"),
         ("ruvnet/ruflo", "Ruflo"), ("usestrix/strix", "Strix"), ("nutlope/hallmark", "Hallmark"), ("justvugg/colibri", "Colibri"),
         ("deusdata/codebase-memory-mcp", "Codebase Memory MCP"), ("hkuds/vibe-trading", "Vibe Trading"), ("iofficeai/officecli", "OfficeCLI"),
         ("xai-org/grok-build", "Grok Build"), ("langchain-ai/openwiki", "OpenWiki")]
wrows = []
watch.sort(key=lambda w: -STARS[w[0].lower()]["stars"])
for repo, nm in watch:
    st = STARS[repo.lower()]
    wrows.append(f'<tr><td><a href="https://github.com/{repo}" rel="noopener">{nm}</a><br><span style="font-size:.82em;color:#595959">{brk(repo)}</span></td>'
                 f'<td style="text-align:right">{st["stars"]:,}</td></tr>')
radar_html = f'''
<h2 class="gb-h2">GitHub radar: the fastest-rising new repositories</h2>
<p>New repositories created since 25 September 2026 with at least 1,000 stars, ranked by stars per day since creation. That rewards a three-week-old project gaining fast over an older one sitting on a large total. Counts were read from GitHub&rsquo;s API on 9 November 2026 by <code>tools/ai_radar.py</code>, which runs eleven searches (agent, llm, mcp, topic:ai and others), removes duplicates and leaves out repositories the tracker already follows.</p>
<div style="overflow-x:auto"><table class="gb-table" style="width:100%;border-collapse:collapse;font-size:.9em">
<thead><tr><th style="text-align:left">Repository</th><th style="text-align:right">Stars</th><th style="text-align:right">Stars a day</th></tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody></table></div>
<p style="font-size:.85em;color:#595959">A star is a bookmark: it measures attention, not use, and it can be bought. Creation date is not launch date, so a project built in private and opened to a waiting audience shows an inflated rate. GitHub search is not a census, so absence here is not evidence of absence.</p>
<h3>Repositories the tracker already follows, 9 November 2026</h3>
<div style="overflow-x:auto"><table class="gb-table" style="width:100%;border-collapse:collapse;font-size:.9em">
<thead><tr><th style="text-align:left">Project</th><th style="text-align:right">Stars</th></tr></thead>
<tbody>
{chr(10).join(wrows)}
</tbody></table></div>
'''
anchor = '<div class="note"><b>How this refresh relates to Edition 03\'s own rule.</b>'
ai = t.find(anchor); ae = t.find("</div>", ai) + len("</div>")
assert ai > 0
t = t[:ai] + radar_html + ('<div class="note"><b>Two instruments, kept apart.</b> The GitHub radar measures open-source attention; the launch board records what '
                           'companies shipped or raised, including much that never appears on GitHub. They are not merged into one score. '
                           'The previous edition is <a href="https://masaladeutsch.blogspot.com/2026/07/ai-high-demand-launch-tracker.html">AI Tools Edition 03</a>.</div>') + t[ae:]

out = ROOT / "out/post-ai-tracker-edition-04.html"
out.write_text(t)
print(f"board {len(board)} (new {n_new}, updated {n_upd}, unchanged 3); retired {len(retired)}; foundation {n_found}; wrote {out} {len(t):,} bytes")
