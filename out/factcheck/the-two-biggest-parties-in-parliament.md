# Fact/interpretation check — the-two-biggest-parties-in-parliament

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/the-two-biggest-parties-in-parliament.html`

Text-SHA1: `79e44a57d658d7ae`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "BJP holds roughly 240 of 543 Lok Sabha seats" — The 18th Lok Sabha election results held in mid-2024 resulted in the BJP winning 240 seats precisely (not "roughly 240"), and total Lok Sabha strength is 543, but stating "roughly 240" is imprecise rather than strictly wrong; however, the table lists BJP with 11,755 Lok Sabha questions and the membership table later cites 783 sitting members total (540 Lok Sabha, 243 Rajya Sabha), which contradicts the constitutional maximum and fixed size of 543 Lok Sabha seats. [confidence: medium]

INTERPRETATION ERRORS:
- "Divide each party's share of questions on a given ministry by that party's overall share of all questions, and you get lift : a value of 1.0 means the party asks about that ministry exactly as often as its overall size would predict; a value of 3.0 means three times more than predicted. Lift strips out size and isolates focus." — The reasoning assumes that all parties allocate their questions uniformly across all ministries absent specific focus, so overall party size dictates expected questions per ministry linearly. In reality, large umbrella parties naturally cover diverse portfolios because they contest national elections across all sectors, whereas smaller parties have fewer MPs who naturally cluster on specific portfolios due to regional or sectoral concentration; dividing by overall share measures specialization relative to the party's own average, but describing it as what "size would predict" confuses portfolio scope requirements with mere headcount proportionality. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"59,381 Combined Lok Sabha + Rajya Sabha questions in this dataset"* — The article later clarifies the actual counts are **34,720 (Lok Sabha)** and **24,661 (Rajya Sabha)**, totaling **59,381 only if including excluded/unmatched questions (138 Lok Sabha questions were excluded due to name reconciliation failures)**. The initial claim conflates raw data with the final filtered dataset. [confidence: high]

**INTERPRETATION ERRORS:**
- *"BJP's single highest-lift ministry is Parliamentary Affairs (1.9×, 49 questions); INC's is Road Transport & Highways (1.4×, 347 questions). Both are modest deviations from perfectly proportional, not specialisations."*
  **Gap:** The claim assumes that a lift of **1.9× or 1.4×** inherently disqualifies a party from being a "specialist," but the article’s own methodology defines specialisation as **any lift >1.0×** (with thresholds like ≥100 total questions and ≥10 questions on the ministry). The BJP’s 1.9× lift on Parliamentary Affairs is statistically significant given its scale (22,881 total questions), but the article later dismisses it as "modest" without adjusting for baseline question volume or comparing it to smaller parties’ lifts (e.g., BAP’s 7.6×). [confidence: high]

**OUTDATED DATA:**
- *"every sitting member of the 18th Lok Sabha and the current Rajya Sabha, mapped to party"* — The article notes the member rosters were pulled at a **snapshot time (not the exact same moment as the question data)**, leading to discrepancies (e.g., 5 smaller parties have sitting members here but no logged questions, while MNF/TMC(M) show no current members despite prior questions). For **real-time accuracy**, re-check:
  - **Lok Sabha member rosters**: [sansad.in](https://sansad.in/members) (current 18th LS composition as of **October 2026**).
  - **Rajya Sabha member rosters**: [rsdoc.nic.in](https://rsdoc.nic.in/members) (current Rajya Sabha composition as of **October 2026**, accounting for by-elections/departures).
  [confidence: high]
