import sys
import random
from functools import partial
from MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication , QMainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.computer_number = random.randint(1,101)
        self.user_number = 0

        self.ui.Button.clicked.connect(self.check)

    def check(self) :

        self.user_number = int(self.ui.txtbox_1.text())

        # self.ui.txtbox_2.setText("")

        if self.computer_number == self.user_number :
            self.ui.txtbox_2.setText(" You win ----- ✨😍🎉")

        elif self.computer_number > self.user_number :
            self.ui.txtbox_2.setText("Incorrect ❌ , give a bigger number ⬆")

        elif self.computer_number < self.user_number < 101 :
            self.ui.txtbox_2.setText("Incorrect ❌ , give a smaller number ⬇ ")

        else :
            self.ui.txtbox_2.setText("Enter a number in range of 1 - 100 ❗")

        
app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()
