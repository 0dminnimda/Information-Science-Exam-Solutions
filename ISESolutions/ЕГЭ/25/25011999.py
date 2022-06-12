from itertools import product

"6789"
"12*0000"
"*0000"
"1200000"

# for i in ("", *map(str, range(1000))):
for n in range(4):
    for i in product("0123456789", repeat=n):
        x = int(f"12{''.join(i)}6789")
        if x > 10**8:
            exit()
        # print(x)
        if x % 39 == 0:
            print(x, x / 39)
