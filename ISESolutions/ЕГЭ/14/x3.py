def to_base(x, base):
    r = []

    while x:
        x, l = divmod(x, base)
        r.append(l)

    return r[::-1]

print(to_base(0b10110, 2))

x = 216**6 + 216**4 + 36**6 - 6**14 - 24

print(len(to_base(x, 6)))
