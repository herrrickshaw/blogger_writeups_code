# Fact/interpretation check — indian-it-in-ai-era

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/indian-it-in-ai-era.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "The current account deficit was $25.2 billion — 0.6% of GDP" — The article does not provide the GDP figure for FY2025-26 to verify this claim [confidence: medium]
- "India's gross services exports reached $421.3 billion in FY2025-26" — This figure cannot be verified without access to the original RBI data or other reliable sources [confidence: medium]

INTERPRETATION ERRORS:
- "Net services receipts hit $216.6bn in FY2025-26 , up $27.8bn in a single year" — The article uses this fact to argue that AI is not hurting Indian IT, but it does not consider that the growth in services exports might be due to other factors, and the impact of AI might be visible in other indicators such as pricing power or employment [confidence: high]
- "India's back-office exports sit 27% above their pre-AI trend" — The article uses this fact to argue that AI is helping India's services exports, but it does not consider that this growth might be due to other factors, and the impact of AI on employment or pricing power might be more significant [confidence: high]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Services · Balance of payments · 4 August 2026" — The article is dated 4 August 2026, but the referenced data (e.g., FY2025-26 figures) and sources (e.g., RBI's Q4 2025-26 report) are for FY2025-26, which would end on 31 March 2026. The article incorrectly labels the data as FY2025-26 while using a future date (4 August 2026) for publication. [confidence: high]

- "Net services receipts hit $216.6bn in FY2025-26, up $27.8bn in a single year." — The RBI's *Developments in India's Balance of Payments, Q4 2025-26* shows net services receipts at $216.6bn for FY2025-26, but the $27.8bn increase is incorrect. The actual increase from FY2024-25 ($188.8bn) to FY2025-26 ($216.6bn) is $27.8bn, but the article implies this is a single-year jump from the previous year's data, which is accurate. However, the phrasing "in a single year" could be misinterpreted as a year-over-year increase from FY2024-25 to FY2025-26, which is correct, but the claim is technically accurate. No factual error found here. [confidence: none]

INTERPRETATION ERRORS:
- "The warning signs are elsewhere: net hiring has collapsed from ~450,000 (FY22) to 135,000 (FY26) against a growing revenue base, and chief executives now name 'AI deflation' worth 3–5% of revenue." — The article correctly notes the decline in net hiring and the acknowledgment of "AI deflation" by executives. However, it conflates these two observations to imply a causal link between AI and the hiring collapse without sufficient evidence. The hiring decline could be due to other factors (e.g., automation, restructuring, or cyclical trends), and the "AI deflation" claim is based on executive statements rather than measured data. The article does not establish that AI is the primary driver of the hiring decline. [confidence: high]

- "So when people ask whether AI threatens Indian IT, the question that matters for the country is narrower and sharper: does it threaten the dollar receipts that make a $337 billion goods deficit survivable at 0.6% of GDP?" — The article argues that the key risk is to dollar receipts from services exports, not jobs. However, this interpretation assumes that the current account deficit's sustainability is solely dependent on services receipts without considering other factors like capital flows, foreign investment, or policy responses. The conclusion that an AI shock would primarily manifest as a currency problem is plausible but not definitively supported by the data presented. The article does not address potential mitigating factors (e.g., RBI interventions, capital inflows) that could stabilize the rupee even if services receipts decline. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
