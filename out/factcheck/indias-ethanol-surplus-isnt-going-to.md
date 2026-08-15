# Fact/interpretation check — indias-ethanol-surplus-isnt-going-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-ethanol-surplus-isnt-going-to.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "The U.S. Grains & Bioproducts Council publishes a weekly ethanol and co-product pricing report sourced from World Perspectives, Inc. Its 7 January 2026 edition puts U.S. ethanol FOB Gulf at $1.698 per gallon — $0.449 per litre" — The conversion from gallons to liters seems incorrect, as 1 gallon is approximately 3.785 liters, so $1.698 per gallon would be approximately $0.448 per liter, but this is a minor discrepancy and may be due to rounding. [confidence: medium]
- "India's own EBP administered price (₹68/L) at current INR/USD — above both" — The exchange rate used is ₹95/$1 (August 2026), but the article does not specify if this rate is the exact rate used for the conversion of ₹68/L to $0.72/L. [confidence: low]

INTERPRETATION ERRORS:
- "The direction is nonetheless unambiguous: India's own government is already paying its distillers more than they'd fetch on the world market" — This statement assumes that the domestic price is the only factor determining the viability of export, ignoring other potential costs such as transportation, tariffs, and quality-grade differences. [confidence: high]
- "The practical case for pharma-grade diversification is that it doesn't require competing head-on with Brazilian sugarcane or U.S. corn economics on a commodity export market where India is structurally not the low-cost producer" — This statement implies that India's cost structure is not competitive in the global market, but it does not consider the potential for India to improve its cost competitiveness or the potential benefits of exporting to nearby countries. [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹68/L" — The article cites ₹68/L as the administered EBP procurement price, but the exchange rate used (₹95/$1) is dated August 2026, while the ethanol price data is from January 2026. The exchange rate in January 2026 was likely different, making the conversion to $0.72/L inaccurate. [confidence: high]

- "~57% India fuel-ethanol distillery utilisation on ~2,100 cr L capacity (CareEdge)" — The article does not provide a direct source or date for the 57% utilization figure, making it unverifiable. The claim lacks a clear citation or context. [confidence: medium]

INTERPRETATION ERRORS:
- "India's own government is already paying its distillers more than they'd fetch on the world market" — While the domestic EBP price (~$0.72/L) is higher than the U.S. benchmark (~$0.449/L), this comparison ignores landed costs (freight, tariffs, quality differences) and arbitrage realities. The claim assumes direct price parity without accounting for these factors, which could narrow or eliminate the gap in practice. [confidence: high]

- "The practical case for pharma-grade diversification is that it doesn't require competing head-on with Brazilian sugarcane or U.S. corn economics" — The article conflates *structural cost advantages* (e.g., feedstock access) with *regulatory/compliance barriers*. Pharma-grade ethanol requires significant capital and quality-control investments, which may not be trivial for Indian distillers, even if feedstock costs are lower. The claim oversimplifies the transition costs. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
