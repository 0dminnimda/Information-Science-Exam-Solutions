with open(r'ISESolutions\ЕГЭ\26\e2\28138.txt') as f:
    data_s = f.read().split("\n")

size, n = map(int, data_s.pop(0).split(" "))
data = sorted([int(i) for i in data_s])

disk = []

for v in data:
    if sum(disk) + v <= size:
        disk.append(v)

disk.pop(-1)

data = list(set(data))
for prev, cur in zip(data, data[1:]):
    if sum(disk) + cur > size:
        disk.append(prev)
        break

print(len(disk), disk)
print(sum(disk), size)
print(data)
