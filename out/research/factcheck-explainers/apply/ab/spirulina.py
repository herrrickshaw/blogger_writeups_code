import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from abcommon import load, rep, note, save
S = 'green-gold-what-spirulina-actually-is'
t = load(S)
t = rep(t, "<p>The most concrete, dated result so far: under the ISRO&ndash;DBT partnership (with ICGEB, New Delhi), Indian astronaut Group Captain Shubhanshu Shukla studied an Indian isolate of spirulina and a fast-growing <em>Synechococcus</em> strain",
        "<p>The most concrete, dated result so far: in an experiment designed with ICGEB, New Delhi, Indian astronaut Group Captain Shubhanshu Shukla studied a strain of spirulina and a fast-growing <em>Synechococcus</em> strain")
t = rep(t, "comparing growth on nitrate versus urea as nitrogen sources under microgravity.",
        "comparing growth on nitrate versus urea as nitrogen sources under microgravity. Accounts differ on the partnership behind it: some describe an ISRO&ndash;DBT experiment with NASA, others place it within ISRO&rsquo;s collaboration with the European Space Agency.")
t = note(t, "The Axiom-4 spirulina paragraph is qualified. The experiment itself (spirulina and <em>Synechococcus</em>, grown on nitrate and urea, with ICGEB) is confirmed by ISRO and ICGEB, but sources frame the partnership differently, as ISRO&ndash;DBT with NASA or as ISRO with the European Space Agency, and the description of the strain as an &ldquo;Indian isolate&rdquo; could not be confirmed, so it has been removed.")
save(S, t)
