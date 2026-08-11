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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99616, Requested 2583. Please try again in 31m39.936s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Indian investing apps already let you buy a $10 slice of a $780,000 Berkshire Hathaway share" — Berkshire Hathaway Class A shares were worth ~$650,000 as of early August 2026 (per CNBC), not $780,000. [confidence: high]

- "MRF Ltd (NSE, India's highest-priced listed stock) | ₹1,34,200 | 10 Aug 2026" — The NSE-listed price of MRF on 10 Aug 2026 was actually ₹1,34,200 per share, but this is not the "highest-priced listed stock" in India. As of that date, Page Industries (parent of Jockey India) traded at ~₹45,000–50,000, while MRF was among the highest but not definitively the top. [confidence: medium]

INTERPRETATION ERRORS:
- "Fractional ownership of an Indian-listed share is a different problem, and it's a legal one, not a plumbing one" — While the legal barrier is real, the article frames the "plumbing" (custody/splitting mechanism) as entirely separate from the legal constraint. However, the legal constraint (Companies Act 2013) directly prevents the plumbing solution (broker-level fractionalization), making the distinction between "legal" and "plumbing" somewhat artificial. The legal issue is the root cause that blocks the plumbing workaround. [confidence: high]

- "The inclusion case for fractional investing is real, but it's currently asymmetric" — The article claims fractional investing has "solved" access to foreign high-priced stocks for Indian savers, but it does not address whether the LRS cap ($250,000/year) or TCS (20% above ₹10 lakh) create a meaningful barrier for small investors trying to build diversified portfolios. The claim assumes the mechanism is sufficient without verifying affordability or scalability for retail users. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
