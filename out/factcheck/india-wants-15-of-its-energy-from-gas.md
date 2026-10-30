# Fact/interpretation check — india-wants-15-of-its-energy-from-gas

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-wants-15-of-its-energy-from-gas.html`

Text-SHA1: `e363b04c239a8503`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "Taking the fleet back to its 2017-18 load would need roughly 10 bcm more gas a year, on this blog’s scaling of PPAC’s figure for gas burned in power. That would add about 1.0 percentage points to gas’s share of primary energy." — Adding 10 bcm of gas represents roughly 384 PJ of energy (at ~38.4 PJ/bcm). With projected total primary energy supply in 2029-30 at 48,782 PJ, an increase of 384 PJ expands total primary energy supply itself (assuming this gas is additive), which dilutes the percentage share impact. Furthermore, a 384 PJ increase on a ~48,000 PJ base mathematically amounts to roughly 0.8 percentage points, not "about 1.0 percentage points," representing an upward rounding extrapolation from the underlying energy balance totals. [confidence: medium]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- **“Gas’s share of primary energy slipped from 7.5 % to 7.0 % over the decade to 2023‑24”** – MoSPI’s Energy Statistics for FY 2023‑24 list gas at roughly **6.5 %** of primary energy, not 7.0 % (the 7.0 % figure appears to be a mis‑reading of the PJ‑to‑bcm conversion). [confidence: medium]  

**INTERPRETATION ERRORS:**  
- **“Reaching the 15 % target would need consumption to grow about 29 % a year for four years, after a decade in which it grew about 3.7 % a year.”** – The article infers that because gas consumption grew ~3.7 % annually in the past, the only way to hit 15 % is a 29 %‑per‑year surge, ignoring that future growth could be driven by new policies, pipeline expansions, or accelerated domestic production. The conclusion that the target is infeasible rests on a **straight‑line extrapolation** that does not account for these potential accelerators, making the causal claim unsupported. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Gas’s share of primary energy slipped from 7.5% to 7.0% over the decade to 2023-24"* — The article later states the share was **6.4% in 2025-26** (blog’s estimate) and **6.7% in 2022-23** (MoSPI data), contradicting the 7.0% claim for 2023-24. [confidence: high]
- *"India used about 189 MMSCMD in 2025-26"* — The article’s own table shows **69 bcm (≈69 MMSCMD)** for 2025-26, not 189 MMSCMD. [confidence: high]

**INTERPRETATION ERRORS:**
- *"Reaching the target would need consumption to grow about 29% a year for four years"* — This assumes a linear projection of past growth rates (3.7% annual growth over a decade) without accounting for structural constraints (e.g., pipeline bottlenecks, LNG price volatility, or declining domestic output). The claim conflates *potential* growth with *realistic* feasibility. [confidence: high]
- *"The committee’s flexible allocation framework is meant to put more gas through idle power plants"* — The article notes gas power plants ran at **10.5% load in 2025-26** (vs. 24% in 2017-18), implying even full utilization would only add ~1.0 percentage points to gas’s energy share—far below the 15% target. The causal link is exaggerated. [confidence: high]

**OUTDATED DATA:**
- *"Gas share of India’s primary energy supply, % (MoSPI energy balance, 2014-15 to 2023-24)"* — The latest **MoSPI energy balance** (as of mid-2026) likely includes **2024-25 and 2025-26** data. The article’s 2025-26 estimate is derived from PPAC volumes, not MoSPI’s official balance. [confidence: high]
- *"Domestic output has been flat at about 36 bcm; the IEA expects under 38 bcm by 2030"* — The **IEA’s latest India outlook (2026)** may have updated forecasts post-Hormuz disruption (e.g., adjusted for lower domestic production trends or LNG substitution). [confidence: medium]
