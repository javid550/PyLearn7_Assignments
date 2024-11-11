import random

numbers = []
n = int(input("Enter your number : "))

while len(numbers) < n :
    new_number = random.randint(1 , n*10)
    if new_number not in numbers :
        numbers.append(new_number)

print (numbers)
