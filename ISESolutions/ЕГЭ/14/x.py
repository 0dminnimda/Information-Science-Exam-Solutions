def to_base(x, b):
    out = []
    while x:
        x, r = divmod(x, b)
        out.append(r)
    return out[::-1]

print(to_base(24234, 2), bin(24234))

for base in range(2, 10000):
    a = to_base(56, base)
    b = to_base(45, base)
    if a[-1] == b[-1] == 1:
        print(base, a, b)
