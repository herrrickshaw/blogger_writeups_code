# Fact/interpretation check — how-to-use-research-design-system-one

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/how-to-use-research-design-system-one.html`

Text-SHA1: `e9dc42bb5567a461`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS**
- **Claim:** “Code: github.com/**herrrickshaw**/research-design-system”  
  **Issue:** The actual repository is hosted at **github.com/**herrickshaw**/research-design-system** (single “r” in the username). The extra “r” makes the URL incorrect and would lead to a 404.  
  **[confidence: high]**

**INTERPRETATION ERRORS**
- **Claim:** “What it replaces: re‑copying styles between HTML pages, Blogger themes and one‑off dashboards.”  
  **Issue:** The design‑system kit only supplies a shared set of CSS tokens and themes; it does **not** automatically migrate or rewrite existing stylesheets, nor does it adapt disparate HTML structures. Users still need to manually adjust their pages to use the tokens and themes. Therefore the statement overstates the causal effect—​the kit reduces the amount of copying **but does not fully replace** the need for manual style work.  
  **[confidence: medium]**

**OUTDATED DATA**
- none found

## Mistral open-mistral-nemo

Here’s the structured fact-checking response based on the provided article:

---

**FACTUAL ERRORS:**
- *"Revised 26 October 2026"* — The date **26 October 2026** is implausible for a published article (as of June 2024) and contradicts the revision history ("v1.0.0 — 26 October 2026 — first published") unless the article is intentionally set in the future for narrative purposes. [confidence: high]

**INTERPRETATION ERRORS:**
- *"The same report template rendered in all four themes by changing only the theme stylesheet and one body class"* — While this is technically correct for the *visual* demonstration, the claim implies **generalizability** to all use cases without acknowledging that:
  1. The article explicitly states the **WeasyPrint PDF path and Blogger theme were not tested** for this post.
  2. The "scratch copy" of the template was edited per theme for screenshots, meaning the repo itself was not modified—limiting reproducibility for others. The claim overstates the kit’s out-of-the-box functionality. [confidence: high]

**OUTDATED DATA:**
- *"Four themes rendered in the demo 18 component class names in the set"* — No newer official release is mentioned, but the **19 October 2026 render date** (and 26 October 2026 revision) suggests these figures may be outdated if the project is no longer active or has since evolved. Re-check the [GitHub repository](https://github.com/herrrickshaw/research-design-system) for updates. [confidence: medium]

---
