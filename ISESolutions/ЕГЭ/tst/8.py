# from itertools import product

# s = "ABCD"
# c = set()
# for comb in product(s, repeat=3):
#     comb = "".join(comb)
#     # if len(set(comb)) != len(comb):
#     #     continue

#     if "AA" in comb or "AB" in comb or "BA" in comb or "AC" in comb or "CA" in comb:
#         # print(comb)
#         continue

#     if "BC" in comb or "CB" in comb:
#         # print(comb)
#         continue

#     print(comb)
#     c.add(comb)

# rc = {"ADA", "ADB", "ADC", "ADD", "BAD", "BBB", "BBD", "BDA", "BDB", "BDC", "BDD", "CAD", "CCC", "СCD", "CDA", "CDB", "CDC", "CDD", "DAB", "DAC", "DAD", "DBB", "DBD", "DCC", "DCD", "DDA", "DDB", "DDC", "DDD"}

# print(len(c), rc - c)

from itertools import product

# s = "ДЖОБС"
# c = 0

# for comb in product(s, repeat=6):
#     comb = "".join(comb)

#     if comb.count("Д") != 1 or comb.count("О") != 1 or comb.count("С") != 1:
#         continue

#     if comb.count("Ж") > 2:
#         continue

#     c += 1

# print(c)

from itertools import product

c = 0
t = False
s = "РЕЖИМДНО"

for comb in product(s, repeat=6):
    comb = "".join(comb)

    if len(set(comb)) != len(comb):
        continue

    # if comb == "ДОМОК":
    #     t = True
    # elif comb == "КОМОД":
    #     c += 1
    #     t = False

    # if t:
    #     c += 1

    if comb[0] not in "РЖМДН":
        continue

    if comb[1] not in "ЕИО":
        continue

    if comb[-1] not in "ЕИО":
        continue

    c += 1

print(c)
