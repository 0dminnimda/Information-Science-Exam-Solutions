with open(r"ISESolutions\ЕГЭ\27\8_polak_tren\27-8b.txt") as f:
    data = f.read().split("\n")

n = int(data.pop(0))
nums = [int(i) for i in data[:-1]]

K = 5
minPrev = 1001
R = 2*1000**2 + 1

for i in range(K, n):
    minPrev = min(minPrev, nums[i - K])
    R = min(R, minPrev**2 + nums[i]**2)

print(R)
