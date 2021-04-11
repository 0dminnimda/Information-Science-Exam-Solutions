def digit_sum(n):
    out = 0
    while n > 0:
        out += n % 10
        n //= 10
    return out


def to_base(number, base):
    if number == 0:
        return [0]
    digits = []
    while number:
        number, mod = divmod(number, base)
        digits.append(int(mod))
    return digits[::-1]


def g(n):
    n = int(bin(n)[2:])

    n = str(n) + str(digit_sum(n) % 2)
    n = int(n)

    n = str(n) + str(digit_sum(n) % 2)
    n = int(n)

    return int(str(n), 2)


def r(n):
    n = to_base(n, 2)

    n.append(sum(n) % 2)

    n.append(sum(n) % 2)

    strings = [str(i) for i in n]

    return int("".join(strings), 2)



def g(n):
    n = to_base(n, 2)

    el = n[1]
    del n[-1]

    n.append(el)
    n.append(el)

    strings = [str(i) for i in n]
    return int("".join(strings), 2)




c = 170
c = 92
c = 76


# 5
# for i in range(2, 100):
#     if g(i) > c:
#         print(i)
#         break


# 14
# num = 81**15+3**22-27
# base = 9
# res = to_base(num, base)
# print(res.count(8))


# num = 343**5+7**3-1
# base = 7
# for x in range(500):
#     res = to_base(num - x, base)
#     if res.count(6) == 12:
#         print(x, res)

# num = 216**5+6**3-1
# base = 6
# for x in range(500):
#     res = to_base(num - x, base)
#     if res.count(5) == 12:
#         print(x, res)
