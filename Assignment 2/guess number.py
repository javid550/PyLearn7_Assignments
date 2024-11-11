import random

computer_number = random.randint(0,100)

for i in range (10):

    user_number = int(input("Enter a number between 0-100 : "))

    if computer_number == user_number :
        print("---You win---")
        print(f"you try for {i} time")
        break
    elif computer_number > user_number :
        print("give bigger number ⬆⬆⬆ ")

    elif computer_number < user_number :
        print("give smaller number ⬇⬇⬇ ")



