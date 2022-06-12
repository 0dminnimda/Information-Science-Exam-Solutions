from itertools import product

for i, comb in enumerate(product(sorted("ПАРУС"), repeat=5)):
    comb = "".join(comb)
    if (comb[0] == "У") and (comb.count("А") == 2) and ("АА" not in comb):
        print(comb, i + 1)
        break
