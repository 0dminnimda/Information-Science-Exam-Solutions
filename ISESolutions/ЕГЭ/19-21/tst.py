def out(step):
    return step%2 == mx%2


##############################
# from math import ceil


# def our(step):
#     return step%2 == mx%2


# def win(a, b, step):
#     if a + b <= 20:
#         return our(step)
#     if step == mx:
#         return 0
#     step += 1
#     h = [win(a-1, b, step), win(a, b-1, step),
#          win(ceil(a/2), b, step), win(a, ceil(b/2), step)]
#     return any(h) if our(step) else all(h)


# for b in range(11, 1000):
#     for mx in range(1, 5):
#         if win(10, b, 0):
#             if mx == 4: print(b, mx)
#             break


################################
# def our(step):
#     return step % 2 == mx % 2


# def win(a, b, step):
#     if a + b >= 74:
#         return our(step)
#     if step == mx:
#         return 0
#     step += 1
#     h = [win(a+2, b, step), win(a*2, b, step),
#          win(a, b+2, step), win(a, b*2, step)]
#     return any(h) if our(step) else all(h)


# for b in range(1, 67):
#     for mx in range(1, 5):
#         if win(7, b, 0):
#             if mx == 4: print(b, mx)
#             break


############################
# def out(step):
#     return step%2 == mx%2


# def win(s, step):
#     if s >= 43:
#         if s <= 72:
#             return out(step)
#         else:
#             return not out(step)

#     if step == mx:
#         return 0

#     step += 1
#     h = [win(s, step) for s in (s+1, s*2, s*3)]
#     return any(h) if out(step) else all(h)


# for s in range(1, 43):
#     for mx in range(1, 5):
#         if win(s, 0):
#             if mx == 3: print(s, mx)
#             break


#############################
# def our(step):
#     return step % 2 == mx % 2


# def win(s, step):
#     if s >= 30:
#         return our(step)
#     if step == mx:
#         return 0
#     step += 1
#     h = [win(s, step) for s in (s+2, s+3, s*2)]
#     return any(h) if our(step) else all(h)


# for s in range(1, 30):
#     for mx in range(1, 5):
#         if win(s, 0):
#             if mx == 4:
#                 print(s, mx)
#             break
