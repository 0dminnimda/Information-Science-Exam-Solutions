from itertools import product

c = 0
s = "ПИР"
for comb in product(s, repeat=5):
    comb = "".join(comb)

    if comb.count("П") != 1:
        continue


    c += 1

print(c)