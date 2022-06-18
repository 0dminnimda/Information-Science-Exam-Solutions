a = set(range(1, 1000))
p = set(range(2, 21, 2))
q = set(range(5, 51, 5))

for x in range(1, 1000):
    f = ((x in a) <= (x in p)) and ((x in q) <= (x not in a))
    if not f:
        a.remove(x)

print(len(a), a)
