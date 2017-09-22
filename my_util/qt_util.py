from typing import Callable
from .check_util import check_type
from PyQt5.QtWidgets import QWidget


def try_to_disconnect(signal: Callable, slot: Callable) -> bool:
    try:
        signal.disconnect(slot)
        return True
    except TypeError:
        return False


def connect(signal: Callable, slot: Callable) -> None:
    signal.connect(slot)
