# Visual-first rewrite: status (15 Nov 2026)

Pipeline: `docs/VIZ_LEAF_BRIEF.md` (the leaf instructions), `tools/viz_verify.py` (the oracle), `tools/viz_triage.py`,
`tools/viz_new.py`, `tools/viz_plan.py`. Run state lives in `.unlazy/viz/` (not committed: machine-specific).
Nothing here is published. Editions are `out/viz/<slug>/edition.html` (NOT out/update-*.html: phase3_publish.sh publishes every file with that name); publish each with
`python3 tools/blogger_api.py update --slug <slug> --file <edition> --dry-run` after reading it.

## Triage of the 482 live posts (`out/viz/triage.json`)

| Disposition | Posts | What happens |
|---|---|---|
| rewrite | 246 | leaf agent builds an edition; ~609,000 words |
| frame | 109 | different page template; `tools/viz_frame.py` needs a second template before they can be rewritten |
| walkthrough | 64 | "How to use ..." command walkthroughs; phone layout only (theme module) |
| interactive | 34 | scripts, canvas or iframes; phone layout only |
| light | 27 | fewer than 30 distinct numbers; nothing to chart |
| done | 2 | edition passes the oracle (blending, chloride) |

## Wave 1 (6 posts): 6 of 6 verified

| Post | Words (post incl. frame) | Charts | Agent tokens | Time |
|---|---|---|---|---|
| the-milk-india-doesnt-drink-cheese-and | 4,430 to 3,314 | 3 bar + 1 timeline | 143k | 149s |
| guar-gum-indias-35-billion-export-peak | 2,270 to 1,651 | 4 bar | 128k | 108s |
| global-biofuels-m-bankruptcy-bolt-on | 2,384 to 2,034 | 4 bar | 137k | 132s |
| sixteen-crops-twenty-years-where-indias | 3,706 to 2,203 | 4 bar | 149k | 187s |
| where-indias-fdi-actually-lands-state | 4,741 to 2,516 | 4 bar | 153k | 176s |
| one-nation-one-ration-card-doesnt-move | 7,765 to 2,767 | 4 bar | 145k | 147s |

Cost to scale: about 140k tokens and 2.5 minutes per post, so the 246-post queue is roughly 35 million tokens
in waves of 20 to 30. Every leaf reached PASS on its own re-runs; the parent re-ran every gate and read every chart.
What the parent caught that the leaf missed: a line chart joining five dated points across nine-year gaps (guar seed price),
replaced by one bar per dated reading.

## Defects found in the live posts while rewriting (for the author; originals not changed)

- one-nation-one-ration-card: Fix 1 says interstate use is "under 1 per cent" but the 25 October correction says up to 2.4%;
  section 8 gives the allocation as 554.93 lakh tonnes, the rest of the post 554.99; 6.35 million tonnes of rice sold to
  distillers sits beside 39 to 44 lakh tonnes used or issued for ethanol.
- where-indias-fdi-actually-lands-state: photo caption says Bengaluru tops four of five quarters, but the 24-quarter totals put
  Navi Mumbai first; Delhi "present in 25 of 24 quarters"; text says every other Maharashtra district is under 0.3% but Nashik
  is 0.32%; the Calendar 2021 chart cites "figures as stated in this article" and its numbers appear nowhere else.
- sixteen-crops-twenty-years: standfirst calls maize the "fastest-growing major crop", but moong (6.1%) outgrows maize (5.8%);
  the edition says "fastest-growing cereal".
- global-biofuels: "SAF and RNG still get capital" sits awkwardly with Montana Renewables' second DOE draw cut from up to
  $658 million to $34 million in September 2026.
- guar-gum: the hero image does not load offline (alt text only); it is an external image, not a fault of the edition.

## Known limits of the kit (improvements to make before the next wave)

- `exec_viz.bars` has no diverging (negative) bars: negative growth shows as a tiny grey bar with a minus sign.
- A chart that mixes a flow, a stock and a norm on one axis (ration-card allocation chart) passes the oracle; only the
  manual read catches it. The oracle cannot judge whether a chart type fits the data.
- The oracle's counted items (`count:`) are listed for review; FDI used four (row counts).
