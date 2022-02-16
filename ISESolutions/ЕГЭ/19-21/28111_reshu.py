from functools import lru_cache

def moves(x):
    return x + 1, x * 3 + 1

@lru_cache
def game(s):
    if s > 31:
        return 0

    if any(game(m) == 0 for m in moves(s)):
        return 1
    if all(game(m) == 1 for m in moves(s)):
        return -1
    if any(game(m) == -1 for m in moves(s)):
        return 2
    if all(game(m) > 0 for m in moves(s)):
        return -2

    return -10000

for s in range(1, 32):
    r = game(s)
    if r != -10000:
        print(s, r)
