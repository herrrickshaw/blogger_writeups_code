"""28 Oct 2026: newer SAMARTH co-firing figures and the November 2025 policy in the ethanol coal-boilers post."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "factcheck-explainers" / "apply"))
from common import load, rep, insert_note, ROOT

S = "ethanols-coal-boilers-briquette-gap-and"
t = load(S)
t = rep(t, "rising to 7% from FY 2025-26 &mdash; administered through the SAMARTH Mission.",
        "rising to 7% from FY 2025-26 &mdash; administered through the SAMARTH Mission. A comprehensive policy issued in November 2025 replaced that path: from FY 2025-26 plants must co-fire 5% biomass pellets, and plants in the National Capital Region 5% pellets plus 2% torrefied charcoal made from municipal solid waste. "
        "By 31 December 2025, 72 thermal plants (11 of them in the NCR) had co-fired about 40.2 lakh tonnes of biomass cumulatively, 24.76 lakh tonnes of it in calendar 2025, according to the Ministry of Power&rsquo;s annual report for 2025-26.")
t = rep(t, "against an estimated 15&ndash;20 million tonnes needed to meet the current mandated co-firing rate across all obligated plants.</p>",
        "against an estimated 15&ndash;20 million tonnes needed to meet the current mandated co-firing rate across all obligated plants. The official co-firing figure for 2025, about 2.5 million tonnes, is consistent with that production estimate.</p>")
t = rep(t, "Ministry of Power SAMARTH biomass co-firing mandate (5&#8211;7% from FY2024-25/25-26)",
        "Ministry of Power co-firing mandate (5%; 5% + 2% MSW charcoal in NCR, Nov 2025 policy)")
t = rep(t, "Revised biomass co-firing policy (5% from FY2024-25, 7% from FY2025-26) per the Ministry of Power's PIB press release, 2 August 2023 (Release ID 1885751), and follow-up PIB coverage of the SAMARTH Mission.",
        "Revised biomass co-firing policy (5% from FY2024-25, 7% from FY2025-26) per the Ministry of Power's PIB press release, 2 August 2023 (Release ID 1885751), and follow-up PIB coverage of the SAMARTH Mission; superseded by the comprehensive co-firing policy of November 2025 (Power Line, 13 November 2025; K&amp;S Partners and Energetica India summaries). Co-firing achieved to 31 December 2025: Ministry of Power Annual Report 2025-26.")
t = insert_note(t, "Updated with the Ministry of Power&rsquo;s annual report for 2025-26 (SAMARTH figures): 72 thermal plants had co-fired about 40.2 lakh tonnes of biomass by 31 December 2025, 24.76 lakh tonnes of it in 2025. "
                   "The 2023 path to a 7% mandate from FY 2025-26 was replaced in November 2025 by a 5% requirement (5% pellets plus 2% municipal-waste charcoal in the NCR); the text and chart note now say so.")
t = t.replace("<b>Updated 27 October 2026.</b> Updated with the Ministry", "<b>Updated 28 October 2026.</b> Co-firing figures updated with the Ministry", 1)
out = ROOT / "out" / f"update-2026-10-28-{S}.html"
out.write_text(t, encoding="utf-8"); print("wrote", out.name, len(t))
