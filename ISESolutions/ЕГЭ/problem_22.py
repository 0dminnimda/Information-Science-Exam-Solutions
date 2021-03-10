def f(x):
    a = 1
    while x > 0:
        a *= x % 7
        x //= 7
    return a


for i in range(500):
    if f(i) == 40:
        print(i)
        break