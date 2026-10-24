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

**INTERPRETATION ERRORS**  
- *“What it replaces: guessing whether a rewrite is worth it; the repo documents a measured 5.94× speedup on one pipeline and, just as usefully, the benchmarking mistake that first made C++ look 40 % slower.”* — The article treats the 5.94× speed‑up observed on a single, highly specific 19‑market pipeline as evidence that a C++ rewrite is broadly “worth it” for any quant‑research workflow. The benchmark covers only one particular data layout, set of libraries, and hardware configuration; it does not account for other pipelines, different data volumes, or alternative C++ implementations. Extrapolating this single result to a general claim about the value of rewriting entire stacks is an apples‑to‑oranges comparison. [confidence: high]

**OUTDATED DATA**  
- *“Grand total: Python 9.52 s vs C++ 1.60 s = 5.94×”* — These timing figures are taken from the committed report dated **12 July 2026**. The repository continues to be active (e.g., later commits may have added optimisations, changed dependencies, or altered the benchmark data layout). A newer benchmark report (or updated `MIGRATION_PLAN.md`) released after July 2026 would provide the current performance picture. The series to re‑check is the **pipeline_cutover benchmark results** in `benchmarks/pipeline_cutover/report_*.html`; look for any report dated after July 2026. [confidence: medium]

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- **"5.94x C++ release vs Python, 19-market pipeline (committed report) 19/19 markets with exact output match (committed report) 9.52s vs 1.60s total benchmark time, Python vs C++ release 40% slower: the original debug-build result, later corrected"** — The claim conflates two distinct benchmark results (debug vs. release) without clarifying that the "40% slower" figure (12.29s C++ vs 8.79s Python) is from a debug build, while the 5.94x speedup (1.60s C++ vs 9.52s Python) is from a release build. The article does not explicitly state that the "40% slower" claim is incorrect or misleading in context. [confidence: medium]

INTERPRETATION ERRORS:
- **"The build needs vcpkg and heavy dependencies, and the benchmark needs the author's production data layout, which is not in the repo."** — The article implies that the benchmark *cannot* be reproduced without the author’s specific data layout, but the repo’s `benchmarks/pipeline_cutover` directory includes environment variables (`BAZAARTALKS_REPO`, `BAZAARTALKS_OHLC_SEED`, etc.) designed to override paths, suggesting partial reproducibility is possible with alternative data. The claim overstates irreproducibility. [confidence: high]

OUTDATED DATA:
- **"report dated 12 July 2026"** — The article was published on 22 October 2026, and no newer benchmark report or update is referenced. While the data may still be current, readers should verify if the repo has updated benchmarks or corrected figures post-publication. [confidence: medium]
