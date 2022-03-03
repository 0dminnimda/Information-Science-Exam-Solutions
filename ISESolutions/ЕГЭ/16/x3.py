def F(n):
    if n > 1:
        return F(n-1) + G(n-1)
    else: return n
def G(n):
    if n > 1:
        return G(n-1) + F(n)
    else: return n
print(G(5))