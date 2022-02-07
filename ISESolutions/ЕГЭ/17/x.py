with open(r"ISESolutions\ЕГЭ\17\17.txt") as f:
    data = f.read().split("\n")

del data[-1]
data = [int(i) for i in data]

o = []
for a, b in zip(data, data[1:]):
    if (a + b) % 7 == 0:
        o.append(a+b)

print(len(o), max(o))
