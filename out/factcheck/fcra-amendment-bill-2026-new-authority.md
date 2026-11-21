# Fact/interpretation check — fcra-amendment-bill-2026-new-authority

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fcra-amendment-bill-2026-new-authority.html`

Text-SHA1: `ddfe72cc8ffc48e8`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "A committee that has met stakeholders on 12 November and the ministries on 19 November is at the stage of taking evidence" — This states that the committee has already met with the ministries on 19 November. However, the article was analysed on 18 November 2026, and earlier sections explicitly state that "19 November is the date of the next Joint Committee sitting" and "it sits again on 19 November". Describing the 19 November meeting in the past tense as having already occurred contradicts the article's own timeline. [confidence: high]
- "The Bill has been with a joint committee for 99 days; it sits again on 19 November" — The Bill was referred to the Joint Parliamentary Committee on 12 August 2026. As of the date of analysis (18 November 2026), exactly 98 days had elapsed (19 days in August + 30 in September + 31 in October + 18 in November). The day count only reaches 99 on 19 November. [confidence: medium]

INTERPRETATION ERRORS:
- "Each of the four points concerns what happens to an organisation after a decision by the government, and in each the Bill supplies a consequence without supplying a remedy." — The reasoning gap is that not all four flagged points arise from an executive decision by the government. "No clean exit" and "Loss of assets on cessation" describe situations where an organisation voluntarily chooses not to apply for renewal or surrenders its certificate. Furthermore, "Different routes" concerns a statutory classification between certificate holders and prior-permission applicants, which is a legislative distinction rather than a post-decision consequence imposed on an organisation without a remedy. [confidence: high]
- "The Joint Committee should ask the Home Ministry to table the renewal-refusal numbers and the stated reasons for them, since the Bill’s effect depends on how often renewal is denied." — This extrapolates the Bill's impact to depend solely on renewal denials. As the article itself notes in the table, the asset vesting provisions also apply when a certificate is cancelled, surrendered, or when an organisation simply does not apply for renewal. Therefore, the Bill's overall effect also depends on voluntary exits and cancellations, not just on how often renewal is refused. [confidence: medium]

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**
- *“The FCRA Amendment Bill 2026 would … cut the maximum jail term from 5 years to 1.”* — The 2026 amendment, as drafted by PRS and the Ministry of Home Affairs, **does not reduce the statutory imprisonment term**; it retains the existing maximum of five years and only amends the monetary penalty and asset‑vesting provisions. No official text shows a reduction to one year. [confidence: high]

**INTERPRETATION ERRORS:**
- *“The lower jail term and the new asset provisions cut in different directions, since an organisation that stops renewing loses assets that foreign funds paid for, even if it breaks no rule.”* — This statement treats the reduction in imprisonment as a compensatory “cut in a different direction” to the asset‑vesting rule, implying a causal or balancing relationship between the two. In reality, the two provisions address **separate policy objectives** (criminal sanction vs. post‑exit asset management) and are not logically offsetting each other. The inference therefore misrepresents how the bill’s provisions interact. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The FCRA Amendment Bill 2026 would vest assets of organisations that lose their certificate in a Designated Authority and cut the maximum jail term from 5 years to 1."*
  — The Bill’s timeline is incorrect: it was introduced in the Lok Sabha on **25 March 2026** and referred to a Joint Committee on **12 August 2026**, not 2026 as a year (likely a typo for 2026 as the year). [confidence: high]

**INTERPRETATION ERRORS:**
- *"The lower jail term and the new asset provisions cut in different directions, since an organisation that stops renewing loses assets that foreign funds paid for, even if it breaks no rule."*
  — The claim conflates *asset vesting* (triggered by cancellation/surrender/non-renewal) with *violations* (which attract the reduced jail term). The two provisions are distinct: asset seizure is a procedural consequence of FCRA exit, not a penalty for rule-breaking. [confidence: high]

**OUTDATED DATA:**
- *"The Bill has been with a joint committee for 99 days; it sits again on 19 November [2026]."*
  — The article was analyzed on **18 November 2026**, meaning the 99-day count is now outdated (as of the cutoff date). The next sitting date (19 Nov) is also irrelevant. [confidence: high]
