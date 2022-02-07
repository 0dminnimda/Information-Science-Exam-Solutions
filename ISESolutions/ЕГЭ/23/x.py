### my origina idea ###
# from itertools import chain


# def f(x):
#     if x > mx:
#         return 0, 0
#     if x == mx:
#         return 0, 1

#     if x in banned:
#         return 0, 0

#     opts = [
#         f(x+1),
#         f(x+3),
#         f(x*3),
#     ]

#     chained = list(chain(*opts))

#     if x in needed:
#         return sum(chained), 0

#     return sum(chained[::len(opts)]), sum(chained[1::len(opts)])


# mx = 23
# needed = 10, 17
# banned = ()
# r = f(4)
# print(r)


### beautiful version ###

# def do(x, s):
#     s += "|  "
#     print(s, x)

#     if x == goal:
#         print(s, x, 1)
#         return 1
#     if x > goal or x in banned:
#         print(s, x, 0)
#         return 0

#     opts = [
#         do(x+1, s),
#         do(x+3, s),
#         do(x*3, s),
#     ]

#     r = sum(opts)
#     print(s, x, r)
#     return r


from collections import defaultdict


def do_array(start, end):
    data = defaultdict(int)
    data[end] = 1

    for x in range(start, end)[::-1]:
        if x in banned:
            continue

        opts = [
            x + 1,
            x * 2
        ]

        data[x] = sum(data[opt] for opt in opts)

    return data[start]


def do_recursion(x):
    if x == goal:
        return 1
    if x > goal or x in banned:
        return 0

    opts = [
        x + 1,
        x * 2
    ]

    return sum(do_recursion(opt) for opt in opts)


banned = {20}
points = 3, 11, 25

res1 = 1
for s, e in zip(points, points[1:]):
    res1 *= do_array(s, e)

res2 = 1
for p, goal in zip(points, points[1:]):
    res2 *= do_recursion(p)

print(res1, res2)
