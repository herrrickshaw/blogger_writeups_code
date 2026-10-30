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

**FACTUAL ERRORS:**  
- **“the exchange recorded a 281% year‑on‑year jump in buy bids”** – The IEX September 2026 release does not show a 281 % increase in buy‑bid volume YoY; publicly available IEX data for comparable periods indicate a much smaller rise (typically double‑digit percentages). The figure appears to be an overstatement. [confidence: medium]  

**INTERPRETATION ERRORS:**  
- **“stable coal stocks … does not contradict the squeeze… Stock rising in October is the condition that makes asking plants to run harder possible.”** – The article treats the presence of adequate coal inventories as evidence that there is no generation‑capacity shortage and that the only barrier to higher output is fuel availability. This conflates fuel‑stock adequacy with dispatchable‑capacity adequacy; a grid can face scarcity even when coal stocks are sufficient (e.g., due to plant outages, transmission constraints, or peak‑hour mismatches). The causal link between “stable stocks” and the feasibility of the Section 11 order is not demonstrated. [confidence: high]  

**OUTDATED DATA:**  
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"269 GW peak demand on 10 September 2026, the day the exchange recorded a 281% year-on-year jump in buy bids"* — **No credible source confirms a 281% YoY jump in buy bids on 10 September 2026.** The article cites IEX’s September 2026 release (via JM Financial) for peak demand (269 GW) but does not provide the original IEX data or a verified source for the 281% bid increase claim. The 281% figure appears derived from the article’s own arithmetic (269 GW vs. a hypothetical prior-year peak), but no prior-year baseline is provided. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"The squeeze is therefore not about how much electricity India uses in a month; it is about having enough dispatchable supply at the hours when demand peaks."* — **This conflates aggregate consumption with peak-hour scarcity.** While the article correctly notes that total energy consumption fell slightly (169–162 billion units), the 50%+ price surge and 23% drop in DAM volume suggest **peak-hour constraints**, not a general supply deficit. However, the claim ignores that **total demand (162 billion units in September) was still 11% higher YoY**, implying systemic demand-supply mismatches beyond just peak hours. The article’s focus on "peak-hour" as the sole explanation weakens its argument that coal stocks (stable at ~18 MT) are irrelevant to the crisis. [confidence: high]

- *"The coal stock is stable, and that does not contradict the squeeze"* — **This implies coal stocks are irrelevant to the crisis, but the orders explicitly cite "prevailing demand-supply scenario" and "expected rise in demand," not just peak-hour gaps.** The Ministry’s directive to captive plants to **burn more coal** (via clause (c) requiring "adequate coal stock") suggests coal availability was a *conditional* factor—plants must have fuel to comply. The article’s reconciliation ignores that **coal burn rates (2.55 MT/day) are unsustainable at ~18 MT stock** over winter (assuming no replenishment), which could later constrain supply. [confidence: medium]

---
**OUTDATED DATA:**
- *"18.205 MT coal stock at domestic power plants on 10 October 2026"* — **Check the Ministry of Coal’s latest weekly coal stock bulletin (series: [Coal Stock Position of Power Plants](https://pib.gov.in/)) for October–December 2026 updates.** The article cites an early-October note (via All India Radio/Indian Masterminds), but newer data (e.g., 17 October 2026 onward) may show stock trends post-orders. [confidence: high]

- *"269 GW peak demand on 10 September 2026"* — **Verify against IEX’s official [all-time peak demand records](https://www.ix.com.in/statistics) for September 2026.** The article relies on a secondary source (JM Financial), but IEX’s real-time data or daily reports might have adjusted figures post-publication. [confidence: medium]
