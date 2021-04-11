from itertools import product

def g(s):
    while "01" in s or "02" in s or "03" in s:
        s = s.replace("01", "30")
        s = s.replace("02", "101")
        s = s.replace("03", "202")
    return s


def test():
    for i in product("321", repeat=70):
        si = "0" + "".join(i)
        res = g(si)
        print(res.count("1"), res.count("2"), res.count("3"),
              si.count("1"), si.count("2"), si.count("3"))
# test()

def sol2_1():
    for i in product("321", repeat=20):
        si = "0" + "1"*50 + "".join(i)
        res = g(si)
        if res.count("2") == 10:
            if res.count("1") == 20:
                print(res.count("3"), si, si.count("1"))


def sol2_2():
    for i in product("12", repeat=60):
        si = "0" + "3"*10 + "".join(i)
        res = g(si)
        if res.count("2") == 10:
            if res.count("1") == 20:
                print(res.count("3"), si, si.count("1"))
# sol22()

def sol1():
    for i in product("321", repeat=20):
        si = "".join(i)
        res = g("0" + "1"*40 + si)
        if res.count("2") == 10:
            if res.count("1") == 15:
                print("3:", res.count("3"), si.count("1") + 40, si)
