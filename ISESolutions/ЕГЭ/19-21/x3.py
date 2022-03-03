from functools import lru_cache

def moves(x):
    return x + 1, x * 3

@lru_cache(None)
def game(x):
    if x >= 46:
        return 0

    if any(game(m) == 0 for m in moves(x)):
        return 1
    if any(game(m) == 1 for m in moves(x)):
        return -1
    if any(game(m) == -1 for m in moves(x)):
        return 2
    if all(game(m) > 0 for m in moves(x)):
        return -2

    return -10000

for x in range(1,46):
    r = game(x)
    if r != -10000:
        print(x, r)

