s = open(r"ISESolutions\ЕГЭ\24\24_19999.txt").read()

while "DDBB" in s or "BBDD" in s:
    s = s.replace("DDBB", "BBBB").replace("BBDD", "BBBB")
    print(0)

# print("DD" in s)

s = s.replace("BB", "0").replace("DD", "0")

# import re

# def f(m):
#     a = m.group(0)
#     # print(a, "0"*(len(a)-1))
#     # assert len(set(a)) == 1
#     print(a)
#     return "0"*(len(a)-1)

# s = "DDTBBBTDDDDBBBD"
# new = re.sub(r"(BB+|DD+)+", f, s)
# print(new)

# new = ""
# for a, b in zip(s, s[1:]):
#     if a in "DB":
#         if a == b:
#             new += "0"
#     else:
#         new += a

# if not (a in "DB" and a == b):
#     new += b

c = 1
mx = 0
for a, b in zip(s, s[1:]):
    if a == b == "0":
        c += 1
    else:
        c = 1
    mx = max(mx, c)

print(mx)

# 534 !-

# 317

# DDDBBBB
# DDDDDBB
