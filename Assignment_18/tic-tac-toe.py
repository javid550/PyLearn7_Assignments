import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication , QMessageBox
from PySide6.QtUiTools import QUiLoader


app = QApplication(sys.argv)

loader = QUiLoader()
main_window = loader.load("session 18\Tic Tac Toa\main.ui")
main_window.show()


def about() :
    msg_box = QMessageBox(windowTitle = "TIC-TAC-TOA ✖⭕" ,
                          text="This game is double player game ! \n To winning the match you should align three of your pieces . 😃")
    msg_box.exec()

def clear() :
    for i in range(3) :
        for j in range(3) :
            Buttons[i][j].setText("")
            Buttons[i][j].setStyleSheet("")

def New_Game() :
    global win_score
    global lose_score
    global draw_score

    win_score = lose_score = draw_score = 0
    main_window.win.setText("Wins : " + str(win_score))
    main_window.lose.setText("Loses : " + str(lose_score))
    main_window.draw.setText("Draw : " + str(draw_score))

    clear()

def check() :
    global win_score
    global lose_score
    global draw_score
    global state
    state = "false"
    
    for i in range(3) :
        if (   Buttons[i][0].text() == "✖" and Buttons[i][1].text() == "✖" and Buttons[i][2].text() == "✖" 
            or Buttons[0][i].text() == "✖" and Buttons[1][i].text() == "✖" and Buttons[2][i].text() == "✖" 
            or Buttons[0][2].text() == "✖" and Buttons[1][1].text() == "✖" and Buttons[2][0].text() == "✖"
            or Buttons[0][0].text() == "✖" and Buttons[1][1].text() == "✖" and Buttons[2][2].text() == "✖" ) :

            msg_box = QMessageBox(windowTitle = "Game result 😀" ,text="You WIN ---> 😍🎉")
            msg_box.exec()
            win_score += 1
            main_window.win.setText("Wins : " + str(win_score))

            clear()

            state = "true"

        elif ( Buttons[i][0].text() == "O" and Buttons[i][1].text() == "O" and Buttons[i][2].text() == "O" 
            or Buttons[0][i].text() == "O" and Buttons[1][i].text() == "O" and Buttons[2][i].text() == "O" 
            or Buttons[0][2].text() == "O" and Buttons[1][1].text() == "O" and Buttons[2][0].text() == "O"
            or Buttons[0][0].text() == "O" and Buttons[1][1].text() == "O" and Buttons[2][2].text() == "O" ) :

            msg_box = QMessageBox(windowTitle = "Game result 😀" , text="You LOSE ----> 🙁")
            msg_box.exec()
            lose_score += 1
            main_window.lose.setText("Loses : " + str(lose_score))

            clear()

            state = "true"

        elif (   Buttons[0][0].text() != "" and Buttons[1][0].text() != "" and Buttons[2][0].text() != "" 
             and Buttons[0][1].text() != "" and Buttons[1][1].text() != "" and Buttons[2][1].text() != "" 
             and Buttons[0][2].text() != "" and Buttons[1][2].text() != "" and Buttons[2][2].text() != "" ) :
              
            msg_box = QMessageBox(windowTitle = "Game result 😀" , text="You're DRAW ---> 🙄")
            msg_box.exec()
            draw_score += 1
            main_window.draw.setText("Draw : " + str(draw_score))

            clear()

            state = "true"
        
def mode(a) :
    global mode
    mode = a

player = 1

def play(row , col) :
    global player
    global state
    # global Buttons

    if mode == "player_vs_player" :

        if player == 1 and Buttons[row][col].text() == "" :
            Buttons[row][col].setText("✖")
            Buttons[row][col].setStyleSheet("color: red ; background-color: lightblue ;")
            player = 2 

        elif player == 2 :
            Buttons[row][col].setText("O")
            Buttons[row][col].setStyleSheet("color: blue ; background-color: lightblue ;")
            player = 1

        check()

    if mode == "player_vs_computer" :
        if player == 1 and Buttons[row][col].text() == "" :
            Buttons[row][col].setText("✖")
            Buttons[row][col].setStyleSheet("color: red ; background-color: lightblue ;")
            Pc_move()

def Pc_move() :
    global player 

    empty = [(i,j) for i in range(3) for j in range(3) if Buttons[i][j].text() == ""]
    if empty :
        row , col = random.choice(empty)
        Buttons[row][col].setText("O")
        Buttons[row][col].setStyleSheet("color: blue ; background-color: lightblue ;")
        player = 1
        check()

Buttons = [[main_window.Button_9 , main_window.Button_8 , main_window.Button_7] ,
           [main_window.Button_6 , main_window.Button_5 , main_window.Button_4] , 
           [main_window.Button_3 , main_window.Button_2 , main_window.Button_1]]

for i in range(3):
    for j in range(3):
        Buttons[i][j].clicked.connect(partial(play , i , j))

New_Game()

main_window.about.clicked.connect(about)
main_window.reset.clicked.connect(New_Game)
main_window.pc_rbtn.clicked.connect(partial(mode , "player_vs_computer"))
main_window.player_rbtn.clicked.connect(partial(mode , "player_vs_player"))


app.exec()