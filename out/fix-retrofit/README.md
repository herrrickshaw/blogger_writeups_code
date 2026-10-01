# Rule 8 retrofit: "What would fix this" on every archived post

Built 1 October 2026. `proposals/<slug>.json` holds the drafted section for each post
(mode `add`: 3–5 proposals; `rename`: an existing fixes section retitled; `skip`: not an
analytical piece). `tools/retrofit_fix_section.py` inserts it into `posts/<slug>.html` and
writes `post-<slug>.html` here; the inserted block is the only change to each body.

- 294 posts updated: 289 new sections, 5 existing fixes sections renamed.
- 9 skipped: ai-high-demand-launch-tracker, annexure-314-hsn-codes-mapped-to,
  chemical-import-substitution-full-hsn-8_01082878313, india-trade-sector-policy,
  ipa-digital-twin-reportage-latest, quarterly-reportage-4034-scheme,
  rajya-sabha-question-registry-scheme, tech-for-business-so-2019-tech-as,
  us-stock-picks-multi-screen-quant. Also left alone: about-author,
  article-index-start-here, the-masala-deutsch-shop-books-things.
- Placement follows rule 8: before the "What this piece does not establish" caveats where a
  post has them, else before Sources, the related-links box, or the disclaimer, and never
  inside a card, note or disclaimer box.

Publish with `bash tools/apply_batch.sh out/fix-retrofit` (resumable; stops at the daily
write ceiling), then `python3 tools/snapshot.py --as minor ...` after each day's run.
Rebuild after any post changes with `python3 tools/retrofit_fix_section.py` — it always
starts from the current `posts/` snapshot, so run it after `git pull` and before applying.
