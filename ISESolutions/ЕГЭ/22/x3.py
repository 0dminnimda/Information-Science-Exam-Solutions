for xx in range(1000000):
    x = xx
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if x % 2 == 1:
            M = M + (x % 10) // 2
        x = x // 10
    if L == 3 and M == 7:
        print(xx)
    # print(L)
    # print(M)
