import PySide6
import PySide6.QtCore
import PySide6.QtWidgets
import PySide6.QtGui
import sys
import random

# Prints PySide6 version and Qt version used to compile PySide6
print("PySide6:", PySide6.__version__)
print("PySide6.QTCore:", PySide6.QtCore.__version__)


class MyWidget(PySide6.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = PySide6.QtWidgets.QPushButton("Click me!")
        self.text = PySide6.QtWidgets.QLabel(
            "Hello World", alignment=PySide6.QtCore.Qt.AlignCenter
        )

        self.layout = PySide6.QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @PySide6.QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = PySide6.QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec())
