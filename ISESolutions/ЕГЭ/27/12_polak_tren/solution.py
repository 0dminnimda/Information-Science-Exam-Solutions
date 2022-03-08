"""
     7 5 6 12
0: 0 0 0 1 2
1: 0 1 1 1 1
2: 0 0 0 0 0
3: 0 0 0 0 0
4: 0 0 0 0 0
5: 0 0 1 1 1

     7 5 6 12
0: 0 0 0 2 5
1: 0 0 0 0 0
2: 0 0 0 0 0
3: 0 0 0 0 0
4: 0 0 0 0 0
5: 0 0 1 1 1

"""
with open(r"ISESolutions\ЕГЭ\27\12_polak_tren\27-12b.txt") as f:
    data = f.read().split("\n")

n = int(data.pop(0))
del data[-1]

nums = [int(i) for i in data]

D = 6

count = [0]*D
pairs = [0]*D

for step, x in enumerate(nums):
    for i, c in enumerate(count):
        pairs[(i * x) % D] += c

    count[x % D] += 1
    # print(count, pairs, x)

print(pairs[0])
