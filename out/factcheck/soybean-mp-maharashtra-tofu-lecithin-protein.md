# Fact/interpretation check — soybean-mp-maharashtra-tofu-lecithin-protein

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/soybean-mp-maharashtra-tofu-lecithin-protein.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 98943, Requested 3483. Please try again in 34m56.063999999s. Need more tokens? Upgrade to Dev Tier today a]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India is one of the world's largest soybean growers by area" — This claim is vague and potentially misleading. While India is a major soybean grower, it is not among the *top* global producers by area (e.g., Brazil, Argentina, and the U.S. have larger soybean areas). The article later correctly states that MP and Maharashtra account for most of India's soybean area, but the initial claim overstates India's global ranking. [confidence: high]

- "National output for the 2025-26 oil year is estimated by SOPA at around 105.36 lakh tonnes, down roughly 16% from the prior season's 125.82 lakh tonnes" — The article does not provide a primary source for the "2025-26 oil year" estimate, and SOPA typically reports crop-year estimates (e.g., Kharif 2025). The 16% decline figure is not directly verifiable from the cited sources in the article. [confidence: medium]

INTERPRETATION ERRORS:
- "This is the same maize-for-ethanol pull this blog has covered from the ethanol side; here it shows up as an oilseed-acreage problem instead" — The article conflates two separate trends: maize's role as an ethanol feedstock (driving acreage shifts) and soybean's price weakness (due to floor price mismatches). While both contribute to reduced soybean acreage, the causal link between maize-for-ethanol and soybean acreage reduction is not directly supported by the data presented. The article does not provide evidence that ethanol demand is the *primary* driver of soybean acreage decline, only that it is "partly" responsible. [confidence: high]

- "Lecithin didn't require India to build a new industry. It required India to keep the one it already had for meal and oil, and sell what used to be a processing waste stream" — While lecithin is indeed a byproduct of oil refining, the claim that India "leads the world" in lecithin exports is not fully explained by this alone. The article does not address whether India's lecithin leadership is due to processing capacity, export infrastructure, or other factors (e.g., global demand shifts). The conclusion oversimplifies the reasons behind India's lecithin export dominance. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
