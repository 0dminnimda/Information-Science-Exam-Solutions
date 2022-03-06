

# data = []

# new = [[], []]
# for i in data:
#     r, d = divmod(i, 89)
#     new[0].append(r)
#     new[1].append(d)

# hits = []
# for j in range(len(new[1])):
#     for i in range(len(new[1]))[j:]:
#         s = sum(new[1][j:i])
#         if s % 89 == 0:
#             hits.append(s)

#     # i = j
#     # while i >= 0:
#     #     sum(new[])
#     #     i -= 1


# # 0 0 0 0 0
# # 1 1 1 1
# # 2 2 2
# # 3 3
# # 4
# #

f = open(r'ISESolutions\ЕГЭ\27\27_B.txt')
n = int(f.readline())
k = 89
r = {0: (0, 0)}
ms = 0
m = float('inf')
for _ in range(n):
    x = int(f.readline())
    t = {}
    for key in r:
        t[(key+x) % k] = (r[key][0] + x, r[key][1] + 1)
    if x % k not in t:
        t[x % k] = (x, 1)
    r = t.copy()
    print(ms, m, r)
    if 0 in r:
        if ms < r[0][0]:
            ms = r[0][0]
            m = r[0][1]
        elif ms == r[0][0]:
            m = min(t[0][1], m)

print(m)
quit()

f = open(r'ISESolutions\ЕГЭ\27\27_B.txt')

k, s = 89, 0

mins = {0: (0, 0)}
lst = {**mins}

res = []

for i in range(1, int(f.readline())+1):

    s += int(f.readline())

    if s % k in mins:
        aa = [(s - mins[s % k][0], mins[s % k][1] - i)]
        # print(aa)
        res += aa

    else:

        mins[s % k] = (s, i)

        print(mins)

print(-max(res)[1])
quit()

f = open(r'ISESolutions\ЕГЭ\27\27_B.txt')

n = int(f.readline())

nums = list(map(int, f.readlines()[:n]))

m, ms = float('inf'), 0

for i in range(len(nums)):
    print(i)
    for j in range(i, len(nums)):

        s = sum(nums[i:j + 1])

        if s % 89 == 0 and s > ms:

            ms, m = s, j - i + 1

        if s % 89 == 0 and s == ms:

            m = min(m, j - i + 1)

print(m)
quit()

