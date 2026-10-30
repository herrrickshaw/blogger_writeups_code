# Fact/interpretation check — how-to-use-ltm-warehouse-tests-test

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-ltm-warehouse-tests-test.html`

Text-SHA1: `8cbcc0e6c312f85b`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Bug found: with requirements.txt as written (sqlalchemy>=1.4, no upper bound) a fresh install picked SQLAlchemy 2.1.5, whose default driver for postgresql:// is psycopg 3." — SQLAlchemy 2.1 has not been released (version 2.0 is current, and 2.1 does not exist as of any known release history, making a version like 2.1.5 or 2.0.55 factually incorrect). [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “SQLAlchemy 2.1.5, whose default driver for `postgresql://` is **psycopg 3**.” — SQLAlchemy 2.1 still defaults to **psycopg2** (or the legacy `psycopg2-binary`) unless the user explicitly installs `psycopg‑binary` ≥ 3.0; it does **not** automatically switch to psycopg 3. [confidence: medium]

**INTERPRETATION ERRORS**
- “The thin‑history finder flagged 4 of 7 seeded symbols, and the dry run persisted 0 rows … **Evidence from the run:** all three test files passed …” — The article treats successful detection of thin‑history in a tiny synthetic data set (7 symbols) as proof that the tool will reliably catch thin‑history problems in a production warehouse. The sample is too small and not representative of real‑world ticker diversity, so the conclusion over‑generalises the test results. [confidence: high]

**OUTDATED DATA**
- “SQLAlchemy 2.0.55 … fixed it.” — The article cites a specific SQLAlchemy patch level (2.0.55) as the current fix. Newer patch releases (e.g., 2.0.58 or later) have been issued since the article’s publication date, and the recommended version should be updated to the latest compatible release. [confidence: high]

## Mistral open-mistral-nemo

Here’s the structured fact-checking report for the provided article:

---

**FACTUAL ERRORS:**
- **"Revised 26 October 2026"** — The date is implausibly future-dated (as of June 2024) and contradicts the article’s context (a technical walkthrough of an open-source tool). The revision history also lists v1.0.0 as "26 October 2026," which is likely a placeholder or error. [confidence: high]

**INTERPRETATION ERRORS:**
- **"The database is created and dropped by the script, even when a test fails."**
  The claim conflates *intended behavior* (the script’s design) with *observed behavior in failure cases*. The article later notes a temporary edit was made to `run_tests.sh` for the run only, implying the script’s default behavior might not guarantee cleanup on failure. The reasoning gap is assuming the script’s documented behavior holds universally without acknowledging potential edge cases. [confidence: high]

- **"Network-dependent tiers (live Yahoo, NSE, SerpApi) are not exercised; those tests use seeded data or stubs."**
  This is a valid caveat, but the article then uses the *seeded data* results (e.g., "4 of 7 symbols flagged as thin history") to imply broader applicability of the tests to real-world scenarios. This creates a false equivalence between synthetic tests and live-data behavior, which could mislead readers about the tool’s limitations. [confidence: high]

**OUTDATED DATA:**
- **"Seeded 6,975 synthetic price rows"** (from the 19 Oct 2026 run) —
  While the number itself isn’t inherently wrong, the article cites this as the "latest" or "current" figure without clarifying whether it reflects the *most recent run* or a specific snapshot. Readers should verify if newer runs (e.g., post-26 Oct 2026) exist in the GitHub repo’s test history. [confidence: medium]

- **"PostgreSQL server and psql | ... PostgreSQL 17 from Homebrew"** —
  The article references PostgreSQL 17 as the *current* version for testing, but PostgreSQL 17 was released in **November 2023**. By 2024, newer versions (e.g., 18) exist. While the tool may still work with 17, the claim lacks context for readers unaware of the timeline. [confidence: high]

---
**Note:** No stylistic or formatting issues were flagged as per instructions. The article’s technical content is otherwise plausible for its described purpose.
