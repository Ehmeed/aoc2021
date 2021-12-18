import functools
import math
from typing import Generator
from collections import namedtuple
from itertools import permutations, starmap

SFNumber = namedtuple('SFNumber', 'left right')
SFRegularNumber = namedtuple('SFRegularNumber', 'value')


def snailfish(in_data: Generator[str, None, None]) -> int:
    return _magnitude(functools.reduce(lambda a, b: _add(a, b), [_parse_number(eval(it)) for it in in_data]))


def snailfish_largest_magnitude(in_data: Generator[str, None, None]) -> int:
    return max(map(_magnitude, starmap(_add, permutations([_parse_number(eval(it)) for it in in_data], 2))))


def _magnitude(n) -> int:
    if type(n) is SFNumber:
        return 3 * _magnitude(n.left) + 2 * _magnitude(n.right)
    else:
        return n.value


def _parse_number(n):
    if type(n) is list:
        return SFNumber(_parse_number(n[0]), _parse_number(n[1]))
    else:
        return SFRegularNumber(n)


def _add(a, b):
    sf_number = SFNumber(a, b)
    while True:
        while True:
            prev_iteration_number = _tolist(sf_number)
            sf_number = _explode(sf_number, 0)[0]
            curr_iteration_number = _tolist(sf_number)
            if curr_iteration_number == prev_iteration_number:
                break
        prev_iteration_number = _tolist(sf_number)
        sf_number = _split(sf_number)[0]
        curr_iteration_number = _tolist(sf_number)
        if curr_iteration_number == prev_iteration_number:
            break
    return sf_number


def _explode(n, nesting_level=0):
    if type(n) is SFNumber and type(n.left) is SFRegularNumber and nesting_level >= 4:
        return SFRegularNumber(0), n.left.value, n.right.value
    elif type(n) is SFNumber:
        left_reduced, lladd, lradd = _explode(n.left, nesting_level + 1)
        if lradd >= 0:
            return SFNumber(left_reduced, _add_to_first_left(n.right, lradd)), lladd, 0
        right_reduced, rladd, rradd = _explode(n.right, nesting_level + 1)
        if rladd >= 0:
            return SFNumber(_add_to_first_right(left_reduced, rladd), right_reduced), 0, rradd
        return SFNumber(left_reduced, right_reduced), -1, -1
    else:
        return SFRegularNumber(n.value), -1, -1


def _split(n):
    if type(n) is SFNumber:
        left_split, did_split = _split(n.left)
        if did_split:
            return SFNumber(left_split, n.right), did_split
        right_split, did_split = _split(n.right)
        if did_split:
            return SFNumber(left_split, right_split), did_split
        return SFNumber(left_split, right_split), False
    elif n.value >= 10:
        return SFNumber(SFRegularNumber(math.floor(n.value / 2)), SFRegularNumber(math.ceil(n.value / 2))), True
    else:
        return SFRegularNumber(n.value), False


def _add_to_first_left(n, value):
    if type(n) is SFNumber:
        return SFNumber(_add_to_first_left(n.left, value), n.right)
    else:
        return SFRegularNumber(n.value + value)


def _add_to_first_right(n, value):
    if type(n) is SFNumber:
        return SFNumber(n.left, _add_to_first_right(n.right, value))
    else:
        return SFRegularNumber(n.value + value)


def _tolist(n):
    if type(n) is SFNumber:
        return [_tolist(n[0]), _tolist(n[1])]
    else:
        return n.value


SFNumber.__str__ = lambda it: _tolist(it).__str__()
