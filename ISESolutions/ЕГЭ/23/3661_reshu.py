from functools import lru_cache

s = set()

@lru_cache
def f(x, c):
    if x < 0:
        return None
    # if x in s:
    #     return None

    if c == 0:
        print(x, c)
        s.add(x)
        return None

    f(x + 3, c-1)
    f(x - 4, c-1)

f(5, 15)
print(len(s), s)
