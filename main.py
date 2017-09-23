from slider.float_slider import FloatSlider
from slider.float_slider_with_editor import FloatSliderWithEditor

from pprint import pprint
from inspect import getmembers

import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QSlider


@pyqtSlot(float)
def tmp_slot(value: float) -> None:
    print(value)


def main():
    app = QApplication(sys.argv)

    widget = FloatSliderWithEditor(float)
    widget.is_editable_by_text = False
    widget.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
