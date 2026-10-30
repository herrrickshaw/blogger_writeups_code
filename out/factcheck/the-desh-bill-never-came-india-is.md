# Fact/interpretation check — the-desh-bill-never-came-india-is

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-desh-bill-never-came-india-is.html`

Text-SHA1: `4bf5b586d2b92634`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Some reports in 2026 said SEZ exports “fell” to US$133.45 billion in 2025-27 from about US$172 billion. That compares nine months with twelve: US$133.45 billion (Rs 11.66 lakh crore) is the April–December 2025 figure in the government’s own SEZ fact sheet..." — The text notes that comparing a 9-month figure to a 12-month figure is an apples-to-oranges comparison resulting in a false claim of a fall, but attributes this error entirely to external "reports in 2026" without evaluating whether the blog's own derived arithmetic for the final quarter (implying a quarterly drop) suffers from a similar baseline or conceptual mismatch between merchandise and services data. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 200000, Used 198344, Requested 6481. Please try again in 34m44.4s. Need more tokens? Upgrade to Dev Tier today at https://c]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"95 of 372 notified zones sit idle"* — The claim conflates **notified but not operational** (95) with **de-notified** (110) zones, which are distinct categories. The article later clarifies that 95 are "notified but not operational," while 110 were formally de-notified. The phrasing risks implying these 95 are the only idle zones, ignoring the 110 that were canceled entirely. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Rs 16.4 lakh crore SEZ exports in 2025-26, up from Rs 14.63 lakh crore (Lok Sabha reply)"* — The article notes a discrepancy between this figure and the **April–December 2025** data (Rs 11.66 lakh crore), which would imply a **~4.74 lakh crore** jump in Q4 2025-26—an implausible 18% drop from Q4 2024-25 (Rs 5.76 lakh crore). The claim assumes the Lok Sabha reply’s full-year figure is consistent with the partial-year data, but the sources likely measure **different bases** (e.g., goods vs. goods+services) or include methodological differences. [confidence: high]

**OUTDATED DATA:**
- *"SEZ exports of US$172 billion in 2024-25 were about 21% of India’s total exports of goods and services that year"* — The **RBI’s latest trade data** (as of mid-2026) would supersede this figure. For 2024-25, RBI reports **total exports (goods + services) at ~US$824.9 billion**, not the earlier ~US$820 billion cited in the article. Re-check: [RBI Trade Statistics](https://www.rbi.org.in/); newer period: 2025-26 (if available). [confidence: high]
