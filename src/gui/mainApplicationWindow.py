import PySide6 as qt
import PySide6.QtCore as qtc
import PySide6.QtWidgets as qtw
import PySide6.QtGui as qtg
import sys
import random

# Prints PySide6 version and Qt version used to compile PySide6
print("PySide6:", qt.__version__)
print("PySide6.QTCore:", qtc.__version__)


class MyWidget(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = qtw.QPushButton("Click me!")
        self.text = qtw.QLabel("Hello World", alignment=qtc.Qt.AlignCenter)

        self.layout = qtw.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @qtc.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = qtw.QApplication([])

    widget = MyWidget()
    widget.resize(400, 400)
    widget.show()

    sys.exit(app.exec())
