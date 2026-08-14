# Fact/interpretation check — india-environmental-clearances-state

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-environmental-clearances-state.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "PARIVESH 2.0's open API — 113,970 proposals (2022–2026)" / "Source: PARIVESH 2.0 open API, full EC register, fetched 22 Jul 2026." — The date cited (22 July 2026) and the time span ending in 2026 are future dates, making the timeframe and data retrieval date factually impossible. [confidence: high]

INTERPRETATION ERRORS:
- "Fresh vs reuse — only 49% are new projects; 22% are mostly re-appraisals of expiring minor-mineral leases on the same plots, plus transfers, expansions and amendments." — In a fresh vs. reuse classification, if fresh projects account for 49%, the non-fresh/reuse share should account for the remaining 51%. Stating that re-appraisals, transfers, expansions, and amendments account for only 22% leaves 29% of total proposals unaccounted for, likely duplicating the 22% auto-delisting attrition figure from the funnel analysis. [confidence: high]
- "Real attrition here isn't rejection — it's auto-delisting and pipeline backlog..." — Treating a "pipeline backlog" as part of the approval process's "attrition" is an extrapolation error; backlogged proposals are pending or under active review in the appraisal queue, not terminated or rejected applications. [confidence: medium]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "88.7% grant rate of decided proposals" — cannot verify against what is known, as the article does not provide enough context or information about the source of this statistic, although it does mention that the data comes from the PARIVESH 2.0 open API [confidence: medium]
- "only 10.7% of decided wildlife proposals are granted" — cannot verify against what is known, as the article does not provide enough information about the source of this statistic, although it does mention that it is covered in the companion post Forest, Wildlife & CRZ Clearances [confidence: medium]

INTERPRETATION ERRORS:
- "The headline 88.7% grant rate makes India's EC process look more permissive than the underlying dynamics suggest" — the article concludes that the EC process is not as permissive as the grant rate suggests, but it does so based on the presence of auto-delisting and pipeline backlog, which may not necessarily be the primary factors influencing the grant rate [confidence: medium]
- "that fresh-vs-reuse split is the number that actually matters, and the state × sub-sector breakdown shows where the concentration sits" — the article implies that the fresh-vs-reuse split is the most important factor in understanding new industrial capacity, but it does not provide sufficient evidence to support this claim, and other factors may also be relevant [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "113,970 proposals (2022–2026)" — The date range is incorrect as the data is fetched on 22 Jul 2026, meaning the latest proposals could extend beyond 2026. The claim implies all proposals are within 2022–2026, which is unverifiable without knowing the exact submission dates. [confidence: high]

- "88.7% grant rate of decided proposals" — The article does not clarify whether "decided proposals" includes auto-delisted cases, which are mentioned as a major attrition factor. If auto-delisted proposals are excluded from "decided," the grant rate could be misleadingly high. [confidence: medium]

INTERPRETATION ERRORS:
- "The headline 88.7% grant rate makes India's EC process look more permissive than the underlying dynamics suggest." — While the grant rate is high, the article does not provide evidence that this rate is unusually permissive compared to historical trends or other countries' EC processes. The claim assumes the rate is high without a benchmark. [confidence: high]

- "only about half of all proposals are genuinely new projects rather than re-appraisals, transfers, expansions and amendments of the same underlying assets." — The article does not explain why this split (49% fresh) is problematic for measuring new industrial capacity. It assumes that re-appraisals/expansions do not contribute to new capacity, which may not be true (e.g., expansions could represent new investment). [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
