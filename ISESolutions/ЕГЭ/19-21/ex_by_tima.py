from functools import lru_cache
from collections import defaultdict


def moves(lol):
    a, b = lol
    return (a+1, b), (a*2, b), (a, b+1), (a, b*2)


nums = defaultdict(int)


@lru_cache
def gay(lol):
    nums[lol] += 1
    # print(nums)
    if sum(lol) >= 62:
        return "W"

    if any(gay(m) == "W" for m in moves(lol)):
        return "P1"
    if any(gay(m) == "P1" for m in moves(lol)):
        return "B1"
    if any(gay(m) == "B1" for m in moves(lol)):
        return "P2"
    if all(gay(m) == "P1" or gay(m) == "P2" for m in moves(lol)):
        return "B2"
    # if all(gay(m) == "P1" or ma)
    # all(map(labmda x: x == "", moves(lol)))


for i in range(1, 52):
    r = gay((10, i))
    if r is not None:
        print(i, r)
    print(nums)

# @lru_cache
# def calc(x):
#     print(x)
#     return x + 1

# calc(100)
# calc(100)

cache = {}

def lru_cache(f):
    def intetnal(*args, **kw):
        key = (args, tuple(kw))
        r = cache.get(key)
        if r is None:
            cache[key] = result = f(*args, **kw)
        else:
            result = r
        return result
    return intetnal


import this