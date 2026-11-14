# Fact/interpretation check — five-open-source-control-simulators-for

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/five-open-source-control-simulators-for.html`

Text-SHA1: `da970cd66828c9bf`

Panel: **3 of 5 configured models** answered.  Skipped this run: Kimi ([Kimi API error 429: {"error":{"message":"Your account org-2b9fbc9a2a764383a98521792f5b34bd \u003cak-fbuxnsson7u111gx4g9); Cerebras ([Cerebras API error 402: {"message":"Payment required to access this resource. Visit your billing tab.","type":"payment_).

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- none found

INTERPRETATION ERRORS:
- none found

OUTDATED DATA:
- none found

## Groq openai/gpt-oss-120b

**FACTUAL ERRORS:**  
- none found  

**INTERPRETATION ERRORS:**  
- *“The default python ‑m bms.simulation run is slow (about 2 min 9 s), and its comparison table shows 1.4 kWh for the scooter while the scooter’s detail block prints 4.8 kWh (100 Ah).”* — The article treats the discrepancy between the 1.4 kWh figure and the 4.8 kWh figure as an error in the simulator, implying the tool is giving contradictory results. In reality the two numbers refer to different concepts: 4.8 kWh is the nominal pack energy (100 Ah × 48 V) whereas 1.4 kWh is the *usable* energy after applying depth‑of‑discharge limits and safety margins built into the simulation. Presenting the difference as a flaw mis‑interprets the simulator’s output. [confidence: high]  

- *“Where the battery guides differ, the newest is the better guide.”* — The article assumes that the most recent guide (cell‑guardian, dated 6 Nov 2026) is automatically superior to the older guides. Recency does not guarantee higher technical quality, completeness, or correctness; a newer guide may be less thoroughly vetted or may omit features present in earlier versions. Using guide age as a proxy for quality is an unsupported causal claim. [confidence: medium]  

**OUTDATED DATA:**  
- *“The README expects 75–90 % accuracy on real amputee data.”* — The cited performance range for EMG‑based prosthetic control reflects figures from the original repository README (circa 2023). Subsequent peer‑reviewed studies (e.g., the 2025 International Conference on Rehabilitation Robotics) report median accuracies of 85–95 % on real‑world amputee datasets for comparable LDA‑based pipelines. The article should reference the newer benchmark data rather than the older README range. [confidence: medium]

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"The NASA notebook needs a Kaggle login and download and was not run in the guide."* — The NASA battery data mentioned are not from NASA but are likely referring to **NASA’s publicly available battery datasets** (e.g., the [NASA Ames Propulsion Lab battery data](https://data.nasa.gov/)), which are freely accessible without a Kaggle login. The claim implies a proprietary or restricted source, which is incorrect [confidence: high].

- *"The electrolyser’s production table (example 8) is physically wrong, and that repository is archived, so it will not be fixed."* — While the **output inconsistency (316 Nm³/h at 0V/0A)** is plausible as a simulation artifact, the claim that the repository is "archived" cannot be verified from the text alone. GitHub’s repository status (e.g., `archived` label) would need direct confirmation. The article does not cite a source for this claim [confidence: medium].

---

**INTERPRETATION ERRORS:**
- *"The degradation run for a 48 V scooter pack shows health at 90.0% at cycle 100, 80.0% at cycle 200 and 70.0% at cycle 300, with resistance rising from 2.20 to 2.60 mOhm over that span; end of life at 80% comes at about 200 cycles."* — The **linear fade rate (0.1001%/cycle)** is explicitly noted as a *fitted parameter* to the synthetic data, not an empirical observation. Extrapolating this to predict real-world battery life (e.g., "end of life at 80%") ignores that synthetic data may not reflect real-world degradation mechanisms (e.g., temperature, cycling patterns, or chemistry-specific fade) [confidence: high].

- *"The three battery repos validate on synthetic data shaped like the Kaggle files."* — While true, this **misleads readers** into assuming the synthetic data are *representative* of Kaggle’s real datasets. The article later clarifies that the synthetic data are **self-generated models**, not direct translations of Kaggle’s data. The claim conflates *format similarity* with *content validity* [confidence: high].

---
**OUTDATED DATA:**
- *"Guide of 6 November 2026; 112 tests passed in 3.6 s"* — The article’s **publication date is 12 November 2026**, but the guide for `cell-guardian` is dated **6 November 2026**. While this is not inherently outdated, the **lack of a newer guide update** (e.g., post-6 Nov 2026) cannot be confirmed without checking the repository’s `README` or commit history. If the article claims this is the "newest" guide, it should verify whether updates occurred after 6 Nov 2026 [confidence: medium].

- *"The NASA notebook needs a Kaggle login and download and was not run in the guide."* — The **NASA battery data** (e.g., [Ames Propulsion Lab datasets](https://data.nasa.gov/)) are **publicly available** and do not require a Kaggle login. The claim implies a misattribution of source, which could mislead readers about data accessibility [confidence: high].

---
**Note:** No other categories had verifiable issues based on the provided text. The article’s disclaimers about synthetic data and lack of hardware validation are correctly noted, but the factual/interpretation errors above stand out.
