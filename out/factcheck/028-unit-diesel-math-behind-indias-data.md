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

**FACTUAL ERRORS:**  
- **“India's 606,300 telecom towers — 83 per cent of them owned by neutral, non‑discriminatory tower companies … the second‑highest tower‑co‑penetration rate in the world after China's 100 per cent.”** – The 83 % figure is not supported by publicly available TRAI/industry data, which places tower‑co ownership closer to 70 % (≈ 420 k of ~ 600 k towers) as of 2023‑24. The claim of a world‑ranking second only to China is therefore inaccurate. [confidence: high]

**INTERPRETATION ERRORS:**  
- **“Diesel backup is already losing the cost argument to solar‑charged battery storage … the Auroville Consulting study shows diesel LCOE ₹49.58–57.63/kWh vs. solar‑charged BESS ₹39.71–61.72/kWh, making solar‑charged BESS the cheaper backup option across most hours‑of‑autonomy scenarios tested.”** – The study is a Tamil Nadu‑specific commercial/industrial backup analysis, not a data‑centre‑level assessment. Data‑centres have far larger, near‑continuous loads and stricter uptime requirements than the industrial customers modeled. Extrapolating the Tamil Nadu cost ratios to all Indian data‑centres therefore overstates the economic advantage of BESS and creates a false causal link between the study’s results and nationwide data‑centre backup economics. [confidence: high]

## Mistral mistral-small-latest

[Mistral API error 429: {"object":"error","message":"Rate limit exceeded","type":"rate_limited","param":null,"code":"1300","raw_status_code":429}]
