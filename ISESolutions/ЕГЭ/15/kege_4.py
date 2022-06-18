def d(a, b): return a % b


def f(x, a):
    return ((d(x, 4) != 3) or (d(x, 6) != 1)) <= (d(x, 36) != a)


for a in range(1, 100):
    if all(f(x, a) for x in range(1, 1000000)):
        print(a)
