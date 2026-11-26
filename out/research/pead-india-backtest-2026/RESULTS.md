# India price-only drift backtest, results

Panel: {'start': '2016-01-01', 'end': '2025-12-31', 'symbols': 3273, 'days': 2468, 'glitch_moves_dropped': 477}
Events: {'total': 25647, 'in_season_share': 0.4603657347837954, 'null_season_share': 0.3972602739726027}

## Signed 60-day drift (percent, continuation = positive), by period and size

| subset | period | size | n | mean60 | t (date-clustered) | median60 | share positive | mean20 | t20 | gap60 Q5-Q1 | monotonicity | slope | slope t |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| all events | 2016-18 | small | 1897 | 1.71 | 3.25 | -0.35 | 49.1 | 0.47 | 1.66 | 3.79 | 0.90 | 0.174 | 2.92 |
| all events | 2016-18 | mid | 1779 | -0.31 | -0.62 | -1.61 | 46.0 | -0.34 | -1.19 | 2.33 | 0.30 | 0.256 | 1.93 |
| all events | 2016-18 | large | 1615 | 0.02 | 0.04 | 0.06 | 50.1 | -0.20 | -0.75 | -0.70 | -0.30 | 0.014 | 0.20 |
| all events | 2016-18 | all | 5291 | 0.51 | 1.67 | -0.69 | 48.4 | -0.01 | -0.04 | 1.78 | 0.30 | 0.155 | 2.87 |
| all events | 2019-21 | small | 2444 | 1.17 | 2.35 | -0.97 | 48.0 | 0.01 | 0.03 | 3.86 | 0.90 | 0.184 | 2.71 |
| all events | 2019-21 | mid | 2200 | -0.50 | -1.02 | -2.24 | 45.7 | -0.62 | -2.30 | -1.76 | -1.00 | -0.018 | -0.23 |
| all events | 2019-21 | large | 1972 | -0.61 | -1.27 | -1.86 | 45.6 | -0.51 | -1.77 | -1.11 | -0.10 | -0.009 | -0.12 |
| all events | 2019-21 | all | 6616 | 0.08 | 0.27 | -1.58 | 46.5 | -0.35 | -2.08 | 1.31 | 0.30 | 0.075 | 1.70 |
| all events | 2022-25 | small | 4818 | -0.57 | -2.00 | -2.11 | 44.8 | -0.28 | -1.56 | -2.81 | -0.90 | -0.136 | -3.91 |
| all events | 2022-25 | mid | 4690 | 0.41 | 1.45 | -1.37 | 47.2 | -0.02 | -0.13 | 2.46 | 0.90 | 0.088 | 2.18 |
| all events | 2022-25 | large | 4232 | -0.03 | -0.12 | -0.65 | 48.3 | 0.04 | 0.22 | -0.35 | 0.00 | -0.008 | -0.21 |
| all events | 2022-25 | all | 13740 | -0.07 | -0.41 | -1.40 | 46.7 | -0.09 | -0.90 | -0.47 | 0.00 | -0.023 | -1.04 |
| all events | all | small | 9159 | 0.36 | 1.58 | -1.49 | 46.5 | -0.05 | -0.34 | 0.41 | 0.70 | 0.026 | 0.89 |
| all events | all | mid | 8669 | 0.03 | 0.15 | -1.61 | 46.6 | -0.24 | -1.88 | 1.20 | 0.80 | 0.092 | 2.22 |
| all events | all | large | 7819 | -0.17 | -0.79 | -0.84 | 48.0 | -0.15 | -1.18 | -0.77 | 0.00 | -0.006 | -0.18 |
| all events | all | all | 25647 | 0.09 | 0.65 | -1.31 | 47.0 | -0.14 | -1.81 | 0.46 | 0.40 | 0.044 | 2.10 |
| results-season events | 2016-18 | small | 760 | 2.25 | 3.24 | 0.47 | 51.6 | 0.80 | 1.92 | 6.32 | 0.90 | 0.236 | 3.54 |
| results-season events | 2016-18 | mid | 691 | 0.83 | 1.07 | -1.05 | 47.9 | -0.08 | -0.19 | 4.04 | 0.90 | 0.389 | 1.98 |
| results-season events | 2016-18 | large | 858 | 0.13 | 0.22 | 0.29 | 50.9 | 0.09 | 0.27 | -0.93 | -0.30 | -0.005 | -0.05 |
| results-season events | 2016-18 | all | 2309 | 1.04 | 2.34 | 0.06 | 50.2 | 0.27 | 1.17 | 2.88 | 0.70 | 0.196 | 2.41 |
| results-season events | 2019-21 | small | 1117 | 2.71 | 3.61 | 0.38 | 50.6 | 0.45 | 1.05 | 9.26 | 1.00 | 0.417 | 3.63 |
| results-season events | 2019-21 | mid | 981 | 0.39 | 0.56 | -0.45 | 49.2 | -0.64 | -1.57 | -0.13 | 0.10 | 0.114 | 0.89 |
| results-season events | 2019-21 | large | 1019 | 0.57 | 0.80 | -0.50 | 48.5 | 0.09 | 0.26 | 3.52 | 0.30 | 0.138 | 1.28 |
| results-season events | 2019-21 | all | 3117 | 1.28 | 2.79 | -0.26 | 49.5 | -0.01 | -0.04 | 5.05 | 0.90 | 0.242 | 3.43 |
| results-season events | 2022-25 | small | 2084 | 0.08 | 0.19 | -0.88 | 47.8 | 0.20 | 0.69 | -1.39 | -0.60 | -0.068 | -1.35 |
| results-season events | 2022-25 | mid | 2168 | 0.76 | 1.84 | -0.56 | 49.0 | 0.34 | 1.44 | 3.35 | 0.80 | 0.126 | 2.59 |
| results-season events | 2022-25 | large | 2129 | 0.02 | 0.06 | -0.02 | 49.9 | 0.29 | 1.28 | 0.22 | 0.60 | 0.004 | 0.08 |
| results-season events | 2022-25 | all | 6381 | 0.29 | 1.20 | -0.44 | 48.9 | 0.28 | 1.81 | 1.17 | 0.90 | 0.024 | 0.81 |
| results-season events | all | small | 3961 | 1.24 | 3.65 | -0.28 | 49.3 | 0.39 | 1.84 | 3.30 | 0.90 | 0.122 | 2.82 |
| results-season events | all | mid | 3840 | 0.68 | 2.08 | -0.71 | 48.9 | 0.02 | 0.08 | 2.92 | 0.90 | 0.171 | 3.03 |
| results-season events | all | large | 4006 | 0.18 | 0.64 | -0.09 | 49.8 | 0.20 | 1.18 | 0.55 | 0.40 | 0.034 | 0.73 |
| results-season events | all | all | 11807 | 0.70 | 3.51 | -0.30 | 49.3 | 0.20 | 1.76 | 2.54 | 0.90 | 0.117 | 3.93 |

