with open(r"ISESolutions\ЕГЭ\26\27880.txt") as f:
    data = f.read().split("\n")

size, n = [int(i) for i in data.pop(0).split(" ")]

data = [int(i) for i in data]

out = []
for x in sorted(data):
    if x + sum(out) < size:
        out.append(x)
    else:
        break

print(len(out))
del out[-1]

mx = -10000
for x in data:
    if x + sum(out) < size:
        mx = max(mx, x)

print(mx)
print(out)
print(sorted(data))
