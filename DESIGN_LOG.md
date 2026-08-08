# Design log — masaladeutsch.blogspot.com

Decisions about how posts look and are built, why they were made, and what was
rejected. Newest at the bottom. Append an entry whenever the house style changes;
`CHANGELOG.md` records *what* the HTML became, this records *why*.

The enforceable form of these rules lives in `~/blog-consistency-check/`
(`checks.py` rules, `audit.py` two-pass checker, `fix.py` repair generator) and in
`templates/post-skeleton.html` here. If a rule below isn't checkable, that's a gap.

---

## Frozen baseline — 2026-08-06

The design was frozen against the fertiliser/fuel-prices post, which was the
cleanest example at the time. Everything below is what a post must satisfy.

### Required elements, in document order

1. `<div class="artx …">` wrapper — every rule is scoped to a post-level class so
   nothing leaks into the Blogger theme.
2. `<style>` block, post-scoped.
3. Google Translate widget (`#google_translate_element` + the two inline scripts).
4. Index backlink to `article-index-start-here`.
5. Hero / stats / body.
6. Sources paragraph.
7. AI-disclosure paragraph, tagged `data-gs-ai-disclosure-v1="1"`, **last, after
   every `</script>`**.

### Colour and contrast

- **Light is the only committed theme.** A `gs-light-lock` block re-asserts the
  post's own `:root` custom properties with `!important`, so a Blogger theme
  switching to dark cannot repaint post text.
- **Deliberately dark panels survive** via `gs-dark-panel-guard`: each dark
  selector re-declares its background `!important`, forces `color:#fff` on itself
  and descendants, and lightens links to `#cfe3ff`.
  - *Rejected:* a blanket light-lock over everything. It whitened panels designed
    to be dark, converting "all text invisible" into "headline invisible" — a
    smaller bug, still a bug.
- **`@media not all and (prefers-color-scheme: dark)` is banned.** It reads like
  "only when not dark" and in fact applies in **light** mode. Four posts shipped
  dark-mode palettes into light rendering this way.
- Contrast is measured on the **rendered** page, not the source. The checker walks
  ancestors for an effective background and **must stop at gradients**
  (`background-image`), which is where the hero colours actually live — an early
  version ignored gradients and reported dark heroes as white-on-white.

### Typography and tables

- `gs-typo-unify-v1`: Georgia / Times New Roman across body, headings, tables,
  lists, blockquotes; `line-height:1.3` on headings (fixes an h1 overlap that hit
  every bulletin-template post).
- **Units belong in the table header, never in the cells.** `₹ crore` goes in the
  `<th>`; cells carry bare numbers. Repeating units per cell was the single most
  common defect (up to 91% of cells in one post).
- Every table sits in an `overflow-x:auto` wrapper. Cells wrap
  (`word-wrap:break-word`); the page body never scrolls sideways.
- Numeric columns right-align; the first column left-aligns.

### Charts and scripts

- Chart JS is inline and self-contained.
- **Never let generated boilerplate splice into a JS string literal.** Seven posts
  had the AI-disclosure `<p>` injected before a `\n</div>';` inside a script,
  producing a SyntaxError and a blank chart. Append after the final `</script>`
  by direct concatenation — *not* at `lastIndexOf('</div>')`, which matches
  literal text inside scripts.
- **Syntax-check scripts in Node, never in the page.** Blogger's CSP blocks
  `unsafe-eval`, so an in-page `new Function()` probe throws on *valid* code and
  reports phantom breakage. `tools/verify_live.py` uses Node.

### Numbers and sourcing

- Official primary sources only (PPAC, DGH, PIB, MoSPI, DPIIT/OEA, NITI ICED,
  PRAAPTI, myScheme). Commercial market-research figures are **question
  generators, not sources** — bottom-up sanity-check before any use, and attribute
  as a commercial estimate with scope unstated if used at all.
- Storage is quoted in **GWh with a duration**, never bare GW.
- Provisional figures carry `(P)`; the label is kept from the source.

### Process

- Verify only by `curl` with a cache-buster. The Blogger editor UI lies in both
  directions — it shows saved content that never persisted, and shows stale
  content that did.
- `setValue()` on the CodeMirror instance does **not** dirty the editor. Focus the
  editor body, then send `space` and `BackSpace` as separate keystrokes.
- Blogger throttles writes after roughly 40 updates in a session. Creating and
  publishing a *new* post still works when updating an existing one silently
  fails.
- **A drafted post keeps holding its slug.** Reverting the old post to draft does
  not free the URL for a replacement; only deleting it does. Same-month
  replacements therefore break the original URL unless the old post is deleted.

---

## 2026-08-06 — semantic versioning for posts

