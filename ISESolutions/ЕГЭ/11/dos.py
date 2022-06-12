from math import log2, ceil
x = 250 * ceil(log2(10 + 1560))
print(ceil(x / 8) * 32768 / 2**10)
