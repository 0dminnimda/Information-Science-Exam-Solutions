# min sum of squares

with open(r"ISESolutions\ЕГЭ\27\8_polak_tren\27-8b.txt") as f:
    data = f.read().split("\n")

n = int(data.pop(0))
del data[-1]

nums = [int(i) for i in data]

mn = 10**10

for i in range(n):
    print(i, n)
    x = nums[i]

    r = nums[i+5:]
    if r:
        v = x**2 + min(r)**2
        mn = min(mn, v)

    # r = nums[:max(i-5, 0)]
    # if r:
    #     v = x**2 + min(r)**2
    #     mn = min(mn, v)

print(mn)
