def p(x): return 17 <= x <= 54
def q(x): return 37 <= x <= 83
def a(x): return mn <= x <= mx


def f(x):
    return p(x) <= (((q(x)) and (not a(x))) <= (not p(x)))


m = 10**8

for mn in range(100):
    for mx in range(mn, 100):
        if all(f(x) for x in range(100)):
            if mx - mn < m:
                print(mx, mn, mx-mn)
                m = mx - mn
