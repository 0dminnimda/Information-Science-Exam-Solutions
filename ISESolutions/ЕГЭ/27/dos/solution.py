with open(r"ISESolutions\ЕГЭ\27\dos\27-B.txt") as f:
    lines = f.read().split("\n")

del lines[-1]
n = int(lines.pop(0))
nums = [int(i) for i in lines]

s = 0
c = 10000000

for shift in range(len(nums)):
    cost = 0
    for i, num in enumerate(nums):
        i += 1
        dist = abs(i - shift)
        if dist > n // 2:
            dist = shift + n - i
        cost += dist * num
        # print(dist, num, end="; ")

    # print("\n", shift, cost)

    if cost < c:
        c = cost
        s = shift
        print(shift, cost)


print((s-1)%(n+1))

#   0
# 4   1
#  3 2
