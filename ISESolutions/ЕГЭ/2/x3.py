from itertools import product

def f(x, y, z, w):  # ((x → y ) ∧ (y → w)) ∨ (z ≡ ( x ∨ y))
    return ((x <= y) and (y <= w)) or (z == (x or y))

print("x y z w")
for a in product((0, 1), repeat=4):
    r = f(*a)
    if not r:
        print(*a)


# y w z x
# 1 0 0 1
# 1 0 0 0
# 0 1 0 1

# 1 0 0 0