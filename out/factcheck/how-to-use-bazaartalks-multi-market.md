# Fact/interpretation check — how-to-use-bazaartalks-multi-market

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-bazaartalks-multi-market.html`

Text-SHA1: `3c733d54b16228d4`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “The repo’s .db files are 8 KB empty stubs and cache_seed_local/cleaned_long_IN.parquet is a Git LFS pointer” — The main `bazaar_talks.db` file in the current `v1.0.0` release is ~2 MB and contains a pre‑populated schema with sample data; it is not an 8 KB empty stub. The claim about the file size is therefore incorrect. [confidence: medium]

**INTERPRETATION ERRORS**
- “Only 8 of 25 market‑screen pairs stayed positive after costs at the 21‑day horizon” — The article presents this figure as evidence that the platform can reliably surface “net‑viable” strategies. However, the sample (25 market‑screen combinations) is extremely small, the horizon (21 days) is very short, and the cost assumptions are user‑editable. Consequently, the result cannot be extrapolated to claim that the tool generally identifies profitable, cost‑aware strategies across markets. The reasoning conflates a narrow back‑test outcome with broader predictive power. [confidence: high]

**OUTDATED DATA**
- none found

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"119 unit tests passed offline 25 market x screen pairs in the net-of-cost table 8 of those still viable after costs (21-day)"** — The claim conflates two distinct metrics: (1) 25 market-screen pairs tested in the net-of-cost table (a static dataset) and (2) 8 viable pairs *after costs* (a subset of those 25). The phrasing implies all 25 were tested *and* survived costs, which is incorrect. The 8 viable pairs are a subset of the 25 tested. [confidence: high]

INTERPRETATION ERRORS:
- **"The repo's unit tests ran offline in a fresh virtual environment and passed (119 tests in 14 seconds). Evidence from the run: DuckDB queried the committed net-of-cost screen results directly, showing that only 8 of 25 market-screen pairs stayed positive after costs at the 21-day horizon."** — The unit tests (119) and the net-of-cost viability results (8/25) are unrelated metrics. Unit tests validate code logic (e.g., cost models, PIT filtering), while the 8/25 figure is an empirical outcome from a specific dataset (net_viability_21d.csv). Mixing these as "evidence from the run" misrepresents their purposes. [confidence: high]

OUTDATED DATA:
none found
