def Pascal(row) :

    for i in range(1 , row+1) :
        culomn = 1
        for j in range (1 , i+1) :
            print(culomn , end="")
            culomn = culomn * (i-j) // j
        print()

row = int(input("Enter the row_size : "))
Pascal(row)
