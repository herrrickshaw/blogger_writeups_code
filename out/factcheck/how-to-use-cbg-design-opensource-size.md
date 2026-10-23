# Fact/interpretation check — how-to-use-cbg-design-opensource-size

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-cbg-design-opensource-size.html`

Text-SHA1: `80e1d8dc1bf8b6fc`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Barsana's real feedstock mix is not public, so this gap is unresolved." — The feedstock mix for Phase I of the Barsana CBG plant is public knowledge. Operator Adani Total Gas Ltd (ATGL) / Adani TotalEnergies Biomass Ltd (ATBL) explicitly disclosed in press releases and regulatory filings that Phase I is designed to process 225 tonnes per day of 100% cattle dung (sourced from the Shree Mataji Gaushala in Barsana), while agricultural residues such as paddy straw are planned only for Phase II and III expansion. [confidence: high]

INTERPRETATION ERRORS:
- "Every mix that includes straw overshoots, up to 29.31 t/day for pure straw. Straw's calibrated gas yield is about 3x dung's. Barsana's real feedstock mix is not public, so this gap is unresolved." — This is an apples-to-oranges comparison. The author treats the higher CBG output from straw (29.31 t/day) as an "overshoot" relative to the Barsana Phase I benchmark (10 t/day). However, Barsana Phase I is specifically rated for 225 t/day of cattle dung. Because agricultural straw has much higher dry matter, volatile solids, and specific biomethane potential than raw cattle dung, a plant processing pure straw or straw blends is expected to produce substantially more biogas per tonne of feed. Comparing straw model outputs to a dung-only plant's capacity does not represent a model calibration failure or an unresolved gap. [confidence: high]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “upgrading to the IS 16087 gas standard” — IS 16087 is the Indian Standard for **Compressed Natural Gas (CNG)**, not for **Compressed Biogas (CBG)**. The appropriate standard for CBG is IS 16087‑2 (or other specific CBG specifications). The article misidentifies the standard being met. [confidence: high]

**INTERPRETATION ERRORS**
- “Straw's calibrated gas yield is about 3× dung's… Every mix that includes straw overshoots, up to 29.31 t/day for pure straw.” — The model assumes a simple linear multiplier (≈3×) between straw and dung methane yields and uses this to explain the large CBG output from a pure‑straw feed. In reality, straw’s higher lignocellulosic content leads to slower hydrolysis, lower digestibility, and often **lower** specific methane yields than a straight 3× factor would suggest. Thus the claim that the overshoot is solely due to a 3× yield ratio is an **apples‑to‑oranges** extrapolation that overstates straw’s conversion potential. [confidence: medium]

**OUTDATED DATA**
- none found

## Mistral open-mistral-nemo

Here is the structured critique of the article:

---
**FACTUAL ERRORS:**
- *"10.14 t/day CBG from a pure dung feed vs 10 published 29.31 t/day CBG from pure straw"* — The claim that the published Barsana Phase I plant produces **10 t/day CBG** from a pure dung feed is inconsistent with the later statement that the model’s output for pure dung (10.14 t/day) "lands near" the published figure. If the published figure is indeed **10 t/day**, the model’s 10.14 t/day is a minor overestimate, but the article does not clarify whether the published figure is for pure dung or a mixed feedstock. The core issue is the lack of explicit attribution for the "published plant" data (e.g., source document, exact feedstock composition, or operational conditions). [confidence: high]

**INTERPRETATION ERRORS:**
- *"The model uses literature correlations only, with no vendor data... Run it as a sanity check, not as a guarantee of what a real plant will produce"* — While this caveat is correct, the article **fails to acknowledge that the 2.93× overshoot for straw-based CBG (29.31 t/day vs. published 10 t/day) could stem from unaccounted real-world factors** (e.g., feedstock moisture content, digester efficiency losses, or upgrading inefficiencies). The claim that "only a 100% dung feed lands near the published plant" implies a causal link between feedstock type and output discrepancy, but the reasoning ignores that **published plants may use hybrid feedstocks or operational optimizations** not reflected in literature correlations. The article conflates model limitations with empirical validation without addressing alternative explanations. [confidence: high]

**OUTDATED DATA:**
- *"Revised 18 October 2026"* — The article’s revision date suggests it is based on data/current as of late 2026. However, **no newer official updates** (e.g., SATAT scheme amendments, IS 16087 revisions, or Barsana Phase I operational data post-2026) are referenced. If the article claims to validate against "published plant" data, readers should verify whether:
  - The Barsana Phase I figures (10 t/day CBG) have been updated in **Ministry of New and Renewable Energy (MNRE) reports** or **SATAT scheme progress documents** (e.g., 2023–24 annual reports).
  - The **IS 16087 standard** (last revised in 2016) has undergone changes requiring re-calibration of upgrading yields.
  [confidence: medium]

---
**Note:** The article’s core technical claims (e.g., Buswell equation application, compression stages) are plausible and not flagged as errors, as they align with standard CBG engineering practices. The issues lie in **transparency of sources**, **causal reasoning**, and **data freshness**.
