# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(200, 110, 249, 88))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.lblOutput = QLabel(self.widget)
        self.lblOutput.setObjectName(u"lblOutput")

        self.gridLayout.addWidget(self.lblOutput, 2, 0, 1, 3)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.lblTitle = QLabel(self.widget)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lblTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 3)

        self.btnSubmit = QPushButton(self.widget)
        self.btnSubmit.setObjectName(u"btnSubmit")
        self.btnSubmit.setFlat(False)

        self.gridLayout.addWidget(self.btnSubmit, 1, 2, 1, 1)

        self.lblInput = QLabel(self.widget)
        self.lblInput.setObjectName(u"lblInput")

        self.gridLayout.addWidget(self.lblInput, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblOutput.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.lblTitle.setText(QCoreApplication.translate("MainWindow", u"Text Input", None))
        self.btnSubmit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.lblInput.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
    # retranslateUi

