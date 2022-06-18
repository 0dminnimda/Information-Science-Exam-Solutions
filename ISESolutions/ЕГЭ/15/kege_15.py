a = set()
b = {1, 2, 3, 4, 5, 6}
c = {3, 6, 9, 12}

for x in range(100):
    f = (not ((x not in a) and (x in c))) or (x not in b)
    if not f:
        a.add(x)

print(len(a), a)
