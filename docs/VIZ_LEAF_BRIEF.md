# Leaf brief: visual-first edition of one post

You are rewriting ONE live post into the visual-first format. You own only `out/viz/<slug>/**` and
`out/update-2026-11-15-<slug>.html`. Do not touch any other file, do not publish, do not run git.
Work from the repo root `/home/user/blogger_writeups_code`.

## Steps

1. `python3 tools/viz_new.py <slug>` (skip if `out/viz/<slug>/outline.md` exists). Read `out/viz/<slug>/outline.md`
   (the post as headings, paragraphs and pipe-row tables). Read `docs/VISUAL_STORY_STYLE.md`. Read
   `out/research/blending-visual/build.py`: it is a finished example (a longer post, 4 charts) that passes the oracle.
2. Decide the 3 or 4 findings the post exists to show. A finding is a comparison, a trend, a share, a gap or a
   sequence that the post's own numbers support. Choose the chart form by the job (`docs/VISUAL_STORY_STYLE.md`):
   ranking or comparison -> `bars`; range -> `bars` with `(low, high)`; share with uncertain top ->
   `bars(..., from_zero=True)`; change over time -> `line`; how a total is built -> `waterfall`; sequence of
   events -> `flow`. One chart per section. Put the data behind a chart in `numbers([...], [...])` when a reader may want it.
3. Edit `out/viz/<slug>/build.py`: `top_line([...])` (1 to 3 bullets, a big number first, drawn from the post's headline
   figures), then `insight(headline, chart, "What it means: one sentence.", "What to do: one sentence.", anchor)` for each
   section. Put the things a reader may still want but that do not earn a section in collapsed blocks:
   caveats the original made ("what this could not establish"), standards or method notes, and
   `sources_block(body_links(FR.body))` for every external link in the original body (already in the skeleton).
   Keep dated "Updated ..." notes and photographs (the skeleton does: `FR.keep_front + FR.notes`).
4. Every number you write must be in the original post, or computed from its numbers: put the computation in
   `out/viz/<slug>/derived.json`, e.g. `{"190": "570/3"}` (operands must be original numbers), or
   `{"7": "count: seven countries in the table"}` for a count you made yourself. Never round a figure to a different
   number, and never add a number from memory or from outside the post. Keep units, years and qualifiers
   ("about", "reported", "projected") the original used. If the original disputes or hedges a figure, the chart title
   and the sentence must too.
5. Run `python3 out/viz/<slug>/build.py` then `python3 tools/viz_verify.py <slug>`. Read every FAIL line, fix the build,
   repeat. It must print `PASS <slug>`. Do not edit anything under `tools/` to make it pass.
6. Look at the result: `node tools/mobile_audit.js out/update-2026-11-15-<slug>.html --shot /tmp/<slug>.png`, then Read the
   PNG (it is a full-page 375px screenshot; if it is very tall, that is expected). Check that each bar, label and value is
   legible and unclipped, each headline is supported by its chart, the accent colour marks the finding the headline names,
   and nothing from the original's argument was reversed or lost. Fix and re-run until you would publish it.
7. Report back in under 120 words: the three or four headlines, anything you left out of the body on purpose and where
   it went, any `count:` items, and any figure in the original that looked wrong or inconsistent (do not silently fix the
   original's content; say so).

## Rules that matter most

- Fidelity beats polish. A chart whose headline overstates the data is worse than no chart.
- Headlines: "Subject: what the data shows", sentence case, 90 characters or fewer, no idioms, questions or teasers
  (`docs/HEADLINE_STYLE.md`). Chart titles state the takeaway; section `<h2>`s state the finding.
- Exactly two sentences per section after the chart, each ending in a full stop, no other full stops followed by a capital.
  Use `Rs`/`₹` forms and abbreviations that do not contain ". " (write "No. 5" as "number 5", "Dr." as "Dr").
- Collapsed detail is the place for nuance, not the body. The body is what a busy reader takes in on a phone.
- Do not invent a recommendation the original does not support. "What to do" must follow from the post's own
  proposals or findings; if the post proposes fixes, use them.
- No scripts, no iframes, no new external links, no old domain (`masaladeutsch.blogspot.com`).
