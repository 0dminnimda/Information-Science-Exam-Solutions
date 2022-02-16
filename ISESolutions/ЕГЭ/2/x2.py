# (x ≡ ( w ∨ y)) ∨ ((w → z ) ∧ (y → w))

from itertools import product


def f(x, y, z, w):
    return (x == (w or y)) or ((w <= z) and (y <= w))


for a in product((0, 1), repeat=4):
    r = f(*a)
    if not r:
        print(*a)

# z x y w
# 1 0 0 1
# 0 0 0 1
# 1 0 1 0

# 1 0 0 0