p = set(range(192, 256))
q = set(range(0, 256, 2))
a = set()

for x in range(0, 256):
    if not ((x not in a) <= ((x in p) or (x not in q))):
        a.add(x)

print(len(a))
