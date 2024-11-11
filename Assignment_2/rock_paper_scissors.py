import random

print("I hope to have good match")

print("-----------------------")
print("---rock---")
print("---paper---")
print("---scissors---")
print("-----------------------")

x = random.randint(1,3)

if x == 1 :
    computer_choice = "rock"
elif x == 2 :
    computer_choice = "paper"
elif x == 3 :
    computer_choice = "scissors"

user_choice = input("what's your choice : ")

print(" computer_choice : ", computer_choice)
print(" user_choice : ", user_choice)

if (computer_choice == user_choice) :
    print("we are Equal")
elif (user_choice == 'rock' and computer_choice == 'scissors' or user_choice == 'scissors' and computer_choice == 'paper' or user_choice == 'paper' and computer_choice == 'rock'):
        print('...you win...')
elif (user_choice == 'scissors' and computer_choice == 'rock' or user_choice == 'paper' and computer_choice == 'scissors' or user_choice == 'rock' and computer_choice == 'paper'):
        print('...you lose...')
else :
        print('your move is wrong!!!')