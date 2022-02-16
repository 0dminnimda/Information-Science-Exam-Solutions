# s = set()

# def do_recursion(x, goal):
#     s.add(x)
#     if x == goal:
#         return 1
#     if x > goal or x in banned:
#         return 0

#     opts = [
#         x + 1,
#         x * 2
#     ]

#     [do_recursion(opt, goal) for opt in opts]


# banned = {20}
# print(s, do_recursion(3, 11))

from functools import lru_cache

s = set()

@lru_cache(None)
def f(x, c):
    s.add(x)

    if c == 0:
        return

    f(x + 1, c-1)
    f(x * 2, c-1)

f(1, 5)
print(len(s), s, set(range(100)) - s)

