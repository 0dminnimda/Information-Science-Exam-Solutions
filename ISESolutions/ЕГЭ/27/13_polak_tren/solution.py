with open(r"ISESolutions\ЕГЭ\27\13_polak_tren\27-13b.txt") as f:
    data = f.read().split("\n")

n = int(data.pop(0))
del data[-1]

nums = [int(i) for i in data]

D = 14

pairs = [0]*D
count = [0]*D

# a_i, a_j
# 1 <= i + 7 <= j <= n
# 1 <= i + 6 < j <= n
# i=1, j>7

for step, x in enumerate(nums):
    if step - 6 >= 0:
        for i, c in enumerate(count):
            pairs[(i * x) % D] += c

        count[nums[step - 6] % D] += 1

    # print(count, pairs, x, step)

print(pairs[0])
