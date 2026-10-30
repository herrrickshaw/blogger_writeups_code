# Fact/interpretation check — how-to-use-eu-ets-compliance-platform

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-eu-ets-compliance-platform.html`

Text-SHA1: `a57741efd99b32cc`

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
- **“CBAM phase‑in schedule … 2026 = 97.5 % free allocation, 2.5 % CBAM factor … 2034 = 0 % free allocation, 100 % CBAM factor.”** – The percentages shown do not match the official EU CBAM phase‑in schedule, which (as of the latest EU Commission Delegated Regulation) starts with 100 % free allocation in 2023 and reduces to 0 % only by 2035, with a different step‑down pattern. The article presents the seeded demo values as if they were the real schedule. **[confidence: high]**  

**INTERPRETATION ERRORS**  
- **“The run shows why the choice matters in CBAM: for the same 1,000 t of Indian steel, default values gave 3,223 t of embedded CO₂ versus 2,200 t with supplied actuals (illustrative data).”** – The article extrapolates from a single, artificial demo run to imply that using default values will always lead to substantially higher embedded emissions for real imports. In practice, the gap between default and actual emissions depends on the specific product, supplier data quality, and the actual default factors set by the EU; a single illustrative example cannot substantiate a general claim about the magnitude of the effect. **[confidence: high]**  

**OUTDATED DATA**  
- **“Default factors: India steel = 2.45 t CO₂/t direct and 0.48 t CO₂/t indirect (plus a 10 % mark‑up).”** – These emission factors are presented without a date reference and are described as “illustrative”. The EU’s CBAM methodology was updated in 2024 with revised product‑specific emission factors for Indian steel (e.g., ~2.10 t CO₂/t direct, ~0.35 t CO₂/t indirect). The article should flag the source series (EU CBAM product‑specific emission factors) and note that a newer official factor set exists. **[confidence: medium]**

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"1,900 t same shipment with supplied actual direct emissions"** — The claim conflates two separate declarations (1,000 t steel with actuals and 500 t cement with defaults) into a single "same shipment" comparison. The 1,900 t figure only applies to the 1,000 t steel shipment, not a combined total. [confidence: high]

INTERPRETATION ERRORS:
- **"The numbers matched hand calculation from the default-value table"** — This suggests the prototype’s reconciliation logic was validated against a static default-value table, but the article later notes the default factors are "illustrative values" (not official) and the phase-in schedule is also illustrative. Thus, the "match" doesn’t prove compliance with real EU CBAM rules. [confidence: high]

OUTDATED DATA:
- **"CBAM phase-in schedule (2026 to 2034)"** — The schedule is explicitly labeled as "seeded illustrative values" and not tied to any official source. However, if the article claims this as "current" for India-focused readers, it should note that the latest official CBAM phase-in (e.g., 2023–2034) may differ (check [EU Commission CBAM Registry](https://ec.europa.eu/clima/cbam_en)). [confidence: medium]
