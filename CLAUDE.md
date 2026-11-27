# CLAUDE.md — working in this repository

**Folder:** commands for the user's Mac start with `cd ~/vertistrat-archive` (or use `tools/vblog`). Never `~/masaladeutsch-archive`: that is a different repo. The Pages repo `herrrickshaw/masaladeutsch` hosts `accordion.js` and is not renamed.

This is the version-history archive for the blog now published as **VertiStrat Solutions**
at **blog.vertistratsolution.com** (formerly Masala Deutsch, masaladeutsch.blogspot.com;
migrated 14 Nov 2026 -- never write the old domain or name into a post). Blogger
keeps no usable revision history, so this repo is the only way to see what a post
used to say, or to put it back.

**Knowledge graph (related links and keyword hubs):** `tools/keyword_graph.py` learns each article's keywords and phrases from the text and pairs articles that share them; `tools/index_graph.py --hubs` feeds the same graph to the index. Rebuild the index with `python3 tools/index_graph.py --json /tmp/graph.json --hubs /tmp/hubs.json`, then `python3 tools/build_index_page.py --graph /tmp/graph.json --hubs /tmp/hubs.json --out /tmp/fresh-index.html`, then the splice step. For a new draft, `python3 tools/keyword_graph.py --suggest <name> --file out/<draft>.html` lists the live articles to link from it, with the shared terms as the reason. `out/knowledge-graph.json` is the full graph (keywords, related links, hubs).

**Titles and section headings follow `docs/HEADLINE_STYLE.md`** (plain reference tone:
"Subject: what the data shows", sentence case, <= 90 characters, no idioms or teasers),
so they survive the 15-language translate widget.

**New and rewritten posts are visual-first** (`docs/VISUAL_STORY_STYLE.md`): a three-bullet top line,
three or four insight sections of one chart plus two sentences, charts built with `tools/exec_viz.py`
(phone-sized, no open data grids). Check phone rendering with `node tools/mobile_audit.js <file>`.

**The single most important fact: `posts/` and `meta/` are OUTPUTS, not a
workspace.** `tools/snapshot.py` writes them by pulling the live blog. Editing
them by hand breaks the thing the repo exists to provide. See rule 1 below.

---

## Rules that will bite you

Each of these has cost someone real work. They are not style preferences.

### 1. Never edit `posts/` or `meta/` in place

Draft into `out/`, publish from `out/`, let `snapshot.py` write `posts/`.

`snapshot.py` decides a post's version bump by diffing the on-disk previous body
against the freshly fetched one. If you draft your changes *into* `posts/` and
then publish from there, both sides of that diff are the new body — every change
looks like a no-op, and a real revision gets recorded as a PATCH with the reason
"visible text identical". This happened once (the WPI post, 2026-08-07) and the
audit that found it noted the obvious detector never will: the bad edit is
committed *by* the snapshot run that mis-scores it.

Existing drafts live at `out/post-<topic>.html` — reuse the file for that post.

### 2. Blogger returns HTTP 200 on HEAD for dead posts

