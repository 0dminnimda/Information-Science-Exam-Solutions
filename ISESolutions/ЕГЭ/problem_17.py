c = 0

minimal = float("inf")

divisible = 100000*7

minimal = 2*10**10 + 400000

for i in range(minimal, 4*10**10+1, divisible):
    if (
            i % 101 != 0
            and i % 43 != 0
            and i % 29 != 0
            and i % 13 != 0):

        c += 1

print(c, minimal)