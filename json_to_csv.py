import json
import csv
import sys

# convert json to csv
# usage: python json_to_csv.py input.json output.csv

if len(sys.argv) < 3:
    print("need input and output files")
    sys.exit(1)

with open(sys.argv[1]) as f:
    data = json.load(f)

if isinstance(data, list) and len(data) > 0:
    keys = data[0].keys()
    with open(sys.argv[2], 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print("done")
