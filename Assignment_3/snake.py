snake_long = int(input("Enter Snake length : "))

snake = " "

for i in range(snake_long) :
    if i % 2 == 0 :
        snake += '*'

    else :
        snake += '#'

print(snake)