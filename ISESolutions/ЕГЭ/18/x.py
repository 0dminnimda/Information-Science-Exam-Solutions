d=[
[24, 59, 17, -11, 1, 43, 12, 30, 30, 21, 6, -17, 47, 29, 32],
[8, -11, -34, -38, 17, -10, 29, 56, -39, 0, 5, -19, -1, -24, -25],
[-10, 48, -33, -17, 4, 47, 34, -10, 54, 48, 1, 24, 36, -14, 5],
[58, 44, 29, -38, -13, 56, 49, 59, -23, 33, 1, 5, -28, 8, 24],
[2, -9, 9, -12, 44, 26, -27, -31, -30, 6, 6, 23, 14, 59, -4],
[-30, 22, 20, 28, -2, 30, 12, 37, 38, 16, -4, 31, 28, -24, 39],
[-33, -40, 25, -17, -10, -39, 26, -5, -17, 29, 5, 12, -29, -15, -17],
[14, 25, 52, -7, -5, 42, 11, -4, 56, 31, 32, -9, 58, -15, -30],
[44, -15, -3, 55, 16, -1, 52, 29, 46, 19, 52, 49, -22, 58, 30],
[34, 36, 11, 15, 60, -3, 29, 41, -39, 19, 14, 56, -33, -9, 40],
[-31, -10, -19, -39, -32, 33, -20, -12, 24, 29, 18, 51, -29, 49, -2],
[53, 30, 0, 15, -9, -39, -34, -23, 35, -24, 5, -2, 22, -6, 54],
[-28, -31, 26, -29, 26, -31, 9, -36, -8, 15, -12, 13, 15, 0, -22],
[46, 21, -24, 7, 34, -40, -7, -6, 21, 54, 20, 14, -33, -9, 33],
[56, 29, 55, 40, 34, -33, -14, -5, 2, 41, 39, -36, 6, 16, 12],
]

# d = [
# [4, 21, -36, 11, 0],
# [37, -12, 29, 7, 0],
# [-30, 24, -1, -5, 0],
# [8, -8, 9, 21, 0],
# [0, 0, 0, 0, 0]
# ]

m = -100000
new = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, m],
    [m, m, m, m, m, m, m, m, m, m, m, m, m, m, m, 0],
    # [0, 0, 0, 0, m],
    # [0, 0, 0, 0, m],
    # [0, 0, 0, 0, m],
    # [0, 0, 0, 0, m],
    # [m, m, m, m, 0],
]

n = 15

for i in range(n*2-1):
    j = 0
    while i >= 0:
        if i < n and j < n:
            # print(i, j)
            new[i][j] = d[i][j] + max(new[i-1][j-1], new[i][j-1], new[i-1][j])

        j += 1
        i -= 1

# print()
# for j in range(1, n):
#     i = n - 1
#     while j < n:
#         print(i, j)
#         new[i][j] = d[i][j] + max(new[i-1][j-1], new[i][j-1], new[i-1][j])

#         j += 1
#         i -= 1

# from pprint import pprint
# pprint(new)
print("[")
for item in new[:-1]:
    print(f" {item[:-1]},")
print("]")
