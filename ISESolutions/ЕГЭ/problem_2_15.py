#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

def implication(a, b):
    return not (a and not b)


FT = ((False,), (True,))


def boolean_enumerator(number):
    if number <= 0:
        raise ValueError("number must graeter than 0")
    elif number == 1:
        return FT
    else:
        smaller_enumerator = boolean_enumerator(number - 1)
        result = []
        for i in FT:
            for j in smaller_enumerator:
                result.append(i + j)
        return tuple(result)


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

        # python source https://git.io/JYYqZ
        return int.__and__(self, other)

    # __ror__ is left for python
    def __or__(self, other):
        if other is False:
            return self
        if other is True:
            return True

        # python source https://git.io/JYYqa
        return int.__or__(self, other)

    # __rxor__ is left for python
    def __xor__(self, other):
        if type(other) is bool:
            return self

        # python source https://git.io/JYYqj
        return int.__xor__(self, other)

    # __ne__ is left for python
    def __eq__(self, other):
        if type(other) is bool:
            return True

        # since AnyBoolType doesn't support integers,
        # 0 and 1 (False and True representations)
        # will be ignored

        # AnyBoolType only represents True and False
        return False


AnyBool = AnyBoolType()


def validate(values1, values2):
    if len(values2) != len(values1):
        raise ValueError("different lengths")

    for v1, v2 in zip(values1, values2):
        if not (v1 is AnyBool or v2 is AnyBool):
            if v1 is not v2:
                return False
    return True


def find(values, function, number_of_values):
    # TODO: does not work
    successes = []

    for inputs in boolean_enumerator(number_of_values):
        result = function(*inputs)

        for v, r in values:
            if result == r:
                pass
                #print(validate(v, i), v, i)

            if r == result and validate(v, inputs):
                successes.append((*inputs, result))
                # values.remove([*v, r])
                # break

        if result:
            print([int(j) for j in inputs])

    print("\n".join([str(i) for i in successes]))


def f(x, y, z, w):
    return implication(x, y) and (x or not z) and (x != w)


ans = ("z", "y", "w", "x")


find(
    [
        [[True, True, AnyBool, True], True],
        [[AnyBool, True, AnyBool, AnyBool], True],
        [[AnyBool, True, AnyBool, True], True]],
    f, 4)


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
