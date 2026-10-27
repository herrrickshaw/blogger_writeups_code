from common import *
S = "the-4-nobody-notices-and-three-other"
t = load(S)
t = rep(t, "the integrated <strong>Krishi Decision Support System</strong> that brings satellite imagery, weather, soil, groundwater and scheme-eligibility data into one platform.</p>",
        "the integrated <strong>Krishi Decision Support System</strong>, a geospatial platform with layers for crops, soil, weather, water resources and drought and flood monitoring. Farmers&rsquo; scheme eligibility sits in a separate part of the mission, the AgriStack Farmers&rsquo; Registry.</p>")
t = insert_note(t, "The Krishi Decision Support System was described as bringing &ldquo;scheme-eligibility data&rdquo; into one platform with satellite, weather, soil and groundwater data. Its layers cover crops, soil, weather, water resources and drought and flood monitoring; scheme eligibility is handled by the AgriStack Farmers&rsquo; Registry, a separate component of the Digital Agriculture Mission. The mission&rsquo;s &#8377;2,817 crore outlay and the One Nation One Ration Card dates were confirmed.")
save(S, t)
