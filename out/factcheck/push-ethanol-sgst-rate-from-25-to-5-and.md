# Fact/interpretation check — push-ethanol-sgst-rate-from-25-to-5-and

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/push-ethanol-sgst-rate-from-25-to-5-and.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "PPAC's state-wise annual Motor Spirit (petrol) sales data (FY2024-25, the latest full year published)" — FY2024-25 is an incomplete/ongoing fiscal year (April 2024 – March 2025) and full-year annual sales data cannot be published as a completed financial year; the latest full published fiscal year for PPAC annual consumption data is FY2023-24. [confidence: high]
- "Uttar Pradesh tops this list on volume alone — it's India's largest petrol market by PPAC's own figures" — Per official PPAC state-wise petroleum consumption data, Maharashtra is consistently India's largest market for Motor Spirit (petrol), not Uttar Pradesh. While UP is the top consumer for diesel (HSD), it ranks second to Maharashtra in petrol sales. [confidence: high]

INTERPRETATION ERRORS:
- "This method reproduces the companion piece's own published figures almost exactly (Maharashtra: 5.91 billion litres of petrol-equivalent volume in that piece vs. 5.91 billion litres independently recomputed here from the raw PPAC file; Karnataka: 0.83 billion litres of ethanol in both) — confirming the two pieces are directly comparable rather than using silently different assumptions." — This is an apples-to-oranges comparison of different metrics to validate consistency. It compares Maharashtra's total petrol sales volume (5.91 billion litres) directly against Karnataka's ethanol blend volume (0.83 billion litres, derived from ~4.15 billion litres of petrol). Equating a total petrol volume metric for one state with an ethanol volume metric for another does not logically verify that identical calculation assumptions were applied across both states. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "In June 2024, Karnataka raised its own state sales tax on petrol from 25.92% to 29.84% and on diesel from 14.34% to 18.44%, a straight ₹3/litre increase, expected to earn the state an additional ₹2,500–3,000 crore a year." — The article does not provide a primary source to verify this information, and it may not be accurate. [confidence: medium]
- "petroleum products are explicitly outside GST" — This statement may be outdated or incorrect, as the article does not provide a primary source to verify this information. [confidence: medium]

INTERPRETATION ERRORS:
- "Pushing the rate from today's 2.5% to 10% would earn Uttar Pradesh, Maharashtra and Tamil Nadu each several hundred crore a year in extra SGST — genuinely worth pursuing — but at the national level it recovers well under half of the ₹17,865 crore states already lose to ethanol blending at E20, even at rates well above what's currently being discussed." — The article concludes that pushing the rate is "genuinely worth pursuing" based on the potential earnings for a few states, but it does not consider the potential impact on other states, consumers, or the overall economy. [confidence: high]
- "Karnataka's 2024 VAT hike proves states can and will raise fuel taxes unilaterally when the lever is in their own hands; ethanol's SGST split isn't in any single state's hands, which is exactly why this blog's structural-fix piece argues the real solution runs through GST Council reclassification, not a state-by-state rate push." — The article uses Karnataka's VAT hike as evidence that states can raise fuel taxes, but it does not consider the differences between VAT and SGST, or the potential challenges of implementing a national solution through the GST Council. [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Karnataka's June 2024 petrol/diesel VAT hike (25.92%→29.84% petrol, 14.34%→18.44% diesel)" — The VAT rates cited (25.92%→29.84% for petrol and 14.34%→18.44% for diesel) are incorrect. Karnataka's actual VAT hike in June 2024 was a flat ₹3/litre increase, not a percentage-point change. The rates provided in the article do not match official reports or government announcements. [confidence: high]

- "₹17,865 crore net state VAT shortfall" — The article does not provide a clear source or methodology for this figure, and it is not verifiable against publicly available data or official reports. The claim appears to be an internal model estimate without external corroboration. [confidence: medium]

INTERPRETATION ERRORS:
- "Even at 15%, this is a smaller number than the ₹17,865 crore net state VAT shortfall this blog's companion piece calculated at the same E20 blend — consistent with that piece's own finding that full parity via an ethanol-only rate would need something close to 27%" — The article assumes that the ethanol SGST rate alone can offset the VAT shortfall from ethanol blending, but this is a false causal claim. The VAT shortfall arises from the difference between the tax on blended petrol (which includes ethanol) and the tax on pure petrol, while the SGST on ethanol is a separate levy. The two are not directly comparable or substitutable in the way implied. [confidence: high]

- "Karnataka's hike is useful evidence that fuel taxation is politically viable to raise when a state controls the lever directly — it is not evidence that the GST Council would agree to reweight the CGST:SGST split specifically for ethanol" — The article correctly notes that Karnataka's VAT hike is not directly transferable to ethanol's SGST split, but it incorrectly implies that the GST Council's decision-making process is the only obstacle. The interpretation overlooks that ethanol's SGST rate is part of the GST framework, and any change would require broader consensus beyond just the GST Council's weighted-majority vote, including political and economic considerations. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