A deleted or drafted post serves a custom error page with status 200 to `HEAD`,
and 404 only to `GET`. Any "is this URL still live" check must use GET.
(`build_md_summary.py`'s `is_live()`.)

### 3. The language audit is report-only — never auto-apply it

A manual review on 2026-08-10 found roughly **85% of LanguageTool's suggestions
were false positives** on this content: chart captions, code identifiers, valid
grammar it misparsed, and some outright wrong-word substitutions. Unattended
auto-apply would silently introduce real errors into live posts. Fixes get
applied by hand, one confirmed finding at a time.

The same contract covers `tools/multi_model_factcheck.py`: model output is not a
verified fact. Every flagged claim needs primary-source confirmation before it
changes anything.

### 4. No unattended writes to the live blog

Every scheduled job is read-only, report-only, or a narrowly-scoped sync of
already-approved content. Nothing on a timer drafts, edits or publishes post
content. Publishing is a manual, reviewed action. Keep it that way.

### 5. Version bumps mean something

**MAJOR** = a figure or conclusion changed · **MINOR** = a section was added ·
**PATCH** = wording, styling, a typo, a URL move.

`snapshot.py` classifies heuristically and gets it wrong sometimes; override with
`--as major|minor|patch`. Rationale in `DESIGN_LOG.md`.

### 6. `verify_live` probes must be flattened on both sides

A probe built from tag-stripped source but checked against raw fetched HTML fails
whenever the probe text spans a tag boundary or contains a character Blogger
re-encodes as a numeric entity (interpunct, em/en dash). Use `_flatten_html()` in
`tools/blogger_api.py` on both sides — `do_update`, `cmd_insert`, `cmd_page` and
`verify_live` all do.

### 7. `TRACKED` entries in `tools/ai_radar.py` must be lowercase

The membership test is `fn.lower() in TRACKED`. A capitalised entry silently
never matches, and the repo resurfaces in weekly discovery forever.

### 8. Every problem piece proposes fixes (rule added 2026-09-19)

If a post's finding is a problem — a number the government publishes two ways,
a scheme graded on an ungradeable ratio, a technology gap, a survey with a
seam through it — the post carries a `What would fix this` section before its
"What this piece does and doesn't cover" caveats: three to five concrete,
checkable proposals, each something a named agency could actually do, closed
with the line "These are proposals from this blog, not recommendations any
agency has adopted." Highlighting a problem without saying what would fix it
is a draft, not a post. Applied to every post published from 2026-09-19;
retrofitting earlier posts is a separate, tracked job.

---

## Where things actually live

`DESIGN_LOG.md` says the enforceable rules live in `~/blog-consistency-check/`.
**They do not — they are in this repo**, and that stale pointer has misdirected
readers before:

| What | Where |
|---|---|
| Rule definitions | `consistency-check/checks.py` (`STATIC_RULES`) |
| Two-pass checker | `consistency-check/audit.py` |
| Repair generator | `consistency-check/fix.py` |
| Post skeleton | `templates/post-skeleton.html` |
| House style, and why | `DESIGN_LOG.md` (newest entries at the **bottom**) |
| Pipeline, schedules, sharp edges | `MAINTENANCE.md` |
| Blogger API recipes | `docs/BLOGGER_API_RUNBOOK.md` |

`market-pipeline/` is referenced in `MAINTENANCE.md` §1 and is a **separate
private repo** (`herrrickshaw/market-pipeline`), not a missing directory here.

---

## Changing a published post

```bash
# 1. draft into out/ (never into posts/ — see rule 1)
#    edit out/post-<topic>.html

# 2. publish, dry-run first
python3 tools/blogger_api.py update --slug <slug> --file out/post-<topic>.html --dry-run
python3 tools/blogger_api.py update --slug <slug> --file out/post-<topic>.html

# 3. let snapshot write posts/ and meta/, and set the level deliberately
python3 tools/snapshot.py --as major --note "why you ran this" --push

# 4. check the published result against the house rules
#    (audit.py fetches over the network; it checks live URLs, not local drafts)
python3 consistency-check/audit.py --url <live post url>
```

Never skip step 3, and never hand-edit `meta/*.json` — the sidecar's `bytes` and
`sha256` describe what Blogger actually serves.

## Verifying your work

The ten static rules in `consistency-check/checks.py` are the enforceable spec:
`js-parses`, `no-disclaimer-in-script`, `no-inverted-media-query`,
`dark-vars-locked`, `wpi-attribution`, `disclaimer-present`, `translate-widget`,
`index-link`, `bw-override`, `table-units-in-header`.

`r_scripts_parse` expects `node_check` to be **the list of scripts that already
failed a syntax check**, not a callable — compute it first and pass the result.

An interactive-embed post (the AI Tracker dashboard) renders its cards from a
JavaScript `DATA` array. Run that script against a DOM shim before publishing;
a syntax error there silently blanks the whole board.

## Things that are machine-specific by design

The cron wrappers call `/opt/homebrew/bin/python3` by absolute path because cron
runs with a minimal `PATH`. That is deliberate — do not "fix" it. Repo paths in
those scripts are resolved relative to the script (`$(dirname "$0")/..`), so the
chain itself is not tied to one machine.

`consistency-check/fixes/manifest.json` still stores absolute
`~/blog-consistency-check/fixes/...` paths in its `path` field, and
`add_revision_line.py`, `add_index_link.py` and `blogger_api.py` all open that
field directly — so those three fail outside the original machine. Known, not
yet fixed.

## Scale, so you know what a full run costs

Order of magnitude, not a figure to quote: a couple of hundred posts, a
matching sidecar for each, several hundred snapshot commits since 2026-08-06,
and a fact-check corpus in the low hundreds. `--all` runs are long; they
resume, so let them.

**This section deliberately carries no exact counts.** They were pinned twice
and went stale twice inside a single day — the archive gained five posts and
seven snapshot commits in one three-hour stretch — and a stale number in a
document a newcomer is told to trust is worse than no number at all. Read the
current values instead:

```bash
ls posts/ | wc -l
ls meta/*.json | grep -v manifest.json | wc -l
git log --oneline --grep='^snapshot ' | wc -l
```

Expect the snapshot count to differ by one or two between a branch and `main`:
merge commits change what is reachable. That is normal and is another reason
not to treat any single reading as authoritative.

Do **not** add `--since=2026-08-06` to that last command. It looks like the
obvious way to scope the count, and it silently undercounts by around fifteen:
`--since` prunes on commit timestamps, and the archive's opening commits carry
a `+05:30` offset that puts them on the far side of the UTC boundary, so the
filter excludes part of the very day it names. The shortfall is a fixed set of
early commits, so it does not shrink as the archive grows. Every snapshot
commit is reachable from `HEAD` anyway, so no date filter is needed — compare
the two counts yourself if you want to see the gap.

Sidecar coverage is **complete apart from posts published since the last
snapshot run**, which is the normal steady state: `blogger_api.py` writes the
post, `snapshot.py` writes the sidecar, and between those two the slug shows up
as uncovered. Those clear themselves on the next snapshot. What is *not* normal
is an uncovered slug that survives several snapshot runs — that is a post which
left the public feed and took its sidecar question with it (19 were in that
state as of 2026-08-18), and MAINTENANCE §5's per-post `version_history`
recovery does not cover it. Run this, then re-run it after the next snapshot to
tell the two apart:

```bash
comm -23 <(ls posts/ | sed 's/\.[^.]*$//' | sort -u) \
         <(ls meta/ | sed 's/\.json$//' | sort -u)
```

Cloud sessions often get a **shallow** clone. Check with
`git rev-parse --is-shallow-repository` before drawing any conclusion from
`git log` — a "this never existed" answer from a truncated history is worthless.
Run `git fetch --unshallow` first.

## Cross-session project memory

A session rooted here has no memory of its own. Decisions and hazards for the
broader personal-projects portfolio (of which this archive is one) live under
the `~` (home) session, indexed by `~/.claude/projects/-Users-umashankar/memory/MEMORY.md`
— reach it with `qmd search "<topic>"` rather than assuming this session
remembers anything. A point-in-time snapshot of 128 incident-sourced rules
distilled from that memory is browsable at
https://claude.ai/code/artifact/e29ceaeb-099e-4de7-ab43-dcd97a2d8f57
("Ways of Working"), good for fast orientation but not authoritative over
anything specific to this repo — the rules above override it where they
conflict.

<!-- source-fetch-toolkit:v1 (managed by ~/bin/add_source_fetch_section.py — edit there, not here) -->
## Source fetching for data collection & literature surveys

When a task needs a primary document (statute, regulator data, government release, paper, filing),
fetch the document itself — never cite a search snippet as if it had been read.

- **On the owner's Mac:** `fetch_source.py "<url | doi:… | celex:… | arxiv:…>" --out ./sources`
  (in `~/bin`; full guide `~/bin/SOURCE_FETCH_TOOLKIT.md`). Scheduled/unattended runs use only
  `bash /Users/umashankar/bin/fetch_source.sh "<target>"` (allowlisted) and then Read the `.txt` it reports.
- **Elsewhere (cloud sessions, CI):** follow the same ladder by hand — direct GET with a browser User-Agent →
  headless browser only if the page needs JavaScript → official alternates (DOI → OpenAlex
  `api.openalex.org/works/doi:<doi>` locations → repository copy; EUR-Lex → EU Publications Office
  `publications.europa.eu/resource/celex/<CELEX>`; arXiv pdf/abs) → Wayback Machine `id_` snapshot.
- **Hard rule:** a CAPTCHA, robot check, Cloudflare/Akamai/WAF challenge or login wall means stop on that
  host. Do not bypass it (no TLS impersonation, stealth browsers, identity rotation or challenge solving);
  look for the same document via another route, or report it as unavailable.
- **Record** for every figure: URL read, title/date, page/table, fetch route; mark abstract-only or
  snippet-only sources. Fetch politely (~1 request/second per host, no bulk crawling).
<!-- /source-fetch-toolkit -->

<!-- BACKLOG.MD GUIDELINES START -->
<!-- backlog.md-instructions-version: 1.55.3 -->
<CRITICAL_INSTRUCTION>

## Backlog.md Workflow

This project uses Backlog.md for task and project management.

**At the beginning of each conversation in this project, run `backlog instructions overview` before answering or taking action. Re-read it only if you have not read it yet in the current conversation.**

Use the overview to decide whether to search, read, create, or update Backlog tasks.

Before task lifecycle actions, read the matching detailed guide:
- `backlog instructions task-creation` before creating or splitting tasks
- `backlog instructions task-execution` before planning, changing status or assignee, adding a plan or implementation notes, or implementing task work
- `backlog instructions task-finalization` before checking acceptance criteria, writing final summaries, or moving tasks to terminal statuses

Use `backlog <command> --help` before running unfamiliar commands. Help shows options, fields, and examples.

Do not edit Backlog task, draft, document, decision, or milestone markdown files directly. Use the `backlog` CLI so metadata, relationships, and history stay consistent.

</CRITICAL_INSTRUCTION>
<!-- BACKLOG.MD GUIDELINES END -->
