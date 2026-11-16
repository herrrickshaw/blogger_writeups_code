[kept verbatim: dated update notes]

## 1. What ABHA actually is

ABHA sits inside the Ayushman Bharat Digital Mission (ABDM), run by the National Health Authority under the Ministry of Health and Family Welfare, launched September 2021. ABHA itself is the citizen-facing piece: a random 14-digit number that acts as a portable identifier for a person's health records across hospitals, labs, clinics and digital health apps, created free of cost and entirely voluntary. Two other pieces sit alongside it — an ABHA Address, an easy-to-remember username in the form name@abdm, and the ABHA mobile app (or any compatible Personal Health Record app), which is where a user actually views, stores and consents to sharing their linked records.

An Ayushman Bharat health facility in Nagpur — the kind of provider where ABHA's consent-gated record-linking, the subject of this piece, actually happens. [Urban Primary Health Centre Ayushman Bharat Bidipeth Nagpur](https://commons.wikimedia.org/wiki/File:Urban_Primary_Health_Centre_Ayushman_Bharat_Bidipeth_Nagpur.jpg), Ganesh Dhamodkar, CC BY-SA 4.0, via Wikimedia Commons.

The mechanism that makes this work is consent-gated data exchange, not a central government database of everyone's medical history. Records generated at a hospital, lab or clinic stay with that provider; ABHA links a pointer to them under the person's ID, and nothing is pulled or shared without an explicit, per-request consent action from the user in their PHR app.

On the provider side, ABDM runs two companion registries that make this interoperable: the Healthcare Professionals Registry (HPR) for doctors and clinicians, and the Health Facility Registry (HFR) for hospitals, clinics and labs — plus a Health Information Exchange & Consent Manager (HIE-CM), a Unified Health Interface (UHI) for appointment booking, and a National Health Claims Exchange (NHCX) for insurance claims. ABHA is the identity that threads through all of them.

## 2. The scale, in real numbers

Update, 27 September 2026. The 93+ crore accounts / 104+ crore records figures below, from a 6 July 2026 fact sheet, are now superseded. PIB's own subsequent release, "100 Crore Health Records Linked with ABHA under ABDM" (PRID 2264241), and later reporting put the count at roughly 97.6 crore ABHA IDs and 119.95 crore linked health records as of 17 September 2026 — growth of more than 4 crore accounts and 15 crore records in under three months. The stat cards, table and verdict box below have been updated to the newer figures; the growth trajectory this section describes (never plateauing) still holds and is, if anything, understated by the numbers originally published here.

Cumulative ABHA creation has grown every year since launch, and accelerated rather than plateaued: from 14.7 crore accounts at the end of 2021 to over 90 crore by May 2026, and to roughly 97.6 crore by 17 September 2026, with 119.95 crore health records linked to those accounts — up from the 93+ crore accounts and 104+ crore records reported here as of a July 2026 fact sheet.


[T1 "2. The scale, in real numbers" 6 rows; use rows by number in a chart "table" spec]
  cols: c0 Year (cumulative, calendar-year end) | c1 ABHA accounts, crore
  r0: 2021 | 14.7
  r1: 2022 | 30.4
  r2: 2023 | 50.6
  r3: 2024 | 72.2
  r4: 2025 | 84.5
  r5: 2026 (milestone crossed 30 May) | 90+


Source: PIB, "Ayushman Bharat Digital Mission Crosses Landmark Milestone of 90 Crore ABHA Accounts," 30 May 2026. The 93+ crore and 104+ crore figures below are from a subsequent NHA fact sheet reported 6 July 2026 and are not directly comparable to the year-end series above (different reporting dates, mid-2026 vs. calendar-year-end).

97.6crABHA accounts as of 17 September 2026, up from 14.7cr at end-2021

119.95crHealth records linked to ABHA accounts, per PIB's 17 September 2026 update

49.75%Share of ABHA holders who are women, per NHA's May 2026 milestone release

23.21crScan-and-Share digital OPD tokens generated as of 18 June 2026

Adoption is uneven across states, both in absolute numbers and as a share of population. Uttar Pradesh leads outright with over 15.3 crore ABHAs, followed by Rajasthan and Maharashtra at 7.1 crore each, Bihar at 6.3 crore and West Bengal at 5.9 crore.

But raw counts favour big states; on saturation (ABHAs relative to population), a different set of states leads — Andhra Pradesh at 98.5%, Odisha at 91.9%, Chandigarh at 90.8%, Rajasthan at 89.7%, Himachal Pradesh at 88.9% and Chhattisgarh at 86.6%, with the Andaman & Nicobar Islands, Ladakh, Lakshadweep, and Dadra & Nagar Haveli and Daman & Diu all reporting full saturation (small union territories where 100% coverage is a much smaller absolute lift than in a state the size of Uttar Pradesh).

