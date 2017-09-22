from slider.float_slider import FloatSlider
from slider.slider_with_edit import SliderWithEdit

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

    int_widget = SliderWithEdit(int)
    int_widget.show()

    float_widget = SliderWithEdit(float)
    float_widget.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
