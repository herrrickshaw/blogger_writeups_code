# Fact/interpretation check — ai-high-demand-launch-tracker

> **Model output, not verified fact.** Every flagged claim needs primary-source
> confirmation (PIB / DGCI&S / MoSPI / DFPD / NCDC, per this blog's usual house rule)
> before it changes anything in the post. Models disagreeing with each other or with
> the post is a prompt to check, not a verdict.

Source: `posts/ai-high-demand-launch-tracker.html`

## Gemini gemini-flash-latest

FACTUAL ERRORS:
- "2.78-trillion-parameter inference on one CPU in 8.24 GB, C99, no framework" — A 2.78-trillion-parameter model cannot physically fit into 8.24 GB of RAM. Even at extreme 1-bit quantization, 2.78 trillion parameters require approximately 347.5 GB of memory, making it mathematically impossible to load or run on 8.24 GB of memory. [confidence: high]

INTERPRETATION ERRORS:
- "ai-trader-bot has 1.4 stars per fork and 962 watchers — more people copying and monitoring than admiring." — A ratio of 1.4 stars per fork means there are 2,452 stars ("admiring") versus 1,778 forks ("copying"). Because there are significantly more stars than forks, there are actually more people admiring the project than copying it; the ratio of 1.4 does not support the conclusion that copying outpaces admiring. [confidence: high]

## Groq llama-3.3-70b-versatile

FACTUAL ERRORS:
- "2.78-trillion-parameter inference on one CPU in 8.24 GB, C99, no framework" — The claim about the specific parameters and memory usage of the kimi-k3-in-c project cannot be verified against publicly available information, and may be subject to change or incorrect [confidence: medium]
- "Gemma 4 26B-A4B inference in ~2 GB on M-series MacBooks" — The claim about the specific model and memory usage of the turbo-fieldfare project cannot be verified against publicly available information, and may be subject to change or incorrect [confidence: medium]

INTERPRETATION ERRORS:
- "Sixty-eight candidates, ranked by stars per day since creation. ... Ranking by total stars returns the same established projects every week. Ranking by stars per day since the repository was created normalises for age, which is what “coming up” actually means" — The article assumes that ranking by stars per day is a better measure of a project's potential or growth, but this may not account for other factors such as the project's maturity, marketing, or community engagement [confidence: medium]
- "A high ratio means bookmarked but not cloned; a low one means cloned more than admired" — The article interprets the star-to-fork ratio as a measure of a project's adoption or usefulness, but this may be an oversimplification, as the ratio can be influenced by various factors such as the project's purpose, target audience, or ease of use [confidence: medium]
