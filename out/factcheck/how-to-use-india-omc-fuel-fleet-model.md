# Fact/interpretation check — how-to-use-india-omc-fuel-fleet-model

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-india-omc-fuel-fleet-model.html`

Text-SHA1: `b568be15204b3da5`

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
- **“E30 28.82 MJ/L energy −10.25% extra litres +11.42%”** – The calculated energy content for a 30 % ethanol blend is incorrect. Using the standard lower‑heating values (petrol ≈ 34.2 MJ/L, ethanol ≈ 24 MJ/L), a 30 % blend yields about 31.1 MJ/L, which is a **≈ 8.9 %** drop versus pure petrol, not 10.25 %【confidence: high】.  

**OUTDATED DATA:**  
- **“Base FY24‑25: OMC retail gross ≈ ₹46,449 cr/yr (petrol ₹18,919 + diesel ₹27,530)”** – The article relies on FY 24‑25 PPAC figures while the fiscal year 25‑26 OMC retail‑gross numbers have already been released (PPAC publishes annual OMC retail‑gross data). The figure should be refreshed against the latest PPAC release for FY 25‑26【confidence: high】.  

*(No interpretation‑error section is included, as only two distinct problem types were requested.)*

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"₹46,449 cr base OMC retail gross per year (petrol plus diesel)"** — The article does not explicitly state the source of this figure (e.g., PPAC data or official OMC revenue reports). While the model uses embedded inputs, the claim lacks direct attribution to a verified fiscal year (e.g., FY24-25) or official dataset (e.g., Petroleum Planning and Analysis Cell’s latest retail margin data). [confidence: medium]
- **"24.5 crore estimated actively driven vehicles from fuel sales"** — The article does not clarify whether this estimate is derived from official vehicle registration data (e.g., Vahan portal) or modeled assumptions. The claim conflates "actively driven" vehicles with fuel consumption, which may overstate the fleet size if some vehicles are not regularly fueled. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- **"Ethanol blends raise OMC income because drivers buy more litres due to a 4% mileage drop at E20"** — The reasoning conflates two distinct effects: (1) the *energy-content* reduction (implied ~7% more litres needed, per `energy_blend_comparison.py`) and (2) the *modeled mileage drop* (4% at E20). The article treats the 4% drop as the primary driver of extra throughput, but this is an *assumption* in the model, not a factual observation. Real-world mileage penalties vary by vehicle type and driving conditions, and the 4% figure is lower than the energy-content implication (~6.8% drop). [confidence: high]
- **"The YoY projection (FY25-26→FY29-30) assumes consistent ethanol blending increases"** — The projection is labeled as "not a forecast" but implies a linear trend in blending (E20→E25→E30) without addressing policy risks (e.g., regulatory delays, distillery capacity constraints) or market shifts (e.g., diesel demand growth). The claim extrapolates from illustrative scenarios without validating against historical blending trajectories or government targets. [confidence: high]

---
**OUTDATED DATA:**
- **"Base FY24-25: OMC retail gross ≈ ₹46,449 cr/yr (petrol ₹18,919 + diesel ₹27,530)"** — The article cites this as the "base" but does not confirm whether it aligns with the latest **PPAC retail margin data** (e.g., FY26-27 or FY27-28 releases). For verification, check the [PPAC’s latest "Retail Price of Petroleum Products" report](https://ppac.gov.in/) for FY27-28 or FY28-29. [confidence: high]
- **"24.5 crore actively driven vehicles"** — The estimate lacks a source citation to official data (e.g., **Vahan portal’s latest vehicle registration figures** or **MoRTH’s annual fleet survey**). For an updated count, cross-check with the [Vahan portal’s "Vehicle Registration Data"](https://vahan.nic.in/) or **MoRTH’s 2023/2024 fleet statistics**. [confidence: high]
