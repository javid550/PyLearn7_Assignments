import re

statement = input("Enter a statment : ")

words = re.split(" ",statement)

print(len(words))