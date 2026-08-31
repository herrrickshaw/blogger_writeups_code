# Fact/interpretation check — foreign-capital-found-indias-hospitals

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/foreign-capital-found-indias-hospitals.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "DPIIT reports on a calendar-year basis; unrelated financial-year figures circulating in trade press (e.g. a widely cited “89% growth in FY2023-24”) cannot be reconciled against this table and are flagged here as a methodology mismatch, not a contradiction of it." — DPIIT (Department for Promotion of Industry and Internal Trade) publishes its official FDI data and quarterly fact sheets on an Indian Financial Year basis (April to March), not on a calendar-year basis. [confidence: high]
- "Delhi / NCR | AIIMS, New Delhi | Max Healthcare, Fortis Escorts, Apollo Indraprastha | No (largely listed/promoter)" — Fortis Healthcare is not promoter-controlled; it has been controlled since 2018 by Malaysia-based foreign healthcare group IHH Healthcare Berhad, which acquired a controlling stake after the original promoters lost control. [confidence: high]
- "West Bengal | SSKM Hospital / IPGMER, Kolkata | AMRI Hospitals, Apollo Gleneagles | No" — AMRI Hospitals was acquired in September 2023 by Manipal Hospitals, which is majority-owned by foreign sovereign and private equity funds (Temasek and Mubadala). [confidence: high]

INTERPRETATION ERRORS:
- "World Bank’s own WHO-sourced series (SH.MED.BEDS.ZS) puts India at 1.59 as of 2021, down from 2.13 in 2000... Foreign hospital investment since 2000 has not moved this ratio." — The metric measures beds per 1,000 population. Between 2000 and 2021, India's population grew by more than 350 million people. A declining or flat per-capita ratio does not imply that total hospital beds failed to increase or that investment produced no capacity; bed growth can be substantial in absolute terms while still lagging high population growth. [confidence: high]
- "Every deal above is a change of ownership of beds that already existed. None of them, on the reporting available, is a foreign-financed hospital built where one was not standing before. None of the deals in the table above materially changes either bed-ratio figure, because none of them adds beds" — The article conflates secondary buyouts/platform acquisitions with long-term capital deployment. PE and sovereign funds acquiring hospital networks routinely inject growth capital into those platforms to finance brownfield bed additions and new hospital builds post-acquisition; asserting that buyouts contribute zero new capacity assumes static capacity based solely on the initial ownership transfer. [confidence: medium]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Hospitals have permitted 100 per cent FDI on the automatic route since January 2000" — The correct phrasing should be "Hospitals have been permitted 100 per cent FDI on the automatic route since January 2000." The word "permitted" is missing, which changes the meaning from passive permission to active permission. [confidence: high]

- "India's hospital beds fall well short of world norms" — The article later clarifies that there is no formal WHO minimum standard for hospital beds per 1,000 population, and the "world norms" are based on the global average (3.29 in 2021). The claim implies a formal standard exists, which is incorrect. [confidence: high]

INTERPRETATION ERRORS:
- "Foreign hospital investment since 2000 has not moved this ratio [hospital beds per 1,000 population]." — While the claim itself is factually correct (no new beds were added by foreign investment), the interpretation that this implies foreign investment has failed to address the bed shortage is an overgeneralization. The article does not provide evidence that foreign investment was intended to directly address the bed shortage, nor does it rule out indirect contributions (e.g., efficiency gains enabling existing beds to serve more patients). The causal link between foreign investment and bed shortage is not established. [confidence: medium]

- "If the thesis were 'India needs more beds,' the rational foreign-capital response would be to build them." — The article assumes that the primary goal of foreign capital in hospitals is to address bed shortages, but it does not provide evidence that this was the intended or expected outcome of the investments. Private equity and sovereign funds may prioritize returns over public health goals, making this assumption an apples-to-oranges comparison between profit-driven investment and public health needs. [confidence: high]
