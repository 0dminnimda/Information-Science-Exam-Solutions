def f(a):
    for x in range(1000):
        for y in range(10000):
            r = ((x < a) <= (x**2 < 100)) and (((y**2) <= 64) <= (y <= a))
            if not r:
                return False
    return True

for a in 8, 9, 10:#range(100000):
    r = f(a)
    if r:
        print(a)
