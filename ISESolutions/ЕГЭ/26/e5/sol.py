with open(r'ISESolutions\ЕГЭ\26\e5\26.txt') as f:
    data_s = f.read().split("\n")

n = int(data_s.pop(0))
del data_s[-1]
data = ([list(map(int, i.split(" "))) for i in data_s])

week_s = 1634515200
week_l = 60*60*24*7
week_e = week_s + week_l

steps = [0]*(week_l)
for s, e in data:
    if s == 0:
        s = 0
    else:
        s = min(max(s - week_s, 0), week_l)

    if e == 0:
        e = week_l
    else:
        e = min(max(e - week_s, 0), week_l)

    if 0 <= s < week_l:
        steps[s] += 1
    if 0 <= e < week_l:
        steps[e] -= 1

mx = 0
count = 0
s = 1
for step in steps:
    count += step
    if count > mx:
        s = 1
        mx = count
    elif count == mx:
        s += 1

print(mx, s)
