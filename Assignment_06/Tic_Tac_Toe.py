import pyfiglet
import colorama
import random
import time

title = pyfiglet.figlet_format("Tic Tac To" , font = "slant")
print(title)

def show():

    for row in game_board :
        for cell in row :
            if cell == "X": 
                print(colorama.Fore.RED + cell,colorama.Fore.RESET , end="" ) 
            elif cell == "O": 
                print(colorama.Fore.BLUE + cell,colorama.Fore.RESET, end="" ) 
            else :
                print(cell , end = " ")
        print( )

def check_game():
    draw=0 

    for i in range (3): 
        r1 = 0 ; c1 = 0 ; d1 = 0 ; r2 = 0 ; c2 = 0 ; d2 = 0 
        for j in range (3): 
            if game_board[i][j] =="X": 
                r1 += 1  
            elif game_board[i][j]=="O": 
                r2 += 1 
            if game_board[j][i]=="X": 
                c1 += 1 
            elif game_board[j][i]=="O": 
                c2 += 1 
            if game_board[j][j]=="X": 
                d1 += 1 
            elif game_board[j][j]=="O": 
                d2 += 1 
            if r1==3 or c1==3 or d1==3 or (game_board[0][2]=="X" and game_board[1][1]=="X" and game_board[2][0]=="X"): 
                if choice==1: 
                    print("----- You win -----") 
                else: 
                    print (" --- Palyer 1 win --- ") 
                return("end") 
            if r2==3 or c2==3 or d2==3 or (game_board[0][2]=="O" and game_board[1][1]=="O" and game_board[2][0]=="O"): 
                if choice==1: 
                    print (" --- Computer win --- ") 
                else: 
                    print (" --- Palyer 2 win --- ") 
                return("end") 
            if game_board[i][j] != "_": 
                draw += 1 
                if draw == 9: 
                    print(" ----- EQUAL ----- ") 
                    return("end") 
  
def player(p,row,col): 
  
    if 0<= row <= 2 and 0 <= col <= 2: 
        if game_board [row][col]=="_": 
            if p==1: 
                return ("X") 
            if p==2: 
                return("O") 
        else: 
            print("It's not possible :/ ") 
    else: 
        print("choose correctly :| ") 
  

game_board = [["_","_","_"],
              ["_","_","_"],
              ["_","_","_"]]

choice=int(input("Choose 1 or 2 ---> play with 1 = computer or 2 = other player : ")) 
show()

while True :
    start=time.time() 
    print("Player 1 : ")

    while True :    

        row = int(input("row : "))
        col = int(input("col : "))

        if 0 <= row <= 2 and 0 <= col <= 2 :
            if game_board[row][col] == "_" :
                game_board[row][col] = "X"
                break 

    show()
    if check_game()=="end" :
        break


    if choice==2: 
        print("Player 2 : " ) 

        while True: 

            row =int(input("row : ")) 
            col= int (input("col : ")) 

            if 0 <= row <= 2 and 0 <= col <= 2 :
                if game_board[row][col] == "_" :
                    game_board[row][col] = "O"
                    break
  
        show() 
        if check_game()=="end": 
            break 
  
    elif choice ==1: 
        print("Computer : ") 
        while True: 
            row = random.randint(0,2) 
            col=random.randint(0,2) 

            if 0 <= row <= 2 and 0 <= col <= 2 :
                if game_board[row][col] == "_" :
                    game_board[row][col] = "O"
                    break


        show() 
        if check_game()=="end": 
            break 

print("Time of your game : ",str(time.time()-start), "second")