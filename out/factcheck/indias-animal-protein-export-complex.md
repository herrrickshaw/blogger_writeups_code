# Fact/interpretation check — indias-animal-protein-export-complex

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-animal-protein-export-complex.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Roughly 513 plants across the country carry this export registration, current as of APEDA's most recent published list (July 2026)." / "Seafood exports hit an all-time high of ₹72,325.82 crore (~$8.28 billion) in FY2025-26..." — July 2026 and FY2025-26 are future dates; completed fiscal year export statistics and APEDA published lists cannot exist for these periods. [confidence: high]

INTERPRETATION ERRORS:
- "By share of India's overall meat production, West Bengal (12.62%), Uttar Pradesh (12.29%), Maharashtra (11.28%), Telangana (10.85%) and Andhra Pradesh (10.41%) together account for well over half the national total." — The author uses aggregate national meat production data (which is heavily dominated by poultry and includes sheep, goat, and pork) to explain the geographic concentration of the buffalo-meat (carabeef) export trade. States like West Bengal lead in overall meat production due to poultry and goat meat, not export-oriented buffalo processing, creating an apples-to-oranges conflation. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "₹72,325.82cr Record India seafood export value, FY2025-26 (~$8.28bn, MPEDA)" — The fiscal year notation is inconsistent. FY2025-26 is the same as FY2026, but the article later mentions "FY2025-26" for seafood exports and "FY2024-25" for buffalo meat exports. This creates confusion about the actual fiscal year referenced for seafood exports. [confidence: high]

- "₹47,973.13cr Frozen shrimp alone — roughly two-thirds (66.3%) of total seafood export earnings" — The percentage (66.3%) does not match the implied calculation from the given figures. ₹47,973.13cr / ₹72,325.82cr ≈ 66.3%, but the article states this as a fact without verifying the source or calculation. While the math appears correct, the lack of explicit confirmation from the cited source (MPEDA) makes this unverified. [confidence: medium]

INTERPRETATION ERRORS:
- "The constraint isn't feedstock availability — it's structure. Tallow supply is almost entirely a derivative of the meat-processing and rendering industry, which means it inherits that industry's volatility. When COVID-era lockdowns cut meat exports and shut abattoirs, India's nascent tallow-biodiesel supply chain lost its raw material at the same time, a linkage flagged directly in contemporary trade reporting." — While the claim about volatility is correct, the conclusion that the constraint is solely "structure" (i.e., logistics and collection) is an oversimplification. The article does not address other critical factors such as economic viability (e.g., cost competitiveness of tallow vs. UCO), policy incentives (e.g., pricing, subsidies), or technological readiness (e.g., processing efficiency). The reasoning gap is that the article attributes the lack of scaling primarily to structural issues without adequately ruling out or addressing these other potential constraints. [confidence: high]

- "The pattern across all three: India already has the raw production base — buffalo herds, rendering byproducts, brackish-water shrimp ponds. What separates the businesses that have scaled (buffalo meat, and now shrimp) from the one that hasn't (tallow biodiesel) is regulatory and logistics infrastructure..." — This claim conflates correlation with causation. While regulatory and logistics infrastructure are important, the article does not provide evidence that these are the *primary* or *only* factors separating scaled vs. unscaled businesses. Other factors such as market demand, profitability, policy support, and technological maturity are not addressed. The reasoning gap is that the article assumes infrastructure is the sole or main differentiator without ruling out or analyzing other contributing factors. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
