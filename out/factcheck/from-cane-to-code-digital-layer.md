# Fact/interpretation check — from-cane-to-code-digital-layer

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/from-cane-to-code-digital-layer.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Ethanol Supply Year runs roughly December–November" — In India, the Ethanol Supply Year (ESY) officially runs from 1 November to 31 October. The Ministry of Petroleum and Natural Gas revised the ESY schedule from December–November to November–October starting from ESY 2023-24. [confidence: high]
- "seen Maruti Suzuki launch India's first flex-fuel car (June 2026)" — Maruti Suzuki did not launch India's first flex-fuel car. Toyota launched India's first flex-fuel vehicle (the electrified flex-fuel Innova HyCross) in August 2023. [confidence: high]

INTERPRETATION ERRORS:
- "Government figures put the cumulative impact of the programme, from ESY2014-15 to January 2026, at roughly 283 lakh tonnes of crude oil displaced, ₹1.67 lakh crore in foreign exchange saved, ₹1.47 lakh crore paid to farmers through the ethanol value chain, and 851 lakh tonnes of CO₂ avoided . Those numbers, reported to the Rajya Sabha in March 2026, are the scale this article's digital layer now has to operate at." — The author equates cumulative multi-year macroeconomic and environmental outputs (12 years of aggregate forex savings, crude substitution, and emissions reduction) with the technical operational scale required of a digital tracking layer. The system scale of a software or traceability infrastructure depends on live data throughput, active supply chain nodes, concurrent batch updates, and daily transaction volume, not the cumulative historical economic savings of the entire national program. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "The Ethanol Blended Petrol programme launched in 2003, mandating a 5% blend in selected states." — The article does not provide a source to verify this specific launch date and mandate, but it does not necessarily mean it is incorrect. However, without further information, the confidence in this claim being incorrect is low. [confidence: low]
- None of the other claims appear to be factually incorrect based on the information provided in the article.

INTERPRETATION ERRORS:
- "A 0.5-point recovery gain on a 5,000-tonnes-crushed-per-day mill is, on the interview's own framing, worth “several crores in a season”" — This claim may be an example of extrapolation beyond what the data shows, as it is based on vendor-reported figures and not independently audited outcomes. The article itself notes that these numbers should be read as directional, not audited. [confidence: medium]
- "10–20% Farm yield improvement claimed for growers on an AI advisory pilot in Maharashtra" — This claim may be an example of double-counting or an apples-to-oranges comparison, as it is not clear how this improvement is measured or compared to other factors that may influence farm yield. [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 8 August 2026 · v1.0.0 · KPMG–ChiniMandi, “Beyond E20” (June 2026)" — The publication date of the article (8 August 2026) contradicts the cited report's date (June 2026), which is impossible unless the report was published in June and the article was published later. The article claims the report is from June 2026, but the publication date suggests it is newer. [confidence: high]

- "Maruti Suzuki launch India's first flex-fuel car (June 2026)" — While Maruti Suzuki did announce a flex-fuel car in 2026, the claim that it was the *first* in India is unverified and potentially incorrect, as other manufacturers may have launched flex-fuel vehicles earlier. [confidence: medium]

INTERPRETATION ERRORS:
- "4–8% Additional ethanol yield claimed from AI-tuned fermentation, same molasses input" — The claim implies a direct causal relationship between AI-tuned fermentation and increased ethanol yield, but the article does not provide evidence that the yield increase is solely attributable to AI rather than other factors like improved feedstock quality, operational changes, or seasonal variations. [confidence: high]

- "10–20% Farm yield improvement claimed for growers on an AI advisory pilot in Maharashtra" — The article presents this as a general improvement without clarifying whether the yield increase is statistically significant, sustained over multiple seasons, or applicable beyond the specific pilot cohort. The claim extrapolates from a small, localized pilot to broader farm yields without sufficient context. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
