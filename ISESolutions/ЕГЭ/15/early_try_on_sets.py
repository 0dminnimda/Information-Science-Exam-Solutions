# P = set(range(25, 51))
# Q = set(range(32, 48))
# print(Q - P)

# P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
print(sum(Q.intersection(P)))


def belonging(x, s):
    return x in s


def implies(a, b):
    return b ** a

p = P
q = Q


def g(x, a):
    return implies(
        implies(
            not belonging(x, a),
            belonging(x, p)
        ),
        implies(
            belonging(x, a),
            belonging(x, q)
        )
    )


for i in range(100):
    pass

# ^\s*#.*$\n
# ^\s*\n