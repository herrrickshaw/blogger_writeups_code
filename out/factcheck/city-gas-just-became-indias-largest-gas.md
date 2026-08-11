# Fact/interpretation check — city-gas-just-became-indias-largest-gas

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/city-gas-just-became-indias-largest-gas.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "...leading in May and June individually." / "May 2026 was the first month; June confirmed it; the quarter settled it." — According to Exhibit 2 in the article's own data, CGD consumed 1,482 MMSCM in April 2026 compared to fertiliser's 1,400 MMSCM. Thus, CGD led fertiliser in April as well, making April (not May) the first month of the crossover, with CGD leading in all three months individually. [confidence: high]

INTERPRETATION ERRORS:
- "CGD did not become number one by racing a growing market; it became number one because everything else stalled or shrank while it kept compounding." — Over the decade analyzed in Exhibit 1, total gas consumption expanded significantly (+44.3%, from 47,849 to 69,048 MMSCM). Other major sectors did not stall or shrink: fertiliser grew by 21.8% (16,135 to 19,649 MMSCM) and "Other/miscellaneous" grew by 126% (4,298 to 9,716 MMSCM). The author incorrectly generalizes a single year of pool contraction (FY2025-26) to explain a decade-long shift that actually occurred within an expanding market. [confidence: high]
- "What makes the crossover structural rather than cyclical is what each side is doing: in FY2025-26, within a national pool that shrank 3.0% , CGD grew +9.7% while fertiliser fell 4.1% and power fell 10.5%." — A single year of growth divergence (FY2025-26) cannot establish that a crossover is permanent/structural rather than cyclical, as fertiliser and power demand fluctuate with weather and seasonal cycles. Moreover, the article directly contradicts this assertion in its note to Exhibit 2, acknowledging that "a strong Rabi fertiliser season could still flip individual months back." [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "India's gas is now majority imported : RLNG supplied 51.5% of consumption in FY2025-26 and 52.7% in Q1 FY2026-27, with PPAC putting overall import dependency at roughly 50% in both FY2024-25 and FY2025-26." — The claim of 50% import dependency is not directly supported by the provided data, which only mentions RLNG supply percentages and not the overall import dependency, although it is mentioned that PPAC puts it roughly at 50% [confidence: medium]
- "1,72,55,095 domestic PNG connections as of 31.05.2026" — The article mentions 1.73 crore domestic PNG connections, which translates to 17,300,000, not 1,72,55,095 [confidence: high]

INTERPRETATION ERRORS:
- "CGD is the only large sector still compounding — and the infrastructure behind it explains why: 8,980 CNG stations and 1.73 crore domestic PNG connections as of 31 May 2026" — The claim implies a direct causal relationship between the infrastructure (CNG stations and PNG connections) and CGD's growth, but it does not account for other potential factors that could be driving this growth, such as changes in consumer behavior, government policies, or economic conditions [confidence: medium]
- "The crossover, month by month ... May 2026 was the first month; June confirmed it; the quarter settled it." — The article interprets the crossover in gas consumption between CGD and fertiliser as a structural change, but it does not consider the possibility that this crossover could be due to seasonal fluctuations or other temporary factors, rather than a long-term trend [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "4,964 vs 4,703 CGD vs fertiliser, Q1 FY2026-27, MMSCM" — The article states these figures as exact values, but they are presented in the table as provisional data (e.g., "Q1 FY2026-27, provisional"). The claim implies certainty where the source itself acknowledges provisional status. [confidence: high]

- "8,980 CNG stations and 1.73 crore domestic PNG connections as of 31 May 2026" — The article cites "1,72,55,095 domestic PNG connections" in the sources section, which is 1.7255095 crore, not 1.73 crore. The rounding is inconsistent with the precise figure provided elsewhere. [confidence: high]

INTERPRETATION ERRORS:
- "CGD is the only large sector still compounding — and the infrastructure behind it explains why" — While CGD grew (+9.7% in FY2025-26) while other sectors shrank, the article does not establish a causal link between CGD's infrastructure (e.g., CNG stations, PNG connections) and its growth. The infrastructure may facilitate growth, but the claim implies causation without evidence. [confidence: medium]

- "The gas-fired fleet is the oldest member of the club" — The article notes that gas power's share halved and absolute burn declined, but it does not provide data on the age of the gas-fired fleet or compare it to other sectors. The claim is an unsupported extrapolation. [confidence: low]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
