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

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99604, Requested 2583. Please try again in 31m29.568s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India has roughly 23.15 crore demat accounts as of June 2026" — The cited source (SBI Securities) reports 17.10 crore as of an earlier date, and the article itself notes this discrepancy ("cross-checked against more recent June 2026 industry reporting of 23.15 crore"). The 23.15 crore figure appears to be an estimate or projection, not a verified count. [confidence: high]

- "MRF Ltd (NSE, India's highest-priced listed stock) | ₹1,34,200 | 10 Aug 2026" — The price of ₹1,34,200 for MRF Ltd on 10 Aug 2026 is unverifiable against the cited source (StockAnalysis.com), which does not provide a date-specific price for that exact day. The article does not provide a primary source confirming this specific price on that date. [confidence: medium]

INTERPRETATION ERRORS:
- "Fractional ownership of an Indian-listed share is a different problem, and it's a legal one, not a plumbing one" — While the legal barrier is real, the article conflates the *legal* prohibition (Companies Act, 2013) with the *practical* barrier (e.g., custody, depository infrastructure). The claim implies the only issue is legal, but the Xaults sandbox pilot (admitted in July 2025) is testing a *custody model* to address the legal gap—suggesting the problem is not purely legal but also technical/operational. The framing oversimplifies the multi-faceted nature of the barrier. [confidence: high]

- "The inclusion case for fractional investing is real, but it's currently asymmetric" — The article correctly notes that fractional investing for US stocks is available while Indian stocks are not. However, the claim that this asymmetry *solely* reflects a lack of financial inclusion for Indian stocks is an overgeneralization. The asymmetry also stems from regulatory constraints (e.g., Companies Act) and market structure (e.g., high share prices), not just inclusion gaps. The framing risks attributing the entire problem to inclusion without acknowledging the regulatory and structural dimensions. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
