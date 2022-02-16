with open(r"ISESolutions\ЕГЭ\26\27884.txt") as f:
    raw_data = f.read().split("\n")


free = int(raw_data.pop(0).split(" ")[0])

# del data[-1]
data = sorted([int(i) for i in raw_data])
print(data)

c = 0
s = 0
item = 0
for item in data:
    if s + item > free:
        break

    s += item
    c += 1

s -= item
ans = 0
for i, item in enumerate(data):
    if s + item > free:
        break

print(c, data[i-1])
