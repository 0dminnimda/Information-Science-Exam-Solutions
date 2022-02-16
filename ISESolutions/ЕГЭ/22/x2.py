for xx in range(101, 100000):
    x = xx
    L = x-30
    M = x+30
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 15:
        print(xx)