# Fact/interpretation check — the-world-bank-says-496-million-indians

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-world-bank-says-496-million-indians.html`

Text-SHA1: `d329637d2ea2ae9d`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 5952, Requested 4328. Please try again in 17.099999999s. Need more tokens? Upgrade to Dev Tier today at https]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The Gini of 23 says more about whom the survey misses than about India"* — The claim conflates the **consumption Gini (23.0)** with broader inequality measures (e.g., income Gini at **62** from WID). While the consumption Gini is indeed sensitive to survey coverage (e.g., missing high earners), the statement overgeneralizes by implying the **23 figure itself is unreliable for India’s inequality**, ignoring that it aligns with MoSPI’s own rural/urban consumption Gini trends (0.237/0.284 in 2023-24). The **gap** is that the article later acknowledges consumption Gini understates inequality (due to savings/survey bias) but frames the 23 figure as *only* about survey limitations, which is misleading given its consistency with official data. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"About a fifth of the twelve-year fall at the $4.20 line came in a single year that the World Bank flags as partly better recording"* — While the **2022-23 to 2023-24 drop (33% → 16.1%) is acknowledged as "unprecedented"** and partly survey-driven, the claim **overstates the share of the total decline attributable to this year**. The **12-year fall** (57.7% → 16.1%) is **41.6 percentage points**; the **2023-24 drop alone** is **7.8 points** (23.9% → 16.1%). **7.8/41.6 ≈ 18.8%**, not "a fifth" (which would be ~20.5%). The **gap** is the rounding/approximation error in the article’s phrasing ("about a fifth"), which could mislead readers about the relative contribution of this year’s change. [confidence: high]

---
**OUTDATED DATA:**
- *"Rs 19.47 per international dollar (2021 PPP conversion factor)"* — The **latest official PPP conversion factor for India** (as of 2025) is **Rs 19.60** (International Comparison Program, 2023 round). The article’s figure (Rs 19.47) is from the **2021 PPP update** (used for the $3.00/$4.20 lines in 2021 prices). While the **2021 PPP remains the most recent official benchmark for these lines**, the **2023 round’s factor (Rs 19.60)** would adjust the rupee equivalents slightly (e.g., $3.00 → **Rs 58.80** instead of Rs 58). Re-check: **ICP PPP data (2023 round)**. [confidence: high]
