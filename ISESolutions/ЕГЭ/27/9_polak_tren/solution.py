# min sum of squares

with open(r"ISESolutions\ЕГЭ\27\9_polak_tren\27-9b.txt") as f:
    data = f.read().split("\n")

n = int(data.pop(0))
del data[-1]

nums = [int(i) for i in data]

mn = 10**10

from time import time

start = time()

for i in range(n):
    if i % 200 == 100:
        print(i, n, time() - start, n / i * (time() - start))

    x = nums[i]

    r = nums[i+6:]
    for m in r:
        v = x * m
        if v % 2 == 1:
            mn = min(mn, v)

if mn == 10**10:
    mn = -1

print(mn, time() - start)
