def g():
    res = 128 * 320  # pixels
    mem = 50 * 2**10 * 8  # bits

    for_each = mem / res
    print(2 ** for_each)

g()