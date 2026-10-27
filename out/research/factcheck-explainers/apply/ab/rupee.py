import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from abcommon import load, rep, note, save
S = 'can-rupee-trade-actually-offset'
t = load(S)
t = rep(t, "<span>Indian Oil Corporation's crude purchase from ADNOC (UAE), already settled entirely in rupees rather than dollars</span>",
        "<span>Indian Oil Corporation's purchase of about 1 million barrels of crude from ADNOC (UAE) in August 2023, settled in rupees and dirhams rather than dollars</span>")
t = rep(t, "formally allowing rupee-dirham settlement for bilateral trade, followed by a payment-system interlinking MoU in 2024. It has already produced a genuinely notable transaction: Indian Oil Corporation paying ADNOC for a crude oil cargo entirely in rupees &mdash; not a pilot",
        "formally allowing rupee-dirham settlement for bilateral trade, and on the same day (15 July 2023) an MoU to interlink the two countries&rsquo; payment systems, which led to the UPI&ndash;AANI and RuPay&ndash;JAYWAN links launched in February 2024. It has already produced a genuinely notable transaction: Indian Oil Corporation paying ADNOC in rupees and dirhams for about 1 million barrels of crude in August 2023 &mdash; not a pilot")
t = rep(t, "the IOC-ADNOC rupee-settled crude oil deal, and the 2024 payment-system interlinking MoU</li>",
        "the IOC-ADNOC crude oil deal settled in rupees and dirhams (Indian Embassy, Abu Dhabi, August 2023), and the July 2023 payment-system interlinking MoU (RBI, 15 July 2023) with its February 2024 UPI&ndash;AANI and RuPay&ndash;JAYWAN links</li>")
t = note(t, "Two details of the India&ndash;UAE section were wrong. The payment-system interlinking MoU was signed on 15 July 2023, the same day as the local-currency settlement pact, not in 2024; what came in February 2024 were the UPI&ndash;AANI and RuPay&ndash;JAYWAN links that followed from it. And Indian Oil&rsquo;s August 2023 purchase of about 1 million barrels from ADNOC was paid in rupees and dirhams, according to the Indian Embassy in Abu Dhabi, not &ldquo;entirely in rupees&rdquo;. The text has been corrected.")
save(S, t)
