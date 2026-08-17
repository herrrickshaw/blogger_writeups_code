# Fact/interpretation check — india-forest-wildlife-crz-clearances

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-forest-wildlife-crz-clearances.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "Grant rate of decided: 10.7%" (under Wildlife Clearance) and "Grant rate of decided: 31.3%" (under CRZ Clearance) — These calculations are factually incorrect based on the definition of "decided" cases (`granted ÷ (granted + dead)`). For Wildlife Clearance, 517 granted out of 600 decided (517 granted + 83 dead) is **86.2%**, not 10.7%. For CRZ Clearance, 468 granted out of 550 decided (468 granted + 82 dead) is **85.1%**, not 31.3%. The figures 10.7% and 31.3% were calculated using `granted ÷ (granted + in process)`, contradicting the stated metric. [confidence: high]
- "Grant rate of decided (granted ÷ granted+dead): 69.7%" vs. "Grant rate = granted ÷ (granted + in-process); 'dead' (rejected/withdrawn/returned) and 'delisted' (PARIVESH auto-cleanup) are excluded from the denominator" (in methodology note) — The article provides two mutually contradictory mathematical formulas for "Grant rate." The Forest Clearance section defines it as excluding in-process applications, whereas the methodology note explicitly defines the denominator as `granted + in-process` while excluding dead cases. [confidence: high]

INTERPRETATION ERRORS:
- "For scale: the entire national industrial land bank shows ~253,720 developed-and-vacant acres... Forest diversion adds ~122,666 more acres of granted land-use change" — Apples-to-oranges comparison. The industrial land bank figure represents a static stock of currently available, vacant industrial land, whereas the forest diversion figure represents a cumulative historical flow of land diverted across projects (linear infrastructure, hydro, mining) that is already occupied or utilized, not available land supply. [confidence: high]
- "Wildlife (10.7% granted) is the real bottleneck: 4,319 of 4,919 sit in process, most 'Pending at Proponent' (the ball is with the project applicant, not the regulator) — projects near protected areas stall here for the National/State Board for Wildlife recommendation." — False causal attribution. The author characterizes the clearance process and the Wildlife Board as the bottleneck, while simultaneously noting that the vast majority of files are stalled with the project applicants ("Pending at Proponent"), meaning the delay at this stage is driven by proponent inaction rather than regulatory review. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Grant rate = granted ÷ (granted + in-process)" — This claim is incorrect because the article later states that the grant rate is calculated as "granted ÷ (granted + dead)", excluding 'in-process' and including 'dead' (rejected/withdrawn/returned) applications, but then also mentions that 'dead' and 'delisted' are excluded from the denominator, which is consistent with the initial statement but contradicts the inclusion of 'dead' [confidence: medium]
- None found for other factual errors

INTERPRETATION ERRORS:
- "Forest Clearance is a second land-creation channel" — This claim may be misleading because it implies that Forest Clearance directly creates new land, whereas it actually involves the diversion of existing forest land for other uses, which is a different concept [confidence: high]
- "Forest diversion adds ~122,666 more acres of granted land-use change — a different channel (mining, linear infra, hydro), on a different clock" — This comparison may be problematic because it juxtaposes the area of forest land diverted with the national industrial land bank without considering that these are different types of land use and may not be directly comparable in terms of economic or environmental impact [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "generated 2026-07-22" — The date is in the future (2026) relative to the current year (2023), making it unverifiable and likely incorrect. [confidence: high]

- "the entire national industrial land bank shows ~253,720 developed-and-vacant acres (Industrial Information & Land Bank, retrieved 2026)" — The cited source (Industrial Information & Land Bank) is a real Indian government database, but the retrieval date of 2026 is impossible, and the figure itself is unverifiable as stated. [confidence: high]

INTERPRETATION ERRORS:
- "Forest Clearance is a second land-creation channel" — The claim implies that Forest Clearance *creates* land (e.g., by converting non-forest to forest), but the context suggests it measures land *diversion* (conversion of forest land to non-forest uses like mining or infrastructure). The wording conflates "land creation" with "land-use change," which is a misinterpretation of the process. [confidence: high]

- "Grant rate = granted ÷ (granted + in-process); 'dead' (rejected/withdrawn/returned) and 'delisted' (PARIVESH auto-cleanup) are excluded from the denominator, as in the EC analysis." — The article claims the grant rate calculation method is consistent with Environmental Clearance (EC) analysis, but it does not provide evidence or citation that EC uses the same exclusion criteria (e.g., whether EC also excludes "dead" and "delisted" cases from the denominator). This is an unsupported methodological equivalence. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
