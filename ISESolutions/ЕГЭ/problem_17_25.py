def gg():
    c = 0

    divisible = 100000*7

    minimal = 2*10**10 + 400000

    for i in range(minimal, 4*10**10+1, divisible):
        if (
                i % 101 != 0
                and i % 43 != 0
                and i % 29 != 0
                and i % 13 != 0):

            c += 1

    print(c, minimal)

def isprime(n):
    for d in range(2, int(n**0.5 + 1)):
        if n % d == 0:
            return False
    return True


def get_n_divisors(n):
    c = 1
    i = 1
    while c <= n:
        if isprime(i):
            yield i
            c += 1
        i += 1

mul = 1
for i in get_n_divisors(17):
    mul *= i
print(mul)


# 25

def needed_num(n):
    c = 0
    for d in range(2, int(n**0.5 + 1)):
        if n % d == 0:
            c += 1

            if c == 3:
                return True

    return False

nums = []
for i in range(101*10**6, 102*10**6+1, 2):
    if needed_num(i):
        nums.append(i) #print(i)
breakpoint()