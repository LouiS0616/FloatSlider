from typing import Callable
from .check_util import check_type
from PyQt5.QtWidgets import QWidget, QHBoxLayout


def try_to_disconnect(signal: Callable, slot: Callable) -> bool:
    try:
        signal.disconnect(slot)
        return True
    except TypeError:
        return False


def connect(signal: Callable, slot: Callable) -> None:
    signal.connect(slot)


class SingleLayout(QHBoxLayout):
    def __init__(self, widget: QWidget):
        QHBoxLayout.__init__(self)
        self.setContentsMargins(0, 0, 0, 0)
        self.addWidget(widget)
