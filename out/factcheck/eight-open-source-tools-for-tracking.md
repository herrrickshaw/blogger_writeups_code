# Fact/interpretation check — eight-open-source-tools-for-tracking

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/eight-open-source-tools-for-tracking.html`

Text-SHA1: `c9479dfb33aa568e`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "the 18th Lok Sabha convened in June 2024" — The 18th Lok Sabha actually convened in July 2024 (specifically, the first session of the 18th Lok Sabha began on June 24, 2024, but it formally convened/swore in members over late June/early July, and the election results were declared in June; however, stating it convened in June is factually loose regarding official parliamentary session dates, though June 2024 is technically when members took oath). [confidence: medium]

INTERPRETATION ERRORS:
- "A party that asks more Parliament questions has more members; a high grant rate in a small state may rest on a handful of proposals. Counts are not judgements." — While acknowledging that counts are not judgments, the article pairs seat share directly with question volume without adjusting for party-allotted time or opposition status, which heavily dictates parliamentary question allocation regardless of sheer member count. [confidence: low]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 2491, Requested 6118. Please try again in 4.5675s. Need more tokens? Upgrade to Dev Tier today at https://con]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The data.gov.in company master is labelled ‘data up to 3 November 2023’"* — The article does not provide evidence that this label is accurate or up-to-date as of the article’s publication date (November 2026). The data.gov.in company master is known to be updated periodically, and without a citation to the latest official release, this claim risks being outdated. [confidence: medium]

**INTERPRETATION ERRORS:**
- *"A high grant rate in a small state may rest on a handful of proposals"* — While this is a valid caveat, the article does not explain how the grant rate is calculated (e.g., whether it is a simple ratio of granted proposals to total proposals or a more nuanced metric accounting for sub-sector or project size). This could lead readers to misinterpret the significance of the grant rate without understanding the denominator or potential biases in the data. [confidence: high]

**OUTDATED DATA:**
- *"The data.gov.in company master is labelled ‘data up to 3 November 2023’"* — The article should reference the latest official release of the company master from data.gov.in, as the data is likely to have been updated since November 2023. [confidence: high]
  *(Series to re-check: [data.gov.in company master](https://data.gov.in/); likely newer period: post-2023, possibly 2024 or later.)*

- *"The committed snapshot was built on 22 July 2026 and holds 113,970 proposals in 22 sub-sectors"* — The article does not indicate whether a newer snapshot of the PARIVESH 2.0 Environmental Clearance register exists. [confidence: high]
  *(Series to re-check: [PARIVESH 2.0 Environmental Clearance register](https://parivesh.nic.in/); likely newer period: post-July 2026.)*

- *"The pairing file was retrieved on 20 July 2026 and has 12 verified and 7 prospective pairs"* — The article does not confirm whether this file has been updated since July 2026, especially given the note that "policy status changes quickly." [confidence: high]
  *(Series to re-check: [PIB releases and Cabinet approvals](https://pib.gov.in/); likely newer period: post-July 2026.)*
