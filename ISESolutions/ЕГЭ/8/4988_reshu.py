from itertools import product

c = len(list(product("-.", repeat=3))) + len(list(product("-.", repeat=4))) + len(list(product("-.", repeat=5)))

print(c)