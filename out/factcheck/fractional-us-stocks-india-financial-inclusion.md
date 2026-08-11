# Fact/interpretation check — fractional-us-stocks-india-financial-inclusion

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/fractional-us-stocks-india-financial-inclusion.html`

## Gemini gemini-flash-latest

[Gemini API error 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota ex]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "India has roughly 23.15 crore demat accounts as of June 2026" — This claim cannot be verified against a primary source, but it is cross-checked against more recent June 2026 industry reporting, so the confidence is medium [confidence: medium]
- "SEBI rejected a similar fractional-ownership proposal in its regulatory sandbox in 2021" — This claim is based on the article's text, but the primary source is not provided, so the confidence is medium [confidence: medium]

INTERPRETATION ERRORS:
- "The inclusion case for fractional investing is real, but it's currently asymmetric" — The article concludes that fractional investing has solved the problem of accessing foreign high-priced stocks, but not domestic ones. However, this conclusion is based on the current regulatory environment and may not account for potential future changes or workarounds [confidence: medium]
- "A claim worth flagging and setting aside: several crypto-industry news sites... have reported that SEBI has already launched 'tokenized' fractional shares of Reliance Industries for retail investors" — The article dismisses this claim as unverified, but it may be a genuine development that has not been officially announced by SEBI, highlighting the need for verification of information through official channels [confidence: high]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "Indian investing apps already let you buy a $10 slice of a $780,000 Berkshire Hathaway share." — The article later states Berkshire Hathaway Class A shares are worth ~$780,000 as of early August 2026, but the claim that Indian apps allow fractional purchases of this share is presented as a current reality. However, the article also notes that fractional ownership of Indian stocks is illegal and the regulatory path only opened in mid-2025, implying fractional US stock investing may not yet be widely available in India. The claim lacks verification in the article itself. [confidence: medium]

- "India has roughly 23.15 crore demat accounts as of June 2026" — The article cites this figure but also references "17.10 crore mark" from SBI Securities, creating inconsistency. The June 2026 figure is not corroborated by the primary source cited (SBI Securities), which only mentions exceeding 17.10 crore. [confidence: high]

INTERPRETATION ERRORS:
- "Fractional investing hasn't closed that gap yet" — The article claims fractional investing hasn't closed the gap between the price of an Apple slice and an MRF slice, but this conflates two different markets (US vs. Indian stocks). Fractional investing in US stocks (like Apple) is already possible, while fractional investing in Indian stocks (like MRF) is not. The "gap" is not between two similar products but between two distinct regulatory regimes. The claim implies a failure of fractional investing in general, when the issue is specific to Indian stocks. [confidence: high]

- "The inclusion case for fractional investing is real, but it's currently asymmetric." — While the article correctly notes that fractional investing in US stocks is possible and in Indian stocks is not, the claim that this creates an "asymmetric" inclusion case is an overgeneralization. The asymmetry is not in the concept of fractional investing itself but in the legal and regulatory frameworks governing Indian vs. foreign stocks. The term "asymmetric" suggests a balanced comparison where one side is more developed, but the reality is a binary legal barrier for Indian stocks. [confidence: medium]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
