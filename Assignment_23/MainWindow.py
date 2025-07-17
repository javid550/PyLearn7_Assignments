<<<<<<< HEAD
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

from sudoku_grid import SudokuGrid

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(469, 499)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        MainWindow.setWindowIcon(icon)
        self.menu_newgame = QAction(MainWindow)
        self.menu_newgame.setObjectName(u"menu_newgame")
        self.menu_openfile = QAction(MainWindow)
        self.menu_openfile.setObjectName(u"menu_openfile")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        # self.gridLayout = QGridLayout(self.centralwidget)
        # self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayoutWidget = SudokuGrid(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 451, 451))
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.grid_layout = self.gridLayoutWidget.grid_layout

        # self.grid_layout_widget = SudokuGrid(self.centralwidget)
        # self.grid_layout = self.grid_layout_widget.grid_layout

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 469, 22))
        self.menunew_game = QMenu(self.menubar)
        self.menunew_game.setObjectName(u"menunew_game")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menunew_game.menuAction())
        self.menunew_game.addAction(self.menu_newgame)
        self.menunew_game.addAction(self.menu_openfile)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudoku Game", None))
        self.menu_newgame.setText(QCoreApplication.translate("MainWindow", u"New game", None))
        self.menu_openfile.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.menunew_game.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
    # retranslateUi

=======
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

from sudoku_grid import SudokuGrid

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(469, 499)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        MainWindow.setWindowIcon(icon)
        self.menu_newgame = QAction(MainWindow)
        self.menu_newgame.setObjectName(u"menu_newgame")
        self.menu_openfile = QAction(MainWindow)
        self.menu_openfile.setObjectName(u"menu_openfile")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        # self.gridLayout = QGridLayout(self.centralwidget)
        # self.gridLayout.setObjectName(u"gridLayout")

        self.gridLayoutWidget = SudokuGrid(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 451, 451))
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.grid_layout = self.gridLayoutWidget.grid_layout

        # self.grid_layout_widget = SudokuGrid(self.centralwidget)
        # self.grid_layout = self.grid_layout_widget.grid_layout

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 469, 22))
        self.menunew_game = QMenu(self.menubar)
        self.menunew_game.setObjectName(u"menunew_game")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menunew_game.menuAction())
        self.menunew_game.addAction(self.menu_newgame)
        self.menunew_game.addAction(self.menu_openfile)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudoku Game", None))
        self.menu_newgame.setText(QCoreApplication.translate("MainWindow", u"New game", None))
        self.menu_openfile.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.menunew_game.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
    # retranslateUi

>>>>>>> 6728bcf5d32f2f5a1539c3c4d5760f434ef7b9da
