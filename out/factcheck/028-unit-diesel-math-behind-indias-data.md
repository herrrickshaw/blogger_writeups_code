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
- *“Indus Towers … has already converted its 50,000th cell site to run diesel‑free (back in March 2016).”* — Public disclosures and annual reports show that Indus Towers announced its first diesel‑free sites only in the late‑2010s, and the 50,000‑site milestone was reached **after** 2020, not in 2016. The date and milestone are therefore incorrect. [confidence: high]  

- *“PNGRB had authorised 307 geographical areas by 2026, reaching close to 100 per cent of India’s landmass outside the islands and around 784 districts.”* — The PNGRB’s official releases list **≈ 300** authorized areas, but the claim that this covers “close to 100 per cent of the landmass outside the islands” is overstated; many districts (especially in the Northeast and tribal regions) remain without city‑gas pipelines. The statement exaggerates the coverage. [confidence: medium]  

**INTERPRETATION ERRORS**  
- *“Diesel generation runs about $0.28 per kWh, against an Indian grid average of $0.085 /kWh and round‑the‑clock renewable PPAs $0.076–0.112 /kWh… therefore diesel backup is already losing the cost argument to solar‑charged battery storage.”* — The comparison treats diesel’s **full‑load levelised cost** as if it were the marginal cost of the occasional backup power that diesel generators actually provide. Grid or renewable PPAs reflect continuous supply, whereas diesel is only run during outages (often a few hours per year). Using full‑load LCOE for diesel against continuous‑supply rates is an apples‑to‑oranges comparison that overstates the cost disadvantage of diesel backup. [confidence: high]  

- *“Telecom tower diesel‑phase‑out is driven by cheaper operating costs once grid reliability clears a threshold, so data‑centre operators will follow the same economic logic.”* — Telecom towers have **low, intermittent loads** and can often rely on limited‑capacity solar‑plus‑battery packs, whereas data centres require **high, near‑continuous uptime** and larger backup capacities. Assuming the same cost‑driven dynamics ignores the different load profiles and reliability requirements, making the causal inference unsupported. [confidence: medium]

## Mistral mistral-small-latest

[Mistral API error 429: {"object":"error","message":"Rate limit exceeded","type":"rate_limited","param":null,"code":"1300","raw_status_code":429}]
