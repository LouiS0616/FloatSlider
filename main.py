from slider.float_slider import FloatSlider

import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication


@pyqtSlot(float)
def tmp_slot(value: float) -> None:
    print(value)


def main():
    app = QApplication(sys.argv)

    slider = FloatSlider((0, 100))
    slider.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
