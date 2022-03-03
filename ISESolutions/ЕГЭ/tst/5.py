def f(x):
    if x % 3 == 0:
        x //= 3
    else:
        x -= 1

    if x % 7 == 0:
        x //= 7
    else:
        x -= 1

    if x % 11 == 0:
        x //= 11
    else:
        x -= 1

    return x


c = 0
for x in range(2, 1000000):
    r = f(x)
    if r == 6:
        print(x)
        c += 1

print(c)
# 7
