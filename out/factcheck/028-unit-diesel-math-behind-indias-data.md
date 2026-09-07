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
- *“a five‑fold expansion of telecom tower sites for 5G”* — The article says India’s tower base must grow from ~750,000 to ~1.2 million sites, which is roughly a 1.6‑times increase, not a five‑fold (5×) increase. [confidence: high]  
- *“Indus Towers … converted its 50,000th cell site to run diesel‑free (back in March 2016)”* – Indus Towers was incorporated in 2017; it could not have marked a 50 k‑site diesel‑free milestone in 2016. The date and milestone are therefore inaccurate. [confidence: high]  

**INTERPRETATION ERRORS**  
- *“Solar‑charged BESS is the cheaper backup option across most hours‑of‑autonomy scenarios tested”* – The cost figures cited (₹39.71–61.72 /kWh) come from a Tamil Nadu‑specific commercial/industrial study. Extrapolating this to all Indian data‑centres and telecom towers ignores regional grid‑tariff differences, load‑profile variations, and the higher capital intensity of large‑scale data‑centre backup. The conclusion that BESS is universally cheaper is therefore an unsupported generalisation. [confidence: high]  

- *“DRUPS has a 9‑month payback against SUPS on a 1.5 MW system, purely from lower operating cost ($1.84 M vs $5.46 M OpEx)”* – The comparison is between a diesel‑rotary UPS (which still uses diesel fuel) and a static battery UPS, yet the article uses it to argue that diesel‑based backup is becoming uneconomical. The metric (payback period) does not capture the full lifecycle cost or emissions of diesel generators, so the claim mis‑interprets the data to support a broader conclusion about diesel’s declining economics. [confidence: medium]

## Mistral mistral-small-latest

[Mistral API error 429: {"object":"error","message":"Rate limit exceeded","type":"rate_limited","param":null,"code":"1300","raw_status_code":429}]
