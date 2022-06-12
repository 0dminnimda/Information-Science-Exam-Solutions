from itertools import product


def old_f(x):
    a = 0
    b = 0
    while x > 0:
        # x, d = divmod(x, 10)
        a += 1
        d = x % 10
        if d % 3 == 0:
            b += d
        x //= 10
    return a, b


def f(x):
    return sum(x)
    # b = 0
    # for d in x:
    #     if d % 3 == 0:
    #         b += d
    # return b

# print(old_f(999999999907))
# exit()
# print(f(0), f(1), f(10), f(11), f(12), f(12345), f(1234533), f(10**11))

c = 0
for comb in product((0, 3, 6, 9), repeat=12):
    r = f(comb)
    if r == 99:
        if 0 in comb:
            c += comb.count(0)*7
            if comb[0] == 0:
                c -= 1
        else:
            c += 1
        print("".join(map(str, comb)), r, c)
    # print(comb, f(comb))
print(c)

# 435
# 31812

# c = 0
# for x in range(10**11, 10**12):
#     # a, b = f(x)
#     # if a == 12 and b == 99:
#     if f(x) == 99:
#         c += 1
#         print(x, c)
# print(c)
