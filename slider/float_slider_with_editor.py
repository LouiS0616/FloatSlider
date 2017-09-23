from my_util import *

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QSlider, QLineEdit, QHBoxLayout, QSizePolicy
from PyQt5.QtGui import QFont
from .float_slider import FloatSlider


class FloatSliderWithEditor(QWidget):
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

        connect(self._slider.valueChanged, self.slider_changed)
        connect(self._editor.returnPressed, self.editor_return_pressed)

        layout = QHBoxLayout()
        layout.addWidget(self._slider)
        layout.addWidget(self._editor)
        self.setLayout(layout)

    @pyqtSlot(float)
    def slider_changed(self, value: float) -> None:
        self._editor.setText(str(value))

    @pyqtSlot()
    def editor_return_pressed(self) -> None:
        text = self._editor.text()

        if text == 'max' or text == 'min':
            text = str(self._slider.val_range[0 if text == 'min' else 1])
            self._editor.setText(text)

        try:
            self._slider.set_value(str_to_float(text))
        except ValueError:
            pass

    @property
    def slider(self):
        return self._slider

    @property
    def editor(self) -> QLineEdit:
        return self._editor
