# Fact/interpretation check — how-to-use-vehiclefuelmileage-running

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-vehiclefuelmileage-running.html`

Text-SHA1: `85e8ab4cad481f8a`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Inputs: petrol Rs 102.12/L, diesel Rs 95.20/L, CNG Rs 83.09/kg, electricity Rs 10.6/kWh blended" (under "Cost per km, Delhi prices") — In Delhi, diesel has never retailed at Rs 95.20/litre (actual Delhi diesel prices have ranged around Rs 87.62–89.62/litre due to Delhi's lower 16.75% VAT rate), petrol is around Rs 94.72/litre, and IGL retail CNG in Delhi has stayed around Rs 75–76.59/kg. Diesel at Rs 95.20/litre and CNG at Rs 83.09/kg contradict Delhi's actual retail fuel price structure. [confidence: high]

INTERPRETATION ERRORS:
- "Same-model petrol->CNG mean distance uplift: +40.3% (11 nameplates)" — This is an apples-to-oranges comparison of non-equivalent units. Petrol fuel economy is measured volumetrically in km per litre, whereas CNG fuel economy is measured gravimetrically in km per kilogram. Because 1 kg of CNG contains substantially more energy (~50 MJ/kg) than 1 litre of petrol (~32–34 MJ/L), comparing km/kg directly to km/L does not represent a true vehicle efficiency or distance uplift. [confidence: high]
- "The same data showed the E20 effect on an average petrol car: 16.67 kmpl falls to about 16.0 kmpl at a 4% drop." — Extrapolation beyond what the data shows. The 2020 SIAM BS-VI certification dataset records certified test results run on standard regulatory reference fuel (E0/E5). The 4% reduction is an external user-specified modeling haircut, not an empirical result derived or demonstrated by the SIAM declaration dataset. [confidence: high]

OUTDATED DATA:
- "The SIAM declaration dataset is from passenger vehicles as on 1 April 2020; it has only 11 CNG, 8 hybrid and 1 electric entries, so those means are thin." — Bureau of Energy Efficiency (BEE) / SIAM Corporate Average Fuel Economy (CAFE) compliance and passenger vehicle fuel economy declarations; CAFE Phase II reporting began from FY 2022–23 (April 1, 2022 onwards) with significantly more factory-fitted CNG, hybrid, and electric vehicle declarations. [confidence: high]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- **“Petrol (E20)”** – The article treats E20‑blended gasoline as the prevailing petrol fuel in India. As of October 2026, India’s nationwide standard gasoline blend is still E10; E20 has only been piloted in a few states and is not the default market fuel. Therefore the statement that the model is for “petrol (E20)” misrepresents the actual fuel composition. [confidence: medium]

**INTERPRETATION ERRORS**
- **“Same‑model petrol→CNG mean distance uplift: +40.3% (11 nameplates)”** – The article presents this 40 % uplift as evidence that converting a petrol car to CNG will reliably give a 40 % increase in distance per litre (or per kg). The figure is derived from only 11 nameplates (a very small, non‑representative sample) and does not control for vehicle‑specific factors such as engine tuning, load, or driving conditions. Extrapolating this result to all cars constitutes an over‑generalised causal claim. [confidence: high]

**OUTDATED DATA**
- **“The SIAM declaration dataset is from passenger vehicles as on 1 April 2020; it has only 11 CNG, 8 hybrid and 1 electric entries.”** – The dataset is six‑plus years old. The Society of Indian Automobile Manufacturers released updated fuel‑efficiency declarations for 2022‑2023, which contain many more CNG and EV entries. The article should be re‑checked against the latest SIAM data (e.g., the 2023 BSVI declaration file). [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Delhi petrol Rs 102.12/L in the model"* — As of mid-2024, Delhi’s average petrol price was closer to **Rs 110–115/L** (post-2023 tax hikes and global crude fluctuations). The July 2026 figure is implausible given India’s fuel price trends (confidence: **high**).
- *"SIAM declaration dataset is from passenger vehicles as on 1 April 2020"* — SIAM’s latest **BS-VI fuel-efficiency declarations** (as of 2024) are typically updated annually; the 2020 cutoff is outdated for current market comparisons (confidence: **high**).

**INTERPRETATION ERRORS:**
- *"Petrol cost already includes the selected 4% E20 mileage drop"* — While this is technically correct, the claim **misrepresents causality**: the 4% drop is an *assumption* (not a measured effect of E20), and extrapolating it to all petrol cars conflates **blended fuel efficiency** with **real-world variability** (confidence: **high**).
- *"Mean petrol declared FE 16.67 kmpl → E20@4% 16.0 kmpl"* — The 0.67 kmpl drop is presented as a universal adjustment, but **E20’s impact varies by engine** (e.g., older cars may see a 2–5% drop, while newer ones could be unaffected). The article treats it as a fixed multiplier, ignoring engine-specific sensitivity (confidence: **high**).

**OUTDATED DATA:**
- *"Prices are inputs in the workbook: update them to today's before drawing conclusions"* — The **July 2026 price snapshot** (Rs 102.12/L petrol, Rs 95.20/L diesel, Rs 83.09/kg CNG) is likely superseded by **2024–2025 official data** from:
  - **Petrol/diesel**: [Petroleum Planning & Analysis Cell (PPAC) monthly bulletins](https://ppac.gov.in/) (check latest fiscal year).
  - **CNG**: [Petroleum & Natural Gas Regulatory Board (PNGRB) state-wise price orders](https://pngrb.gov.in/) (e.g., Delhi’s CNG prices were revised in 2023).
  - **Electricity**: [Central Electricity Authority (CEA) tariff data](https://cea.nic.in/) (state-specific blended rates).
  *(confidence: **high** for all; newer periods available post-2023)*
