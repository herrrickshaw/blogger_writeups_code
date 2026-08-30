# Repository analysis — `herrrickshaw/blogger_writeups_code`

*Compiled 18 August 2026 against commit `04e60b0` (manifest snapshot
2026-08-18T04:43 IST). Every figure below was measured from the repository as
checked out, not estimated — the command that produced each one is named so the
reading can be repeated. Where something could not be measured, it says so
rather than being filled in.*

## Scope and method

Measured: the 188 files in `posts/`, the 169 sidecars in `meta/`, the 28 scripts
in `tools/` and the 5 in `consistency-check/`, the three GitHub workflows, the 186
fact-check reports in `out/factcheck/`, and the governing documents
(`README.md`, `MAINTENANCE.md`, `DESIGN_LOG.md`, `CHANGELOG.md`,
`docs/BLOGGER_API_RUNBOOK.md`, `consistency-check/CHECKLIST.md`).

**Not measured**, and therefore not claimed anywhere below: whether the live
blog matches `posts/` right now (that needs a network read of Blogger), whether
the cron jobs in `MAINTENANCE.md` §3 are currently running (that needs
`crontab -l` on the maintainer's machine), and anything about traffic beyond
what `out/ga_report/` already holds. This is a static read of one checkout.

---

## 1. What is healthy

These were checked expecting to find problems, and did not.

**Secret hygiene is clean.** No credential file is tracked; a scan of every
tracked file for Google, OpenAI-style, Groq and OAuth token shapes returns
nothing. `.gitignore` covers `*client_secret*.json`, `*blogger_client*.json` and
`*token*.json`. The only matches for "token" in tracked paths are a post slug
about a discom token charge.

**The 2026-08-06 normalisation held.** Zero of 169 sidecars carry
`light_lock`, `dark_panel_guard`, `inverted_media_query` or
`disclaimer_in_script`. The layers that caused the contrast bug were removed and
have not crept back in over the 271 snapshot commits since.

*(Corrected 18 August 2026: an earlier revision said "~180 snapshots". The
checkout this analysis ran against was a **shallow** clone reaching back only to
2026-08-15, so no count — and no "this never existed in history" claim — was
answerable from it. Re-run after `git fetch --unshallow`: 447 commits on `main`,
271 of them snapshots since 2026-08-06. The §2.1 finding that `CLAUDE.md` was
never added is now verified across all 453 commits on all refs, rather than
inferred from a truncated history.)*

**CI is portable.** All five tools the workflows invoke — `snapshot.py`,
`site_health.py`, `link_audit.py`, `units_in_header.py`, `ai_radar.py` — resolve
their root with `Path(__file__)` rather than an absolute path, so the Actions
runners are not depending on any one machine. `archive-sync.yml` reads the
public feed with no credentials, which is what makes the disaster-recovery copy
actually independent.

**Required-element coverage is high.** `index_link` and `ai_disclosure` are
present on 168 of 169 posts (99.4%); the single exception is `about-author`,
which is a page rather than an article.

---

## 2. Findings, worst first

### 2.1 There is no `CLAUDE.md`, and there never has been

`git log --diff-filter=A` returns nothing for `CLAUDE.md`, `.claude/` or
`AGENTS.md`. Against that, the rules an agent must satisfy before it can safely
touch this repo run to **9,290 lines / 673 KB** across six documents —
`DESIGN_LOG.md` alone is 2,725 lines.

The cost is not theoretical. Preparing the Edition 03 refresh in this same
session, the working plan was to edit
`posts/ai-high-demand-launch-tracker.html` directly. That violates the
2026-08-07 rule (*"draft into `out/`, publish from `out/`, let `snapshot.py`
write `posts/`"*) and would have made the version classifier diff the new body
against itself and score a real change as a no-op. It was caught only by
grepping DESIGN_LOG's headings before writing. The log entry recording that bug
also notes that the obvious detector never finds it, because the bad edit is
committed *by* the snapshot run that mis-scores it.

So the repo carries a trap that is (a) documented, (b) invisible to tooling, and
(c) reachable by any session that does not happen to read a specific entry
2,700 lines into a design log. That is what a `CLAUDE.md` is for.

The traps a short file would need to carry, all already documented somewhere:

| Rule | Source | Consequence if missed |
|---|---|---|
| Never edit `posts/` in place before publishing | DESIGN_LOG 2026-08-07 | Version classifier scores a real change as a no-op |
| Blogger returns 200 on HEAD for dead posts — use GET | MAINTENANCE §6 | Dead posts counted as live |
| Language audit is report-only (~85% false positives) | MAINTENANCE §3 | Unattended auto-apply injects errors into live posts |
| No unattended writes to the live blog | MAINTENANCE §1 | Publishing without review |
| MAJOR = figure/conclusion changed; MINOR = new section | README | Version history stops meaning anything |
| `verify_live` probes must be flattened on both sides | MAINTENANCE §6 | False "publish failed" on dashes and interpuncts |
| `ai_radar.py` `TRACKED` entries must be lowercase | `tools/ai_radar.py` | Repo silently resurfaces in discovery every week |

### 2.2 Half of the daily fact-check spend buys nothing

`multi_model_factcheck.py` runs daily over every post (`MAINTENANCE.md` §3,
09:20 IST). Parsing all 186 reports in `out/factcheck/` by provider heading:

| Provider | Usable | Failed | Usable % | Failure |
|---|---:|---:|---:|---|
| Groq `llama-3.3-70b-versatile` | 94 | 91 | **50.8%** | 429 ×91 (tokens-per-day cap) |
| Mistral `mistral-small-latest` | 169 | 1 | 99.4% | 429 ×1 |
| Gemini `gemini-flash-latest` | 82 | 103 | **44.3%** | 429 ×99, 503 ×4 |
| Kimi `kimi-k2-0711-preview` | 0 | 172 | **0%** | 429 ×172, insufficient balance |
| Cerebras `gpt-oss-120b` | 0 | 171 | **0%** | 402 ×171, payment required |

**538 of 883 calls wasted — 60.9%.** Kimi and Cerebras have never returned a
usable answer in the entire report corpus, and are called on every post on every
run.

*(Corrected 18 August 2026. An earlier revision of this document reported
Groq at 185/0/100% and the total waste at 447 calls / 50.6%. Groq's failures are
labelled `[Groq/llama-3.3-70b-versatile …]` — with a slash — and the pattern used
to harvest them accepted word characters only, so all 91 were missed. The
correction makes the finding worse, not better: the one provider described as
fully reliable actually answers barely half the time, and on a day both Groq and
Gemini are capped the "five-model panel" can be Mistral alone.)*

The editorial consequence is the larger one. The module's docstring describes a
five-model cross-vendor panel, and the value of that design is independence —
models from outside the Claude family, disagreeing with each other. In practice
the panel is **three**, and one of those three answers less than half the time.
A post checked on a day Gemini is quota-capped got a two-model check while the
report still renders five headings, two of them error blocks. Nothing in the
report says the panel was degraded that day.

Two fixes, in order of cost:

1. Gate Kimi and Cerebras on a live-credential probe, or drop them. Recovers 343
   dead calls per full sweep and stops the reports implying a five-model check.
2. Add real fallback so a quota-capped provider is replaced rather than recorded
   as an error. This is what a gateway with quota-aware routing does; the module
   currently hand-rolls provider selection with per-key commentary and no
   fallback path.

### 2.3 The daily maintenance chain runs on exactly one machine

Six files hardcode `/Users/umashankar/masaladeutsch-archive`:

```
tools/build_md_summary.py:13        ROOT = '/Users/umashankar/...'
tools/language_audit.py:23          ROOT = '/Users/umashankar/...'
tools/daily_maintenance_cron.sh:14  cd /Users/umashankar/...
tools/update_summary_cron.sh:6      cd /Users/umashankar/...
tools/retitle_chemicals.py:26       sys.path.insert(0, '/Users/umashankar/...')
consistency-check/add_revision_line.py:19  MANIFEST = Path('/Users/umashankar/...')
```

CI is unaffected — none of these is invoked by a workflow. But they are exactly
the tools `MAINTENANCE.md` §3 documents as the daily 09:35 chain. So the
published pipeline cannot be run from a second machine, from Actions, or from a
cloud Claude Code session without editing source first.

`MAINTENANCE.md` §2 already states the underlying risk — *"Single maintainer
(Uma). No team handoff process exists yet"* — and §5 correctly claims three
independent copies of the **content**. The gap is that the *pipeline* has one
copy. Content survives the machine; the automation does not. Swapping the six
constants for the `Path(__file__).resolve().parent.parent` pattern the other 22
tools already use closes it.

### 2.4 The documented recovery path does not cover 10% of the archive

`posts/` holds **188** files; `meta/` holds **169** sidecars; the manifest counts
169. **19 posts have no sidecar**, including `_drafted-chemical-import-...`,
`tamil-nadu-wind-power-potential-niwe`, `inr-jpy-yen-the-missing-currency` and
16 others. Every one is a post that left the public feed — drafted, deleted or
republished under a new slug — which `README.md` explains is expected: the file
stays in `posts/` rather than being removed.

What is not stated anywhere is the consequence. `MAINTENANCE.md` §5 gives the
recovery path as *"`posts/<slug>.html` in the GitHub repo has every version
snapshotted (`meta/<slug>.json`'s `version_history`)"*. For these 19 there is no
sidecar, so no version history and no marker record — only whatever single body
was last captured. The recovery guarantee silently does not apply to 10% of what
is in `posts/`. Either the sidecar should be retained when a post leaves the
feed, or §5 should name the exception.

### 2.5 Semver is being applied to generated pages, where it means nothing

| Post | Version | History entries | MAJOR bumps |
|---|---|---:|---:|
| `article-index-start-here` | **v28.0.0** | 62 | 27 |
| `the-masala-deutsch-shop-books-things` | v7.2.0 | 26 | 6 |
| `upi-fees-are-now-legal-petrol-pumps` | v11.0.7 | 18 | 10 |
| `indias-wholesale-prices-next-to` | v6.0.11 | 18 | 5 |

The index page is built by `build_index_page.py` and the shop by
`build_shop.py`. Every regeneration changes counts and dates, the classifier
reads changed figures, and it scores MAJOR — 27 times for the index. Under the
README's definition (*MAJOR = a figure or conclusion changed*) each bump is
technically correct and collectively meaningless: nobody revised a conclusion 27
times, a build ran 27 times.

This costs nothing today but it degrades the one artifact the repo exists to
provide. "v28.0.0" cannot be read as editorial history the way "v2.1.0" on a
written article can. Worth either exempting generated pages from semver, or
giving them a separate `build:` counter, so a reader can tell a rewrite from a
rebuild.

### 2.6 Seven articles miss a required element

Against the frozen baseline's required-elements list, `translate_widget` is
absent from: `indias-animal-protein-export-complex`,
`indias-tyre-waste-problem-and-crumb`, `rare-earth-magnets-and-specialty-steel`,
`the-empty-shed-greenhouse-what-indias`, `the-ethanol-sectors-buyers-market`,
`vehicles-out-motors-in-indias-chapter`, `whos-actually-building-mri-and-ct`.
(`about-author` also lacks it, plus `index_link` and `ai_disclosure`, but it is a
page and arguably out of scope for the article baseline — which the baseline
itself should say.)

At 95.3% coverage this is drift, not breakage, but it is the kind that
compounds: the checklist is enforceable and nothing is currently enforcing it on
a schedule.

### 2.7 Governing docs point outside the repository

`DESIGN_LOG.md` states the enforceable form of its rules *"lives in
`~/blog-consistency-check/`"*. That directory is not in the repo — the rules are
in-repo at `consistency-check/` (`checks.py`, `audit.py`, `fix.py`), which is
where they were found for this analysis. `market-pipeline/` is referenced once and is
also not in this tree, but that reference is **correct and not drift**:
`MAINTENANCE.md` §1 points at *"that repo's `weekly_maintenance.sh`"*, and
`herrrickshaw/market-pipeline` exists as a separate private repository. Named
here only so a future reader does not go looking for a missing directory.
*(Corrected 18 August 2026: an earlier revision of this document listed it
alongside the genuine drift below.)* The drift is not confined to prose: committed data
points there too — every `path` entry in `consistency-check/fixes/manifest.json`
is an absolute `~/blog-consistency-check/fixes/...` location, and
`consistency-check/out/priority_run.log` records its report path the same way.
`add_revision_line.py` reads that manifest, so the script is resolving paths
that do not exist in this checkout. `masaladeutsch-archive` appears 10 times as a path
prefix, correct only on the maintainer's machine.

None of this breaks anything for a human who knows the layout. All of it
misdirects a reader — or an agent — who does not, and it is the same root cause
as §2.1.

---

## 3. Recommended order

1. **Write `CLAUDE.md`** carrying the seven traps in §2.1 and the correct in-repo
   paths from §2.7. Highest return, no dependencies, closes a live bug class.
2. **Gate or drop Kimi and Cerebras** (§2.2). A few lines; recovers 343 dead
   calls per sweep and stops the reports overstating the panel.
3. **De-hardcode the six paths** (§2.3) using the pattern 22 other tools use.
   Makes the daily chain reproducible off one laptop.
4. **Decide the sidecar question** for unpublished posts (§2.4) — retain, or
   document the exception in `MAINTENANCE.md` §5.
5. **Separate build versions from editorial versions** (§2.5).
6. **Re-run the required-element fix** for the seven posts in §2.6.

Items 1–3 are the ones with a failure mode attached. Items 4–6 are correctness
of the record rather than risk to it.

---

## 4. Limits of this analysis

It is a static read of one checkout on one day. It cannot tell whether the live
blog currently matches `posts/`, whether the documented cron jobs are still
firing, or whether any provider failure in §2.2 has been fixed since the last
report was written — the newest report is only as fresh as the last run. The
fact-check numbers describe 186 reports as committed, and a provider that
started failing yesterday would barely show. Re-run the counts before acting on
§2.2 if any time has passed.
