# Fact/interpretation check — petrol-pump-margins-and-e20-one-dealer

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/petrol-pump-margins-and-e20-one-dealer.html`

Text-SHA1: `318e363fc23538a0`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "No dealer-commission revision after October 2024 was found." — This directly contradicts several other sections of the article, which explicitly document a subsequent revision and formula re-set on 1 December 2024 (reducing the fixed part to Rs 3,144.03/KL for petrol and Rs 2,332.51/KL for diesel, while increasing the variable percentages to 0.870% and 0.266%). [confidence: high]
- "The ₹49.41–71.86 range in the table below is for 2025-26." — In the table below that statement, the price range across feedstocks for ESY 2025-26 is ₹57.97 to ₹71.86 per litre. The ₹49.41 figure belongs to C-heavy molasses in ESY 2022-23, not 2025-26. [confidence: high]

INTERPRETATION ERRORS:
- "The party that gained directly from E20 is the ethanol supplier, whose price is set by the government." / "Ethanol suppliers: the clear gainers: Rs 1.72 lakh crore of purchases across three ethanol supply years." — The article conflates gross procurement expenditure (topline turnover) with economic margin or profit. While assessing dealers and OMCs on per-litre net or marketing margins, it judges ethanol suppliers as the "clear gainers" purely on total procurement outlays (Rs 1.72 lakh crore) paid by OMCs. This ignores distillers' and farmers' feedstock, processing, energy, transportation, and capital costs, confusing gross revenue with profitability. [confidence: high]
- "The average Indian outlet earns about Rs 4.77 lakh a month in gross commission... Gross commission after 30 Oct 2024 | Rs 4.77 lakh | Rs 4.39 on petrol and about Rs 3.03 on diesel, Delhi" — Geographic extrapolation / apples-to-oranges calculation. The author multiplies national average throughput volumes (45,000 litres of petrol and 92,000 litres of diesel) by Delhi-specific commission figures (Rs 4.39 and Rs 3.03). Dealer commission structures and net realizations vary widely across states, freight zones, slab tiers, and site ownership models (A-site vs. B-site); applying Delhi price-sheet averages to nationwide average volumes does not yield what the "average Indian outlet" earns. [confidence: high]

OUTDATED DATA:
- "CNG stations | 7,395 on 30 Nov 2024" — PPAC (Petroleum Planning & Analysis Cell) monthly gas infrastructure reports ("Number of CNG Stations"). In an article updated through late 2026 that provides November 2025 and 2026 counts for other fuel retail networks, a CNG outlet figure from November 2024 is superseded by newer official data for FY 2024–25 and FY 2025–26. [confidence: high]

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 413: {"error":{"message":"Request too large for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Requested 9371, please reduce your message size and try again. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The October 2024 revision, a litigation settlement, was the first increase in seven years and did not restore what inflation had taken."*
  — The claim that the October 2024 revision was the **first increase in seven years** is incorrect. PPAC’s table (posted 3 Dec 2024) shows **four increases after October 2016**, including a significant hike on **1 August 2017**, and a small cut in February 2019. The 2024 revision was the first increase since **August 2017** (not October 2016), making it closer to **7 years and 2 months**, not 7 years. [confidence: high]

- *"The Odisha dealers’ association said on 6 July 2026 that margins had not risen since 2024 despite a promise of six-monthly revisions."*
  — The article does not verify whether the Odisha dealers’ claim aligns with **PPAC’s official records** or other regional associations. The claim is presented as fact without cross-checking against PPAC’s updated table (which may have later revisions) or national dealer bodies. [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"The dealer got one rise in seven years, it was a litigation settlement, and in real terms it gave back less than half of what inflation had taken since 2017."*
  — The reasoning conflates **inflation erosion** (measured via MoSPI CPI) with the **fixed-component revision alone**, ignoring the **percentage-of-price component** of the commission formula (which grew with fuel price hikes post-2017). The blog’s own inflation-adjusted calculations (Dec 2025 rupees) show the fixed part restored **~40% of its 2017 value for petrol** and **~34% for diesel**, but the **total commission** (fixed + variable) likely offset more erosion due to rising fuel prices. The claim overstates the "loss" by excluding the dynamic percentage component. [confidence: high]

- *"The oil companies’ margin was high while crude was cheap and went negative when crude spiked in 2026."*
  — While crude prices correlate with OMC margins, the article **does not isolate E20’s impact** from other factors like **excise duty cuts (March 2026), frozen retail prices (May 2026), or tax actions**. The swing in margins is attributed to crude alone, but the **March excise reduction (Rs 10/litre)** and **May price freezes** (after crude spikes) likely exacerbated losses. The causal link to E20 is **unproven**—the ministry’s July 2026 statement explicitly notes E20 is **more expensive to produce than plain petrol at $70 crude**, contradicting the "clear gainer" claim. [confidence: high]

---
**OUTDATED DATA:**
- *"100,266 Fuel retail outlets at end-November 2025 (PPAC via press)"*
  — PPAC’s latest outlet counts (as of **October 2026**) show:
  - Indian Oil: ~41,664 (Nov 2025) → **no update found post-Nov 2025**.
  - BPCL/HPCL: ~24,605 and ~24,418 (Nov 2025) → **no newer figures**.
  - Private players (Nayara: 7,108 on 3 Oct 2026; Jio-bp: ~2,221 in Q1 FY27).
  **Re-check:** PPAC’s [official outlet data](https://ppac.gov.in) or Ministry of Petroleum’s latest reports for **FY27 or Q1 FY27 counts**. [confidence: high]

- *"Ethanol prices for the 2026-27 supply year run from ₹57.97 to ₹68.86"*
  — The article cites **ESY 2025-26 prices** (₹57.97–₹71.86) but claims these are for **2026-27**. No official **ESY 2026-27 ethanol price notification** is referenced. The **latest available** is ESY 2025-26 (published July 2026). **Re-check:** Ministry of Petroleum’s [ethanol price orders](https://petroleum.gov.in) for **ESY 2026-27** (expected by October 2026). [confidence: high]
