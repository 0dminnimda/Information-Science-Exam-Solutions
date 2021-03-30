def f(x):
    a = 1
    while x > 0:
        a *= x % 7
        x //= 7
    return a

def f(x):
    m = 0
    s = 0
    while x > 0:
        d = x % 8
        s += d
        if d > m:
            m = d
        x //= 8
    return m, s

out = 40
out = 5, 12

for i in range(500):
    if f(i) == out:
        print(i)
         #break