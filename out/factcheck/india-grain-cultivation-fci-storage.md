# Fact/interpretation check — india-grain-cultivation-fci-storage

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-grain-cultivation-fci-storage.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "the storage belt and the FPO belt are different states . Madhya Pradesh has both (200 LMT storage, 348 FPOs); Punjab has 174 LMT of storage but only 78 FPOs; Uttar Pradesh has 758 FPOs (the most of any state) but a fraction of MP's storage." — The article uses FPO registry data exclusively from SFAC (Small Farmers' Agribusiness Consortium), representing only ~3,649 FPOs out of roughly 45,000+ FPOs nationwide (where the majority are promoted by NABARD, NCDC, and state-level agencies). Drawing broad conclusions about the geographical distribution of India's entire "FPO belt" based on a single implementing agency's registry is an invalid extrapolation from an unrepresentative subset. Furthermore, FCI covered storage is dedicated to centralized public buffer stocking and MSP procurement operations (principally wheat and rice), whereas FPOs are decentralized farmer collectives covering diverse agricultural commodities; treating their geographic non-alignment as a structural mismatch compares two fundamentally different policy and logistics mechanisms. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Punjab has 569 FCI depots but only 78 FPOs" — The article later states that Punjab has 174.5 LMT storage, 78 FPOs, and 569 FCI depots, which seems to be consistent, but without external verification, it's unclear if these numbers are accurate [confidence: medium].
- "Uttar Pradesh has 758 FPOs (the most of any state)" — According to the article, the India-wide FPO count is ~45,000 across all promoting agencies, and the SFAC channel only has 3,649 FPOs, but it does not provide an external source to verify that Uttar Pradesh indeed has the most FPOs [confidence: medium].

INTERPRETATION ERRORS:
- "the storage belt and the FPO belt are different states" — This conclusion is based on the observation that some states have high storage capacity but low FPO counts, and vice versa, but it does not consider other factors that might influence the relationship between storage and FPOs, such as agricultural production, market demand, or government policies [confidence: high].
- "Madhya Pradesh has both (200 LMT storage, 348 FPOs)" — The article presents Madhya Pradesh as an example of a state with both high storage capacity and a high number of FPOs, but it does not explain why this is significant or what it implies about the relationship between storage and FPOs [confidence: medium].

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Punjab has 569 FCI depots but only 78 FPOs" — The article later lists Punjab as having 569 FCI depots and 78 FPOs, but the initial claim in the schematic state map states "Punjab has 569 FCI depots but only 78 FPOs" (correct), while the later detailed list confirms the same numbers. No factual error found here. [confidence: high]
- "Madhya Pradesh is the one with both" — The article later specifies Madhya Pradesh has 200.4 LMT storage and 348 FPOs, confirming it has both storage and FPOs. No factual error found here. [confidence: high]

INTERPRETATION ERRORS:
- "the storage belt and the FPO belt are different states" — The article implies that the "storage belt" and "FPO belt" are distinct geographic phenomena based on the data, but it does not provide a clear definition of what constitutes a "belt" or the criteria for inclusion in either belt. The claim assumes a categorical distinction without explaining the thresholds or methodology used to define these belts. [confidence: high]
- "Uttar Pradesh has 758 FPOs (the most of any state) but a fraction of MP's storage" — While Uttar Pradesh has the highest number of FPOs (758), the claim that it has "a fraction of MP's storage" is misleading because Uttar Pradesh's storage (47.2 LMT) is not a "fraction" of Madhya Pradesh's storage (200.4 LMT) in a strict mathematical sense (47.2 is roughly 23.5% of 200.4, which is a significant portion, not a "fraction"). The phrasing suggests a much smaller proportion than the data supports. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
