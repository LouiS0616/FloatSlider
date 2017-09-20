from typing import Callable
from .check_util import check_value, is_ratio, is_range, is_iterable


def compute_diff(arg1: float, arg2: float):
    return abs(arg1 - arg2)


def compute_value_by_ratio_and_range(ratio: float, val_range: tuple) -> float:
    check_value(ratio, is_ratio)
    check_value(val_range, is_range)
    value = compute_diff(*val_range) * ratio + val_range[0]
    return value


def try_to_map(func: Callable, value):
    if is_iterable(value):
        return type(value)(map(func, value))
    else:
        return func(value)
