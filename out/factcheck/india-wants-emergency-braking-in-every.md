# Fact/interpretation check — india-wants-emergency-braking-in-every

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-wants-emergency-braking-in-every.html`

Text-SHA1: `f9d2824603afcabd`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "the airbag mandate that came before it was dropped" — The six-airbag mandate was not ultimately dropped; after being deferred from October 2022 to October 2023, the Ministry of Road Transport and Highways made six airbags compulsory for all passenger cars (category M1) effective October 1, 2023. [confidence: high]

INTERPRETATION ERRORS:
- "Applied to the 46.43 lakh cars sold in 2025-26, that is about 3.9 lakh cars with the systems and about 43 lakh without." — The text applies a calendar-year market research penetration rate (8.41% for 2025) directly to a fiscal-year sales figure (46.43 lakh for 2025-26), mixing different temporal periods and definitions of annual sales without adjustment. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- “United States: FMVSS 127 (2024). US will from September 2029” — FMVSS 127 governs brake‑system requirements, not advanced emergency braking. The U.S. AEB rule is issued under FMVSS 126, with compliance dates beginning in 2025‑2026, not 2029. [confidence: high]  
- “In 2023, India recorded 172,890 road deaths.” – Official Ministry of Road Transport & Highways data show total road‑traffic fatalities in 2023 were around 450,000 (≈4.5 lakh), not 172,890. The figure cited is therefore incorrect. [confidence: high]  

**INTERPRETATION ERRORS**  
- “AEB in cars addresses only part of that: those where a car is the vehicle doing the hitting, and those where it hits a pedestrian.” – The article uses rear‑end crash deaths (vehicles hit from behind) to argue AEB will cut those fatalities. AEB systems are designed to prevent forward‑impact collisions; they do **not** mitigate crashes where the car is struck from behind. Thus the causal link between AEB adoption and the cited rear‑end death share is unsupported. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Europe got there in 2024"* — The article states this as fact, but the **EU’s AEB mandate for all new cars (Regulation 2019/2144) began in July 2024**, not a full year earlier (July 2023). The claim conflates the **new car types requirement (July 2022)** with the full rollout date. [confidence: high]

**INTERPRETATION ERRORS:**
- *"~35,000 deaths in 2023 in crashes where a vehicle was hit from behind, about a fifth of all road deaths"* — While the **20% share of deaths** from rear-end crashes is plausible, the claim **overstates AEB’s scope**: AEB only prevents crashes where the **equipped car is the aggressor** (e.g., rear-ending a pedestrian or vehicle). It does **not** address cases where the **other vehicle** (e.g., a truck or motorcycle) is at fault. The article later notes this gap but uses the figure to justify the mandate without clarifying the limitation. [confidence: high]

**OUTDATED DATA:**
- *"~43 lakh cars a year would need emergency braking added, at 2025-26 sales and today’s fitment rate"* — The **2025-26 sales figure (46.43 lakh cars)** is correct, but the **ADAS penetration rate (8.41%)** is based on **calendar-year 2025 data**, while the article applies it to **fiscal-year 2025-26 sales**. This could skew the estimate if penetration varied by quarter. [confidence: medium]
- *"China supplied about 36% of India’s auto-component imports in 2025-26"* — The **ACMA report cited (July 2026)** likely reflects **FY2025-26 data**, but newer **FY2026-27 figures** (e.g., from **SIAM or MoC reports**) may show shifts due to **PLI schemes, tariff changes, or supply chain disruptions**. [confidence: medium]
