def to_base(x, base):
    res = []
    while x:
        x, rem = divmod(x, base)
        res.append(rem)
    return res[::-1]


print(to_base(1235, 2), bin(1235))
x = 3 * 16**2018 - 2 * 8**1028 - 3 * 4**1100 - 2**1050 - 2022
print(to_base(x, 4).count(3))
