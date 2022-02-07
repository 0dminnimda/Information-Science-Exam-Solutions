from math import log2, ceil

x = ceil(15 * ceil(log2(len(set("КТАМРОФНИ")))) / 8)
print(x * 30)