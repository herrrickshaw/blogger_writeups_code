from common import *
S = "indias-labour-codes-took-six-years-to"
t = load(S)
t = rep(t, "<p>The government's original target was to bring all four codes into effect by financial year 2024, i.e. around April 2023. That timeline collapsed: disagreements between the central government and states over jurisdiction, and public pushback over job-loss and worker-rights concerns, left the codes passed but dormant for years.",
        "<p>The government's original target was to bring all four codes into effect from 1 April 2021. That date was deferred because most states had not yet framed their own rules, which they must do because labour is on the Concurrent List, and later dates in 2021 slipped too amid opposition from trade unions over job-security and worker-rights concerns. The codes stayed passed but dormant for years.")
t = rep(t, "The pre-2025 delay history (original FY2024 target, state/centre and worker-rights disagreements) per ISAS and Drishti Judiciary analysis.",
        "The pre-2025 delay history (original 1 April 2021 target, deferred because states had not framed rules, and later 2021 dates that slipped amid union opposition) per ThePrint (2021) and Business Standard (31 March 2021); corrected 27 October 2026 from an earlier version that gave an FY2024 target.")
t = insert_note(t, "This piece said the original target for the codes was financial year 2024 (around April 2023) and that the delay came from centre&ndash;state disagreements over jurisdiction. The original target was 1 April 2021; it was deferred because most states had not framed their rules (labour is on the Concurrent List), and later 2021 dates slipped amid trade-union opposition. The text has been corrected.")
save(S, t)
