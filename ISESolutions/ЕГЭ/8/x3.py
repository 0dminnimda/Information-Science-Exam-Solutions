from itertools import product

for i, comb in enumerate(product(sorted("ПАРУС"), repeat=4)):
    comb = "".join(comb)
    print(comb)

    if comb[0] == "Р":
        print(i, comb)
