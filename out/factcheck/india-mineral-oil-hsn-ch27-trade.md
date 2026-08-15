# Fact/interpretation check — india-mineral-oil-hsn-ch27-trade

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-mineral-oil-hsn-ch27-trade.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "121.1 MMT Crude imported (FY25-26 H1)" — This claim cannot be verified against publicly available data as of my knowledge cutoff, and the article itself mentions that the data is provisional and based on half-year columns. [confidence: medium]
- None found for other factual errors.

INTERPRETATION ERRORS:
- "The landed-cost stack a trader must build before quoting. Duty rates change by notification — verify on CBIC/ICEGATE before costing a real cargo." — This statement implies that traders can easily verify duty rates, but it does not account for potential complexities or nuances in the verification process, such as changes in notification or varying interpretations of the rules. [confidence: medium]
- None found for other interpretation errors.

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "121.1 MMT Crude imported (FY25-26 H1)" — The claim is unverifiable as FY25-26 H1 data is provisional and not yet finalized in official sources like PPAC or DGCI&S. The article itself notes FY25-26 is provisional in the caveats section. [confidence: high]

- "$203.4B Ch.27 imports FY25-26 (26.2% of all imports)" — The 26.2% share is likely incorrect because Chapter 27 includes coal, LNG, and electricity alongside petroleum, which are not part of "all imports" in standard trade statistics. The share calculation appears to double-count or misclassify these non-petroleum items. [confidence: high]

INTERPRETATION ERRORS:
- "80 : 20 Trade Parity Price = IPP : EPP weight" — The claim implies a direct causal relationship between the 80:20 ratio and the Trade Parity Price (TPP) formula, but the TPP formula (TPP = 0.80 × IPP + 0.20 × EPP) is a pricing mechanism for sensitive products (MS, HSD), not a trade balance metric. The 80:20 ratio is not a trade parity weight but a pricing weight, and conflating the two misrepresents the purpose of the formula. [confidence: high]

- "Gas (Kirit Parikh 2023): APM gas sloped to the same Indian crude basket, floor $4 / ceiling $6.5 per MMBtu (+$0.5/yr), difficult fields cap $12.46 — one crude commodity anchors crude, LPG, MS, HSD and gas." — The claim suggests a single crude commodity price (Indian basket) directly anchors the pricing of gas, LPG, MS, and HSD, but this ignores the distinct pricing mechanisms for each product (e.g., LPG uses Saudi Aramco CP, gas uses APM with its own formula). The "one crude commodity anchors" phrasing implies an oversimplified causal link that does not reflect the actual multi-benchmark pricing structure. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
