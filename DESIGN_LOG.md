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
