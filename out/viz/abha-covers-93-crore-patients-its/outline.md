Revised
17 September 2026
· v1.0.0 · [what changed](#changelog)

93+crABHA patient accounts, mid-2026 — but a patient-side number only

≤67%Upper bound on the share of India's ~14.2 lakh registered doctors who also hold a Healthcare Professional ID (HPR): the registry count also includes nurses, pharmacists and other professionals

Not mandatoryStatus of insurer participation in the National Health Claims Exchange (NHCX), as of this writing

95%+Share of Estonia's doctors actively using its national EHR, a system live since 2008

Estonia's digital identity card. The same eID infrastructure underlies tax filing, voting and the national health record — one identity layer doing every job, not a health-specific one built in parallel. Source: Wikimedia Commons, [File:E-Residency_card.jpg](https://commons.wikimedia.org/wiki/File:E-Residency_card.jpg), CC BY 2.0.

This blog's own reporting on ABHA already established the patient-facing numbers: 93+ crore accounts, 104+ crore linked health records, a voluntary and consent-gated design with no central medical database. What that piece flagged but didn't have room to answer is the harder question implied by "for the benefit of doctors and insurers" — a record only helps a doctor if enough other doctors are on the matching registry to have put something into it, and it only helps an insurer if claims actually flow through a shared exchange rather than a fax machine.

Three countries usually cited as having solved this — Estonia, Denmark and the UK — show three different paths, and comparing India's actual numbers against theirs is more useful than comparing slogans.

Update, 28 September 2026. The 93+ crore accounts / 104+ crore records figures used throughout this piece, from the 6 July 2026 fact sheet this blog's earlier ABHA piece cited, are now superseded. PIB's own subsequent release ("100 Crore Health Records Linked with ABHA under ABDM", PRID 2264241) puts the count at roughly 97.6 crore ABHA IDs and 119.95 crore linked health records as of 17 September 2026 — the same date this piece was first published. The structural comparison below (patient accounts far outpacing doctor-registry and insurer-exchange coverage) still holds; only the specific account/record counts have grown.

[kept verbatim: dated update notes]

## 1. The patient side: ABHA's coverage is real, but "account created" isn't "record complete"

By sheer count, ABHA's 93+ crore accounts dwarf the population of any single comparison country here. The more useful comparison is coverage as a share of population, and completeness of what's actually linked:


[T1 "1. The patient side: ABHA's coverage is real, but "account created" is" 5 rows; use rows by number in a chart "table" spec]
  cols: c0 Country | c1 Patient-record system | c2 Population coverage | c3 Live since
  r0: Estonia | National Health Information System (X-Road) | ~100% of residents | 2008
  r1: Denmark | Sundhed.dk / Shared Medication Record | 96% recognition; CPR-linked for all residents | 2003 (portal); CPR itself since 1968
  r2: UK (England) | Summary Care Record | 96%+ (55M+ people), <5% opted out | 2010 rollout
  r3: Australia | My Health Record | 90.1% (opt-out since 2019) | 2012 (opt-in), 2019 (opt-out)
  r4: India | ABHA / ABDM | 93+ crore accounts created (voluntary opt-in) | 2021 launch


What the India row doesn't tell you. "93+ crore accounts" measures account creation, not active use the way Denmark's 2.3 million monthly Sundhed.dk visits or Estonia's 2.5 million monthly doctor queries do. This blog's own ABHA piece already found the one genuinely comparable usage number — 23.21 crore Scan-and-Share tokens actually generated at real hospital visits — and flagged that most of the 93+ crore figure can't be verified as active use from public reporting. That gap between accounts created and records actually used in a clinical encounter is exactly what the doctor- and insurer-side numbers below explain.

## 2. The doctor side: a 67% registry versus a 95%+ one

Estonia's national EHR is used by more than 95% of the country's doctors, per Invest in Estonia's own figures, with the system queried roughly 2.5 million times a month. India's equivalent — the Healthcare Professionals Registry (HPR), which issues a 14-digit Healthcare Professional ID (HPID) — had enrolled over 9.5 lakh healthcare professionals by mid-2026 (9.85 lakh in July, per the Health Ministry), against a National Medical Commission count of roughly 1,421,853 total registered doctors in India (Indian Medical Register, April 2026). That registry count covers nurses, pharmacists and other professionals as well as doctors, so dividing it by the doctor count (about 67%) gives an upper bound on doctor coverage, not the doctor share itself; a doctors-only HPR count is not published.

[chart: 
 
 Share of the Country's Doctors on the National Digital Registry 
 HPR (India, voluntary) vs. national EHR (Estonia, tied to practice) 

 India (HPR) 
 
 67% 
 ~9.5 lakh of ~14.2 lakh registered doctors, 2026 

 Estonia (national EHR) 
 
 95%+ 
 System live since 2008; ~2.5 million doctor queries a month 

 Sources: HPR/NMC figures per 2026 secondary reporting; Estonia figure per Invest in Estonia. 
]

A real, substantial registry — and still meaningfully behind a system that made registration effectively universal.

The structural difference is what HPR registration is tied to. In Estonia, a doctor uses the national EHR because it is simply how care is documented and paid for — there is no separate "digital-registration" decision distinct from practising medicine. In India, HPR registration is a voluntary, additional step layered on top of NMC licensure, taking roughly 20–30 minutes with a 3–5 day verification window, per current registration guidance — a real but optional action a licensed doctor has to separately choose to take. 67% coverage after a few years of a voluntary opt-in scheme is a genuinely fast adoption curve; it is also, by definition, not the same thing as a doctor being unable to practise without it.

## 3. The insurer side: this is where India is furthest behind

Denmark's Shared Medication Record already gives hospitals, GPs, pharmacists and municipalities real-time, shared access to a resident's current prescriptions — a single record multiple institution types read and write to, not a claims-specific side channel. India's equivalent mechanism, the National Health Claims Exchange (NHCX), went live in June 2024 as a standardised, FHIR-based pipe for insurance claims — but as of this writing, an IRDAI-constituted panel has only recommended mandating NHCX integration for insurers, in August 2026. Recommending mandatory adoption two years after launch means the exchange this piece's own comparison depends on for "insurers" is, on the evidence available, still in a voluntary onboarding phase, not a functioning universal pipe.

What is working already. This is not a system standing still: NHCX is live, FHIR-compliant claim formats are a real technical standard already in use by early adopters, and the regulatory direction (IRDAI recommending mandatory integration) points toward exactly the outcome Denmark already has. The honest read is "earlier stage, same direction," not "not happening."

## 4. The identifier lesson: a health-specific ID versus a repurposed universal one

Denmark's CPR number has existed since 1968, decades before any digital health record, and does double duty as the identifier for taxation, residency, banking and health together. Estonia's digital ID card plays the same generalist role across its whole e-government stack, health included. ABHA and HPID, by contrast, are purpose-built health-specific identifiers, created as an additional layer alongside — not replacing — Aadhaar, India's own general-purpose ID.

That is not a design mistake; a country building digital health infrastructure decades after Denmark's civil registry doesn't get to retroactively make Aadhaar do double duty the way CPR already did. But it does mean India's health-ID adoption curve has to be built from a standing start that Denmark and Estonia's already-universal identifiers didn't need, which is one honest reason the doctor- and insurer-side numbers above trail the patient-side one.

## 5. The complication: high coverage numbers don't always mean a unified record

The UK is the case worth reading carefully rather than copying the headline figure. England's Summary Care Record covers 96%+ of the population (55 million-plus people), with fewer than 5% opted out and roughly 80,000 SCR views a week by clinicians in urgent and emergency care — a coverage number that looks as strong as Estonia's. But "Summary" is the operative word: the SCR is a limited extract (medications, allergies, adverse reactions), not the comprehensive record Denmark's or Estonia's systems provide.

The UK's actual unified "Single Patient Record," bringing GP, hospital and specialist data together in one place, is legislated for in the May 2026 Health Bill but isn't due to reach patients via the NHS App until 2028 — eighteen years after the SCR itself first rolled out, and twenty years after Estonia's system went live. A high population-coverage number is necessary but not sufficient; what the record actually contains, and who can act on it, is the harder number to find and the one that actually matters.

## What would fix this

[kept verbatim, open: What would fix this; 3 items]
