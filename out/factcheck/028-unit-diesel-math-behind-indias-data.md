# Fact/interpretation check — 028-unit-diesel-math-behind-indias-data

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/028-unit-diesel-math-behind-indias-data.html`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

[Gemini API error 503: {
  "error": {
    "code": 503,
    "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
    "status": "UNAVAILABLE"
  }
}
]

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- “Indus Towers … converted its 50,000th cell site to run diesel‑free (back in March 2016)” — The 50 k‑site diesel‑free milestone was announced by Indus Towers in 2021, not 2016. The article’s date is therefore incorrect. [confidence: high]  
- “India’s telecom‑tower base needs to grow from roughly 750,000 towers already in place to around 1.2 million to support a full pan‑India 5G rollout” — TRAI’s latest tower‑count data (2023‑24) puts the existing inventory at about 800 k‑plus towers, and industry estimates for a full‑scale 5G rollout range from 1.4 million to 1.6 million sites, not 1.2 million. The figures cited are therefore inaccurate. [confidence: medium]  

**INTERPRETATION ERRORS**  
- “Diesel generators cost roughly three times what grid power costs and roughly three‑and‑a‑half times what solar‑charged battery storage costs, and India is about to build a lot more of both data centres and telecom towers — the two infrastructure categories that lean hardest on diesel for backup power.” — The $0.28/kWh diesel figure is a levelised cost of generation (including capital, fuel, O&M) while the $0.076–0.112/kWh renewable figure is a power‑purchase‑agreement price for grid‑connected supply. Comparing a backup‑only diesel LCOE with a grid‑supply PPA ignores that diesel is used only intermittently, that battery storage incurs separate capital costs, and that capacity factors differ. Hence the claim that diesel “is already losing the cost argument” overstates the evidence. [confidence: high]  
- “A gas genset running on piped natural gas costs roughly ₹6.06 per kVA‑hour … and gas gensets emit no visible smoke or particulates and substantially less NOx and CO₂ per unit generated.” — While natural‑gas generators emit fewer particulates than diesel, they still produce CO₂ and NOx; the statement presents them as essentially “clean” without qualifying the magnitude of emissions or accounting for upstream methane leakage. Using the lower fuel‑cost figure alone also omits the higher capital cost of gas‑fired sets, so the overall economic and environmental advantage is not demonstrated. [confidence: medium]

## Mistral mistral-small-latest

[Mistral API error 429: {"object":"error","message":"Rate limit exceeded","type":"rate_limited","param":null,"code":"1300","raw_status_code":429}]
