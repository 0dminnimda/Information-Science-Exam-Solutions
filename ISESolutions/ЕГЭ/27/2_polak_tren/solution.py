with open(r"ISESolutions\ЕГЭ\27\2_polak_tren\27-2b.txt") as f:
    data = f.read().split("\n")

n = int(data.pop(0))

D = 3

sums = [0]*D

elem = 0

for i in range(n):
    ab = list(map(int, data.pop(0).split(" ")))

    cur_sums = [elem]*D

    for s in sums:
        for x in ab:
            if s != 0 or i == 0:
                r = (s + x) % D
                cur_sums[r] = max(cur_sums[r], s + x)

    sums = cur_sums

print(sums[0])
