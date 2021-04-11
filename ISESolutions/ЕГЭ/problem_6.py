def g(s):
    n = 2
    while s < 37:
        s += 3
        n *= 2
    return n

def g(s):
    s = (s + 1) // 7
    if s == 0:
        return None
    n = 36
    while s < 2050:
        s *= 2
        n += 3
    return n


c = 128
c = 66


for i in range(1000):
    # print(i, g(i))
    if g(i) == c:
        print(i)
        # break