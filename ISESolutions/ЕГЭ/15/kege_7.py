def f(x, a):
    A = (((x & 13 != 0) or (x & a != 0)) <= (x & 13 != 0))
    return A or ((x & a != 0) and (x & 39 == 0))


for a in range(1000):
    if all(f(x, a) for x in range(100000)):
        print(a)
