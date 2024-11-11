print("Enter '000' to finish")

list = []

while True :

    numbers = int(input("Enter your number : "))

    if numbers == 000 :
        print("The list that you entered : " , list)
        break
    else :
        list.append(numbers)

list.reverse()

print("Oppsite of your list : " , list)
