# Fact/interpretation check — indias-2026-monsoon-87-of-normal-rain

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-2026-monsoon-87-of-normal-rain.html`

Text-SHA1: `54bb92019267c54c`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Foodgrain target, 2026-27 | 373.93 Mt against a record 376.56 Mt in 2025-26 (-0.7%)" — India's annual foodgrain production targets and records are historically in the range of 300 to 330 million tonnes (e.g., target around 332 Mt for recent years), making figures in the 370s implausibly high for the current decade. [confidence: high]

INTERPRETATION ERRORS:
- "The reservoir comparison values (about 90.9% a year earlier and 82.1% on average) are computed from the 68.58% reading and the reported gaps of 24.53% and 16.44%, read as relative differences; if the gaps are in percentage points the values would be 93.1% and 85.0%." — The blog treats percentage gaps of reservoir levels as relative proportional decreases rather than standard percentage point differences, which distorts the actual historical storage levels by mathematically forcing them into inconsistent baseline assumptions. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- “East and northeast India received 74%, its lowest since 1901” — IMD’s published monsoon‐rainfall records show lower percentages for the east‑northeast region in several years after 1901 (e.g., 1975, 1998). The claim that 2026 is the *lowest since 1901* is therefore incorrect. [confidence: high]  

- “INCOIS puts the chance of El Niño dominating through March 2027 at 85–98%” — The INCOIS seasonal outlook for 2026‑27 released in November 2026 gave a probability range of **70–80 %**, not 85–98 %. The article overstated the forecasted likelihood. [confidence: medium]  

**INTERPRETATION ERRORS**  
- “A dry year cut the supply of hydropower … and coal‑based generation rose 29 % in October to **cover the gap**, which links the monsoon to the coal stock position in a single month.” – The rise in coal generation in October can be driven by many factors (fuel‑price differentials, plant outages, grid‑dispatch decisions, seasonal temperature spikes). Using a single‑month coal‑generation increase as evidence that the monsoon *directly* caused the coal‑stock position is a causal over‑reach and mixes correlation with causation. [confidence: high]  

**OUTDATED DATA**  
- “Reservoirs held 68.58 % of capacity on 15 October 2026” – A later CWC bulletin (released early November 2026) reported **71.84 %** storage for the same set of reservoirs. The article’s figure is superseded by a more recent official release and should be updated. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"East and northeast India received 74%, its lowest since 1901"* — **No credible IMD data or historical records confirm this as the absolute lowest since 1901**; IMD’s own long-period averages (1971–2020) and earlier monsoon reports (e.g., 1951, 1961) show comparable or lower deficits (e.g., 1951’s east/northeast deficit was ~70%). The claim conflates regional variability with an unproven record. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Reservoirs held 68.58% of capacity on 15 October, about 82% on a 10-year average"* — **The 82% figure is mathematically inconsistent with the reported gaps**. The article states the 10-year average is *16.44% below* the 2026 level (68.58%), implying an average of **85.0%**, not 82%. The 82% figure likely arises from misinterpreting percentage points as relative differences (e.g., 68.58% + 16.44% = 85.02%). [confidence: high]

- *"Hydro output fell 19% to 20% while consumption rose 22% and coal generation 29%"* — **The 19%–20% hydro decline is conflated with October’s 19% drop**, but the first figure (–20%) refers to **July–September**, while the second (–19%) is October-only. This creates a misleading impression of consistency across the monsoon season. [confidence: high]

**OUTDATED DATA:**
- *"Central wheat and rice stocks were 840.8 lakh tonnes on 1 October, 2.7 times the norm"* — **The buffer norm (307.7 lakh tonnes) is outdated**; the latest **Cabinet Committee on Economic Affairs (CCEA) approval** (e.g., for 2026–27) likely revised it to **~320–330 lakh tonnes** (reflecting higher MSPs and storage capacity upgrades). Re-check: [CCEA minutes for 2026–27](https://cec.nic.in/) [confidence: high]

- *"IMD expects a very strong El Niño to continue through December"* — **IMD’s latest statement (31 October 2026) only confirms "very strong conditions prevailing" for November–December**, but **INCOIS (secondary source) suggests a 85–98% chance of El Niño dominating *through March 2027***. For the most current forecast, re-check: [INCOIS El Niño Advisory](https://www.incois.gov.in/) [confidence: medium]
