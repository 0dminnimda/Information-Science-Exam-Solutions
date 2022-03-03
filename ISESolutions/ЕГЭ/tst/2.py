from itertools import product


def f(x, y, z, w):
    return w or (x <= y) and ((not z) <= x)


print("x y z w")
for a in product((0, 1), repeat=4):
    r = f(*a)
    if not r:
        print(*a)

# w z y x
