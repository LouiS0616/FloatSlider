from float_slider import FloatSlider

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout


@pyqtSlot(float)
def tmp_slot(value: float) -> None:
    print(value)


def main():
    pass

    app = QApplication(sys.argv)

    dialog = QDialog(None)
    layout = QVBoxLayout()

    for i in range(10):
        slider = FloatSlider(val_range=(0.0, 100.0 * (i + 1) / 10), ini_ratio=i / 10)
        slider.valueChanged.connect(tmp_slot)
        layout.addWidget(slider)

    dialog.setLayout(layout)
    dialog.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
