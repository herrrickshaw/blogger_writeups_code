import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from abcommon import load, rep, note, save
S = 'a-17-rural-pay-rise-that-nobody-received'
t = load(S)
# swapped June 2025 inflation figures
t = rep(t, "with year-on-year inflation of <strong>1.42 per cent and 1.73 per cent</strong> respectively.",
        "with year-on-year inflation of <strong>1.73 per cent and 1.42 per cent</strong> respectively.")
t = rep(t, "Consider what 1.42 per cent means as an input to a wage formula. Whatever agricultural labourers were experiencing in mid-2025, a 1.42 per cent annual rise",
        "Consider what 1.73 per cent means as an input to a wage formula. Whatever agricultural labourers were experiencing in mid-2025, a 1.73 per cent annual rise")
t = rep(t, "how much of the 1.42 per cent June 2025 inflation print comes from the averaging change alone.",
        "how much of the 1.73 per cent June 2025 CPI-AL inflation print comes from the averaging change alone.")
t = rep(t, "with year-on-year inflation of 1.42 per cent (CPI-AL) and 1.73 per cent (CPI-RL) are from",
        "with year-on-year inflation of 1.73 per cent (CPI-AL) and 1.42 per cent (CPI-RL), as given by MoSPI&rsquo;s data service, are from")
# Rs 370 is not a national average
t = rep(t, "<p>Two figures on that table do not reconcile with the ones the government published a year earlier, and are worth flagging rather than smoothing. In March 2025 the Ministry of Rural Development notified an MGNREGA national average of <strong>&#8377;370 a day</strong>, up from &#8377;349, with Haryana at &#8377;400 and Nagaland and Arunachal Pradesh at &#8377;241. The VB-G RAM G announcement describes the outgoing MGNREGA average as &#8377;298.8. Both are official. The most likely explanation is that one is a simple average across states and the other is weighted &mdash; but no published note says which, so the &ldquo;10 per cent rise&rdquo; should not be compared against the &#8377;370 figure.</p>",
        "<p>The &#8377;298.8 average for the outgoing MGNREGA wage is consistent with the state rates the Ministry of Rural Development notified in March 2025 for 2025-26, which ran from &#8377;241 in Nagaland and Arunachal Pradesh to &#8377;400 in Haryana. Only Haryana (&#8377;400), Goa (&#8377;378) and Karnataka (&#8377;370) paid &#8377;370 or more, and the simple average across 17 major states was about &#8377;307. An earlier version of this piece described &#8377;370 as a national average and treated it as a second official figure that could not be reconciled with &#8377;298.8; it was not a national average.</p>")
t = rep(t, "and say whether its national average is simple or weighted, so the ₹370 and ₹298.8 figures can be reconciled.</li>",
        "and say whether its national average is simple or weighted, so figures such as ₹298.8 and ₹327.4 can be reproduced from the state rates.</li>")
t = rep(t, "<p>The two national average wage figures for MGNREGA, &#8377;370 and &#8377;298.8, are both government numbers and this piece could not determine the weighting behind either.",
        "<p>Whether the government&rsquo;s &#8377;298.8 national average is a simple or a weighted average of state rates is not published.")
t = rep(t, "The March 2025 MGNREGA notification of a &#8377;370 average, up from &#8377;349, with Haryana at &#8377;400 and Nagaland and Arunachal Pradesh at &#8377;241, is per the Ministry of Rural Development.",
        "The March 2025 MGNREGA state wage rates for 2025-26 (Haryana &#8377;400, Goa &#8377;378, Karnataka &#8377;370, Nagaland and Arunachal Pradesh &#8377;241) are per the Ministry of Rural Development notification as reported; the 17-state simple average of about &#8377;307 is this blog&rsquo;s arithmetic.")
t = note(t, "Two corrections. First, the March 2025 MGNREGA notification did not set &ldquo;a national average of &#8377;370 a day&rdquo;: in 2025-26 only Haryana (&#8377;400), Goa (&#8377;378) and Karnataka (&#8377;370) paid that much or more, and the simple average across 17 major states was about &#8377;307. So the government&rsquo;s &#8377;298.8 average is consistent with the state rates, and there is no second official figure to reconcile; the paragraph, proposal and caveat that treated &#8377;370 as one have been rewritten. Second, the June 2025 inflation figures were the wrong way round: year-on-year inflation was 1.73% for agricultural labourers (CPI-AL) and 1.42% for rural labourers (CPI-RL). The argument is unchanged, since either figure justifies almost no wage revision. The follow-up piece, <a href=\"https://masaladeutsch.blogspot.com/2026/10/rural-job-guarantee-pay-rose-96-in-july.html\">Rural Job-Guarantee Pay Rose 9.6% in July</a>, sets out the state rates.")
save(S, t)
