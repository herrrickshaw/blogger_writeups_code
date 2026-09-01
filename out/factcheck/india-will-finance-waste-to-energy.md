# Fact/interpretation check — india-will-finance-waste-to-energy

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/india-will-finance-waste-to-energy.html`

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
- "India already has small commercial units running (10 tonnes-per-day plants are a common reference scale)" — The claim implies that 10 tonnes-per-day (TPD) pyrolysis plants are a *common* scale in India, but the article later cites a single example (Nepra) and does not provide broader evidence of widespread 10 TPD commercial operations. The claim lacks sufficient sourcing to verify its generality. [confidence: medium]

- "Delhi burns waste that falls short of its own legal calorific-value threshold" — The article cites the SWM Rules 2016 threshold (1,500 kcal/kg) and notes Delhi's unsegregated waste averages 800–2,150 kcal/kg, but it does not provide *specific* evidence that Delhi's waste *actually* falls below the threshold in practice. The claim assumes the general range applies to Delhi without direct verification. [confidence: medium]

INTERPRETATION ERRORS:
- "China's incineration fleet and its sorting mandates are reinforcing each other, aimed at the same calorific-value problem India's own SWM Rules identify. Delhi's incineration fleet, without a comparably enforced sorting mandate feeding it, is absorbing that problem instead of solving it — burning waste at a calorific value the law already says shouldn't qualify." — The claim suggests that China's sorting mandates *directly* enabled its incineration fleet's success, but the article does not establish a causal link between the two. While sorting improves calorific value, the article does not prove that this was the *primary* reason for China's incineration fleet's scale or efficiency. The comparison is correlational, not causal. [confidence: high]

- "robotics and computer vision are real technologies that could eventually substitute for some of that missing sorting capacity, but they are, at best, a more expensive way to buy back what a properly financed segregation shed would have delivered more cheaply at the source" — The claim assumes that AI/robotics sorting is inherently *more expensive* than source segregation without providing comparative cost data. The article acknowledges that AI sorting is still lab-stage and does not cite any operational cost benchmarks for AI sorting at municipal scale, making the cost comparison speculative. [confidence: high]
