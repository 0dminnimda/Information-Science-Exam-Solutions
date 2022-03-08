with open(r"ISESolutions\ЕГЭ\27\9_polak_tren\27-9b.txt") as f:
    data = f.read().split("\n")

n = int(data.pop(0))
nums = [int(i) for i in data[:-1]]

K = 6
minPrev = 1001
R = 2*1000**2 + 1

for i in range(K, n):
    minPrev = min(minPrev, nums[i - K])
    new_r = minPrev * nums[i]
    if new_r % 2 == 1:
        R = min(R, new_r)

print(R)
