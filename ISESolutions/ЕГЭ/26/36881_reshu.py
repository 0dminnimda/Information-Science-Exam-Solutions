with open(r"ISESolutions\ЕГЭ\26\inf_26_04_21_26.txt") as f:
    data = f.read().split("\n")

del data[-1]
data = [int(i) for i in data]
# data = [6, 3, 8, 14, 11, 22, 17]

s_data = set(data)

new = [[], []]

for item in data:
    new[item % 2].append(item)

sums = []
for i, it1 in enumerate(new[0]):
    for it2 in new[0][i+1:]:
        if it1 + it2 in s_data:
            print(it1, it2)
            sums.append(it1 + it2)

for i, it1 in enumerate(new[1]):
    for it2 in new[1][i+1:]:
        if it1 + it2 in s_data:
            print(it1, it2)
            sums.append(it1 + it2)

print(len(sums), max(sums))
