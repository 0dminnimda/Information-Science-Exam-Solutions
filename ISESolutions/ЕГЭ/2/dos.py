from itertools import product

def f(x, y, z, w):
    # ¬(𝑥 → 𝑧) ∨ (𝑦 ≡ 𝑤) ∨ ¬𝑦
    return (not (x <= z)) or (y == w) or (not y)


for a in product((0, 1), repeat=4):
    r = f(*a)
    if not r:
        print(*a)


# x z y w
# 0 0 1 0
# 0 1 1 0
# 1 1 1 0
