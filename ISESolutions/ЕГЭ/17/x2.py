with open(r"ISESolutions\ЕГЭ\17\17 (2).txt") as f:
    data = f.read().split("\n")

del data[-1]
data = [int(i) for i in data]

sms = []
for tr in zip(data, data[1:], data[2:]):
    tr = list(tr)
    mx = max(tr)
    tr.remove(mx)
    if mx**2 < (tr[0]**2 + tr[1]**2):
        sms.append(mx + sum(tr))

print(len(sms), max(sms))
