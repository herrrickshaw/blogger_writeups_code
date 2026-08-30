# CLAUDE.md — working in this repository

This is the version-history archive for **masaladeutsch.blogspot.com**. Blogger
keeps no usable revision history, so this repo is the only way to see what a post
used to say, or to put it back.

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

169 sidecars, 188 files in `posts/` (19 are posts that left the public feed and
have no sidecar), 271 snapshot commits since 2026-08-06, and a fact-check corpus
of 186 reports. `--all` runs are long; they resume, so let them.

Cloud sessions often get a **shallow** clone. Check with
`git rev-parse --is-shallow-repository` before drawing any conclusion from
`git log` — a "this never existed" answer from a truncated history is worthless.
Run `git fetch --unshallow` first.
