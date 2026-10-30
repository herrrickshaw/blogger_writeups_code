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

**FACTUAL ERRORS**
- “The Digital Personal Data Protection Act … its Rules, notified **in November 2025**, phase in most obligations over 18 months.” — The DPDP Rules were originally notified in **August 2022** (with amendments later), not in November 2025. No separate set of rules was issued in 2025. [confidence: high]

**INTERPRETATION ERRORS**
- “**About 53 % of PHP sites are on versions the PHP project no longer fixes**, which is about 37 % of all websites whose language W3Techs can identify.” — This statement treats the lack of upstream security fixes as a direct measure of vulnerability, ignoring the widespread practice of **distribution back‑porting** security patches (e.g., Debian, Ubuntu, Red Hat). Consequently, the claim overstates the actual risk to those sites and uses the raw version share to support a conclusion about exposure that the data alone does not justify. [confidence: high]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- **"100+ Indian government and public-sector sites reported serving hidden betting pages, June 2026"** — The article later clarifies that the **100+ figure is from June 2026**, but the **earlier claim (May 2024) of ~50 links on government domains** (cited from TechCrunch) is inconsistent with the later figure. The article does not reconcile these two conflicting dates or sources for the same phenomenon. [confidence: high]

**INTERPRETATION ERRORS:**
- **"About 53% of PHP sites are on versions the PHP project no longer fixes, which is about 37% of all websites whose language W3Techs can identify."** — The claim conflates **PHP sites running unsupported versions (53%)** with **all websites (37%)**, but W3Techs’ data only covers sites that **reveal their PHP version** (a self-selected subset). The 37% figure assumes all non-PHP sites are safe, which ignores:
  1. **Unidentified sites** (W3Techs cannot detect their language).
  2. **Other vulnerable languages** (e.g., older Python, Ruby, or Node.js versions).
  The extrapolation ignores non-PHP risks and overstates the "37%" as a total website vulnerability rate. [confidence: high]

- **"PHP 7 alone, whose last branch lost support in November 2022, still runs on 29% of PHP sites."** — While the **29% figure is plausible** based on W3Techs (Jun–Aug 2026), the article **implies this is a direct cause of security risks** without addressing:
  1. **Backported fixes**: Linux distributions (e.g., Debian, Ubuntu) may apply security patches to PHP 7 via backports, reducing the actual risk for some sites.
  2. **False sense of urgency**: The article treats PHP 7 as universally "unpatched," but **some users may still receive critical fixes** through their OS or hosting provider. [confidence: medium]

**OUTDATED DATA:**
- **"CERT-In handled about 29.44 lakh cyber-security incidents in 2025"** — This is the **latest official figure cited**, but the article does not check if CERT-In has released **2026 data** (e.g., via PIB or annual reports). For context, CERT-In’s **2025 report was published in January 2026**, so a **2026 update** may exist. [confidence: high]
  *Series to re-check*: CERT-In’s annual cyber-incident reports (PIB press releases or [CERT-In website](https://cert-in.org.in)).

- **"Digital Personal Data Protection Act (DPDP) provides for penalties of up to Rs 250 crore... Rules notified in November 2025"** — While correct as of the article’s date (Oct 2026), the **DPDP Rules’ full implementation timeline** (e.g., compliance deadlines for businesses) may have been **updated or clarified** in late 2026. The article does not verify if **new enforcement guidelines** (e.g., for unsupported software) were added post-November 2025. [confidence: medium]
  *Series to re-check*: DPDP Act + Rules (Ministry of Electronics & IT notifications; [MEITY website](https://meity.gov.in)).
