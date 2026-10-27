from common import *
S = "tasmacs-retail-exit-case-for"
t = load(S)
t = rep(t, "per contemporary Tamil Nadu government budget reporting, as covered by",
        "per the Tamil Nadu Prohibition and Excise Department&rsquo;s policy note for 2025-26, which gives them &ldquo;subject to reconciliation&rdquo; (the 2026-27 policy note restates FY2024-25 at &#8377;48,381 crore), as covered by")
t = rep(t, "up from &#8377;45,855.70 crore the year before.</p>",
        "up from &#8377;45,855.70 crore the year before, according to the Excise Department&rsquo;s 2025-26 policy note, which gives the figures subject to reconciliation; its 2026-27 note restates FY2024-25 at &#8377;48,381 crore.</p>")
t = insert_note(t, "The &#8377;48,344 crore figure for FY2024-25 (&#8377;37,323.57 crore VAT plus &#8377;11,020.43 crore excise) and &#8377;45,855.70 crore for FY2023-24 are confirmed, but they come from the Prohibition and Excise Department&rsquo;s policy note for 2025-26, &ldquo;subject to reconciliation&rdquo;, not from budget reporting as the sources note said. The 2026-27 policy note restates FY2024-25 at &#8377;48,381 crore. The comparison table keeps &#8377;48,344 crore; the difference does not change any conclusion.")
save(S, t)
