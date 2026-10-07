# Fact/interpretation check — re-spinning-charkha

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/re-spinning-charkha.html`

Text-SHA1: `9e8598a06ebc4483`

Panel: **2 of 2 configured models** answered.

## Gemini gemini-flash-lite-latest

FACTUAL ERRORS:
- "FY2025-26 imports, USD million... China supplies 45% of Ch29 organic-chemical imports and 30% of Ch39 plastics imports... Source: Ministry of Commerce & Industry, TRADESTAT country-wise commodity data, FY2025-26" — The article attributes full fiscal year 2025-26 trade data to the Ministry of Commerce, but as of the author's writing timeframe (August 2026 or earlier), complete official data for the full fiscal year 2025-26 would not yet be finalized and published by official sources like DGCI&S, given typical government data lag. [confidence: medium]

INTERPRETATION ERRORS:
- "As E20 (and a prospective E30) ethanol blending displaces petrol at the pump... refiners are left with petrol-range naphtha and reformate that no longer needs to becomes petrol. That freed volume feeds the same two conversion paths..." — The reasoning assumes a direct, 1:1 chemical and volumetric equivalence where displaced petrol volumes (which are oxygenated fuel blends containing anhydrous ethanol) cleanly convert into surplus refinery streams (naphtha and reformate) of identical quality and quantity suitable for steam crackers without accounting for complex refinery yield optimization, octane balancing, or the fact that ethanol itself is produced largely from food grains/molasses rather than directly freeing up an equivalent stream of petrochemical-grade naphtha within the same refining slate. [confidence: medium]

OUTDATED DATA:
- none found

## Mistral open-mistral-nemo

**FACTUAL ERRORS:**
- *"China supplies 45% of Ch29 organic-chemical imports and 30% of Ch39 plastics imports"* — The article’s own TRADESTAT table shows China’s share for **Ch29 (organic chemicals)** is **11,521.5/25,600 ≈ 45%** (correct), but for **Ch39 (plastics)**, the share is **6,711.5/22,500 ≈ 30%** (also correct). However, the **$20bn deficit claim** conflates Ch29 and Ch39 totals (11,521.5 + 6,711.5 = **$18.2bn**, not $20bn). The article later cites **$20.4bn** (FY2025-26 TRADESTAT running total) but does not reconcile this with the table’s subchapter sums. [confidence: high]

---

**INTERPRETATION ERRORS:**
- *"India's $20bn petrochemical-feedstock deficit... is dominated by one country far more than any other single supplier"* — While China’s **45% share in Ch29** (organic chemicals) is correct, the **Ch39 (plastics) data shows a more diversified supplier base** (e.g., UAE’s 1,195.8M USD share is larger than Russia’s 38.5M USD). The article later notes that **specific monomers (e.g., PTA, PE) have different supplier maps** (e.g., PTA: 60% South Korea, 2.5% China). Claiming China is the "single largest source" of the **entire $20bn deficit** overstates its role in **monomer-specific imports**, which are critical for the ethanol-backed substitution strategy. [confidence: high]

- *"The freed volume [from ethanol blending] feeds the same two conversion paths Reliance built... into olefins (ethylene, propylene → MEG, polypropylene, acrylonitrile)"* — The article assumes **all freed naphtha/reformate** will automatically flow into petrochemicals, but this ignores:
  1. **Export arbitrage**: Freed naphtha/reformate may be **exported** (e.g., to Gulf refiners) rather than used domestically.
  2. **Competing uses**: Naphtha could also feed **petrochemicals for non-fibre uses** (e.g., solvents, adhesives) or **petrol blending** if ethanol mandates ease.
  3. **Infrastructure gaps**: Without dedicated cracker capacity (e.g., in PM MITRA parks), even freed feedstock may not convert efficiently. The claim **overstates causal certainty** between ethanol blending and feedstock substitution. [confidence: high]

---
**OUTDATED DATA:**
- *"FY2025-26 imports, USD million (Ch29 organic chemicals + Ch39 plastics)"* — TRADESTAT’s **FY2025-26 data is preliminary** and subject to revisions. For **real-time figures**, check:
  - **DGCI&S Trade Data Portal** ([https://dgcis.gov.in](https://dgcis.gov.in)) for **FY2026-27** (latest fiscal year).
  - **Niryat.gov.in** (if accessible) for **monthly/quarterly updates** post-FY2026-27.
  The article’s **$20.4bn deficit** (TRADESTAT running total) may differ from the **finalized FY2025-26 figures** (e.g., post-audit adjustments). [confidence: high]

- *"PPAC should publish each year the volume of petrol-range naphtha and reformate freed by ethanol blending"* — No **official PPAC data** on this exists yet. For **real-time tracking**, rely on:
  - **OIL/BPCL/RIL quarterly reports** (e.g., "Ethanol Blending Progress" in their sustainability reports).
  - **CII/PIB press releases** on ethanol mandates (e.g., E20/E30 rollout updates).
  The article’s **10.8 billion litres displaced under E20** (PPAC/CareEdge estimate) lacks a **primary source citation** for FY2025-26. [confidence: high]
