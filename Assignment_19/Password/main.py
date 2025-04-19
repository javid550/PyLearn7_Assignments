import sys
import random
import string
from functools import partial
from ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication , QMainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.length = 0
        self.password = ''
        self.characters = ""

        self.ui.Button_1.clicked.connect(self.generate)
        self.ui.rbt_1.clicked.connect(partial(self.mode , "Normal"))
        self.ui.rbt_2.clicked.connect(partial(self.mode , "Difficult"))
        self.ui.rbt_3.clicked.connect(partial(self.mode , "High_level"))

        
    def mode(self , a) :
        global mode
        mode = a


    def generate(self) :

        if mode == "Normal" :

            self.length = 8
            self.characters = ""
            self.characters += string.ascii_lowercase + string.ascii_uppercase

        elif mode == "Difficult" :

            self.length = 12
            self.characters = ""
            self.characters += string.ascii_lowercase + string.ascii_uppercase + string.digits

        elif mode == "High_level" :

            self.length = 16
            self.characters = ""
            self.characters += string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits


        self.password = ''.join(random.choice(self.characters) for i in range(self.length))
        self.ui.txt_box.setText(str(self.password))


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()