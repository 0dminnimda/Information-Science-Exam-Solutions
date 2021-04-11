from itertools import product

# st = "тимофей"

# c = 0
# for comb in product(st, repeat=5):
#     if comb.count("т") < 1:
#         continue
#     if comb.count("й") > 1:
#         continue
#     c += 1
# print(c)

st = "андрей"

c = 0
for comb in product(st, repeat=5):
    if comb.count("а") < 1:
        continue
    if comb.count("й") > 1:
        continue
    c += 1
print(c)
