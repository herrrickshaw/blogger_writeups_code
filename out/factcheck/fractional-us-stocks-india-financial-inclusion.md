# Fact/interpretation check — fractional-us-stocks-india-financial-inclusion

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fractional-us-stocks-india-financial-inclusion.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99687, Requested 2583. Please try again in 32m41.28s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India has roughly 23.15 crore demat accounts as of June 2026" — The cited source (SBI Securities) reports 23.15 crore demat accounts as of June 2026, but the article itself notes this is a cross-check against "more recent June 2026 industry reporting," implying the figure may not be final or officially confirmed. The claim is unverified against a primary regulatory source (e.g., SEBI or CDSL/NSDL). [confidence: medium]

- "over 2.5 million added in June 2026 alone, the highest monthly count in months" — The article does not provide a source for this specific monthly addition figure, and it is not corroborated by the cited sources (e.g., SBI Securities or other industry reporting). The claim lacks verifiable evidence. [confidence: low]

INTERPRETATION ERRORS:
- "Fractional ownership of an Indian-listed share is a different problem, and it's a legal one, not a plumbing one" — While the legal barrier is correctly identified, the article conflates the *legal* issue (fractional shares not being recognized under the Companies Act) with the *operational* challenge of custody. The Xaults sandbox pilot (admitted in July 2025) is framed as addressing the legal issue by testing a depository-level custody model, but the article does not clarify that the legal amendment (Companies Act) is still pending. The claim implies the legal barrier is purely a "plumbing" issue solvable by custody models, which is an oversimplification. [confidence: high]

- "The inclusion case for fractional investing is real, but it's currently asymmetric" — The article correctly notes that fractional investing for US stocks is available while Indian stocks are not, but it does not address the *quantitative* impact of this asymmetry on financial inclusion. For example, it does not provide data on how many Indian retail investors actually use fractional US stock investing or the proportion of demat accounts that could benefit from domestic fractional shares. The claim is presented as a broad conclusion without supporting evidence or context. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
