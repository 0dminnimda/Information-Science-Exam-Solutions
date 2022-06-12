from collections import defaultdict

f = open(r"ISESolutions\ЕГЭ\26\25011999\26.txt")
next(f)

d: dict = defaultdict(set)

for i in f:
    a, b = map(int, i.split(" "))
    d[a].add(b)

mx = 7
mxi = -1
for i, values in d.items():
    values = sorted(values)
    c = 1
    for a, b in zip(values, values[1:]):
        if b - a == 1:
            c += 1
        else:
            c = 1
        if c >= 7:
            mxi = i
            print(i)

print(mx, mxi)
