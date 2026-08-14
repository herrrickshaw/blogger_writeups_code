# Fact/interpretation check — india-ec-approval-funnel-parivesh-20

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-ec-approval-funnel-parivesh-20.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The real attrition is auto-delisting (22%) and pipeline backlog (31% of live still pending) - not rejection." — Conflating active pipeline backlog with "attrition." Applications currently pending review across ToR, screening, and appraisal are ongoing work-in-progress, not lost or terminated proposals (attrition). [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "113,970 EC proposals" — The article does not provide a source to verify this specific number, but it does mention that the data comes from the PARIVESH 2.0 open API, which may be a reliable source. However, without direct access to the API or more information about the data collection, the accuracy of this number cannot be confirmed. [confidence: medium]
- None other found.

INTERPRETATION ERRORS:
- "The real attrition is auto-delisting (22%) and pipeline backlog (31% of live still pending) - not rejection." — This statement implies that auto-delisting and pipeline backlog are the primary causes of proposal failure, while rejection is not a significant factor. However, the article also states that 6,954 proposals were not approved, which includes 2,553 rejections. This number, although smaller than auto-delisted and pending proposals, still represents a significant portion of proposals that did not move forward. The statement may downplay the importance of rejection as a factor in proposal failure. [confidence: medium]
- None other found.

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Only 49% of these EC proposals are fresh new projects" — The article does not provide a source or methodology to verify this claim. The percentage appears to be an unsupported assertion rather than a verified fact. [confidence: low]

INTERPRETATION ERRORS:
- "Grant rate of DECIDED proposals: 88.7%" — The claim that "once a proposal reaches a decision, it is overwhelmingly approved" is an overgeneralization. The grant rate is calculated as granted ÷ decided, but the article does not account for the fact that "decided" proposals may include withdrawn or returned applications, which are not rejections but also not approvals. This inflates the perceived approval rate. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