Each post carries a semver number in `meta/<slug>.json` (`version`, plus a
`version_history` list). [semver.org](https://semver.org) is written for APIs, so
the mapping has to be stated explicitly. **A post's public API is what a reader
could act on: its figures and its claims.**

| Level | Meaning | Examples |
|---|---|---|
| **MAJOR** | A figure or a conclusion changed. Someone who acted on the previous version could now be wrong. | A revised WPI series; a corrected import number; a section deleted |
| **MINOR** | Material new content, backward compatible. Nothing previously stated stopped being true. | A new section, table or chart |
| **PATCH** | Nothing the reader relies on moved. | Styling, markup, a design fix, a typo, a reworded sentence, a URL move |

Posts start at **1.0.0**, not 0.1.0 — semver reserves `0.y.z` for "anything MAY
change at any time", and a published post is not that. The 90 posts live when
versioning was introduced were seeded at 1.0.0 with a `baseline` history entry.

`tools/snapshot.py` classifies each bump automatically by comparing the previous
body on disk against the newly fetched one: it strips scripts, styles and tags,
then compares the **multiset of numbers** first (any difference ⇒ MAJOR), then
headings (removed ⇒ MAJOR, added ⇒ MINOR), then prose length. It is a heuristic
and it will be wrong sometimes — `--as major|minor|patch` overrides it. All three
paths were tested against a real post body before this was committed.

**What gets recorded per revision** (following the practice in
`argenius.in/blog-details/blog-versioning-track-post-updates`): version, date,
level, reason, byte delta, any URL change, and any design-marker change. That
article recommends recording the change set and showing freshness to readers but
prescribes no numbering scheme, which is why the numbering comes from semver.

**Reader-facing.** The template now carries a `revision_line` block under the
hero — `Revised <time datetime="…">…</time> · v1.0.0 · what changed` — and an
optional `#changelog` list near the foot. The `<time>` element gives search
engines a machine-readable `dateModified`; the visible line tells a reader the
piece is maintained. `revision_line` is tracked as a design marker, so coverage
is measurable: **0 of 90 posts carry it today**. It applies to new and revised
posts from here rather than being back-filled across the archive by hand — but
all **16 pending fix files** in `~/blog-consistency-check/fixes/` now carry it
(`add_revision_line.py`), so coverage reaches 16/90 as that queue is applied.

Two things that bit while wiring this up, both now guarded in code:

- **The revision line must not feed back into its own classification.** It
  contains a date and a version number, so the classifier read adding it as
  "figures changed" ⇒ MAJOR. `visible_text()` and `headings()` strip the
  `data-gs-revision-v1` paragraph and the `#changelog` block before comparing.
- **Anchor the line on the *first* `</style>`, never the last.** `fix.py` appends
  the light-lock and dark-panel guard as extra `<style>` blocks at the *end* of
  the document, so the last one sits next to the AI disclosure — the line landed
  at the foot of six posts before this was caught. `add_revision_line.py` now
  also refuses any anchor past 50% of the document or within 500 characters of
  the disclosure.

## 2026-08-06 — versioning added

Every published post is now snapshotted into this repo by `tools/snapshot.py`,
with a per-post marker set (light-lock, dark-panel guard, translate widget, index
link, AI disclosure, inverted media query, disclaimer-in-script) recorded in
`meta/*.json`. A design regression that leaves the prose untouched still shows up
as a marker flip in `CHANGELOG.md`.

Reverting a post to an earlier state is `git show <commit>:posts/<slug>.html`
piped back into the editor — see `README.md`.

## 2026-08-06 — the added layers were the bug (measured, not inferred)

Decisive experiment on the worst post (mineral-oil), run in the live DOM:
disable only the CSS layers this project added — the BW-override, the
light-lock, the dark-panel guard — and leave the post's own CSS untouched.

    before  795 / 1403 text nodes below 3:1
    after     0 / 1403

**Every one of the "fixes" was the problem.** The post's original CSS was
internally consistent: it declared dark panels and white text together. Layering
a BW-override (black text everywhere), then a light-lock (light backgrounds,
which redefined the very custom properties the panels referenced), then a guard
(white text on panels whose backgrounds had just been lightened) produced three
mutually contradictory `!important` layers. Each fix was a response to the
previous fix.

**But stripping is not a universal cure.** The same experiment on
`the-grain-value-loop-integrated-rice` gives 20 → 15, not 20 → 0. That post has a
genuine pre-existing defect: its inverted media query redefines `:root` text
tokens to a dark-surface palette (`--text:#e8e8e8`, `--ink-2`, `--ink-3`), and
because an inverted query applies in LIGHT mode those pale tokens land on light
surfaces. Removing the query removes the accident that made it look deliberate.

So there are two populations:

| | posts | cure |
|---|---|---|
| Damaged by the added layers | those carrying light-lock / guard | strip the layers |
| Own palette assumes a dark surface | the 37 carrying an inverted media query | needs a real palette, not a strip |

Layer census across 90 live posts: 58 typo-unify · 37 BW-override · 37 inverted
media query · 12 light-lock · 4 dark-panel guard. 35 posts carry three layers,
5 carry four, 32 carry none.

**Conclusion, and the direction from here:** per-post palettes cannot be
reconciled one post at a time — that is what produced this mess. Colour must be
defined once, centrally, and post bodies must stop declaring it. Structure and
class names stay in the posts; every colour token moves to a single theme
stylesheet. Posts will look uniform afterwards; that is the intended trade.

## 2026-08-07 — the homepage post count is a size budget, not a setting

The homepage renders two posts however high "Max posts shown on main page" is
set (tested at 3 and 5). The cause is Blogger's per-page rendering budget, and
the evidence is the cut point:

| # | post | bytes | cumulative |
|---|---|---:|---:|
| 1 | diesel-doesnt-move-cpi | 27,727 | 27,727 |
| 2 | chemical-import-substitution | 381,972 | **409,699** — last rendered |
| 3 | india-mineral-oil | 99,774 | 509,473 — not rendered |

Blogger populates `data:posts` with full post bodies even when the index
template only reads `data:post.snippet`, so body weight is charged against the
budget whether or not it is displayed. The theme already renders snippets and
carries a comment warning that full bodies here "would exhaust Blogger's page
budget, which silently empties the whole list" — that mechanism is what is
biting, just at snippet level.

**One post causes it.** The chemical HSN-8 registry is 382 KB, roughly 93% of
everything rendered on the index. Until that post is smaller the homepage cannot
list more than two entries.

**Corrected 2026-08-07 after acting on this.** The ~410 KB figure above was one
data point mistaken for a limit. With a second point the threshold is far lower —
see the entry below.

Options, none applied:
- Split the 827-code registry into a short article plus a linked data page.
- Move the full table into a separate page and leave a summary in the post.
- Accept two posts on the index and rely on the topic index widget for browsing.

Do NOT raise the max-posts setting further expecting an effect; it is not the
binding constraint. (Also note the folkloric 1 MB per rendered page figure in
BLOGGER_API_RUNBOOK.md — the observed index cut is well below that, so treat the
budget as smaller than the folklore for index pages.)


## 2026-08-07 — registry split, and the real index threshold

Acted on the entry above. The chemical registry post was 96% table markup:
367,706 of 381,972 bytes, 835 rows in 8 chapter tables, against ~14 KB of prose.

**What was done.** Tables moved to their own post, backdated to 2026-08-05 so it
falls outside the newest-five window the homepage draws from. The article keeps
the analysis and links out to it, and drops 381,972 → 13,748 bytes (3% of
original). Article and data post both verified live; the data post renders all
8 tables and 835 rows.

**A Blogger PAGE will not work for this, and that cost an attempt.** Pages were
the obvious home for a large reference table. The API accepted and *stored* all
375,511 bytes with every row intact — confirmed by reading the page back through
the API — but the rendered page returned 39,784 bytes with zero tables. A post
with the same content renders all 835 rows at 422 KB. **Pages have a much tighter
render budget than posts.** The page was deleted; use a backdated post instead.

**The index threshold is ~100 KB, not ~410 KB.** Two cut points, each inclusive
of the post that crosses:

| | cumulative at cut | posts rendered |
|---|---:|---:|
| before the split | 409,699 (post 2 crossed) | 2 |
| after the split | 141,249 (post 3 crossed) | 3 |

41,475 did not cut; 141,249 did. So the budget lies between those, and Blogger
renders the post that crosses it before stopping. The earlier 410 KB reading was
a single observation treated as a boundary.

**Next blocker is india-mineral-oil at 99,774 bytes** — on its own it takes the
running total past the threshold at position three. Slimming it the same way
(charts and data out to a backdated companion post) should let four or five
posts through. Not done.

Note the rendered homepage is only ~40 KB with a 4 KB Blog widget block, so this
is not an output-size cap — Blogger charges the *source* weight of each post it
must process for the index, whatever the template displays.

## 2026-08-07 — mineral-oil: a date correction, not a split

The homepage now renders **five** posts. Getting the last two took a different
technique from the chemical split, because the post has a different shape.

**Why not the same treatment.** The chemical registry was 96% static table
markup — liftable. `india-mineral-oil` is 78% *script*: a single 76,889-byte
block holding a 59,817-byte data object that populates 47 DOM targets (6 in
sections 1-6, 41 in sections 7-21). Splitting it means operating on live chart
JS, which is exactly the class of change that silently killed a chart earlier
in this project and took several rounds to detect.

**What was done instead.** The post's published date read 2026-08-06 — an
artefact of republishing it to strip the CSS layers, not its real date. Its true
date, **2026-07-30T09:42:00**, was recovered from the original post still
sitting in the blog as a draft. Restoring it is a correction, and it moves the
post out of the newest-five window the homepage draws from. No content changed;
charts verified intact afterwards (4 scripts, 0 broken).

**A Blogger date change does NOT move the post URL.** This mattered: Blogger
URLs embed `/YYYY/MM/`, and `/2026/07/india-mineral-oil-hsn-ch27-trade.html` is
already burned by the draft, so a URL move would have produced another dead
link. Rather than test that on a flagship post, the date change was first run on
the registry data post created an hour earlier — URL unchanged — then that post
was restored and the same change applied. **Test a destructive-looking mechanism
on something disposable first.**

**Snapshot gap closed.** A re-dated post changes neither body hash nor URL, so
`snapshot.py` reported "0 changed" for an edit that reorders the whole blog and
decides what the homepage shows. It now detects and logs re-dates as their own
category, verified with a synthetic manifest edit.

Homepage progression across the two fixes: **2 → 3 → 5**.

## 2026-08-07 — never edit `posts/` in place before publishing

The WPI post gained a whole new section and `snapshot.py` classified it
**PATCH — "visible text identical"**. The classifier was right about what it was
shown; it was shown the wrong thing.

`posts/<slug>.html` is the **previous snapshot**, and the classifier diffs it
against the freshly fetched body. Drafting the new section directly into that
file and then publishing from it means both sides of the diff are the new body:
every change looks like a no-op. The byte delta still moved (12,337 → 16,278)
only because it is read from `meta/`, which is why the run *looked* plausible.

**Rule: draft into `out/`, publish from `out/`, let `snapshot.py` write
`posts/`.** The archive directory is an output, not a workspace. Version
corrected by hand to 1.1.0 (minor — section added).

Worth noting the failure mode: a diff-based check that silently compares
something to itself reports "clean", not "error".

## 2026-08-07 — audit: the in-place edit happened once, and two real bugs behind it

Every snapshot commit was replayed and each changed `posts/*.html` diffed
parent-vs-commit through `snapshot.py`'s own `visible_text()`, then checked
against the level the CHANGELOG recorded. **One post out of 95** was classified
"visible text identical" while its visible text actually moved: the WPI post,
7,788 → 10,650 characters. Every other PATCH with that reason was genuine — the
45-post normalisation really did remove only style blocks.

The obvious detector (posts/ touched outside a snapshot commit) finds nothing
and never would: the in-place edit is committed *by* the snapshot run that
mis-scored it. Replaying the diff is the test that works.

Two bugs the audit exposed:

**1. Sidecars never carried a version.** `meta/<slug>.json` was written in the
middle of the loop, before `version` and `version_history` were attached to the
record. Ninety-five sidecars shipped with no version field while the manifest
held the real one — a hand-edit to a sidecar looked like it worked and changed
nothing. The write now happens at the end of the loop.

**2. `classify()` scored a self-diff as "nothing changed".** It now returns
`None` when the on-disk previous body is byte-identical to the fetched one, with
a reason naming the cause, and an unclassified default is labelled
`UNCLASSIFIED, defaulted to patch: …` instead of silently reading as a routine
1.0.1. A comparison that can't be made must not report "clean".

## 2026-08-07 — the calm in the table is an average of two different decades

The doubling table invites a wrong reading, so the post now says so outright.
Split at April 2020, the fourteen-year averages come apart:

| | 2012–20 | 2020–26 | 14-yr avg | Jun 2026 YoY |
|---|---|---|---|---|
| HSD (diesel) | **−4.72%** | **+17.53%** | 4.25% | +32.57% |
| Fuel & Power | −2.09% | +12.46% | 3.90% | +27.41% |
| All Commodities | 1.63% | 5.84% | 3.42% | +9.87% |
| Food Articles | 4.80% | 4.52% | 4.68% | +5.49% |
| Urea | 1.10% | 0.70% | 0.93% | +1.09% |

Diesel's 4.25% "average" describes neither half — it is one period falling and
another rising, cancelling. Run the rule of 72 on the current pace instead and
diesel doubles in **2.2 years**, not 16.9; three of the eight series double
before 2030. Food and urea are the exceptions: food was never calm, urea still is.

The general rule this is an instance of: **a long-run average across a
structural break is not a description of either side of it.** Both tables now
carry an explicit note on which question each one answers.

## 2026-08-07 — the break audit, and one post whose conclusion it changed

Scanned all 95 posts for long-span rate claims. Most CAGR mentions are vendor
forecasts (already governed by the vendor-estimate rule) or already split by the
author — `securitising-deficit` correctly quotes both a ten-year and a three-year
rupee depreciation rate. One post had the problem in a way that changed a stated
conclusion.

**`hsn-wise-historical-importexport-trends`** ranks 24 HS chapters by eight-year
CAGR. Splitting each series at FY2021-22 shows the ranking is measuring two
different things at once:

- **10 of 24 finished at their eight-year peak.** For these the CAGR means what
  it appears to mean. Electrical machinery exports went $12.7bn → $54.0bn with
  no reversal — a real 22.9% trend.
- **4 are round trips**, ending ≥20% below a mid-window peak. Iron & steel
  exports tripled to $22.9bn in FY2021-22 and gave all of it back: an 0.8%
  eight-year CAGR that is arithmetically correct and informationally empty.
- The post's headline finding — fertilisers as "fastest-growing chapter … likely
  reflecting global fertiliser price shocks since 2022" — was **wrong in its
  attribution**. The series ran flat near $6.7bn for three years, spiked to
  $15.3bn by FY2022-23, collapsed to $8.3bn, then spiked again. Growth was
  +24.2%/yr *before* FY2021-22 and +3.4%/yr after. It is the most volatile
  chapter on the page, not the fastest-growing one. Corrected, and a shape
  section added; the post went to **v2.0.0** (a stated conclusion moved).

The rule now applies twice, so it is worth stating generally: **before quoting a
multi-year rate, split the window and check the two halves agree.** If they do
not, the rate is an artefact of its endpoints. A ranking built on such rates
ranks volatility as if it were growth.

## 2026-08-07 — 54EC bonds: validating someone else's model before publishing on it

New post on reinvesting long-term capital gains. It began from a spreadsheet
model supplied by the user; the engine was reproduced independently in Python
before any of it was written up, and it checked out exactly (₹60.09L / ₹56.96L
terminal values, 9.92% / 8.66% / 7.72% breakevens, ₹64.33L policy scenario).
Reproducing first was the right order — two of the model's own flagged
uncertainties resolved against it:

- **IREDA is notified.** The model listed four issuers and flagged IREDA as
  unverified. PIB release 2143668 (10 Jul 2025, MNRE) confirms CBDT notified
  IREDA bonds as a long-term specified asset effective **9 July 2025**, with a
  renewable-energy end-use condition. Five issuers, not four — and, more
  usefully, the notification power was exercised **twice in 2025** (HUDCO
  1 April, IREDA 9 July), which is the article's central point: widening the set
  needs a notification, not an amendment.
- **The tax-free PSU YTM conflict resolves downward.** Two sources differed by
  ~100bp. Live ISIN-level quotes settle it near the lower band — PFC 8.67% 2033
  at ~5.2%, IRFC 8.63% 2029 at ~5.11%. Using 5.15% instead of the model's 6.0%
  moves tax-free PSU bonds from 4th place to 8th. The model was right to refuse
  to pick a side; the fix was to go and get the primary quote.
- **The SDL row was dropped entirely.** Its only input was a spread estimate with
  no quote behind it. A row that exists only to be caveated should not be in the
  table.

Two figures in the first draft were wrong and caught by recomputation before
publishing: the 5% and 20% slab rows of the breakeven grid. Written from
plausible interpolation, they were out by 40–90bp. **Every number in a table gets
computed, never estimated to look right.**

The article also inherits this session's other lesson: the RBI bond's 8.05% is a
*floating* rate reset half-yearly, and holding it flat for five years is an
assumption. That is said in the text, with a link back to the WPI post.

## 2026-08-08 — the overflow-x:auto wrapper never engaged

The frozen spec says "every table sits in an `overflow-x:auto` wrapper". Every
table did. The scroller had never once activated.

`.tw{overflow-x:auto}` around a `table{width:100%}` does nothing: the table is
told to fit its container, so it never exceeds it, so there is nothing to
scroll. What it does instead is compress. Measured on a 375px phone, Exhibit 1
of the 54EC post crushed six columns into 305px and grew rows to **eight lines
and 170px tall**. The page passed every check the spec asks for — no sideways
body scroll, cells wrapping, wrapper present — and was still unreadable.

**Fix**, tested in the live DOM against two alternatives before being written to
the file:

```css
.bnd table{width:auto;min-width:100%}
.bnd th,.bnd td{white-space:nowrap}
```

`min-width:100%` keeps narrow tables filling the column; `width:auto` lets a wide
one exceed it, which is what finally engages the scroller. `nowrap` puts every
row on one line — 38px, uniform, the way a financial table should read. On the
54EC post: 999 / 441 / 743px tables inside a 305px scroller, page still not
scrolling sideways. A variant keeping the first column wrapping was rejected —
it starved the label column and produced 60px rows for no gain.

This **supersedes the spec's "cells wrap" rule**, which was written to stop the
body scrolling sideways. Nowrap inside a working scroller achieves the same thing
and reads better. Four other posts carry the same dead pattern
(`diesel-doesnt-move-cpi`, `fourteen-years-of-indian-wholesale`,
`indias-oil-fields-are-running-down`, `rooftop-solar-is-working-household`) and
should get the same two lines.

Contrast was clean throughout: 200 text nodes, 0 WCAG failures at both widths.
One near-miss worth recording — 11.52px text on mobile looked like a finding
until the node was identified as the `.eyebrow` label, which is `.72rem` by
design. Body prose is 16.32px. **Read what the selector actually is before
calling it a bug.**

## 2026-08-08 — /2026/07/india-mineral-oil is a 404, and three links pointed at it

The post renders fine at `/2026/08/india-mineral-oil-hsn-ch27-trade.html`. The
`/2026/07/` address returns **HTTP 404** and always will: that slug is burned by
the original, and Blogger never releases a slug.

The trap is that the post's *published date* now reads 30 July 2026 while its URL
still says `/2026/08/`. Restoring the true date does not move the URL — that was
verified deliberately before the date change — so date and address permanently
disagree on this post. Anyone reading the date and constructing the URL from it
lands on a 404. That is exactly what happened here.

Three internal links pointed at the dead address and are now repointed:
`half-of-indias-import-bill-is` (2) and `fuel-pricing-to-crude-cost` (1). A feed
sweep of all 95 posts confirms zero remaining in post content.

**One occurrence remains, in `theme/theme.xml`** — a hardcoded "further reading"
list in an HTML gadget. It is fixed in the repo copy but the theme has no API;
applying it needs the Blogger theme editor.

## 2026-08-08 — the dead URL is fixed with a 301, not a republish

`/2026/07/india-mineral-oil-hsn-ch27-trade.html` now returns **HTTP 301** to
`/2026/08/…`, verified by curl. The post loads at 139,734 bytes with its charts.

None of the obvious repairs would have worked. The slug is burned, so
republishing under it mints a suffix. Deleting whatever holds it does not release
it — that was established the hard way earlier in this project. Changing the
post's date does not move its URL either, which is *why* the date and the address
disagree on this post in the first place.

The fix is **Blogger Settings → Errors and redirects → Custom redirects**, with
Permanent on so it is a 301 rather than a 302. This is the right tool for any
burned-slug situation on this blog and should be the first thing reached for next
time, instead of another republish attempt.

Two UI traps worth writing down:

- **The From/To fields already render a leading `/`.** Typing `/2026/07/…`
  produces `//2026/07/…`, which the summary view shows plainly. Type the path
  **without** the leading slash.
- **The viewport resizes between tool calls** (1416×840 → 1486×812 mid-flow), so
  a coordinate captured from one screenshot can miss by the next. Two attempts
  were silently lost this way — the click landed outside the dialog and dismissed
  it, and the list read "no items" afterwards. **Screenshot immediately before
  every button click in this dialog**, and confirm the outer dialog says
  "1 item" before trusting it. There are two levels: OK commits the rule to the
  list, SAVE commits the list to the blog. Stopping after OK saves nothing.

## 2026-08-08 — table scroller fix rolled out

Applied to the four remaining posts carrying the dead pattern: diesel/CNG,
fourteen-years WPI, oil fields, rooftop solar. All 15 tables confirmed inside a
`.tw` wrapper first — the fix makes tables exceed their container, so an
unwrapped table would have started scrolling the page body instead. Verified live
on the diesel post at 375px: 218 text nodes, 0 contrast failures, every row 38px,
four of five tables scrolling internally, no sideways page scroll.

## 2026-08-08 — theme.xml fix applied in the editor

The stale `/2026/07/` mineral-oil link in the theme's "further reading" gadget is
gone from the live theme. Verified three ways: the editor's own buffer after a
full page reload (0 July, 1 August, 68,153 chars, 5 widgets, the `:has()` rule
and the HTML2-in-main-bottom move both still present), and by curl on three
rendered pages — `fuel-pricing-to-crude-cost`, `half-of-indias-import-bill-is`
and the index — all reporting 0 dead links.

**Method that worked, for next time.** Do not paste the whole file. The live
theme had drifted from the repo copy, so a full-buffer paste would have silently
reverted whatever the drift was. Instead:

1. Read the buffer via `document.querySelector('.CodeMirror').CodeMirror` and
   **count occurrences first** — abort if the target appears more than once.
2. Replace the exact range with `cm.replaceRange(new, from, to)`, not
   `setValue`. `replaceRange` is a real edit; `setValue` does not dirty the
   editor and the save silently does nothing.
3. Belt and braces on the dirty flag: focus the editor and send `space` then
   `BackSpace` as **separate** keystrokes.
4. Re-read the buffer and assert the invariants before saving — length delta,
   widget count, that it still ends `</html>`, and that unrelated `/2026/07/`
   links (there are 25, all legitimate) were untouched.
5. Save, then **verify by curl on the rendered blog**, never by the editor UI.

`theme/theme.xml` in this repo carries the same corrected URL. It differs from
the live buffer by 16 characters — whitespace or entity normalisation applied by
the editor, present before this change and not introduced by it. Recording the
delta rather than pretending the two are byte-identical.

## 2026-08-08 — whole-site link audit

Every `href` in all 96 posts plus the theme: **537 unique links**, checked with a
browser user-agent.

| Class | Count | Result |
|---|---|---|
| Internal (blogspot) | 96 | 2 dead, both in the theme — fixed |
| External | 399 | **391 return 200**, 1 genuinely dead — fixed |
| Relative | 41 | **all dead**, 1 a false positive — 40 fixed |

**The relative links were the real finding.** Forty reader-facing `<a href>`
targets pointing at a local build bundle: `charts/*.html`, `../data/*.json`,
`fdi_pitch/*.pptx|pdf`, and sibling report HTML. On a Blogger post these resolve
against `blogspot.com/2026/xx/` and cannot ever exist. `india-trade-sector-policy`
was the worst — a 26-link contents page where every link was dead.

Handling, deliberately conservative:

- **Repointed 6** where the anchor text and a published post title matched
  unambiguously (e.g. "import-side" → *Priority Trade Partners by Import-Growth
  Sector*, "country-deficit" → *Where India's Forex Goes*).
- **De-linked 39** to `<span class="was-link">`, keeping the visible label.
  Several chart names were *plausibly* mappable — `state_iem_implementation`
  could be either of two IEM posts — and a confidently wrong link is worse than
  no link. Verified after publishing that visible text is byte-identical on all
  six posts and that 0 relative hrefs survive on the rendered pages.

**Two more dead links in the theme**, same gadget as the mineral-oil one:
`/2026/08/chemical-import-substitution-full-hsn-8.html` (the registry's real URL
carries the `_01082878313` suffix Blogger minted) and `https://www.bis.org/statistics/`
(404; `…/statistics/index.htm` works). Both fixed and verified live.

**Not dead, do not "fix":** LinkedIn returns `999` and ScienceDirect and Tomra
return `403` to scripted requests. Tomra was opened in a real browser and loads
fine. A non-200 from a bot-hostile host is not evidence of a broken link.

**The save trap, again — and it bit.** The theme save silently did nothing: the
buffer held 68,174 chars while the server still had 68,153. `replaceRange` alone
does not set Blogger's dirty flag, and neither does a `space`+`BackSpace` pair
that nets to zero — Blogger reads the document as clean again and the Save button
stays inert. What worked: park the cursor at end of document, **type a real
character and delete it**, confirm the undo/save icons have gone active, then
save. **Always confirm by reloading the editor and re-reading the buffer** — the
greyed-out save icon looks identical whether it means "saved" or "nothing to
save".

## 2026-08-08 — the published site has no dependency on this machine

Checked because it matters: **nothing a reader loads comes from this laptop.**

- **Zero** references to `localhost`, `127.0.0.1`, `file://`, dev ports
  (`:8000`, `:5173`, `:8765`, `:8766`) or `/Users/` paths in any post or in the
  theme.
- Every asset host is third-party: Google Translate, `blogger.googleusercontent.com`,
  `resources.blogblog.com`, jsDelivr, cdnjs, Wikimedia, Google Tag Manager.
- All GitHub links — `herrrickshaw.github.io` pages and
  `raw.githubusercontent.com` datasets — resolve **anonymously**, so they are
  public repos, not authenticated pulls.
- The 40 relative links fixed above were the one real vestige of local hosting.
  They were already dead for every visitor; they are now gone.

What *does* depend on this machine is authoring-side only: `snapshot.py`,
`blogger_api.py`, the versioning archive and the push to
`blogger_writeups_code`. If the laptop stops, the blog keeps serving and the
**backup stops updating** — that is the only exposure, and it is a
disaster-recovery concern, not an availability one.

## 2026-08-08 — the archive syncs itself now

The backup of a 96-post blog depended on one laptop being switched on. The blog
itself never did — nothing a reader loads comes from here — but the archive, the
version history and the ability to revert the site all did. Two GitHub Actions
close that.

**`archive-sync.yml`** — daily 02:40 UTC. Runs `snapshot.py` against the
**public** Blogger feed, commits, pushes, then runs `site_health.py`. No
credentials anywhere in it: the feed carries full post bodies, and publishing
still needs OAuth from a workstation. Read-only by construction, which is the
point — a scheduled job that can only read cannot damage the blog.

**`link-audit.yml`** — weekly, plus the fast internal pass on any push touching
`posts/` or `theme/`. Runs `link_audit.py`, keeps **one standing `link-rot`
issue** rather than filing a new one weekly, and closes it when the audit comes
back clean.

Two new tools, both with a bug that would have shipped a false alarm:

- `site_health.py` counted Blogger's stock `post-outer` class. This theme renders
  `<div class='card'>` in **single quotes**, so a perfectly healthy homepage read
  as zero cards.
- A burst of parallel requests drew a 503 on a 415 KB post that served fine on
  retry.

Both were caught by running the tools against the live blog before wiring them
up. **A monitor you have not watched succeed is not a monitor.**

### The mistake worth keeping: "cannot check" is not "broken"

The first CI run reported **83 of 93 posts broken**. Every one was a `429`.
Blogger rate-limits by IP and a shared GitHub runner is throttled far harder than
a home connection — the identical check had passed 93/93 locally minutes before.

The same conflation then bit twice more: once in the post loop, once in the
homepage branch, where a throttled fetch fell through to a generic handler and
printed "homepage unreachable". Three instances of one reasoning error in a
single afternoon.

Throttles now go in their own bucket, are counted as **inconclusive**, and never
fail the run. Pacing was set from measurement rather than taste: at 2 workers and
0.6s the runner still drew 429s on 10 of 25 posts, and a check that comes back
40% inconclusive is not a check. **1 worker, 1.5s apart, the 12 most recent
posts** returns a real verdict in about twenty seconds. The weekly link audit
covers the long tail.

A monitor that cries wolf gets muted, and a muted monitor is worse than none —
it looks like coverage.

### Also fixed: the daily empty commit

`snapshot.py` wrote a CHANGELOG entry and committed on every run, including runs
that found nothing. Left alone, a daily schedule would have added roughly 365
empty commits a year on top of a history whose whole purpose is being readable
enough to revert from. It now returns before touching the changelog when nothing
was added, changed, moved, removed, re-dated or version-bumped; `--allow-empty`
restores the old behaviour.

### Where the checker runs changes its answer

The first full link audit from CI reported **243 of 399 external links dead**.
Zero were 404s: 99 `URLError`, 89× `429`, 55× `403`. The same links returned
**391/399 OK from an Indian connection**. Many Indian government portals —
`cm.karnataka.gov.in`, `dipr.mizoram.gov.in`, `mpinfo.org` — refuse foreign
datacentre IPs outright, and a GitHub runner is exactly that.

An audit whose verdict depends on which continent it runs from is not a signal.
So **only 404 and 410 count as dead**. Everything else non-200 is UNVERIFIABLE
and never fails the run. The final CI run: `DEAD 0 | unverifiable 229` — a large
unverifiable count is expected and fine, because the number that matters is zero.

Final state, both workflows green:

- `archive-sync` — no change → no changelog entry, no commit, nothing pushed;
  homepage 200 with 5 cards; 10/12 posts verified, 2 inconclusive; **healthy**.
- `link-audit` — 494 links, **DEAD 0**, 229 unverifiable.

## 2026-08-08 — extending WPI/CPI abroad, and the comparison that no longer exists

New post. The intended shape — India's WPI beside a dozen peers — turned out to
be impossible, and finding out why became the article's spine.

**India publishes a Wholesale Price Index as its headline producer-side number.
Almost nobody else does.** Most comparable economies moved to a Producer Price
Index decades ago: PPI measures prices producers receive for their own output
and excludes imports, WPI measures goods at the wholesale stage and includes
them. For an economy importing 85%+ of its crude that is most of the gap in any
energy year. Japan's Corporate Goods Price Index was itself called a wholesale
index until 2002.

**Then the data ran out.** Until 2022 the OECD published a harmonised
wholesale/producer family covering members and partners, India included. It was
discontinued, and every mirrored series stops that year — India's wholesale
aggregate at Dec 2022, Japan's at Apr 2022, China's and the euro area's at
Dec 2022. The OECD's current price database is live and extensive and contains
**no producer price data at all**. Verified by querying the dataflow list
directly, not inferred from a failed lookup.

So the producer panel is three economies assembled one statistical office at a
time — India (MoSPI API), US (BLS PPI All Commodities via FRED), euro area
(Eurostat `sts_inpp_a`) — with the instrument differences stated rather than
smoothed. The consumer panel is the OECD's live G20 CPI dataflow, which does
include India and is genuinely harmonised.

Findings worth keeping:

- The producer-minus-consumer wedge **flips sign in the same two years in all
  three economies** — negative pre-2021, sharply positive 2021-22, negative from
  2023. The 2022 Indian wholesale spike was not a domestic policy failure.
- Amplitude differs enormously: India swung 16.2pp between 2022 and 2023, the
  euro area **27.3pp**.
- **India's consumer inflation is now 2.8%** — below the US, Brazil, Mexico,
  South Africa, Japan and Korea. In 2019 it was the highest in the table outside
  Argentina. That reversal is underdiscussed.
- April 2026 wholesale came in at **+8.3%**, with no counterpart in the US or
  euro-area series. For the first time in this comparison India's producer-side
  move looks domestic.

**A vintage discrepancy, stated rather than reconciled.** The MoSPI API returns
**167.0** for April 2026 all-commodities WPI; the OEA index file used in the
earlier wholesale piece gives **167.6** — 0.36%, about a third of a point on the
year-on-year rate. Both official, different vintages of a provisional figure.
The new post uses the API value and says so, and neither post was adjusted to
match the other. Silently picking one would have made the blog internally
consistent and externally wrong.

## 2026-08-08 — adding Japan refuted a claim published four hours earlier

Asked to add China and Japan producer prices from national sources.

**Japan: obtained.** Bank of Japan, Corporate Goods Price Index, Producer Price
Index all-commodities, year-on-year, monthly back to 1980 and updated the morning
it was fetched. The series lives in BoJ's Main Time-series Statistics at
`stat-search.boj.or.jp/ssi/mtshtml/pr01_m_1_en.html` — found by listing the
`mtshtml` prefixes on the index page rather than guessing URLs.

**China: not obtained, and the article says so.** The National Bureau of
Statistics data portal returns `403 Forbidden` to this IP and the main site does
not respond at all. The OECD mirror stops in December 2022 with everything else.
Every remaining route is a commercial redistributor, which this blog does not
cite for a headline figure. So the piece carries an explicit gap rather than a
sourced-to-a-vendor number. China's *consumer* inflation is unaffected — that
comes through the OECD and was already in Exhibit 2.

**The finding that mattered was the refutation.** The version published that
morning ended: *"For the first time in this comparison, India's producer-side
move looks domestic."* Adding Japan, and pulling 2026 monthlies for the others
to check it, showed that claim is simply false:

| 2026 | Jan | Mar | Apr | May | Jun |
|---|---|---|---|---|---|
| US PPI | +2.4 | +6.8 | +9.4 | **+12.3** | +10.1 |
| Japan PPI | — | +2.9 | +5.4 | +6.6 | **+7.1** |
| Euro area PPI | −1.9 | +1.6 | +4.1 | +4.9 | +4.2 |
| India WPI | — | — | **+8.3** | — | — |

The United States accelerated **ten points in four months**, harder and faster
than India. India's +8.3% sits in the middle of the range, not outside it. The
post is now v2.0.0, the revision line states plainly that the earlier claim was
wrong, and the correction is the strongest part of the piece.

The general lesson, which this session has now supplied three times over: **the
claim most worth testing is the one that says a thing is unique.** "For the first
time" and "only in India" are the sentences that fall over when one more column
of data arrives — and the column that refutes them is usually one request away.

## 2026-08-08 — Korea and Brazil, and a second qualification to the same claim

Both obtained from national sources, both with a wrinkle worth recording.

**Korea — Bank of Korea ECOS.** The documented public `sample` key works but
caps at **10 rows per call**, which a 100-month series will not fit. Rather than
page it a dozen times, request annual frequency (10 years = 10 rows) for the
history and two 6-row monthly calls for 2026 and its base year. Series 404Y014,
total index, 2020=100.

**Brazil — IBGE.** Aggregate 6903, *&Iacute;ndice de Pre&ccedil;os ao Produtor*,
general industry, variable 1394 (change on the same month a year earlier). Note
the URL needs percent-encoded brackets — `localidades=N1%5Ball%5D` — or curl
silently writes nothing and the parse fails on a missing file rather than a bad
response.

**Brazil qualified the central claim a second time.** The article said the
2021–22 producer surge was a shared global cycle. For India, the US, Japan,
Korea and the euro area it is. Brazil is not a variation on it:

- **+11.1% in 2020**, the year every other economy here was flat or negative
- **peak +31.6% in 2021** — earliest and roughly double anyone else's
- hardest fall too, −6.2% in 2023

That is the real losing about a quarter of its value against the dollar in 2020,
not the commodity shock, which had not arrived. A producer index in a country
with a collapsing currency and a heavy imported-input bill is partly measuring
the exchange rate. Brazil is also the 2026 laggard, entering the year at −4.4%
and only now crossing positive — the economy that led the last cycle trails this
one.

Korea, by contrast, is India's near-twin in 2026: +1.9% in January to +8.6% in
May against India's +8.3% in April. That makes the corrected claim stronger, not
weaker — the US turned harder and Korea turned identically.

Post now v3.0.0. Verified live: 298 text nodes, 0 contrast failures, three
tables scrolling, no sideways page scroll.

**Twice now, adding data has qualified the headline claim** — first "uniquely
domestic", then "a shared global cycle". Both were true of the countries in the
table at the time and false once the table grew. The pattern is not that the
claims were careless; it is that **a claim about universality is only ever as
strong as the widest sample you have tried**, and the honest move is to name the
sample in the sentence rather than to generalise past it.

## 2026-08-08 — China, reached through the Archive rather than a proxy

The NBS portal returns `403` to this IP and its main site does not respond at
all. Asked for "a proxy or archived NBS release", the archive route is the one
worth taking: an open proxy would give an unverifiable chain of custody for a
headline figure, while the Internet Archive gives **the Bureau's own published
text**, timestamped.

**Method.** The annual *Statistical Communiqué on National Economic and Social
Development* carries the line "the producer prices for industrial products went
down/up by X percent". Wayback's CDX API lists the archived NBS English
press-release pages; the communiqués are the late-February entries. Six years
recovered, 2019–2024:

| 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|
| −0.3 | −1.8 | +8.1 | +4.1 | −3.0 | −2.2 |

Four overlap the OECD mirror and agree exactly, which is the check that makes
the route usable rather than merely available.

**Two honest limits, both in the post.** 2025 is missing — that communiqué would
have appeared in February 2026 and the Archive has no capture; the site went dark
to crawlers at about the point it went dark to us. And China is absent from the
monthly 2026 panel, because monthly releases are not archived at all. An annual
series recovered from archived press releases is a weaker instrument than a live
API and is labelled as such rather than quietly mixed in.

**China is the second exception, opposite in direction to Brazil.** It is the
only economy in the panel with producer prices falling in two consecutive years
(−3.0%, −2.2%) and its 2021 peak was among the mildest at +8.1%. Against consumer
inflation of 0.2 / 0.2 / 0.0 across 2023–25, both ends of the price chain agree:
the one large economy here that never had an inflation problem, and now has the
opposite one. Brazil's deviation is a currency story; China's is a demand story.

Post now v4.0.0, seven economies. The headline claim has been qualified three
times in a day — "uniquely domestic", then "a shared global cycle", now "five out
of seven". Each version was true of its sample. That is the whole lesson.

## 2026-08-08 — the five-year cumulative summary

Year-on-year rates are how prices get reported and a poor way to feel their
weight. Exhibit 3 compounds 2021–25 into the question people actually ask.

| | Producer, 5y | Consumer, 5y |
|---|---|---|
| Brazil | **+48.9%** | +35.7% |
| United States | +33.9% | +21.1%* |
| Euro area | +32.5% | — |
| **India** | **+29.4%** | **+25.2%** |
| Japan | +26.9% | +11.9% |
| Korea | +20.5% | +16.6% |
| China | +6.8%* | **+3.3%** |

\* four years, not five — China's producer figure because the 2025 communiqué is
unavailable, the US consumer figure because the OECD has no 2025 print. Both are
labelled in the exhibit rather than silently averaged in.

Brazil's producer prices rose **seven times** as much as China's over the window.
India sits mid-table on both sides.

**Where index levels existed, endpoints were used instead of compounding rates**
— India 119.2→154.2, Korea 100.00→120.45, US 194.4→260.3, euro area 91.4→121.1.
Compounding rounded annual rates accumulates error; an index has none.

**A claim caught before it shipped.** The draft said India's 4.2-point
producer-consumer gap was "smaller than the United States' or Japan's". Japan's
15.0 is a fair comparison; the US number was not, because its producer side ran
five years and its consumer side four. Recut to a matched 2020–24 window the US
gap is 9.8 points — the conclusion survives, but only because it was checked.
**A gap between two series is only meaningful if both cover the same window**, and
this article had two series that did not.

**And a defect the browser caught that the markup validator could not.** The new
exhibit was numbered 4 but sits third in reading order, so the page ran
1, 2, 4, 3. Balanced tags, valid HTML, wrong document. Renumbered. Worth adding
to the check list: after inserting an exhibit, read the sequence of `.exno`
labels off the rendered page.

Post now v5.0.0. Verified live: 388 text nodes, 0 contrast failures, four tables
scrolling, no sideways page scroll.

## 2026-08-08 — a second post, global-first, and what the supplied links changed

"Push as a new blog" was ambiguous between a **separate Blogger site** and a
**new post here**, and the two are very different: Blogger API v3 cannot create
blogs at all, so a separate site means the UI plus porting the theme, index,
versioning, GitHub sync and audits — every one of which is wired to blogId
2071644453461588122. Asked; the answer was a new post.

The new post is **not a copy**. The India piece is the methodology argument with
an India anchor; *Inflation Trends Globally* leads with the five-year cumulative
spread, carries the full G20 consumer panel including Argentina, and treats the
producer side as the second act. The two cross-link each other in both
directions, and the shared exhibits are labelled to the same sources.

**One supplied link changed a claim in both posts.** Ireland's CSO publishes a
monthly release literally titled *Wholesale Price Index* — which on its face
contradicts "almost nobody else publishes a WPI". Reading the release's table
list settles it the other way: Tables 1–4 are Manufacturing Output Price Indices,
Industrial Producer Price Indices, Capital Goods Price Indices, and a genuinely
wholesale index **confined to building and construction materials**. Germany's
Destatis leads with a *Producer price index for industrial products* and a
separate services PPI, no economy-wide wholesale basket.

So the name survives in a couple of places where the instrument does not, which
is a sharper version of the original point and is now a note in both articles.
**Checking the link that looked like a counter-example produced the best
sentence in the piece.**

Of the seven links supplied, six are official statistical sources (IMF, OECD,
ECB, Destatis, CSO Ireland, FRED). The seventh, S&P Global Market Intelligence,
is a commercial forecaster and is not cited: this blog does not source headline
figures to vendors, per the standing rule.

Both posts verified live: the new one at 376 text nodes / 0 contrast failures,
four tables scrolling, exhibits in order; the companion at v5.1.0. Index now 92
items; internal link audit clean at 97 links, DEAD 0.

## 2026-08-08 — the methodology check that should have come first

Asked to look up cumulative-CPI methodology and the cross-country literature
*after* publishing. It cleared the arithmetic and broke the comparison.

**The arithmetic stands.** Cumulative inflation is the ratio of index endpoints,
not the sum of annual rates; annualising a total needs the geometric mean, not
the arithmetic average. Both were done that way, and index endpoints were
preferred over compounding rounded rates wherever an index existed.

**The comparison did not.** The World Bank maintains a *Global Database of
Inflation* (Ha, Kose & Ohnsorge, PRWP 9737) — up to 209 countries from 1970,
headline/core/food/energy CPI, **producer prices** and deflators, updated twice a
year. It exists for precisely the exercise this article attempted, and it was
missed because the search stopped at "the OECD discontinued its series".

Checking the hand-built producer panel against it:

| | national source | World Bank | gap |
|---|---|---|---|
| Brazil 2019 | +4.6 | +29.2 | **24.6pp** |
| US 2022 | +16.3 | +8.1 | 8.2pp |
| China 2021 | +8.1 | +1.6 | 6.5pp |
| India 2023 | −0.8 | +3.3 | 4.1pp |

Across 36 country-years: median gap 0.8pp, mean 2.7pp, **19 of 36 agree within a
point**. Compounded to four years the US still lands 30.9% against 22.5%.

The causes are all legitimate: "US PPI" can mean All Commodities (used here, and
the most volatile choice) or final demand; Brazil's IBGE industrial IPP is not
the broader producer measure; India's April anchoring is not a calendar average.
Every figure is defensible and they disagree by eight points.

**The honest resolution was to publish the disagreement**, not to swap panels
silently or to bury it in a caveat. The rankings and turning points survive; the
levels are now explicitly "one defensible measurement among several, instrument
named". The World Bank series is recommended for anything turning on the level,
with the note that it stops in 2024 — which is why this article's panel, running
to June 2026, was not simply replaced.

**Two more things the literature gave.** National CPIs are not built to be
compared: the US imputes rental equivalence for owner-occupied housing with a
shelter weight above 30%, the euro area's HICP excludes owner-occupied housing
entirely with a rent weight near 6%. And the synchronisation this article argued
qualitatively is measured — Ha, Kose & Ohnsorge put a common global factor at
about **22% of variation in national inflation since 2001**, which calibrates the
claim nicely: the shared cycle is real and roughly a fifth of the story, which is
exactly why Brazil and China can run their own.

**The lesson, and it is the same one as the uniqueness claims.** The check that
would have most changed this work was a twenty-minute literature search, and it
was run last instead of first. Nothing published was wrong, but the panel would
have been built differently — probably World Bank as the spine with national
sources extending it past 2024. *Look for the canonical dataset before assembling
your own.* Somebody has usually already solved the comparability problem, and
finding out afterwards costs a rewrite.

Post now v2.0.0, five exhibits. Verified live: 458 text nodes, 0 contrast
failures, all tables scrolling, exhibits in order.

## 2026-08-08 — the units rule, stated once and made checkable

The house rule everyone already half-followed, now written in one line and
enforced by a script instead of by memory:

> **A table's units live in its header. The cells carry bare numbers.**
>
> ```html
> <th>Annual imports, US$ bn</th>   <td>14.18</td>     <!-- yes -->
> <th>Annual imports</th>           <td>$14.18bn</td>  <!-- no  -->
> ```

**Why it is worth a script.** A unit repeated down a column is noise in every
row and a transcription risk in each one; it breaks numeric alignment, and it
makes the column impossible to sort or paste into a spreadsheet. It was the most
common defect ever found on this blog — 91% of cells in the worst table.

`tools/units_in_header.py` audits `posts/*.html` and exits 1 on any violation.
Wired into the house-style workflow as **advisory**: it reports and never fails
the run, because the archive still carries a backlog and a check that fails on
every commit is a check nobody reads.

**The rule had to be made conservative to be useful**, and the first version was
not. It fires only when the *same* unit appears in at least half a column's
cells — a one-off "n/a" or a single footnoted value never trips it, and a column
of genuinely mixed units is left alone because it cannot be hoisted. Two further
guards were added after the first run flagged 216 items including prose columns:
skip a column whose median cell is longer than four words, and skip one where
fewer than 80% of cells contain a digit. A "Detail" column mentioning rupees is
not a repeated unit. That took it from **216 findings to 152**, and the ones
removed were all noise.

**Current state: 152 violations across 29 posts, 78 of 332 tables.** Spot-checked
against the HTML before believing it — `a-tax-play` has `<th>DPNG VAT</th>` over
cells reading `5%`, `14.5%`; `chemical-import-substitution-analysis` has
`<th>Annual Imports</th>` over `$14.18bn`. Both real. Worst three posts are
`nature-versus-nurture` (25), `securitising-deficit` (25) and
`state-by-state-who-actually-earns-from` (20).

Fixing them is a separate pass and has not been done — the ask was for the rule.

## 2026-08-08 — the table standard, gs-table-v1

One template for every table on the blog, and a script that applies it.

```css
/*gs-table-v1 — scoped to .post-body */
.post-body table{display:block;overflow-x:auto;max-width:100%;width:max-content;
 min-width:100%;border-collapse:collapse;font-size:.86rem}
.post-body thead th,.post-body tr:first-child th{background:#111;color:#fff;
 font-weight:700;text-align:right;vertical-align:bottom;padding:.6rem .7rem;
 border:1px solid #111;word-break:keep-all;min-width:5.5rem}
.post-body thead th:first-child{text-align:left}
.post-body td{border:1px solid #d9d9d9;padding:.5rem .7rem;text-align:right;
 font-variant-numeric:tabular-nums;white-space:nowrap;color:#111;background:#fff}
.post-body td:first-child{text-align:left;white-space:normal;min-width:8rem}
.post-body tbody tr:nth-child(even) td{background:#fafafa}
```

Dark header band at 18.9:1 contrast, every cell bordered, numerics right-aligned
and tabular, first column left and allowed to wrap, units in the header.

**Two design decisions taken only after a canary post proved the alternative
wrong**, and both would have shipped broken across ninety-eight posts:

1. **Scope to `.post-body`, not `.artx`.** The first version was `.artx`-scoped.
   On the canary the table's wrapper turned out to be `.tblwrap`, the rules
   matched nothing, and the published page had a transparent header and no
   borders — while every local check passed. Every Blogger post body is inside
   `.post-body`; that is the only wrapper you can rely on.
2. **`display:block` on the table, so it is its own scroller.** With `width:auto`
   and no `.tw` wrapper the table pushed the whole page sideways — the canary
   reported `pageScrollsSideways: true`. A block-level table scrolls itself and
   needs no wrapper, which matters because the posts do not agree on wrappers.

**The unit hoist.** `tools/table_standard.py` moves a repeated unit out of a
column and into its `<th>`, and refuses anything it cannot do cleanly:
**73 units hoisted, 61 cells refused**. The refusals are correct and are the
point — `tax on input 10%` is prose in a numeric column, and `$620mn` sitting in
a column headed in billions would need silent rescaling. Both are human calls,
so the script reports them instead of guessing. Compound units are stripped
together (`₹9,743 cr` needs both tokens, one at a time never gets there) and a
trailing `/qtl` is carried into the header as part of the unit.

Guard: the script compares all visible non-table text before and after and
refuses the file if any of it moved.

**Verification on the canary before the batch:** header `rgb(17,17,17)` on white
at **18.9:1**, 1px borders, four tables all self-scrolling, page not scrolling
sideways, and `FY30 Substitution, %` over `-30 to -40` where the cells had read
`-30% to -40%`.

## 2026-08-08 — the last post, and a guarded push

**`top-15-chemicals-for-import--4751284523575450171` is fixed.** It was the one
post the table rollout could not reach, and the cause is the same-slug collision
recorded earlier: two live posts share the slug `top-15-chemicals-for-import`,
so the archive stores one under a `--<id>` filename that matches no live URL and
`find_post()` searches by slug. `blogger_api.py update` now takes `--id` as an
alternative to `--slug`. All 94 posts that have tables now carry `gs-table-v1`;
the index page is the only one without, and it has none.

**`snapshot.py --push` now rebases first.** The scheduled Action snapshots the
same blog on its own timer, and when a local run and a CI run capture the same
state a straight push is rejected — then rebasing conflicts on every
`meta/*.json` at once, seventy files in the first real collision. It now fetches,
counts how far behind the branch upstream is, and pulls with rebase before
pushing. If the rebase conflicts it **aborts cleanly and prints the recovery**
rather than leaving a half-rebased tree:

    git reset --hard origin/<branch> && python3 tools/snapshot.py --push

which re-captures from the feed on top of the remote. That is the right recovery
because both commits describe the same live blog — the conflict is never a
disagreement about content, only about which snapshot recorded it.

**Not fully verified, and worth saying so.** The behind-count is confirmed
correct — with the branch upstream it returns 1 when the remote has moved. But
the rebase branch itself has not run end-to-end: reaching it needs the blog to
have changed *and* the remote to have moved in the same run, and the no-op guard
returns before the push block whenever the blog is unchanged, so the obvious test
cannot get there. I also blamed an unset `origin/HEAD` for the first failed
attempt; that was wrong, `origin/HEAD` resolves fine here. Using the branch
upstream is still the more correct ref, but the real reason that attempt did not
fire is not established. The next genuine collision is the test.

## 2026-08-08 — nature-versus-nurture: 23 unit violations, 17 hoisted, 6 kept

The worst-offending post, done by hand because each column needed a different
answer. **23 → 6**, 62 cells rewritten, non-table text verified byte-identical.

Hoisted: `Revised requirement, MT` · `Domestic output, MT` · three gas-demand
columns to `mmscmd` · `Capacity, LMTPA` · `Total incremental demand, mmscmd` ·
the whole scenario grid to `mmscmd`/`%` · four cost columns to `US$ bn` ·
`Combined incremental demand by 2030, mmscmd`.

**The six left alone are the interesting half**, and each is a reason the rule
needs judgement rather than a regex:

- **`Import growth y/y`** holds `+120%` and `up from 56%`. The first is a growth
  rate, the second is prose about a level. Hoisting the `%` would leave
  "up from 56", which is not a number and not true.
- **`Gas price scenario`** holds `APM ($7/MMBtu)`. The unit sits inside a
  descriptive label, not a numeric column; "APM (7)" reads worse than the
  original. A label is not a measurement.
- **`Domestic output, MT`** still shows `%` — but that is the parenthetical
  change, `19.75 (−3.7%)`, not the column's unit. The MT was hoisted and the
  change stayed, which is right: two different things were in that cell.
- **`Figure`** mixes `7.17 MT` with `89.30 LMT`. Two units in one column, an
  order of magnitude apart. Hoisting either would require silently rescaling the
  other, which is exactly the thing not to do.

**The checker will keep reporting these six, and it should.** A rule that can be
permanently silenced per cell becomes a rule nobody re-examines. Six standing
findings on a 25-table post, each with a recorded reason, is the honest state.

Remaining across the blog: **57 violations in 17 posts**, largest now
`securitising-deficit` at 9.

## 2026-08-08 — securitising-deficit: 9 → 3

Four columns hoisted, 20 cells rewritten: `Break-even INR depreciation, % p.a.`,
`Annual saving, US$ bn`, `PBoC swap line, ¥ bn`, `Annual value, US$ bn`.

**A currency symbol hid behind its entity.** The yen cells read `&yen;190` in the
source, so stripping the literal `¥` removed nothing and the published cells
would have kept their symbol under a header that already carried it. Caught by
reading the rewritten cells rather than trusting the rewrite. **Strip the entity
form as well as the glyph** — `&yen;`, `&#8377;`, `&euro;` — or check the raw
cell, not the rendered one.

Three left, all correct:

- **`Tenor`** runs `91 days`, `364 days`, `4–5 years`. Days and years in one
  column; there is no single unit to hoist.
- **`Then` / `Now`** mix `13% (2019)` with `¥9 tn (2017)` — a share and a volume
  in the same column, which is a table-design question rather than a units one.
  Splitting them would change what the table says, so it is left for a human
  edit rather than done as part of a formatting pass.

Blog-wide: **63 → 57 violations across 16 posts.** Next largest is
`the-grain-value-loop-integrated-rice` at 7.

## 2026-08-08 — the-grain-value-loop: 7 violations, 0 safely fixable, 2 real defects found

The first post in this pass where **nothing could be hoisted**. Every flagged
column mixes units, confirmed by tabulating the unit signature of each cell:

| table | column contents |
|---|---|
| 1 | `₹/qtl` ×3, `₹/MT` ×1, `₹/kg` ×1 — three different denominators |
| 10 | `LMT` ×6, `MT` ×1 |
| 12 | `₹ L cr` ×4, `₹ cr` ×2 |
| 13 | `₹ cr` ×4, plus a bare multiple `3–5×` |

Hoisting any of them would mean rescaling published figures to a common unit,
which is a content change and not a formatting pass. **Nothing was published for
this post.**

**Two of these are readability defects, not just untidy formatting**, and finding
them is worth more than the fix that was not available:

- **Table 10** puts `40.99 MT` in a column of `LMT` values. 40.99 MT is 409.9
  LMT — the largest figure in the column is displayed as the smallest-looking
  number, next to `122 LMT` and `168 LMT`.
- **Table 12** puts `₹18,000 cr` and `₹7,650 cr` in a column whose other entries
  are `₹2.32 L cr` and `₹2.05 L cr`. A lakh crore is 100,000 crore, so
  `₹2.32 L cr` is ₹232,000 cr — again the biggest number reads as the smallest.

Both need the author to pick one unit per column and restate, which is a
one-minute edit but a decision about the source figures, not about CSS. Logged
rather than guessed at.

Blog-wide unchanged at **57 violations across 16 posts**. Next largest:
`annadata-to-urjadata-farmer-income-case` at 6.

## 2026-08-08 — one inversion fixed, one revert: check the prose before restating a unit

Authorised to fix both unit inversions in the grain post. **One was fixed. The
other was reverted mid-edit**, because the fix would have made the table
contradict its own article.

**Table 10 — fixed.** `40.99 MT` sat in a column of LMT values. Verified the
magnitudes against reality before touching it: 520 LMT rice, 168 LMT edible-oil
imports and ~41 Mt oilseed output only reconcile if LMT is lakh tonnes and MT is
million tonnes, so 40.99 Mt = **409.9 LMT**. Restated, and the table — which had
no header row at all — gained `Measure | LMT`. The prose never quotes 40.99, so
nothing else moved.

**Table 12 — reverted.** The plan was to restate `₹2.32 L cr` and `₹18,000 cr`
into one unit. Grepping the prose first killed it: the article says
"₹2.05 L cr", "₹1.68 lakh cr" and "₹7,650 cr" repeatedly, in its own voice.
Converting the column to crore would have printed 205,000 in a table whose
article says ₹2.05 L cr two paragraphs above. Converting the other way gives
`0.0765 L cr` where the prose says ₹7,650 cr. **Either direction introduces an
inconsistency worse than the one being fixed.**

So that column is not a formatting defect at all. The article deliberately uses
lakh crore for state aggregates and crore for specific line items, and the prose
does the same — the unit is in every cell, and a reader who reads rather than
scans is not misled. It stays.

**The rule this adds: before restating a figure's unit, grep the prose for that
figure.** A table does not live alone. This is the same failure mode as the
earlier `.artx` scoping and the self-diff classifier — a change that is locally
correct and globally wrong, and the only way to catch it is to look outside the
thing being changed.

Blog-wide: **57 → 56 violations across 16 posts.**

## 2026-08-08 — annadata-to-urjadata: 6 → 5, and the checker overruled me

I read all six as unhoistable and was about to publish nothing. The classifier
disagreed on one, and it was right.

**Table 5, the FCI-rice-share column.** I had rejected it because the last cell
reads `54–57% — workable at current stocks; 72–91% if stocks revert to 2021–24
levels` — two percentages, and stripping both would strand the second. The fix
is to strip **only the leading one**: the column's value is the figure at the
front, and the trailing qualifier is prose that keeps its own sign. Header now
`vs. ~240–250 lakh MT surplus, %`, cells read `21–22 — comfortable` and
`54–57 — workable at current stocks; 72–91% if stocks revert`.

**Two mixed-by-design columns stay.** Both `Metric | Value` lists: one holds
`₹1,97,000 crore` beside `316 lakh metric tonnes`, the other five `cr L/yr` rows
beside one `~65–75%`. In a key-value list the unit belongs with each value —
that is what the format is for.

**Arithmetic checked while I was in there**, since these tables assert
relationships rather than just reporting: 52 / 79 / 105 / 136 lakh MT against a
240–250 lakh MT surplus give 20.8–21.7%, 31.6–32.9%, 42.0–43.8% and 54.4–56.7%
— every published range correct. And 2,000 − 1,100 − 325 = 575 cr L/yr, with
+400 of FY27 capacity giving 975 against a claimed "~950". All sound.

### What is actually left

Classifying the remaining 42 flagged columns by whether they carry one unit
signature or several: **24 likely hoistable, 18 genuinely mixed.** So the
realistic endpoint of this pass is roughly **18 standing findings, not zero** —
key-value lists and columns that mix magnitudes on purpose. Worth knowing before
anyone tries to drive the number to zero and starts rescaling to get there.

Hoistable work remaining, by post: `indias-textile-import-export-strategy` (5),
`a-tax-play-grow-ethanol-sgst-revenue` (4), then `indias-ev-market-single-digit`,
`nature-versus-nurture` and `raising-green-debt-globally` at 2 each.

Blog-wide: **56 → 55.**

## 2026-08-08 — indias-textile-import-export-strategy: 5 → 3

Two columns hoisted, 10 cells: `Investment, US$ bn` (t6) and
`Investment, ₹ crore` (t7). Both were bare currency figures with a uniform
magnitude, the easiest case there is.

**Totals re-checked after the rewrite**, because both tables carry a TOTAL row
and a hoist that dropped a digit would show up there. t7 is exact —
1,28,509 + 58,918 + 73,518 = 2,60,945. t6's components sum to 31.0 against a
stated 30.9, which is **pre-existing rounding** of five one-decimal figures, not
something this edit introduced. Left as published.

Three left, all correct to leave:

- **`Capacity Add`** reads `+1.2 MMTPA refining + C2/C3 crackers`. The unit sits
  inside a descriptive phrase; hoisting it would leave "+1.2 refining", which is
  not English.
- **`Current Need`** and **`FY30 Addressable`** mix `$3.5B/year` with
  `$800M/year`, and `$2.4B` with `$660M`. Billions beside millions — the same
  shape as the grain post's LMT/MT, though far less dangerous because B and M
  are read correctly at a glance and the unit is in every cell. Normalising
  would mean restating published figures, so it is flagged rather than done.

Blog-wide: **55 → 53 across 15 posts.** Five posts through this pass; 34 units
hoisted in total.

## 2026-08-08 — a-tax-play: 4 → 0, the first post cleared completely

Four `%` columns, 56 cells. Each column was 20-of-21 (or 10-of-11) plain values
like `5%` with **exactly one compound cell** — Uttar Pradesh, which levies a
split rate: `tax on input 10%; tax on sale 12.5%`.

The rule applied was to strip only from cells that are a bare percentage, and to
**leave the compound cell exactly as written**. A header reading `%` tells you
the column's unit; it cannot tell you which of two rates in one cell is which,
so that cell keeps its own signs. The column now scans as bare numbers with a
single self-describing exception, which is what it should look like.

This is the first post in the pass to reach **zero** — but only on the second
attempt, and the first attempt is the lesson.

**Never `str.replace()` a table cell value that is not unique in the document.**
The first pass walked the rows and called `new.replace(f'>{raw}<', bare, 1)` for
each. `>5%<` occurs dozens of times in a table of state VAT rates, so every call
hit the *earliest remaining* match rather than the cell being iterated. The right
number of replacements happened; four landed on the wrong cells, and four bare
`5%` and `4%` values survived in a column whose header now claimed `%`.

It was caught by a residual check on the **published** page — grepping the live
HTML for `>[\d.]+%</td>` inside the columns that had just been cleaned. Without
that check the post would have shipped looking finished.

The fix was to stop replacing and start rebuilding: parse each `<tr>`, walk its
cells by index, and reassemble the row. Positional identity, not string
identity. That pattern should be the default for every table edit in this repo —
`table_standard.py` has the same weakness and should be moved over to it.

Blog-wide: **53 → 49 across 14 posts.** Six posts done, 90 units hoisted.

## 2026-08-08 — the last two posts, and a third encoding trap

`indias-ev-market-single-digit` **2 → 0** (12 cells) and
`raising-green-debt-globally-rec-euroyen` **2 → 0** (6 cells). Both clear.

`nature-versus-nurture` was on the list at 2 but had nothing to do — the
classifier counted its `Gas price scenario` label column, already judged
unhoistable because the unit sits inside `APM ($7/MMBtu)`.

**Three encoding traps in one pass, all the same shape.** A cell that renders as
one character is stored as another:

| renders as | stored as | where it bit |
|---|---|---|
| `¥190` | `&yen;190` | securitising-deficit |
| `−14.7%` | `&minus;14.7%` | raising-green-debt |
| `4%` | `<b>4%</b>` | indias-ev, markup-wrapped |

Every one produced a silent no-op — the script reported success and changed
nothing. **Match against the raw cell, allowing entity and markup forms, and
verify by re-reading the rewritten value.** The count of cells changed is not
evidence; only the resulting text is.

The green-debt table also carried its own precedent: its JPY column already read
`🇯🇵 JPY, %` with bare cells while USD and EUR still had signs in every row. The
fix was to make the other two match what was already there.

### Pass complete

Eight posts worked through. **80 → 49 violations**, 108 cells rewritten,
three posts cleared to zero. The remaining 49 sit in 30 tables across 14 posts
and are, on the earlier classification, mostly the ~18 genuinely mixed columns —
key-value lists, deliberate magnitude mixes, and units inside descriptive labels.
Driving that to zero would mean rescaling published figures, which is the one
thing this pass consistently refused to do.

## 2026-08-08 — petroleum dashboard published, and a dark-theme trap re-run

New post from `petroleum_trade_pairings_dashboard.html` — 23,000 words, 9 tables,
8 inline SVGs, **no JavaScript**, sources Comtrade / EIA / DGCI&S TRADESTAT.
Wrapped in the house shell, one unit column hoisted (`Named destinations, %`),
and published.

**It went out with 89 contrast failures and I had to fix it live.** The dashboard
is a **dark** design — surfaces at `rgb(30,27,22)` — and every house element I
bolted on (revision line `#595959`, disclaimer `#555`, index link `#0b5394`) is
styled for the blog's light theme. Dark-on-dark at 2.4–2.7:1. This is precisely
the bug the light-lock work eliminated across the archive, reintroduced by
importing a dark artefact and not checking the surface it landed on.

**Check the background before styling the foreground.** The source file even
declared `--bg:#FBF8F…` near the top, which is what I glanced at; the dark
values win further down. A declared variable is not the computed surface.

Fixed by raising `--ink-3` from `#8A7F70` (4.37:1, just under AA) to `#C2B6A2`
and recolouring the house elements for a dark surface. **0 failures across 1,412
nodes**, 8 SVGs rendering, no sideways scroll.

**My measuring function was also wrong**, and it inflated the count. It returned
the first non-transparent background it found without compositing alpha, so
`rgba(79,125,74,0.16)` over near-black was scored as if it were pale green —
several "failures" in the 89 and 59 counts were artifacts. The corrected version
composites the stack down to an opaque colour. **A contrast checker that does not
composite alpha will invent failures on any translucent chip.**

## 2026-08-08 — LNG status report, European-import focus

New post built from two sources: ACER's *Analysis of the European LNG market
developments* (13 May 2026, 46pp, extracted locally) and the IGU *World LNG
Report 2026* (7 July 2026).

**The two sources were reconciled before anything was written**, because they
report in different units — IGU in million tonnes of LNG, ACER in billion cubic
metres of gas. At 1 Mt ≈ 1.36 bcm:

| check | IGU | ACER | verdict |
|---|---|---|---|
| 2025 growth | +6.3% of 437 MT = 37 bcm | +35 bcm | agrees |
| 2025 FIDs | 68.4 Mtpa = 93 bcm | 90 bcm | agrees |
| EU total | — | 84 bcm at 58% ⇒ 145 bcm vs 146 stated | internally closes |

Three independent checks, all within rounding. The conversion is stated in the
article rather than applied silently to either source's figures, and Exhibit 2
deliberately keeps both units side by side with the source named per row — which
is why the units checker still flags that column, correctly.

**The finding.** The EU imported a record 146 bcm in 2025 and passed China and
Japan to become the largest LNG importer. 84 bcm of it — **58%** — came from the
United States, which is 25% of all EU gas consumption. The 2022 problem was one
dominant supplier by pipeline; the 2025 position is one dominant supplier by sea.
And the Russian phase-out at end-2026 raises the US share by construction: taking
a supplier out of a concentrated portfolio concentrates it further.

The Hormuz fork is the sharpest number: ACER's two 2026 scenarios are **47 bcm
apart**, about a third of the EU's annual intake, on whether the Strait reopens
by 1 July.

Verified live: 179 text nodes, **0 contrast failures**, three tables scrolling,
no sideways scroll, `gs-table-v1` applied.

**One process note.** The article was first published without `gs-table-v1`
because it was built from the older per-post CSS template rather than the
standard. Caught by grepping the published page for the marker. When the standard
lives in a script, hand-built posts miss it — the marker check belongs in the
pre-publish routine, not just in `table_standard.py`.

## 2026-08-08 — LNG post v1.1.0: the primary document changed two definitions

Re-sourced from the full 88-page IGU report instead of its press release. The
headline numbers held, but the report surfaced two definitional traps the press
summary had hidden — both now stated in the article.

**"Largest importer" depends on the unit of comparison.** ACER says the EU
overtook China and Japan. The IGU report says *China remained the world's largest
LNG importer in 2025*, at about 69 Mt. Both are right: ACER ranks the EU as a
27-country bloc, the IGU ranks countries. The EU's 146 bcm is ~107 Mt, above
China as a bloc and not comparable as a country. Published side by side without
explanation, the two look like one of them is wrong.

**"Europe" is not "the EU".** The IGU puts Europe's 2025 imports at about
**126 Mt** against the ~107 Mt implied by ACER for the EU. The ~19 Mt gap is the
UK, Türkiye and other non-EU importers — geography, not a data dispute. The
article now uses ACER's EU figures for EU policy and says "Europe" only where the
wider geography is meant.

**The lesson is the cheap one.** A press release gives you the numbers; the
report gives you what they mean. Both traps were invisible in the summary and
obvious in the source, and neither would have been caught by cross-checking
arithmetic — the arithmetic was fine all along.

## 2026-08-08 — LNG v2.0.0: the India angle and a source-coverage map

**The India finding is a division.** IGU gives India 24.60 Mt of imports in 2025,
**down 1.5 Mt**, against **52.5 Mtpa of regas capacity across eight terminals** —
**47% utilisation**. And India *added* 7.1 Mtpa during that year, commissioning
Chhara and expanding Dabhol after its breakwater was finally finished. On the
prior 45.4 Mtpa base, 2024 utilisation was ~57%. India built a tenth more
capacity into a year it bought less gas and pushed utilisation down ten points,
with a further Dahej expansion under construction.

Europe and South Asia are the two sides of the same 2025 trade: when the EU is
refilling empty storage at any price, the price-sensitive buyer steps back.
India and Pakistan were the only Asian importers to shrink.

**Exhibit 5 maps who publishes what**, because assembling an Indian LNG picture
means working across three bodies whose coverage barely overlaps:

- **IGU** names the eight terminals with capacities and 2025 changes, but
  publishes no price.
- **PPAC** publishes national volumes, values and prices, but nothing
  terminal-level.
- **PNGRB** authorises terminals, pipelines and CGD areas and sets tariffs, but
  publishes neither imports nor prices.

**The gap in the middle is real and is stated as a finding:** nobody publishes
terminal-level throughput against terminal-level capacity, which is exactly the
number that would show whether 47% national utilisation is spread evenly or
concentrated in a few idle assets.

**One thing not retrieved, and labelled as such in the article.** The PPAC LNG
import price series was not obtained — PPAC's flash report carries petroleum
products only and the LNG series sits in a separate report this pass did not
reach. The price rows in Exhibit 5 therefore describe *what PPAC publishes*, not
figures reproduced here. An empty cell honestly labelled beats a plausible number
from somewhere else.

## 2026-08-08 — LNG v3.0.0: a published claim withdrawn, and a vendor figure rejected

**v2.0.0 said "nobody publishes terminal-level throughput against terminal-level
capacity". PNGRB does.** It sits in section 4.2 of *India's Evolving Natural Gas
Landscape — NG Demand Projections for 2030 and 2040*, on the board's
knowledge-sharing page, attributed to PPAC. The claim is withdrawn in the
revision line rather than quietly edited out, because it was the closing line of
the section and a reader who acted on it was misled.

**The data changes the reading of the article's own headline number.** National
utilisation of 47% is an average across a system where **Dahej runs at 95%** and
has averaged 98% for eight years, while the six other terminals with a reported
figure hold 30.2 Mtpa and moved 7.8 Mt — **26%**. Worse, the mid-tier is
deteriorating: Hazira 67%→30%, Dabhol 58%→43%, Mundra 25%→15%. Kochi and Ennore
rose, from 13% and 12%. This is the average-hiding-a-break problem again, in a
number I had already published.

**The counter-case is included because PNGRB makes it in the same document** —
demand to ~200 MMSCMD by 2030, imports more than doubling, capacity takes years.
Its weak points are also PNGRB's own: affordability against an APM price capped
at US$6.50/MMBtu, and terminals not integrated with demand centres. Presenting
only the overbuild reading would have been the easier and worse article.

**One drafting correction caught before publishing.** I had written that the
underused terminals are "furthest from cheap domestic supply" — a mechanism I
invented. PNGRB points at evacuation and demand-centre integration, i.e. missing
pipelines. Replaced with what the source actually says.

**Vendor check (seala.ai).** Asked to evaluate a commercial LNG-statistics site.
It gives EU-plus-UK 2025 imports as **359 Mt**. Global LNG trade in 2025 was
**437 Mt**; Europe's share was **126.2 Mt**. The figure is 82% of every cargo
shipped anywhere on earth. Source undisclosed, product paid. Not used — and the
check is now *in* the article, because "no commercial vendors" reads as
fastidiousness until you show what one division turns up.

**Rule reinforced:** before writing that a figure is unpublished, check the
regulator's non-statistical output. Studies, conclave booklets and projection
reports carry data that never appears in a statistics release.

## 2026-08-08 — Author photo replaces the "UT" monogram, site-wide

**Three places rendered the monogram, and only one of them was a post.** The
about-author page (88px), the article index (72px) and — the one that matters —
the **Contact Us card in `theme.xml` (56px), which renders on every single page**.
Grepping `>UT<` found all three; a per-post pass would have missed the theme and
left the monogram on 90-odd pages.

**Source image.** The professional headshot was not on disk — only the passport
photo was. Found the original in Drive at 1004x1339, cropped to a full-width
square anchored at the top (face lands at ~40% height, which is where a circular
avatar wants it), resized to 200px for 88px @2x. 10.5 KB JPEG, 14 KB as a data
URI. Master kept at `assets/author-avatar-200.jpg`.

**Data URI, not a hosted file.** Blogger's API cannot upload images and the
archive has no public host. Inlining keeps every page self-contained, which is
this archive's whole premise. Cost is 14 KB per page load, uncached, against
70-140 KB pages.

**The theme edit, which is the part that goes wrong.** Blogger has no theme API.
Two routes: Backup/Restore (replaces the *whole* theme — destructive if the
archived copy has drifted) or a targeted edit in the HTML editor. Took the
targeted route after confirming no drift: **live theme 68,174 chars against the
archive's 68,190** — a 16-character difference, so nothing had been changed
outside the archive.

Pasting 14 KB into CodeMirror is the failure-prone step. Instead: served the JPEG
from a **local HTTP server with `Access-Control-Allow-Origin: *`**, had the page
`fetch()` it and build the data URI in-page, then `cm.replaceRange()` at an index
computed from the live text. Confirmed the recipe from the earlier session still
holds — **a programmatic CodeMirror edit does not set Blogger's dirty flag**, so
the save is a silent no-op unless you follow it with a real keystroke. Typed `x`,
pressed Backspace, verified the buffer was byte-identical to the intended text
and carried no stray character, then saved.

**Verified on the live site, never in the editor.** Homepage: zero `>UT</div>`,
exactly one data-URI image, 56x56, complete, correct alt text.

**One pre-existing bug fixed in passing.** The index page's author blurb rendered
`India’s` literally — a JSON escape that had been written straight into HTML.

**Not touched:** `theme-html2-moved.xml` and `theme-dedup-h1.xml` still carry the
monogram. They are historical snapshots, not live templates, and editing them
would falsify the record.

## 2026-08-08 — JSON-LD structured data, site-wide via the theme

**One `@graph` per page**: `WebSite` + `Person` + `WebPage` everywhere, plus
`BlogPosting` on post pages only, cross-referenced by `@id` rather than repeated.

**The JSON is built in JavaScript from `data-*` attributes, not printed into the
script body.** Blogger escapes an attribute value as XML; `JSON.stringify`
escapes it as JSON. A template string would emit invalid JSON the first time a
post title contained a double quote, and it would fail silently: the page still
renders, the rich result just never appears.

**Three things went wrong, all caught before they shipped.**

1. **`--` is illegal inside an XML comment.** The first patch broke the theme
   parse. Caught locally by `ET.parse()` before it went anywhere near Blogger.

2. **I patched a dead includable.** The theme has `<b:includable id='post'>`,
   which looks like the post renderer and is not — it is leftover Blogger
   boilerplate. This theme renders posts inside the Blog widget's own `main`
   includable, in the `pageType == "item"` branch. The give-away: the live page
   had no `.post.hentry` wrapper at all, and `.post-body` was a direct child of
   `#Blog1`. Result: `WebSite`/`Person`/`WebPage` appeared, `BlogPosting` did
   not. **Grepping the theme for a plausible-looking hook is not evidence that
   the hook runs. Check the rendered DOM.**

3. **The save silently no-opped, again, and for a new reason.** The dirty-flag
   trick worked (the browser blocked navigation with "unsaved changes"), but the
   Save click at a remembered coordinate missed: the viewport had resized from
   1416x840 to 1200x656 between calls. Resolving the button by element ref hit
   it and returned "Update successful". **Never click Blogger's toolbar by
   remembered coordinates. Resolve the element.**

**Description had to be sourced deliberately.** Blogger emits no meta
description on these pages, and its auto-generated `og:description` is the top
of the raw post body, which here is the index link and the eyebrow line: pure
chrome. The chain is now meta description, then the hand-written `.standfirst`,
then `og:` as a last resort. `dateModified` comes from the post's own revision
`<time>` where one exists and is omitted where it does not, rather than invented.

**Existing BlogPosting microdata on the post wrapper is left alone.** Google
reads either, they agree, and removing it is a bigger change than this needed.

**Verified on live pages, in a browser that executes the script**: post pages
emit all four types with the right headline, dates and `@id` links; the homepage
emits three and no `BlogPosting`, which is the point of the branch guard.

## 2026-08-08 — The publish-date bug that was not there

**I flagged a data-loss bug that does not exist, and the correction matters more
than the flag did.** I saw the LNG post's `datePublished` come back as today's
date in the new JSON-LD and inferred that API updates were resetting publish
dates. Checked before acting:

- **Zero of 97 live posts** have a `published` value differing from the earliest
  one recorded anywhere in the archive's history.
- The LNG post specifically: `published` sat at **2026-08-08T10:31:50** across
  **all six snapshots taken today**, while `updated` moved four times. It reads
  as today's date because it *was* published today.
- `snapshot.py` has detected and reported re-dating since it was written. Across
  **104 commits it has never once fired.**

So the dates were never lost. Had I "restored" them from a guess, I would have
falsified the publication history of a blog whose whole argument is that it
checks its numbers.

**The latent risk was real even though the damage was not.** `posts.update` is a
PUT — a whole-resource replace — and `do_update` was sending only
`{id, title, content}`. Blogger has preserved `published` on every write so far,
but that is Blogger's choice, not ours. It now sends the existing date back
explicitly, so the guarantee is ours.

**Adding the parameter immediately broke both call sites**, which were passing
`dry_run` positionally straight into the new `published` slot — a dry run would
have become a live write with a garbage date. Both now use keywords. This is the
argument for keyword-only parameters on anything that writes.

**Verified by round-trip, not by reading the code**: fetched about-author
(published 2026-08-05T10:43:35), wrote its own body back, re-fetched. `published`
unchanged, `updated` moved to 11:40. That is the behaviour we want and now
explicitly ask for.

**Recrawl.** Nothing to fix: `sitemap.xml` lists all 97 posts with `lastmod`, and
robots.txt declares it. Every entry carries a fresh `lastmod`, which is the
signal Google actually uses. There is no API route for requesting reindexing of
articles — the Indexing API is restricted to JobPosting and BroadcastEvent — so
the remaining step is Search Console, by hand, and it is the owner's to take.

## 2026-08-08 — Discoverability: descriptions, titles, labels, robots

Four changes from the keyword analysis, all verified live.

**1. Per-page descriptions.** No page on the site had a meta description; Google
was writing snippets from the top of the body, which on this blog is the index
link and the eyebrow line. Blogger's `customMetaData` field is **not settable
through the API** — it accepts the write and returns null — so per-post search
descriptions cannot be scripted. Route taken instead: enable Blogger's search
description feature, set a blog-level default so social shares are never blank,
and have the existing structured-data script override `description` and
`og:description` per page from the post's own standfirst. Google renders JS;
social scrapers do not, which is why the blog-level tag stays in the markup as
the floor rather than being removed.

**2. Titles.** Every `<title>` was `Thinking global, living local: <post>` —
31 characters of blog name before the subject, against Google's ~55-60 character
display. Post pages now emit `data:blog.pageName` alone. The LNG post went from
109 characters to 78.

**3. Labels: 0 of 99 posts had one.** 80 posts now carry 1-3 of thirteen topic
labels, assigned from H1/H2/H3 text only — body text is useless for this because
one boilerplate sentence appears 2,648 times across four HSN-registry posts and
swamps every count. 17 posts are deliberately unlabelled: no cluster fits.
Utility pages (About, Index) are excluded by an explicit override, because
"About the Author" otherwise scores Industrial Policy on "investment promotion"
in the job title and lands in a topic hub next to actual analysis.

**Labels alone would have been invisible.** The theme's label-rendering markup
sits in the boilerplate `post` includable — the same dead code that swallowed the
first JSON-LD attempt. Topic links now render in the live path.

**4. robots.txt** narrowed from `Disallow: /search` to `Disallow: /search?`, so
the new label hubs are crawlable while query-search pages stay out. This was only
worth doing *because* the posts now link to those hubs; blocked-but-linked pages
produce "indexed, though blocked" warnings.

**Three failures worth recording.**

- **Blogger rejected a theme save with `SAXParseException: The element type
  "div" must be terminated`** and I nearly missed it — the toast is the only
  signal, and I had been checking the live page instead. The cause: I extracted
  the fragment by searching for `"          </b:loop>"` (10 spaces), which
  matched *inside* the 16-space-indented inner loop and truncated the block
  before its own closing tags. **Anchor on a full closing sequence, and assert
  tag balance on the fragment before sending it.**
- **A programmatic `textarea.value` set does not register with Blogger's
  settings form** — the same failure mode as CodeMirror's `setValue`. It saved an
  empty robots.txt, briefly losing the sitemap declaration. Then typing on top of
  the ghost value produced 329 characters of doubled content. Select-all, delete,
  type.
- **A save can look identical whether it succeeded or failed.** The reliable
  test is to attempt navigation: Blogger blocks it with "unsaved changes" when
  the buffer is dirty. That distinguishes "save failed" from "page is cached",
  which cost two wrong diagnoses today.

## 2026-08-08 — Fuel surplus and the neighbourhood: the brief did not survive the data

Asked for a piece on India's petrol/diesel surplus and the opportunity to sell to
Nepal, Sri Lanka and Bhutan along with ethanol. Two of those three premises hold.
One inverts.

**The surplus is real and large.** DGCI&S TRADESTAT, HS 2710: exports
**US$52,973mn** against imports **US$9,320mn** in FY2025-26 — a net
**US$43.7bn**. Diesel-led: the 271019 group alone exported US$34.6bn.

**The neighbourhood is 5.2%, and two of the three markets are already closed.**
Nepal 1,522, Sri Lanka 1,013, Bhutan 240 US$mn — 2,775 combined. And PPAC's own
footnote settles what kind of market these are: *"Nepal sales by IOCL, Nepal and
Bhutan sales by BPCL are considered in total exports"*. Indian PSUs are not
competing for Nepal and Bhutan, they are the incumbent supplier, booking
subsidiary sales as exports. **Nepal's purchases fell 5.3% last year.** The one
genuine growth market is Sri Lanka, +30.3% — and it is the only one that sells
refined product back, i.e. the only competitive one.

**The largest buyer is the Netherlands at US$8.4bn, 15.9%** — Rotterdam, and the
diesel end of the Russia-crude-to-Europe trade. The neighbourhood does not appear
until well down the list.

**Ethanol inverts the brief, and then the user's own source made it sharper.**
TRADESTAT: exports **US$54.3mn**, imports **US$407.2mn** (94% from the US) — a
net deficit of **US$353mn**. Exports to Nepal: US$0.09mn. On the trade measure,
India buys alcohol.

The user then supplied CareEdge Ratings (May 2026): capacity past 20 bn litres,
+4 bn coming, E20 absorbing 11 bn, non-fuel 3–3.5 bn, distilleries at ~60%.
**Not a contradiction — a different quantity.** CareEdge measures idle *capacity*;
TRADESTAT measures *traded product*. India has unused distilleries and an alcohol
import bill simultaneously. Idle plant is not a stock of exportable litres.

**Two checks worth recording.** The press figure of "nearly 7 billion litres" of
surplus does not reconcile with CareEdge's own components: 20 − (11 + 3–3.5)
gives **5.5–6 bn** now, ~9.5 bn once new capacity lands. Published the components
and the discrepancy rather than the headline number. Separately, **WebFetch
mis-converted crore to billion by a factor of ten** ("2,000 crore litres (200
billion litres)"); 2,000 crore is 20 billion. A summarising model is not a unit
converter — check every crore/lakh conversion it hands back.

**The pattern this joins.** LNG regas terminals at 47% utilisation, distilleries
at ~60%, both adding capacity, both proposing exports as the remedy for the
shortfall. Named it in the article.

**Sourcing.** CareEdge is a commercial ratings agency, so its figures are
attributed as industry context and carry no headline claim — same treatment as
S&P Global in the inflation piece. Every load-bearing number is DGCI&S or PPAC.

**Also stated plainly: TRADESTAT returned no quantity columns**, so the entire
article is in dollars. A 15.3% fall in export value is not a 15.3% fall in
barrels when crude prices have moved, and the piece says so rather than implying
volume.

## 2026-08-08 — Index rebuilt: by topic, by geography, by connection

Replaced the hand-maintained ten-section index with three generated views, built
by `tools/index_graph.py` (extraction) and `tools/build_index_page.py` (page).
Regenerating is now two commands, so the index stops drifting from the archive.

**By topic** is now twelve links to the Blogger label hubs rather than a
hardcoded list of posts. The hubs update themselves as pieces are labelled;
the old sections had to be hand-edited and were already stale.

**By geography** required a decision. Almost every post is about India, so India
is not a category — it would hold all 96 and say nothing. The page indexes the
*second* geography instead: the counterpart economy a trade piece measures
against, or the Indian state whose policy is examined. **25 countries** and
**20 states**. China leads at 16 posts, then the US and Germany at 6 each;
Gujarat leads the states at 11.

**Extraction had to resist the tables.** Four HSN-registry posts repeat one
sentence 2,648 times, so any raw term frequency is table furniture. Headings are
weighted four times body text, body counts are capped per post, and a place has
to clear a floor before it counts as a subject — every trade post mentions China
somewhere, few are about China.

**By connection** is a static inline SVG of subject co-occurrence: 17 subjects
appearing in five or more posts, 57 edges where two share at least two posts,
node size by post count. Deterministic circular layout, no JavaScript and no
external library — a force-directed layout would look better and land differently
on every rebuild, which makes a data change indistinguishable from jitter. Each
of the 96 entries also carries up to three related pieces, ranked by shared
subjects weighted inversely by how common the subject is, so "rare earths"
links harder than "GST".

**Verification note worth keeping.** The browser pane was collapsed to zero
width, and `getBoundingClientRect()` in a zero-width viewport reported every SVG
label as overflowing. That is a measurement artefact, not a layout bug. Checked
the geometry arithmetically instead — label extents run 85 to 783 inside a
920-wide viewBox — which needs no browser and cannot lie about a hidden pane.
**A measurement taken through a broken instrument is not evidence.**

Live: 96 post links all resolving to live posts, 12 hub links, 17 graph nodes.

## 2026-08-08 — The "duplicate" chemical posts were not duplicates

The keyword analysis flagged four posts competing for one query. Read all four
before touching anything, and the diagnosis was wrong in an instructive way.

**They are four different documents.** `hsn-8-registry` (5.5k chars, 0 tables) is
the methodology page — the signal framework, four categories with counts, and an
explicit list of what the analysis cannot do; its tables were deliberately moved
out in v3.0.0 to keep the page under Blogger's budget.
`full-hsn-8_01082878313` (185k chars, 8 tables) is where they went. The two
`top-15` posts are a code-by-code detail piece and an FY26-30 roadmap summary,
sharing a slug across two month paths.

**So the defect was never duplication. It was that each pair opened with the same
words** — "Chemical Import Substitution — Full HSN-8 Registry (827 Codes)" twice,
"Top 15 Chemicals for Import Substitution" twice — which is what makes them
compete in search and indistinguishable in a list. Consolidating or 301-ing would
have destroyed working pages to fix a naming problem.

**Retitled to lead with the differentiator. Nothing deleted, no URL changed.**

**Both the Blogger title and the in-body `<h1>` had to change.** The theme hides
its own h1 when the body supplies one, so changing only the API title would have
left every page heading disagreeing with its own search result.

**Two failures of assumption, both caught by refusing to guess.** The h1 anchors
did not match on three of four posts because the live markup carries `&#8212;`
rather than a literal em dash, and one h1 had newlines inside it. The script
counted occurrences and skipped rather than doing a fuzzy match — then I read the
raw markup and used it verbatim. Second: my verification regex initially caught
an `<h1>` inside a *theme comment* and reported all four as mismatched. Stripping
comments and scoping to `.post-body` showed all four correct. **Two verification
bugs in one task, both of which would have reported failure on a working change.**

## 2026-08-08 — South Africa: the brief inverted twice

Asked to analyse India's opportunity to export petrol, diesel and biofuels to
South Africa. The data turned the piece around, then a source the user re-sent
turned it around again.

**First inversion: India is losing this market, not entering it.** TRADESTAT HS
2710 to South Africa fell from **US$2,793m to US$1,882m — 32.6%** in FY2025-26,
against a 15.3% fall in India's total refined exports. South Africa is India's
9th-largest fuel market and shrinking twice as fast as the average.

**Second inversion, from the Reuters piece.** South Africa's Gulf supply — Oman,
Saudi Arabia, UAE — was cut off when Hormuz closed, and the replacement cargoes
were **American**: four tankers, ~165,000 t at Durban in April 2026, roughly
double January's US arrivals. **India is ~6,000 nautical miles closer than the US
Gulf Coast, and the buyer's stated complaint was freight and premiums.** The
supplier that gained was the furthest away.

**The timing had to be handled carefully and nearly was not.** TRADESTAT's
FY2025-26 ends March 2026; the disruption is April 2026. The 32.6% fall therefore
happened *before* the crisis, and the US surge *after*. Two adjacent periods, not
one story — stated explicitly rather than blurred into a single narrative, and
the article says it has no Indian export data for the post-March window.

**The real finding is regulatory, not commercial.** South Africa's Basic Fuel
Price is import parity off **Mediterranean/Singapore (petrol)** and
**Mediterranean/Arabian Gulf (diesel)** — India is in none of them, so an Indian
cargo is priced off someone else's assessment regardless of origin. But the
industry association is publicly asking for "a transparent, market-reflective
basket of alternative international supply sources" and government talks are
under way. **Getting an Indian assessment into that basket is worth more than any
cargo, and the window is open now.** That is the piece's actual argument.

**Sourcing under blockade.** `gov.za` refused connections outright; the Consulate
General of India Johannesburg PDF never cleared Cloudflare; the Reuters article
403'd to both WebFetch and curl and only opened in a real browser that executes
the challenge. DMPR and the Agriculture Ministry brief came through. Every gap is
named in the article rather than papered over — including that South Africa's
biofuels mandate status could not be established, which matters because the brief
asked about biofuels.

**One clean contrast worth keeping.** India's agri exports to South Africa *rose*
8.94% to US$296m in the same year fuel fell 32.6%. Same country, same customs
source, opposite direction — which is what rules out "the relationship" as the
explanation and points at petroleum specifically.

## 2026-08-08 — Index now tracks the blog from the day it opened

Cleared the stray `Meta` label from about-author (an artefact of testing whether
the API could write labels at all — `apply_labels.py` skips posts that already
have labels, so its own override never got the chance to blank it). Verified the
orphan hub is empty and linked from nowhere: **Blogger returns HTTP 200 for any
`/search/label/` path**, so a 200 proves nothing and the real test is whether the
page renders any cards. It renders none.

Two gaps surfaced while checking. **AI Tracker existed as a label but was missing
from the index chips** — thirteen labels, twelve hubs listed. And the index had
been built before the last two posts. Both fixed by regenerating.

**Then the index was given a fourth axis: date.** It now opens with the founding
date and carries a month-by-month table with a running total.

**The interesting part is what that exposed.** The blog opened on **4 October
2020** with a single post, then published nothing for **six years**. The archive
proper starts **21 July 2026**. The month table shows October 2020 (1), July 2026
(23), August 2026 (73) — and the gap is described in the text rather than hidden
by starting the chart in 2026. A histogram that quietly begins at the busy part
is a way of not mentioning the quiet part.

**Also recorded on the page: three withdrawn drafts and duplicate variants** exist
in the archive with no live URL. They are counted as absent rather than silently
dropped, because "97 articles" should be a statement someone can check.

The date logic is derived, not hardcoded: the founding date, the gap length and
the month buckets all come from the manifest, so the section stays correct as
posts are added.

## 2026-08-08 — AI Tracker Edition 02, and its own methodology caught out

**Edition 01 promised "GitHub stars are checkable" and then copied its star
counts from a roundup article.** That is not the same thing, and Edition 02 says
so in the text. Every figure now comes from the **GitHub search API**, queried on
publication day, which also resolved each project name to its real repository.

**The re-measurement is the edition.** All eleven repositories with a star figure
grew between the two editions: **265,900 to 407,271 combined, +53.2% in roughly a
fortnight**, three more than doubling — grok-build +162.6%, OmniRoute +139.1%,
hallmark +126.3% — and Graphify crossing 100,000. Ranked by velocity rather than
size, because in a two-week window direction is the information.

**The precision is stated as worse than it looks.** Edition 01's baselines were
rounded ("32K", "18K", "10K") and dated only to "mid-to-late July", so both ends
of every growth calculation are approximate and the interval is somewhere between
two and four weeks. The edition says to read the ordering, not the decimal place,
and commits Edition 03 to an exact API baseline with an exact date. Publishing
"+162.6%" off a rounded base without saying so would have been the easy version.

**Model releases were demoted rather than dressed up.** Aggregators disagreed on
dates and on whether entries were new models, point updates or marketplace
listings, and none was checked against a vendor page. They appear under a heading
that says *explicitly unverified*, with an instruction not to cite the dates.
A star count has an API; a model release has a blog post someone has to read.

**Structural fix worth noting.** Edition 01 rendered its entries from a
JavaScript `DATA` array, so the archived HTML contained an empty `<div id="grid">`
and the content existed nowhere in the markup. Edition 02 is a server-rendered
table in the house `gs-table-v1` style — legible to the archive, to crawlers and
to anyone reading source.

**Index:** the tracker now has its own section rather than sitting as one dated
row among 97, because it is a standing serial that replaces itself in place at a
fixed URL. Rebuilt after snapshotting — the first attempt pulled the pre-retitle
name from a stale manifest, which is the argument for regenerating from the
manifest rather than hand-editing.
