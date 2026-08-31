# Fact/interpretation check — how-india-actually-plans-to-hit-net

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-india-actually-plans-to-hit-net.html`

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
- "India's Long-Term Low-Carbon Development Strategy (LT-LEDS), submitted to the UNFCCC by MoEFCC in 2022" — The LT-LEDS was actually submitted in **2021**, not 2022. [confidence: high]

- "the 2015 NDC's 33-35% emissions-intensity-reduction target and 40% non-fossil-capacity target were both achieved years early (in February 2026, non-fossil capacity had already reached 52.57%)" — While the non-fossil capacity target was achieved early, the **emissions-intensity-reduction target (33-35%) was met by 2020**, not "years early" in 2026. The phrasing suggests the target was achieved closer to the scenario's publication date, which is misleading. [confidence: high]

INTERPRETATION ERRORS:
- "The single most quoted finding from the entire exercise is also the least comfortable one for a simple decarbonisation narrative: India's coal consumption will continue to rise until 2047, in absolute terms, even inside the scenario that reaches Net Zero by 2070." — While the claim about rising coal consumption is factually supported, the article **implies a contradiction between rising coal use and Net Zero goals**, which is not necessarily valid. Rising absolute coal consumption can occur alongside declining emissions intensity and a shrinking share of coal in the energy mix, as the article itself notes (coal's share falls to 15–20% by 2070). The framing suggests a false dichotomy between coal use and Net Zero, when in reality, the scenarios reconcile the two through efficiency and decarbonization measures. [confidence: high]

- "CCUS is treated as the specific technology answer for the roughly one-quarter of industrial energy demand the Industry scenario (Vol. 4) does not expect to electrify even by 2070" — The article **overstates the role of CCUS** by implying it is the *only* solution for the remaining fossil-based industrial energy demand. The LT-LEDS (2021) explicitly states that CCUS is not yet mature and is only suitable for demonstration projects, suggesting that other technologies (e.g., green hydrogen, biomass, or process changes) may also play a role. The article does not acknowledge this uncertainty or alternative pathways. [confidence: high]
