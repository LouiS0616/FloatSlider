from MyPyUtil.my_util import *

from enum import Enum

from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QSlider


class FloatSlider(QWidget):
    valueChanged = pyqtSignal(float)

    class EmitType(Enum):
        VALUE_CHANGED = 0
        VALUE_DECIDED = 1

    def __init__(self, val_range: tuple=(0., 100.), ini_value: float=None, ini_ratio: float=.5,
                 orientation: Qt.Orientation=Qt.Vertical, parent: QWidget=None,
                 *, s_digit: int=2, emit_type: EmitType=EmitType.VALUE_DECIDED):

        QWidget.__init__(self, parent)
        self._slider = QSlider(parent=parent if parent is not None else self)
        self._s_digit = check_value(s_digit, cond=lambda x: x > 0)

        check_value(val_range, is_range)
        self._slider.setRange(*self._to_int(val_range))
        self._val_range = val_range

        if ini_value is None:
            check_value(ini_ratio, is_ratio)
            self.set_value_by_ratio(ini_ratio)
        else:
            self.set_value(ini_value)
        self._initial_value = self.value()

        self.setLayout(SingleLayout(self._slider))
        self._slider.setOrientation(check_type(orientation, Qt.Orientation))
        self._connect(emit_type)

    def sizeHint(self):
        return self._slider.sizeHint()

    def set_range(self, *arg_range) -> bool:
        arg_range = (
            self._val_range[0] if arg_range[0] is None else arg_range[0],
            self._val_range[1] if arg_range[1] is None else arg_range[1]
        )

        if is_range(arg_range):
            self._val_range = arg_range
            self._slider.setRange(
                *try_to_map(self._to_int, arg_range)
            )
            return True
        else:
            return False

    def set_max(self, max_limit) -> bool:
        return self.set_range(None, max_limit)

    def set_min(self, min_limit) -> bool:
        return self.set_range(min_limit, None)

    def initial_value(self) -> float:
        return self._initial_value

    def set_initial_value(self, value: float) -> bool:
        if in_range(value, self._val_range):
            self._initial_value = value
            return True
        return False

    @property
    def emit_type(self) -> EmitType:
        return self._emit_type

    @emit_type.setter
    def emit_type(self, emit_type: EmitType) -> None:
        self._connect(emit_type)

    @property
    def val_range(self) -> tuple:
        return self._val_range

    def value(self) -> float:
        return self._to_float(self._slider.value())

    def set_value(self, value: float):
        try:
            check_value(value, cond=lambda x: in_range(x, self._val_range))
        except ValueError:
            return
        value = round(value, self._s_digit)
        self._slider.setValue(self._to_int(value))
        self.valueChanged.emit(value)

    def value_by_ratio(self) -> float:
        return compute_ratio_by_value_and_range(self.value(), self._val_range)

    def set_value_by_ratio(self, ratio: float):
        ratio = max(0.0, min(1.0, ratio))
        self.set_value(compute_value_by_ratio_and_range(ratio, self._val_range))

    def _to_float(self, value):
        return try_to_map(lambda x: x / (10**self._s_digit), value)

    def _to_int(self, value):
        return try_to_map(lambda x: x * (10**self._s_digit), value)

    def _connect(self, emit_type: EmitType) -> None:
        check_type(emit_type, FloatSlider.EmitType, 'to assign emit_type')

        if emit_type == FloatSlider.EmitType.VALUE_CHANGED:
            try_to_disconnect(self._slider.sliderReleased, self._slot_slider_released)
            connect(self._slider.valueChanged, self._slot_value_changed)
        else:
            try_to_disconnect(self._slider.valueChanged, self._slot_value_changed)
            connect(self._slider.sliderReleased, self._slot_slider_released)

    @pyqtSlot()
    def _slot_slider_released(self) -> None:
        self._slot_value_changed(self._slider.value())

    @pyqtSlot(int)
    def _slot_value_changed(self, value: int) -> None:
        self.valueChanged.emit(self._to_float(value))
