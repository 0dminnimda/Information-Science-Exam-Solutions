with open(r"ISESolutions\ЕГЭ\24\24.txt") as f:
    data = f.read()

parts = [len(i) for i in data.split("D")]

mx = -100
for a, b in zip(parts, parts[1:]):
    mx = max(mx, a + b + 1)

print(mx)

# c = 0
# mx = -100
# have = False
# for i in range(len(data)):
#     if a == "Д":
#         if have:
#             have = False
#             mx = max(c, mx)
#             c = 0
#         else:
#             have = True

#     c += 1
