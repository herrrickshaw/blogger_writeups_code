# Visual-first rewrite: status (16 Nov 2026)

Pipeline: `docs/VIZ_LEAF_BRIEF.md` (leaf instructions), `tools/viz_verify.py` (the oracle), `tools/viz_render.py` (spec to edition),
`tools/viz_go.py` (render + check in one call), `tools/viz_triage.py`, `tools/viz_wave.py`, `tools/viz_publish.py`.
Run state lives in `.unlazy/viz/` (not committed: machine-specific). **Nothing is published.** Editions are
`out/viz/<slug>/edition.html`, never `out/update-*.html` (phase3_publish.sh publishes every file with that name).

## Where it stands

| Disposition | Posts | What happens |
|---|---|---|
| done | 313 | edition passes the oracle, a driver read of every chart at 375px, and a contrast check |
| rewrite | 0 | the queue is empty: waves 1 to 18 built every eligible post |
| walkthrough | 64 | How-to command walkthroughs; phone layout only (theme module) |
| light | 41 | fewer than 30 distinct numbers; nothing to chart |
| interactive | 31 | scripts, canvas or iframes; phone layout only |
| frame | 19 | a template the splitter cannot cut yet |
| pending | 15 | an unpublished update or Phase 3 merge exists; rewrite after it is published and snapshotted |

Waves 1 to 18 are closed (313 editions). Each wave: `viz_wave.py prepare N 20`, 20 leaves, `seal`, `collect`, a contact sheet read
(`tools/viz_sheet.js`), `tools/viz_contrast.js`, `close`, commit.

## How the oracle works (what a leaf cannot get wrong)

Frame bytes (head, tail, sources card, caveats, dated notes) are kept by code; the leaf only chooses the findings. Every number
in the new text must be in the original or declared as arithmetic or a count in `derived.json`. One-sentence takeaways, one unit
per chart, no overflow at 375px, no chart label under 9.5px, collapsed tables, no script or old-domain link. Posts whose header
leaves a wrapper open (slide decks) get a bridge of closing and opening tags so charts keep a light surface.

## Token findings

Cost is turns x context: each leaf turn re-reads about 100k tokens of tool and system overhead, so 8 turns is about 100k. What cut it:
spec-driven rendering (the leaf writes JSON, never HTML), a compact outline instead of the full post, one command that renders and
checks and prints every fix at once, Haiku (same pass rate as the default model on a 12-post A/B), a prompt that names the required
steps. Median 8 turns, 100k tokens, 45 s per post.

## Defects the leaves found in the originals

Each leaf reports figures that look wrong in the post it read. They are collected in the commit messages of each wave only as
"checked"; the posts themselves are not edited. Repeated kinds: a headline number that disagrees with its own table by one unit or a
rounding step; a section that still states a figure its own later update replaced; a ratio quoted as "about three times" that
computes to 2.3; a count of items named that is smaller than the count claimed.

## Publishing (on the Mac, after reading the editions)

    git pull
    zsh out/gsc_index/phase3_publish.sh        # first: the merged posts must be live, and it publishes the old relink files
    python3 tools/viz_publish.py --dry-run     # shows what it would send
    python3 tools/viz_publish.py --limit 20    # publishes the next 20; stops at Blogger's daily write ceiling; run again tomorrow
    python3 tools/snapshot.py && git add -A && git commit -m "snapshot" && git push

`viz_publish.py` holds back an edition that links to a retired post and lists it (three today: they link to How-to guides that the Phase 2 hubs replace;
repoint after the hubs are published). Published slugs are recorded in `out/viz/published.json`.

## Possible errors found in the originals

`out/viz/leaf-flags.md` lists every figure a leaf flagged as inconsistent in the post it read (about 90 items from waves 14 to 18).
They are unverified leads, one line each with the post slug: rounding slips, a headline that disagrees with its own table, a
claim that a later dated update overtook. Nothing in `posts/` was edited.

## Still to do

- Publish on the Mac (steps above); the editions replace the live bodies and need `python3 tools/snapshot.py` afterwards.
- The 15 pending, 19 frame and 31 interactive posts need hand work or a template fix; the 64 walkthroughs and 41 light posts only need the theme module.
- The seven dated notes in `out/freshness/updates-2026-11-15/` are not yet applied to the posts or their editions.
