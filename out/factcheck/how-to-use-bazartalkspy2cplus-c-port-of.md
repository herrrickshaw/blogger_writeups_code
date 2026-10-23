# Fact/interpretation check — how-to-use-bazartalkspy2cplus-c-port-of

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-bazartalkspy2cplus-c-port-of.html`

Text-SHA1: `26cc5619f57b9f0d`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 5665, Requested 4729. Please try again in 17.955s. Need more tokens? Upgrade to Dev Tier today at https://con]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"5.94x C++ release vs Python, 19-market pipeline (committed report) 19/19 markets with exact output match (committed report) 9.52s vs 1.60s total benchmark time, Python vs C++ release 40% slower: the original debug-build result, later corrected"** — The claim conflates two distinct benchmark results (debug vs. release builds) without clarifying that the 40% slower figure refers only to the debug build, not the overall 5.94x speedup. The 19/19 exact-match assertion is correct for both runs, but the phrasing risks implying the 40% slowdown applies to the release build, which it does not. [confidence: high]

INTERPRETATION ERRORS:
- **"The build needs vcpkg and heavy dependencies, and the benchmark needs the author's production data layout, which is not in the repo."** — The article correctly notes the benchmark cannot be reproduced from the repo alone, but this is framed as a limitation of the *build* process (vcpkg/dependencies) rather than the *benchmark* specifically. The core issue is the data layout, not the build itself, which could mislead readers into thinking the build is inherently non-reproducible. [confidence: high]

OUTDATED DATA:
- **"report dated 12 July 2026"** — The article was published on **22 October 2026**, and no newer benchmark report or data revision is mentioned. While the claim may still be accurate, readers should verify if the author has updated the benchmark since the original report (e.g., via a later commit or release). [confidence: medium]
