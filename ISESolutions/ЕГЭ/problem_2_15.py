#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

from itertools import product


def implication(a, b):
    return b ** a  # not (a and not b)


FT = (False, True)


class AnyBoolType:
    __slots__ = ()

    def __repr__(self):
        return "AnyBool"

    # __rand__ is left for python
    def __and__(self, other):
        if other is False:
            return False
        if other is True:
            return self
        if other is self:
            return self

        # python source https://git.io/JYYqZ
        return int.__and__(self, other)

    # __ror__ is left for python
    def __or__(self, other):
        if other is False:
            return self
        if other is True:
            return True
        if other is self:
            return self

        # python source https://git.io/JYYqa
        return int.__or__(self, other)

    # __rxor__ is left for python
    def __xor__(self, other):
        if type(other) is bool:
            return self
        if other is self:
            return self

        # python source https://git.io/JYYqj
        return int.__xor__(self, other)

    # __ne__ is left for python
    def __eq__(self, other):
        if type(other) is bool:
            return True
        if other is self:
            return True
        # since AnyBoolType doesn't support integers,
        # 0 and 1 (False and True representations)
        # will be ignored

        # AnyBoolType only represents True and False
        return False


AnyBool = AnyBoolType()


def to_bool(value):
    if value is AnyBool:
        return value
    return bool(value)


def to_int(value):
    if value is AnyBool:
        return value
    return int(value)


def cast_values(values, function=to_int):
    values = list(values)

    for i, (inputs, out) in enumerate(values):
        inputs = (function(inp) for inp in inputs)
        values[i] = tuple(inputs), function(out)

    return tuple(values)


DIFF_LEN = ValueError("different inputs lengths")


def measure_values(values):
    inputs_len = len(values[0][0])

    for inputs, _ in values[1:]:
        if len(inputs) != inputs_len:
            raise DIFF_LEN

    return inputs_len


def iscondidate(inps, given_inps):
    if (inps.count(0) < given_inps.count(0)
            or inps.count(1) < given_inps.count(1)):
        return False

    return True


def find(values, function, names):
    """
    Args:
        values (Iterable[Iterable[Union[Iterable[Any], Any]]):
        [
            [
                [*inputs],
                function_out
            ],
        ]
    """

    # TODO: does not work
    condidates = set()

    inputs_len = measure_values(values)
    # values = cast_values(values)

    if len(names) != inputs_len:
        raise DIFF_LEN
    names = tuple(names)

    print(names)

    for inputs in product(FT, repeat=inputs_len):
        result = function(*inputs)

        for given_inputs, output in values:
            if result == output:
                if iscondidate(inputs, given_inputs):
                    condidates.add((inputs, result))
                # print(given_inputs == i, given_inputs, i)

        #     if result == output and given_inputs == inputs:
        #         print(given_inputs)
        #         successes.append((
        #             [int(j) for j in inputs],
        #             int(result)))
        #         # values.remove([*given_inputs, output])
        #         # break

        # if result == output:
        #     print([int(j) for j in inputs])
        #     pass

    print("\n".join([str(i) for i in condidates]))


names = ("x", "y", "z", "w")[:2]


def f_1(x, y, z, w):
    return int(
        implication(x, y) and (x or not z) and (x != w))


def f_2(x, y, z, w):
    return int(
        ((y and not z) ** (x != y)) or (z and not w))

def f_3(x, y):
    return int(y ** x)

ans = ("z", "y", "w", "x")


vals = [
    [[True, True, AnyBool, True], True],
    [[AnyBool, True, AnyBool, AnyBool], True],
    [[AnyBool, True, AnyBool, True], True]],

vals = [
    [[1, 1, a, 1], 1],
    [[a, 1, a, a], 1],
    [[a, 1, a, 1], 1]]

vals = [
    [[0, 0, a, 0], 0],
    [[a, 0, a, 0], 0],
    [[a, a, a, 0], 0]]
#     w  z  -  y


vals = [
    [[0, 1], 0]]

find(vals, f_3, names)

breakpoint()


