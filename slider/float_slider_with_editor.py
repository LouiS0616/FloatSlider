from MyPyUtil.my_util import *

from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QFont
from .float_slider import FloatSlider


class FloatSliderWithEditor(QWidget):
    valueChanged = pyqtSignal(float)

    def __init__(self, float_slider: FloatSlider=None, parent=None):
        QWidget.__init__(self, parent)

        if isinstance(float_slider, FloatSlider):
            self._slider = float_slider
        else:
            self._slider = FloatSlider(
                parent=self, orientation=Qt.Horizontal
            )
        set_horizontal_ratio(self._slider, 2)

        self._editor = QLineEdit(str(self._slider.value()), parent=self)
        self._editor.setAlignment(Qt.AlignRight)
        self._editor.setFont(QFont('Consolas'))
        set_horizontal_ratio(self._editor, 1)

        connect(self._slider.valueChanged, self._slider_changed)
        connect(self._editor.returnPressed, self._editor_return_pressed)

        layout = QHBoxLayout()
        layout.addWidget(self._slider)
        layout.addWidget(self._editor)
        self.setLayout(layout)

    @property
    def slider(self) -> FloatSlider:
        return self._slider

    @property
    def editor(self) -> QLineEdit:
        return self._editor

    @pyqtSlot(float)
    def _slider_changed(self, value: float) -> None:
        self._editor.setText(str(value))
        self.valueChanged.emit(value)

    @pyqtSlot()
    def _editor_return_pressed(self) -> None:
        text = self._editor.text()

        # input is 'max=float'
        search_result = search_indication_to_set_float_value('max', text)
        if search_result:
            if self._slider.set_max(float(search_result.group(0))):
                self._set_slider_value(self._slider.val_range[1])
            return

        # input is 'min=float'
        search_result = search_indication_to_set_float_value('min', text)
        if search_result:
            if self._slider.set_min(float(search_result.group(0))):
                self._set_slider_value(self._slider.val_range[0])
            return

        """
        # input is 'range'
        if text == 'range':
            self._editor.setText(
                ', '.join(map(str, self._slider.val_range))
            )
            return
        """

        # input is 'max'
        # input is 'min'
        if text == 'max' or text == 'min':
            self._set_slider_value(
                self._slider.val_range[0 if text == 'min' else 1]
            )
            return

        # input is value
        try:
            self._set_slider_value(
                str_to_float(text)
            )
        except ValueError:
            pass

    def _set_slider_value(self, value: float) -> None:
        self._slider.set_value(value)
