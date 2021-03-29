#!/usr/bin/python3.9
# -*- coding: utf-8 -*-

from itertools import product


def implication(a, b):
    return not (a and not b)


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


def validate(values1, values2):
    if len(values2) != len(values1):
        raise ValueError("different lengths")

    for v1, v2 in zip(values1, values2):
        if not (v1 is AnyBool or v2 is AnyBool):
            if v1 is not v2:
                return False
    return True

def cast_values(values, function=to_bool):
    values = list(values)

    for i, (inputs, out) in enumerate(values):
        inputs = (function(inp) for inp in inputs)
        values[i] = tuple(inputs), function(out)

    return tuple(values)


def measure_values(values):
    inputs_len = len(values[0][0])

    for inputs, _ in values[1:]:
        if len(inputs) != inputs_len:
            raise ValueError("different inputs lengths")

    return inputs_len


def find(values, function):

    # TODO: does not work
    successes = []

    inputs_len = measure_values(values)
    values = cast_values(values)

    for inputs in product(FT, repeat=inputs_len):
        result = function(*inputs)

        for given_inputs, output in values:
            if result == output:
                pass
                # print(validate(given_inputs, i), given_inputs, i)

            if result == output and validate(given_inputs, inputs):
                successes.append((*inputs, result))
                # values.remove([*given_inputs, output])
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
