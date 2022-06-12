with open(r"ISESolutions\ЕГЭ\17\17 (4).txt") as f:
    lines = f.read().split("\n")

del lines[-1]
nums = [int(x) for x in lines]

D = 17
mins = [10000000]*D

for n in nums:
    mins[n%D] = min(n, mins[n%D])
print(mins)

t = mins[0]

mx = -10000
c = 0
for a, b in zip(nums, nums[1:]):
    if a % t == 0 or b % t == 0:
        c += 1
        mx = max(mx, a + b)

print(c, mx)
