# Fact/interpretation check — how-to-use-five-open-toolkits-finance

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-five-open-toolkits-finance.html`

Text-SHA1: `7749e8fbca5d991a`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Do not add one (PCPNDT Act)." — The Pre-conception and Pre-natal Diagnostic Techniques (PCPNDT) Act in India regulates the use of pre-natal diagnostic techniques specifically to *prevent* sex determination (and female foeticide), rather than mandating a fetal-sex detector or relating to one in software development in this manner. [confidence: medium]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**
- “Claude subscription or API key; run **claude** inside the cloned folder” — Claude (Anthropic) is accessed via a web UI or through its hosted API; there is no official local command‑line executable named `claude` that can be invoked inside a repository. The article’s description of how to run Claude locally is inaccurate. 【confidence: high】

- “Zotero's connector API starts returning **500** after a few hundred calls” — Zotero’s public API imposes rate limits (typically 100 requests per 5 seconds) but does not habitually return HTTP 500 errors after a few hundred calls. The claim misstates the API’s behavior and is not supported by Zotero’s documentation. 【confidence: medium】

**INTERPRETATION ERRORS:**
- “A DCF that uses levered tax **double counts the interest shield**” — Levered discounted‑cash‑flow models already incorporate the tax shield on interest within the levered free‑cash‑flow calculation. Stating that a levered DCF *necessarily* double‑counts the interest shield is a false causal claim; the double‑counting would only occur if the model were incorrectly constructed, not because the model is levered. The article extrapolates a generic error to all levered DCFs, which the data does not support. 【confidence: high】

**OUTDATED DATA:**
- none found

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- **"The 670-test run was done on the author's main repo with PYTHONPATH set; the public mirror ships the same engines and its dcf and lbo examples gave identical headline numbers."**
  — This implies the public mirror’s outputs are *directly comparable* to the main repo’s, but the article later notes the demo was run on the public mirror (e.g., "the public mirror ships the same engines and its dcf and lbo examples gave identical headline numbers") *without verifying whether the test suite (670 tests) was actually executed on the public mirror or just the main repo. The claim conflates code equivalence with runtime consistency for the test suite. [confidence: high]

OUTDATED DATA:
- none found
