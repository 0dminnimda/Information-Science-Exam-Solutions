def g(s):
    n = 2
    while s < 37:
        s += 3
        n *= 2
    return n

for i in range(1000):
    print(i, g(i))
    if g(i) == 128:
        print(i)
        break