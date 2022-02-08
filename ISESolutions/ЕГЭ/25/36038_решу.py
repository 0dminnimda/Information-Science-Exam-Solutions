def m(x):
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            return d + x // d

    return 0

for x in range(452_021, 1_000_000):
    r = m(x)
    if r % 7 == 3:
        print(x, r)
