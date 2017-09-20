from float_slider import FloatSlider

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication


@pyqtSlot(float)
def tmp_slot(value: float) -> None:
    print(value)


def main():
    app = QApplication(sys.argv)
    slider = FloatSlider(val_range=(0.0, 100.0))
    slider.valueChanged.connect(tmp_slot)
    slider.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
