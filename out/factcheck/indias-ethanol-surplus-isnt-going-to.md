# Fact/interpretation check — indias-ethanol-surplus-isnt-going-to

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indias-ethanol-surplus-isnt-going-to.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

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
- "India's administered ethanol price already beats what Brazil or the U.S. would pay on the export market." — The claim is incorrect because the article itself shows that the U.S. FOB Gulf price ($0.449/L) and Brazil's FOB Santos prices ($0.587–0.611/L) are both below India's domestic EBP price (~$0.72/L). However, the claim implies India's price is higher than what these countries *would pay* (i.e., their import prices), which is not supported by the data. The article only compares export benchmarks, not import prices. [confidence: high]

- "The U.S. Grains & Bioproducts Council publishes a weekly ethanol and co-product pricing report sourced from World Perspectives, Inc. Its 7 January 2026 edition puts U.S. ethanol FOB Gulf at $1.698 per gallon — $0.449 per litre" — The conversion is incorrect. $1.698 per gallon is approximately $0.449 per litre *only if* the calculation is done correctly (1 gallon = 3.78541 liters, so $1.698/3.78541 ≈ $0.4486/L). However, the article rounds this to $0.449/L, which is technically correct but misleadingly precise given the source's likely rounding. The real issue is that the article does not clarify whether the USGC report's $1.698/gallon is already in USD per gallon (which it is) or if it is a converted figure, creating potential confusion. [confidence: medium]

INTERPRETATION ERRORS:
- "India's ethanol surplus isn't going to Brazil or the USA — and the price data explains why" — The reasoning gap here is that the price data only explains why exporting *fuel ethanol* to Brazil or the USA is unattractive (since India's domestic price is higher than export benchmarks). However, the article later acknowledges that India *does* export ENA (extra-neutral alcohol) to markets like West Africa, where prices are competitive. The claim conflates "ethanol" (a broad category) with "fuel ethanol," ignoring that other grades of ethanol (like ENA) are already being exported profitably. The price data does not explain why *all* ethanol exports are unattractive, only a specific subset. [confidence: high]

- "The practical case for pharma-grade diversification is that it doesn't require competing head-on with Brazilian sugarcane or U.S. corn economics on a commodity export market where India is structurally not the low-cost producer." — The reasoning gap is that while pharma-grade ethanol may avoid direct competition with Brazilian/US feedstock economics, the claim assumes that India can *automatically* capture this market by repurposing capacity. However, pharma-grade ethanol requires strict compliance (USP/IP standards, benzene-free, etc.), which is not a trivial manufacturing or regulatory hurdle. The article does not address whether Indian distilleries currently have the infrastructure or certifications to meet these standards at scale, nor does it consider the time and cost required to transition capacity. The conclusion overstates the ease of diversification without evidence of feasibility. [confidence: high]
