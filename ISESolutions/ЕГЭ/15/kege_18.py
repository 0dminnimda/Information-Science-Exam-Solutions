def d(x): return 17 <= x <= 58
def c(x): return 29 <= x <= 80
def a(x): return mn <= x <= mx


def f(x):
    return d(x) <= (((not c(x)) and (not a(x))) <= (not d(x)))


m = 10**8

for mn in range(100):
    for mx in range(mn, 100):
        if all(f(x) for x in range(100)):
            if mx - mn < m:
                print(mx, mn, mx-mn)
                m = mx - mn
