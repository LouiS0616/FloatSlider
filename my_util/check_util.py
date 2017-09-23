from typing import Callable

numeric = (int, float)


def check_type(instance, cor_type, purpose: str=''):
    if isinstance(instance, cor_type):
        return instance
    else:
        raise TypeError('Use ' + cor_type.__name__ + ' ' + purpose)


def check_value(value, cond: Callable):
    if cond(value):
        return value
    else:
        raise ValueError(str(value) + ' is not suited value.')


def str_to_float(text: str) -> float:
    check_type(text, str)
    try:
        return float(text)
    except ValueError:
        raise ValueError(text + ' cannot be interpreted as float.')


def is_range(value: tuple) -> bool:
    try:
        check_value(value, cond=lambda t: len(t) == 2 and t[0] < t[1])
        return True
    except ValueError:
        return False


def in_range(value: numeric, val_range: tuple):
    check_value(val_range, is_range)
    return val_range[0] <= value <= val_range[1]


def is_ratio(value: float):
    return in_range(value, (0., 1.))


def is_iterable(value) -> bool:
    try:
        for _ in value:
            break
        return True
    except TypeError:
        return False
