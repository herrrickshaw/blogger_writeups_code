# Fact/interpretation check — biogas-manure-2065-lakh-tonnes-sold-rs

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/biogas-manure-2065-lakh-tonnes-sold-rs.html`

Text-SHA1: `46e70e3f7cd25369`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "122 are current and 27 lapsed on 14 November 2026." — The text states the article was analysed on 18 November 2026, and that gazette entries authorise bulk sales for three years. An order dated 14 November 2023 would lapse on 14 November 2026, making the date internally consistent with the article's timeline, but the article describes future events occurring after the current real-world date (as the training cutoff and present time precede late 2026). [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“27 lapsed on 14 November 2026”** – The article first says the 149 gazette entries run from 14 Nov 2023 to 27 Jul 2026 and that 27 entries “lapsed on 14 November 2026.” Later it states the 27 entries “lapsed with the November 2023 order” and the table lists them as “Expired, order of 14 Nov 2023.” The correct lapse date is 14 Nov 2023, not 2026. [confidence: high]  

**INTERPRETATION ERRORS**  
- **“Liquid manure is 65 % of the 20.65 lakh tonnes”** – The article adds the three manure types to a total of 2,065,033 t and reports liquid FOM as 1,089,019 t. The share is 1,089,019 ÷ 2,065,033 ≈ 52.7 %, not 65 %. The claim inflates the proportion of liquid manure, misleading the reader about its dominance. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"122 of 149 gazette clearances are current; 27 lapsed on **14 November 2026**"*
  – The article states the 27 entries lapsed on **14 November 2023** (as per the table and text), not 2026. The claim of lapses in November 2026 contradicts the source data (Gazette orders listed up to 27 July 2026) and the timeline provided. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Sales of biogas manure rose from 56,059 tonnes in 2023-24 to **16.73 lakh tonnes in 2025-26**—a **sixfold increase in 2024-25 and fivefold in 2025-26**."*
  – The claim conflates **year-on-year growth** with **multiplicative jumps** without clarifying that 2025-26 is a **partial year (10 months)**. The 16.73 lakh tonnes figure is for **28 Feb 2026**, not a full fiscal year, making the "fivefold" claim misleading for 2025-26. [confidence: high]

**OUTDATED DATA:**
- *"Uttar Pradesh produced a third of the manure reported, **9.64 lakh tonnes of 29.57 lakh**."*
  – The production data is sourced from a **Rajya Sabha starred question (10 March 2026, Annexure II)**, but newer official updates (e.g., **2026-27 fiscal year data** or **quarterly reports post-March 2026**) may exist. Re-check: **Department of Fertilizers’ latest annual report or Ministry of Agriculture’s biogas/manure statistics** for 2026-27. [confidence: medium]
