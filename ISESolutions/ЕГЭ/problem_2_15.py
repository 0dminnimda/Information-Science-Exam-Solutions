#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

from itertools import product


def implies(a, b):
    return b ** a  # not (a and not b)


FT = (0, 1)


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
        if other is AnyBoolCounter:
            return True
        # since AnyBoolType doesn't support integers,
        # 0 and 1 (False and True representations)
        # will be ignored

        # AnyBoolType only represents True and False
        return False

    def __hash__(self):
        return -1


class G:
    def __repr__(self):
        return "-"


a = G()

AnyBool = a  # AnyBoolType()


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

    condidates = set()

    inputs_len = measure_values(values)
    # values = cast_values(values)

    if len(names) != inputs_len:
        raise DIFF_LEN
    names = tuple(names)

    print("  " + "  ".join(names))

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


names = ("x", "y", "z", "w")  # [:2]


def f_1(x, y, z, w):
    return int(
        implies(x, y) and (x or not z) and (x != w))


def f_2(x, y, z, w):
    return int(
        ((y and not z) ** (x != y)) or (z and not w))


def f_3(x, y):
    return int(y ** x)


ans = ("z", "y", "w", "x")


def f_4(x, y, z, w):
    return (x and not y) or implies(not (z == w), (w and not x))


vals_1 = [
    [[True, True, AnyBool, True], True],
    [[AnyBool, True, AnyBool, AnyBool], True],
    [[AnyBool, True, AnyBool, True], True]],

vals_1 = [
    [[1, 1, a, 1], 1],
    [[a, 1, a, a], 1],
    [[a, 1, a, 1], 1]]

vals_2 = [
    [[0, 0, a, 0], 0],
    [[a, 0, a, 0], 0],
    [[a, a, a, 0], 0]]
#     w  z  -  y

vals_3 = [
    [[0, 1], 0]]

vals_4 = [
    [[0, a, 0, 0], 0],
    [[0, a, a, 0], 0],
    [[0, a, a, a], 0]]
#     w  z  y  x

# find(vals_4, f_4, names)

pass


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


# № 15
def div(n, m):
    return n % m == 0


def f2(a, x):
    return implies(
        not div(x, a),
        implies(div(x, 10),
                not div(x, 12)))
    # d_a = div(x, a)
    # return not d_a and (div(x, 10) and div(x, 12))


def f3(a, x):
    return div(70, a) and (
        implies(
            div(x, 28),
            implies(
                not div(x, a),
                not div(x, 21)
            )
        )
    )


def f4(a, x):
    return div(120, a) and implies(
        div(x, 36), implies(not div(x, a), not div(x, 45)))


func = f4

maximum = 120

suss = set()

for a in range(1, maximum+1)[::-1]:
    for x in range(1, 10**4):
        if func(a, x):
            suss.add(a)
        else:
            print(x)
            suss.discard(a)
            break
print(sorted(suss))
