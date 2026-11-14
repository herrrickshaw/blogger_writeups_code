# Visual-first post format

For readers who decide things: business leaders, investors, officials. They read on phones, between other
work, and want the finding before the method. Build the parts with `tools/exec_viz.py`; it enforces most of
the rules below.

## Shape of a post

1. **Top line** (`top_line`): three bullets, each opening with the number in large type. Example:
   **66%** of petrol's energy per litre is what ethanol carries, so E20 costs drivers 2–6% in mileage.
2. **Three or four insight sections** (`insight`): an `<h2>` that states the finding (house headline style,
   `docs/HEADLINE_STYLE.md`), one chart, then exactly two sentences: **What it means** and **What to do**.
3. **Fixes**: a short numbered list, one line each, naming who should act.
4. **Detail on demand**: standards lists, method notes, "what this piece could not establish" go in
   collapsed `<details>` blocks, not open text.
5. Sources, related posts and the disclaimer as before.

## Charts

- **The chart title states the takeaway** ("Brazil and Europe cap all blending ethanol at 1 to 1.5 mg/kg;
  India caps only 2G"), never a label ("Chloride limits"). 90 characters at most.
- **Grey for everything, one accent** (`#2251FF`) for the finding the title is about.
- **No gridlines.** Values are printed on the label line of each bar; a thin marker shows a reference value
  (a limit, 100%, the tank size) and is explained once above the chart.
- **No open data grids.** The numbers behind a chart go in `numbers()`, collapsed under "Show the numbers".
  A table shown open is allowed only for 3 rows or a 2×2.
- **Pick the form by the job:** ranking or comparison → `bars`; a range → `bars` with (low, high);
  a share with an uncertain top → `bars(..., from_zero=True)`; change over time → `line`;
  how a total is built → `waterfall`; a sequence of events → `flow`.
- **Phone first.** Bars are HTML, so labels stay at text size on any screen; the line chart ships a 360-wide
  and a 640-wide drawing. Nothing uses JavaScript (the main site strips scripts).

## Writing

- Paragraphs of 60 words or fewer; one idea each.
- Use only numbers already published in the post or computed from them, and assert the arithmetic in the
  build script (see the two pilots).
- Keep the existing title and URL; add a dated "Updated" note saying the post was rewritten and the figures are unchanged.

## Check before publishing

    python3 <build script>                       # writes out/update-<date>-<slug>.html
    node <scratchpad>/shot.js <file> out.png 375  # no overflow at phone width; look at every chart
    python3 tools/blogger_api.py update --slug <slug> --file out/update-<date>-<slug>.html --dry-run
