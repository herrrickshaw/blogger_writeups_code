# Fact/interpretation check — india-ec-approval-funnel-parivesh-20

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-ec-approval-funnel-parivesh-20.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 429: {"error":{"message":"Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99780, Requested 1176. Please try again in 13m45.984s. Need more tokens? Upgrade to Dev Tier today at http]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Grant rate of DECIDED proposals: 88.7%" — The calculation appears incorrect. The article defines "decided proposals" as those that have reached a decision (61,360 total), with 54,406 granted and 6,954 not approved (2,553 rejected + 2,622 withdrawn + 1,779 returned). The correct grant rate should be 54,406 / 61,360 ≈ 88.67%, which rounds to 88.7%. However, the article's phrasing ("Grant rate = granted ÷ decided") is technically correct, but the claim itself is accurate. No factual error found here.
- "56 raw PARIVESH status values consolidated into canonical process stages" — The article does not provide evidence or a source to verify this claim about the number of raw status values. Without confirmation from the PARIVESH 2.0 API documentation or the cited "full EC register," this cannot be verified. [confidence: medium]

INTERPRETATION ERRORS:
- "Only 49% of these EC proposals are fresh new projects. The rest are activity on land that already holds a clearance: 22% are re-appraisals (mostly minor-mineral mining leases expiring and re-cleared on the same plots), plus transfers of EC to new owners, expansions of existing plants, and amendments." — The article correctly states that 54,406 ECs were granted out of 113,970 proposals, but it does not provide a source or methodology for the claim that "only 49% are fresh new projects." The 49% figure appears to be derived from an unstated assumption (e.g., 54,406 granted proposals × 49% = ~26,659 fresh projects), but there is no evidence or data in the article to support this breakdown. The claim implies a causal or definitional link between the granted proposals and the types of projects, but the data does not distinguish between fresh projects and other activities. [confidence: high]
- "The real attrition is auto-delisting (22%) and pipeline backlog (31% of live still pending) - not rejection." — While the attrition rates are correctly calculated (25,061 auto-delisted out of 113,970 filed = 22%; 27,548 pipeline backlog out of 88,909 live = ~31%), the conclusion that "rejection" is not a major attrition factor is misleading. The article notes that 6,954 proposals were not approved (6.1% of filed), which is a non-trivial attrition rate. The framing downplays the role of rejection by comparing it to auto-delisting and backlog, but the data does not support the claim that rejection is insignificant. The interpretation conflates "attrition" (any loss of proposals) with "rejection" (a specific outcome), creating a false dichotomy. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
