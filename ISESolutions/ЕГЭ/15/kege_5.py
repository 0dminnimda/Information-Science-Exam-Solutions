def d(a, b):
    return a % b == 0


def f(x, a):
    return d(a, 7) and (d(240, x) <= ((not d(a, x)) <= (not d(780, x))))


for a in range(1, 100000):
    if all(f(x, a) for x in range(1, 1000000)):
        print(a)
