# Fact/interpretation check — how-to-use-agentic-insurance-agent-open

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-agentic-insurance-agent-open.html`

Text-SHA1: `44b160d5f1b049b9`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-latest

FACTUAL ERRORS:
none found

INTERPRETATION ERRORS:
none found

OUTDATED DATA:
none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- “The demo did not start the Docker and Operaton stack, so everything about the live engine comes from the README, which reports a verified live run on 2026‑10‑16.” — The article first states the demo never started the workflow engine, yet later claims the README documents a *verified live run* on a specific date. No external evidence exists that such a live run occurred; the README only describes the demo setup. This contradictory statement is factually inaccurate. [confidence: high]

**INTERPRETATION ERRORS**
- “The 100 % eval scores prove that the test harness works, not that a model is good.” — While the scores indeed show the harness behaved as expected, the article uses this to imply the mock model’s performance is irrelevant for any real‑world assessment. However, the evaluation metrics (classification accuracy, field exact match, etc.) were all measured on a *mock* provider with a deliberately tuned model; therefore the scores cannot be generalized to claim the harness alone validates the model’s suitability for production. The reasoning conflates “test harness correctness” with “model quality” without acknowledging that the mock model’s perfect scores are a product of over‑fitting to the test set. [confidence: high]

**OUTDATED DATA**
- “Python 3.12 or newer … python.org or brew install python@3.12” — The article lists Python 3.12 as the minimum required version. As of October 2026, Python 3.13 has been officially released (2026‑09‑xx) and is the current stable release. The requirement should be revisited to reflect the newer version, or at least note compatibility with Python 3.13. [confidence: medium]

## Mistral open-mistral-nemo

Here’s the structured fact-checking report based on the provided article:

---

**FACTUAL ERRORS:**
- *"The demo ran the test suites and the evaluation gate. It did not start the workflow engine or the Docker stack."* — The article claims the demo was run on **18 October 2026** and explicitly states the workflow engine/Docker stack was *not* started, but the README’s own claim of a "verified live run on 2026-10-16" (cited as a source) contradicts this. The article does not reconcile these dates or clarify whether the "verified live run" refers to a separate test or is outdated. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The 100% eval scores prove that the test harness works, not that a model is good."* — While this is factually correct, the article later states the mock model was "tuned on its own golden set," which implies the 100% scores may reflect *artificial* accuracy rather than a robust evaluation. The reasoning gap is that the article conflates "harness functionality" with "model quality" without addressing whether the mock tuning introduces bias or unrepresentative benchmarks. [confidence: high]

**OUTDATED DATA:**
- *"The demo ran the test suites and the evaluation gate... 16 AI service tests passed in the demo"* — The article cites the demo as of **18 October 2026** but does not verify whether newer test suites (e.g., post-v1.0.0 updates) or AI provider integrations (e.g., live model calls) have been added. The GitHub repo’s latest commit or release notes should be checked for updates beyond v1.0.0. [confidence: medium]

---
**Note:** No other categories contained actionable issues based on the provided text. The article’s claims about technical limitations (e.g., lack of production readiness) are transparently disclosed as caveats, not factual errors.
