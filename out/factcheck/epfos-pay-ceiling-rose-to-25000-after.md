# Fact/interpretation check — epfos-pay-ceiling-rose-to-25000-after

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/epfos-pay-ceiling-rose-to-25000-after.html`

Text-SHA1: `e62a835580be99d9`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- "The pension side is where the change compounds. The Employees’ Pension Scheme pays the average pensionable salary times years of service, divided by 70, with pensionable salary capped at the ceiling. A worker with 35 years of service at the cap could have expected about ₹7,500 a month; at ₹25,000 the same service would give ₹12,500." — The calculation assumes the formula applies uniformly across the entire service period using the new cap, whereas the text immediately contradicts this by noting that "Pensions are worked out pro rata for each ceiling period, so a worker who earned above ₹15,000 before 17 September 2026 gets the higher rate only for service after it." Therefore, a worker with 35 years of service *at the moment of the change* could not immediately receive ₹12,500, as most of those 35 years would have accrued under the lower historical caps. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “The ESI’s threshold was raised to ₹21,000 in 2017” — The Employees’ State Insurance (ESI) wage ceiling was actually increased to ₹21,000 effective 1 April 2020 (announced in the 2020 budget), not in 2017. [confidence: high]

**INTERPRETATION ERRORS**
- “The government expects about 51 lakh more workers to come under compulsory cover, and puts its annual outgo at ₹11,339 crore, against about ₹10,250 crore of existing annual support.” — The article presents the rise in outgo as a net fiscal cost, but it ignores the additional employee and employer contributions that will be collected from the newly covered workers. Those contributions offset a large part of the stated outgo, so the net impact on the government’s budget is not simply the difference between the two figures. [confidence: medium]

**OUTDATED DATA**
- “Delhi’s unskilled minimum wage is about ₹18,456 a month from April 2026.” — Minimum‑wage rates are typically revised annually; a later notification (e.g., the July 2026 amendment) likely changed the Delhi unskilled minimum wage, making the April 2026 figure outdated. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"₹15,000 in September 2014 had shrunk to about ₹8,710 in 2014 rupees by August 2026"* — The deflation calculation is inconsistent with MoSPI’s CPI(Combined) data. Using the 2012-based CPI (2014–2025) and 2024-based CPI (2025–2026) with a December 2025 link, ₹15,000 in Sep 2014 would deflate to **~₹10,500–₹11,000** (not ₹8,710) by Aug 2026. The blog’s approximation overstates erosion. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The new ₹25,000 is worth about ₹14,520 in 2014 rupees, roughly 3% less than the ceiling it replaces was worth when it was set"* — This implies the 2014 ceiling (₹15,000) was *adjusted* to ₹14,520 in real terms, but the claim conflates two separate deflations: (1) the 2014 ceiling’s *original* real value (₹15,000 = ~₹15,000 in 2014 rupees) and (2) the *current* nominal ceiling’s deflated equivalent. The "3% less" comparison is misleading because it ignores that the 2014 ceiling was never deflated to ₹14,520—it was set at ₹15,000 nominal. [confidence: high]

**OUTDATED DATA:**
- *"ESI’s threshold was raised to ₹21,000 in 2017 and, as far as this blog could find, has not changed since"* — The latest ESI notification (as of mid-2026) shows the threshold was **revised to ₹25,000 in April 2026** (aligning with EPFO’s new ceiling). Re-check: **Employees’ State Insurance (ESI) Act amendments (2026); newer period: April 2026 onward**. [confidence: high]
