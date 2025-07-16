import sys
import random
from functools import partial
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import *
from MainWindow import Ui_MainWindow
from sudoku import Sudoku

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.menu_newgame.triggered.connect(self.new_game)
        self.ui.menu_openfile.triggered.connect(self.open_file)

        self.line_edit = [[None for i in range(9)] for j in range(9)]
        
        puzzle = Sudoku(3).difficulty(0.5)
        for i in range(9):
            for j in range(9) :
                cell = QLineEdit()
                cell.setFixedSize(30 , 30)

                cell.setAlignment(Qt.AlignCenter)
                cell.setFont(QFont("Arial", 18))
                cell.setMaxLength(1)

                self.ui.grid_layout.addWidget(cell , i , j)

                cell.textChanged.connect(partial(self.validation , i , j))
                self.line_edit[i][j] = cell

        self.new_game()


    def open_file(self) :
        file_pass =  QFileDialog.getOpenFileName(self, "Open file ...")[0]
        print(file_pass)
        f = open(file_pass, "r")
        big_text = f.read()
        rows = big_text.split("\n")
        puzzle_board = [[None for i in range(9)] for j in range(9)]
        for i in range(len(rows)) :
            cells = rows[i].split(" ")
            for j in range(len(cells)) :
                puzzle_board[i][j] = int(cells[j])


        for i in range(9):
            for j in range(9) :
                self.line_edit[i][j].setReadOnly(False)
                if puzzle_board[i][j] != 0 :
                    self.line_edit[i][j].setText(str(puzzle_board[i][j]))
                    self.line_edit[i][j].setReadOnly(True)
                else :
                    self.line_edit[i][j].setText("")

    def new_game(self) :
        
        puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(0.5)

        for i in range(9):
            for j in range(9) :
                self.line_edit[i][j].setReadOnly(False)
                if puzzle.board[i][j] != None :
                    self.line_edit[i][j].setText(str(puzzle.board[i][j]))
                    self.line_edit[i][j].setReadOnly(True)
                else :
                    self.line_edit[i][j].setText("")

    def check(self) :

        board = []
        for i in range (9) :
            row = []
            for j in range(9) :
                text = self.line_edit[i][j].text()
                if text in ["1" , '2' , "3" , "4" , "5" , "6" , "7" , "8" , "9"]:
                    row.append(int(text))
                else :
                    row.append(0)

            board.append(row)

        def is_valid(group) :

            nums = [num for num in group if num != 0 ]
            return len(nums) == len(set(nums))
        
        # Check rows
        for i in range (9) :
            if not is_valid(board[i]) :
                print(f"invalid row {i+1}")
                return False
            
        # Check columns
        for j in range (9) :
            column = [board[i][j] for i in range(9)]

            if not is_valid(column) :
                print(f"invalid column {j+1}")
                return False
            
        # Check 3x3 boxes
        for box_row in range(0 , 9 , 3) :
            for box_col in range(0 , 9 , 3) :
                box = []
                for i in range(3) :
                    for j in range(3) :
                        box.append(board[box_row + i][box_col + j])

                if not is_valid(box) :
                    print(f"invalid 3x3 box starting at ({box_row+1},{box_col+1})")
                    return False
                
        return True



    
    def validation(self, i, j , text) :
        # text = self.line_edit[i][j].text()
        if text not in ["1" , '2' , "3" , "4" , "5" , "6" , "7" , "8" , "9"]:
            self.line_edit[i][j].setText("")
            

        if self.check() == True :
            self.line_edit[i][j].setStyleSheet("background-color: rgb(255, 255, 255);") 
            print("Sudoku board is valid ✅")
        else : 
            self.line_edit[i][j].setStyleSheet("background-color: rgb(255, 80, 80);")
            QMessageBox.critical(self, "Error", "Invalid number , change it please :( ")

        for i in range(9) :
            for j in range(9) :
                if self.line_edit[i][j].text().strip() == "" :
                    return False

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Congratulation 🎉")
        msg_box.setText("You filled all of the blocks successfully. 😍")
        msg_box.exec()


if __name__ == "__main__" :
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    # app.exec()
    sys.exit(app.exec())