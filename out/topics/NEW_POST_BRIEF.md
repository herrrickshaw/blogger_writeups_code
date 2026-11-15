# Brief: build one new visual-first post (read all of it)

Repo: /home/user/blogger_writeups_code. You own only `out/research/<your-dir>/**` and `out/post-<your-slug>.html`.
No git, no blogger_api, no edits under posts/ meta/ tools/ templates/ theme/ docs/. Nothing is published.
Today is 15 Nov 2026. The blog is VertiStrat Solutions (blog.vertistratsolution.com); never write the old name or domain.

## Format (docs/VISUAL_STORY_STYLE.md and docs/HEADLINE_STYLE.md: read both, they are short)
- Title: "Subject: what the data shows", sentence case, 55-80 characters (90 max), one key number, no idioms, no questions.
- Top line: three bullets, each opening with a big number (`top_line`). Then 3 or 4 insight sections (`insight`): an h2 that
  states the finding, ONE chart whose title states the takeaway, then exactly two sentences (What it means / What to do).
- A numbered "What would fix this" list (3 to 5 proposals, each by a named body), closed with the line
  "These are proposals from this blog, not recommendations any agency has adopted."
- Collapsed `<details>` for method and "What this piece could not establish". Sources and caveats block, related links.
- Paragraphs 60 words or fewer. No open data grids; numbers behind a chart go in `numbers()`.
- Build parts with tools/exec_viz.py (bars, line, waterfall, flow, top_line, insight, numbers, sources_block, STYLE).
- Assemble with tools/postbuild/buildpost.py `build(kicker, title, standfirst, body, sources, related, out)` as
  out/research/chloride-ethanol/build_post.py does, with the body made from exec_viz parts as in
  out/research/chloride-ethanol/build_visual.py (read both; copy the pattern, including STYLE at the top of the body).
- Related links: 3 to 5 live posts from meta/manifest.json (pick by topic; use the manifest `url`; do not link to a post whose
  slug is in out/gsc_index/phase1_remove.json or phase3_map.json).

## Data rules (this is what makes the post worth publishing)
1. Research with the tool `mcp__Parallel_Search__web_search` (load its schema with ToolSearch "select:mcp__Parallel_Search__web_search,mcp__Parallel_Search__web_fetch"; reuse one random session_id). WebFetch does not work in this environment; web_fetch of the Parallel tool may.
2. Prefer primary sources (IEA, PPAC, ICAO, European Commission, ministry/PIB releases, company filings). A figure that rests on
   a single secondary page is labelled as such in the post, or left out.
3. Every number in the post is either in a source you read, or computed in the build script with an `assert` on the arithmetic.
   Put each source's URL and date beside the constant in the script as a comment, and keep the same list in the post's sources block.
4. Never round a figure into a different claim; keep "about", "reported", "projected". Where two sources disagree, say so.
5. One unit per chart. Never mix a flow, a stock and a norm on one axis.
6. If you cannot confirm something the headline needs, change the headline. Do not invent or fill a gap.

## Check before you reply
- `python3 out/research/<dir>/build.py` runs clean and writes `out/post-<slug>.html`.
- `node tools/mobile_audit.js out/post-<slug>.html` shows no overflow or tiny-chart flags (read the tool's usage first).
- Re-read the output text once: every figure traceable, title obeys the headline rules, no "you/we".
- Reply in under 120 words: the title, the three top-line bullets, what you left out because it was unconfirmed, any figure
  in sources that disagree.
