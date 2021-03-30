from itertools import product

def g(s):
    while "01" in s or "02" in s or "03" in s:
        s = s.replace("01", "30")
        s = s.replace("02", "101")
        s = s.replace("03", "202")
    return s


for i in product("321", repeat=20):
    si = "".join([str(j) for j in i])
    res = g("0" + "1"*40 + si)
    if res.count("2") == 10:
        if res.count("1") == 15:
            print("3:", res.count("3"), si.count("1") + 40, si)
