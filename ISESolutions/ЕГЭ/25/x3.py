def divs(x):
    r = []
    for d in range(2, int(x**0.5) + 1):
        if x % d == 0:
            r.append(d)
            if x / d != d:
                r.append(x // d)

        if len(r) > 4:
            return False

    if len(r) != 4:
        return False
    return r

for x in range(210235, 210300):
    r = divs(x)
    if r:
        print(x, sorted(r))
