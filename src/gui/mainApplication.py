import PySide6
import PySide6.QtCore
import PySide6.QtWidgets
import PySide6.QtGui


# Prints PySide6 version and Qt version used to compile PySide6
print("PySide6:", PySide6.__version__)
print("PySide6.QTCore:", PySide6.QtCore.__version__)


class MainWindow(PySide6.QtWidgets.QWidget):
    pass


if __name__ == "__main__":
    app = PySide6.QtWidgets.QApplication([])

    window = MainWindow()
    window.resize(400, 600)
    window.show()

    sys.exit(app.exec())
