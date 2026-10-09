# usiponavadaaariponacoffee.blogspot.com: manual updates

The blog API account in `tools/blogger_api.py` cannot edit this blog (see
`docs/CUSTOM_DOMAIN_RUNBOOK.md`), and blogspot pages cannot be opened from the cloud
session, so updates to this blog are prepared here and pasted by hand.

## govt-announcements-policies-and-news (2026/07)

File: `govt-announcements-policies-and-news-oct2026.html`, built 9 October 2026.

- **Content:** the quarter-by-quarter PIB scheme-announcement index. It has 4,146
  announcements across 40 quarters, from January 2017 to 1 October 2026.
- **Display:** each quarter lists its 30 most recent announcements, newest first
  (1,147 rows shown). Each list links to the full filterable list on masaladeutsch.
- **Source:** regenerated from `digital-twin-for-ipa/scripts/build_reportage.py`
  against the local PIB index, which runs to 1 October 2026.
- **Removed:** four keyword collisions:
  - PRID 2306813 Corporate Mitra
  - 2314436 Nidhi companies
  - 2314970 Operation Drishti
  - 2315327 port e-methanol
- **Assumption:** the cloud session could not open the live page. This file assumes the
  page is the quarterly reportage index, as the runbook describes. Before pasting,
  compare its first screen with what is live.
- **Not duplicated:** the masaladeutsch Quarterly Reportage post uses different wording
  and layout. That keeps the two blogs from carrying duplicate content.

To update: open the post in Blogger, switch to HTML view, select everything, paste the
file's contents, then click Update.
