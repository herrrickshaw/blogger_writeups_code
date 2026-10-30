# Fact/interpretation check — how-to-use-fci-warehouse-mspvsmsv-grain

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-fci-warehouse-mspvsmsv-grain.html`

Text-SHA1: `429d1b8b0ec017e5`

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
- **“Evidence from the run: the mandi table shows 92 % of bajra and 84 % of moong market reports below MSP on 23 July 2026, against 19 % for wheat.”** – The article treats a single‑day snapshot (23 July 2026) as if it represents the overall market condition for the whole marketing year. Prices can fluctuate widely day‑to‑day; a one‑day sample cannot reliably support a claim about the general effectiveness of the MSP. This is an apples‑to‑oranges comparison that overstates the evidence. [confidence: high]  

- **“The holding‑economics model produced a clear result: for every commodity tested, estimated storage and financing cost exceeded price appreciation over 12, 24 and 36 months, which bears directly on the ‘why not buy and hold’ question behind MSV.”** – The model’s output shown in the article only presents a 12‑month CAGR and a single carry‑cost figure; it does not actually calculate 24‑ or 36‑month returns. Moreover, the conclusion that MSV cannot work rests on specific assumptions about storage tariffs, financing rates and the WPI price series, which are not universally applicable. The claim extrapolates beyond the data and the model’s stated scope. [confidence: high]  

**OUTDATED DATA**  
- **“MSP series, 2010‑11 onward” (table shows MSP for 2025‑26).** – The Ministry of Agriculture released the MSP for the 2026‑27 season in August 2026. The repository’s MSP series stops at 2025‑26, so the “latest” MSP figures are outdated. The series to re‑check is the official “Ministry of Agriculture & Farmers’ Welfare – Minimum Support Price (MSP) notifications” for 2026‑27. [confidence: medium]  

- **“mandi_vs_msp_20260723.csv … built from the 23 July 2026 Agmarknet daily feed.”** – Agmarknet publishes daily market price data; data for August and September 2026 are already available at the time of the article (19 Oct 2026). Relying on a July‑23 snapshot makes the price‑vs‑MSP comparison outdated. The dataset to re‑check is the Agmarknet “Daily Market Prices” series for the period July – October 2026. [confidence: medium]

## Mistral open-mistral-nemo

Here’s the structured fact-checking report based on the provided article:

---

**FACTUAL ERRORS:**
- *"17,247 mandi records behind that comparison"* — The claim is plausible but **cannot be independently verified** without access to the raw Agmarknet data (23 Jul 2026 feed) referenced in `MANIFEST.md`. While the number aligns with the stated methodology (16 crops × 1,080 records/crop ≈ 17,280), the exact count lacks a cited official source (e.g., Agmarknet’s daily summary) or cross-checkable transparency. [confidence: **medium**]
- *"92% of bajra and 84% of moong market reports below MSP on 23 July 2026"* — The **sample sizes are extremely small** (bajra: 84 records; moong: 161 records), making the percentages statistically unreliable for broad policy conclusions. Even if accurate, the article does not disclose confidence intervals or note the potential for outliers skewing the result. [confidence: **high**]

---

**INTERPRETATION ERRORS:**
- *"The holding-economics model produced a clear result: for every commodity tested, estimated storage and financing cost exceeded price appreciation over 12, 24, and 36 months"* — **Overgeneralizes from stylized assumptions to real-world outcomes**. The model’s "carry costs" combine **arbitrary storage tariffs** (e.g., FCI’s ~Rs 1,000/quintal/year for wheat) and **WPI-based financing rates**, which may not reflect:
  1. **Private storage costs** (often lower for bulk buyers).
  2. **Opportunity costs** (e.g., alternative investments for farmers vs. FCI).
  3. **Price volatility** (the model assumes mean reversion, ignoring crashes like 2023’s wheat spike).
  The verdict conflates **theoretical economics** with **empirical viability** without addressing hedging strategies (e.g., futures markets) or regional storage disparities. [confidence: **high**]
- *"The mandi table shows 92% of bajra and 93% of ragi market reports below MSP"* — **Apples-to-oranges comparison**. The article ignores that:
  - **Ragi (14 records)** and **sunflower (2 records)** are excluded from the trimmed table but likely drove the 93% figure. The claim implies a robust trend, but the **sample size is too small** to generalize (statistical power is insufficient for policy implications).
  - **Bajra’s 92% below-MSP** may reflect **supply glut** (e.g., 2025’s record production) rather than systemic MSP failure, yet the article treats it as evidence against MSP effectiveness without contextualizing production trends. [confidence: **high**]

---

**OUTDATED DATA:**
- *"14 crops in the MSP series, 2010-11 onward"* — The **latest official CACP MSP series** (as of mid-2024) includes **23 crops** (e.g., added maize, soybeans, and pulses like masur in 2023–24). The article’s cutoff (2010–11) is outdated; the **2025–26 MSP list** (released 12 May 2025) should be referenced instead. [confidence: **high**]
  - **Series to re-check**: [CACP MSP notifications](https://cacp.gov.in/); newer period: **2025–26 to 2026–27**.
- *"MSP 2025-26 market reports modal median % reports below MSP"* — The **2025–26 MSP values** (e.g., wheat Rs 2,425/quintal) are correct for the marketing year, but the **2026–27 MSPs** (announced 12 May 2026) differ slightly (e.g., wheat Rs 2,585/quintal). The article does not clarify if the mandi data (23 Jul 2026) uses the **old or new MSP benchmark**. [confidence: **medium**]
  - **Series to re-check**: [Agmarknet daily bulletins](https://www.agmarknet.nic.in/); newer period: **post-12 May 2026 MSPs**.

---
**Note**: No stylistic or formatting issues were flagged as per instructions. The article’s caveats (e.g., "unaudited figures," "stylized models") are correctly disclosed but do not absolve the interpretation gaps noted above.
