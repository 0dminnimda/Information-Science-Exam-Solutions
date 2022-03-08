with open(r"ISESolutions\ЕГЭ\27\6_polak_tren\27-6b.txt") as f:
    data = f.read().split("\n")

D = 6

n = int(data.pop(0))

# max product of 2 different elements across all reminders

"""
     6 60 17 3  7  9  60
0: 0 6 60 60 60 60 60 60   ;
1: 0 0 0  0  0  0  0  0    ;
2: 0 0 0  0  0  0  0  0    ;
3: 0 0 0  0  3  3  9  9    ;
4: 0 0 0  0  0  0  0  0    ;
5: 0 0 0  17 17 17 17 17   ;

Для указанных данных искомое контрольное значение равно 3600.
"""

nums = [0]*D
mx = 0

for step in range(n):
    x = int(data.pop(0))

    for n in nums:
        if (n*x) % D == 0:
            mx = max(mx, n*x)

    r = x % D
    nums[r] = max(nums[r], x)

print(nums)

print(mx)
