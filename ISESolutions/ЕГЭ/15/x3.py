def f(a):
    for x in range(100000000):
        r = (x&41 != 0) <= ((x&33 == 0) <= (x&a != 0))

        if not r:
            return False

    return True

for a in range(8, 100):
    r = f(a)
    print(a)

    if r:
        print(a, r)

