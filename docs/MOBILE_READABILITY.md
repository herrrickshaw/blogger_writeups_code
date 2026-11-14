# Mobile readability: audit and fixes (15 Nov 2026)

## How it was measured

Every archived post (`posts/*.html`, 526) was rendered in Chromium at a 375px phone viewport, inside the
live theme's CSS and content script (extracted from `theme/theme-vertistrat-2026-11-14.xml`). For each post
the script measured page width, tables that need sideways scrolling, the rendered size of chart labels
(SVG font size × the scale the chart is drawn at), and paragraph length.

## What was wrong

| | Before |
|---|---|
| Inline SVG charts whose typical label renders under 9px | 524 of 593 (88%); median label 6.1px |
| Posts with at least one such chart | 350 (67%) |
| Tables that need sideways swiping | 649, in 292 posts (56%) |
| Posts with 3 or more paragraphs over 90 words | 377 (72%) |
| Median post length | about 2,300 words |

The cause of the chart problem: most charts were drawn about 700 units wide with 10–12 unit text, so a
phone shows them at half size. Body text itself is fine (18.7px median); page width was fine (one post
scrolled sideways).

## Fix 1, every post now: theme module `gs-mobile-v1` (CSS + JS)

- A chart whose labels would render under 10px is given the width at which they render at 10px, inside a
  sideways scroller, with a "Swipe sideways to read the whole chart" line above it. Charts built with
  `tools/exec_viz.py` are already phone-sized and are skipped.
- A table that still scrolls sideways gets a "swipe" line, and on phones its first column stays in view
  while the rest scrolls.
- Slightly more line height and paragraph spacing on phones.

After: charts with a typical label of at least 9.5px went from 69 to 462 of 593 (78%). The 131 left are
mostly small multiples (many small SVGs in a grid) and charts already inside a scroll box; they need
redrawing, not CSS. Build and upload: `python3 tools/theme_build.py`, then Theme > Restore with
`theme/theme.xml` (see `docs/THEME_RUNBOOK.md`).

## Fix 2, post by post: the visual-first rewrite

Long paragraphs and dense tables are content problems. `docs/VISUAL_STORY_STYLE.md` sets the format and
`tools/exec_viz.py` builds the parts. Pilots (15 Nov 2026):

- `out/viz/chloride-in-fuel-ethanol-is-15464-sets/edition.html` (`out/research/chloride-ethanol/build_visual.py`)
- `out/viz/blending-on-budget-energy-density-and/edition.html` (`out/research/blending-visual/build.py`): 3,886 words to about 1,740.

Suggested order for the rest: the most-read list first, then posts with the most swipe tables and small charts
(re-run the audit script to rank them).
