from my_util.check_util import check_type

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QSlider, QLineEdit, QHBoxLayout
from .float_slider import FloatSlider


class SliderWithEditor(QWidget):
    def __init__(self, val_type: type, parent=None):
        QWidget.__init__(self, parent)

        check_type(val_type, type)
        if val_type is int:
            self._slider = QSlider(
                parent=self, orientation=Qt.Horizontal
            )
        else:
            self._slider = FloatSlider(
                parent=self, orientation=Qt.Horizontal
            )

        self._edit = QLineEdit(parent=self)

        layout = QHBoxLayout()
        layout.addWidget(self._slider)
        layout.addWidget(self._edit)
        self.setLayout(layout)
