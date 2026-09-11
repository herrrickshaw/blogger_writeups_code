# Masala Deutsch — Maintenance Plan

*Last reviewed: 10 August 2026. Documents the automated pipeline as it actually
runs today, not an aspirational template — every job listed here is live in
`crontab -l` and has a script in `tools/` at the path shown.*

## 1. Purpose & Scope

This plan covers the operational upkeep of `masaladeutsch.blogspot.com` and
its local archive at `~/masaladeutsch-archive`: keeping the published site,
the GitHub mirror, the Dropbox backup, and the site-index/summary artifacts
in sync, catching regressions (grammar, broken links, stale traffic data)
before they compound, and doing all of that **without unattended writes to
the live blog** — every scheduled job here is either read-only/report-only,
or a narrowly-scoped sync of already-approved content (e.g. re-pushing a
snapshot of what's already live). No cron job drafts, edits, or publishes
new post content; that stays a manual, reviewed action.

Out of scope: content strategy, editorial calendar, the R/Python data
pipelines under `market-pipeline/` (those have their own maintenance
cadence — see that repo's `weekly_maintenance.sh`).

## 2. Ownership

Single maintainer (Uma). No team handoff process exists yet — if that
changes, this document needs a "who to page" section before it's usable as
an actual on-call reference.

## 3. Maintenance Schedule

| Time (IST) | Job | Script | Frequency | Log |
|---|---|---|---|---|
| 09:05 | Site-index footer injection | `tools/cron_inject_wrapper.sh` → `tools/inject_site_index.py --apply` | Daily | `~/Library/Logs/masaladeutsch-inject.log` |
| 09:20 | Multi-model fact/interpretation check | `tools/multi_model_factcheck.py --all` | Daily (resumes automatically; report-only) | `out/factcheck/cron.log` + one `.md` per post in `out/factcheck/` |
| 09:35 | Daily maintenance chain (3 steps, see below) | `tools/daily_maintenance_cron.sh` | Daily | `out/daily_maintenance_cron.log` |

### 09:35 chain, in order

1. **`.md` summary regeneration** — `tools/update_summary_cron.sh` → `tools/build_md_summary.py`. Rebuilds `MASALADEUTSCH_ALL_POSTS_SUMMARY.md` (all published posts, grouped by topic and chronologically, plus a Units and a Glossary reference section), skipping any post whose URL now 404s (a real GET check, not just a local-metadata check — Blogger returns 200 on HEAD even for dead posts, so HEAD alone is not sufficient here). Commits and pushes to GitHub if changed, then `rclone`-copies to `dropbox:archive/masaladeutsch-archive/`.
2. **Language audit** — `tools/language_audit.py`. Structure-aware LanguageTool sweep (title + prose blocks only; table rows excluded, which is what made the pre-2026-08-10 version of this mostly noise). Report-only: writes one `.md` per flagged post to `out/language_audit/`, plus `_summary_latest.md`. **Nothing here is auto-applied** — a manual review on 2026-08-10 found roughly 85% of LanguageTool's own suggestions were false positives (chart captions, code identifiers, valid grammar it misparsed, a few outright wrong-word substitutions), so unattended auto-apply would silently introduce real errors into live posts. Fixes get applied by hand, one confirmed finding at a time, via `tools/blogger_api.py update`.
3. **GA4 traffic snapshot** — `tools/ga_report.py --days 28`. Pageviews/active-users/country/city/top-pages for the trailing 28 days, with same-post URL aliases merged (see §6). Written to `out/ga_report/YYYY-MM-DD.md` and `out/ga_report/latest.md`, committed and pushed (needed so the cloud routine in §7 can read it — it has no access to this machine's disk).

A failed step in the chain is logged but does not block the remaining steps (`set -uo pipefail`, not `-e`, in `daily_maintenance_cron.sh`); a failed GA4 pull specifically leaves the previous day's `latest.md` untouched rather than overwriting it with an error.

## 4. Verification / "how do I know it worked"

No automated alerting exists — this is pull-based, not push-based. Ask (in
a Claude Code session against this repo) any of:

- "check the site-audit workflow results"
- "check the languagetool results" / "check the language audit results"
- "check the GA report"

and the relevant `out/` file gets read back and summarized. The daily cloud
routine (§7) does this proactively for the GA4 report specifically, once a
day, but its output lands on its own claude.ai routines page, not pushed
anywhere — it still has to be opened to be seen.

## 5. Backup & Recovery

Three independent copies of the content:
- **Live**: the blog itself, source of truth.
- **GitHub**: `herrrickshaw/blogger_writeups_code`, updated by `tools/snapshot.py --push` after any live edit (pulls the actual rendered post back down, so the archive reflects what a reader sees, not just what was sent).
- **Dropbox**: `dropbox:archive/masaladeutsch-archive/`, currently just the `.md` summary (§3 step 1) and the GA4 reports — not a full posts/ mirror.

Recovery path for "a live post got corrupted": `posts/<slug>.html` in the
GitHub repo has every version snapshotted (`meta/<slug>.json`'s
`version_history`), so a bad live edit can be reverted by re-`update`-ing
from an earlier `posts/` checkout via `tools/blogger_api.py`.

## 6. Known sharp edges (fold into future maintenance, don't relearn them)

- **Blogger's HEAD vs GET**: a dead post returns `200` on `HEAD` (custom error page) but `404` on `GET`. Any "is this URL live" check must use GET. (`build_md_summary.py`'s `is_live()`, fixed 2026-08-10.)
- **`verify_live`'s probe must be flattened the same way on both sides**: a probe built from tag-stripped source, checked against *raw* fetched HTML, fails whenever the probe text spans a tag boundary or contains a character Blogger re-encodes as a numeric HTML entity (interpunct, em/en dash). Fixed via `_flatten_html()` in `tools/blogger_api.py`, used consistently by `do_update`, `cmd_insert`, `cmd_page`, and `verify_live` itself.
- **A post's URL year/month prefix can silently drift from its `published` date**: `tools/blogger_api.py`'s `do_update` deliberately sends the existing `published` field back on every PUT (to stop Blogger re-dating a post on edit), but the permalink itself is fixed at creation time. Hitting the "naturally guessed" URL 301s to the real one — not a bug, but it splits a post's GA4 pageviews across two `pagePath` values. `ga_report.py`'s `merge_page_aliases()` resolves this by slug at report time.
- **Topic labels aren't in `index_graph.py`'s output** (`build_index_page.py`'s data source) — the topic accordion gets labels live from Blogger's own feeds instead. Anything server-rendered that needs a label at build time (e.g. the flat "All articles" list) has to load `meta/*.json` separately (`load_labels_by_slug()`).

## 7. Standing cloud routine

`masaladeutsch-ga4-daily-check` (routine id `trig_01RqNGbMD8x3DY9y4iQAYpnf`) —
daily at 10:00 IST, reads `out/ga_report/latest.md` from the GitHub mirror
(not this machine directly) and compares against the 2026-08-10 baseline,
flagging meaningful geography/traffic shifts or a stale-data signal if the
local cron stopped pushing. Output lands on the routine's own claude.ai
page, not delivered here — check it manually, or ask "check the GA report."

## 8. openDesk / XWiki documentation mirror

`tools/xwiki_mirror.py` pushes this repo's governing documentation into the
openDesk XWiki so it can be read by people who do not have the repo.

**One-directional, on purpose.** Git stays the source of truth; the wiki is a
read-only shop window. Nothing reads a wiki page back into the repo. The moment
a document can be edited in two places the two drift and neither is
authoritative — which this archive has already lived through once, with
`DESIGN_LOG.md` pointing at `~/blog-consistency-check/` for rules that were
actually in-repo. Do not add a write-back path without deciding first which
side wins.

Mirrored: `README.md`, `CLAUDE.md`, `MAINTENANCE.md`, `DESIGN_LOG.md`,
`SEO_KEYWORDS.md` and the six files in `docs/`. The list is explicit in
`MIRRORED`, not a glob, because this tool publishes to somewhere other people
read and a glob would sweep in whatever lands in `docs/` next.

Deliberately excluded: `CHANGELOG.md` and `MASALADEUTSCH_ALL_POSTS_SUMMARY.md`.
Both are generated, both change daily, and mirroring them would bury the
hand-written docs in churn.

```bash
python3 tools/xwiki_mirror.py                 # report-only: what would change
python3 tools/xwiki_mirror.py --apply         # push the changed pages
python3 tools/xwiki_mirror.py --self-test     # prove push+verify without the live wiki
```

Report-only is the default — `--apply` is required to write anything.

**It verifies rather than trusting the HTTP status.** Every page it writes is
read back and compared byte-for-byte against what was sent, and a mismatch is
reported as a problem instead of a success. This is the §6 lesson applied
ahead of time: the daily chain still echoes "committed + pushed" whether or not
the push worked, and that cost two days of unnoticed backlog on 8-9 Sep 2026.

It also checks the syntax the wiki actually stored. If XWiki does not have
`markdown/1.2` enabled it will silently keep the page in its own syntax and the
Markdown will render as literal text; the tool reports that rather than
leaving you to find it in the browser. Override with `--syntax` if the
instance uses something else.

Configuration lives in `~/.config/market-secrets/credentials.env`, never in the
repo — `XWIKI_BASE_URL`, `XWIKI_USER`, `XWIKI_TOKEN`, and optionally
`XWIKI_SPACE` (defaults to `masaladeutsch`).

Not yet wired to a schedule. Running it from CI needs the same four values as
GitHub repository secrets; until then it is a manual step after a docs change.

## 9. Review cycle

No fixed cadence yet. Revisit this document whenever a new daily/weekly job
is added to `crontab`, or when one of the sharp edges in §6 recurs somewhere
new — that's the signal the underlying fix needs to be generalized rather
than patched locally again.
