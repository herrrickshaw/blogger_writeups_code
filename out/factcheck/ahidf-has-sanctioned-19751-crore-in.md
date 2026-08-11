# Fact/interpretation check — ahidf-has-sanctioned-19751-crore-in

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/ahidf-has-sanctioned-19751-crore-in.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "The 2019 PIB scheme note explains the likely structural reason: AHIDF's 3% interest subvention carries a built-in two-year moratorium..." — The AHIDF scheme was first announced in May/June 2020 under the AtmaNirbhar Bharat package (as correctly noted elsewhere in the article). There was no 2019 PIB scheme note for AHIDF because the fund did not exist in 2019. [confidence: high]

INTERPRETATION ERRORS:
- "The two figures aren't the same measurement (the PIB answer counts ministry-approved projects ; the dashboard counts lender- sanctioned applications , an earlier and more numerous stage in the same pipeline), so they shouldn't be read as a contradiction" — Lender sanctioning is a downstream stage in the approval process (occurring after initial project submission/eligibility verification and before loan disbursement), not an "earlier" stage. The higher figure on the live dashboard (916 sanctioned applications in August 2026 versus 402 projects in August 2025) reflects growth in sanctions over a 12-month period, not a position earlier in the processing funnel. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "The fund was announced inside the ₹20-lakh-crore AtmaNirbhar Bharat package in 2020 with a ₹15,000 crore corpus." — The article later mentions that the outlay was raised to ₹29,610.25 crore and also cited as ₹29,110.25 crore, but it does not verify the initial corpus amount [confidence: medium]
- "The Cabinet extended it in February 2024 — folding in the separate Dairy Infrastructure Development Fund (DIDF) — and raised the outlay to ₹29,610.25 crore through FY2025-26, later cited in a subsequent Rajya Sabha answer as ₹29,110.25 crore for the same window." — The discrepancy between ₹29,610.25 crore and ₹29,110.25 crore is not explained [confidence: medium]

INTERPRETATION ERRORS:
- "The disbursement funnel is steep, and it doesn't fully square with the last PIB update" — The article implies that the disbursement rate is unusually low, but it does not account for the fact that term loans are disbursed in tranches tied to construction and equipment-installation milestones, which could be a normal construction-linked lag [confidence: high]
- "Of the ₹19,750.8 crore sanctioned, only ₹7,770.4 crore — 39% — has been disbursed, against 358 of 916 sanctioned applications." — The article presents this as a problem, but it does not consider that a loan sanctioned this year can take several years to fully disburse, which might be a normal timeline for these types of projects [confidence: medium]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Published 10 August 2026 · v1.0.0" — The article claims to be published on 10 August 2026, but the AHIDF live dashboard was accessed on that date, not the publication date. The article itself is likely published after the dashboard check, making the publication date incorrect. [confidence: high]

- "The fund was announced inside the ₹20-lakh-crore AtmaNirbhar Bharat package in 2020 with a ₹15,000 crore corpus." — The AHIDF was announced as part of the AtmaNirbhar Bharat package in May 2020, but the corpus was ₹15,000 crore, not ₹15,000 crore *inside* the ₹20-lakh-crore package. The phrasing suggests the corpus was a subset of the package, which is misleading. [confidence: high]

INTERPRETATION ERRORS:
- "The government's own stated ambition for the scheme: leverage private investment seven times over, and create employment for 35 lakh people directly and indirectly." — The article presents the government's stated ambition as a fact, but it does not verify whether this leverage ratio or employment figure is achievable or supported by evidence. The claim is presented without critical analysis of its feasibility or past performance of similar schemes. [confidence: high]

- "The two schemes are financing opposite ends of the same supply chain: AHIDF the animals and processing infrastructure, GOBARdhan the plants that turn their dung into gas." — While AHIDF and GOBARdhan are related, the claim that they finance "opposite ends of the same supply chain" is an oversimplification. AHIDF funds dairy and animal-husbandry infrastructure, while GOBARdhan funds biogas plants that use dung as feedstock. However, the supply chain connection is not as direct as implied, as GOBARdhan also includes other feedstocks (e.g., agricultural waste), and the two schemes operate independently with different objectives. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
