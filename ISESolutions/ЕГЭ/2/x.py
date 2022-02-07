# (x ≡ y ) ∨ ((y ∨ z) → x)

from itertools import product

def f(x, y, z):
    return (x == y) or ((y or z) <= x)


for a in product((0, 1), repeat=3):
    r = f(*a)
    if not r:
        print(*a)

# x z y
# 0 1 1
# 0 0 1
