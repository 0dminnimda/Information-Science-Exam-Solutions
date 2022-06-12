def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += "10"
    else:
        b = "1" + b + "01"
    return int(b, 2)

print(f(13))

for x in range(100):
    r = f(x)
    if r > 516:
        print(x)
        break
