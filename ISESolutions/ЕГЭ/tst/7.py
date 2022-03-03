# x * z / 2 = 16 * z
# x / 2 = 16
# x = 32

# 32

from math import log2, ceil

# print(log2(256))
# n = ceil(log2(256) * 240 * 320 / 8 / 1024)
# print(n * (60 / 15))

# n = 2048 * 32

# print(192 * 1024 * 8 / n)

n = 600 * 600 * 24
m = 300 * 300 * ceil(log2(16))
# 128*1024*8 / m = x / n
# x = 128*1024*8 * n / m
print(128*1024*8 * n / m / 1024 / 1024 / 8)
