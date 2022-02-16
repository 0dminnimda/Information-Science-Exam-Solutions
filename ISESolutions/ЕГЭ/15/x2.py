def P(x): return 17 <= x <= 46
def Q(x): return 22 <= x <= 57
def A(x): return mn <= x <= mx

def f():
    for x in range(10000):
        r = (not A(x)) <= ((P(x) and Q(x)) <= A(x))
        if not r:
            return False

    return True


lens = []
for mn in range(70):
    for mx in range(mn, 70):
        r = f()
        if r:
            if mx - mn + 1 == 25:
                print(mn, mx, mx - mn + 1)
            lens.append(mx - mn + 1)

print(min(lens))
