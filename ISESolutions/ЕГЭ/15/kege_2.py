def d(a, b):
    return a % b == 0


def f(x, a):
    return ((not d(x, 84)) or (not d(x, 90))) <= (not d(x, a))


for a in range(1, 100000):
    if all(f(x, a) for x in range(1000000)):
        print(a)
