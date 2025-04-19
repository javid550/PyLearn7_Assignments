# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(256, 408)
        MainWindow.setStyleSheet(u"background-color: rgb(226, 226, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txt_box = QLineEdit(self.centralwidget)
        self.txt_box.setObjectName(u"txt_box")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setBold(True)
        self.txt_box.setFont(font)
        self.txt_box.setFrame(False)
        self.txt_box.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_box, 0, 0, 1, 3)

        self.txtbox_1 = QLineEdit(self.centralwidget)
        self.txtbox_1.setObjectName(u"txtbox_1")
        self.txtbox_1.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.txtbox_1, 1, 0, 1, 2)

        self.Button = QPushButton(self.centralwidget)
        self.Button.setObjectName(u"Button")
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        font1.setBold(True)
        self.Button.setFont(font1)
        self.Button.setStyleSheet(u"background-color: rgb(250, 170, 0);")

        self.gridLayout.addWidget(self.Button, 1, 2, 1, 1)

        self.txtbox_2 = QLineEdit(self.centralwidget)
        self.txtbox_2.setObjectName(u"txtbox_2")
        self.txtbox_2.setReadOnly(True)

        self.gridLayout.addWidget(self.txtbox_2, 2, 0, 1, 3)

        self.txtbox_3 = QLineEdit(self.centralwidget)
        self.txtbox_3.setObjectName(u"txtbox_3")
        self.txtbox_3.setFrame(False)
        self.txtbox_3.setReadOnly(True)

        self.gridLayout.addWidget(self.txtbox_3, 3, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 256, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Geussing", None))
        self.txt_box.setText(QCoreApplication.translate("MainWindow", u"Enter a number between 1 - 100  :", None))
        self.Button.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.txtbox_3.setText("")
    # retranslateUi

