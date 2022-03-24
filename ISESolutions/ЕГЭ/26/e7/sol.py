from collections import defaultdict

with open(r'ISESolutions\ЕГЭ\26\e7\26.txt') as f:
    data_s = f.read().split("\n")

n = int(data_s.pop(0))
data = ([list(map(int, i.split(" "))) for i in data_s])

rows = defaultdict(list)

for row, place in data:
    rows[row].append(place)

mn = 100000
pairs = defaultdict(list)
for row, column in rows.items():
    column.sort()
    for a, b in zip(column, column[1:]):
        if b - a == 3:
            pairs[row].append((a, b))

for row, pirs in sorted(pairs.items())[::-1]:
    pirs.sort()
    print(row, pirs, pirs[0][0] + 1)
    break
    # for pir in pirs:
