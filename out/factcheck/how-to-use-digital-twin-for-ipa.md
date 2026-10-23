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
- "Python 3 | the build and refresh scripts are stdlib-only; the demo used Python 3.14" — Python 3.14 is a future version relative to current real-world software timelines, making a claim of a demo run utilizing Python 3.14 on October 18, 2026 implausible and historically inaccurate for the present era. [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 5258, Requested 4248. Please try again in 11.295s. Need more tokens? Upgrade to Dev Tier today at https://con]

## Mistral open-mistral-nemo

Here is the structured report based on the provided article text:

---

**FACTUAL ERRORS:**
- *"1,849 companies in the SQLite database (1,483 flagged as Indian filers)"* — The article claims this count is accurate as of **18 October 2026**, but the **README.md** in the GitHub repo (the primary source) states the company count is **1,785** (with 1,483 Indian filers). This discrepancy suggests either a typo in the article or an outdated snapshot. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The demo only read data and ran one offline rebuild (on a scratch copy). It did not call any live government site and did not run the network-dependent layer builders."* — While technically correct, this claim **misrepresents the project’s limitations for users**. The article later notes that **live sources (e.g., Invest India, MCA) are blocked or crawling-sensitive**, meaning the twin’s **full functionality depends on network access and API keys**—not just "offline rebuilds." The implication that the demo’s offline status proves the tool’s robustness is misleading, as critical layers (e.g., real-time scheme status) require live data. [confidence: high]

**OUTDATED DATA:**
- *"1,785 companies"* (README.md) vs. *"1,849 companies"* (article) — The article’s figure is likely outdated; the **GitHub repo’s README.md** (primary source) should be checked for the latest count. [confidence: high]
- *"312 incentive instruments in the flat index (195 central, 117 state)"* — While correct for the **18 October 2026 snapshot**, the article does not verify if this count has been updated in newer commits or releases. The **`layers/13_flat_instrument_index.json`** file (cited as the source) may have changed post-2026. [confidence: medium]

---
