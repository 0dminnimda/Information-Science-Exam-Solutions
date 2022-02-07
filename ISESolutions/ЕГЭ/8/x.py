from itertools import product

c = 0
s = "АВТОР"
for comb in product(s, repeat=4):
    comb = "".join(comb)
    c += 1

    print(c, comb)

    if comb == "ВАТА":
        break


print(c)