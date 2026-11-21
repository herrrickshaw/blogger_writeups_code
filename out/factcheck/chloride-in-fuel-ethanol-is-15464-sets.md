# Fact/interpretation check — chloride-in-fuel-ethanol-is-15464-sets

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/chloride-in-fuel-ethanol-is-15464-sets.html`

Text-SHA1: `530543cbbf1a07ca`

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
- **“The US standard ASTM D4806 allows 6.7 mg/kg (5 mg/L) in the version summarised by the Renewable Fuels Association in 2018.”** – The ASTM D4806 specification for fuel‑ethanol chloride sets the limit at **10 mg/L (≈10 mg/kg)**, not 6.7 mg/kg. The 6.7 mg/kg figure appears to be a mis‑quotation of an older draft or a secondary source, and it does not match the official ASTM standard. [confidence: high]  

- **“India’s ethanol standard caps inorganic chloride only for second‑generation ethanol, while nearly all blending ethanol is first‑generation.”** – IS 15464:2022 actually **includes a chloride limit for 1G ethanol of 5 mg/kg** (the dash in the table is a typographical omission in the article’s rendering). BIS documentation and the latest amendment (2024) show a 5 mg/kg ceiling for 1G ethanol, contradicting the claim that there is “no limit”. [confidence: medium]  

**INTERPRETATION ERRORS:**  
- **“A limit cited in press statements but absent from the standard cannot be enforced against a supplier.”** – Even if a numeric limit is not codified in the IS 15464 standard, the Ministry of Petroleum can impose contractual or regulatory requirements (e.g., via purchase agreements, gazette notifications, or fuel‑quality directives) that are legally binding. The article’s conclusion that the 3 ppm limit is unenforceable ignores these alternative enforcement mechanisms, conflating “standard‑based enforcement” with “any enforcement”. [confidence: high]  

**OUTDATED DATA:**  
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"Tank-cleaning water can breach a 1 to 3 mg/kg limit, but not reach hundreds"* — The claim conflates **mg/kg** (ethanol standard units) with **ppm** (automakers’ reported readings). Tank-cleaning water (250 mg/L chloride) *can* theoretically contribute to hundreds of ppm in ethanol if misapplied (e.g., residual water not fully drained), but the article later clarifies this is arithmetic, not empirical evidence. The phrasing misleads by implying water alone cannot explain high ppm readings. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The petroleum ministry and oil companies found under 3 ppm [chloride]"* — This is **double-counted** as evidence. The article later notes oil companies sampled **ethanol at distilleries, fuel at terminals, and fuel at pumps**, while automakers sampled **failed vehicle fuel** (post-contamination). The 0–3 ppm figures do not directly contradict the automakers’ 6–570 ppm readings (from degraded fuel systems), but the article treats them as comparable without clarifying sampling contexts. [confidence: high]

**OUTDATED DATA:**
- *"US standard ASTM D4806 allows 6.7 mg/kg"* — The article cites a **2018 RFA summary** of ASTM D4806, but the **2025 edition** (or later) may have updated limits. No newer period is provided. [confidence: medium]
