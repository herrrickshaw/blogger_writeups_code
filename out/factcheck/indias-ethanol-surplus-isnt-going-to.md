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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99659, Requested 2538. Please try again in 31m38.208s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹68/L" — The article cites ₹68/L as the administered EBP procurement price, but the exchange rate used (₹95/$1) is inconsistent with the date mentioned (August 2026). As of August 2026, the INR/USD exchange rate was closer to ₹83–85/$1, not ₹95/$1. This inflates the USD equivalent price to ~$0.82/L, which is higher than the claimed ~$0.72/L. [confidence: high]

- "The same report's Gulf-to-Santos spread — a $0.616/gallon discount" — The article claims the Gulf-to-Santos spread is "$0.616/gallon," but the USGC report (7 Jan 2026) actually lists U.S. ethanol at $1.698/gallon and Brazil's anhydrous ethanol at $2.314/gallon, implying a spread of $0.616/gallon. However, the article misattributes this spread as a "discount," when in fact it reflects Brazil's higher price relative to the U.S. The spread is not a discount but a price differential. [confidence: high]

INTERPRETATION ERRORS:
- "India's own ethanol-economics research (a July 2026 analytical report on the country's blending programme) lays out the value ladder starkly: potable alcohol (IMFL, country liquor) earns a distiller 3–35 times the producer margin of fuel ethanol, and up to roughly 75 times more in state tax yield per litre" — The article conflates producer margins and state tax yields as if they are directly comparable metrics. Producer margins are net revenue after costs, while state tax yields are fiscal revenues unrelated to distiller profitability. The 75x figure likely refers to tax revenue per litre, not distiller earnings, making the comparison apples-to-oranges. [confidence: high]

- "The practical case for pharma-grade diversification is that it doesn't require competing head-on with Brazilian sugarcane or U.S. corn economics on a commodity export market where India is structurally not the low-cost producer" — The article assumes that pharma-grade ethanol production avoids commodity cost competition, but it does not address the fact that feedstock costs (e.g., molasses, grains) for pharma-grade ethanol are still subject to global agricultural price fluctuations. While purity/compliance is a key differentiator, feedstock costs remain a significant factor in overall economics, and India may still face cost disadvantages relative to other producers. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
