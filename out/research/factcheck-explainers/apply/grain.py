from common import *
S = "the-grain-value-loop-integrated-rice"
t = load(S)
t = rep(t, "of maize (+7,940%) — feed takes 60–70% of the ~356 LMT crop", "of maize (+7,940%) — feed takes about 60% of the ~356 LMT crop")
t = rep(t, "Drishti/DownToEarth (net importer, feed 60–70%)", "Drishti/DownToEarth (net importer; feed about 60%, DownToEarth alone gives 60–70%)")
t = insert_note(t, "Feed&rsquo;s share of India&rsquo;s maize crop was given as 60&ndash;70%. The upper end rests on a single source (DownToEarth); the slide now says &ldquo;about 60%&rdquo;. India becoming a net maize importer in 2024 is confirmed.")
save(S, t)
