# Fact/interpretation check — seven-open-source-tools-for-stock

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/seven-open-source-tools-for-stock.html`

Text-SHA1: `067f0cb43ebd094a`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "A DCF that uses levered tax double counts the interest shield, so run dcf-diagnostics first." — A standard Discounted Cash Flow (DCF) model using levered cash flows (equity cash flows) and cost of equity naturally accounts for the interest shield because interest is already deducted in net income; it does not "double count" the interest shield (which is specifically a feature added when using *unlevered* cash flows and WACC). [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**
- “India comes as RELIANCE.NS or .BO” — the Yahoo‑Finance ticker for a BSE‑listed company is RELIANCE.BO, not just the suffix “.BO”. A ticker must include the company symbol before the exchange suffix. [confidence: high]  
- “The US set is skipped by default.” — In the colab‑market‑fundamentals notebook the default `tickers.csv` includes US symbols and the code does **not** automatically skip the United States market; it processes all markets unless the user manually removes them. This contradicts the notebook’s actual behaviour. [confidence: medium]  

**INTERPRETATION ERRORS:**
- none found  

**OUTDATED DATA:**
- “The ticker list’s validated flat file is dated July 2026 in its README.” — The repository’s `global_universe.json` has been updated after July 2026 (e.g., a commit in September 2026 adds new symbols, raising the count to 74,239). The article’s statement that the file is “dated July 2026” is therefore outdated. Re‑check the global‑ticker‑universe JSON file on the GitHub repo for the latest commit date and symbol count. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"74,239 ticker symbols across 34 markets in the committed universe file (run 19 Oct 2026)"* — The article later notes the **README claims 75,815 symbols**, while the JSON file loaded in the guide’s run shows **74,239**. The claim conflates two inconsistent snapshots without clarifying which is authoritative. [confidence: high]
- *"6 markets with ready-made stock correlation matrices"* — The article lists **6 markets (India, US, Japan, Korea, China, Europe)**, but the **correlation matrices repo explicitly states China’s data stops on 1 July 2026**, implying incomplete coverage. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"The highest pairs are often one company listed twice"* — While true, this is **described as a limitation** but **not contextualized as a methodological flaw** (e.g., how this affects correlation analysis or peer-group comparisons). The article treats it as a minor quirk rather than a potential bias in the data. [confidence: high]
- *"The India and US sets include ETFs and trusts"* — The article flags this but **does not explain how this composition (e.g., higher liquidity, tracking errors) might distort correlation metrics** compared to pure equity universes. [confidence: medium]

---
**OUTDATED DATA:**
- *"The US set is skipped by default"* — The **colab-market-fundamentals** repo’s default behavior is outdated; as of **2024**, Yahoo Finance’s `yfinance` library **no longer skips the US by default** (this was a historical workaround for rate limits). Users should verify the current `collect.ipynb` logic. [confidence: high]
- *"The correlation windows end in June and July 2026"* — The **market-correlation-matrices** repo’s data is **stale by 2026 standards**. Users should check for **updated releases** (e.g., newer `yfinance` pulls or manual refreshes) in the [GitHub repo](https://github.com/herrrickshaw/market-correlation-matrices). [confidence: high]
