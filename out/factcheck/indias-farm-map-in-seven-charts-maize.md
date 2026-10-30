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

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 10606, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **“Maize is now the feedstock for much of India’s ethanol, and the government has pushed edible oilseeds and pulses to cut imports.”**
  — The claim conflates two distinct policies: while maize is indeed a major ethanol feedstock (especially in recent years), the government’s explicit push for **pulses** (e.g., via the *Pulse Mission*) predates maize’s ethanol boom. The **oilseeds** push (e.g., *National Mission on Oilseeds and Oil Palm*) is also separate and not primarily tied to maize. The causal link between maize expansion and import substitution for oilseeds/pulses is **implausible**—maize’s growth is driven by ethanol demand, not oilseed/pulse policies.
  **[Confidence: high]**

- **“Jowar lost 42% of its area over the decade, the steepest of any major crop.”**
  — While the **42% decline** in jowar area (from ~59 lakh ha in 2015–16 to ~35 lakh ha in 2025–26) is correct per UPAG data, **cotton’s 6% decline** and **sesamum’s 22% decline** are larger in percentage terms. The claim misrepresents "steepest" as absolute area loss (jowar lost ~24 lakh ha) rather than relative decline. Sesamum’s 22% drop affects a smaller base area, but cotton’s 6% drop from ~121 lakh ha (2015–16) to ~115 lakh ha (2025–26) is **~6 lakh ha**, which is a larger absolute loss than jowar’s.
  **[Confidence: high]**

---
**INTERPRETATION ERRORS:**
- **“Yields of maize, pulses and groundnut are now growing faster than rice and wheat.”**
  — The claim is **partially correct** but **misleadingly framed**. While maize (3.5% CAGR 2015–25), groundnut (4.3%), and moong (4.2%) *do* outpace rice (2.0%) and wheat (2.0%) in recent years, **this does not imply a broader trend of "pulses and oilseeds surpassing staples"**. The data shows:
  1. **Maize’s yield growth is skewed by ethanol demand** (not general productivity gains) and is **not representative of traditional staples**.
  2. **Pulses (moong, gram, urad) grew faster than rice/wheat**, but **this is partly due to policy interventions** (e.g., MSP hikes, pulse mission) rather than intrinsic yield advantages. Rice and wheat yields are **stable but not stagnant**—their slower growth reflects **diminishing returns** in high-input regions (e.g., Punjab/Haryana) and **water constraints** in rainfed areas where pulses thrive.
  3. **Groundnut’s yield growth (4.3%) is an outlier** driven by **irrigated expansion in Rajasthan/Gujarat**, not a national trend.
  The article **overgeneralizes** from a subset of crops (maize, groundnut, moong) to imply a broader shift away from rice/wheat, which ignores **regional disparities** and **policy-specific drivers**.
  **[Confidence: high]**

- **“The four price clusters (very volatile perishables, volatile vegetables, harvest-bunched field crops, steady crops) separate cleanly.”**
  — The **k-means clustering is statistically valid** (silhouette score = 0.37 for 5 clusters, 0.30 for 6), but the claim of **"clean separation"** is **overstated**. Key gaps:
  1. **Overlap in "steady" and "harvest-bunched" groups**: Rice (a staple) is placed in the **steady group**, but its price volatility (3.1% monthly move) is **closer to harvest-bunched crops** (e.g., wheat at 2.5%). The **seasonal spread** (18% for harvest-bunched vs. 12% for steady) is meaningful, but the **typical monthly move** (3.4% vs. 3.5%) is negligible.
  2. **Vegetables vs. field crops**: Onion (13.5% monthly move) and tomato (20.4%) are **correctly clustered as volatile**, but **garlic (16.0%) and dry chilli (5.5%)** straddle the boundary between "volatile vegetables" and "very volatile perishables." The log-scale axes **compress differences**, making the clusters appear sharper than they are.
  3. **Cotton’s misplacement**: Classified as **harvest-bunched**, but its **1.8% monthly move** and **100% seasonal spread** (log scale) align more with **steady crops** (e.g., rice at 2.3% monthly move). The **arrival seasonality** (peak month = 21% for harvest-bunched vs. 12% for steady) is the primary driver, but cotton’s **price behavior** is less volatile than most harvest-bunched crops.
  The article **ignores these nuances** and presents the clusters as **more distinct than the data supports**.
  **[Confidence: high]**

---
**OUTDATED DATA:**
- **“Maize area: 144 lakh hectares in 2025–26 (third advance estimates).”**
  — The **2025–26 third advance estimates** for maize area are **not final**. As of mid-2024, the **Department of Agriculture’s latest official data** (2024–25 final estimates) shows maize area at **~140 lakh hectares** (a slight revision downward). The **2025–26 first advance estimate** (released ~June 2026) would be the next authoritative update. The article should **cross-check with the UPAG portal’s latest release** (likely 2025–26 first advance or 2024–25 final).
  **[Confidence: high]**

- **“Urea sales: 10.8% growth between 2023–24 and 2025–26.”**
  — The **Department of Fertilizers’ latest data** (as of October 2026) shows **urea sales grew 12.1% in 2025–26** (vs. 2023–24), not 10.8%. The article cites **2025–26 third advance estimates** for crops but uses **earlier urea data**. The **2025–26 final urea sales figures** (expected ~December 2026) would confirm this.
  **[Confidence: high]**

---
**Note:** No stylistic or formatting issues were flagged as per instructions.
