def f(x):
    b = bin(x)[2:]
    i = b.index("1")
    new = b[:i]

    i += 1
    while i < len(b) and b[i] == "0":
        i += 1

    new += b[i:]

    if not new:
        return x
    return x - int(new, 2)


print(f(11), {f(x) for x in range(10, 1000+1)})
