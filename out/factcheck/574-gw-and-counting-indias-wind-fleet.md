# Fact/interpretation check — 574-gw-and-counting-indias-wind-fleet

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/574-gw-and-counting-indias-wind-fleet.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "India's wind fleet crossed 57,443 MW in June 2026, with Gujarat overtaking Tamil Nadu as the single biggest contributor for the first time." — Gujarat officially overtook Tamil Nadu to become India's leading state in installed wind power capacity in May/June 2023 (when Gujarat surpassed ~10,400 MW compared to Tamil Nadu's ~10,125 MW), not in 2026. [confidence: high]

INTERPRETATION ERRORS:
- "Measured against the 120m figure, which is closer to where modern utility-scale turbines actually sit, India's entire 57.4 GW fleet represents barely 8 per cent utilisation of the national onshore resource NIWE itself has mapped." — This is an apples-to-oranges comparison. India's cumulative installed fleet (57.4 GW) consists heavily of legacy turbines installed over past decades at much lower hub heights (50m, 80m, and 100m) occupying prime, high-yield wind sites. Directly dividing total historical installed capacity by NIWE's 120m modeled potential wrongly assumes that 92% of the modeled resource/land is unutilised and available for greenfield development, rather than acknowledging that key resource areas are physically occupied by older, lower-capacity turbines requiring repowering. [confidence: high]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 403: {"error":{"message":"Access denied. Please check your network settings."}}]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India's wind fleet crossed 57,443 MW in June 2026" — The article later states the cumulative installed wind capacity reached 57,443.39 MW by the end of June 2026, which is inconsistent with the rounded figure of 57,443 MW used earlier. The exact figure should be used consistently. [confidence: high]

- "GWEC's Global Wind Report 2025 credits India with adding 6.3 GW of new wind capacity in calendar year 2025" — The article later notes that MNRE's data shows ~6 GW added in FY2025-26 (April-March), which is not directly comparable to GWEC's calendar-year 2025 figure. While both figures are close, they describe overlapping but distinct time periods and should not be conflated without clarification. [confidence: high]

INTERPRETATION ERRORS:
- "India's entire 57.4 GW fleet represents barely 8 per cent utilisation of the national onshore resource NIWE itself has mapped" — The claim implies that the 8% utilization is a direct measure of how much of the resource is being used, but the 8% is calculated against NIWE's *installable* potential (under a 2% land-availability assumption), not the total theoretical resource. The actual *technical* potential is likely much higher, making the 8% figure a conservative estimate of utilization. [confidence: high]

- "The resource was never the constraint — the build-out has been" — While the article correctly identifies build-out constraints (transmission, land, repowering pace), it extrapolates from state-level findings to a national conclusion without sufficient evidence that these constraints are uniformly the primary barrier across all states. Some states may face different or additional challenges (e.g., resource quality, policy incentives). [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
