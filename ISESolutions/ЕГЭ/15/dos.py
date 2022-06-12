def d(a, b):
    return a % b == 0


def f(a):
    for x in range(1, 1000000):
        r = (d(x, 3) <= (not d(x, 5))) or (x + a >= 70)
        if not r:
            return False
    return True


# for a in range(100):
for a in [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]:
    if f(a):
        print(a)
