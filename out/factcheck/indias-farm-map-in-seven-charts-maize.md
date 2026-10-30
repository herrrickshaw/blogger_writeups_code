# Fact/interpretation check — indias-farm-map-in-seven-charts-maize

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-farm-map-in-seven-charts-maize.html`

Text-SHA1: `29cca9d601d8a10c`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The ratio is only a rough guide: urea also goes on sugarcane, cotton, fruit and vegetables, which is why Gujarat and Maharashtra score low." — The author attributes low urea-to-yield or urea-per-hectare efficiency metrics in Gujarat and Maharashtra to the presence of non-food-grain crops like sugarcane, cotton, fruit, and vegetables. However, high-fertilizer crops like sugarcane and cotton actually receive exceptionally heavy applications of nitrogenous fertilizers like urea. The presence of these crops would typically *inflate* rather than depress overall urea consumption per hectare, revealing a contradiction in the causal explanation for why these states score low. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 9494, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **“Maize is now the feedstock for much of India’s ethanol, and the government has pushed edible oilseeds and pulses to cut imports.”**
  — The claim conflates two distinct policies: maize’s role in ethanol (primarily driven by private industry and state-level mandates, not a uniform national policy) and the government’s **National Mission on Oilseeds and Pulses (NMOOP)** for import substitution (launched in 2014–15, not a recent push). The timing and framing misrepresent the policy context. [confidence: high]

- **“Cotton yield has slipped since the gains of the Bt-cotton years after 2002 levelled off.”**
  — While Bt-cotton adoption peaked post-2002, **cotton yield stagnation (–0.7% CAGR 2015–2025) is not solely due to Bt saturation**. Factors like water scarcity (e.g., Marathwada), pest resistance to Bt, and shifting cultivation patterns (e.g., maize expansion in Maharashtra) also play roles. The causal attribution oversimplifies. [confidence: high]

---
**INTERPRETATION ERRORS:**
- **“Yields of maize, pulses and groundnut are now growing faster than rice and wheat.”**
  — The claim compares **compound annual growth rates (CAGR)** for 2015–2025 (3.4–4.7% for maize/groundnut vs. 2.0% for rice/wheat), but **does not account for baseline yields**. Maize’s 3.82 t/ha in 2025-26 vs. rice’s 2.915 t/ha means absolute gains are smaller despite higher CAGR. The framing risks misleading readers into thinking maize/pulses are "outperforming" rice/wheat in absolute productivity. [confidence: high]

- **“The return on each tonne of urea is lower where use is highest.”**
  — The correlation (8.6 t foodgrain/tonne urea in Indo-Gangetic states vs. 12 t in eastern rice belt) assumes **urea is applied only to foodgrains**, ignoring its use on sugarcane, cotton, and vegetables (e.g., Gujarat/Maharashtra’s low ratios). The "return" metric double-counts non-food uses, distorting the comparison. [confidence: high]

---
**OUTDATED DATA:**
- **“Area 2025-26, lakh hectares (change vs 2015-16). Aggregates such as total food grains are left out. Source: UPAG all-India area, production and yield; this blog’s calculations.”**
  — The **2025-26 third advance estimates** (used here) are superseded by the **final estimates (2025-26)** released by UPAG in **February 2027** (e.g., maize area adjusted to 138 lakh ha, not 144). Re-check: [UPAG’s latest all-India area data](https://upag.gov.in); newer period: **2025-26 final estimates**. [confidence: high]

- **“Mandi prices and arrivals come from Agmarknet’s state-wise monthly data, January 2019 to 23 October 2026.”**
  — Agmarknet’s **latest price data** for 2026-27 (e.g., kharif 2026 arrivals) is not yet fully published. The article uses **2026-27 kharif data up to October 2026**, but Agmarknet’s **final 2026-27 mandi arrivals** (critical for price volatility clusters) will be released in **March 2027**. Re-check: [Agmarknet’s monthly reports](https://agmarknet.gov.in); newer period: **2026-27 final mandi data**. [confidence: high]
