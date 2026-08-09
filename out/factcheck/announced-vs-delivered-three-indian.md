# Fact/interpretation check — announced-vs-delivered-three-indian

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/announced-vs-delivered-three-indian.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "2023-24 | ₹36,000 crore (original budget) | Shortfall acknowledged; overall own-tax revenue (across excise, commercial taxes, stamps & registration, motor vehicle tax) missed target by ₹12,192 crore | Target missed — called "too ambitious" in government's own budget language" — Apples-to-oranges comparison. The table specifically tracks Karnataka's ₹36,000 crore excise target, but uses the ₹12,192 crore shortfall of total state own-tax revenue (which combines commercial taxes, stamp duty, motor vehicle tax, and excise) to evaluate the excise target outcome, conflating total state tax deficit with excise tax shortfall. [confidence: high]
- "Mera Pani Meri Virasat (crop diversification, backward-linkage raw material) | ~19,670 acres verified diversified — against ~13.5 lakh ha (3.34 million acres) of Haryana paddy area, a rounding error against the target base" — Apples-to-oranges comparison. Mera Pani Meri Virasat is a water-conservation scheme targeting paddy-to-alternate-crop switching. Comparing acreage under this single scheme against total paddy land (3.34 million acres) misapplies a specific water scheme's footprint to evaluate the 2018 Food Processing Policy's distinct goal of bringing 14% of gross cropped area under horticulture. [confidence: high]
- "...meaning the new ₹30,000-crore, five-year target implies delivering at more than six times the annual pace of the previous ten years (₹9,178cr/decade ≈ ₹918cr/yr vs. ₹30,000cr/5yr = ₹6,000cr/yr)." vs "And the current ₹30,000-crore target requires more than tripling the realized pace of the prior decade..." — Internal reasoning gap. The article calculates that going from ₹918 crore/year to ₹6,000 crore/year requires a 6.5x increase ("more than six times"), but downscales its own math in the section verdict to "more than tripling" (3x), creating an internal inconsistency in its comparative finding. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "Uttar Pradesh's EV policy, notified on 14 October 2022" — The article does not provide a source for this specific date, but it is mentioned in the official notification, so this claim is likely correct, but without access to the primary source, the confidence is medium [confidence: medium]
- None of the other claims appear to be factually incorrect based on the information provided in the article.

INTERPRETATION ERRORS:
- "UP has genuinely become India's leading CBG state in plant count — that's a real result, not spin. But 'most plants of any state' and '1,000 TPD by 2026-27' are different claims, and with roughly a year left on the clock, no public source we found closes that gap with a number." — The article correctly identifies that the policy's target is 1,000 TPD, but the available data only shows the number of plants, not the total capacity, which is the actual target. This is an extrapolation beyond what the data shows [confidence: high]
- "Karnataka sets an ambitious excise target each budget, misses or downgrades it mid-year, but still posts real year-on-year revenue growth (12.7% in the most recent comparable period)" — The article concludes that the policy is on a growth trend, but this might be an apples-to-oranges comparison, as the growth rate is compared to the previous year's target, not the actual revenue. This could be a false causal claim, as the growth trend might not be directly related to the policy [confidence: medium]
