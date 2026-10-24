"""CBAM Annex I (Reg. (EU) 2023/956) scope, as CN-code prefixes, mapped onto Indian 8-digit ITC-HS codes.
ITC-HS shares the first 6 digits with CN; 8-digit splits differ, so exclusions are applied at 6 digits."""
import csv, sys
SECTORS = [
    ("Cement", ["250700", "2523"], []),
    ("Electricity", ["2716"], []),
    ("Fertilisers", ["280800", "2814", "283421", "3102", "3105"], ["310560"]),
    ("Iron and steel", ["260112", "72", "7301", "7302", "7303", "7304", "7305", "7306", "7307", "7308", "7309", "7310", "7311", "7318", "7326"],
     ["720221", "720229", "720230", "720250", "720270", "720280", "720291", "720292", "720293", "720299", "7204"]),
    ("Aluminium", ["7601", "7603", "7604", "7605", "7606", "7607", "7608", "7609", "7610", "7611", "7612", "7613", "7614", "7616"], []),
    ("Hydrogen", ["280410"], []),
]
def sector(code):
    for name, inc, exc in SECTORS:
        if any(code.startswith(p) for p in inc) and not any(code.startswith(p) for p in exc):
            return name
    return None
if __name__ == "__main__":
    rows = list(csv.DictReader(open(sys.argv[1])))
    print(len(rows))