"""
Algorithm

values
    v  - - - -
    0  0 1 1 0
    1  0 1 1 1
    2  1 0 0 0
    3  1 0 1 0
    ----------
    l  x y z w
    0  1 1 1 -
    1  - 1 - -
    2  1 1 - -

(iscondidate)
    l|v 0 1 2 3
    0   n y n n
    1   y y y y
    2   y y n y

l0 shoud be v1 =>
    x y z w    w - - -
    1 1 1 - >> 0 1 1 1

(w - - -)
    with new knoladge
    new comparasion (old no-s stays):
    no new info, all w-s is "-"

remove l0, v1, w
    l|v 0 2 3
    1   y y y
    2   y n y
    ---------
    v  - - -
    0  1 1 0
    2  0 0 0
    3  0 1 0
    --------
    l  x y z
    1  - 1 -
    2  1 1 -

(iscondidate):
    l|v 0 2 3
    1   y n y
    2   y n n

l2 shoud be v0 =>
    x y z    - - z
    1 1 - >> 1 1 0

(- - z)
    with new knoladge
    new comparasion (old no-s stays):
    no new info, all z-s is "-"

remove l2, v0, z
    l|v 2 3
    1   n y
    -------
    v  - -
    2  0 0
    3  0 1
    ------
    l  x y
    1  - 1

l1 shoud be v3 =>
    x y    x -
    - 1 >> 0 1

(x -)
    with new knoladge
    new comparasion (old no-s stays):
    no new info, all x-s is "-"

remove l1, v3, x
    l|v 2
    -------
    v  -
    2  0
    ------
    l  y

y is on the remaining place (y)

ans: (w x y z)!
"""

"""
values
    v  - - -
    0  1 1 1
    2  0 0 0
    3  0 1 0
    --------
    l  x y z
    1  - 1 -
    2  1 1 -

(iscondidate):
    l|v 0 2 3
    1   y n y
    2   y n n

l2 shoud be v0 =>
    x y z    - - -
    1 1 - >> 1 1 1
    (no new info about v-s)

remove l2, v0
    l|v 2 3
    1   n y
    --------
    v  - - -
    2  0 0 0
    3  0 1 0
    --------
    l  x y z
    1  - 1 -

l1 shoud be v3 =>
    x y z    - y -
    - 1 - >> 0 1 0

(- y -)
    with new knoladge
    new comparasion (old no-s stays):
    v2 does not match

...
"""

"""
values
    v  - - -
    2  0 0 0
    3  0 1 0
    4  1 1 0
    --------
    l  x y z
    1  - 1 -
    4  0 - 0
    5  1 1 -

(iscondidate):
    l|v 2 3 4
    1   n y y
    4   y y n
    5   n n y

l5 shoud be v4 =>
    x y z    - - z
    1 1 - >> 1 1 0

remove l5, v4, z
    l|v 2 3
    1   n y
    4   y y
    -------
    v  - -
    2  0 0
    3  0 1
    ------
    l  x y
    1  - 1
    4  0 -
    5  1 1

l1 shoud be v3 =>
    x y z    - y -
    - 1 - >> 0 1 0

remove l1, v3
    l|v 2 3
    1   n y
    --------
    v  - - -
    2  0 0 0
    3  0 1 0
    4  1 1 0
    --------
    l  x y z
    1  - 1 -
    4  0 - 0
    5  1 1 -

(- y -)
    with new knoladge
    new comparasion (old no-s stays):
    v: 2 4  l: 4 5
    y  0 1     - 1

l4's y shoud be 0 =>
    l  x y z
    1  - 1 -
    4  0 0 0
    5  1 1 -

...
"""


def c(t):
    tl = len(t)
    max_len = len(str((AnyBool,)*tl))
    for inputs in product(FT+(AnyBool,), repeat=tl):
        # if not iscondidate(inputs, t):
        #     continue

        print(f"{inputs!s: <{max_len}}",
              "-",
              "yes" if iscondidate(inputs, t) else "no ",
              "|",
              inputs.count(0),
              inputs.count(1),
              inputs.count(AnyBoolCounter),
              "|",
              inputs.count(False),
              inputs.count(True),
              inputs.count(AnyBoolCounter))

    # print()

    # for inputs in product(FT+(AnyBool,), repeat=len(t)):
    #     print(inputs, inputs.count(False),
    #           inputs.count(True),
    #           inputs.count(AnyBoolCounter))


c([])
c([0])
c([0, 1])
c([0, 1, 0])

# 15
def divisible(n, m):
    return n % m == 0


def f2(a, x):
    return implication(not divisible(x, a), implication(divisible(x, 10), not divisible(x, 12)))
    # d_a = divisible(x, a)
     #return not d_a and (divisible(x, 10) and divisible(x, 12))


maximum = 50

# a = 36  # 6

for a in range(maximum-1, 0, -1):
    for x in range(1, 10**5):
        if not f2(a, x):
            print(x, "not", a)
            break
