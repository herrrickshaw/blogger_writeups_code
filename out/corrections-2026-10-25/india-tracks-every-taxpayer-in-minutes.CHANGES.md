# CHANGES: india-tracks-every-taxpayer-in-minutes (findings 10)

## Changes applied
1. **Cognizant India workforce share, "more than 85%" -> "about 73%"** (one CORRECTION NEEDED item). Re-checked in raw/10/ctsh.htm (Cognizant Form 10-K FY2025, SEC EDGAR, filed 12 Feb 2026, https://www.sec.gov/Archives/edgar/data/1058290/000105829026000008/ctsh-20251231.htm, "Our People and Culture"): "approximately 351,600 employees, with 256,900 in India" = 73.07%. Occurrences fixed (all four):
   - Stat card (intro): "from a workforce more than 85% in India" -> "from a workforce about 73% in India".
   - Body, health-export section: "more than 85% of its staff in India" -> "about 73% of its staff in India (256,900 of 351,600 at the end of 2025)".
   - Chart bar label (SVG text): "Cognizant (CY2025, 85%+ staff in India)" -> "Cognizant (CY2025, 73% staff in India)".
   - Chart aria-label: same wording change.
   Revenue figures (US$6.35bn, 30.1% bar, 30%) CONFIRMED against the same 10-K (Health Sciences $6,347m of $21,108m); unchanged.
2. **Trust paragraph and sources note**: "government websites could not be opened, so official figures are as relayed" softened to "several ... some official figures are as relayed; the ABDM backgrounder, the Cabinet approval, the PAN 2.0 explainer and Cognizant's 10-K were read directly" (and "several" in the sources note). Why: those documents have now been read.
3. **Sources note, citations added** (links): PIB backgrounder 6 Jul 2026 (PRID 2281466; confirms 23.21 crore ABHA-linked tokens as on 18 Jun 2026, replacing "via summaries"); PIB Cabinet release 26 Feb 2022 (PRID 1801322; Rs 1,600 crore for five years); PIB PAN 2.0 explainer (Rs 1,435 crore, PAN from 1972); Cognizant 10-K as basis for the 73% share. ABHA clause now says the 17 Sep 2026 PIB release itself was not located and gives the bracketing figures (PIB factsheet 12 Aug 2026: 96.43 crore, https://www.pib.gov.in/FactsheetDetails.aspx?id=150834&ModuleId=16&reg=48&lang=1; ABDM dashboard 25 Oct 2026: 98.66 crore, https://dashboard.abdm.gov.in/abdm/).
4. **Visible correction note** (class warn, as a <p> with the post's existing warn styling) inserted directly before the "Sources and caveats" h2. No dateModified element in the post.

## Title / headline
No title change needed (H1 and title do not carry the corrected figure).

## Not applied / author decisions
- **"1.3 lakh of 5.47 lakh facilities actually connected" (~17,000 private)**: STILL UNAVAILABLE as primary; findings found no official 1.3 lakh figure and a July 2026 search snippet reports 2.72 lakh facilities using ABDM-enabled software (would contradict). NOT changed. Author should either find the Digital Health News/ministry source or soften/remove the claim. (Note 5.47 lakh registered facilities is confirmed for 12 Aug; the dashboard now shows 5.91 lakh.)
- **ABHA "about 97.6 crore, 17 September 2026"**: consistent (between 96.43 crore on 12 Aug and 98.66 crore on 25 Oct) but the exact 17 Sep PIB release was not located; not changed. The existing "Updated 22 October" box is left as is. Author may prefer to update to the live 98.66 crore (25 Oct) - that would ripple into the ABHA row of the "Two systems, October 2026" table and any per-capita ratios.
- **80.08 crore PANs / 83% Aadhaar-linked**: no primary found (incometaxindia.gov.in 403); ~80 crore at Mar 2025 plausible from 74.67 crore at Mar 2024 (snippets). Left as is.
- **TCS 10.4% / ~US$3.1bn**: snippet only; TCS fact sheet 403. Left. HCLTech 14.5%, Wipro 14.4%, Infosys 8.0%, Tech Mahindra 7.4% not checked. CPC/GSTN/NHCX timeline items not verified.
- **Two single-source figures** (capability-centre staff; "only a third of mission money spent"): still unavailable; already flagged in the post.
- CONFIRMED, no change: 7.8 crore ITRs for AY 2026-27 (PTI via Telangana Today, 1 Sep 2026); Rs 1,600 crore ABDM outlay; PAN 2.0 Rs 1,435 crore; 23 crore tokens; incentives.

## Ripples checked
- The 85% figure appeared only in the four places above; no derived percentages, JS arrays or tables depend on it. Chart bar widths are driven by revenue share (30.1%), not workforce share, so geometry is unchanged. The script blocks are the accessibility and Google Translate snippets; untouched.

## Verification
    ## diff stat
    13
     india-tracks-every-taxpayer-in-minutes.html |   13 +++++++------
     1 file changed, 7 insertions(+), 6 deletions(-)
    <div orig=      20 new=      20
    </div orig=      20 new=      20
    <table orig=       4 new=       4
    </table orig=       4 new=       4
    <script orig=       4 new=       4
    </script orig=       4 new=       4
    scripts parsed: 2, failures: 0
