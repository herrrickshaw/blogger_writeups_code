# Fact/interpretation check — fy2025-26-sample-report-india-trade

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fy2025-26-sample-report-india-trade.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "USD/INR spot rate | 96.3665 | 2026-07-17" — This exchange rate is factually incorrect and unsupported by real-world foreign exchange market data, where USD/INR trades in the ₹83–₹87 range. [confidence: high]
- "PLI Specialty Steel 1.0/1.1 | 44,106" and "PLI White Goods (committed) | 11,198" under "PLI scheme funding" — These figures misstate the actual government scheme funding/budgetary outlay. The central government outlay for the Specialty Steel PLI scheme is ₹6,322 crore (₹44,106 crore is the committed private investment), and the approved outlay for the White Goods PLI scheme is ₹6,238 crore (₹11,198 crore represents cumulative committed capex/investment). [confidence: high]

INTERPRETATION ERRORS:
- "PLI scheme funding, converted to US$ Million" (including rows for "PLI White Goods (production target) | 190,050", "PLI White Goods (committed) | 11,198", and "PLI total cumulative outlay, 14 sectors | 197,000") — Apples-to-oranges conflation. The table groups three entirely distinct economic metrics under the single heading of "PLI scheme funding": projected private sector sales/production turnover (₹190,050 crore), private investment/capex commitments (₹11,198 crore), and actual government budgetary fiscal outlays (₹197,000 crore). Presenting these metrics side-by-side as "funding" misrepresents projected gross industry output and private capital expenditure as public program expenditure. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "GDP growth (real, FAE) +7% First Advance Estimate" — The article later states that this figure has been superseded by MoSPI's Provisional Estimate, but it does not provide the updated figure, making the claim outdated [confidence: medium]
- None found for other factual errors

INTERPRETATION ERRORS:
- "Merchandise deficit 334,267.7 PIB's figure: -333,190.0 (0.3% narrower)" — The article implies that the 0.3% difference between the two figures is significant, but it does not provide context on whether this difference is statistically significant or material, and it does not consider other factors that might affect the deficit [confidence: medium]
- None found for other interpretation errors

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "GDP growth (real, FAE) +7% First Advance Estimate — MoSPI's Provisional Estimate, released before this snapshot was compiled, has since superseded this figure" — The claim that MoSPI's Provisional Estimate has superseded the First Advance Estimate is incorrect. The First Advance Estimate (FAE) is the earliest official GDP growth estimate released by MoSPI, followed by the Provisional Estimate (PE) later. The PE does not supersede the FAE; both are part of the same sequence of GDP estimates. [confidence: high]

INTERPRETATION ERRORS:
- "NITI Aayog's blended goods+services trade reached $1.84 trillion in FY2025-26 (exports +4.2%, imports +6.5% y-o-y) — this repo's goods-only figures show export growth of just +0.92% over the same year, explained by services exports growing faster (+9.0% per NITI Aayog) and pulling the blended rate up, not a discrepancy." — The reasoning gap here is that the article assumes the difference in growth rates between goods-only exports (+0.92%) and blended goods+services exports (+4.2%) is solely due to faster services export growth (+9.0%). However, this ignores other potential factors such as changes in the composition of trade, methodological differences in data collection, or revisions in services trade data that could also explain the discrepancy. The causal claim is not sufficiently justified by the data provided. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
