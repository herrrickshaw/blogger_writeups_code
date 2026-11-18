# Run order for the November 2026 backlog (Mac)

Run from the repo root, in this order. Each stage can be rerun; finished work is skipped. `DRY=1` shows without writing.

| # | Command | What it does | Notes |
|---|---|---|---|
| 0 | `git pull --no-rebase origin main` | Gets the drafts, scripts and the rebuilt index | The Mac snapshot of 19 Nov shows Phase 3 done (the 11 folded posts are out of the manifest) |
| 1 | `bash out/run_order_nov2026.sh status` | Shows what is pending | Reads only |
| 2 | `bash out/run_order_nov2026.sh editions` | Publishes visual editions, 20 a run (`LIMIT=n` to change) | Exit 3 means Blogger's daily ceiling; rerun next day. 313 editions exist; progress is in `out/viz/published.json` |
| 3 | `bash out/run_order_nov2026.sh updates` | The 3 stale-post updates and the how-to-use access notes (dated 16 Nov) | Skips posts with an edition, posts not live, and notes already present |
| 4 | `bash out/run_order_nov2026.sh drafts` | Inserts the 21 new posts as drafts | Open each in Blogger, check on a phone width, press Publish. Mahanadi IPO first (issue opens 19 Nov) |
| 5 | `python3 tools/snapshot.py && git add -A && git commit -m snapshot && git push` | Records the live state | Needed so the index can see the new posts |
| 6 | `bash out/run_order_nov2026.sh index` | Rebuilds the article index from the snapshot, keeps the injected wrapper/translate/disclosure, publishes it | Do last: one index write after everything is live |

Why the index is last: it is built from `posts/`, which only holds posts that are live and snapshotted. A cloud rebuild today (`out/article-index-updated-2026-11-18.html`) adds 22 posts that were live but missing from the index; stage 6 redoes it so the 21 new posts are included as well.

The article index post is `https://blog.vertistratsolution.com/2026/08/article-index-start-here.html`. `tools/splice_index_injections.py` keeps the pieces injected after the original build (the .artx wrapper and CSS, the translate widget, the AI disclosure); a plain rebuild drops them.
