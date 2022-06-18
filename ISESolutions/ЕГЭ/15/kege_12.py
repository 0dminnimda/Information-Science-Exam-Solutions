def f(a, x, y):
    return (2*x + y != 70) or (x < y) or (a < x)


for a in range(10000):
    if all(f(a, x, y) for x in range(1000) for y in range(1000)):
        print(a)
