def d(a, b):
    return a % b == 0


def f(x, a):
    return (d(x, a) and d(x, 24) and (not d(x, 16))) <= (not d(x, a))


for a in range(1, 100):
    if all(f(x, a) for x in range(1, 10000000)):
        print(a)
