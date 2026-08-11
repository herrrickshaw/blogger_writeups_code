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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99631, Requested 3102. Please try again in 39m21.312s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹68/L" — The article cites ₹68/L as the administered price for ethanol under the EBP programme, but the exchange rate used (₹95/$1) is dated August 2026, which is inconsistent with the 7 January 2026 price benchmark data for US and Brazil ethanol. The exchange rate should align with the January 2026 date for consistency in the comparison. [confidence: high]

- "DGFT Notification No. 32/2025-26 (24 September 2025)" — The notification number format (e.g., "32/2025-26") is incorrect for Indian government notifications, which typically follow a different numbering convention (e.g., "No. 32/2025-26" or similar). The date format is also unusual. [confidence: medium]

INTERPRETATION ERRORS:
- "India's own ethanol-economics research (a July 2026 analytical report on the country's blending programme) lays out the value ladder starkly: potable alcohol (IMFL, country liquor) earns a distiller 3–35 times the producer margin of fuel ethanol, and up to roughly 75 times more in state tax yield per litre — which is exactly why capacity gravitates to liquor wherever licensing allows it." — The claim conflates producer margins and state tax yields, which are distinct financial metrics. Producer margins (revenue minus cost) and tax yields (government revenue) are not directly comparable in terms of "value per litre" for a distiller's decision-making. The reasoning gap is that the article treats these as equivalent metrics when they serve different economic purposes. [confidence: high]

- "The practical case for pharma-grade diversification is that it doesn't require competing head-on with Brazilian sugarcane or U.S. corn economics on a commodity export market where India is structurally not the low-cost producer." — The claim assumes that pharma-grade ethanol production is entirely decoupled from feedstock costs (e.g., sugarcane or corn), but high-purity ethanol production still depends on feedstock availability and pricing. While compliance and quality control are critical, feedstock costs remain a significant factor in the overall economics. The reasoning gap is that the article overstates the independence of pharma-grade ethanol from commodity feedstock economics. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
