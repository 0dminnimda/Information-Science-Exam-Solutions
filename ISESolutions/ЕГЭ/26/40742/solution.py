with open(r"ISESolutions\ЕГЭ\26\40742\26.txt") as f:
    data_s = f.read().split("\n")

n = int(data_s.pop(0))
del data_s[-1]
data = [list(map(int, i.split(" "))) for i in data_s]

start = 1633046400
week_start = 1633305600
week_len = 60*60*24*7
# week_end = week_start + week_len


# def ad(lst, val):
#     for i, v in enumerate(lst):
#         lst[i] = v + val
#     return lst
def ad(lst):
    for v in (lst):
        yield v + 1
    # return lst


mapping = []
week = [0]*week_len
for i, (a, b) in enumerate(data):
    o_a = a
    o_b = b

    if not a:
        a = 0
    else:
        a -= week_start
        a = max(a, 0)
        a = min(a, week_len)

    if not b:
        b = week_len
    else:
        b -= week_start
        b = max(b, 0)
        b = min(b, week_len)
    data[i] = [a, b]

    # week[a:b] = ad(week[a:b])
    if a != b:
        print(i/n, a, b)

        # if i % 100 == 0:
        #     print(*week, sep=";")

    mapping.append((a, i))
    mapping.append((b, i))
    # mapping[a] = i
    # mapping[b] = i


mapping = sorted(mapping, key=lambda x: x[0])

counted = set()
mx = 0
count = 0
gaps_ids = []
for v, i in mapping:
    if i in counted:
        count -= 1
    else:
        counted.add(i)
        count += 1
        gaps_ids.append(i)
        if count > mx:
            mx = count
            gaps_ids.clear()
        # mx = max(mx, count)

gaps = [data[i] for i in gaps_ids]
print(gaps)
real = []
cur = [0, 0]
for (a1, b1), (a2, b2) in zip(gaps, gaps[1:]):
    if b1 == a2:
        cur[-1] = b2
    else:
        print(cur)
        real.append(cur[1] - cur[0])
        cur = [a2, b2]

print(mx, sum(real), real)

# ln = 0
# last = 0
# for i in gaps:
#     a, b = data[i]
#     if a != last:
#         ln = 0
#     ln += 1
#     last = b


# counted = set()
# mx_l = 0
# count = 0
# for (v1, i1), (v2, i2) in zip(mapping, mapping[1:]):
#     if i in counted:
#         count -= 1
#     else:
#         counted.add(i)
#         count += 1
#     if count == mx:

