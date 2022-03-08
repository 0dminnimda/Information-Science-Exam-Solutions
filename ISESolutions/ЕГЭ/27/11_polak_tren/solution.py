with open(r"ISESolutions\ЕГЭ\27\11_polak_tren\27-11b.txt") as f:
    data = f.read().split("\n")

n = int(data.pop(0))
D = 8

sums = [0]*D

for i in range(n):
    x_s = list(map(int, data[i].split(" ")))

    cur_sums = [0]*D
    for s in sums:
        for x in x_s:
            if s != 0 or i == 0:
                r = (s + x) % D
                cur_sums[r] = max(cur_sums[r], s + x)

    sums = cur_sums
    # print(sums)

print(sums[0])
