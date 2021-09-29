###################################################
# 19

# def solve_19(x, c):
#     if c == 2:
#         return sum(x) >= MAX

#     return any(solve_19(i, c+1)
#                for i in calc(*x))


# MAX = 70
# nums = []
# for i in range(1, 64):
#     if solve_19((6, i), 0):
#         nums.append(i)
# print(min(nums), nums)

###################################################


def calc(a, b):
    return (
        (a + 1, b),
        (a * 3, b),
        (a,     b + 1),
        (a,     b * 3))


def next_step(x, c, lvl=0):
    indent = lvl*4*" "

    if sum(x) >= MAX:
        print(indent, x, c % 2 == 0)
        return c % 2 == 0
            # if c == 2:
            #     return True
            # if c > 2:
            #     # print(indent, x, True)
            #     return True
            # if c % 2 == 0:
            #     return True
            # return False

    print(indent, sum(x), x, c)
    return all(next_step(i, c+1, lvl+1)
               for i in calc(*x))


MAX = 70
next_step((6, 0), 0)
# for i in range(1, 64):
#     if next_step([6, i], 1, 0):
#         print(i)
