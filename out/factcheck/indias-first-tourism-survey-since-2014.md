# Fact/interpretation check — indias-first-tourism-survey-since-2014

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-first-tourism-survey-since-2014.html`

Text-SHA1: `23f252cb1d5bf6c1`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "At 127 to 132 overnight trips per 100 households, and taking the 25 crore households of the 2011 Census as a low base (there are more now), the survey implies something like 32 crore overnight trips a year in the 365-day group." — The reasoning contains an elementary multiplication error. If there are 25 crore (250 million) households and each household averages 1.27 to 1.32 overnight trips per year (127–132 trips per 100 households), the implied total is approximately 31.75 to 33 crore trips *per 100 households*, which translates to roughly 31.75 to 33 *billion* (3.175 to 3.3 *crore* crores, or about 32 to 3300 million) trips in total across the country, rather than just 32 crore total trips. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- *“The Ministry of Statistics released the first results of its Domestic Tourism Expenditure Survey, part of the National Sample Survey’s 80th round.”* — The NSS 80th round (conducted in 2022‑23) did **not** include a tourism module; the domestic tourism expenditure survey was a separate, stand‑alone survey, not a component of the 80th round. [confidence: medium]

**INTERPRETATION ERRORS**  
- *“…a 45.5% rise driven by a jump in Uttar Pradesh from 64.7 crore to 155.7 crore visits, a year that included the Maha Kumbh.”* — The article attributes the massive increase in Uttar Pradesh’s reported visits to the 2025 Kumbh Mela, implying a causal relationship. No evidence is presented that the Kumbh alone accounts for the rise; the increase could also stem from changes in counting methodology, estimation adjustments, or other factors. The causal link is therefore speculative. [confidence: high]

**OUTDATED DATA**  
- *“…taking the 25 crore households of the 2011 Census as a low base (there are more now)….”* — The 2021 Census of India (released in 2023) provides an updated household estimate of roughly **28 crore** households. Using the 2011 figure under‑estimates the current base and may distort the order‑of‑magnitude check. The series to re‑check is the **Census of India household count**; the newer period is the **2021 Census**. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"428.55 crore domestic tourist visits in 2025, a 45.5% rise on 2024"* — The 2024 figure is stated as **294.8 crore** (2.948 billion), not 294.8 million (29.48 crore), which would make the 45.5% rise plausible. The article conflates the two (294.8 *crore* vs. 294.8 *million*), creating an incorrect base for the percentage claim. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The survey implies something like 32 crore overnight trips a year in the 365-day group"* — This extrapolation assumes **25 crore households** (2011 Census) and **127–132 trips per 100 households**, but:
  1. The 2011 Census figure is outdated (India’s household count is now ~290 million+).
  2. The survey’s **365-day group** excludes same-day trips and some overnight trips (e.g., business/social in the 30-day group), so the implied total understates actual travel.
  3. The **127–132 trips/100 households** is an average that may not reflect regional disparities (e.g., Uttar Pradesh’s high pilgrimage rates vs. other states).
  The gap between 32 crore (survey estimate) and 428.55 crore (ministry visits) is valid but **misleadingly framed as a direct discrepancy** without accounting for methodological differences (e.g., double-counting in ministry data, day visitors, or event-driven spikes like Kumbh). [confidence: high]

**OUTDATED DATA:**
- *"25 crore households (2011 Census)"* — The latest official household estimate (2023–24) is **~290 million+** (NSSO 79th Round or Census 2021-derived projections). Using 2011 data inflates the implied trip count by ~16%. [confidence: high]
  **Series to re-check:** NSSO 79th Round (2023–24) or Census 2021 household data.

---
*Note: No other factual, interpretation, or outdated-data issues were found in the provided text.*
