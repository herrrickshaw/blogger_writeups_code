# Data validation — the-50-tariff-and-234-one-untangling

> **Tests 2 and 3 are model output, not verified fact.** A flagged claim is a
> prompt to check the cited primary source, never a reason to edit the post
> on its own. Test 1 is deterministic.

Source: `posts/the-50-tariff-and-234-one-untangling.html` · title: From 50% to 10%: How Three Tariff Regimes and a Supreme Court Ruling Reshaped What Hits India's Exports · printed date: 12 September 2026
Run: 2026-09-18T14:25:37+00:00 · endpoint: http://localhost:20128 · model: -

## 1. House rules (static, deterministic)

| rule | severity | result | detail |
|---|---|---|---|
| js-parses | BLOCKER | PASS |  |
| no-disclaimer-in-script | BLOCKER | PASS |  |
| no-inverted-media-query | BLOCKER | PASS |  |
| dark-vars-locked | BLOCKER | PASS | n/a (no dark palette) |
| wpi-attribution | MAJOR | PASS | n/a |
| disclaimer-present | MAJOR | PASS |  |
| translate-widget | MINOR | PASS |  |
| index-link | MINOR | PASS |  |
| bw-override | MINOR | PASS | n/a (no dark palette) |
| table-units-in-header | MINOR | **FAIL** | 40% of 55 cells carry units |

9/10 passed.

## 2. Internal consistency (LLM)

_skipped: LLM disabled_
## 3. Claims ledger (LLM)

_skipped: LLM disabled_
