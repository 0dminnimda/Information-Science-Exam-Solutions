def f(x):
    if x == 0:
        return 0
    elif x % 3 == 0 and x > 0:
        return x + f(x - 3)
    elif x % 3 > 0:
        return x + f(x - (x % 3))
print(f(26))
