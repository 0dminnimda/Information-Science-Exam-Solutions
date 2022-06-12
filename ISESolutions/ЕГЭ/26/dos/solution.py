from collections import defaultdict


with open(r"ISESolutions\ЕГЭ\26\dos\26.txt") as f:
    lines = f.read().split("\n")

del lines[-1]
lines.pop(0)

grid = defaultdict(lambda: defaultdict(int))

for line in lines:
    a, b = map(int, line.split(" "))
    grid[a][b] = 1

p = "1" + "0"*11 + "1"

for n, d in grid.items():
    s = ""
    for i in range(min(d), max(d)+1):
        s += str(d[i])

    ind = s.rfind(p)
    if ind != -1:
        print(n, ind+min(d)+1)
