# Fact/interpretation check — how-to-use-digital-twin-for-ipa

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-digital-twin-for-ipa.html`

Text-SHA1: `7d0e017e3b8f0c81`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Python 3 | the build and refresh scripts are stdlib-only; the demo used Python 3.14" — Python 3.14 has not been released (Python 3.13 was released in late 2024, and 3.14 is scheduled for release in late 2025/2026, making a fully stable production release by an October 2026 demo problematic or an anachronism depending on current real-world timelines, but more importantly, Python's version progression makes a specific version claim for a future date speculative or factually unverifiable). [confidence: medium]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- “Python 3.14” — Python 3.14 has not been released; the latest stable version as of October 2026 is Python 3.13 (with 3.14 still under development). The article incorrectly states the required version. [confidence: high]  

**INTERPRETATION ERRORS:**  
- “Every claim carries a note on how it was verified, and access failures (blocked sites, JavaScript‑only portals) are recorded as data rather than skipped.” — Recording that a site could not be accessed does **not** provide the underlying incentive information; it merely logs a failure. Presenting these failure logs as “data” implies the dataset is complete, which is misleading because the actual scheme details remain missing for those sources. [confidence: high]  

**OUTDATED DATA:**  
- none found

## Mistral open-mistral-nemo

Here is the structured report based on the provided article text:

---

**FACTUAL ERRORS:**
- *"1,849 companies in the SQLite database (1,483 flagged as Indian filers)"* — The article states this count is "as of the 18 October 2026 demo," but the README explicitly claims **1,785 companies** (not 1,849) in the same section. This discrepancy contradicts the primary source (the repo’s own README). [confidence: high]

**INTERPRETATION ERRORS:**
- *"The demo only read data and ran one offline rebuild... It did not call any live government site and did not run the network-dependent layer builders."* — This claim implies the demo’s offline validation (JSON parsing and catalogue rebuild) is sufficient to verify the **stacking rules, legal anchors, or real-time eligibility** of incentives. However, the article later acknowledges that **verified_on_site status is a snapshot** and that many instruments lack on-site verification. Thus, the demo’s offline checks do not confirm whether schemes are *actually* stackable or legally valid in practice. [confidence: high]

**OUTDATED DATA:**
- *"1,785 companies"* (README claim) and *"1,849 companies"* (demo claim) — Both figures are from October 2026, but the article was published in **2026** (as per the revision date). To verify current accuracy, check the **latest `data/companies.db` file on GitHub** (series: `digital-twin-for-ipa/data/companies.db`). [confidence: high]

---
