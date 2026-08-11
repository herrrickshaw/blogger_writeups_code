# Fact/interpretation check — the-rule-of-72-rule-of-114-and-how-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-rule-of-72-rule-of-114-and-how-to.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "so the exact tripling-time constant is 109.9 . That's conventionally rounded to 114" — Standard arithmetic rounding of 109.9 (100 × ln(3)) yields 110, not 114. The constant 114 is selected to account for compound-interest higher-order terms at typical savings rates (around 8–10%), not as a rounding of 109.9. [confidence: high]
- "So the Rule of 144 constant, 2 × 69.3 = 138.6 , rounds to 144" — Standard arithmetic rounding of 138.6 yields 139, not 144. The constant 144 is obtained by doubling the Rule of 72 constant (2 × 72), not by rounding 138.6. [confidence: high]

INTERPRETATION ERRORS:
- "making “144 ÷ r” the same as taking the Rule-of-72 doubling time and doubling it, which is both intuitive and exactly right (since doubling twice literally is quadrupling)." — While exact quadrupling time is mathematically twice the exact doubling time ($\frac{\ln(4)}{\ln(1+r)} = 2 \times \frac{\ln(2)}{\ln(1+r)}$), doubling an approximation ($\frac{72}{r}$) produces another rule-of-thumb approximation ($\frac{144}{r}$), not an "exactly right" result. Describing $\frac{144}{r}$ as "exactly right" conflates an exact logarithmic equality with an imprecise shortcut formula. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "PPF rate of 7.1% per the Ministry of Finance's small-savings notification for Q2 FY2026-27 (July–September 2026), unchanged since April 2020" — The article relies on contemporaneous reporting for the rate figure and effective dates, but does not independently verify the information, which may lead to potential inaccuracies [confidence: medium]
- "the current level of Indian CPI inflation used in the real-rate illustration (~5%) is a round illustrative figure for the arithmetic, not a claimed current official inflation reading" — The article does not provide a source for the 5% inflation figure, which may not reflect the actual current inflation rate [confidence: medium]

INTERPRETATION ERRORS:
- "At 20%+ — the range equity investors and get-rich-quick pitches like to quote — the rule is off by two to three months, which matters less for a rough gut-check but is worth knowing before you rely on it for a real projection" — The article implies that a 2-3 month error is insignificant, but this may not be the case for all investors or investment decisions, and the article does not provide context for what constitutes a significant error [confidence: medium]
- "They do not directly apply to a Systematic Investment Plan (SIP), where money goes in periodically rather than all at once — that needs the future-value-of-annuity formula, not the doubling-time formula, and will always take longer to double than a lump sum earning the same headline rate" — The article concludes that SIPs will always take longer to double than a lump sum, but this may not be true in all cases, depending on the specific SIP schedule and interest rate [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 9 August 2026" — The date is in the future relative to the current date (2023), making it unverifiable and likely incorrect. [confidence: high]

- "PPF rate of 7.1% per the Ministry of Finance's small-savings notification for Q2 FY2026-27 (July–September 2026), unchanged since April 2020" — The PPF rate has not remained unchanged since April 2020; it has been revised multiple times (e.g., 7.1% in Q2 FY2023-24, 8.0% in Q1 FY2020-21). [confidence: high]

INTERPRETATION ERRORS:
- "The Rule of 72, 114 and 144 are all built for a single, one-time lump-sum investment left untouched to compound — you put in money once, at the start, and don't add to it. They do not apply, as-is, to a Systematic Investment Plan (SIP) or any other recurring/staggered investment" — While the article correctly states that the Rule of 72 does not apply to SIPs, it does not provide a clear explanation of why the Rule of 72 *overestimates* the time to double for SIPs (due to the time value of money and the fact that later contributions have less time to compound). The claim is factually correct but lacks the necessary nuance to explain the *direction* of the error. [confidence: medium]

- "a 7.1% PPF return against ~5% inflation is really compounding your purchasing power at roughly 2.1%, which by the Rule of 72 takes about 34 years to double — not 10" — The article correctly calculates the real rate (7.1% - 5% = 2.1%) and applies the Rule of 72 to it, but it does not clarify that the Rule of 72 is an approximation and that the actual time to double at 2.1% is closer to 33.8 years (ln(2)/ln(1.021) ≈ 33.8). The claim is directionally correct but oversimplifies the exact calculation. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
