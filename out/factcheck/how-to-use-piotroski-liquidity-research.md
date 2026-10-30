# Fact/interpretation check — how-to-use-piotroski-liquidity-research

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-piotroski-liquidity-research.html`

Text-SHA1: `d4a13901b2774ce1`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERROR:
- "The universe mean (34%) far above its median (15%) points to outliers, probably unadjusted corporate actions in the price panel, so read medians only." — A right-skewed distribution with a mean significantly higher than the median is a standard mathematical characteristic of equity return data (where returns have a lower bound of -100% and an infinite upside) and does not inherently indicate unadjusted corporate actions or outliers, though outliers can exacerbate skewness. [confidence: high]

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 4648, Requested 6811. Please try again in 25.9425s. Need more tokens? Upgrade to Dev Tier today at https://co]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **none found**

INTERPRETATION ERRORS:
- **"The premium tracks illiquidity, with a capacity of about $250,000"** — The claim conflates two distinct metrics: the *execution cost* ceiling (derived from turnover/day and spread impact) and the *premium attribution* (which is empirically tied to illiquidity tiers but not causally proven to be *only* illiquidity). The cost test later notes the script’s 20% volume ceiling is unused, and the $250k figure is a *proxy* for liquidity constraints, not a direct causal link. The reasoning gap is that the article treats the cost ceiling as evidence of illiquidity’s role without addressing whether size, survivorship bias, or other factors could also explain the premium’s persistence in illiquid firms. [confidence: high]

OUTDATED DATA:
- **none found**
