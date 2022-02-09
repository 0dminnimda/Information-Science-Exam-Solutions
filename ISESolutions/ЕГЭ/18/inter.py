n = 15

import numpy as np

# z = []
# for i in range(n+1):
#     zz = []
#     for j in range(n+1):
#         a = np.zeros(n)
#         a[j] = 1
#         zz.append(a)
#     z.append(zz)

# z = [[np.zeros(n) for j in range(n+1)] for i in range(n+1)]
# z = [[z[i][j][j] = 0 for j in range(n+1)] for i in range(n+1)]

z = [[1 if (i == n or j == n) else 0 for j in range(n+1)]
     for i in range(n+1)]
# idd = [[i * n + j for j in range(n+1)] for i in range(n+1)]
# from pprint import pprint
# pprint(idd)

# # 0|0, 1|1 ... n-1|n-1
# # 1|0, 2|1 ... n-1|n-2
# # ...
# # n-2|0, n-1|1
# # n-1|0
# for i in range(n):
#     j = 0
#     while i != n:
#         print(i, j, idd[i][j])
#         z[i][j] = z[i-1][j-1] + z[i-1][j] + z[i][j-1]

#         i += 1
#         j += 1

for i in range(n):
    j = 0
    while i >= 0:
        # print(i, j)
        z[i][j] = z[i-1][j-1] + z[i][j-1] + z[i-1][j]

        j += 1
        i -= 1

for j in range(1, n):
    i = n - 1
    while j < n:
        # print(i, j)
        z[i][j] = z[i-1][j-1] + z[i][j-1] + z[i-1][j]

        j += 1
        i -= 1

for i in range(n):
    print(z[i][i])

# ln = len(str(max(max(z))))
ln = len(str(np.max(z)))
print(ln)
print("[")
for item in z[:-1]:
    print("    [" + ", ".join(f"{i: >{ln}}" for i in item[:-1]) + "],")
    # print(f" {item[:-1]!s: >{ln}},")
print("]")
# [3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907]
# [3, 13, 63, 321, 1683, 8989, 48639, 265729, 1462563, 8097453, 45046719, 251595969, 1409933619, 7923848253, 44642381823]
# [31, 481, 4991, 39041, 246047, 1303777, 5984767, 24331777, 89129247, 298199265, 921406335, 2653649025, 7178461215, 18359266785, 44642381823]
