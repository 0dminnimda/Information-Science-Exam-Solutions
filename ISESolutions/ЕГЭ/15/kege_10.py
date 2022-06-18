def f(a, x, y):
    return (x*y > a) and (x > y) and (x < 8)


for a in range(10000):
    if all(not f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
