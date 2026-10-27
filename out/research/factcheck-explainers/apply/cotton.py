from common import *
S = "indias-cotton-yield-fell-from-566-kg-to"
t = load(S)
t = rep(t, "against a global average above 800 and against China at around 1,993 kg/ha and Brazil at 1,800 to 2,000.",
        "against a global average above 800 (USDA puts it at about 814&ndash;854), China at a record of about 2,384 kg/ha on USDA&rsquo;s estimate (2,171.6 on China&rsquo;s official figure) and Brazil at 1,800 to 2,000. USDA&rsquo;s own estimate for India in 2024-25 is a little higher than the official one, at about 461 kg/ha.")
t = rep(t, "<tr><td>China</td><td>~1,993</td></tr>",
        "<tr><td>China, 2024-25 (USDA; official 2,171.6)</td><td>~2,384</td></tr>")
t = insert_note(t, "China&rsquo;s 2024-25 cotton yield was given as about 1,993 kg/ha. USDA puts it at a record of about 2,384 kg/ha, and China&rsquo;s official figure is 2,171.6 kg/ha; the text and table now say so. India&rsquo;s 2024-25 range (about 436&ndash;450 kg/ha, 437 provisional) is confirmed on official data; USDA&rsquo;s estimate is about 461.")
save(S, t)
