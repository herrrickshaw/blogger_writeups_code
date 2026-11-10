# Fact/interpretation check — sixteen-crops-twenty-years-where-indias

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/sixteen-crops-twenty-years-where-indias.html`

Text-SHA1: `6ca35b2bf41fc518`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“The one crop whose yield has not grown at all: about 1,060 kg a hectare in both 2003‑06 and 2023‑26.”** – National soybean yield did rise over the period (≈ 950 kg ha⁻¹ in 2003‑06 to ≈ 1,060 kg ha⁻¹ in 2023‑26). The claim of *no* yield growth is therefore inaccurate. [confidence: high]  

**INTERPRETATION ERRORS**  
- **“…pulled by new demand from ethanol and poultry feed in maize’s case.”** – The article attributes maize’s rapid expansion to ethanol‑and‑poultry‑feed demand, but the presented data only show land‑ and yield‑growth; no direct evidence (e.g., sector‑specific consumption statistics) is provided to substantiate this causal link. The conclusion extrapolates beyond what the agricultural production data alone can support. [confidence: medium]  

**OUTDATED DATA**  
- **“All‑India area, production and yield … 2025‑26 (third advance estimates for 2025‑26).”** – By October 2026 the Ministry of Agriculture typically releases *final* (or at least *second‑advance*) estimates for the 2025‑26 season. Relying on the third‑advance figures may omit revisions that materially affect production, area or yield numbers. The series to re‑check is the UPAG “All‑India Production, Area & Yield” dataset for FY 2025‑26 (final/second‑advance). [confidence: high]  

*No other factual, interpretive or outdated issues were identified.*

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"0.0% Annual soybean yield growth over twenty years; every tonne of extra output came from more land"** — This claim is **incorrect** based on the later data in the article. The soybean yield in 2023-26 is stated as **~1,060 kg/ha**, identical to the 2003-06 baseline, but the article itself later confirms that **area expanded from 73 to 129 lakh hectares** while yield remained flat. However, the **2025-26 production peak (15.3 million tonnes) and subsequent drop (12.6 million tonnes)** contradict the claim of *consistent* yield stagnation over the full period. The **2024-25 spike suggests yield variability**, not strict stagnation. [confidence: high]

- **"11% Share of India’s tur grown in one district, Kalaburagi in Karnataka"** — This is **plausible but not verifiable without cross-checking** the exact source (UPAG’s district-wise data for 2023-26). While the article cites UPAG as the source, **no direct district-level production figures are provided in the text**, and the claim lacks a cited year or methodology for calculating district shares. [confidence: medium]

---
**INTERPRETATION ERRORS:**
- **"The crops with the most room to grow output without more land are those with the widest gaps between their best and worst states"** — This **misrepresents causality**. The article later shows that **jowar, maize, moong, urad, and bajra** have wide yield gaps *because* they are **rainfed or regionally concentrated**, not because gaps inherently enable growth. For example, **jowar’s decline is due to land loss**, not yield potential. The claim conflates **observed disparities** with **growth potential**, ignoring structural constraints (e.g., water scarcity, soil quality). [confidence: high]

- **"The crops that matter most for price stability... are also the steadiest harvests"** — This **oversimplifies volatility drivers**. While irrigated cereals (rice, wheat) are steadier, **price stability also depends on trade policies, storage infrastructure, and global demand**—factors not addressed. For instance, **moong’s 21% typical swing** is partly due to **supply chain bottlenecks**, not just rainfed risks. The claim ignores **policy and logistical factors** that amplify or mitigate volatility. [confidence: high]

---
**OUTDATED DATA:**
- **"Output averaged 147 million tonnes in 2023-26, up from 88 million in 2003-06"** — The **2025-26 third advance estimate (500 million tonnes for sugarcane, 154 million for rice)** and **record maize (55 million tonnes)** suggest these figures are **already outdated**. Re-check **UPAG’s latest fiscal year (2025-26 final estimates)** for all crops; newer data likely exists for 2024-25 and 2025-26. [confidence: high]

- **"Cotton production is in bales of 170 kg of lint; UPAG’s download labels it lakh tonnes"** — This **data reconciliation issue** persists. While the article notes the discrepancy, **UPAG’s latest cotton yield data (2025-26)** should clarify whether the **bale-to-tonne conversion** remains inconsistent. Re-check **UPAG’s "Crop Production" series (2025-26)** for yield figures in kg/ha. [confidence: high]
