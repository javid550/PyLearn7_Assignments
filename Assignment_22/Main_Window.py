# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGridLayout, QHBoxLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(297, 301)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentPageSetup))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.verticalLayout.addLayout(self.gl_tasks)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_NewTask = QPushButton(self.centralwidget)
        self.btn_NewTask.setObjectName(u"btn_NewTask")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_NewTask.sizePolicy().hasHeightForWidth())
        self.btn_NewTask.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(15)
        font.setBold(True)
        self.btn_NewTask.setFont(font)
        self.btn_NewTask.setStyleSheet(u"background-color: rgb(0, 85, 255);")

        self.horizontalLayout.addWidget(self.btn_NewTask)

        self.textbox_NewTask = QLineEdit(self.centralwidget)
        self.textbox_NewTask.setObjectName(u"textbox_NewTask")
        self.textbox_NewTask.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.textbox_NewTask)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.DateTime = QDateTimeEdit(self.centralwidget)
        self.DateTime.setObjectName(u"DateTime")

        self.verticalLayout.addWidget(self.DateTime)

        self.tb_newtask_description = QTextEdit(self.centralwidget)
        self.tb_newtask_description.setObjectName(u"tb_newtask_description")
        self.tb_newtask_description.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout.addWidget(self.tb_newtask_description)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 297, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToDoList ", None))
        self.btn_NewTask.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

