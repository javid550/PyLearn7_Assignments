num = int(input("Enter a number : "))

fact = 1
m = 0

while True :
    m = m + 1
    fact = fact * m
    if fact == num :
        print ("YES")
        break
    elif fact > num :
        print ("NO")
        break
