# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(392, 491)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 210, 391, 22))
        font = QFont()
        font.setPointSize(7)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lineEdit.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.computer_btn = QPushButton(self.centralwidget)
        self.computer_btn.setObjectName(u"computer_btn")
        self.computer_btn.setGeometry(QRect(140, 70, 111, 111))
        font1 = QFont()
        font1.setPointSize(35)
        self.computer_btn.setFont(font1)
        self.computer_btn.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.user_btn = QPushButton(self.centralwidget)
        self.user_btn.setObjectName(u"user_btn")
        self.user_btn.setGeometry(QRect(140, 260, 111, 111))
        self.user_btn.setFont(font1)
        self.user_btn.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.paper_btn = QPushButton(self.centralwidget)
        self.paper_btn.setObjectName(u"paper_btn")
        self.paper_btn.setGeometry(QRect(140, 410, 111, 41))
        font2 = QFont()
        font2.setFamilies([u"Segoe Print"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.paper_btn.setFont(font2)
        self.paper_btn.setStyleSheet(u"background-color: rgb(170, 255, 127);")
        self.txt_win = QLineEdit(self.centralwidget)
        self.txt_win.setObjectName(u"txt_win")
        self.txt_win.setGeometry(QRect(10, 20, 113, 22))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.txt_win.setFont(font3)
        self.txt_win.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_draw = QLineEdit(self.centralwidget)
        self.txt_draw.setObjectName(u"txt_draw")
        self.txt_draw.setGeometry(QRect(140, 20, 113, 22))
        self.txt_draw.setFont(font3)
        self.txt_draw.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_lose = QLineEdit(self.centralwidget)
        self.txt_lose.setObjectName(u"txt_lose")
        self.txt_lose.setGeometry(QRect(270, 20, 113, 22))
        self.txt_lose.setFont(font3)
        self.txt_lose.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scissors_btn = QPushButton(self.centralwidget)
        self.scissors_btn.setObjectName(u"scissors_btn")
        self.scissors_btn.setGeometry(QRect(270, 410, 111, 41))
        self.scissors_btn.setFont(font2)
        self.scissors_btn.setStyleSheet(u"background-color: rgb(170, 255, 255);\n"
"background-color: rgb(170, 255, 127);")
        self.rock_btn = QPushButton(self.centralwidget)
        self.rock_btn.setObjectName(u"rock_btn")
        self.rock_btn.setGeometry(QRect(10, 410, 111, 41))
        self.rock_btn.setFont(font2)
        self.rock_btn.setStyleSheet(u"background-color: rgb(170, 255, 127);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 392, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Rock - Paper - Scissors", None))
        self.lineEdit.setText("")
        self.computer_btn.setText("")
        self.user_btn.setText("")
        self.paper_btn.setText(QCoreApplication.translate("MainWindow", u"Paper", None))
        self.txt_win.setText(QCoreApplication.translate("MainWindow", u"Wins :", None))
        self.txt_draw.setText(QCoreApplication.translate("MainWindow", u"Draws :", None))
        self.txt_lose.setText(QCoreApplication.translate("MainWindow", u"Loses :", None))
        self.scissors_btn.setText(QCoreApplication.translate("MainWindow", u"Scissors", None))
        self.rock_btn.setText(QCoreApplication.translate("MainWindow", u"Rock", None))
    # retranslateUi