Women make up nearly half of all ABHA holders nationally (49.75%), which the National Health Authority has specifically flagged as relevant to maternal and child healthcare continuity — an ABHA created at a first antenatal visit can carry a woman's records through delivery, immunisation follow-ups and beyond, across different facilities and even different states.

## 3. What's actually working: the queue-skip and the app consolidation

The most concrete, measurable use of ABHA so far isn't records-sharing across hospitals — it's a much more mundane thing: skipping the outpatient registration queue. NHA's Scan and Share service lets a patient scan a QR code at a participating facility to register digitally instead of filling out paperwork at a desk; as of 18 June 2026, more than 23.21 crore ABHA-linked digital tokens had been generated this way. That's the kind of adoption number that reflects genuine day-to-day use rather than a one-time account-creation drive, since a token has to be generated at an actual hospital visit.

The government has also consolidated the citizen-facing app layer: Aarogya Setu 2.0, the successor to the COVID-era contact-tracing app repurposed as ABDM's main citizen app, now handles ABHA creation, digital health records, teleconsultation and hospital appointment booking, insurance information, a nearby-facility locator, and wearable-device integration in one interface — rather than requiring a separate app for each function. The government has also disbursed financial incentives exceeding ₹107 crore to hospitals and other participating stakeholders to encourage digital adoption, per the same fact sheet, though the public reporting available for this piece didn't break down that figure by recipient category.

## 4. The honest caveat: consent works on paper, less clearly in practice

ABHA's architecture is genuinely consent-gated — no party, including the government, can pull a specific health record without a per-request consent action from the account holder in their PHR app. That's a real, structural privacy protection, not a marketing claim.

The caveat is what "consent" means in practice for a system this size: informed consent assumes the person granting it understands what they're agreeing to, and independent commentary on ABDM has repeatedly flagged that many users — particularly in rural areas or with lower digital literacy — may not fully grasp how their data is stored, shared or used, which risks consent becoming a formality rather than a meaningful choice.

ABHA is voluntary in principle, but as more hospitals and insurers route services through it, it edges toward becoming a practical gateway to care rather than a genuinely optional add-on for some users. India's Digital Personal Data Protection Act, 2023, and the Digital Personal Data Protection Rules, 2025 (notified in November 2025 and being phased in over about 18 months, to May 2027) form the surrounding legal framework for how this data is meant to be governed, but this piece did not find a primary-source breakdown of how DPDP enforcement specifically applies to ABDM as of publication, so that intersection is flagged here as a real open question rather than a resolved one.

Verdict: ABHA is a real, large, and voluntary digital-identity layer for health records — not a health-insurance scheme, and not (yet) a fully realised consent regime. The adoption numbers (97.6+ crore accounts, 119.95+ crore linked records as of 17 September 2026, 23+ crore queue-skip tokens actually used at real hospital visits) are large enough to represent genuine infrastructure, not just a registration drive. The structural design (consent-gated, provider-held records, no central medical database) is a defensible privacy architecture on paper. Whether that consent is meaningfully informed at the scale ABHA now operates — across states with very different levels of digital literacy — is the part this piece could not verify either way from public reporting, and is worth remaining skeptical about rather than assuming solved because the system is large.

### Related on this blog

See also: [ABHA Covers 93 Crore Patients. Its Doctor Registry Covers 67%, and Insurers Aren't Required to Use the Claims Exchange Yet](https://blog.vertistratsolution.com/2026/09/abha-covers-93-crore-patients-its.html) — how ABHA's patient/doctor/insurer coverage compares against Estonia, Denmark and the UK · [Thali Investing: What's Actually on the Plate When People Say “Diversify”](https://blog.vertistratsolution.com/2026/08/thali-investing-whats-actually-on-plate.html) · [India's Two Tracks of Health Cover, and Where They Actually Meet](https://blog.vertistratsolution.com/2026/08/indias-two-tracks-of-health-cover-and.html) · [India Cannot Sell “China-Free” Medicine While Importing 43% of What’s In It](https://blog.vertistratsolution.com/2026/08/india-cannot-sell-china-free-medicine.html) · [Foreign Capital Found India’s Hospitals — It Is Buying Them, Not Building New Ones](https://blog.vertistratsolution.com/2026/08/foreign-capital-found-indias-hospitals.html)

## What would fix this

[kept verbatim, open: What would fix this; 5 items]
