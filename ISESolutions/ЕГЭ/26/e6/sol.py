with open(r'ISESolutions\ЕГЭ\26\e6\inf_26_04_21_26.txt') as f:
    data_s = f.read().split("\n")

n = int(data_s.pop(0))
del data_s[-1]
data = ([int(i) for i in data_s])
data_set = set(data)

odd = []
even = []

for x in data:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

c = 0
mx = 0
for x in odd:
    for y in even:
        s = x + y
        if s in data_set:
            mx = max(mx, s)
            c += 1

print(c, mx)
