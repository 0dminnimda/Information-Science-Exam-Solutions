a = set()
b = {1, 3, 5, 7, 9, 11}
c = {3, 6, 9, 12}

for x in range(100):
    if not (((x in b) <= (x not in c)) or (x in a)):
        a.add(x)

print(sum(a))
