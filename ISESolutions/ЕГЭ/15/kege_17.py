a = set()
p = set(range(2, 21, 2))
q = set(range(3, 31, 3))
r = set(range(12, 61, 12))

for x in range(1, 1000):
    f = (x not in a) <= (((x in p) and (x in q)) <= (x in r))
    if not f:
        a.add(x)

print(a)
