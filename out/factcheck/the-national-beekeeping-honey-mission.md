# Fact/interpretation check — the-national-beekeeping-honey-mission

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-national-beekeeping-honey-mission.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "India became the world's second-largest honey exporter in 2024" — The article cites APEDA and CRISIL's July 2025 dashboard for the claim that India moved from 9th to 2nd place, but the export data provided is for FY2023-24 (ending March 2024), not calendar 2024. The export rank is likely based on FY2023-24 data, not 2024. [confidence: high]

- "The same four years contain a fact the scheme's own success story rarely mentions: a 2020 government-linked investigation found ten of thirteen major honey brands sold in Indian shops failed the internationally accepted purity test" — The investigation was conducted by the Centre for Science and Environment (CSE), a not-for-profit, not a "government-linked" body. [confidence: high]

INTERPRETATION ERRORS:
- "The regulatory response is real and traceable: FSSAI's food product standards for honey (Chapter 2, section 2.8.3) now include, as parameter 13, an explicit test for '2-Acetylfuran-3-Glucopyranoside (2-AFGP) as Marker for Rice Syrup,' required to be absent, alongside a wider panel — C4 sugar capped at 7% by mass, a fructose-to-glucose ratio band of 0.95–1.50, hydroxymethylfurfural (HMF) capped at 80 mg/kg, and a minimum pollen count of 5,000 grains per gram." — While the FSSAI standards include these parameters, the article implies that these standards are sufficient to address the adulteration problem detected by CSE in 2020. However, the CSE investigation specifically used NMR spectroscopy, which is more rigorous than the FSSAI parameters (e.g., the 2-AFGP marker is only for rice syrup, and the FSSAI does not mandate NMR testing for domestic honey). The article does not clarify that the FSSAI standards may still allow some forms of adulteration that NMR can detect, nor does it address whether the strengthened standards have been effectively enforced. [confidence: high]

- "NBHM sanctioned 47 Mini Honey Testing Labs specifically to push quality control down to the district level. Whether that network is being used to test domestic retail honey with the same rigour export shipments require — or is mainly serving the export pipeline the scheme's own success metrics track — is not something this piece could confirm from the sourcing available; it's the open question the scheme's own numbers don't answer." — The article presents the lack of confirmation about the use of Mini Honey Testing Labs as an open question, but it does not critically assess whether the NBHM's infrastructure (e.g., the labs, blockchain traceability portal) is designed to address domestic adulteration at all. The NBHM's metrics focus on export growth, and the article does not explain how the scheme's infrastructure (e.g., Mini Labs) would realistically address domestic market adulteration, given that the domestic market lacks mandatory NMR testing and enforcement mechanisms. The interpretation gap is that the article assumes the NBHM's infrastructure *could* address domestic adulteration without evidence that it is intended or equipped to do so. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
