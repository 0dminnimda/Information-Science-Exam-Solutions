#    5  3   8   2   6
#    1  2   4   5   9
# 0: 0 -|3 0|0 0|0 0|0
# 1: 1 4|7 0|0 0|0 0|0
# 2: 5 8|- 0|0 0|0 0|0

with open(r"ISESolutions\ЕГЭ\27\3_polak_tren\27-3a.txt") as f:
    data = f.read().split("\n")

n = int(data.pop(0))
del data[-1]


sums = [0]*3

for x in map(int, data.pop(0).split(" ")):
    sums[x % 3] = x

for line in data:
    ab = list(map(int, line.split(" ")))

    cur_step = [10**10]*3

    for rem, s in enumerate(sums):
        for x in ab:
            if s != 0:
                r = (x + rem) % 3
                cur_step[r] = min(s+x, cur_step[r])

    sums = [i if i != 10**10 else 0 for i in cur_step]
    print(sums)

print(sums[0])

# better:
#       5     3     8   2   6
#       1     2     4   5   9
# 0: 0 i|i i+3|3   0|0 0|0 0|0
# 1: 0 1|i 4  |7   0|0 0|0 0|0
# 2: 0 i|5 8  |i+2 0|0 0|0 0|0


with open(r"ISESolutions\ЕГЭ\27\3_polak_tren\27-3a.txt") as f:
    data = f.read().split("\n")

n = int(data.pop(0))
del data[-1]


sums = [0]*3

for line in data:
    ab = list(map(int, line.split(" ")))

    cur_step = [10**10]*3

    for rem, s in enumerate(sums):
        for x in ab:
            r = (s+x) % 3
            cur_step[r] = min(s+x, cur_step[r])

    sums = cur_step
    print(sums)

print(sums[0])


# s = 0

# rems = [10**10] * 3

# for line in data:
#     a, b = map(int, line.split(" "))
#     if a < b:
#         a, b = b, a

#     s += b
#     diff = a - b

#     new = rems[:]
#     for rem, diff_s in enumerate(rems):
#         r = (rem + diff) % 3
#         # if rems[r] == 0:
#         #     if r == diff % 3:
#         #         new[r] = diff_s + diff
#         # else:
#         new[r] = min(diff_s + diff, rems[r])
#         print(new, diff_s, diff, r)
#     rems = new
#     print()

# print(s, rems)
