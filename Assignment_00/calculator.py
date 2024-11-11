import math


# a = float(input("enter first number : "))
# b = float(input("enter second number : "))
op = input("Enter a operation PLZ : ")

if op == "+" or op == "-" or op == "*" or op == "/":
    a = float(input("enter first number : "))
    b = float(input("enter second number : "))
else :
    a = float(input("enter first number : "))

if op == "+":
    result = a + b

elif op == "-":
    result = a - b

elif op == "*":
    result = a * b

elif op == "/":
    if b == 0:
        result = "Cannot divde by zero"
    else :
        result = a / b

elif

elif op == "sin":
    result = math.sin(a)

elif op == "log":
    result = math.log(a)


print(result)
