# Fact/interpretation check — fci-grain-flow-procurement-storage

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fci-grain-flow-procurement-storage.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "PIB Year-End Review 2025" — A Year-End Review for 2025 cannot exist as a cited source for a report displaying data as of November 2024 / January 1, 2025. [confidence: high]
- "Wheat procured — RMS 2025-26 300.35 LMT" — Rabi Marketing Season (RMS) 2025-26 procurement takes place in spring/summer 2025; completed procurement cannot be reported as an established fact alongside January 1, 2025 stock figures. Additionally, the sub-bullet immediately references "RMS 2024-25", indicating a season mislabeling error. [confidence: high]

INTERPRETATION ERRORS:
- "476.85 LMT vs 214.1 LMT buffer norm · +~319 LMT unmilled paddy" — Presenting gross unmilled paddy tonnage (~319 LMT) alongside milled central pool stocks and buffer norms is an apples-to-oranges comparison. Paddy yields approximately 67% milled rice (~214 LMT rice equivalent), so adding raw paddy weight directly overstates the actual grain stock available to meet milled buffer requirements. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Punjab ≈ 47% of the RMS 2024-25 wheat pool" — The article states the wheat procurement data is for RMS 2025-26, but the percentage of Punjab's contribution is mentioned for RMS 2024-25, which is inconsistent and may be incorrect due to the mismatch in the marketing seasons mentioned [confidence: medium]
- "Food subsidy released — FY25 ₹1.99 lakh cr" — Without access to the primary sources (DFPD Foodgrain Bulletin, DFPD Annual Report 2024-25, PIB Year-End Review 2025) for verification, it's unclear if this figure is accurate or up-to-date [confidence: low]

INTERPRETATION ERRORS:
- "Central pool stocks — 1 Jan 2025 476.85 LMT vs 214.1 LMT buffer norm · +~319 LMT unmilled paddy" — The comparison between the central pool stocks and the buffer norm might imply that the excess (+~319 LMT) is solely unmilled paddy, which could be misleading if the buffer norm includes both milled and unmilled grains, or if the excess has other implications not directly related to unmilled paddy [confidence: medium]
- "Paddy procured — KMS 2024-25 832.17 LMT record · ~1.19 crore farmers paid" — The statement implies a direct relationship between the record paddy procurement and the number of farmers paid, but it does not account for other factors that could influence these numbers, such as changes in procurement policies, market conditions, or farmer participation rates [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Rice 2024-25 procurement is the official Economic Survey rice-terms figure (544.8 LMT)" — The article cites this figure as part of the data sources but does not explicitly state it as a procurement figure in the main text. The procurement figure for paddy in KMS 2024-25 is given as 832.17 LMT, which, when milled, would typically yield less rice (roughly 60-65% of paddy weight). The claim that "Rice 2024-25 procurement is 544.8 LMT" is not directly supported by the data presented in the article and may be an incorrect extrapolation or misattribution. [confidence: high]

INTERPRETATION ERRORS:
- "Punjab ≈ 47% of the RMS 2024-25 wheat pool" — The article states this as a fact but does not provide the total RMS 2024-25 wheat pool figure or the methodology to derive Punjab's share. Without the total pool size or a clear breakdown, this percentage cannot be verified or logically supported by the data presented. The claim assumes a specific calculation that is not explained or sourced in the text. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
