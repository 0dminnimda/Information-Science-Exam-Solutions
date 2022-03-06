# def divs(x):
#     r = []
#     for d in range(1, int(x**0.5) + 1):
#         if x % d == 0:
#             r.append(d)
#             if x / d != d:
#                 r.append(x // d)

#     return r

def check_divs(x, divs):
    r = []
    for d in divs:
        if x % d == 0:
            r.append(d)
    return r

# divs_26 = divs(26)
# divs_26.remove(1)

# print(divs_26)

# ress = {}.fromkeys(divs_26, 0)

from collections import defaultdict

divs_26 = [1, 2, 13, 26]
ross = defaultdict(int)

# ross = {}.fromkeys([1, 2, 13, 26], 0)


def my_sorted(*args):
    return tuple(sorted(args))


with open(r"ISESolutions\ЕГЭ\27\27-A.txt") as f:
    raw_data = f.read().split("\n")

del raw_data[-1]
data = [int(i) for i in raw_data]

for x in data:
    d = check_divs(x, divs_26)
    assert len(d) < 5

    for dd in d:
        ross[dd] += 1

    if len(d) == 2:
        ross[my_sorted(d[0], d[1])] += 1
    if len(d) == 3:
        # ross[my_sorted(d[0], d[1])] += 1
        # ross[my_sorted(d[1], d[2])] += 1
        ross[my_sorted(d[0], d[1], d[2])] += 1
    if len(d) == 4:
        # ross[my_sorted(d[0], d[1])] += 1
        # ross[my_sorted(d[1], d[2])] += 1
        # ross[my_sorted(d[2], d[3])] += 1
        # ross[my_sorted(d[0], d[1], d[2])] += 1
        # ross[my_sorted(d[1], d[2], d[3])] += 1
        ross[my_sorted(d[0], d[1], d[2], d[3])] += 1

# ross[1] * 

print(ross)

    # for d in ress:
    #     if x % d == 0:
    #         ress[d] += 1

# r = [
#     len(data) * ress[26] - ress[26],
#     ress[2] * ress[13]
# ]
