def b(x): return 18 <= x <= 52
def c(x): return 16 <= x <= 41
def a(x): return mn <= x <= mx


def f(x):
    return (b(x) <= a(x)) and ((not c(x)) or a(x))


m = 10**8

for mn in range(100):
    for mx in range(mn, 100):
        if all(f(x) for x in range(100)):
            if mx - mn < m:
                m = mx - mn
                print(mn, mx, mx-mn)
