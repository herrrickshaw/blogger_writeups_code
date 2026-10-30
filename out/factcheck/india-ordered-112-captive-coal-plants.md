# Fact/interpretation check — india-ordered-112-captive-coal-plants

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-ordered-112-captive-coal-plants.html`

Text-SHA1: `3f696e914985c66b`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 2890, Requested 5383. Please try again in 2.0475s. Need more tokens? Upgrade to Dev Tier today at https://con]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"269 GW peak demand on 10 September 2026, the day the exchange recorded a 281% year-on-year jump in buy bids"* — **No credible public data confirms a 281% YoY jump in buy bids for 10 September 2026.** While IEX’s September 2026 release (via JM Financial) reports a **281% YoY increase in *total buy bids*** (not just on 10 September), the article does not specify the exact date or cross-check if this claim aligns with IEX’s granular daily data. The 269 GW peak itself is plausible (India’s all-time peak in 2026 was 270 GW in May, per IEX), but the **281% bid jump attribution to a single day lacks direct evidence** [confidence: **medium**].

---

**INTERPRETATION ERRORS:**
- *"The exchange was already pricing a squeeze: **prices rose by half in a month while total consumption was lower in September than August**"* — **This misrepresents the causality.** While prices spiked (+50% in DAM, +56% in RTM) and consumption dipped slightly (−4%), the **key driver was *peak demand scarcity*, not aggregate consumption**. The article later clarifies this (e.g., "scarcity looks like... having enough dispatchable supply at peak hours"), but the initial framing conflates **monthly energy consumption trends** (which are stable or declining) with **hourly/peak supply shortages**—the latter being the actual market stress. The data shows **volume cleared dropped 23% in DAM**, not consumption, and the squeeze was about **bid-to-clear ratios**, not total usage [confidence: **high**].

---
**OUTDATED DATA:**
- *"18.205 MT coal stock at domestic power plants on 10 October 2026"* — **This is likely superseded by newer Ministry of Coal data.** The article cites **All India Radio/Indian Masterminds (early October 2026)**, but the **latest Coal Ministry bulletin (e.g., for October–November 2026)** would reflect updated stocks, especially given the **469 rakes/day loaded in 1–10 October** (a 10% increase from September). For real-time tracking, check the **Coal Ministry’s *Weekly Coal Stock Position Report*** (published weekly) [confidence: **high**].

---
**Note:** The article’s reliance on **secondary sources** (e.g., Sahi for CGPL capacity, JM Financial/Mercom for IEX data) increases risk for factual gaps, but no outright contradictions with known macro trends (e.g., 2026 peak demand records). The **2023 Section 11 precedent** claim is speculative ("I found no earlier order aimed at captive plants") and could be verified with a deeper ministry archive search.
