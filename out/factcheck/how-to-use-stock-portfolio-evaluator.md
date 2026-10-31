# Fact/interpretation check — how-to-use-stock-portfolio-evaluator

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-stock-portfolio-evaluator.html`

Text-SHA1: `59c5764dc79a4731`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "Sources: Cloned github.com/herrrickshaw/stock-portfolio-evaluator (archived) into a clean folder, installed it in a throwaway virtualenv with Python 3.14 and ran the tests and the stock-eval commands on an invented six-stock CSV on 23 October 2026." — Python 3.14 does not exist as of the stated date or current knowledge, making this version number factually incorrect. [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**  
- **“installed it in a throwaway virtualenv with Python 3.14”** – Python 3.14 has never been released; the latest stable version as of the knowledge cutoff (2024‑06) is Python 3.12. The claim is therefore factually incorrect. [confidence: high]  
- **“default critical ratio (25% / (8% + 25%)) … 76 percent”** – The arithmetic yields 25 ÷ 33 ≈ 0.7576, i.e. 75.8 %, not 76 %. The statement rounds up without justification and misstates the exact figure. [confidence: medium]  

**INTERPRETATION ERRORS**  
- **“Unknown symbols fall back to Technology, which has the largest sector gain figure in the table.”** – The code’s fallback to the *Technology* sector is a hard‑coded default, not a decision based on which sector has the highest gain figure. Stating that the fallback occurs *because* Technology has the largest sector gain conflates implementation detail with a causal explanation that isn’t supported by the source. [confidence: high]  

**OUTDATED DATA**  
- none found.

## Mistral open-mistral-nemo

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- **"The three-month gain figure is a formula of fixed sector numbers, not a forecast, and the tool fetches no prices or news."**
  — The claim conflates the *static* nature of the gain calculation (which relies on hardcoded sector/beta tables and past returns) with the *lack of market data*. While true that the tool doesn’t fetch live prices, the "three-month gain figure" is still *derived from invented current prices* (e.g., TCS at ₹3,300, ZOMBIECO at ₹120) and *past returns* (e.g., -40% for ZOMBIECO), which are not "fixed" but *simulated inputs*. The distinction between "fixed sector numbers" and "invented price data" is blurred, making the interpretation misleading. [confidence: high]

OUTDATED DATA:
- none found
