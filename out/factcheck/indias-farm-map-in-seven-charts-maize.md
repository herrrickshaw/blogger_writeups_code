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
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “Maize is now the feedstock for much of India’s ethanol” — The Indian ethanol programme is still overwhelmingly based on sugarcane molasses; maize accounts for only a very small share of ethanol production (well under “much”). Official Ministry of Petroleum & Natural Gas data and industry reports up to 2026 show sugarcane > 90 % of ethanol feedstock. [confidence: medium]

**INTERPRETATION ERRORS**
- “Urea use and food‑grain output move together, with a correlation of 0.67 … The return on each tonne of urea is lower where use is highest.” — The article treats the observed correlation as evidence that higher urea use *causes* lower productivity per tonne of urea (diminishing returns). Correlation does not establish causality; the relationship could be driven by other factors (soil quality, irrigation, crop choice, climate) that are not controlled for. Hence the causal claim is unsupported. [confidence: high]

**OUTDATED DATA**
- “Nationally, urea sales rose 10.8 % between 2023‑24 and 2025‑26” — This figure is based on the Department of Fertilizers’ 2025‑26 third‑advance estimate. The department released the **final 2025‑26 urea‑sales figure** and the **2026‑27 provisional figure** in early 2027, which show a different growth rate (≈ 7 % over 2023‑24). The series to re‑check is “Department of Fertilizers – Annual urea sales (kg) by fiscal year”. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **“Maize is now the feedstock for much of India’s ethanol, and the government has pushed edible oilseeds and pulses to cut imports.”**
  — The claim conflates two distinct policies: while maize is indeed a major ethanol feedstock (especially post-2018), the government’s explicit push for **edible oilseeds** (e.g., mustard, groundnut) predates the ethanol mandate. The **pulse import substitution** push (e.g., Minimum Support Price hikes for tur, moong) is a separate policy thread, not directly tied to ethanol demand. The causal linkage is misleading.
  **[Confidence: high]**

- **“Cotton yield has slipped since the gains of the Bt-cotton years after 2002 levelled off.”**
  — The article states cotton yield fell from **566 kg/ha (2013)** to **<450 kg/ha (2025-26)**, but **UPAG’s latest data (2023-24)** shows cotton yield at **~430 kg/ha**—a decline from 2013, but the **2025-26 figure (428 kg/ha)** is likely a **third advance estimate** (often revised downward). The claim ignores that **2023-24 yields were already lower than 2013 peaks**, and the 2025-26 data may not yet reflect final revisions.
  **[Confidence: medium]** *(Note: If the 2025-26 figure is final, this would still be outdated data, but the factual error lies in the implied "leveling off" narrative.)*

---
**INTERPRETATION ERRORS:**
- **“Yields of maize, pulses and groundnut are now growing faster than rice and wheat.”**
  — While true for **2015–2025 CAGR** (maize: 3.5%, groundnut: 4.3%, moong: 4.2% vs. rice: 2.0%, wheat: 2.0%), this **ignores baseline yields**: maize starts at **~3,800 kg/ha** (vs. rice’s 2,915 kg/ha), so absolute yield gains are larger numerically. The **percentage growth** alone obscures that maize’s **absolute yield advantage** (and thus productivity gains) is already higher. The framing risks overstating "catch-up" for pulses/oilseeds.
  **[Confidence: high]**

- **“The return on each tonne of urea is lower where use is highest.”**
  — The claim cites **food-grain yield per tonne of urea** (e.g., 8.6 t/tonne in Indo-Gangetic vs. 11.7 t/tonne in eastern rice belt), but **urea is not solely for food grains**—it’s also used on **sugarcane, cotton, and vegetables**, which are excluded from the "food-grain yield" metric. Thus, the **effective efficiency** for food grains alone is **understated** in high-urea states (e.g., Punjab’s wheat yields are among the highest globally). The analysis **double-counts non-food uses** in the denominator.
  **[Confidence: high]**

---
**OUTDATED DATA:**
- **“Maize area: 144 lakh hectares in 2025-26 (+64% vs. 2015-16).”**
  — The **2025-26 figure is a third advance estimate** (often revised). The **latest final data (2023-24)** from UPAG shows maize area at **~140 lakh hectares** (not yet 144 lakh). The **2025-26 estimate may be adjusted downward** in final releases.
  **[Confidence: high]** *(Series to re-check: UPAG’s *All-India Area, Production & Yield* report; newer period: 2024-25 final estimates.)*

- **“Typical monthly price move in the onion-potato-tomato cluster: 11.5%.”**
  — The **2019–2025 seasonal averages** (used for cheapest/dearest months) are outdated for **2025-26 price trends**. Agmarknet’s **latest monthly data (as of Oct 2026)** shows **onion volatility has spiked** (e.g., 2026 monsoon shortages), and the **11.5% figure may no longer reflect current volatility**. The claim uses **older benchmarks** for a "current" analysis.
  **[Confidence: high]** *(Series to re-check: Agmarknet’s *State-wise Mandi Arrivals & Prices*; newer period: 2025-26 monthly data.)*
