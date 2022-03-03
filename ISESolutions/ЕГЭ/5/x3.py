def f(x):
    s = str(x)
    a = sorted([int(s[0]) + int(s[1]), int(s[1]) + int(s[2])])
    return int("".join([str(i) for i in a]))

c = 0
for i in range(100, 1000):
    r = f(i)
    if r == 1216:
        c += 1
        print(i)
# print(f(843))
print(c)
