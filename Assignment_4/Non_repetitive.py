print("Enter '00' if you're finish")

Your_list = []
Computer_list = []

while True :

    numbers = int(input("Enter your number : "))

    if numbers == 00 :
        print(Your_list)
        break
    else :
        Your_list.append(numbers)

    for i in range(len(Your_list)):
        if Your_list[i] not in Computer_list :
            Computer_list.append(Your_list[i])

print(Computer_list)

