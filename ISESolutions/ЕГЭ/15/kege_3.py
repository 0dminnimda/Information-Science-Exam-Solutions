def d(a, b): return a % b == 0


def f(x, a):
    return (d(x, 15) and (not d(x, 21))) <= ((not d(x, a)) or (not d(x, 15)))


for a in range(1, 100):
    if all(f(x, a) for x in range(1, 100000)):
        print(a)
