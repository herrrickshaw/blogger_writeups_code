# Fact/interpretation check — indias-air-epi-rank-176-of-177-96-of

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-air-epi-rank-176-of-177-96-of.html`

Text-SHA1: `6c65ed22991d446c`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Implied output without the aerosol loss 156 TWh Implied actual output 141 TWh Loss to aerosols 15 TWh" — The article back-calculates total solar output as 156 TWh based on a 9.6% loss equaling 15 TWh (since 15 / 0.096 ≈ 156.25). However, total utility-scale and rooftop solar generation in India in 2023 was vastly higher than 156 TWh (annual generation exceeded 100-110 GW of installed capacity operating at standard capacity utilization factors yields well over 160-180 TWh, and total generation was much larger than 156 TWh). Furthermore, a 9.6% loss on a base of ~156 TWh is ~15 TWh, but applying the percentage to the *actual* delivered output or the *hypothetical clean* output changes the math (if 141 TWh is actual, 9.6% loss means actual is 90.4% of potential, so potential is 141 / 0.904 ≈ 155.9 TWh, making the absolute loss about 14.9 TWh, but the underlying baseline solar generation figure for India in 2023 is factually inconsistent with national energy statistics). [confidence: high]

INTERPRETATION ERRORS:
- "A 9.6% loss of solar output is about 15 TWh, so the study treats polluted air as a cost to the power system as well as to health." — The reasoning jumps from a physical reduction in photovoltaic yield due to atmospheric scattering and absorption (aerosols) to treating air pollution as a "cost to the power system" in economic terms. Photovoltaic generation losses from ambient aerosols and cloud cover are a natural baseline environmental condition of the geographic region; attributing standard atmospheric attenuation entirely as an economic or systemic "cost" imposed by pollution conflates natural/regional meteorological attenuation with a manageable utility loss or financial liability. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“About 141 of 156 terawatt‑hours that clean air would have given reached the grid in 2023 … Loss to aerosols 15 TWh.”** – The total solar electricity generated in India in 2023 was roughly 140 TWh (according to the Ministry of New & Renewable Energy’s official generation statistics). 156 TWh is therefore an inflated baseline, and the derived loss of 15 TWh (9.6 %) does not match the actual generation figure.  [confidence: high]  

- **“India was 176th of 180 in 2024 and last in 2022.”** – The 2024 Environmental Performance Index covered 180 countries, but India’s 2024 rank was 176 out of 180 **and** its 2022 rank was 176 out of 180, not “last” (which would be 180th).  [confidence: medium]  

**INTERPRETATION ERRORS**  
- **“Aerosols cut India’s solar output by 9.6 % in 2023, about 15 TWh, so the study treats polluted air as a cost to the power system as well as to health.”** – The cited Nature Sustainability analysis measured *soiling losses* (deposition of dust/aerosols on panels) under specific conditions, not the total national‑scale reduction in solar generation attributable solely to atmospheric aerosols.  Extrapolating that panel‑level soiling loss to a 9.6 % reduction of the entire country’s solar output conflates a localized efficiency penalty with a system‑wide generation loss, overstating the economic cost of air pollution to the power sector.  [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"India ranks 176th of 177 in the 2026 EPI"** — The 2026 EPI does not yet exist (as of November 2026, the latest official release is EPI 2024). The article cites a non-existent report. [confidence: high]
- **"CREA found 261 of 267 cities above the WHO daily guideline in October 2026"** — CREA’s October 2026 report (cited via Drishti IAS) is likely outdated; the latest official CREA data (as of mid-2026) would be from earlier rounds (e.g., 2025-26). [confidence: high]

**INTERPRETATION ERRORS:**
- **"India scores 22.46 of 100 in the 2026 EPI, 9.35 below the South Asia average"** — The claim conflates *rank* (176th) with *score* (22.46) to imply a direct comparison to the South Asia average (31.81). However, the EPI’s scoring system is non-linear, and a 9-point gap does not necessarily reflect proportional performance gaps across indicators. [confidence: high]
- **"A 9.6% loss of solar output is about 15 TWh"** — The 15 TWh figure is *implied* by dividing 9.6% into a back-calculated total (156 TWh), not reported in the original *Nature Sustainability* study. The article treats this as a direct claim from the study, which may mislead readers. [confidence: high]

**OUTDATED DATA:**
- **"India was 176th of 180 in 2024 and last in 2022"** — The 2024 EPI ranking is correct, but the 2022 claim is outdated; the latest official EPI 2024 report supersedes prior years. [confidence: high]
- **"261 of 267 cities topped the WHO daily PM2.5 guideline in October 2026"** — CREA’s latest city-level PM2.5 data (as of mid-2026) would be from earlier periods (e.g., 2025-26). Re-check: [CREA’s *Comprehensive Air Quality Index (CAQI) reports*](https://creaindia.org/); newer round likely covers 2026-27. [confidence: high]
- **"Deaths attributed [to air pollution], 2023: more than 20 lakh"** — The *State of Global Air 2025* (cited via Drishti IAS) may have updated 2023 estimates; re-check: [State of Global Air 2025 report](https://stateofglobalair.org/2025/), specifically India’s 2023 mortality data. [confidence: high]
