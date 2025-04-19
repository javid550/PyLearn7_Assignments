import sys
import random
from MainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication , QMainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.user_choice = ""
        self.computer_choice = ""

        
        self.win_score = self.lose_score = self.draw_score = 0
        self.ui.txt_win.setText("Wins : " + str(self.win_score))
        self.ui.txt_lose.setText("Loses : " + str(self.lose_score))
        self.ui.txt_draw.setText("Draw : " + str(self.draw_score))

        self.ui.computer_btn.clicked.connect(self.computer_move)

        self.ui.rock_btn.clicked.connect(self.rock)
        self.ui.paper_btn.clicked.connect(self.paper)
        self.ui.scissors_btn.clicked.connect(self.scissors)


    def rock(self) :
        self.computer_move()
        self.ui.user_btn.setText("👊🏻")
        self.win_check()

    def paper(self) :
        self.computer_move()
        self.ui.user_btn.setText("🖐🏻")
        self.win_check()

    def scissors(self) :
        self.computer_move()
        self.ui.user_btn.setText("✂")
        self.win_check()
            

    def computer_move(self) :

        self.random_choice = random.randint(1,3)

        if self.random_choice == 1 :
            self.computer_choice = self.ui.computer_btn.setText("👊🏻")
        elif self.random_choice == 2 :
            self.computer_choice = self.ui.computer_btn.setText("🖐🏻")
        elif self.random_choice == 3 :
            self.computer_choice = self.ui.computer_btn.setText("✂")


    def win_check(self) :

        if (self.ui.computer_btn.text() == self.ui.user_btn.text()) :

            self.draw_score += 1
            self.ui.txt_draw.setText("Draw : " + str(self.draw_score))


        elif (self.ui.user_btn.text() == "👊🏻" and self.ui.computer_btn.text() == "✂" or
              self.ui.user_btn.text() == "✂" and self.ui.computer_btn.text() == "🖐🏻" or
              self.ui.user_btn.text() == "🖐🏻" and self.ui.computer_btn.text() == "👊🏻") :
            
            self.win_score += 1
            self.ui.txt_win.setText("Wins : " + str(self.win_score))
                

        elif (self.ui.user_btn.text() == "✂" and self.ui.computer_btn.text() == "👊🏻" or
              self.ui.user_btn.text() == "🖐🏻" and self.ui.computer_btn.text() == "✂" or
              self.ui.user_btn.text() == "👊🏻" and self.ui.computer_btn.text() == "🖐🏻") :
            
            self.lose_score += 1
            self.ui.txt_lose.setText("Loses : " + str(self.lose_score))
                


app = QApplication(sys.argv)
window = MainWindow()

window.show()

app.exec()
