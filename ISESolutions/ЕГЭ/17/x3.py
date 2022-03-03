with open(r"ISESolutions\ЕГЭ\17\17 (3).txt") as f:
    data = f.read().split("\n")

data = [int(i) for i in data]

# p = []
# for i, a in enumerate(data):
#     print(i)
#     for b in data[i+1:]:
#         if (a * b) % 26 == 0:
#             p.append(a + b)

# print(len(p), max(p))

o = [0] * 26
# m = [0] * 26
count = 0

for x in data:
    for y, c in enumerate(o):
        if (x * y) % 26 == 0:
            count += c
            # m[y] = max(m[y], x)

    o[x%26] += 1

print(count)
