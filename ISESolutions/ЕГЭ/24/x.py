with open(r"ISESolutions\ЕГЭ\24\zadanie24_2.txt") as f:
    data = f.read()

mx = -1
c = 1
for a, b in zip(data, data[1:]):
    if a == b == "R":
        c += 1
    else:
        c = 1
    mx = max(c, mx)

print(mx)
