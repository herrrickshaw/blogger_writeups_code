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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99255, Requested 2583. Please try again in 26m28.032s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Indian investing apps already let you buy a $10 slice of a $780,000 Berkshire Hathaway share." — The article later states Berkshire Hathaway Class A shares are worth ~$780,000 *as of early Aug 2026*, but the claim here is presented without a date, making it unclear if this is current or outdated. [confidence: medium]

- "India has roughly 23.15 crore demat accounts as of June 2026" — The source cited (SBI Securities) mentions "Total Number of Demat Accounts in India Exceed 17.10 crore mark," with the 23.15 crore figure described as "more recent June 2026 industry reporting." This is inconsistent, as the SBI Securities report is older and does not explicitly confirm the 23.15 crore figure. [confidence: high]

INTERPRETATION ERRORS:
- "Fractional investing hasn't closed that gap yet" — The article conflates the *legal availability* of fractional Indian shares (which is not yet permitted) with the *practical accessibility* of fractional US shares (which is already possible). The claim implies fractional investing is uniformly unavailable in India, ignoring the asymmetry between domestic and foreign markets. [confidence: high]

- "The inclusion case for fractional investing is real, but it's currently asymmetric." — While the asymmetry between foreign and domestic fractional investing is correctly noted, the article does not sufficiently emphasize that the *primary barrier* for Indian stocks is a *legal one* (Companies Act, 2013), not a technical one. The framing risks misleading readers into thinking the issue is merely operational rather than regulatory. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
