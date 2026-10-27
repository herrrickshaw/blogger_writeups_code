import sys; sys.path.insert(0, __file__.rsplit('/', 1)[0])
from abcommon import load, rep, note, save
S = 'e20-doesnt-cut-tailpipe-co2-by-30-run'
t = load(S)
t = rep(t, "<p>India's E20 petrol mandate is routinely credited with cutting vehicle CO2 emissions by roughly 30%, and lifecycle claims for the programme run as high as 40&ndash;65%.",
        "<p>India's E20 petrol mandate is routinely credited with cutting vehicle CO2 emissions by roughly 30%, and lifecycle claims for the programme run as high as 40&ndash;65%. The government's own written Lok Sabha reply of 30 July 2026 repeats a version of the first claim, putting E20&rsquo;s CO2 cut at about 30% compared with E10; the reports of that reply do not say whether this is per kilometre, at the tailpipe or over the fuel&rsquo;s lifecycle.")
t = rep(t, "states that E20 can reduce fuel efficiency by <strong>2% to 6%</strong>, depending on vehicle category and age.",
        "states that E20 can reduce fuel efficiency by <strong>2% to 6%</strong>, depending on vehicle category and age; that figure comes from a single PTI report of the reply. A reply a week earlier, on 23 July 2026, put the loss at 3&ndash;5% for vehicles built for E10.")
t = rep(t, "<td>2&ndash;6 (Gadkari, Jul 2026); 1&ndash;7 by vehicle category (NITI/ARAI)</td>",
        "<td>2&ndash;6 (Gadkari, 30 Jul 2026); 3&ndash;5 in E10 vehicles (23 Jul 2026 reply); 1&ndash;7 by vehicle category (NITI/ARAI)</td>")
t = note(t, "Two details from Parliament are added. The 30 July 2026 Lok Sabha reply cited here for the 2&ndash;6% efficiency loss also claims that E20 cuts CO2 by about 30% compared with E10, so the 30% figure this piece tests appears in an official answer, not only in press coverage; the reports do not say whether it is a tailpipe, per-kilometre or lifecycle figure, and this piece&rsquo;s chemistry still finds a per-kilometre tailpipe cut of about zero to 5% at E20. A reply on 23 July 2026 put the efficiency loss for vehicles built for E10 at 3&ndash;5%, within the range above; it has been added to the text and the table.")
save(S, t)
