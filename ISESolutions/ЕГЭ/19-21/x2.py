from functools import lru_cache
from collections import defaultdict


# @lru_cache(None)
def moves(a, b):
    return (a + 1, b), (a, b + 1), (a * 4, b), (a, b * 4)


@lru_cache(None)
def game(nums):
    if sum(nums) >= mx:
        return 0

    if any(game(m) == 0 for m in moves(*nums)):
        return 1
    if all(game(m) == 1 for m in moves(*nums)):  # 19 - any, 20-21 - all
        return -1
    if any(game(m) == -1 for m in moves(*nums)):
        return 2
    if all(game(m) > 0 for m in moves(*nums)):
        return -2

    return -100000


mx = 151
for i in range(1, 141):
    r = game((9, i))
    if r != -100000:
        print(i, r)
