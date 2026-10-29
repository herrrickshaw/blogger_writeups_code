# Fact/interpretation check — half-of-php-websites-run-version-nobody

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/half-of-php-websites-run-version-nobody.html`

Text-SHA1: `f601ddb8ad0603e2`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

[Groq/openai/gpt-oss-120b API error 429: {"error":{"message":"Rate limit reached for model `openai/gpt-oss-120b` in organization `org_01kx5hhftzetdtqn6xnj536ykb` service tier `on_demand` on tokens per minute (TPM): Limit 8000, Used 4244, Requested 6052. Please try again in 17.22s. Need more tokens? Upgrade to Dev Tier today at https://cons]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"100+ Indian government and public-sector sites reported serving hidden betting pages, June 2026"** — The article later clarifies that the **100+ figure is from June 2026**, but the **earlier claim (May 2024) cited in the text ("TechCrunch found about 50 such links on government domains in May 2024") contradicts this**. The June 2026 figure is correct per the source (MediaNama/FalconFeeds), but the May 2024 claim is outdated and inconsistent with the later reporting. [confidence: high]

**INTERPRETATION ERRORS:**
- **"About half of those [PHP] sites run a version of PHP that no longer receives security fixes"** — While the **53% figure is correct for October 2026**, the claim conflates *version shares* (W3Techs data) with *vulnerability exposure*. Many sites on unsupported PHP versions may still receive **backported fixes** (e.g., via Linux distributions like Debian/Ubuntu), meaning the actual unpatched exposure is lower than implied. The article acknowledges this but frames the 53% as a direct vulnerability count, which is misleading. [confidence: high]

**OUTDATED DATA:**
- **"CERT-In handled about 29.44 lakh cyber-security incidents in 2025"** — This is correct as of the article’s date (October 2026), but **no newer official CERT-In data for 2026 is cited**. For updated incident counts, check CERT-In’s latest annual report (likely released in January 2027). [confidence: high]
- **"Digital Personal Data Protection Act (DPDP) Rules notified in November 2025"** — While correct at the time, the **Rules’ full implementation timeline (18-month phase-in) may have seen updates or clarifications** by October 2026. Verify against the latest DPDP Board notifications. [confidence: medium]
