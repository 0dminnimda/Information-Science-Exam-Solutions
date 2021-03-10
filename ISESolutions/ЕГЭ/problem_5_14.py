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


# 5
for i in range(1000):
    assert g(i) == r(i)
    if g(i) > 170:
        print(i)
        break

# 14
res = to_base(81**15+3**22-27, 9)
print(res.count(8))
