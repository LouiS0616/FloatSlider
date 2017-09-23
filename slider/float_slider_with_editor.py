from my_util import *

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QSlider, QLineEdit, QHBoxLayout
from .float_slider import FloatSlider


class FloatSliderWithEditor(QWidget):
    def __init__(self, val_type: type, parent=None):
        QWidget.__init__(self, parent)

        self._val_type = check_type(val_type, type)
        if val_type is int:
            self._slider = QSlider(
                parent=self, orientation=Qt.Horizontal
            )
        else:
            self._slider = FloatSlider(
                parent=self, orientation=Qt.Horizontal
            )

        self._editor = QLineEdit(parent=self)

        layout = QHBoxLayout()
        layout.addWidget(self._slider)
        layout.addWidget(self._editor)
        self.setLayout(layout)

    @property
    def slider(self):
        return self._slider

    @property
    def editor(self) -> QLineEdit:
        return self._editor
