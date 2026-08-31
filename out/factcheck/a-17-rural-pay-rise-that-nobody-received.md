# Fact/interpretation check — a-17-rural-pay-rise-that-nobody-received

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/a-17-rural-pay-rise-that-nobody-received.html`

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

## Groq llama-3.3-70b-versatile

[Groq/llama-3.3-70b-versatile API error 404: {"error":{"message":"The model `llama-3.3-70b-versatile` does not exist or you do not have access to it.","type":"invalid_request_error","code":"model_not_found"}}
]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "The month rural India got a 12.7 per cent raise" — The article claims a 12.7% raise between June and July 2025, but the data shows a rise from ₹454 to ₹511, which is a 12.51% increase (511/454 ≈ 1.1251). The 12.7% figure is incorrect. [confidence: high]

- "VB-G RAM G came into force on 1 July 2026" — The article states this date, but the VB-G RAM G Act received presidential assent on 21 December 2025 and came into force on 1 July 2026. While the date itself is correct, the phrasing implies it came into force immediately after assent, which is misleading. The article does not clarify the interim period. [confidence: high]

INTERPRETATION ERRORS:
- "The newly added regions have smaller agricultural workforces, more concentrated skills, and average wages roughly 50 to 55 per cent above the states in the original sample. Those states held 1.15 per cent of India’s rural population and 1.22 per cent of its workforce at the 2011 Census. They now supply about 11 per cent of sample villages — close to ten times their demographic weight." — The article correctly identifies the compositional shift but then implies that this alone explains the entire wage growth discrepancy. However, it does not account for potential regional wage variations within the original sample or other confounding factors (e.g., seasonal employment patterns, local economic conditions) that could also influence the observed wage differences. The claim oversimplifies the causal mechanism by attributing the entire wage growth to the sample change without ruling out alternative explanations. [confidence: medium]

- "A sample that overstates the wage level, and a methodology that by construction understates the price level, will make real rural wages look healthier than they are twice over — and because the indexation formula runs off the price side, it will also produce smaller statutory wage revisions than the actual cost of living warrants." — The article conflates two separate issues (wage level overstatement and price level understatement) to argue that real rural wages are artificially inflated. However, the impact of these two factors on real wages (nominal wages adjusted for inflation) is not necessarily additive or mutually reinforcing in the way described. The wage indexation formula's effect on real wages depends on the relative magnitudes and timing of the adjustments, which are not clearly disentangled here. The claim extrapolates beyond what the data shows by assuming a compounded effect without empirical validation. [confidence: medium]
