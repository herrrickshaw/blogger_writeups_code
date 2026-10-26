# Theme audit, 26 October 2026

All 376 posts in `posts/` were rendered in headless Chromium at 375px (phone) and 1024px (desktop), inside the theme's own CSS and a copy of its single-post markup (header, `.wrap` column, `#Blog1`, post header, post body, Topics, pager, footer). Each post was rendered twice: once with the live theme (`theme/base.xml`, no modules) and once with the new theme (`theme/theme.xml`). Scripts and raw output are in `out/research/theme-audit/`.

**Limits.** The live blog is blocked from the audit machine, so this is a faithful local copy, not the live page. AdSense does not run locally, so ad placement is simulated: one filled 280px Auto-ads container goes after the first child of every element with two or more children (at most 80 per post, 15,037 in all). That covers every place AdSense *could* put an ad, not where it actually does. Chart.js does not load locally (3 posts).

## Results

| Check | Live theme | New theme |
|---|---|---|
| Posts that scroll sideways on a phone | 20 | 0 |
| Posts that scroll sideways on desktop | 4 | 0 |
| Posts where theme homepage styles leak into the post (`.hero`, `.card`, `.wrap`) | 17 | 0 |
| Simulated ads inside a table | 8,538 (all 376 posts) | 0 |
| … inside a list | 1,119 (358 posts) | 0 |
| … inside a figure (between a chart and its caption) | 480 (242 posts) | 0 |
| … inside a side-by-side row (mostly the accessibility toolbar) | 483 (347 posts) | 0 |
| … inside a multi-column grid (stat tiles) | 306 (216 posts, desktop) | 0 |
| … clipped by a scroll box or collapsed section | 771 (91 posts, phone) | 0 |
| … directly under a heading, cut off from its text | 92 (22 posts) | 0 |
| … narrower than 300px on a phone | 10,797 (375 posts) | 744 (18 posts) |
| Desktop line length, median characters per line | 80 | 70 |
| Posts with text lines over 95 characters (desktop) | 288 | 51 |
| Posts with running text below WCAG AA contrast (4.5:1) | 188 (567 blocks) | 18 (30 blocks) |
| Header link tap height | 22px | 30px |

The homepage renders identically apart from the taller nav links (checked element by element at both widths).

## What was wrong, and the module that fixes it

1. **Theme homepage styles leaked into posts** (`gs-scope-chrome-v1`). The theme styles `.hero` (navy block, white text, 72px padding), `.card` (32px padding, bottom rule) and `.wrap` (20px side padding) for its homepage. Posts that use the same class names got those styles too. In jai-kisan-jai-javan and the-recycling-lottery an intro block turned navy with white text. india-mineral-oil's 32 cards gained 32px padding and rules, adding about 3,300px of page height. These theme rules now apply only outside the post body.
2. **Ads inside structures** (`gs-content-guard-v2`, replaces `gs-table-guard-v1`). The earlier fix moved ads out of tables only. The new guard also moves an Auto-ads container out of lists, figures, code blocks, collapsible sections, quotes, side-by-side rows, multi-column grids, scroll boxes, and boxed notes and cards (tinted, framed or accent-ruled, unless the box holds most of the post). It places the container just after the outermost such structure. An ad directly under a heading moves above the heading.
3. **Long lines** (`gs-readable-v1`). Paragraphs were capped at 70ch, which is about 80 characters in Georgia; list items had no cap, and 234 posts had list items over 95 characters. Text blocks now stop at 64ch. The remaining long lines are fine print (disclaimers, source lines) whose own CSS sets a wider measure.
4. **Page overflow on phones** (`gs-readable-v1`). Long links and `data/...` file paths, code blocks and a fixed-width canvas pushed pages sideways. Long words now break, code scrolls in its box, and media is capped at the column width. The table template had already fixed the table causes.
5. **Contrast** (`gs-readable-v1`). `.gb-note` (196 posts) was #868e96 on white, 3.3:1; it is now #5f6871 (5.7:1). The theme's "Advertisement" label was #8a8a8a (3.4:1) at 9.6px and is now #6b6b6b (5.3:1) at 10.6px. In the 18 posts left, 14 use a one-off grey note class of their own (`.mp-note`, `.et-note`, `.tr-note` and similar, 3.0–3.9:1), best fixed in those posts. The other 4 are white text on a dark image or gradient, which the check cannot see, so they are probably fine.
6. **Section links under the sticky header** (`gs-readable-v1`). On desktop the header is sticky, so a contents link scrolled its heading under the header. Headings now stop 76px below the top.
7. **Tables** (`gs-table-template-v1`, earlier today; see `out/research/table-audit-2026-10-26.md`).

## Not fixed by the theme

- Fine print below 15px (disclaimers, source notes) in 365 posts is the posts' own design, kept small on purpose.
- 18 posts have a content column narrower than 300px on phones (a padded wrapper around the whole post), so any ad there is narrower too.
- Per-table problems listed in the table audit (27-column tables, headerless tables, ragged rows) need post edits.
- Where AdSense actually places ads, and how many, is set in AdSense (Auto ads > ad load, excluded areas, page exclusions), not in the theme.

## AdSense note

Moving an Auto-ads container that AdSense has placed is a change to ad placement. The theme never hides, resizes, reloads or blocks an ad, and the container moves before it is shown. Still, AdSense's policies are the final word. If the account gets a placement warning, retire `gs-content-guard-v2` in `theme/modules.json` and rely on CSS and AdSense's own excluded areas.
