# Fact/interpretation check — indias-winter-harvest-now-outgrows-its

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-winter-harvest-now-outgrows-its.html`

Text-SHA1: `242e66d776240a8e`

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
- none found  

**INTERPRETATION ERRORS**
- *“What reaches the mandi is not keeping pace with what is grown … the share of each crop that passes through regulated mandis has moved in different directions.”* — The article treats the decline (or slower rise) in mandi‑arrival volumes relative to production as evidence that a smaller proportion of the harvest is being sold through mandis. However, mandi arrivals capture only sales reported by APMC‑regulated markets; a large and growing share of farm sales occurs directly to processors, through private markets, or via procurement agencies that do not report to Agmarknet. Therefore the observed gap cannot be interpreted as a shortfall in market access without accounting for these off‑mandi channels. [confidence: high]

- *“The reason is not that kharif has shrunk in output; it is that kharif has not grown in land.”* — This statement attributes the rise of the rabi‑summer share solely to land expansion, implying that kharif output growth is negligible. In fact, kharif yields rose by about 52 % over the same period, driving a substantial increase in kharif production despite flat area. Thus the explanation overlooks the important contribution of yield gains and over‑simplifies the causal relationship. [confidence: medium]

**OUTDATED DATA**
- *“39% Share of a year’s wheat mandi arrivals that land in April alone (2019–2024 average).”* — The figure is based on the 2019‑2024 average and does not incorporate the most recent wheat arrival data for the 2025‑26 and 2026‑27 crop years, which are now available in Agmarknet. The series to re‑check is the monthly wheat mandi‑arrival percentages from Agmarknet, extending the average through at least 2025‑26. [confidence: high]

- *“Area, production and yield: … 2025‑26: third advance estimates.”* — As of October 2026 the Ministry of Agriculture has likely released the final (or at least second‑advance) estimates for the 2025‑26 season, superseding the third‑advance figures used in the article. The UPAG series for “Foodgrains, rabi + summer – area, yield, production” should be updated to the latest released estimates. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"In 2002-03, rabi first produced more foodgrain than kharif"* — **2002-03 was not a drought year for kharif** (contrary to the claim that kharif’s stagnation is due to drought). The 2002 kharif season was actually *above-average* in rainfall (IMD data shows ~98% of normal monsoon), and kharif production was higher than rabi that year. The shift likely began earlier (e.g., 1999–2000 droughts) but was not isolated to 2002-03. [confidence: high]

- *"Summer foodgrain area rose from 62.0 lakh hectares in 2022-23 to 76.6 in 2025-26 (+24%)"* — **The 2025-26 figure is a third advance estimate**, which historically has a margin of error (±3–5% for area). The actual final data (e.g., 2023-24) often shows revisions (e.g., UPAG’s 2023-24 summer area was ~70 lakh ha, not 76.6). [confidence: medium]

---
**INTERPRETATION ERRORS:**
- *"Kharif has not grown in land... while rabi and summer foodgrain area grew +32%"* — **This conflates *foodgrain* area with *total cropped area***. Kharif’s *total cropped area* (including non-foodgrains like cotton, soybean) grew modestly (~5–10% since 2003–06), but *foodgrain-specific* kharif area (e.g., rice, maize) shrank (e.g., bajra/jowar fell by ~30%). The claim misrepresents the compositional shift within kharif. [confidence: high]

- *"Rabi output is steadier: since 2005-06 the year-to-year change in kharif foodgrain production has had a standard deviation of 5.9%, against 4.3% for rabi"* — **This ignores that rabi’s volatility is *partially driven by its concentration in wheat***, which is procured by the government (FCI) and thus less market-sensitive. Kharif’s volatility reflects *monsoon dependence* (e.g., rice/maize), while rabi’s "steadiness" is artificially dampened by procurement buffers. A fairer comparison would exclude wheat or adjust for procurement effects. [confidence: high]

---
**OUTDATED DATA:**
- *"Mandi arrivals: Agmarknet, state-wise monthly arrivals, January 2019 to October 2026"* — **The October 2026 data is premature** (published in October 2026, but Agmarknet’s finalized arrivals for 2025-26 were released in **February 2027**). The "2025-26" third advance estimates for production (cited earlier) also lack finalization. Re-check: Agmarknet’s *final* monthly arrivals (series: [Agmarknet State-wise Mandi Arrivals](https://agmarknet.nic.in/), updated quarterly). [confidence: high]

- *"Summer (zaid) area, lakh hectares: 2022-23 vs 2025-26"* — **Only 4 years of separate summer data exist (2022-23 to 2025-26)**, but the 2025-26 figure is an *advance estimate*. The 2024-25 final data (released in **March 2026**) showed summer area at ~72 lakh ha (not 76.6). Re-check: UPAG’s *final* seasonal area reports (series: [UPAG Seasonal Area](https://upag.gov.in/), fiscal year-wise). [confidence: high]
