from collections import deque

f = open(r"ISESolutions\ЕГЭ\27\25011999\27B.txt")
n, mx = map(int, next(f).split(" "))
nums = [int(i) for i in f]

seq = deque()
s = 0
r = 0
for n in nums:
    seq.append(n)
    s += n
    if s <= mx:
        r = max(r, len(seq))
    else:
        while s > mx:
            s -= seq.popleft()

print(r)
