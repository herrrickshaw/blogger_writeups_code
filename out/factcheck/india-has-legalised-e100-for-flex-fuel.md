# Fact/interpretation check — india-has-legalised-e100-for-flex-fuel

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-has-legalised-e100-for-flex-fuel.html`

Text-SHA1: `3ede7881d677e301`

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
- “E20 becomes the only petrol sold” (effective 1 Apr 2026) — India’s mandate made **E20 the standard blend for petrol**, but other blends (e.g., E10 in some states) and diesel continued to be sold. The statement that it is “the only petrol sold” is inaccurate. [confidence: high]  
- “Constitutional Amendment 123/2022 requires biofuels to be taxed below fossil fuels for 20 years” — Amendment 123 introduced a **bio‑fuel policy and tax incentives**, but it does **not** constitutionally obligate a lower tax rate for bio‑fuels for a fixed 20‑year period. The claim overstates the amendment’s legal effect. [confidence: high]  

**INTERPRETATION ERRORS:**  
- “E85 is about 6 % dearer per kilometre than petrol” – The calculation is based solely on the lower energy density of ethanol (21.3 MJ/L vs 32.4 MJ/L) and assumes **identical engine efficiency** for both fuels. In practice, flex‑fuel engines can achieve higher thermal efficiency (e.g., due to higher octane allowing higher compression), so the per‑kilometre cost gap cannot be inferred from energy content alone. The conclusion therefore extrapolates beyond the data. [confidence: high]  
- “The unsold surplus would cover flex‑fuel vehicles taking about 8 % of petrol demand” – This assumes **all 576 crore L of surplus ethanol can be redirected to E100** without accounting for quality constraints, logistics, seasonal storage limits, or the fact that some of the surplus may already be earmarked for other uses (e.g., industrial feedstock). The inference that the surplus alone can support an 8 % shift in petrol demand is therefore an over‑extension of the arithmetic. [confidence: medium]  

**OUTDATED DATA:**  
none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Today’s unsold ethanol would cover about 8% of petrol demand"* — The claim conflates **unsold surplus (576 crore litres)** with **petrol demand (42.6 Mt = 4,260 crore litres)**. While the arithmetic later clarifies that 576 crore litres could theoretically replace ~8% of petrol *energy* (after accounting for E20’s 20% ethanol content), the phrasing risks implying a literal volume match (576 crore litres ≈ 8% of 4,260 crore litres is incorrect; 8% of 4,260 crore litres ≈ 340 crore litres). The error lies in omitting the energy-density adjustment in the headline claim.
  [confidence: high]

- *"E100 can only compete if it is taxed far below petrol"* — The article later states that **E100 would need to be taxed ~Rs 1 a litre (vs. ~Rs 36 for petrol)** to match per-kilometre costs, not "far below." The original phrasing is vague and overstates the required tax differential.
  [confidence: high]

---
**INTERPRETATION ERRORS:**
- *"E85 is cheaper per litre but dearer per kilometre"* — While true for **current prices (Rs 82.12 vs. Rs 102.12 for E20)**, this ignores:
  1) **E85’s energy content (76% of E20’s per litre)**, meaning the per-kilometre cost gap narrows if drivers account for fuel efficiency (e.g., flex-fuel engines could offset 5% of the gap, per the article’s own sensitivity analysis).
  2) **The claim assumes static efficiency**, but real-world flex-fuel engines may achieve higher compression ratios with ethanol, reducing the per-km cost difference further. The article later corrects this but the initial framing misleads readers into assuming E85 is *always* more expensive per km.
  [confidence: high]

- *"There is not enough ethanol for a large flex-fuel fleet"* — The claim is **correct in principle** (unsold surplus = 576 crore litres covers ~8% of petrol energy demand), but the reasoning **double-counts constraints**:
  1) The 576 crore litres are **already allocated to E20 blending** (per the "net of E20 ethanol" note), leaving little for flex-fuel use.
  2) The article later states that **E30 alone would require 2,221 crore litres by 2029–30**, implying current surplus is insufficient even for incremental flex-fuel adoption *and* higher blends. The error is treating the surplus as a standalone pool rather than a **zero-sum resource** competing with E20/E30 mandates.
  [confidence: high]

---
**OUTDATED DATA:**
- *"E85 goes on sale | Indian Oil, Pusa Road, Delhi, at Rs 82.12/litre against Rs 102.12 for E20; targets of 500 pumps by Dec 2026 and 5,000 by Dec 2027"* —
  **Series to re-check:** Indian Oil’s **E85/E100 pricing and pump rollout updates** (official press releases or [Indian Oil’s corporate website](https://www.iocl.com)).
  **Newer period:** As of **October 2026**, the article notes E85 is "on sale in Delhi" but does not confirm whether:
  - The **Rs 82.12 price** remains current (inflation or tax changes could have altered it).
  - The **500-pump target** has been met or adjusted (e.g., delays, expansions to other states).
  [confidence: high]

- *"unsold surplus 576 [crore litres] ... On the 2025-26 petrol pool (42.6 Mt)"* —
  **Series to re-check:** **2026-27 ethanol supply/demand data** from:
  - [PIB’s monthly ethanol bulletins](https://pib.gov.in/)
  - [NITI Aayog’s biofuel reports](https://niti.gov.in/)
  - [ChiniMandi’s market updates](https://www.chinimandi.com/)
  **Newer period:** The **2025-26 surplus (576 crore litres)** may not reflect:
  - **2026-27 production increases** (e.g., new distilleries like those in Maharashtra or Uttar Pradesh).
  - **2026-27 petrol demand shifts** (e.g., slower growth due to EV adoption or economic conditions).
  The article’s **2029-30 forecast (2,221 crore litres for E30)** suggests the 2026-27 surplus could differ significantly.
  [confidence: high]
