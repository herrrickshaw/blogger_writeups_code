"""Season-wise APY (UPAG all-India) and mandi arrival calendars (Agmarknet state-monthly), from
herrrickshaw/india-mandi-arrivals. Rabi includes summer for comparability (UPAG reports summer
separately only from 2022-23)."""
import csv, gzip, collections, statistics
REPO = '/tmp/claude-0/-home-user--github/bf61733e-4e03-51c3-9ac3-07a35af41a6a/scratchpad/india-mandi-arrivals'
_r = list(csv.DictReader(gzip.open(f'{REPO}/data/upag/apy_all_india.csv.gz', 'rt')))
APY = collections.defaultdict(float)     # (crop, season, year, metric) -> value; season in Kharif/Rabi+/Summer/Total
for x in _r:
    try:
        v = float(x['Value'])
    except ValueError:
        continue
    if x['Metric'] not in ('Area', 'Production'):
        continue
    s = x['Season']
    if s in ('Rabi', 'Summer'):
        APY[(x['Crop'], 'Rabi+', x['Crop Year'], x['Metric'])] += v
    if s in ('Kharif', 'Summer', 'Total'):
        APY[(x['Crop'], s, x['Crop Year'], x['Metric'])] = v
CYCLE = {x['Crop Year']: x['Estimation Cycle'] for x in _r}
YEARS = sorted({x['Crop Year'] for x in _r})


def yr(y):
    return f"{y}-{str(y + 1)[2:]}"


def avg3(crop, season, metric, end):
    ys = [yr(end - 2), yr(end - 1), yr(end)]
    return sum(APY.get((crop, season, y, metric), 0) for y in ys) / 3


def change(crop, season, a_end=2005, b_end=2025):
    a0, p0 = avg3(crop, season, 'Area', a_end), avg3(crop, season, 'Production', a_end)
    a1, p1 = avg3(crop, season, 'Area', b_end), avg3(crop, season, 'Production', b_end)
    if not (a0 and a1 and p0 and p1):
        return None
    y0, y1 = p0 / a0, p1 / a1
    return dict(a0=a0, a1=a1, p0=p0, p1=p1, y0=y0 * 1000, y1=y1 * 1000,
                da=a1 / a0 - 1, dy=y1 / y0 - 1, dp=p1 / p0 - 1)


# ---------------------------------------------------------------- arrivals
_m = list(csv.DictReader(gzip.open(f'{REPO}/data/agmarknet/state_monthly.csv.gz', 'rt')))
ARR = collections.defaultdict(float)     # (commodity, 'YYYY-MM') -> tonnes, all states
for x in _m:
    try:
        ARR[(x['commodity'], x['month'])] += float(x['arrivals_t'] or 0)
    except ValueError:
        pass
