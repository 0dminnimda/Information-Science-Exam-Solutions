def f(x):
    res = []
    for d in range(2, int(x**0.5)+1):
        r, m = divmod(x, d)
        print(r, m)
        if m == 0:
            res.append(r)
            if len(res) == 2:
                return sum(res)

    return 0

print(f(10))
quit()
for x in range(13_500_000, 14_000_000):
    r = f(x)
    # if 0 < r < 200_000:
    #     print("nn", x, r)
    if 0 < r < 100_000:
        print("n", x, r)
    # print(r)
    if 0 < r < 10_000:
        print(x, r)
