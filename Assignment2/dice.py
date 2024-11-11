import random

dice = random.randint(1,6)
prize = random.randint(1,6)

while True :
    #print(f"You got : {dice} , & your prize : {prize}")

    if dice in (1,2,3,4,5):
        print (f"Your chance : {dice}") 
        break

    else :
        print(f"You got : {dice}")
        print(f"You have prize , here you are : {prize}")
    break