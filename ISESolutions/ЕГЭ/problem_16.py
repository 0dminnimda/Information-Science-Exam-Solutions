# def f(n):
#     if n == 1:
#         return 1
#     elif n % 2 == 0:
#         return n * f(n-1)
#     elif n > 1:
#         return n + f(n-2)

# print(f(-1))

def f(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return f(n//2)
    else:
        return 1 + f(n-1)


def f(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return f(n//2)
    else:
        return 1 + f(n-1)


c = 12
c = 11

for i in range(10**4):
    if f(i) == c:
        print(i)
