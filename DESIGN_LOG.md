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
