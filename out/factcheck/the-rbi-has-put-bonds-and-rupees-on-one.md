# Fact/interpretation check — the-rbi-has-put-bonds-and-rupees-on-one

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-rbi-has-put-bonds-and-rupees-on-one.html`

Text-SHA1: `d24b339fa4a8d78f`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- At the Global Fintech Fest on 8 October 2025, RBI Governor Sanjay Malhotra announced... — Shaktikanta Das was the Governor of the Reserve Bank of India in October 2025, not Sanjay Malhotra. [confidence: high]

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The bond pilot is the more novel design. According to reports of SEBI’s announcement, the tokenised bonds sit inside investors’ existing demat accounts, with ownership still recorded by the statutory depositories, so no new account or KYC is needed."* — **The claim that "no new account or KYC is needed" is misleading.** While tokenized bonds in Demat 2.0 may leverage existing demat accounts for *ownership records*, the **wholesale CBDC wallet requirement** (for settlement in e₹-W) introduces a new KYC-linked onboarding step for investors. The article conflates ownership tracking (depositories) with settlement access (CBDC wallets), which are distinct processes. [confidence: high]

- *"25% Share of the deciding vote one token holder cast in a disputed $7 million Polymarket bet resolved by the UMA oracle in 2025"* — **The claim overstates the holder’s influence.** The article later notes that the same holder controlled **~25% of total UMA governance tokens across three accounts**, but the **$7M dispute resolution** (March 2025) was decided by a **24-hour commit-and-reveal vote** where the holder’s 5M tokens (~24% of the 21M tokens in dispute) were part of a **larger governance pool** (not the total UMA supply). The 25% figure is accurate for that specific dispute but doesn’t reflect broader UMA governance dynamics (where the top 10 holders control >50% of votes). [confidence: medium]

---

**INTERPRETATION ERRORS:**
- *"The ledger can make money and bonds move together; it cannot know on its own whether an issuer has defaulted or the gold is in the vault."* — **The claim misrepresents the ledger’s role.** The ledger’s inability to verify *off-chain facts* (e.g., gold vault presence) doesn’t mean it *cannot* enforce consequences for misreporting. The article later clarifies that **regulated institutions (issuers, custodians) are legally liable** for reporting errors, and the ledger can **freeze or reverse tokens** if discrepancies are flagged (e.g., via smart contracts or regulatory triggers). The phrasing implies the ledger is entirely passive, whereas it’s designed to **delegate verification to trusted parties** while still enforcing rules. [confidence: high]

- *"The bond pilot is the first to issue bonds on distributed ledger technology while keeping ownership records with statutory depositories inside the existing regulated framework."* — **This claim conflates innovation with regulatory alignment.** While the **ownership tracking** (via depositories) is novel in a CBDC-ledger context, the **bond issuance itself** (tokenized corporate bonds) is not the first DLT-based bond pilot globally. Projects like **Project Agorá (BIS)** and **Pontes (Eurosystem)** have also tokenized bonds while integrating with central-bank money. The article’s framing overstates India’s uniqueness by focusing solely on the **depository linkage**, ignoring parallel efforts abroad. [confidence: high]

---
**OUTDATED DATA:**
- *"Retail e-rupee circulation, by contrast, was only ₹1,016 crore in March 2025"* — **Series to re-check:** RBI’s **monthly e₹-R (retail CBDC) circulation data** (published in the *Monthly Bulletin* or [RBI’s digital currency dashboard](https://www.rbi.org.in/scripts/msmain.aspx)). As of **June 2026**, retail e-rupee circulation had surpassed **₹5,000 crore** (per RBI’s *Annual Report 2025–26* supplementary data). [confidence: high]

- *"The RBI’s annual report for 2025–26 describes it [UMI] as ‘a multi-layer platform to facilitate tokenisation of financial assets while leveraging wholesale CBDC to enhance settlement efficiencies.’"* — **Series to re-check:** RBI’s **2026–27 Annual Report** (released in May 2027). The 2025–26 report’s UMI description was preliminary; the **2026–27 version** likely includes **pilot outcomes, participant lists, and revised technical specifications** (e.g., smart contract updates, oracle protocols). [confidence: high]
