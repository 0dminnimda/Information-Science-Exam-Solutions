
def f(x, c):
    if x == mx:
        return c
    if x > mx:
        return 1000000000
    c += 1
    h = [f(x+2, c), f(x*2, c)]
    return min(h)


mx = 3
print(f(1, 0))
