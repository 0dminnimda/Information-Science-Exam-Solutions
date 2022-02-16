def divs(x):
    r = []
    for d in range(1, int(x**0.5) + 1):
        if x % d == 0:
            r.append(d)
            if x / d != d:
                r.append(x // d)

    return sorted(r)

print(divs(100), divs(1*2*3*4*5))
for x in range(185311, 185331):
    r = divs(x)
    if len(r) == 4:
        print(x, r)
