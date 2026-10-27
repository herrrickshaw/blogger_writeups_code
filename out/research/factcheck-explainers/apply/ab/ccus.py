import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from abcommon import load, rep, note, save
S = 'everyone-worries-about-who-pays-for'
t = load(S)
t = rep(t, "The current &#8377;19,700 crore government scheme is roughly 1-2% of that low-end figure &mdash;",
        "The current &#8377;19,700 crore (about $2.2 billion) government scheme is about 2.2% of the $100 billion low end, and about 1.5% of the $150 billion high end &mdash;")
t = rep(t, "Set the current &#8377;19,700 crore scheme against even the low end of that range and it accounts for roughly one to two percent of the total investment NITI Aayog itself says is needed.",
        "Set the current &#8377;19,700 crore scheme, about $2.2 billion, against that range and it accounts for about 1.5% to 2.2% of the total investment NITI Aayog itself says is needed: about 2.2% of the $100 billion low end.")
t = rep(t, "The one-to-two-percent comparison between the current scheme and the total investment need is this piece's own arithmetic, using the low end of NITI Aayog's stated range",
        "The 1.5&ndash;2.2% comparison between the current scheme and the total investment need is this piece's own arithmetic, using both ends of NITI Aayog's stated range")
t = note(t, "An arithmetic slip is corrected. The &#8377;19,700 crore CCUS scheme, about $2.2 billion, is about 2.2% of the $100 billion low end of NITI Aayog&rsquo;s $100&ndash;150 billion investment estimate and about 1.5% of the high end; the piece had called it &ldquo;roughly 1&ndash;2% of that low-end figure&rdquo;. The conclusion, that the scheme is a first instalment rather than the full bill, is unchanged.")
save(S, t)
