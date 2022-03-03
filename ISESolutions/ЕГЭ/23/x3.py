def f(x, goal):
    if x == goal:
        return 1
    if x > goal:
        return 0

    return f(x + 1, goal) + f(x * 3, goal)

print(f(3, 37))
