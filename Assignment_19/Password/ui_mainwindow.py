# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
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
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(280, 362)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rbt_2 = QRadioButton(self.centralwidget)
        self.rbt_2.setObjectName(u"rbt_2")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(10)
        font.setBold(False)
        self.rbt_2.setFont(font)

        self.gridLayout.addWidget(self.rbt_2, 3, 0, 1, 1)

        self.Label = QLineEdit(self.centralwidget)
        self.Label.setObjectName(u"Label")
        font1 = QFont()
        font1.setFamilies([u"Segoe Print"])
        font1.setBold(True)
        self.Label.setFont(font1)
        self.Label.setFrame(False)
        self.Label.setReadOnly(True)

        self.gridLayout.addWidget(self.Label, 0, 0, 1, 1)

        self.txt_box = QLineEdit(self.centralwidget)
        self.txt_box.setObjectName(u"txt_box")

        self.gridLayout.addWidget(self.txt_box, 7, 0, 1, 1)

        self.Button_1 = QPushButton(self.centralwidget)
        self.Button_1.setObjectName(u"Button_1")
        font2 = QFont()
        font2.setFamilies([u"System"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.Button_1.setFont(font2)

        self.gridLayout.addWidget(self.Button_1, 6, 0, 1, 1)

        self.rbt_3 = QRadioButton(self.centralwidget)
        self.rbt_3.setObjectName(u"rbt_3")
        self.rbt_3.setFont(font)

        self.gridLayout.addWidget(self.rbt_3, 5, 0, 1, 1)

        self.rbt_1 = QRadioButton(self.centralwidget)
        self.rbt_1.setObjectName(u"rbt_1")
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(10)
        self.rbt_1.setFont(font3)

        self.gridLayout.addWidget(self.rbt_1, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 280, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password_Generator", None))
        self.rbt_2.setText(QCoreApplication.translate("MainWindow", u"Difficult", None))
        self.Label.setText(QCoreApplication.translate("MainWindow", u"Enter the level of difficulty :", None))
        self.Button_1.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.rbt_3.setText(QCoreApplication.translate("MainWindow", u"High level", None))
        self.rbt_1.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
    # retranslateUi