## Continuation slope (d60 on first move) by year

| subset | year | size | n | slope | slope t | mean60 | t60 |
|---|---|---|---|---|---|---|---|
| all events | 2016 | small | 286 | 0.111 | 0.95 | 1.83 | 1.52 |
| all events | 2016 | large | 203 | 0.052 | 0.45 | -0.11 | -0.13 |
| all events | 2016 | all | 751 | 0.045 | 0.68 | -0.15 | -0.23 |
| all events | 2017 | small | 937 | 0.290 | 2.68 | 3.29 | 3.96 |
| all events | 2017 | large | 748 | -0.043 | -0.39 | -1.39 | -2.14 |
| all events | 2017 | all | 2526 | 0.165 | 2.22 | 0.88 | 1.84 |
| all events | 2018 | small | 674 | 0.052 | 0.63 | -0.53 | -0.74 |
| all events | 2018 | large | 664 | 0.119 | 1.13 | 1.63 | 2.50 |
| all events | 2018 | all | 2014 | 0.185 | 1.87 | 0.31 | 0.64 |
| all events | 2019 | small | 579 | 0.215 | 1.29 | -1.12 | -1.07 |
| all events | 2019 | large | 511 | -0.149 | -0.87 | -0.34 | -0.37 |
| all events | 2019 | all | 1616 | 0.012 | 0.12 | -0.80 | -1.32 |
| all events | 2020 | small | 826 | 0.028 | 0.28 | 1.00 | 1.18 |
| all events | 2020 | large | 595 | -0.014 | -0.10 | -0.17 | -0.18 |
| all events | 2020 | all | 2112 | 0.015 | 0.17 | 0.13 | 0.22 |
| all events | 2021 | small | 1039 | 0.190 | 2.33 | 2.57 | 3.51 |
| all events | 2021 | large | 866 | 0.216 | 2.37 | -1.07 | -1.59 |
| all events | 2021 | all | 2888 | 0.167 | 3.63 | 0.54 | 1.25 |
| all events | 2022 | small | 1081 | -0.094 | -1.11 | 0.14 | 0.22 |
| all events | 2022 | large | 928 | -0.146 | -2.06 | -0.70 | -1.20 |
| all events | 2022 | all | 3111 | 0.016 | 0.34 | 0.36 | 1.05 |
| all events | 2023 | small | 1327 | -0.128 | -1.95 | -0.09 | -0.16 |
| all events | 2023 | large | 1172 | 0.229 | 2.47 | 1.11 | 2.03 |
| all events | 2023 | all | 3732 | 0.080 | 1.81 | 0.65 | 1.84 |
| all events | 2024 | small | 1398 | -0.118 | -1.78 | -0.58 | -1.05 |
| all events | 2024 | large | 1212 | -0.014 | -0.18 | -0.37 | -0.68 |
| all events | 2024 | all | 3968 | -0.023 | -0.52 | -0.30 | -0.90 |
| all events | 2025 | small | 1012 | -0.247 | -4.16 | -1.96 | -3.82 |
| all events | 2025 | large | 920 | -0.127 | -1.89 | -0.38 | -0.70 |
| all events | 2025 | all | 2929 | -0.189 | -4.59 | -1.14 | -3.31 |
| results-season events | 2016 | all | 279 | 0.037 | 0.46 | 0.56 | 0.56 |
| results-season events | 2017 | small | 353 | 0.353 | 3.18 | 3.77 | 3.74 |
| results-season events | 2017 | large | 389 | -0.145 | -1.04 | -1.33 | -1.55 |
| results-season events | 2017 | all | 1076 | 0.151 | 1.48 | 1.11 | 1.65 |
| results-season events | 2018 | small | 309 | 0.157 | 1.60 | 0.32 | 0.29 |
| results-season events | 2018 | large | 375 | 0.232 | 1.55 | 1.99 | 2.35 |
| results-season events | 2018 | all | 954 | 0.296 | 2.03 | 1.10 | 1.56 |
| results-season events | 2019 | small | 273 | 0.515 | 1.86 | 1.49 | 0.87 |
| results-season events | 2019 | large | 285 | 0.148 | 0.65 | 1.19 | 0.88 |
| results-season events | 2019 | all | 795 | 0.287 | 1.92 | 1.40 | 1.47 |
| results-season events | 2020 | small | 375 | 0.366 | 2.43 | 2.58 | 2.22 |
| results-season events | 2020 | large | 290 | -0.024 | -0.11 | 0.89 | 0.61 |
| results-season events | 2020 | all | 972 | 0.241 | 1.47 | 1.36 | 1.42 |
| results-season events | 2021 | small | 469 | 0.287 | 2.32 | 3.53 | 3.09 |
| results-season events | 2021 | large | 444 | 0.269 | 2.32 | -0.03 | -0.03 |
| results-season events | 2021 | all | 1350 | 0.227 | 3.94 | 1.16 | 2.00 |
| results-season events | 2022 | small | 439 | -0.076 | -0.58 | 1.16 | 1.12 |
| results-season events | 2022 | large | 473 | -0.095 | -1.05 | 0.31 | 0.45 |
| results-season events | 2022 | all | 1369 | 0.045 | 0.69 | 1.27 | 2.62 |
| results-season events | 2023 | small | 598 | -0.073 | -0.79 | 0.97 | 1.20 |
| results-season events | 2023 | large | 576 | 0.120 | 1.00 | 0.48 | 0.67 |
| results-season events | 2023 | all | 1765 | 0.121 | 2.07 | 1.12 | 2.28 |
| results-season events | 2024 | small | 593 | -0.079 | -0.77 | -0.56 | -0.68 |
| results-season events | 2024 | large | 609 | 0.054 | 0.52 | -0.03 | -0.04 |
| results-season events | 2024 | all | 1803 | 0.012 | 0.20 | -0.14 | -0.31 |
| results-season events | 2025 | small | 454 | -0.078 | -1.05 | -1.28 | -2.03 |
| results-season events | 2025 | large | 471 | -0.112 | -1.33 | -0.77 | -1.18 |
| results-season events | 2025 | all | 1444 | -0.088 | -1.80 | -1.11 | -2.55 |
