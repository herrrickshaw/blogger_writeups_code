# Fact/interpretation check — indias-draft-steel-policy-plans-604-mt

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-draft-steel-policy-plans-604-mt.html`

Text-SHA1: `654037a93f23db83`

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
- “…with Russia the main supplier of coal injected into furnaces.” — India’s coking‑coal imports are dominated by Australia (and to a lesser extent Canada, Mozambique and the United States); Russia supplies mainly thermal coal, not the coking coal used for blast‑furnace coke. This statement misidentifies the principal supplier. [confidence: high]  

**INTERPRETATION ERRORS**  
- “The emissions goal needs cleaner blast furnaces, not only more scrap … the industry reaches 1.54 t CO₂ per tonne only if its blast furnaces emit about 1.66–1.68 t, …” — The calculation assumes that all DRI steel will be produced with low‑carbon gas (1.6 t CO₂/t) and that scrap emissions stay at 1.2 t CO₂/t. In reality, the majority of India’s DRI today is coal‑based, which has a higher emission factor than the 1.6 t assumed. By ignoring the higher‑emission coal‑DRI pathway, the analysis overstates how much blast‑furnace emissions can be reduced while still meeting the 1.54 t target. This is a false causal inference that the target can be met by cleaning up blast furnaces alone. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"India imported 29.5% more steel this year despite a safeguard duty"* — This claim is not directly supported by the article’s context (which focuses on 2026 steel policy drafts and coal/emissions data) and contradicts the article’s own sources (e.g., SteelOrbis, GMK Center) for steel imports. The 29.5% figure appears unrelated to the policy’s timeline or data. [confidence: low]

**INTERPRETATION ERRORS:**
- *"The draft’s 236 Mt coking coal forecast implies blast furnaces keep 43–57% of output, so the emissions target rests on cleaning up blast furnaces themselves"* — While the arithmetic is plausible, the causal leap is flawed. The 43–57% range depends on **assumptions** (e.g., India’s vs. world-average coal efficiency, coal use outside steelmaking) that are not explicitly validated in the draft policy. The article itself notes these are "calibrated from the draft’s current-demand figure," which may overstate coal needs. Thus, the claim conflates *possible* coal demand with *certain* blast-furnace dominance without addressing alternative routes (e.g., gas-based DRI) or policy constraints. [confidence: high]

**OUTDATED DATA:**
- *"Capacity was 138 Mt in 2017-18 and reached 220.4 Mt in 2025-26"* — The 2025-26 capacity figure (220.4 Mt) is likely outdated. The latest **Ministry of Steel’s annual report (2025-26)** or **JPC data** (e.g., via Lok Sabha replies) should confirm this, but newer fiscal-year data (e.g., 2026-27) may exist. [confidence: medium]
- *"Iron ore: 289 Mt mined in 2024-25"* — The **Ministry of Mines’ latest annual report (2025-26)** or **SteelOrbis’ 2026 data** could supersede this figure. [confidence: medium]

*(Note: The 2017 policy’s 2030-31 targets are correctly flagged as outdated in the article itself, so no additional action needed there.)*
