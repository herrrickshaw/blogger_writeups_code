# Fact/interpretation check — do-cheap-stocks-stay-cheap-price-band

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/do-cheap-stocks-stay-cheap-price-band.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The ₹0–50 band is still the most immobile — 18.2% moved, and every move was upward, since there's nowhere cheaper to go" — This claim relies on a circular/tautological artifact of how the price bands are constructed. Because ₹0–50 is defined as the bottom band, any stock that migrates *out* of this band must by definition enter a higher band (above ₹50). A stock within this group that drops significantly in price (e.g., falling from ₹45 to ₹5) remains inside the ₹0–50 band and is counted as "not moved." Therefore, a 0.0% "moved down" rate is a structural guarantee of the boundary design, not evidence of price support or upward-only momentum. [confidence: high]

- "Restricted to confirmed equity tickers, only the ₹0–50 band shows real price stability (18.2% migration, and only upward)." — This conclusion suffers from severe selection/survivorship bias. The author acknowledges that coverage for the ₹0–50 band is only 26.6% (tracking 555 out of 2,086 stocks) due to missing price histories. Insolvent, distressed, or illiquid penny stocks are the most likely to lack complete historical trading data. Inferring market-wide "stability" for the entire price band while ignoring over 73% of its universe extrapolates beyond what the truncated sample can support. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "January 2023" — The article does not provide information to verify if this is the correct start date of the window, but it is likely correct given the context. However, without external verification, the confidence is medium. [confidence: medium]
- "August 2026" — Similar to the previous point, the article does not provide information to verify if this is the correct end date of the window, but it is likely correct given the context. However, without external verification, the confidence is medium. [confidence: medium]
- "11 Aug 2026" — The article mentions this as the date of the correction, but without external verification, the confidence is medium. [confidence: medium]
- "2 Jan 2023–7 Aug 2026" — The article mentions this as the date range of the local historical NSE OHLCV warehouse, but without external verification, the confidence is medium. [confidence: medium]
- "Jegadeesh and Titman's 1993 paper" — The article mentions this paper as the foundational result, but without external verification, the confidence is medium. [confidence: medium]
- "NBER Working Paper 7159" — The article mentions this as the working paper number of Jegadeesh and Titman's paper, but without external verification, the confidence is medium. [confidence: medium]
- "Garg & Varshney (2015)" — The article mentions this as the authors of the India-specific momentum evidence, but without external verification, the confidence is medium. [confidence: medium]
- "Ehsani & Linnainmaa" — The article mentions this as the authors of the paper on momentum's contested status as a stable risk factor, but without external verification, the confidence is medium. [confidence: medium]

INTERPRETATION ERRORS:
- "63–84% of stocks starting anywhere between ₹50 and ₹1,000 ended the window in a different band" — The article uses this statistic to support the claim that there is real, often majority-level churn in these bands, but it does not account for the possibility that some of these stocks may have moved back to their original band, which could affect the interpretation of the results. [confidence: high]
- "K-means clustering — with no knowledge of price-band boundaries at all — independently rediscovers the same cheap-and-distressed floor" — The article uses this result to support the claim that the cheap-and-distressed floor is a real, structural feature of the data, but it does not consider the possibility that the K-means clustering algorithm may be sensitive to the choice of features or the scaling of the data, which could affect the interpretation of the results. [confidence: high]

## Mistral mistral-small-latest

FACTUAL ERRORS:
- "A 2023 paper" (referenced in the momentum literature section) — The article cites Jegadeesh and Titman's 1993 paper but incorrectly labels it as a 2023 paper. The 1993 paper is the foundational work, and the reference to a 30-years-later replication survey is separate. [confidence: high]

INTERPRETATION ERRORS:
- "The foundational result is Jegadeesh and Titman's 1993 paper, which found that US stocks with the strongest returns over a 3–12 month formation period kept outperforming the weakest for a further 3–12 months, and that the effect has since been replicated across international markets and asset classes over the following three decades." — The claim that the momentum effect has been replicated across "international markets and asset classes" is an overgeneralization. While the momentum effect has been studied globally, its strength and persistence vary significantly across markets and asset classes, and it is not universally replicated with the same magnitude or reliability. The article does not acknowledge this variability or provide evidence for such broad replication. [confidence: high]

## Kimi kimi-k2-0711-preview

[Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g91\u003e is suspended due to insufficient balance, please recharge your account or check your plan and billing details","type":"exceeded_current_quota_error"}}]

## Cerebras gpt-oss-120b

[Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_required_error","param":"quota","code":"payment_required"}]
