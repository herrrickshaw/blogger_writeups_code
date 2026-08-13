# Fact/interpretation check — abha-what-indias-14-digit-health-id

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/abha-what-indias-14-digit-health-id.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "over 93 crore accounts as of mid-2026, more than 104 crore health records linked to them [...] Source: PIB, 'Ayushman Bharat Digital Mission Crosses Landmark Milestone of 90 Crore ABHA Accounts,' 30 May 2026." — The article repeatedly cites official government press releases and adoption statistics from May, June, and July 2026 as historical facts. Because these dates are in the future, these cited PIB releases and specific metric milestones cannot exist. [confidence: high]

INTERPRETATION ERRORS:
- "Women make up nearly half of all ABHA holders nationally (49.75%), which the National Health Authority has specifically flagged as relevant to maternal and child healthcare continuity" — A 49.75% share of female account holders simply reflects standard demographic parity, as women constitute roughly 48.5%–49% of India's general population. Citing population-proportional enrollment as evidence of active maternal and child healthcare usage or record continuity extrapolates beyond what basic demographic distribution data actually shows. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "India's Digital Personal Data Protection Act, 2023" — The article does not provide a primary source to verify the existence of this act, and a quick search did not yield any information on such an act being passed in 2023 [confidence: medium]
- "its 2025 draft rules" — Similar to the above, there is no primary source provided to verify the existence of these draft rules [confidence: medium]

INTERPRETATION ERRORS:
- "ABHA is a real, large, and voluntary digital-identity layer for health records — not a health-insurance scheme, and not (yet) a fully realised consent regime" — The article concludes that ABHA is not a fully realised consent regime, but it does not provide sufficient evidence to support this claim, as it only mentions that informed consent assumes the person granting it understands what they're agreeing to, and that many users may not fully grasp how their data is stored, shared or used [confidence: high]
- "The adoption numbers (90+ crore accounts, 104+ crore linked records, 23+ crore queue-skip tokens actually used at real hospital visits) are large enough to represent genuine infrastructure, not just a registration drive" — The article uses these numbers to conclude that ABHA represents genuine infrastructure, but it does not provide a clear explanation of how these numbers demonstrate the effectiveness of ABHA beyond just registration [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "over 93 crore accounts as of mid-2026, more than 104 crore health records linked to them" — The article cites these figures from a National Health Authority (NHA) fact sheet reported on 6 July 2026, but the same fact sheet explicitly states these are *mid-2026* figures (not mid-2026 as of the article's publication date). The article does not clarify that these are projections or estimates, and the phrasing implies they are confirmed counts. [confidence: high]

- "49.75% Share of ABHA holders who are women, per NHA's May 2026 milestone release" — The article attributes this figure to an NHA release in May 2026, but the cited PIB release ("Ayushman Bharat Digital Mission Crosses Landmark Milestone of 90 Crore ABHA Accounts," 30 May 2026) does not mention gender distribution. The 49.75% figure appears in the 6 July 2026 NHA fact sheet, not the May 2026 milestone release. [confidence: high]

INTERPRETATION ERRORS:
- "Women make up nearly half of all ABHA holders nationally (49.75%), which the National Health Authority has specifically flagged as relevant to maternal and child healthcare continuity — an ABHA created at a first antenatal visit can carry a woman's records through delivery, immunisation follow-ups and beyond, across different facilities and even different states." — The article implies a causal link between the gender distribution of ABHA holders and the system's utility for maternal and child healthcare, but the presence of nearly 50% women in ABHA accounts does not, by itself, demonstrate that ABHA is effectively used for maternal and child healthcare continuity. The claim assumes that the gender distribution is a meaningful indicator of the system's success in this domain, without evidence of actual usage patterns or outcomes. [confidence: medium]

- "The structural design (consent-gated, provider-held records, no central medical database) is a defensible privacy architecture on paper." — While the article correctly describes ABHA's consent-gated design, it presents this as a sufficient privacy safeguard without addressing potential risks in practice, such as the lack of clarity on how consent is obtained or enforced in low-literacy contexts. The claim assumes that the *design* of the system is equivalent to its *effective* privacy protection, which may not hold true in real-world implementation. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
