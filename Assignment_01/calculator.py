import math

print ("Basic calculator : - , + , * , / ")
print ("advanced calculator : sqrt , fact , sin , cos , tan , cot ")

op = input("Enter a operation PLZ : ")

if op == ("+" or op == "-" or op == "*" or op == "/"):
    a = float(input("enter first number : "))
    b = float(input("enter second number : "))

elif op == ("fact" or "sqrt") :
    a = float(input("enter a number bigger than zero : "))

elif op == ("sin" or "cos" or "tan" or "cot") :
    a = float(input("enter the degrees number : "))

else :
    print("SORRY , Your operation is not correct !!!")

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

elif op == "fact":
    result = math.factorial(a)

elif op == "sqrt":
    result = math.sqrt(a)

elif op == "sin":
    result = math.sin(a*math.pi/180)

elif op == "cos":
    result = math.cos(math.radians(a))

elif op == "tan":
    result = math.tan(a*math.pi/180)

elif op == "cot":
    result = math.cot(math.radians(a))

print("result : " ,result)