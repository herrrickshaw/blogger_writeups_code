from common import *
S = "the-price-of-grain-msp-msv-and"
t = load(S)
t = rep(t, "(up &#8377;25 from &#8377;2,585, described in press reports as the smallest percentage rise in 17 years)",
        "(up &#8377;25 from &#8377;2,585, about 1%, which some press reports called the smallest percentage rise in 17 years, a claim this blog could not verify)")
t = insert_note(t, "The 9 October note below repeated a press description of the wheat MSP rise for 2027-28 as &ldquo;the smallest percentage rise in 17 years&rdquo;. That could not be verified against the official MSP series, and the note now says so. All MSP levels, the &#8377;1,264 cost of production and the procurement figures were confirmed against PIB.")
save(S, t)
