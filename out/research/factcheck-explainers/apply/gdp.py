from common import *
S = "real-gdp-growth-india-fy2012-13-to"
t = load(S)
t = rep(t, "MoSPI has said a full back series on the new base will follow by December 2026, after which",
        "Reports have said a full back series on the new base will follow by December 2026, though this blog could not confirm that date from MoSPI itself; once it is out,")
t = insert_note(t, "The 22 October note below said MoSPI had committed to a full back series on the new 2022-23 base by December 2026. That date comes from secondary reports and could not be confirmed from MoSPI; the note now says so. The growth figures in that note (7.2% in FY2023-24, 7.1% in FY2024-25, 7.7% in FY2025-26 and 7.8% in Q1 FY2026-27) were confirmed.")
save(S, t)
