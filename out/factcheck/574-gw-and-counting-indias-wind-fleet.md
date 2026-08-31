# Fact/interpretation check — 574-gw-and-counting-indias-wind-fleet

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/574-gw-and-counting-indias-wind-fleet.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "India's wind fleet crossed 57,443 MW in June 2026, with Gujarat overtaking Tamil Nadu as the single biggest contributor for the first time." — Gujarat officially overtook Tamil Nadu in cumulative installed wind power capacity much earlier, in May/June 2023 (reaching approximately 10,416 MW against Tamil Nadu's 10,125 MW), not in 2026 for the first time. [confidence: high]

INTERPRETATION ERRORS:
- "Measured against the 120m figure, which is closer to where modern utility-scale turbines actually sit, India's entire 57.4 GW fleet represents barely 8 per cent utilisation of the national onshore resource NIWE itself has mapped." — Apples-to-oranges comparison. NIWE's 695.5 GW potential estimate assumes modern, high-capacity turbines deployed at 120-meter hub heights across 2% of available land. India's cumulative 57.4 GW installed capacity was built over decades and consists predominantly of legacy turbines installed at 50m to 100m hub heights with much lower nameplate ratings. Dividing cumulative historical capacity by a 120m potential model distorts "resource utilisation," as many prime wind sites are already occupied by older, lower-capacity turbines. [confidence: high]
- "Part of why the FY2025-26 growth rate jumped is a 7 December 2023 MNRE circular, the National Repowering & Life Extension Policy for Wind Power Projects..." — Unsubstantiated causal claim. The article attributes the acceleration in annual wind capacity additions to the 2023 repowering policy without presenting any evidence that repowering projects contributed to the new capacity figures. Wind capacity growth in India has been driven almost entirely by greenfield utility-scale tenders (particularly in Gujarat and Karnataka), whereas repowering has historically faced commercial, PPA, and transmission hurdles with minimal commissioned capacity. [confidence: medium]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India's wind fleet crossed 57,443 MW in June 2026" — The article later states the installed capacity as 57,443.39 MW, which is inconsistent with the rounded figure of 57,443 MW in the opening sentence. The exact figure should be used consistently. [confidence: high]

- "GWEC's Global Wind Report 2025 credits India with adding 6.3 GW of new wind capacity in calendar year 2025" — The article later acknowledges that MNRE's figure for FY2025-26 is ~6 GW, which covers a different period (April-March) than the calendar year 2025. The two figures are not directly comparable without adjustment. [confidence: high]

INTERPRETATION ERRORS:
- "India's entire 57.4 GW fleet represents barely 8 per cent utilisation of the national onshore resource NIWE itself has mapped" — The claim implies that the 8% utilization is a measure of progress toward exploiting the resource, but the 8% is derived from dividing the installed capacity (57.4 GW) by the NIWE potential at 120m hub height (695.5 GW). This is not a utilization rate but a ratio of installed capacity to technical potential, which does not account for practical constraints like land availability, transmission capacity, or economic viability. [confidence: high]

- "The resource was never the constraint — the build-out has been" — While the article correctly identifies build-out constraints (transmission, land, repowering pace), it extrapolates from the low ratio of installed capacity to technical potential to conclude that the resource itself is not a constraint. However, the technical potential figures (e.g., 695.5 GW at 120m) are based on a conservative 2% land-availability assumption, which may not reflect actual land-use realities or economic feasibility. The conclusion oversimplifies the relationship between technical potential and actual build-out potential. [confidence: medium]
