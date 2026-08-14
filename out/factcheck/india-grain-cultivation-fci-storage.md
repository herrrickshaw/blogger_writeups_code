# Fact/interpretation check — india-grain-cultivation-fci-storage

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-grain-cultivation-fci-storage.html`

## Gemini gemini-flash-latest

[Gemini API error 503: {
  "error": {
    "code": 503,
    "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
    "status": "UNAVAILABLE"
  }
}
]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Madhya Pradesh has 200 LMT storage" — The article does not provide a primary source to verify this specific number, and the source data is mentioned as "national_fci_fpo_by_state.csv (FCI-warehouse-MSPvsMSV repo)", which may not be accessible for verification [confidence: medium]
- "Uttar Pradesh has 758 FPOs (the most of any state)" — The article mentions that the FPO count is from the "SFAC 10,000-FPO registry, 24-02-2025" which reports 3,649 FPOs in the SFAC channel, but it also mentions that the India-wide FPO count is "~45,000 across all promoting agencies", which may indicate that the number of FPOs in Uttar Pradesh might not be the highest when considering all promoting agencies [confidence: medium]

INTERPRETATION ERRORS:
- "the storage belt and the FPO belt are different states" — This conclusion is based on the comparison of storage capacity and FPO counts across states, but it does not consider other factors that might influence the difference, such as the type of crops grown, agricultural policies, or geographical characteristics [confidence: high]
- "Punjab has 174 LMT of storage but only 78 FPOs" — This statement is used to support the idea that the storage belt and FPO belt are different, but it does not account for the fact that Punjab is a major wheat-producing state and might have different storage and FPO requirements compared to other states [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Punjab has 569 FCI depots but only 78 FPOs" — The article text later contradicts this by stating Punjab has 569 FCI depots but only 78 FPOs, which is consistent. However, the initial claim in the schematic state map section ("Punjab has 569 FCI depots but only 78 FPOs") is accurate based on the later detailed list. No factual error found here. [confidence: high]
- "FCI covered storage, Nov 2024 (LMT)" — The article mentions "~841 LMT all-India, all agencies" but the state-by-state figures do not sum to this total (e.g., Madhya Pradesh 200.4 + Punjab 174.5 + Haryana 100.2 + Uttar Pradesh 47.2 + Chhattisgarh 35.5 + Andhra Pradesh 24.6 + Telangana 24.4 + Maharashtra 24.3 + Bihar 20.9 + Tamil Nadu 20.9 + West Bengal 20.0 + Rajasthan 16.4 = ~768.9 LMT, excluding other states). This discrepancy suggests either missing data or double-counting in the all-India total. [confidence: high]

INTERPRETATION ERRORS:
- "the storage belt and the FPO belt are different states" — While the data shows a spatial mismatch between storage capacity and FPO density across states, the article does not provide evidence or reasoning to support the causal claim that this mismatch is problematic or requires policy intervention. The observation alone does not justify the conclusion that this is a systemic issue. [confidence: medium]
- "Madhya Pradesh has both (200 LMT storage, 348 FPOs)" — The article implies that Madhya Pradesh's dual advantage in storage and FPOs is a positive or optimal outcome, but it does not explain why this combination is desirable or how it benefits farmers or the agricultural supply chain. The presence of both does not inherently validate their effectiveness or efficiency. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
